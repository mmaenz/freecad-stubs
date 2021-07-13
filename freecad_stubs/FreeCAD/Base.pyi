import typing

import FreeCAD


# VectorPy.xml
class Vector(FreeCAD.PyObjectBase):
    """This class represents a 3D float vector"""

    @typing.overload
    def __init__(self, arg1: float = None, arg2: float = None, arg3: float = None, /): ...

    @typing.overload
    def __init__(self, arg1: FreeCAD.Vector, /): ...

    @typing.overload
    def __init__(self, arg1: object, /):
        """This class represents a 3D float vector"""

    @property
    def Length(self) -> float:
        """Length([Float]) -> Float
        						  gets or sets the length of this vector
        				"""

    @Length.setter
    def Length(self, value: float): ...

    @property
    def x(self) -> float:
        """x([Float]) -> Float
        						  gets or sets the X component of this vector
        				"""

    @x.setter
    def x(self, value: float): ...

    @property
    def y(self) -> float:
        """y([Float]) -> Float
        						  gets or sets the Y component of this vector
        				"""

    @y.setter
    def y(self, value: float): ...

    @property
    def z(self) -> float:
        """z([Float]) -> Float
        						  gets or sets the Z component of this vector
        				"""

    @z.setter
    def z(self, value: float): ...

    def __reduce__(self):
        """__reduce__()
                              Serialization of Vector objects
                    """

    def add(self, Vector: FreeCAD.Vector, /):
        """add(Vector)
        					      returns the sum of this and another vector
        				"""

    def cross(self, Vector: FreeCAD.Vector, /):
        """cross(Vector)
        					      returns the cross product between this and another vector
        				"""

    def distanceToLine(self, Vector: object, Vector2: object, /):
        """distanceToLine(Vector,Vector)
        						  returns the distance between this vector and a line defined by
        						  a base point and a direction
        				"""

    def distanceToLineSegment(self, Vector: object, Vector2: object, /):
        """distanceToLineSegment(Vector,Vector)
        						  returns the distance between this vector and a line segment defined by
        						  a base point and a direction
        				"""

    def distanceToPlane(self, Vector: object, Vector2: object, /):
        """distanceToPlane(Vector,Vector)
        						  returns the distance between this vector and a plane defined by
        						  a base point and a normal
        				"""

    def distanceToPoint(self, Vector: FreeCAD.Vector, /):
        """
        					distanceToPoint(Vector)
        					returns the distance to another point
        				"""

    def dot(self, Vector: FreeCAD.Vector, /):
        """dot(Vector)
        						  returns the dot product of the this vector with another one
        				"""

    def getAngle(self, Vector: FreeCAD.Vector, /):
        """getAngle(Vector)
        					      returns the angle in radians between this and another vector
        				"""

    def isEqual(self, Vector: FreeCAD.Vector, tolerance: float, /):
        """isEqual(Vector, tolerance) -> Boolean
                                  If the distance to the given point is less or equal to the tolerance
                                  bith points are considered equal.
                        """

    def multiply(self, Float: float, /):
        """multiply(Float)
        					      multiplies (scales) this vector by a single factor
        				"""

    def negative(self):
        """negative()
        					      returns the negative (opposite) of this vector
        				"""

    def normalize(self):
        """normalize()
        						  normalizes the vector to the length of 1.0
        				"""

    def projectToLine(self, Vector_pnt: object, Vector_vec: object, /):
        """projectToLine(Vector pnt,Vector vec)
        						  Projects the point 'pnt' on a line that goes through the origin with the direction vector 'vec'.
        						  The result is the vector from point 'pnt' to the projected point.
        						  NOTE: The result does not depend on the vector instance 'self'.
        						  NOTE: This method modifies the vector instance 'self'.
        				"""

    def projectToPlane(self, Vector: object, Vector2: object, /):
        """projectToPlane(Vector,Vector)
        						  projects the vector on a plane defined by a base point and a normal
        				"""

    def scale(self, Float: float, Float2: float, Float3: float, /):
        """scale(Float,Float,Float)
        					      scales (multiplies) this vector by a factor
        			    """

    def sub(self, Vector: FreeCAD.Vector, /):
        """sub(Vector)
        					      returns the difference of this and another vector
        				"""

    def __eq__(self, other) -> bool: ...

    def __ne__(self, other) -> bool: ...

    def __lt__(self, other) -> bool: ...

    def __le__(self, other) -> bool: ...

    def __ge__(self, other) -> bool: ...

    def __gt__(self, other) -> bool: ...

    def __add__(self, other) -> Vector: ...

    def __sub__(self, other) -> Vector: ...

    def __mul__(self, other) -> Vector: ...

    def __floordiv__(self, other): ...

    def __divmod__(self, other): ...

    def __truediv__(self, other) -> Vector: ...

    def __pow__(self, power, modulo=None): ...

    def __neg__(self) -> Vector: ...

    def __pos__(self) -> Vector: ...

    def __abs__(self) -> Vector: ...

    def __invert__(self): ...

    def __lshift__(self, other): ...

    def __rshift__(self, other): ...

    def __and__(self, other): ...

    def __xor__(self, other): ...

    def __or__(self, other): ...

    def __int__(self): ...

    def __float__(self): ...


