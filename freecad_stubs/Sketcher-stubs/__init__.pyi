import typing

import FreeCAD
import Part
import Part as PartModule
import Sketcher

DocAndStr_t: typing.TypeAlias = tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]]
LinkSub_t: typing.TypeAlias = FreeCAD.DocumentObject | None | tuple[()] | DocAndStr_t
LinkList_t: typing.TypeAlias = None | FreeCAD.DocumentObject
SequenceDoc_t: typing.TypeAlias = tuple[FreeCAD.DocumentObject, str | typing.Sequence[str]]
LinkSubList_t: typing.TypeAlias = typing.Sequence[SequenceDoc_t | FreeCAD.DocumentObject]


# ConstraintPy.xml
class Constraint(FreeCAD.Persistence):
    """
    This class can be imported.
    With this object you can handle sketches
    """

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, arg1: str, arg2: int, /): ...

    @typing.overload
    def __init__(self, arg1: str, arg2: int, arg3, /): ...

    @typing.overload
    def __init__(self, arg1: str, arg2: int, arg3: int, arg4, /): ...

    @typing.overload
    def __init__(self, arg1: str, arg2: int, arg3: int, arg4: int, arg5, /): ...

    @typing.overload
    def __init__(self, arg1: str, arg2: int, arg3: int, arg4: int, arg5: int, arg6, /): ...

    @typing.overload
    def __init__(self, arg1: str, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7, /):
        """
        With this object you can handle sketches
        Possible exceptions: (TypeError).
        """

    @property
    def Driving(self) -> bool:
        """Driving Constraint"""

    @property
    def First(self) -> int:
        """First geometry index the Constraint refers to"""

    @First.setter
    def First(self, value: int): ...

    @property
    def FirstPos(self) -> int:
        """Position of first geometry index the Constraint refers to"""

    @property
    def InVirtualSpace(self) -> bool:
        """Constraint in virtual space"""

    @property
    def Name(self) -> str:
        """Name of the constraint"""

    @Name.setter
    def Name(self, value: str): ...

    @property
    def Second(self) -> int:
        """Second geometry index the Constraint refers to"""

    @Second.setter
    def Second(self, value: int): ...

    @property
    def SecondPos(self) -> int:
        """Position of second geometry index the Constraint refers to"""

    @property
    def Third(self) -> int:
        """Third geometry index the Constraint refers to"""

    @Third.setter
    def Third(self, value: int): ...

    @property
    def ThirdPos(self) -> int:
        """Position of third geometry index the Constraint refers to"""

    @property
    def Type(self) -> str:
        """Get the constraint type"""

    @property
    def Value(self) -> float:
        """Value of the Constraint"""


# SketchObjectSFPy.xml
class SketchObjectSF(PartModule.Part2DObject):
    """With this objects you can handle sketches"""

    @property
    def SketchFlatFile(self):
        """SketchFlat file (*.skf) which defines this sketch."""

    @SketchFlatFile.setter
    def SketchFlatFile(self, value): ...


