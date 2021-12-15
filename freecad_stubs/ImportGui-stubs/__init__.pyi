import FreeCAD


# AppImportGuiPy.cpp
def ocaf(string: str, /) -> None:
    """
    ocaf(string) -- Browse the ocaf structure.
    Possible exceptions: (Exception, IOError, FreeCAD.FreeCADError, RuntimeError).
    """


def open(name: str, docName: str = None, importHidden=None, merge=None, useLinkGroup=None, mode: int = None) -> 'object' | object | None:
    """
    open(string) -- Open the file and create a new document.
    Possible exceptions: (Exception, IOError, FreeCAD.FreeCADError, RuntimeError).
    """


def insert(name: str, docName: str = None, importHidden=None, merge=None, useLinkGroup=None, mode: int = None) -> 'object' | object | None:
    """
    insert(string,string) -- Insert the file into the given document.
    Possible exceptions: (Exception, IOError, FreeCAD.FreeCADError, RuntimeError).
    """


def export(obj, name: str, exportHidden=None, legacy=None, keepPlacement=None) -> None:
    """
    export(list,string) -- Export a list of objects into a single file.
    Possible exceptions: (Exception, RuntimeError, FreeCAD.FreeCADError).
    """