# RotationPy.xml
class Rotation(FreeCAD.PyObjectBase):
    """
    				A Rotation using a quaternion.
    				The Rotation object can be created by:
    				-- an empty parameter list
    				-- a Rotation object
    				-- a Vector (axis) and a float (angle)
    				-- two Vectors (rotation from/to vector)
    				-- three floats (Euler angles) as yaw-pitch-roll in XY'Z'' convention
    				-- four floats (Quaternion) where the quaternion is specified as:
    				   q=xi+yj+zk+w, i.e. the last parameter is the real part
    				-- three vectors that define rotated axes directions + an optional
    				   3-characher string of capital letters 'X', 'Y', 'Z' that sets the
    				   order of importance of the axes (e.g., 'ZXY' means z direction is
    				   followed strictly, x is used but corrected if necessary, y is ignored).
    			"""

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, arg1: FreeCAD.Rotation, /): ...

    @typing.overload
    def __init__(self, arg1: FreeCAD.Vector, arg2: float, /): ...

    @typing.overload
    def __init__(self, arg1: FreeCAD.Matrix, /): ...

    @typing.overload
    def __init__(self, arg1: float, arg2: float, arg3: float, arg4: float, /): ...

    @typing.overload
    def __init__(self, arg1: float, arg2: float, arg3: float, /): ...

    @typing.overload
    def __init__(self, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: float, arg16: float, /): ...

    @typing.overload
    def __init__(self, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, /): ...

    @typing.overload
    def __init__(self, arg1: FreeCAD.Vector, arg2: FreeCAD.Vector, /): ...

    @typing.overload
    def __init__(self, arg1: FreeCAD.Vector, arg2: FreeCAD.Vector, arg3: FreeCAD.Vector, arg4: str = None, /):
        """
        				A Rotation using a quaternion.
        				The Rotation object can be created by:
        				-- an empty parameter list
        				-- a Rotation object
        				-- a Vector (axis) and a float (angle)
        				-- two Vectors (rotation from/to vector)
        				-- three floats (Euler angles) as yaw-pitch-roll in XY'Z'' convention
        				-- four floats (Quaternion) where the quaternion is specified as:
        				   q=xi+yj+zk+w, i.e. the last parameter is the real part
        				-- three vectors that define rotated axes directions + an optional
        				   3-characher string of capital letters 'X', 'Y', 'Z' that sets the
        				   order of importance of the axes (e.g., 'ZXY' means z direction is
        				   followed strictly, x is used but corrected if necessary, y is ignored).
        			"""

    @property
    def Angle(self) -> float:
        """The rotation angle of the quaternion"""

    @Angle.setter
    def Angle(self, value: float): ...

    @property
    def Axis(self) -> FreeCAD.Vector:
        """The rotation axis of the quaternion"""

    @Axis.setter
    def Axis(self, value: FreeCAD.Vector): ...

    @property
    def Q(self) -> tuple[float, float, float, float]:
        """The rotation elements (as quaternion)"""

    @Q.setter
    def Q(self, value: tuple[float, float, float, float]): ...

    def invert(self):
        """
                            invert() -> None
                            Sets the rotation to its inverse
        				"""

    def inverted(self):
        """
                            inverted() -> Rotation
                            Returns the inverse of the rotation
                        """

    def isIdentity(self):
        """
                            isIdentity() -> Bool
                            returns True if the rotation equals the unity matrix
                        """

    def isNull(self):
        """
        					isNull() -> Bool
                            returns True if all Q values are zero
        				"""

    def isSame(self, Rotation: FreeCAD.Rotation, /):
        """
                            isSame(Rotation)
                            Checks if the two quaternions perform the same rotation
                        """

    def multVec(self, Vector: FreeCAD.Vector, /):
        """
        					multVec(Vector) -> Vector
        					Compute the transformed vector using the rotation
        				"""

    def multiply(self, Rotation: FreeCAD.Rotation, /):
        """
        					multiply(Rotation)
        					Multiply this quaternion with another quaternion
        				"""

    def toEuler(self):
        """
        					toEuler(Vector) -> list
        					Get the Euler angles of this rotation
        					as yaw-pitch-roll in XY'Z'' convention
        				"""

    def __eq__(self, other) -> bool: ...

    def __ne__(self, other) -> bool: ...

    def __lt__(self, other) -> bool: ...

    def __le__(self, other) -> bool: ...

    def __ge__(self, other) -> bool: ...

    def __gt__(self, other) -> bool: ...


# PersistencePy.xml
class Persistence(FreeCAD.BaseClass):
    """This is a persistence class"""

    @property
    def Content(self) -> str:
        """Content of the object in XML representation"""

    @Content.setter
    def Content(self, value: str): ...

    @property
    def MemSize(self) -> int:
        """Memory size of the object in byte"""


