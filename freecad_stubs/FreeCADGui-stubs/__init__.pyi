import typing

from FreeCADGui.TaskDialogPython import Control as ControlClass
import FreeCAD
import FreeCADGui
import FreeCADGui.Selection
import FreeCADTemplates
import qtpy
import qtpy.QtGui
import qtpy.QtWidgets


class ReturnGetObjectInfoDict(typing.TypedDict):
    x: float
    y: float
    z: float
    Document: str
    Object: str
    Component: str


class ReturnGetObjectsInfoDict(typing.TypedDict):
    x: float
    y: float
    z: float
    Document: str
    Object: str
    Component: str



# WorkbenchPy.xml
class Workbench(FreeCAD.BaseClass):
    """This is the base class for workbenches"""

    MenuText = ""
    ToolTip = ""

    def Initialize(self):
        raise NotImplementedError

    def ContextMenu(self, recipient): ...

    def appendToolbar(self, name, cmds): ...

    def removeToolbar(self, name): ...

    def appendCommandbar(self, name, cmds): ...

    def removeCommandbar(self, name): ...

    def appendMenu(self, name, cmds): ...

    def removeMenu(self, name): ...

    def appendContextMenu(self, name, cmds): ...

    def removeContextMenu(self, name): ...

    def GetClassName(self): ...

    def activate(self):
        """Activate this workbench"""

    def name(self) -> str:
        """Return the workbench name"""


# ViewProviderPy.xml
class ViewProvider(FreeCAD.ExtensionContainer):
    """This is the ViewProvider base class"""

    @property
    def Annotation(self) -> object:
        """A pivy Separator to add a custom scene graph to this ViewProvider"""

    @Annotation.setter
    def Annotation(self, value: object): ...

    @property
    def IV(self) -> str:
        """Represents the whole ViewProvider as an Inventor string."""

    @property
    def Icon(self) -> str | qtpy.QtGui.QIcon:
        """The icon of this ViewProvider"""

    @property
    def RootNode(self) -> object:
        """A pivy Separator with the root of this ViewProvider"""

    @RootNode.setter
    def RootNode(self, value: object): ...

    def addDisplayMode(self, arg1, arg2: str, /):
        """
        Add a new display mode to the view provider
        Possible exceptions: (RuntimeError).
        """

    def addProperty(self, arg1: str, arg2: str = None, arg3: str = None, arg4: str = None, arg5: int = None, arg6: bool = None, arg7: bool = None, /) -> FreeCADGui.ViewProvider:
        """
        addProperty(string, string) -- Add a generic property.
                            The first argument specifies the type, the second the
                            name of the property.
                
        Possible exceptions: (RuntimeError, Exception).
        """

    def claimChildren(self) -> list[FreeCAD.DocumentObject | None]:
        """Returns list of objects that are to be grouped in tree under this object."""

    def finishEditing(self):
        """Finish editing mode"""

    def hide(self):
        """Hide the object"""

    def isEditing(self) -> bool:
        """Returns True if the view provider is in editing mode, False otherwise"""

    def isVisible(self) -> bool:
        """Check if the object is visible"""

    def listDisplayModes(self) -> list[str]:
        """Show a list of all display modes"""

    def removeProperty(self, string: str, /) -> bool:
        """
        removeProperty(string) -- Remove a generic property.
                            Note, you can only remove user-defined properties but not built-in ones.
                
        Possible exceptions: (RuntimeError).
        """

    @typing.overload
    def setTransformation(self, arg1: FreeCAD.Matrix, /): ...

    @typing.overload
    def setTransformation(self, arg1: FreeCAD.Placement, /):
        """
        Set a transformation on the Inventor node
        Possible exceptions: (FreeCAD.FreeCADError).
        """

    def show(self):
        """Show the object"""

    def startEditing(self, arg1: int = None, /) -> bool:
        """Start the editing mode (default=0)"""

    def supportedProperties(self) -> list[str]:
        """A list of supported property types"""

    def toString(self) -> str:
        """Return a string representation of the Inventor node"""


