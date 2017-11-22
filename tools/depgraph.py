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

import javalang
from javalang import tree
from collections import defaultdict, namedtuple
import warnings
from warnings import warn
from bs4 import UnicodeDammit

class Imports:
    def __init__(self, precise, wildcards, namespace, filename):
        self._ns, self.precise, self.wildcards, self.filename = namespace, precise, wildcards, filename

    @classmethod
    def for_ast(kls, pkg, ast, *args):
        imports = { imp for _path, imp in ast.filter(tree.Import) }
        precise = { imp.path.rpartition('.')[2]: imp.path for imp in imports if not imp.wildcard or imp.static }
        wildcards = {pkg.name} | { imp.path.rpartition('.')[0] for imp in imports if imp.wildcard }
        return kls(precise, wildcards, *args)

    def resolve_type(self, name):
        if name in self.precise:
            path = self.precise[name]
            if not any(path.startswith(pkg+'.') for pkg in self._ns.include_packages):
                return None
            if path in self._ns.types:
                return self._ns.types[path]
            else:
                warn('Cannot locate type {} in {}'.format(name, self.filename))
                return None

        for path in self.wildcards:
            candidate = '{}.{}'.format(path, name)
            if candidate in self._ns.types:
                return self._ns.types[candidate]
        else:
            warn('Cannot resolve type {} in {}'.format(name, self.filename))
            return None


class JavaClass:
    def __init__(self, package, astnode, imports):
        self.package = package
        self.name = astnode.name
        self.fullpath = '{}.{}'.format(self.package, self.name)
        if isinstance(astnode, javalang.tree.ClassDeclaration):
            self._parent_ref = astnode.extends.name if astnode.extends else None
            self._implements_refs = { impl.name for impl in astnode.implements } if astnode.implements else set()
            self.javatype = 'abstract_class' if 'abstract' in astnode.modifiers else 'class'
        elif isinstance(astnode, javalang.tree.EnumDeclaration):
            self._parent_ref = None
            self._implements_refs = { impl.name for impl in astnode.implements } if astnode.implements else set()
            self.javatype = 'enum'
        else:
            self._parent_ref = None
            self._implements_refs = { impl.name for impl in astnode.extends } if astnode.extends else set()
            self.javatype = 'interface'
        self._refs = { elem.name for _path, elem in astnode.filter(javalang.tree.ReferenceType) }
        self.imports = imports

    def resolve_types(self):
        self.parent = self.imports.resolve_type(self._parent_ref) if self._parent_ref else None
        self.implements = { self.imports.resolve_type(impl) for impl in self._implements_refs } - {None}
        self.references = { self.imports.resolve_type(ref) for ref in self._refs } - {None}

    def __str__(self):
        return self.fullpath


class JavaNamespace:
    def __init__(self, include_packages=set()):
        self.packages = defaultdict(lambda: set())
        self.types = {}
        self.include_packages = set(include_packages)

    def load_file(self, path):
        try:
            with open(path, 'rb') as fb:
                data = UnicodeDammit(fb.read()).unicode_markup
                ast = javalang.parse.parse(data)

            pkg = [ elem for _path, elem in ast.filter(tree.PackageDeclaration) ]
            if not pkg:
                warn('Found no package declaration in {}'.format(path))
                return
            pkg, = pkg
            interesting_elems = [ elem for t in (tree.ClassDeclaration, tree.InterfaceDeclaration, tree.EnumDeclaration) for _path, elem in ast.filter(t) ]
            if not interesting_elems:
                warn('Found no relevant declarations in {}'.format(path))
                return
            cd, *rest_cds = interesting_elems

            jclass = JavaClass(pkg.name, cd, Imports.for_ast(pkg, ast, self, path))
            self.packages[pkg.name] |= {jclass}
            self.types['{}.{}'.format(pkg.name, cd.name)] = jclass
        except Exception as ex:
            raise ValueError('Error parsing file {}'.format(path)) from ex