# BoundBoxPy.xml
class BoundBox(FreeCAD.PyObjectBase):
    """Bound box class
    A bounding box is an orthographic cube which is a way to describe outer boundaries.
    You get a bounding box from a lot of 3D types. It is often used to check if a 3D
    entity lies in the range of another object. Checking for boundig interference first
    can save a lot of computing time!

    Constructor:
    App.BoundBox([Xmin,Ymin,Zmin,Xmax,Ymax,Zmax])
    App.BoundBox(Tuple, Tuple)
    App.BoundBox(Vector, Vector)
    App.BoundBox(BoundBox)
    	  """

    @typing.overload
    def __init__(self, Xmin: float, Ymin: float = None, Zmin: float = None, Xmax: float = None, Ymax: float = None, Zmax: float = None, /): ...

    @typing.overload
    def __init__(self, Tuple: tuple, Tuple2: tuple, /): ...

    @typing.overload
    def __init__(self, Tuple: FreeCAD.Vector, Tuple2: FreeCAD.Vector, /): ...

    @typing.overload
    def __init__(self, Vector: tuple, Vector2: tuple, /): ...

    @typing.overload
    def __init__(self, Vector: FreeCAD.Vector, Vector2: FreeCAD.Vector, /): ...

    @typing.overload
    def __init__(self, BoundBox: FreeCAD.BoundBox, /):
        """Bound box class
        A bounding box is an orthographic cube which is a way to describe outer boundaries.
        You get a bounding box from a lot of 3D types. It is often used to check if a 3D
        entity lies in the range of another object. Checking for boundig interference first
        can save a lot of computing time!

        Constructor:
        App.BoundBox([Xmin,Ymin,Zmin,Xmax,Ymax,Zmax])
        App.BoundBox(Tuple, Tuple)
        App.BoundBox(Vector, Vector)
        App.BoundBox(BoundBox)
        	  """

    @property
    def Center(self) -> object:
        """Center point of the bounding box"""

    @property
    def DiagonalLength(self) -> float:
        """Diagonal length of the BoundBox"""

    @property
    def XLength(self) -> float:
        """Length of the BoundBox in x direction"""

    @property
    def XMax(self) -> float:
        """The maximum x boundary position"""

    @XMax.setter
    def XMax(self, value: float): ...

    @property
    def XMin(self) -> float:
        """The minimum x boundary position"""

    @XMin.setter
    def XMin(self, value: float): ...

    @property
    def YLength(self) -> float:
        """Length of the BoundBox in y direction"""

    @property
    def YMax(self) -> float:
        """The maximum y boundary position"""

    @YMax.setter
    def YMax(self, value: float): ...

    @property
    def YMin(self) -> float:
        """The minimum y boundary position"""

    @YMin.setter
    def YMin(self, value: float): ...

    @property
    def ZLength(self) -> float:
        """Length of the BoundBox in z direction"""

    @property
    def ZMax(self) -> float:
        """The maximum z boundary position"""

    @ZMax.setter
    def ZMax(self, value: float): ...

    @property
    def ZMin(self) -> float:
        """The minimum z boundary position"""

    @ZMin.setter
    def ZMin(self, value: float): ...

    @typing.overload
    def add(self, BoundBox: tuple, /): ...

    @typing.overload
    def add(self, BoundBox: FreeCAD.Vector, /): ...

    @typing.overload
    def add(self, BoundBox: FreeCAD.BoundBox, /):
        """method add(BoundBox)
        Add (enlarge) the given BoundBox"""

    @typing.overload
    def closestPoint(self, Vector: tuple, /): ...

    @typing.overload
    def closestPoint(self, Vector: FreeCAD.Vector, /):
        """method closestPoint(Vector)
        Get the closest point of the bounding box to the given point
                """

    def enlarge(self, Float: float, /):
        """method enlarge(Float)
        Enlarge the BoundBox by the given value in each direction.
        A negative value shrinks the box."""

    def getEdge(self, Int: int, /):
        """method getEdge(Int)
        Get the edge points of the given index. The index must be in the range of [0,11]
                """

    def getIntersectionPoint(self, Vector_Base: FreeCAD.Vector, Vector_Dir: FreeCAD.Vector, float_epsilon: float = 0.0001, /):
        """method Vector getIntersectionPoint(Vector Base, Vector Dir, [float epsilon=0.0001])
        Calculate the intersection point of a line with the BoundBox
        The Base point must lie inside the bounding box, if not an
        exception is thrown.
        			  """

    def getPoint(self, Int: int, /):
        """method getPoint(Int)
        Get the point of the given index. The index must be in the range of [0,7]
                """

    def intersect(self, BoundBox_Vector_Base: FreeCAD.Vector, Vector_Dir: FreeCAD.Vector, /):
        """method intersect(BoundBox|Vector Base, Vector Dir)
        Checks if the given object intersects with the BoundBox. That can be:
        - Another BoundBox
        - A line, specified by Base and Dir
        		"""

    def intersected(self, BoundBox: FreeCAD.BoundBox, /):
        """method intersected(BoundBox)
        Returns the intersection of this and the given bounding box.
        		"""

    def isCutPlane(self, Vector_Base: FreeCAD.Vector, Vector_Normal: FreeCAD.Vector, /):
        """method bool isCutPlane(Vector Base, Vector Normal)
        Check if the plane specified by Base and Normal intersects (cuts) the BoundBox"""

    @typing.overload
    def isInside(self, Vector_Base_BoundBox_box: tuple, /): ...

    @typing.overload
    def isInside(self, Vector_Base_BoundBox_box: FreeCAD.Vector, /): ...

    @typing.overload
    def isInside(self, Vector_Base_BoundBox_box: FreeCAD.BoundBox, /):
        """
        					method bool isInside(Vector Base|BoundBox box)
        Check if the point or bounding box is inside this bounding box
        				"""

    def isValid(self):
        """method isValid()
        Checks if the bounding box is valid"""

    @typing.overload
    def move(self, Vector: tuple, /): ...

    @typing.overload
    def move(self, Vector: FreeCAD.Vector, /):
        """ method move(Vector)
        Move the BoundBox by the given vector
        			  """

    def scale(self, x: float, y: float, z: float, /):
        """ method scale(x,y,z)
        Scale the BoundBox by the given values in x, y and z
        			  """

    def setVoid(self):
        """method setVoid()
        Invalidate the bounding box"""

    def transformed(self, Matrix: FreeCAD.Matrix, /):
        """ method transformed(Matrix)
        Return a new bounding box with the transformed corner of this bounding box
        			  """

    def united(self, BoundBox: FreeCAD.BoundBox, /):
        """method united(BoundBox)
        Returns the union of this and the given bounding box.
        		"""


