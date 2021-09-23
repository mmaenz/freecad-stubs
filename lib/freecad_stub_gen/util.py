import re
import textwrap
from pathlib import Path
from xml.etree import ElementTree as ET

from freecad_stub_gen.config import SOURCE_DIR


def indent(block, distance=1, indentSize=4):
    return textwrap.indent(block, ' ' * distance * indentSize)


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


def formatDocstring(docs: str | None) -> str | None:
    if docs and (preparedDocs := prepareDocs(docs)):
        return f'"""{preparedDocs}"""\n'


def getDocFromNode(node: ET.Element) -> str | None:
    if docs := node.find("./Documentation//UserDocu").text:
        return docs


_REG_COMMENT_REM = re.compile(
    r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
    re.DOTALL | re.MULTILINE)


def _replacer(match):
    s = match.group(0)
    if s.startswith('/'):
        return ' '  # note: a space and not an empty string
    else:
        return s


def removeComments(text):
    """Based on https://stackoverflow.com/a/241506"""
    return re.sub(_REG_COMMENT_REM, _replacer, text)


def readContent(file: Path):
    try:
        content = file.read_text()
    except UnicodeDecodeError:
        content = file.read_text('iso8859-1')

    return removeComments(content)


def genPyCppFiles(sourcePath: Path = SOURCE_DIR):
    yield from Path(sourcePath).glob('**/*.cpp')


def genXmlFiles(sourcePath: Path = SOURCE_DIR):
    yield from Path(sourcePath).glob('**/*.xml')