# PythonWorkbenchPy.xml
class PythonWorkbench(FreeCADGui.Workbench):
    """This class handles document objects in group"""

    def appendCommandbar(self, arg1: str, arg2, /):
        """
        Append a new command bar
        Possible exceptions: (AssertionError).
        """

    def appendContextMenu(self, arg1, arg2, /):
        """
        Append a new context menu item
        Possible exceptions: (AssertionError).
        """

    def appendMenu(self, arg1, arg2, /):
        """
        Append a new menu
        Possible exceptions: (AssertionError).
        """

    def appendToolbar(self, arg1: str, arg2, /):
        """
        Append a new toolbar
        Possible exceptions: (AssertionError).
        """

    def listCommandbars(self) -> list[str]:
        """Show a list of all command bars"""

    def listMenus(self) -> list[str]:
        """Show a list of all menus"""

    def listToolbars(self) -> list[str]:
        """Show a list of all toolbars"""

    def removeCommandbar(self, arg1: str, /):
        """Remove a command bar"""

    def removeContextMenu(self, arg1: str, /):
        """Remove a context menu item"""

    def removeMenu(self, arg1: str, /):
        """Remove a menu"""

    def removeToolbar(self, arg1: str, /):
        """Remove a toolbar"""


# ViewProviderDocumentObjectPy.xml
class ViewProviderDocumentObject(FreeCADGui.ViewProvider):
    """This is the ViewProvider base class"""

    @property
    def Proxy(self) -> FreeCADTemplates.ViewProviderPython: ...

    @Proxy.setter
    def Proxy(self, value: FreeCADTemplates.ViewProviderPython): ...

    @property
    def Object(self) -> FreeCAD.DocumentObject:
        """Return the associated data object"""

    @property
    def DisplayMode(self) -> int:
        """Property TypeId: App::PropertyEnumeration."""

    @DisplayMode.setter
    def DisplayMode(self, value): ...

    @property
    def Visibility(self) -> bool:
        """Property TypeId: App::PropertyBool."""

    @Visibility.setter
    def Visibility(self, value: int | bool): ...

    def update(self):
        """Update the view representation of the object"""


# SelectionObjectPy.xml
class SelectionObject(FreeCAD.BaseClass):
    """This class represents selections made by the user. It holds information about the object, document and sub-element of the selection."""

    @property
    def Document(self) -> FreeCADGui.Document:
        """Selected document"""

    @property
    def DocumentName(self) -> str:
        """Name of the document of the selected object"""

    @property
    def FullName(self) -> str:
        """Name of the selected object"""

    @property
    def HasSubObjects(self) -> bool:
        """Selected sub-element, if any"""

    @property
    def Object(self) -> object:
        """Selected object"""

    @property
    def ObjectName(self) -> str:
        """Name of the selected object"""

    @property
    def PickedPoints(self) -> tuple[FreeCAD.Vector, ...]:
        """Picked points for selection"""

    @property
    def SubElementNames(self) -> tuple[str, ...]:
        """Name of the selected sub-element if any"""

    @property
    def SubObjects(self) -> tuple[object, ...]:
        """Selected sub-element, if any"""

    @property
    def TypeName(self) -> str:
        """Type name of the selected object"""

    def isObjectTypeOf(self, arg1: str, /) -> bool:
        """
        Test for a certain father class.
        Possible exceptions: (TypeError).
        """

    def remove(self):
        """Remove this selection item from the selection. This object becomes invalid."""