# PlacementPy.xml
class Placement(FreeCAD.PyObjectBase):
    """Placement
    A placement defines an orientation (rotation) and a position (base) in 3D space.
    It is used when no scaling or other distortion is needed.

    The following constructors are supported:
    Placement() -- empty constructor
    Placement(Placement) -- copy constructor
    Placement(Matrix) -- 4D matrix consisting of rotation and translation
    Placement(Base, Rotation) -- define position and rotation
    Placement(Base, Rotation,Center) -- define position and rotation with center
    Placement(Base, Axis, Angle) -- define position and rotation
    		"""

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, Placement: FreeCAD.Matrix, /): ...

    @typing.overload
    def __init__(self, Placement: FreeCAD.Placement, /): ...

    @typing.overload
    def __init__(self, Matrix: FreeCAD.Matrix, /): ...

    @typing.overload
    def __init__(self, Matrix: FreeCAD.Placement, /): ...

    @typing.overload
    def __init__(self, Base: FreeCAD.Vector, Rotation: FreeCAD.Rotation, /): ...

    @typing.overload
    def __init__(self, Base: FreeCAD.Vector, Rotation: FreeCAD.Vector, Center: float, /): ...

    @typing.overload
    def __init__(self, Base: FreeCAD.Vector, Rotation: FreeCAD.Rotation, Center: FreeCAD.Vector, /): ...

    @typing.overload
    def __init__(self, Base: FreeCAD.Vector, Axis: FreeCAD.Vector, Angle: float, /): ...

    @typing.overload
    def __init__(self, Base: FreeCAD.Vector, Axis: FreeCAD.Rotation, Angle: FreeCAD.Vector, /):
        """Placement
        A placement defines an orientation (rotation) and a position (base) in 3D space.
        It is used when no scaling or other distortion is needed.

        The following constructors are supported:
        Placement() -- empty constructor
        Placement(Placement) -- copy constructor
        Placement(Matrix) -- 4D matrix consisting of rotation and translation
        Placement(Base, Rotation) -- define position and rotation
        Placement(Base, Rotation,Center) -- define position and rotation with center
        Placement(Base, Axis, Angle) -- define position and rotation
        		"""

    @property
    def Base(self) -> FreeCAD.Vector:
        """Vector to the Base Position of the Placement"""

    @Base.setter
    def Base(self, value: FreeCAD.Vector): ...

    @property
    def Rotation(self) -> FreeCAD.Rotation:
        """Orientation of the placement expressed as rotation"""

    @Rotation.setter
    def Rotation(self, value: FreeCAD.Rotation): ...

    def copy(self):
        """
                            copy()
                            Returns a copy of this Placement
                        """

    def inverse(self):
        """
        					inverse() -> Placement
        					compute the inverse placement
        				"""

    def isIdentity(self):
        """
                            isIdentity() -> Bool
        					returns True if the placement has no displacement and no rotation
        				"""

    def move(self, Vector: FreeCAD.Vector, /):
        """
        					move(Vector) 
        					Move the placement along the vector
        				"""

    def multVec(self, arg1: FreeCAD.Vector, /):
        """
        					multVector(Vector) -> Vector
        					Compute the transformed vector using the placement
        				"""

    def multiply(self, Placement: FreeCAD.Placement, /):
        """
        					multiply(Placement)
        					Multiply this placement with another placement
        				"""

    def toMatrix(self):
        """
        					toMatrix()
        					convert the placement to a matrix representation
        				"""

    def __eq__(self, other) -> bool: ...

    def __ne__(self, other) -> bool: ...

    def __lt__(self, other) -> bool: ...

    def __le__(self, other) -> bool: ...

    def __ge__(self, other) -> bool: ...

    def __gt__(self, other) -> bool: ...


