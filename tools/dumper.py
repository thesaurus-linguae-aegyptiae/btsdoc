#!/usr/bin/env python3
#
# depgraph - Analyze and graph Java project dependencies
# Copyright (C) 2017 Sebastian Götte
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


from depgraph import *
import sqlite3

def sqlite_dump(conn, ns):
    conn.execute('PRAGMA foreign_keys = ON;')
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS metatypes')
    cur.execute('DROP TABLE IF EXISTS types')
    cur.execute('DROP TABLE IF EXISTS extends')
    cur.execute('DROP TABLE IF EXISTS implements')
    cur.execute('DROP TABLE IF EXISTS reference')

    typemap = {}
    cur.execute('CREATE TABLE metatypes (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')
    cur.execute('INSERT INTO metatypes(name) VALUES ("abstract_class")')
    typemap['abstract_class'] = cur.lastrowid
    cur.execute('INSERT INTO metatypes(name) VALUES ("class")')
    typemap['class'] = cur.lastrowid
    cur.execute('INSERT INTO metatypes(name) VALUES ("enum")')
    typemap['enum'] = cur.lastrowid
    cur.execute('INSERT INTO metatypes(name) VALUES ("interface")')
    typemap['interface'] = cur.lastrowid

    cur.execute('CREATE TABLE types (id INTEGER PRIMARY KEY AUTOINCREMENT, fullname TEXT, type INTEGER, FOREIGN KEY(type) REFERENCES metatypes(id))')
    cur.execute('CREATE TABLE extends (id INTEGER PRIMARY KEY AUTOINCREMENT, source INTEGER, target INTEGER, FOREIGN KEY(source) REFERENCES types(id), FOREIGN KEY(target) REFERENCES types(id))')
    cur.execute('CREATE TABLE implements (id INTEGER PRIMARY KEY AUTOINCREMENT, source INTEGER, target INTEGER, FOREIGN KEY(source) REFERENCES types(id), FOREIGN KEY(target) REFERENCES types(id))')
    cur.execute('CREATE TABLE reference (id INTEGER PRIMARY KEY AUTOINCREMENT, source INTEGER, target INTEGER, FOREIGN KEY(source) REFERENCES types(id), FOREIGN KEY(target) REFERENCES types(id))')

    dbtypes = {}
    for t in ns.types.values():
        cur.execute('INSERT INTO types(fullname, type) VALUES (?, ?)', (t.fullpath, typemap[t.javatype]))
        typeid = dbtypes[t] = cur.lastrowid

    for t in ns.types.values():
        if t.parent:
            conn.execute('INSERT INTO extends(source, target) VALUES (?,?)', (dbtypes[t.parent], dbtypes[t])) 
        for impl in t.implements:
            conn.execute('INSERT INTO implements(source, target) VALUES (?,?)', (dbtypes[impl], dbtypes[t])) 
        for ref in t.references:
            conn.execute('INSERT INTO reference(source, target) VALUES (?,?)', (dbtypes[t], dbtypes[ref])) 


def progress(elems, thing):
    nelems = len(elems)
    pdigits = 1 + math.floor(math.log10(nelems))
    for i, elem in enumerate(elems):
        print('  Processing {{}} {{:{}d}}/{{:{}d}} ({{:7.3f}}%): {{}}'.format(pdigits, pdigits).format(thing, i, nelems, 100*i/nelems, elem))
        yield elem

if __name__ == '__main__':
    import argparse
    import sys
    import os
    import math
    parser = argparse.ArgumentParser()
    parser.add_argument('db', type=str, help='SQLite3 database file')
    parser.add_argument('src', nargs='*', type=str, help='Source file(s)')
    parser.add_argument('-s', '--stdin-files', action='store_true', help='Read source files from stdin instead of command line')
    parser.add_argument('-p', '--packages', action='append', type=str, help='Package(s) to analyze')
    parser.add_argument('-q', '--quiet', action='store_true', help='Do not complain about non-critical things')
    args = parser.parse_args()

    if args.stdin_files and args.src:
        print('Error: Can only read files to parse from either command line *or* stdin', file=sys.stderr)
        os.exit(1)

    
    files = sys.stdin.readlines() if args.stdin_files else args.src

    if args.quiet:
        warnings.simplefilter('ignore')

    ns = JavaNamespace(args.packages)

    print('Reading files')
    for fn in progress(files, 'file'):
        ns.load_file(fn)

    print('Resolving types')
    types = ns.types.values()
    for t in progress(types, 'type'):
        t.resolve_types()

    print('Dumping data')
    db = sqlite3.connect(args.db)
    with db as conn:
        sqlite_dump(conn, ns) 