# DocumentPy.xml
class Document(FreeCAD.Persistence):
    """This is a Document class"""

    @property
    def ActiveObject(self) -> FreeCADGui.ViewProvider | None:
        """The active object of the document"""

    @ActiveObject.setter
    def ActiveObject(self, value: FreeCADGui.ViewProvider | None): ...

    @property
    def ActiveView(self) -> FreeCADGui.MDIViewPy | None:
        """The active view of the document"""

    @ActiveView.setter
    def ActiveView(self, value: FreeCADGui.MDIViewPy | None): ...

    @property
    def Document(self) -> FreeCAD.Document:
        """The related App document to this Gui document"""

    @property
    def Modified(self) -> bool:
        """Returns True if the document is marked as modified, and False otherwse"""

    def activeObject(self) -> FreeCADGui.ViewProvider:
        """deprecated -- use ActiveObject"""

    def activeView(self) -> FreeCADGui.MDIViewPy:
        """deprecated -- use ActiveView"""

    def addAnnotation(self, arg1: str, arg2: str, arg3: str = None, /):
        """Add an Inventor object"""

    def getInEdit(self) -> FreeCADGui.ViewProvider:
        """
        getInEdit()
                  Returns the current object in edit mode or None if there is no such object
        """

    def getObject(self, arg1: str, /) -> FreeCADGui.ViewProvider:
        """Return the object with the given name"""

    def hide(self, arg1: str, /):
        """Hide the object"""

    def mdiViewsOfType(self, arg1: str, /) -> list[FreeCADGui.MDIViewPy]:
        """Return a list if mdi views of a given type"""

    def mergeProject(self, arg1: str, /):
        """Merges this document with another project file"""

    def resetEdit(self):
        """Reset (end) the current editing."""

    def scrollToTreeItem(self, ViewObject: FreeCADGui.ViewProviderDocumentObject, /):
        """scrollToTreeItem(ViewObject) - scroll the tree view to the item of a view object"""

    def sendMsgToViews(self, arg1: str, /):
        """Send a message to all views of the document"""

    @typing.overload
    def setEdit(self, String_Name_ViewProvider_DocumentObject_: str, mod: int = None, /) -> bool: ...

    @typing.overload
    def setEdit(self, String_Name_ViewProvider_DocumentObject_: FreeCAD.DocumentObject, mod: int = None, /) -> bool: ...

    @typing.overload
    def setEdit(self, String_Name_ViewProvider_DocumentObject_: FreeCADGui.ViewProvider, mod: int = None, /) -> bool:
        """
        setEdit([String:Name|ViewProvider|DocumentObject]|,mod)
                  Set the given object in edit mode.
        
        Possible exceptions: (TypeError).
        """

    def setPos(self, arg1: str, arg2: FreeCAD.Matrix, /):
        """Set the position"""

    def show(self, arg1: str, /):
        """Show the object"""

    def toggleTreeItem(self, DocObject: FreeCAD.DocumentObject, int: int = 0, /):
        """toggleTreeItem(DocObject,int=0) - change TreeItem of a document object 0:Toggle,1:Collaps,2:Expand"""

    def update(self):
        """Update the view representations of all objects"""


# Application.cpp
def subgraphFromObject(object: FreeCAD.DocumentObject, /) -> object | None:
    """
    subgraphFromObject(object) -> Node

    Return the Inventor subgraph to an object
    """


def getSoDBVersion() -> str:
    """
    getSoDBVersion() -> String

    Return a text string containing the name
    of the Coin library and version information
    """


