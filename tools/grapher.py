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

import sqlite3
import textwrap
import hashlib
import colorsys
from collections import Counter

_GRAPH_TEMPLATE = '''
digraph G {{
    graph [sep=0.5, ranksep=2];
    node [colorscheme="pastel18"];
    rankdir="LR";

    subgraph {cluster}interface_like {{
        style=invis;
        subgraph interface {{
            /*node [
                style=filled,
                fillcolor=1
            ];*/
{interfaces}
        }}
    }}

    subgraph {cluster}class_like {{
        style=invis;
        subgraph class {{
            node [
                shape=box,
                /*style=filled,
                fillcolor=2*/
            ];
{classes}
        }}

        subgraph abstract_class {{
            node [
                shape=box,
                style=bold
                /*style="bold,filled",
                fillcolor=3*/
            ];
{abstract_classes}
        }}

        subgraph enum {{
            node [
                style=dotted
                /*style="dotted,filled",
                fillcolor=4*/
            ];
{enums}
        }}
    }}

    subgraph extends {{
        edge [weight=2.0];
{extends}
    }}
    
    subgraph interface_extends {{
        edge [len=1.0, weight=5.0, dir=back];
{iextends}
    }}

    subgraph implements {{
        edge [len=1.0, weight=5.0, dir=back];
{implements}
    }}

    subgraph references {{
        edge [color=gray, weight=0];
/* {references} */
    }}
}}
'''

def makecolor(s):
    val = hashlib.sha256(s.encode()).digest()[-2]/255
    r,g,b = colorsys.hsv_to_rgb(val, 0.7, 0.8)
    return '#{:02x}{:02x}{:02x}'.format(int(r*256), int(g*256), int(b*256))

def db_to_dot(conn, prettify=lambda s: s, include_pkgs={}, exclude_pkgs={}, exclude_simple_hierarchies=True, cluster=False, interfaces_only=False, classes_only=False):
    cur = conn.cursor()
    escape = lambda s: '"{}"'.format(prettify(s))
    
    fetch_type = lambda t: { e for e, in cur.execute('SELECT types.fullname FROM types INNER JOIN metatypes ON types.type = metatypes.id WHERE metatypes.name = ?', (t,)) }
    fetch_relation = lambda table: set(cur.execute('SELECT srctype.fullname, tgttype.fullname FROM {0} INNER JOIN types AS srctype ON {0}.source = srctype.id INNER JOIN types AS tgttype ON {0}.target = tgttype.id'.format(table)))

    interfaces = fetch_type('interface')
    classes = fetch_type('class')
    abstract_classes = fetch_type('abstract_class')
    enums = fetch_type('enum')

    extends = fetch_relation('extends')
    implements = fetch_relation('implements')
    iextends = { (a, b) for a, b in implements if a in interfaces and b in interfaces }
    implements -= iextends
    references = fetch_relation('reference')

    all_types = interfaces | classes | abstract_classes | enums
    inheritance = extends | implements
    inheritance_any = Counter( e for edge in inheritance for e in edge )

    exclude_types = set()

    if include_pkgs:
        exclude_types |= { t for t in all_types if not any(t.startswith(pkg) for pkg in include_pkgs) }

    if exclude_pkgs:
        exclude_types |= { t for t in all_types if any(t.startswith(pkg) for pkg in exclude_pkgs) }

    if exclude_simple_hierarchies:
        exclude_types |= { t for t in all_types if inheritance_any[t] == 0 } # exclude single nodes or two-subgraphs

    format_type = lambda elems: textwrap.indent('\n'.join( '{} [color="{}"];'.format(escape(e), makecolor(e)) for e in elems-exclude_types ), ' '*8)
    format_relation = lambda elems, left_color=True: textwrap.indent('\n'.join( '{} -> {} [color="{}"];'.format(escape(a), escape(b), makecolor(a if left_color else b)) for a, b in elems if not (a in exclude_types or b in exclude_types) ), ' '*8)

    # This is to make interfaces stack to the right of regular classes
    reverse_relation = lambda rel: { (b, a) for (a, b) in rel }

    return _GRAPH_TEMPLATE.format(
            classes=format_type(classes if not interfaces_only else set()),
            interfaces=format_type(interfaces if not classes_only else set()),
            abstract_classes=format_type(abstract_classes if not interfaces_only else set()),
            enums=format_type(enums if not interfaces_only else set()),
            extends=format_relation(extends if not interfaces_only else set(), True),
            implements=format_relation(reverse_relation(implements) if not (interfaces_only or classes_only) else set(), False),
            iextends=format_relation(reverse_relation(iextends) if not classes_only else set(), False),
            references=format_relation(references),
            cluster='cluster_' if cluster else '')

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('db', help='The sqlite3 relationship database file to read')
    parser.add_argument('output', help='The DOT output file to write')
    parser.add_argument('-i', '--include-pkgs', nargs='*', help='Include only these java packages. Can be given multiple times and takes comma-separated package names.')
    parser.add_argument('-e', '--exclude-pkgs', nargs='*', help='Exclude these java packages. Takes precedence over --include-pkgs. Can be given multiple times and takes comma-separated package names.')
    parser.add_argument('-s', '--strip-pkg-prefix', default=None, help='Strip this prefix from all package names and replace it with "*".')
    parser.add_argument('--with-shallow', action='store_true', help='Do not suppress shallow one or two-type connected components in output.')
    parser.add_argument('--cluster', action='store_true', help='Cluster interfaces and classes in output.')
    parser.add_argument('--only-interfaces', action='store_true', help='Only display interfaces in output')
    parser.add_argument('--only-classes', action='store_true', help='Only display classes in output')
    args = parser.parse_args()

    if args.strip_pkg_prefix:
        prettify = lambda s: s.replace(args.strip_pkg_prefix, '*')
    else:
        prettify = lambda s: s

    comma_set_opt = lambda opt: { pkg for pkgs in opt or () for pkg in pkgs.split(',') }

    db = sqlite3.connect(args.db)
    with open(args.output, 'w') as f:
        with db as conn:
            f.write(db_to_dot(conn, prettify, comma_set_opt(args.include_pkgs), comma_set_opt(args.exclude_pkgs), not args.with_shallow, args.cluster, args.only_interfaces, args.only_classes))