# SketchObjectPy.xml
class SketchObject(PartModule.Part2DObject):
    """With this objects you can handle sketches"""

    @property
    def AxisCount(self) -> int:
        """Return the number of construction lines in the sketch which can be used as axes"""

    @property
    def ConstraintCount(self) -> int:
        """Number of Constraints in this sketch"""

    @property
    def GeometryCount(self) -> int:
        """Number of geometric objects in this sketch"""

    @property
    def Constraints(self) -> list[Sketcher.Constraint]:
        """
        Property group: Sketch.
        Property TypeId: Sketcher::PropertyConstraintList.
        Sketch constraints.
        """

    @Constraints.setter
    def Constraints(self, value: typing.Iterable[Sketcher.Constraint] | dict[int, Sketcher.Constraint]): ...

    @property
    def ExternalGeometry(self) -> list[tuple[FreeCAD.DocumentObject, list[str]]]:
        """
        Property group: Sketch.
        Property TypeId: App::PropertyLinkSubList.
        Sketch external geometry.
        """

    @ExternalGeometry.setter
    def ExternalGeometry(self, value: LinkSub_t | LinkList_t | LinkSubList_t): ...

    @property
    def Geometry(self) -> list[Part.Geometry]:
        """
        Property group: Sketch.
        Property TypeId: Part::PropertyGeometryList.
        Sketch geometry.
        """

    @Geometry.setter
    def Geometry(self, value: typing.Iterable[Part.Geometry] | dict[int, Part.Geometry]): ...

    def DeleteUnusedInternalGeometry(self, arg1: int, /):
        """
        Deprecated -- use deleteUnusedInternalGeometry
        Possible exceptions: (ValueError).
        """

    def ExposeInternalGeometry(self, arg1: int, /):
        """
        Deprecated -- use exposeInternalGeometry
        Possible exceptions: (ValueError).
        """

    def addConstraint(self, arg1, /) -> int | tuple[int, ...]:
        """
        add a constraint to the sketch
        Possible exceptions: (TypeError, IndexError).
        """

    def addCopy(self, arg1, arg2: FreeCAD.Vector, arg3: bool = None, /) -> tuple[int, ...]:
        """
        add a copy of geometric objects to the sketch displaced by a vector3d
        Possible exceptions: (TypeError).
        """

    def addExternal(self, arg1: str, arg2: str, /):
        """
        add a link to an external geometry to use it in a constraint
        Possible exceptions: (ValueError).
        """

    @typing.overload
    def addGeometry(self, arg1, arg2: bool, /) -> int | tuple[int, ...]: ...

    @typing.overload
    def addGeometry(self, arg1, /) -> int | tuple[int, ...]:
        """
        add a geometric object to the sketch
        Possible exceptions: (TypeError).
        """

    def addRectangularArray(self, arg1, arg2: FreeCAD.Vector, arg3: bool, arg4: int, arg5: int, arg6: bool = None, arg7: float = None, /):
        """
        add an array of size cols by rows where each element is a copy of the selected geometric objects displaced by a vector3d in the cols direction and by a vector perpendicular to it in the rows direction
        Possible exceptions: (TypeError).
        """

    def addSymmetric(self, arg1, arg2: int, arg3: int = None, /) -> tuple[int, ...]:
        """
        add a symmetric geometric objects to the sketch with respect to a reference point or line
        Possible exceptions: (TypeError).
        """

    def calculateAngleViaPoint(self, GeoId1: int, GeoId2: int, px: float, py: float, /) -> float:
        """
        calculateAngleViaPoint(GeoId1, GeoId2, px, py) - calculates angle between
                  curves identified by GeoId1 and GeoId2 at point (x,y). The point must be
                  on intersection of the curves, otherwise the result may be useless (except
                  line-to-line, where (0,0) is OK). Returned value is in radians.
        
        Possible exceptions: (ValueError).
        """

    def calculateConstraintError(self, index: int, /) -> float:
        """
        calculateConstraintError(index) - calculates the error function of the
                  constraint identified by its index and returns the signed error value.
                  The error value roughly corresponds to by how much the constraint is
                  violated. If the constraint internally has more than one error function,
                  the returned value is RMS of all errors (sign is lost in this case).
        
        Possible exceptions: (ValueError).
        """

    def carbonCopy(self, arg1: str, arg2: bool = None, /):
        """
        copy another sketch's geometry and constraints
        Possible exceptions: (ValueError).
        """

    def changeConstraintsLocking(self, bLock: int, /) -> int:
        """
        changeConstraintsLocking(bLock) - locks or unlocks all tangent and
                  perpendicular constraints. (Constraint locking prevents it from
                  flipping to another valid configuration, when e.g. external geometry
                  is updated from outside.) The sketch solve is not triggered by the
                  function, but the SketchObject is touched (a recompute will be
                  necessary). The geometry should not be affected by the function.

                  The bLock argument specifies, what to do. If true, all constraints
                  are unlocked and locked again. If false, all tangent and perp.
                  constraints are unlocked.
        """

    def convertToNURBS(self, arg1: int, /):
        """
        Approximates the given geometry with a B-Spline
        Possible exceptions: (ValueError).
        """

    def delConstraint(self, arg1: int, /):
        """
        delete a constraint from the sketch
        Possible exceptions: (ValueError).
        """

    def delConstraintOnPoint(self, arg1: int, arg2: int = None, /):
        """
        delete coincident constraints associated with a sketch point
        Possible exceptions: (ValueError).
        """

    def delExternal(self, arg1: int, /):
        """
        delete a external geometry link from the sketch
        Possible exceptions: (ValueError).
        """

    def delGeometry(self, arg1: int, /):
        """
        delete a geometric object from the sketch
        Possible exceptions: (ValueError).
        """

    def deleteAllGeometry(self):
        """
        delete all the geometry objects and constraints from the sketch except external geometry
        Possible exceptions: (ValueError).
        """

    def deleteUnusedInternalGeometry(self, arg1: int, /):
        """
        Deletes all unused (not further constrained) internal geometry
        Possible exceptions: (ValueError).
        """

    def exposeInternalGeometry(self, arg1: int, /):
        """
        Exposes all internal geometry of an object supporting internal geometry
        Possible exceptions: (ValueError).
        """

    def extend(self, arg1: int, arg2: float, arg3: int, /):
        """
        extend a curve to new start and end positions
        Possible exceptions: (ValueError, TypeError).
        """

    @typing.overload
    def fillet(self, arg1: int, arg2: int, arg3: FreeCAD.Vector, arg4: FreeCAD.Vector, arg5: float, arg6: int = None, /): ...

    @typing.overload
    def fillet(self, arg1: int, arg2: int, arg3: float, arg4: int = None, /):
        """
        create fillet between two edges or at a point
        Possible exceptions: (ValueError, TypeError).
        """

    def getAxis(self, arg1: int, /) -> FreeCAD.Axis:
        """return an axis based on the corresponding construction line"""

    @typing.overload
    def getDatum(self, arg1: int, /) -> FreeCAD.Quantity: ...

    @typing.overload
    def getDatum(self, arg1: str, /) -> FreeCAD.Quantity:
        """
        Get the value of a datum constraint
        Possible exceptions: (IndexError, NameError, TypeError).
        """

    def getDriving(self, arg1: int, /) -> bool:
        """
        Get the Driving status of a datum constraint
        Possible exceptions: (ValueError).
        """

    def getPoint(self, GeoIndex: int, PointPos: int, /) -> FreeCAD.Vector:
        """
        getPoint(GeoIndex,PointPos) - retrieve the vector of a point in the sketch
        
        Possible exceptions: (ValueError).
        """

    def getVirtualSpace(self, arg1: int, /) -> bool:
        """
        Get the VirtualSpace status of a constraint
        Possible exceptions: (ValueError).
        """

    def increaseBSplineDegree(self, arg1: int, arg2: int = None, /):
        """
        Increases the given BSpline Degree by a number of degrees
        Possible exceptions: (ValueError).
        """

    def isPointOnCurve(self, arg1: int, arg2: float, arg3: float, /) -> bool:
        """
        isPointOnObject(GeoIdCurve, float x, float y) - tests if the point (x,y)
                  geometrically lies on a curve (e.g. ellipse). It treats lines as infinite,
                  arcs as full circles/ellipses/etc. Returns boolean value.
        
        Possible exceptions: (ValueError).
        """

    def modifyBSplineKnotMultiplicity(self, arg1: int, arg2: int, arg3: int = None, /):
        """
        Increases or reduces the given BSpline knot multiplicity
        Possible exceptions: (ValueError).
        """

    def movePoint(self, GeoIndex: int, PointPos: int, Vector: FreeCAD.Vector, relative: int = None, /):
        """
        movePoint(GeoIndex,PointPos,Vector,[relative]) - move a given point (or curve)
                  to another location.
                  It moves the specified point (or curve) to the given location by adding some
                  temporary weak constraints and solve the sketch.
                  This method is mostly used to allow the user to drag some portions of the sketch
                  in real time by e.g. the mouse and it works only for underconstrained portions of
                  the sketch.
                  The argument 'relative', if present, states if the new location is given
                  relatively to the current one.
        
        Possible exceptions: (ValueError).
        """

    def renameConstraint(self, arg1: int, arg2: str, /):
        """
        Rename a constraint of the sketch
        Possible exceptions: (IndexError, ValueError).
        """

    def setConstruction(self, arg1: int, arg2: bool, /):
        """
        set construction mode of a geometry on or off
        Possible exceptions: (ValueError).
        """

    @typing.overload
    def setDatum(self, arg1: int, arg2: FreeCAD.Quantity, /): ...

    @typing.overload
    def setDatum(self, arg1: int, arg2: float, /): ...

    @typing.overload
    def setDatum(self, arg1: str, arg2: FreeCAD.Quantity, /): ...

    @typing.overload
    def setDatum(self, arg1: str, arg2: float, /):
        """
        set the Datum of a Distance or Angle constraint
        Possible exceptions: (ValueError, TypeError).
        """

    def setDriving(self, arg1: int, arg2: bool, /):
        """
        set the Driving status of a datum constraint
        Possible exceptions: (ValueError).
        """

    def setVirtualSpace(self, arg1: int, arg2: bool, /):
        """
        set the VirtualSpace status of a constraint
        Possible exceptions: (ValueError).
        """

    def solve(self) -> int:
        """solve the actual set of geometry and constraints"""

    def toggleConstruction(self, arg1: int, /):
        """
        switch a geometry to a construction line
        Possible exceptions: (ValueError).
        """

    def toggleDriving(self, arg1: int, /):
        """
        toggle the Driving status of a datum constraint
        Possible exceptions: (ValueError).
        """

    def toggleVirtualSpace(self, arg1: int, /):
        """
        toggle the VirtualSpace status of a constraint
        Possible exceptions: (ValueError).
        """

    def trim(self, arg1: int, arg2: FreeCAD.Vector, /):
        """
        trim a curve with a given id at a given reference point
        Possible exceptions: (ValueError).
        """


