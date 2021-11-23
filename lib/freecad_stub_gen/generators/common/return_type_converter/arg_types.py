from functools import cached_property
from typing import TypeVar, Generator

from freecad_stub_gen.generators.common.names import getModuleName
from freecad_stub_gen.util import OrderedSet, indent

T = TypeVar('T')


class EmptyType:
    @property
    def value(self):
        return self

    def __eq__(self, other):
        return other is None or other == 'object'

    def __hash__(self):
        return 1

    def __str__(self):
        return 'object'


Empty = EmptyType()


class ArgumentsIter:
    @cached_property
    def imports(self):
        return OrderedSet()

    def __iter__(self):
        """
        Cannot inherit this class from Iterable/Iterator
        because super() will not find correct class.
        """
        for argType in super().__iter__():
            match argType:
                case str() if '[' not in argType and (mod := getModuleName(argType)):
                    self.imports.add(mod)
                case UnionArguments() as ua:
                    self.imports.update(ua.imports)
            yield str(argType)


class UnionArguments(ArgumentsIter, OrderedSet):
    def __str__(self):
        values = list(self)
        if 'None' in values:
            values.remove('None')
            values.append('None')

        return ' | '.join(values)


class TupleArgument(ArgumentsIter, list):
    def __init__(self, gen: Generator[T, None, bool | None] = ()):
        super().__init__()
        while True:
            try:
                self.append(next(gen))
            except StopIteration as st:
                self.repeated = len(self) == 1 and bool(st)
                return

    def __str__(self):
        if len(self) == 1 and self.repeated:
            return f'tuple[{self[0]}, ...]'
        elif self:
            return f'tuple[{", ".join(self)}]'
        return 'tuple'


RetType = UnionArguments[str] | EmptyType | str


class InvalidReturnType(ValueError):
    pass


class DictArgument(ArgumentsIter):
    def __init__(self):
        self.keys = UnionArguments()
        self.values = UnionArguments()

    def add(self, key: RetType, value: RetType):
        if isinstance(key, UnionArguments):
            keyStr = str(key)
            self.imports.update(key.imports)
            key = keyStr
        self.keys.add(key)
        self.values.add(value)

    def __bool__(self):
        return bool(self.keys and self.values)

    def __str__(self):
        if not self:
            return 'dict'

        ret = f'dict[{self.keys}, {self.values}]'
        self.imports.update(self.keys.imports)
        self.imports.update(self.values.imports)
        return ret


class ListIter(list, ArgumentsIter):
    pass


class TypedDictGen(dict, ArgumentsIter):
    def __init__(self, funName: str):
        super().__init__()
        self.funName = funName
        self.alternativeSyntax = False

    def add(self, key: str, value: RetType):
        if not key.isidentifier():  # + keyword (not implemented)
            self.alternativeSyntax |= True
        self[key] = value

    def __str__(self):
        typedDictName = f'Return{self.funName[0].upper() + self.funName[1:]}Dict'
        listIter = ListIter(self.values())

        if self.alternativeSyntax:
            content = ', '.join(f"'{k}': {v}" for k, v in zip(self.keys(), listIter))
            fun = f"{typedDictName} = typing.TypedDict('{typedDictName}', {{{content}}})"

        else:
            lines = [f'{k}: {v}' for k, v in zip(self.keys(), listIter)]
            content = indent('\n'.join(lines))
            fun = f"class {typedDictName}(typing.TypedDict):\n{content}"

        self.imports.add('typing')
        self.imports.update(listIter.imports)
        self.imports.add(fun)
        return typedDictName