# View3DPy.cpp
class View3DInventorPy:
    """Python binding class for the Inventor viewer class"""

    def message(self, arg1: str, /) -> None:
        """message()"""

    def fitAll(self, arg1: float = None, /) -> None:
        """fitAll()"""

    def viewBottom(self) -> None:
        """viewBottom()"""

    def viewFront(self) -> None:
        """viewFront()"""

    def viewLeft(self) -> None:
        """viewLeft()"""

    def viewRear(self) -> None:
        """viewRear()"""

    def viewRight(self) -> None:
        """viewRight()"""

    def viewTop(self) -> None:
        """viewTop()"""

    def viewAxometric(self) -> None:
        """viewAxonometric()"""

    def viewAxonometric(self) -> None:
        """viewAxonometric()"""

    def viewRotateLeft(self) -> None:
        """viewRotateLeft()"""

    def viewRotateRight(self) -> None:
        """viewRotateRight()"""

    def zoomIn(self) -> None:
        """zoomIn()"""

    def zoomOut(self) -> None:
        """zoomOut()"""

    def viewPosition(self, arg1: FreeCAD.Placement = None, arg2: int = None, arg3: int = None, /) -> FreeCAD.Placement | None:
        """viewPosition()"""

    def startAnimating(self, arg1: float, arg2: float, arg3: float, arg4: float, /) -> None:
        """startAnimating()"""

    def stopAnimating(self) -> None:
        """stopAnimating()"""

    def setAnimationEnabled(self, arg1: int, /) -> None:
        """setAnimationEnabled()"""

    def isAnimationEnabled(self) -> bool:
        """isAnimationEnabled()"""

    def dump(self, arg1: str, /) -> None:
        """dump()"""

    def dumpNode(self, node, /) -> str:
        """dumpNode(node)"""

    @typing.overload
    def setStereoType(self, arg1: int, /) -> None: ...

    @typing.overload
    def setStereoType(self, arg1: str, /) -> None:
        """setStereoType()"""

    def getStereoType(self) -> str:
        """getStereoType()"""

    def listStereoTypes(self) -> list:
        """listStereoTypes()"""

    def saveImage(self, arg1: str, arg2: int = None, arg3: int = None, arg4: str = None, arg5: str = None, /) -> None:
        """saveImage()"""

    def saveVectorGraphic(self, arg1: str, arg2: int = None, arg3: str = None, /) -> None:
        """saveVectorGraphic()"""

    def getCamera(self) -> str:
        """getCamera()"""

    def getCameraNode(self):
        """getCameraNode()"""

    def getViewDirection(self) -> FreeCAD.Vector:
        """
        getViewDirection() --> tuple of integers
        returns the direction vector the view is currently pointing at as tuple with xyz values
        """

    def setViewDirection(self, tuple, /) -> None:
        """
        setViewDirection(tuple) --> None
        Sets the direction the view is pointing at. The direction must be given as tuple with
        three coordinates xyz
        """

    def setCamera(self, arg1: str, /) -> None:
        """setCamera()"""

    def setCameraOrientation(self, arg1, arg2: bool = None, /) -> None:
        """setCameraOrientation()"""

    def getCameraOrientation(self) -> FreeCAD.Rotation:
        """getCameraOrientation()"""

    def getCameraType(self) -> str:
        """getCameraType()"""

    @typing.overload
    def setCameraType(self, arg1: int, /) -> None: ...

    @typing.overload
    def setCameraType(self, arg1: str, /) -> None:
        """setCameraType()"""

    def listCameraTypes(self) -> list:
        """listCameraTypes()"""

    def getCursorPos(self) -> tuple[int, int]:
        """
        getCursorPos() -> tuple of integers

        Return the current cursor position relative to the coordinate system of the
        viewport region.
        """

    def getObjectInfo(self, tuple_int_int_, pick_radius: float = None, /) -> ReturnGetObjectInfoDict | None:
        """
        getObjectInfo(tuple(int,int), [pick_radius]) -> dictionary or None

        Return a dictionary with the name of document, object and component. The
        dictionary also contains the coordinates of the appropriate 3d point of
        the underlying geometry in the scenegraph.
        If no geometry was found 'None' is returned, instead.
        """

    def getObjectsInfo(self, tuple_int_int_, pick_radius: float = None, /) -> ReturnGetObjectsInfoDict | list[ReturnGetObjectsInfoDict] | None:
        """
        getObjectsInfo(tuple(int,int), [pick_radius]) -> dictionary or None

        Does the same as getObjectInfo() but returns a list of dictionaries or None.
        """

    def getSize(self) -> tuple[int, int]:
        """getSize()"""

    def getPoint(self, arg1: int, arg2: int, /) -> FreeCAD.Vector:
        """
        getPoint(pixel coords (as integer)) -> 3D vector

        Return the according 3D point on the focal plane to the given 2D point (in
        pixel coordinates).
        """

    def getPointOnScreen(self, arg1: FreeCAD.Vector, /) -> tuple[int, int]:
        """
        getPointOnScreen(3D vector) -> pixel coords (as integer)

        Return the projected 3D point (in pixel coordinates).
        """

    def addEventCallback(self, arg1: str, arg2, /) -> typing.Callable:
        """addEventCallback()"""

    def removeEventCallback(self, arg1: str, arg2, /) -> None:
        """removeEventCallback()"""

    def setAnnotation(self, arg1: str, arg2: str, /) -> None:
        """setAnnotation()"""

    def removeAnnotation(self, arg1: str, /) -> None:
        """removeAnnotation()"""

    def getSceneGraph(self):
        """getSceneGraph()"""

    def getViewer(self) -> FreeCADGui.View3DInventorViewerPy:
        """getViewer()"""

    def addEventCallbackPivy(self, arg1, arg2, arg3: int = None, /) -> typing.Callable:
        """addEventCallbackPivy()"""

    def removeEventCallbackPivy(self, arg1, arg2, arg3: int = None, /) -> typing.Callable:
        """removeEventCallbackPivy()"""

    def addEventCallbackSWIG(self, arg1, arg2, arg3: int = None, /) -> typing.Callable:
        """Deprecated -- use addEventCallbackPivy()"""

    def removeEventCallbackSWIG(self, arg1, arg2, arg3: int = None, /) -> typing.Callable:
        """Deprecated -- use removeEventCallbackPivy()"""

    def listNavigationTypes(self):
        """listNavigationTypes()"""

    def getNavigationType(self):
        """getNavigationType()"""

    def setNavigationType(self, arg1: str, /) -> None:
        """setNavigationType()"""

    def setAxisCross(self, arg1: int, /) -> None:
        """switch the big axis-cross on and off"""

    def hasAxisCross(self) -> bool:
        """check if the big axis-cross is on or off()"""

    def addDraggerCallback(self, SoDragger, String_CallbackType: str, function, /) -> typing.Callable:
        """
        addDraggerCallback(SoDragger, String CallbackType, function)
        Add a DraggerCalback function to the coin node
        Possibles types :
        'addFinishCallback','addStartCallback','addMotionCallback','addValueChangedCallback'
        """

    def removeDraggerCallback(self, SoDragger, String_CallbackType: str, function, /) -> typing.Callable:
        """
        removeDraggerCallback(SoDragger, String CallbackType, function)
        Remove the DraggerCalback function from the coin node
        Possibles types :
        'addFinishCallback','addStartCallback','addMotionCallback','addValueChangedCallback'
        """

    def setActiveObject(self, name: str, object: FreeCAD.DocumentObject, /) -> None:
        """
        setActiveObject(name,object)
        add or set a new active object
        """

    def getActiveObject(self, name: str, /) -> FreeCAD.DocumentObject | None:
        """
        getActiveObject(name)
        returns the active object for the given type
        """

    def getViewProvidersOfType(self, name: str, /) -> list[FreeCADGui.ViewProvider]:
        """
        getViewProvidersOfType(name)
        returns a list of view providers for the given type
        """

    def redraw(self) -> None:
        """redraw(): renders the scene on screen (useful for animations)"""

    def boxZoom(self, XMin: int, YMin: int, XMax: int, YMax: int) -> None:
        """boxZoom()"""