# UnitPy.xml
class Unit(FreeCAD.PyObjectBase):
    """
     Unit
     defines a unit type, calculate and compare.

     The following constructors are supported:
     Unit()                        -- empty constructor
     Unit(i1,i2,i3,i4,i5,i6,i7,i8) -- unit signature
     Unit(Quantity)                -- copy unit from Quantity
     Unit(Unit)                    -- copy constructor
     Unit(string)                  -- parse the string for units
            """

    @typing.overload
    def __init__(self, i1: int = None, i2: int = None, i3: int = None, i4: int = None, i5: int = None, i6: int = None, i7: int = None, i8: int = None, /): ...

    @typing.overload
    def __init__(self, Quantity: FreeCAD.Quantity, /): ...

    @typing.overload
    def __init__(self, Quantity: FreeCAD.Unit, /): ...

    @typing.overload
    def __init__(self, Quantity: str, /): ...

    @typing.overload
    def __init__(self, Unit: FreeCAD.Quantity, /): ...

    @typing.overload
    def __init__(self, Unit: FreeCAD.Unit, /): ...

    @typing.overload
    def __init__(self, Unit: str, /): ...

    @typing.overload
    def __init__(self, string: FreeCAD.Quantity, /): ...

    @typing.overload
    def __init__(self, string: FreeCAD.Unit, /): ...

    @typing.overload
    def __init__(self, string: str, /):
        """
         Unit
         defines a unit type, calculate and compare.

         The following constructors are supported:
         Unit()                        -- empty constructor
         Unit(i1,i2,i3,i4,i5,i6,i7,i8) -- unit signature
         Unit(Quantity)                -- copy unit from Quantity
         Unit(Unit)                    -- copy constructor
         Unit(string)                  -- parse the string for units
                """

    @property
    def Type(self) -> str:
        """holds the unit type as a string, e.g. 'Area'."""

    def __eq__(self, other) -> bool: ...

    def __ne__(self, other) -> bool: ...

    def __lt__(self, other) -> bool: ...

    def __le__(self, other) -> bool: ...

    def __ge__(self, other) -> bool: ...

    def __gt__(self, other) -> bool: ...

    def __add__(self, other) -> Unit: ...

    def __sub__(self, other) -> Unit: ...

    def __mul__(self, other) -> Unit: ...

    def __floordiv__(self, other): ...

    def __divmod__(self, other): ...

    def __truediv__(self, other) -> Unit: ...

    def __pow__(self, power, modulo=None): ...

    def __neg__(self) -> Unit: ...

    def __pos__(self) -> Unit: ...

    def __abs__(self) -> Unit: ...

    def __invert__(self): ...

    def __lshift__(self, other): ...

    def __rshift__(self, other): ...

    def __and__(self, other): ...

    def __xor__(self, other): ...

    def __or__(self, other): ...

    def __int__(self): ...

    def __float__(self): ...


