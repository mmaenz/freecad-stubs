import keyword
import re
from inspect import Parameter
from itertools import count
from typing import Generator, Iterator
from xml.etree import ElementTree as ET

from freecad_stub_gen.generators.common.cpp_function import findFunctionCall, \
    generateExpressionUntilChar
from freecad_stub_gen.generators.common.names import validatePythonValue
from freecad_stub_gen.generators.common.types_converter import DEFAULT_ARG_NAME, RawRepr


def generateArgSuitFromDocstring(name: str, docString: str, argNumStart: int = 0):
    for match in re.finditer(fr'{name}\((.*?)\):?', docString):
        funCall = findFunctionCall(docString, match.start(), bracketL='(', bracketR=')')
        funCall = funCall.removeprefix(name).removeprefix('(').removesuffix(')')
        yield list(_parameterSuiteGen(funCall, argNumStart))


def _parameterSuiteGen(funDocString: str, argNumStart: int) -> Iterator[Parameter]:
    uniqueNameGen = _uniqueArgNameGen(argNumStart)
    next(uniqueNameGen)

    for argText in generateExpressionUntilChar(funDocString, 0, ','):
        argText = argText.strip()
        paramType = Parameter.POSITIONAL_ONLY

        if argText == '':
            return
        elif argText[-2:] == '[]':
            pass
        else:
            # TODO parse type?

            if argText.startswith('[') and argText.endswith(']'):
                paramType = Parameter.POSITIONAL_OR_KEYWORD
            argText = argText.removeprefix('[').removesuffix(']')

        if '=' in argText:
            argName, defValue = argText.split('=')
            argName, defValue = argName.strip(), defValue.strip()
            defValue = validatePythonValue(defValue)
        elif argText == '...':
            yield Parameter('args', Parameter.VAR_POSITIONAL)
            continue

        else:
            argName, defValue = argText, Parameter.empty

        uniqueName, argNum = uniqueNameGen.send(argName)
        yield Parameter(uniqueName, paramType, default=RawRepr(defValue))


REG_ALL_EXCEPT_WORLD = re.compile(r'\W+')
REG_START_WITH_LETTER = re.compile(r'[a-zA-Z].*')


def _uniqueArgNameGen(argNumStart: int = 1) -> Generator[tuple[str, int], str, None]:
    name: str = yield
    seen = set()

    for argNum in count(argNumStart):
        name = re.sub(REG_ALL_EXCEPT_WORLD, '_', name)
        if not re.match(REG_START_WITH_LETTER, name):
            name = f'{DEFAULT_ARG_NAME}{argNum}'
        elif keyword.iskeyword(name):
            name += '_'

        if name in seen:
            name = f'{name}{argNum}'

        seen.add(name)
        name = yield name, argNum


_REG_REMOVE_NEW_LINE = re.compile(r'\\n"\s*"')
_REG_WHITESPACE_WITH_APOSTROPHE = re.compile(r'"\s*"')


def prepareDocs(docs: str) -> str:
    docs = _REG_REMOVE_NEW_LINE.sub('\n', docs)
    docs = _REG_WHITESPACE_WITH_APOSTROPHE.sub('', docs)
    docs = docs.replace('\\n', '\n').replace('\\"', '"')

    docs = docs.strip()
    if docs.count('\n'):
        if not docs.startswith('\n'):
            docs = '\n' + docs
        if not docs.endswith('\n'):
            docs = docs + '\n'

    return docs


def formatDocstring(docs: str):
    if preparedDocs := prepareDocs(docs):
        return f'"""{preparedDocs}"""\n'
    return ''


def getDocFromNode(node: ET.Element) -> str:
    if docs := node.find("./Documentation//UserDocu").text:
        return docs
    return ''