# WidgetFactory.cpp
class UiLoader:
    """UiLoader to create widgets"""

    @typing.overload
    def load(self, string, QWidget_parent=None, /): ...

    @typing.overload
    def load(self, QIODevice, QWidget_parent=None, /):
        """
        load(string, QWidget parent=None) -> QWidget
        load(QIODevice, QWidget parent=None) -> QWidget
        """

    def createWidget(self):
        """createWidget()"""


class PyResource:
    """PyResource"""

    def value(self, arg1: str, arg2: str, /) -> list | str | float | bool | int | None: ...

    def setValue(self, arg1: str, arg2: str, arg3, /) -> None: ...


# PythonConsolePy.cpp
class PythonStdout:
    """Redirection of stdout to FreeCAD's Python console window"""

    def isatty(self):
        """isatty()"""

    def write(self):
        """write()"""

    def flush(self):
        """flush()"""


class PythonStderr:
    """Redirection of stdout to FreeCAD's Python console window"""

    def isatty(self):
        """isatty()"""

    def write(self):
        """write()"""

    def flush(self):
        """flush()"""


class OutputStdout:
    """Redirection of stdout to FreeCAD's output window"""

    def isatty(self):
        """isatty()"""

    def write(self):
        """write()"""

    def flush(self):
        """flush()"""


class OutputStderr:
    """Redirection of stdout to FreeCAD's output window"""

    def isatty(self):
        """isatty()"""

    def write(self):
        """write()"""

    def flush(self):
        """flush()"""


class PythonStdin:
    """Redirection of stdin to FreeCAD to open an input dialog"""

    def readline(self):
        """readline()"""


# SplitView3DInventor.cpp
class AbstractSplitViewPy:
    """Python binding class for the Inventor viewer class"""

    def fitAll(self) -> None:
        """fitAll()"""

    def viewBottom(self) -> None:
        """viewBottom()"""

    def viewFront(self) -> None:
        """viewFront()"""

    def viewLeft(self) -> None:
        """viewLeft()"""

    def viewRear(self) -> None:
        """viewRear()"""

    def viewRight(self) -> None:
        """viewRight()"""

    def viewTop(self) -> None:
        """viewTop()"""

    def viewAxometric(self) -> None:
        """viewAxometric()"""

    def getViewer(self, index: int, /) -> FreeCADGui.View3DInventorViewer:
        """getViewer(index)"""

    def close(self) -> None:
        """close()"""