# QuantityPy.xml
class Quantity(FreeCAD.PyObjectBase):
    """Quantity
    defined by a value and a unit.

    The following constructors are supported:
    Quantity() -- empty constructor
    Quantity(Value) -- empty constructor
    Quantity(Value,Unit) -- empty constructor
    Quantity(Quantity) -- copy constructor
    Quantity(string) -- arbitrary mixture of numbers and chars defining a Quantity
    		"""

    @typing.overload
    def __init__(self, Value: FreeCAD.Quantity, /): ...

    @typing.overload
    def __init__(self, Value: str, /): ...

    @typing.overload
    def __init__(self, Value: float, Unit: FreeCAD.Unit, /): ...

    @typing.overload
    def __init__(self, Value: float, Unit: FreeCAD.Quantity, /): ...

    @typing.overload
    def __init__(self, Quantity: FreeCAD.Quantity, /): ...

    @typing.overload
    def __init__(self, Quantity: str, /): ...

    @typing.overload
    def __init__(self, string: FreeCAD.Quantity, /): ...

    @typing.overload
    def __init__(self, string: str, /):
        """Quantity
        defined by a value and a unit.

        The following constructors are supported:
        Quantity() -- empty constructor
        Quantity(Value) -- empty constructor
        Quantity(Value,Unit) -- empty constructor
        Quantity(Quantity) -- copy constructor
        Quantity(string) -- arbitrary mixture of numbers and chars defining a Quantity
        		"""

    @property
    def Format(self) -> tuple:
        """Format of the Quantity"""

    @Format.setter
    def Format(self, value: tuple): ...

    @property
    def Unit(self) -> object:
        """Unit of the Quantity"""

    @Unit.setter
    def Unit(self, value: object): ...

    @property
    def UserString(self) -> str:
        """Unit of the Quantity"""

    @property
    def Value(self) -> float:
        """Numeric Value of the Quantity (in internal system mm,kg,s)"""

    @Value.setter
    def Value(self, value: float): ...

    @typing.overload
    def getValueAs(self, arg: FreeCAD.Quantity, /): ...

    @typing.overload
    def getValueAs(self, arg: FreeCAD.Unit, /): ...

    @typing.overload
    def getValueAs(self, arg: str, /): ...

    @typing.overload
    def getValueAs(self, arg: float, arg2: FreeCAD.Unit, /): ...

    @typing.overload
    def getValueAs(self, FreeCAD_Units_Pascal: FreeCAD.Quantity, /): ...

    @typing.overload
    def getValueAs(self, FreeCAD_Units_Pascal: FreeCAD.Unit, /): ...

    @typing.overload
    def getValueAs(self, FreeCAD_Units_Pascal: str, /): ...

    @typing.overload
    def getValueAs(self, Qantity_N_m_2_: FreeCAD.Quantity, /): ...

    @typing.overload
    def getValueAs(self, Qantity_N_m_2_: FreeCAD.Unit, /): ...

    @typing.overload
    def getValueAs(self, Qantity_N_m_2_: str, /): ...

    @typing.overload
    def getValueAs(self, Unit_0_1_0_0_0_0_0_0_: FreeCAD.Quantity, /): ...

    @typing.overload
    def getValueAs(self, Unit_0_1_0_0_0_0_0_0_: FreeCAD.Unit, /): ...

    @typing.overload
    def getValueAs(self, Unit_0_1_0_0_0_0_0_0_: str, /):
        """
                  returns a floating point value as the provided unit

                  Following parameters are allowed:
                  getValueAs('m/s')  # unit string to parse
                  getValueAs(2.45,1) # translatrion value and unit signature
                  getValueAs(FreeCAD.Units.Pascal) # predefined standard units 
                  getValueAs(Qantity('N/m^2')) # a quantity
                  getValueAs(Unit(0,1,0,0,0,0,0,0)) # a unit
                """

    def __eq__(self, other) -> bool: ...

    def __ne__(self, other) -> bool: ...

    def __lt__(self, other) -> bool: ...

    def __le__(self, other) -> bool: ...

    def __ge__(self, other) -> bool: ...

    def __gt__(self, other) -> bool: ...

    def __add__(self, other) -> Quantity: ...

    def __sub__(self, other) -> Quantity: ...

    def __mul__(self, other) -> Quantity: ...

    def __floordiv__(self, other): ...

    def __divmod__(self, other): ...

    def __truediv__(self, other) -> Quantity: ...

    def __pow__(self, power, modulo=None): ...

    def __neg__(self) -> Quantity: ...

    def __pos__(self) -> Quantity: ...

    def __abs__(self) -> Quantity: ...

    def __invert__(self): ...

    def __lshift__(self, other): ...

    def __rshift__(self, other): ...

    def __and__(self, other): ...

    def __xor__(self, other): ...

    def __or__(self, other): ...

    def __int__(self): ...

    def __float__(self): ...


# BaseClassPy.xml
class BaseClass(FreeCAD.PyObjectBase):
    """This is the base class"""

    @property
    def Module(self) -> str:
        """Module in which this class is defined"""

    @property
    def TypeId(self) -> str:
        """Is the type of the FreeCAD object with module domain"""

    def getAllDerivedFrom(self):
        """Returns all descentences"""

    def isDerivedFrom(self, arg1: str, /):
        """Returns true if given type is a father"""


