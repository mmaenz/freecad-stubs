from __future__ import annotations

import itertools
import logging
import re
from functools import cached_property
from typing import TYPE_CHECKING, Self, TypeVar, cast, overload

from freecad_stub_gen.generators.common.cpp_function import (
    generateExpressionUntilChar,
    genFuncArgs,
)
from freecad_stub_gen.generators.common.return_type_converter.full import (
    ReturnTypeConverter,
)
from freecad_stub_gen.ordered_set import OrderedStrSet

if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator

R = TypeVar('R')
T = TypeVar('T')
logger = logging.getLogger(__name__)


class BlockItem:
    def __init__(self, raw: str, cppBlock: CppBlock):
        self.raw = raw
        self.cppBlock = cppBlock


class QtSignal(BlockItem):
    def __init__(self, raw: str, cppBlock: CppBlock):
        super().__init__(raw, cppBlock)
        self.sigArgCppTypes = list(genFuncArgs(self.raw))

        self.requiredImports = OrderedStrSet()
        rtc = ReturnTypeConverter(requiredImports=self.requiredImports)
        self.sigArgPythonTypes = [
            rtc.getExpressionType(c, onlyLiteral=True) for c in self.sigArgCppTypes
        ]

        returnTypeAndName = self.raw[: self.raw.find('(')]
        self.name = returnTypeAndName.rsplit(' ', maxsplit=1)[-1]

    def getStrRepr(self, requiredImports: OrderedStrSet):
        """triggered: typing.ClassVar[QtCore.pyqtSignal]."""
        requiredImports.update(self.requiredImports)
        requiredImports.add('typing')
        requiredImports.add('FreeCADTemplates.qt_types as qt')

        protocolNames = []
        for argNum in range(len(self.sigArgPythonTypes) + 1):
            protArgs = ['self']
            protArgs += [
                f'a{i}: {t}' for i, t in enumerate(self.sigArgPythonTypes[:argNum])
            ]
            if len(protArgs) > 1:
                protArgs.append('/')

            on = f'__{self.cppBlock.cppClass.name}_{self.name}_{argNum}'
            protocolNames.append(on)

            requiredImports.add(
                f'class {on}(typing.Protocol):\n'
                f'    def __call__({", ".join(protArgs)}): ...'
            )

        slots = " | ".join(protocolNames)
        return f'{self.name}: qt.Signal[{slots}]'


class ClassVarContainer[T]:
    """Workaround for parametrized class variables.

    See more: https://github.com/python/mypy/issues/5144
    """

    def __init__(self, val):
        self.val = val

    def __get__(self, instance, _owner) -> T:
        return self.val


class LateInit[T]:
    def __init__(self):
        self.name = ''

    def __set_name__(self, _owner, name: str):
        self.name = name

    @overload
    def __get__(self, instance: None, _owner) -> Self: ...

    @overload
    def __get__(self, instance, _owner) -> T: ...

    def __get__(self, instance, _owner):
        if instance is None:
            return self
        try:
            return instance.__dict__[self.name]
        except KeyError as ke:
            msg = f"Value {self.name} is not initialized in {instance}"
            raise ValueError(msg) from ke

    def __set__(self, instance, value: T):
        if self.name in instance.__dict__:
            msg = f"Value {self.name} is already initialized in {instance}"
            raise ValueError(msg)
        instance.__dict__[self.name] = value


BI = TypeVar('BI', bound=BlockItem)


class CppBlock[BI: BlockItem]:
    ITEM_TYPE = ClassVarContainer[type[BI]](BlockItem)

    cppClass = LateInit['CppClass']()

    def __init__(
        self,
        firstMatch: re.Match[str],
        secondMatch: re.Match[str] | None,
        classBody: str,
    ):
        self._firstMatch = firstMatch
        self._secondMatch = secondMatch
        self._classBody = classBody

    def __repr__(self):
        return self._firstMatch.group()

    @cached_property
    def body(self) -> str:
        start = self._firstMatch.end()
        end = None if self._secondMatch is None else self._secondMatch.start()
        return self._classBody[start:end].strip()

    def __iter__(self) -> Iterator[BI]:
        for e in generateExpressionUntilChar(
            self.body, 0, splitChar=';', bracketL='{', bracketR='}'
        ):
            if exp := e.strip():
                yield self.ITEM_TYPE(exp, self)


class QtSignalBlock(CppBlock[QtSignal]):
    ITEM_TYPE = ClassVarContainer(QtSignal)


class QtSlotBlock(CppBlock[BlockItem]):
    pass  # ITEM_TYPE - not implemented


class CppClass:
    def __init__(self, name: str):
        self.name = name
        self._blocks: list[CppBlock] = []

    @property
    def blocks(self) -> Iterable[CppBlock]:
        return tuple(self._blocks)

    def addBlock(self, block: CppBlock):
        self._blocks.append(block)
        block.cppClass = self


REG_BLOCK = re.compile(
    r"""
(
    ((public|protected|private)\s+)?    # optional QT access modifier
    (?P<qt_mod>Q_SLOTS|Q_SIGNALS)       # QT macro
    \s*:                                # must ends on `:`
)|(
    (public|protected|private)          # c++ modifier
    \s*:                                # must ends on `:`
)""",
    re.VERBOSE,
)


def pairwiseLongest[T, R](
    it: Iterable[T], fill: R | None = None
) -> Iterator[tuple[T, T | R]]:
    return itertools.pairwise(itertools.chain(it, [cast('T', fill)]))


def parseClass(className: str, fileContent: str) -> CppClass:
    classBodyReg = re.compile(
        rf"""
class\s+            # keyword `class`
(?:\w+\s+)?         # there may be optional macro: GuiExport|AppExport
{className}\s*      # original class name
[^{{]*              # optional inheritance
{{                  # class body block
    """,
        re.VERBOSE,
    )
    if not (match := re.search(classBodyReg, fileContent)):
        msg = f'Cannot find class {className}'
        raise ValueError(msg)

    classBody = next(
        generateExpressionUntilChar(
            fileContent, match.end(), splitChar='NONE', bracketL='{', bracketR='}'
        )
    )

    cppClass = CppClass(className)

    for first, sec in pairwiseLongest(REG_BLOCK.finditer(classBody)):
        if 'Q_SIGNALS' in first.group():
            blockType: type[CppBlock] = QtSignalBlock
        elif 'Q_SLOT' in first.group():
            blockType = QtSlotBlock
        else:
            blockType = CppBlock

        cppClass.addBlock(blockType(first, sec, classBody))

    return cppClass