# SelectionFilter.cpp
class SelectionFilter:
    """
    Filter for certain selection
    Example strings are:
    "SELECT Part::Feature SUBELEMENT Edge",
    "SELECT Part::Feature", 
    "SELECT Part::Feature COUNT 1..5"
    """

    def match(self) -> bool:
        """Check if the current selection matches the filter"""

    def result(self):
        """If match() returns True then with result() you get a list of the matching objects"""

    def test(self, Feature: FreeCAD.DocumentObject, SubName: str = '', /) -> bool:
        """
        test(Feature, SubName='')
        Test if a given object is described in the filter.
        If SubName is not empty the sub-element gets also tested.
        """

    def setFilter(self, arg1: str, /) -> None:
        """Set a new selection filter"""


# PythonDebugger.cpp
class PythonDebugStdout:
    """Redirection of stdout to FreeCAD's Python debugger window"""

    def write(self, arg1: str, /) -> None:
        """write to stdout"""


class PythonDebugStderr:
    """Redirection of stderr to FreeCAD's Python debugger window"""

    def write(self, arg1: str, /) -> None:
        """write to stderr"""


class PythonDebugExcept:
    """Custom exception handler"""

    pass
# ApplicationPy.cpp
def activateWorkbench(string: str, /) -> None:
    """
    activateWorkbench(string) -> None

    Activate the workbench by name
    """


def addWorkbench(arg0, /) -> None:
    """
    addWorkbench(string, object) -> None

    Add a workbench under a defined name.
    """


def removeWorkbench(string: str, /) -> None:
    """
    removeWorkbench(string) -> None

    Remove the workbench with name
    """


def getWorkbench(string: str, /):
    """
    getWorkbench(string) -> object

    Get the workbench by its name
    """


def listWorkbenches():
    """
    listWorkbenches() -> list

    Show a list of all workbenches
    """


def activeWorkbench():
    """
    activeWorkbench() -> object

    Return the active workbench object
    """


def addResourcePath(string: str, /) -> None:
    """
    addResourcePath(string) -> None

    Add a new path to the system where to find resource files
    like icons or localization files
    """


def addLanguagePath(string: str, /) -> None:
    """
    addLanguagePath(string) -> None

    Add a new path to the system where to find language files
    """


def addIconPath(string: str, /) -> None:
    """
    addIconPath(string) -> None

    Add a new path to the system where to find icon files
    """


def addIcon(string: str, string_or_list: str, /) -> None:
    """
    addIcon(string, string or list) -> None

    Add an icon as file name or in XPM format to the system
    """


def getMainWindow() -> qtpy.QtWidgets.QMainWindow:
    """
    getMainWindow() -> QMainWindow

    Return the main window instance
    """


def updateGui() -> None:
    """
    updateGui() -> None

    Update the main window and all its windows
    """


def updateLocale() -> None:
    """
    updateLocale() -> None

    Update the localization
    """


def getLocale() -> str:
    """
    getLocale() -> string

    Returns the locale currently used by FreeCAD
    """


def createDialog(string: str, /):
    """createDialog(string) -- Open a UI file"""


@typing.overload
def addPreferencePage(string: str, string1: str, /) -> None: ...


@typing.overload
def addPreferencePage(string: type, string1: str, /) -> None: ...


@typing.overload
def addPreferencePage(string: typing.Type, string1: str, /) -> None:
    """
    addPreferencePage(string,string) -- Add a UI form to the
    preferences dialog. The first argument specifies the file nameand the second specifies the group name
    """


def addCommand(arg0: str, arg1, arg2: str = None, /) -> None:
    """
    addCommand(string, object) -> None

    Add a command object
    """


def runCommand(arg0: str, arg1: int = None, /) -> None:
    """
    runCommand(string) -> None

    Run command with name
    """


def listCommands() -> list[str]:
    """
    listCommands() -> list of strings

    Returns a list of all commands known to FreeCAD.
    """


def SendMsgToActiveView(arg0: str, arg1: bool = None, /) -> str | None:
    """deprecated -- use class View"""


def hide(arg0: str, /):
    """deprecated"""


def show(arg0: str, /):
    """deprecated"""