# MatrixPy.xml
class Matrix(FreeCAD.PyObjectBase):
    """A 4x4 Matrix"""

    @typing.overload
    def __init__(self, arg1: float = None, arg2: float = None, arg3: float = None, arg4: float = None, arg5: float = None, arg6: float = None, arg7: float = None, arg8: float = None, arg9: float = None, arg10: float = None, arg11: float = None, arg12: float = None, arg13: float = None, arg14: float = None, arg15: float = None, arg16: float = None, /): ...

    @typing.overload
    def __init__(self, arg1: FreeCAD.Matrix, /):
        """A 4x4 Matrix"""

    @property
    def A(self) -> typing.Sequence:
        """The matrix elements"""

    @A.setter
    def A(self, value: typing.Sequence): ...

    @property
    def A11(self) -> float:
        """The matrix elements"""

    @A11.setter
    def A11(self, value: float): ...

    @property
    def A12(self) -> float:
        """The matrix elements"""

    @A12.setter
    def A12(self, value: float): ...

    @property
    def A13(self) -> float:
        """The matrix elements"""

    @A13.setter
    def A13(self, value: float): ...

    @property
    def A14(self) -> float:
        """The matrix elements"""

    @A14.setter
    def A14(self, value: float): ...

    @property
    def A21(self) -> float:
        """The matrix elements"""

    @A21.setter
    def A21(self, value: float): ...

    @property
    def A22(self) -> float:
        """The matrix elements"""

    @A22.setter
    def A22(self, value: float): ...

    @property
    def A23(self) -> float:
        """The matrix elements"""

    @A23.setter
    def A23(self, value: float): ...

    @property
    def A24(self) -> float:
        """The matrix elements"""

    @A24.setter
    def A24(self, value: float): ...

    @property
    def A31(self) -> float:
        """The matrix elements"""

    @A31.setter
    def A31(self, value: float): ...

    @property
    def A32(self) -> float:
        """The matrix elements"""

    @A32.setter
    def A32(self, value: float): ...

    @property
    def A33(self) -> float:
        """The matrix elements"""

    @A33.setter
    def A33(self, value: float): ...

    @property
    def A34(self) -> float:
        """The matrix elements"""

    @A34.setter
    def A34(self, value: float): ...

    @property
    def A41(self) -> float:
        """The matrix elements"""

    @A41.setter
    def A41(self, value: float): ...

    @property
    def A42(self) -> float:
        """The matrix elements"""

    @A42.setter
    def A42(self, value: float): ...

    @property
    def A43(self) -> float:
        """The matrix elements"""

    @A43.setter
    def A43(self, value: float): ...

    @property
    def A44(self) -> float:
        """The matrix elements"""

    @A44.setter
    def A44(self, value: float): ...

    def analyze(self):
        """
        analyze() -> string
        Analyzes the type of transformation.
                """

    def determinant(self):
        """
        determinant() -> Float
        Compute the determinant of the matrix
                """

    def inverse(self):
        """
        inverse() -> Matrix
        Compute the inverse matrix, if possible
                """

    def invert(self):
        """
        invert() -> None
        Compute the inverse matrix, if possible
                """

    def isOrthogonal(self, Float: float = None, /):
        """
        isOrthogonal([Float]) -> Float
        Checks if the matrix is orthogonal, i.e. M * M^T = k*I and returns
        the multiple of the identity matrix. If it's not orthogonal 0 is returned.
        As argument you can set a tolerance which by default is 1.0e-6.
                """

    @typing.overload
    def move(self, Vector: tuple, /): ...

    @typing.overload
    def move(self, Vector: FreeCAD.Vector, /):
        """
        move(Vector)
        Move the matrix along the vector
                """

    @typing.overload
    def multiply(self, Matrix_Vector: FreeCAD.Matrix, /): ...

    @typing.overload
    def multiply(self, Matrix_Vector: FreeCAD.Vector, /):
        """
        multiply(Matrix|Vector)
        Multiply a matrix or vector with this matrix
                """

    @typing.overload
    def rotateX(self, float: FreeCAD.Quantity, /): ...

    @typing.overload
    def rotateX(self, float: float, /):
        """rotateX(float) - rotate around X"""

    @typing.overload
    def rotateY(self, float: FreeCAD.Quantity, /): ...

    @typing.overload
    def rotateY(self, float: float, /):
        """rotateY(float) - rotate around Y"""

    @typing.overload
    def rotateZ(self, float: FreeCAD.Quantity, /): ...

    @typing.overload
    def rotateZ(self, float: float, /):
        """rotateZ(float) - rotate around Z"""

    @typing.overload
    def scale(self, Vector: tuple, /): ...

    @typing.overload
    def scale(self, Vector: FreeCAD.Vector, /):
        """
        scale(Vector)
        Scale the matrix with the vector
                """

    def submatrix(self, int: int, /):
        """
        submatrix(int) -> Matrix
        Get the sub-matrix. The parameter must be in the range [1,4].
                """

    def transform(self, Vector: FreeCAD.Vector, Matrix: FreeCAD.Matrix, /):
        """transform(Vector,Matrix) - return the dot product of the two vectors"""

    def transpose(self):
        """
        transpose() -> None
        Transpose the matrix. 
                """

    def transposed(self):
        """
        transposed() -> Matrix
        Returns a transposed copy of this matrix.
                """

    def unity(self):
        """unity() - make this matrix to unity"""

    def __eq__(self, other) -> bool: ...

    def __ne__(self, other) -> bool: ...

    def __lt__(self, other) -> bool: ...

    def __le__(self, other) -> bool: ...

    def __ge__(self, other) -> bool: ...

    def __gt__(self, other) -> bool: ...

    def __add__(self, other) -> Matrix: ...

    def __sub__(self, other) -> Matrix: ...

    def __mul__(self, other) -> Matrix: ...

    def __floordiv__(self, other): ...

    def __divmod__(self, other): ...

    def __truediv__(self, other) -> Matrix: ...

    def __pow__(self, power, modulo=None): ...

    def __neg__(self) -> Matrix: ...

    def __pos__(self) -> Matrix: ...

    def __abs__(self) -> Matrix: ...

    def __invert__(self): ...

    def __lshift__(self, other): ...

    def __rshift__(self, other): ...

    def __and__(self, other): ...

    def __xor__(self, other): ...

    def __or__(self, other): ...

    def __int__(self): ...

    def __float__(self): ...