# SketchPy.xml
class Sketch(FreeCAD.Persistence):
    """
    This class can be imported.
    With this objects you can handle constraint sketches
    """

    @property
    def Conflicts(self) -> tuple[int, ...]:
        """Tuple of conflicting constraints"""

    @property
    def Constraint(self) -> int:
        """0: exactly constraint, -1 under-constraint, 1 over-constraint"""

    @property
    def Geometries(self) -> tuple:
        """Tuple of all geometric elements in this sketch"""

    @property
    def Redundancies(self) -> tuple[int, ...]:
        """Tuple of redundant constraints"""

    @property
    def Shape(self) -> PartModule.Shape:
        """Resulting shape from the sketch geometry"""

    def addConstraint(self, arg1, /) -> tuple[int, ...] | int:
        """
        add an constraint object to the sketch
        Possible exceptions: (TypeError).
        """

    def addGeometry(self, arg1, /) -> int | tuple[int, ...]:
        """
        add a geometric object to the sketch
        Possible exceptions: (TypeError).
        """

    def clear(self):
        """clear the sketch"""

    def movePoint(self, GeoIndex: int, PointPos: int, Vector: FreeCAD.Vector, relative: int = None, /) -> int:
        """
        movePoint(GeoIndex,PointPos,Vector,[relative]) - move a given point (or curve)
                  to another location.
                  It moves the specified point (or curve) to the given location by adding some
                  temporary weak constraints and solve the sketch.
                  This method is mostly used to allow the user to drag some portions of the sketch
                  in real time by e.g. the mouse and it works only for underconstrained portions of
                  the sketch.
                  The argument 'relative', if present, states if the new location is given
                  relatively to the current one.
        """

    def solve(self) -> int:
        """solve the actual set of geometry and constraints"""


# AppSketcherPy.cpp
def open(arg1: str, /): ...


def insert(arg1: str, arg2: str, /) -> None: ...