def hideObject(object: FreeCAD.DocumentObject, /):
    """
    hideObject(object) -> None

    Hide the view provider to the given object
    """


def showObject(object: FreeCAD.DocumentObject, /):
    """
    showObject(object) -> None

    Show the view provider to the given object
    """


def open(arg0: str, /):
    """Open a macro, Inventor or VRML file"""


def insert(arg0: str, arg1: str = None, /):
    """Open a macro, Inventor or VRML file"""


def export(arg0, arg1: str, /):
    """save scene to Inventor or VRML file"""


def activeDocument() -> FreeCADGui.Document:
    """
    activeDocument() -> object or None

    Return the active document or None if no one exists
    """


@typing.overload
def setActiveDocument(string_or_App_Document: str, /): ...


@typing.overload
def setActiveDocument(string_or_App_Document: FreeCAD.Document, /):
    """
    setActiveDocument(string or App.Document) -> None

    Activate the specified document
    """


def activeView() -> FreeCADGui.MDIViewPy:
    """
    activeView() -> object or None

    Return the active view of the active document or None if no one exists
    """


@typing.overload
def getDocument(string: str, /) -> FreeCADGui.Document: ...


@typing.overload
def getDocument(string: FreeCAD.Document, /) -> FreeCADGui.Document:
    """
    getDocument(string) -> object

    Get a document by its name
    """


def doCommand(string: str, /):
    """
    doCommand(string) -> None

    Prints the given string in the python console and runs it
    """


def doCommandGui(string: str, /):
    """
    doCommandGui(string) -> None

    Prints the given string in the python console and runs it but doesn't record it in macros
    """


def addModule(string: str, /) -> None:
    """
    addModule(string) -> None

    Prints the given module import only once in the macro recording
    """


def showDownloads() -> None:
    """
    showDownloads() -> None

    Shows the downloads manager window
    """


def showPreferences(string: str = None, int: int = None, /) -> None:
    """
    showPreferences([string,int]) -> None

    Shows the preferences window. If string and int are provided, the given page index in the given group is shown.
    """


def createViewer(arg0: int = None, arg1: str = None, /) -> object | FreeCADGui.AbstractSplitViewPy | None:
    """
    createViewer([int]) -> View3DInventor/SplitView3DInventor

    shows and returns a viewer. If the integer argument is given and > 1: -> splitViewer
    """


# View3DViewerPy.cpp
class View3DInventorViewerPy:
    """Python binding class for the 3D viewer class"""

    def getSoRenderManager(self):
        """
        getSoRenderManager() -> SoRenderManager
        Returns the render manager which is used to handle everything related to
        rendering the scene graph. It can be used to get full control over the
        render process
        """

    def getSoEventManager(self):
        """
        getSoEventManager() -> SoEventManager
        Returns the event manager which is used to handle everything event related in
        the viewer. It can be used to change the event processing. This must however be
        done very carefully to not change the user interaction in an unpredictable manner.
        """

    def getSceneGraph(self):
        """getSceneGraph() -> SoNode"""

    def setSceneGraph(self, SoNode, /) -> None:
        """setSceneGraph(SoNode)"""

    def seekToPoint(self, tuple, /) -> None:
        """
        seekToPoint(tuple) -> None
        Initiate a seek action towards the 3D intersection of the scene and the
        ray from the screen coordinate's point and in the same direction as the
        camera is pointing. If the tuple has two entries it is interpretet as the
        screen coordinates xy and the intersection point with the scene is
        calculated. If three entries are given it is interpretet as the intersection
        point xyz and the seek is done towards this point
        """

    def setFocalDistance(self, float: float, /) -> None:
        """setFocalDistance(float) -> None"""

    def getFocalDistance(self) -> float:
        """getFocalDistance() -> float"""

    def getPoint(self, x: int, y: int, /) -> FreeCAD.Vector:
        """getPoint(x, y) -> Base::Vector(x,y,z)"""

    def getPickRadius(self) -> float:
        """getPickRadius(): returns radius of confusion in pixels for picking objects on screen (selection)."""

    def setPickRadius(self, new_radius: float, /) -> None:
        """setPickRadius(new_radius): sets radius of confusion in pixels for picking objects on screen (selection)."""


Workbench: FreeCADGui.Workbench
ActiveDocument: FreeCADGui.Document
Control = ControlClass()  # hack to show this module in current module hints