# CoordinateSystemPy.xml
class CoordinateSystem(FreeCAD.PyObjectBase):
    @property
    def Axis(self) -> FreeCAD.Vector:
        """Set or get axis"""

    @Axis.setter
    def Axis(self, value: FreeCAD.Vector): ...

    @property
    def Position(self) -> object:
        """Set or get position"""

    @Position.setter
    def Position(self, value: object): ...

    @property
    def XDirection(self) -> object:
        """Set or get x direction"""

    @XDirection.setter
    def XDirection(self, value: object): ...

    @property
    def YDirection(self) -> object:
        """Set or get y direction"""

    @YDirection.setter
    def YDirection(self, value: object): ...

    @property
    def ZDirection(self) -> object:
        """Set or get z direction"""

    @ZDirection.setter
    def ZDirection(self, value: object): ...

    def displacement(self, CoordinateSystem: FreeCAD.CoordinateSystem, /):
        """displacement(CoordinateSystem)
        Computes the placement from this to the passed coordinate system"""

    @typing.overload
    def setAxes(self, Axis_or_Vector_z: FreeCAD.Axis, Vector_x: FreeCAD.Vector, /): ...

    @typing.overload
    def setAxes(self, Axis_or_Vector_z: FreeCAD.Vector, Vector_x: FreeCAD.Vector, /):
        """setAxes(Axis or Vector z, Vector x)
        Set axis or z direction and x direction"""

    def setPlacement(self, arg1: FreeCAD.Placement, /):
        """setPlacment(Placement)
        Set placement to the coordinate system.
                """

    @typing.overload
    def transform(self, Rotation_or_Placement: FreeCAD.Placement, /): ...

    @typing.overload
    def transform(self, Rotation_or_Placement: FreeCAD.Rotation, /):
        """transform(Rotation or Placement)
        Applies the rotation or placement on this coordinate system
                """

    def transformTo(self, Vector: FreeCAD.Vector, /):
        """transformTo(Vector)
        Computes the coordinates of the point in coordinates of this system
                """


# AxisPy.xml
class Axis(FreeCAD.PyObjectBase):
    """Axis
    An defines a direction and a position (base) in 3D space.

    The following constructors are supported:
    Axis() -- empty constructor
    Axis(Axis) -- copy constructor
    Axis(Base, Direction) -- define position and direction
    		"""

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, Axis: FreeCAD.Axis, /): ...

    @typing.overload
    def __init__(self, Base: FreeCAD.Vector, Direction: object, /):
        """Axis
        An defines a direction and a position (base) in 3D space.

        The following constructors are supported:
        Axis() -- empty constructor
        Axis(Axis) -- copy constructor
        Axis(Base, Direction) -- define position and direction
        		"""

    @property
    def Base(self) -> object:
        """Vector to the Base position of the Axis"""

    @Base.setter
    def Base(self, value: object): ...

    @property
    def Direction(self) -> object:
        """Direction vector of the Axis"""

    @Direction.setter
    def Direction(self, value: object): ...

    def copy(self):
        """
                            copy()
                            Returns a copy of this Axis
                        """

    def move(self, Vector: FreeCAD.Vector, /):
        """
        					move(Vector)
        					Move the axis base along the vector
        				"""

    def multiply(self, Placement: FreeCAD.Placement, /):
        """
        					multiply(Placement)
        					Multiply this axis with a placement
        				"""

    def reversed(self):
        """
        					reversed() -> Axis
        					compute the reversed axis
        				"""


# ParameterPy.cpp
class ParameterGrp:
    """Python interface class to set parameters"""

    def GetGroup(self, str: str, /):
        """GetGroup(str)"""

    def RemGroup(self, str: str, /):
        """RemGroup(str)"""

    def HasGroup(self, str: str, /):
        """HasGroup(str)"""

    def IsEmpty(self):
        """IsEmpty()"""

    def Clear(self):
        """Clear()"""

    def Attach(self, arg1: object, /):
        """Attach()"""

    def Detach(self, arg1: object, /):
        """Detach()"""

    def Notify(self, arg1: str, /):
        """Notify()"""

    def NotifyAll(self):
        """NotifyAll()"""

    def SetBool(self, arg1: str, arg2: int, /):
        """SetBool()"""

    def GetBool(self, arg1: str, arg2: int = None, /):
        """GetBool()"""

    def RemBool(self, arg1: str, /):
        """RemBool()"""

    def SetInt(self, arg1: str, arg2: int, /):
        """SetInt()"""

    def GetInt(self, arg1: str, arg2: int = None, /):
        """GetInt()"""

    def RemInt(self, arg1: str, /):
        """RemInt()"""

    def SetUnsigned(self, arg1: str, arg2: int, /):
        """SetUnsigned()"""

    def GetUnsigned(self, arg1: str, arg2: int = None, /):
        """GetUnsigned()"""

    def RemUnsigned(self, arg1: str, /):
        """RemUnsigned()"""

    def SetFloat(self, arg1: str, arg2: float, /):
        """SetFloat()"""

    def GetFloat(self, arg1: str, arg2: float = None, /):
        """GetFloat()"""

    def RemFloat(self, arg1: str, /):
        """RemFloat()"""

    def SetString(self, arg1: str, arg2: str, /):
        """SetString()"""

    def GetString(self, arg1: str, arg2: str = None, /):
        """GetString()"""

    def RemString(self, arg1: str, /):
        """RemString()"""

    def Import(self, arg1: str, /):
        """Import()"""

    def Insert(self, arg1: str, /):
        """Insert()"""

    def Export(self, arg1: str, /):
        """Export()"""

    def GetContents(self):
        """GetContents()"""


# Sequencer.cpp
class ProgressIndicator:
    """Progress indicator"""

    def start(self, string: str, int: int, /):
        """start(string,int)"""

    def next(self, arg1: int = None, /):
        """next()"""

    def stop(self):
        """stop()"""
