import typing

import FreeCAD
import Part


# StepShapePy.xml
class StepShape(FreeCAD.PyObjectBase):
    """StepShape in Import
    This class gives a interface to retrieve TopoShapes out of an loaded STEP file of any kind. 
    		"""

    def __init__(self, arg1: str, /):
        """StepShape in Import
        This class gives a interface to retrieve TopoShapes out of an loaded STEP file of any kind. 
        		"""

    def read(self):
        """method read()
        Read a STEP file into memory and make it accessible
        			  """


# AppImportPy.cpp
def open(arg1: str, arg2: str = None, /):
    """open(string) -- Open the file and create a new document."""


def insert(string: str, string1: str = None, /):
    """insert(string,string) -- Insert the file into the given document."""


def export(list: object, string: str, /):
    """export(list,string) -- Export a list of objects into a single file."""


def readDXF(arg1: str, arg2: str = None, arg3: int = None, arg4: str = None, /):
    """readDXF(filename,[document,ignore_errors]): Imports a DXF file into the given document. ignore_errors is True by default."""


@typing.overload
def writeDXFShape(arg1: list, arg2: str, arg3: int = None, arg4: object = None, arg5: str = None, /): ...


@typing.overload
def writeDXFShape(arg1: Part.TopoShape, arg2: str, arg3: int = None, arg4: object = None, arg5: str = None, /):
    """writeDXFShape([shape],filename [version,usePolyline,optionSource]): Exports Shape(s) to a DXF file."""


@typing.overload
def writeDXFObject(objects: list, filename_: str, version: int = None, usePolyline: object = None, optionSource: str = None, /): ...


@typing.overload
def writeDXFObject(objects: FreeCAD.DocumentObject, filename_: str, version: int = None, usePolyline: object = None, optionSource: str = None, /):
    """writeDXFObject([objects],filename [,version,usePolyline,optionSource]): Exports DocumentObject(s) to a DXF file."""


# AppImportGuiPy.cpp
def open(string):
    """open(string) -- Open the file and create a new document."""


def insert(string: str, string1: str = None, /):
    """insert(string,string) -- Insert the file into the given document."""


def export(list: object, string: str, /):
    """export(list,string) -- Export a list of objects into a single file."""


def ocaf(string: str, /):
    """ocaf(string) -- Browse the ocaf structure."""
