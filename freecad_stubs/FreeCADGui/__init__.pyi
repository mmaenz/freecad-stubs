import typing

import FreeCAD
import FreeCADGui
import FreeCADGui.Selection


# WorkbenchPy.xml
class Workbench(FreeCAD.BaseClass):
    """This is the base class for workbenches"""

    def activate(self):
        """Activate this workbench"""

    def getToolbarItems(self):
        """Show a dict of all toolbars and their commands"""

    def listCommandbars(self):
        """Show a list of all command bars"""

    def listMenus(self):
        """Show a list of all menus"""

    def listToolbars(self):
        """Show a list of all toolbars"""

    def name(self):
        """Return the workbench name"""


# LinkViewPy.xml
class LinkView(FreeCAD.BaseClass):
    """Helper class to link to a view object"""

    @property
    def Count(self) -> int:
        """Set the element size to create an array of linked object"""

    @property
    def LinkedView(self) -> object:
        """The linked view object"""

    @property
    def Owner(self) -> object:
        """The owner view object of this link handle"""

    @property
    def RootNode(self) -> object:
        """A pivy node holding the cloned representation of the linked view object"""

    @property
    def SubNames(self) -> object:
        """The sub-object reference of the link"""

    @property
    def Visibilities(self) -> object:
        """Get/set the child element visibility"""

    def getBoundBox(self, vobj: object, /):
        """getBoundBox(vobj=None): get the bounding box. """

    def getChildren(self):
        """Get children view objects"""

    def getDetailPath(self, arg1: str, arg2: object, /):
        """
        getDetailPath(element): get the 3d path an detail of an element.

        Return a tuple(path,detail) for the coin3D SoPath and SoDetail of the element
                        """

    def getElementPicked(self, pickPoint: object, /):
        """getElementPicked(pickPoint): get the element under a 3d pick point. """

    def reset(self):
        """Reset the link view and clear the links"""

    def setChildren(self, obj_: object, vis: object = [], type: str = 0, /):
        """
        setChildren([obj...],vis=[],type=0)
        Group a list of children objects. Note, this mode of operation is incompatible 
        with link array. Calling this function will deactivate link array. And calling
        setSize() will reset all linked children.

        vis: initial visibility status of the children

        type: children linking type, 
           0: override transformation and visibility, 
           1: override visibility, 
           2: override none.
                        """

    def setLink(self, object: object, subname: object = None, /):
        """
        setLink(object): Set the link

        setLink(object, subname): Set the link with a sub-object reference

        setLink(object, [subname,...]): Set the link with a list of sub object references

        object: The linked document object or its view object

        subname: a string or tuple/list of strings sub-name references to sub object
                 or sub elements (e.g. Face1, Edge2) belonging to the linked object.
                 The sub-name must end with a '.' if it is referencing an sub-object,
                 or else it is considered a sub-element reference.
                        """

    def setMaterial(self, Material: object, /):
        """
        setMaterial(Material): set the override material of the entire linked object

        setMaterial([Material,...]): set the materials for the elements of the link
                                     array/group. 

        setMaterial({Int:Material,...}): set the material for the elements of the
                                         link array/group by index. 

        If material is None, then the material is unset. If the material of an element
        is unset, it defaults to the override material of the linked object, if there
        is one
                        """

    def setTransform(self, matrix: object, /):
        """
        setTransform(matrix): set transformation of the linked object

        setTransform([matrix,...]): set transformation for the elements of the link
                                    array/group

        setTransform({index:matrix,...}): set transformation for elements of the link
                                          array/group by index
                        """

    def setType(self, type: int, sublink: object = True, /):
        """
        setType(type, sublink=True): set the link type.

        type=0:  override transformation and visibility
        type=1:  override visibility
        type=2:  no override
        type=-1: sub-object link with override visibility
        type=-2: sub-object link with override transformation and visibility

        sublink: auto delegate to the sub-object references in the link, if there is
                 one and only one.
                        """


# ViewProviderPy.xml
class ViewProvider(FreeCAD.ExtensionContainer):
    """This is the ViewProvider base class"""

    @property
    def Annotation(self) -> object:
        """A pivy Separator to add a custom scenegraph to this ViewProvider"""

    @Annotation.setter
    def Annotation(self, value: object): ...

    @property
    def CanRemoveChildrenFromRoot(self) -> bool:
        """Tells the tree view whether to remove the children item from root or not"""

    @property
    def DefaultMode(self) -> int:
        """Get/Set the default display mode in turns of coin node index"""

    @DefaultMode.setter
    def DefaultMode(self, value: int): ...

    @property
    def DropPrefix(self) -> str:
        """Subname referecing the sub-object for holding dropped object"""

    @property
    def IV(self) -> str:
        """Represents the whole ViewProvider as an Inventor string."""

    @property
    def Icon(self) -> object:
        """The icon of this ViewProvider"""

    @property
    def LinkVisibility(self) -> bool:
        """Get/set visibilities of all links to this view object"""

    @property
    def RootNode(self) -> object:
        """A pivy Separator with the root of this ViewProvider"""

    @RootNode.setter
    def RootNode(self, value: object): ...

    @property
    def SwitchNode(self) -> object:
        """A pivy SoSwitch for the display mode switch of this ViewProvider"""

    @SwitchNode.setter
    def SwitchNode(self, value: object): ...

    def addDisplayMode(self, arg1: object, arg2: str, /):
        """Add a new display mode to the view provider
        """

    def addProperty(self, arg1: str, arg2: str = None, arg3: str = None, arg4: str = None, arg5: int = None, arg6: bool = None, arg7: bool = None, /):
        """Add a generic property.
        addProperty(string, string)
        --
        The first argument specifies the type, the second the name of the property.
                        """

    def canDragAndDropObject(self, obj: FreeCAD.DocumentObject, /):
        """Check whether the child object can be removed from other parent and added here by drag and drop
        canDragAndDropObject(obj)
        """

    def canDragObject(self, obj: object = None, /):
        """check whether the child object can be removed by dragging
        canDragObject(obj=None)
        """

    def canDropObject(self, arg1: object = None, arg2: object = None, arg3: str = None, arg4: object = None, /):
        """check whether the child object can be added by dropping
        canDropObject(obj=None,owner=None,subname=None)
        """

    def claimChildren(self):
        """Returns list of objects that are to be grouped in tree under this object.
        """

    def doubleClicked(self):
        """Trigger double clicking the corresponding tree item of this view object
        """

    def dragObject(self, obj: FreeCAD.DocumentObject, /):
        """remove a child object by dropping
        dragObject(obj)
        """

    def dropObject(self, arg1: FreeCAD.DocumentObject, arg2: object = None, arg3: str = None, arg4: object = None, /):
        """add a child object by dropping
        dropObject(obj,owner=None,subname=None)"""

    def getBoundingBox(self, subname: str = None, transform: object = True, view: object = None, /):
        """obtain the bounding box of this view object
        getBoundingBox(subname=None, transform=True, view=None)
        --
        subname: the optional subname referring a sub-object
        transform: whether to apply the transformation matrix of this view provider
        view: the MDIView, default to active view
        """

    def getDetailPath(self, subname: str, path: object, append: object = True, /):
        """return Coin detail and path of an subelement
        getDetailPath(subname,path,append=True)
        --
        subelement: dot separated string reference to the sub element
        pPath: output coin path leading to the returned element detail
        append: If true, path will be first appended with the root node and the mode
        switch node of this view provider.
        """

    def getElementColors(self, elementName: str = None, /):
        """
        getElementColors(elementName=None) -> dict(elementName:color)
                        """

    def getElementPicked(self, pickPoint: object, /):
        """return the picked subelement
        getElementPicked(pickPoint)
        """

    def hide(self):
        """Hide the object
        """

    def isVisible(self):
        """Check if the object is visible
        """

    def listDisplayModes(self):
        """Show a list of all display modes
        """

    def partialRender(self, sub: object = None, clear: object = False, /):
        """render only part of the object
        partialRender(sub=None,clear=False)
        --
        sub: string or list of string refer to the subelement. If it is None then reset the partial rendering.
        clear: true to add, or false to remove the subelement(s) for rendering.
        """

    def removeProperty(self, string: str, /):
        """Remove a generic property.
        removeProperty(string)
        --
        Note, you can only remove user-defined properties, not built-in ones.
                        """

    def replaceObject(self, oldObj: FreeCAD.DocumentObject, newObj: FreeCAD.DocumentObject, /):
        """replace a child object
        replaceObject(oldObj, newObj) -> Int
        --
        Returns 1 if succeeded, 0 if not found, -1 if not supported
        """

    def setElementColors(self, colors: object, /):
        """
        setElementColors(colors): set element colors
        --
        colors: color dictionary of type elementName:(r,g,b,a)
                        """

    @typing.overload
    def setTransformation(self, arg1: FreeCAD.Matrix, /): ...

    @typing.overload
    def setTransformation(self, arg1: FreeCAD.Placement, /):
        """Set a transformation on the Inventor node
        """

    def show(self):
        """Show the object
        """

    def signalChangeIcon(self):
        """Trigger icon changed signal"""

    def supportedProperties(self):
        """A list of supported property types
        """

    def toString(self):
        """Return a string representation of the Inventor node
        """


# ViewProviderLinkPy.xml
class ViewProviderLink(FreeCADGui.ViewProviderDocumentObject):
    """This is the ViewProviderLink class"""

    @property
    def DraggingPlacement(self) -> object:
        """Get/set dragger placement during dragging"""

    @property
    def LinkView(self) -> object:
        """Get the associated LinkView object"""

    @property
    def UseCenterballDragger(self) -> bool:
        """Get/set dragger type"""


# ViewProviderExtensionPy.xml
class ViewProviderExtension(FreeCAD.Extension):
    """Base class for all view provider extensions"""

    def ignoreOverlayIcon(self, arg1: str, /):
        """Ignore the overlay icon of an extension"""

    def setIgnoreOverlayIcon(self, arg1: bool, arg2: str, /):
        """Ignore the overlay icon of an extension"""


# CommandPy.xml
class Command(FreeCAD.PyObjectBase):
    """FreeCAD Python wrapper of Command functions"""

    @staticmethod
    def get(string: str, /):
        """Get a given command by name or None if it doesn't exist.
        get(string) -> Command
        """

    def getAction(self):
        """Return the associated QAction object.
        getAction() -> list of QAction"""

    def getInfo(self):
        """Return information about this command.
        getInfo() -> list of strings
        --
        Usage: menuText, tooltipText, whatsThisText, statustipText, pixmapText, shortcutText.
        """

    def getShortcut(self):
        """Returns string representing shortcut key accelerator for command.
        getShortcut() -> string
        """

    def isActive(self):
        """Returns True if the command is active, False otherwise.
        isActive() -> bool
        """

    @staticmethod
    def listAll():
        """Returns the name of all commands.
        listAll() -> list of strings
        """

    @staticmethod
    def listByShortcut(string: str, bool_bUseRegExp: int = False, /):
        """Returns a list of all commands, filtered by shortcut.
        listByShortcut(string, bool bUseRegExp=False) -> list of strings
        --
        Shortcuts are converted to uppercase and spaces removed prior to comparison.
        """

    def resetShortcut(self):
        """Resets shortcut for given command back to the default, returns bool True for success.
        resetShortcut() -> bool
        """

    def run(self, arg1: int = None, /):
        """Runs the given command.
        run() -> None
        """

    def setShortcut(self, string: str, /):
        """Sets shortcut for given command, returns bool True for success.
        setShortcut(string) -> bool
        """

    @staticmethod
    def update():
        """Update active status of all commands.
        update() -> None
        """


# PythonWorkbenchPy.xml
class PythonBaseWorkbench(FreeCADGui.Workbench):
    """This class handles document objects in group"""

    def appendCommandbar(self, arg1: str, arg2: object, /):
        """Append a new command bar"""

    def appendContextMenu(self, arg1: object, arg2: object, /):
        """Append a new context menu item"""

    def appendMenu(self, arg1: object, arg2: object, /):
        """Append a new menu"""

    def appendToolbar(self, arg1: str, arg2: object, /):
        """Append a new toolbar"""

    def removeCommandbar(self, arg1: str, /):
        """Remove a command bar"""

    def removeContextMenu(self, arg1: str, /):
        """Remove a context menu item"""

    def removeMenu(self, arg1: str, /):
        """Remove a menu"""

    def removeToolbar(self, arg1: str, /):
        """Remove a toolbar"""


# AxisOriginPy.xml
class AxisOrigin(FreeCAD.BaseClass):
    """Class for creating a Coin3D representation of a coordinate system"""

    @property
    def AxisLength(self) -> float:
        """Get/set the axis length"""

    @property
    def Labels(self) -> dict:
        """
        Get/set axis component names as a dictionary. Available keys are,
        'O': origin
        'X': x axis
        'Y': y axis
        'Z': z axis
        'XY': xy plane
        'XZ': xz plane
        'YZ': yz plane
                        """

    @property
    def LineWidth(self) -> float:
        """Get/set the axis line width for rendering"""

    @property
    def Node(self) -> object:
        """Get the Coin3D node"""

    @property
    def Plane(self) -> tuple:
        """Get/set axis plane size and distance to axis line"""

    @property
    def PointSize(self) -> float:
        """Get/set the origin point size for rendering"""

    @property
    def Scale(self) -> float:
        """Get/set auto scaling factor, 0 to disable"""

    def getDetailPath(self, subname: str, path: object, /):
        """
        getDetailPath(subname,path): return Coin detail and path of an subelement

        subelement: dot separated string reference to the sub element
        pPath: output coin path leading to the returned element detail
                        """

    def getElementPicked(self, pickPoint: object, /):
        """getElementPicked(pickPoint): return the picked subelement"""


# ViewProviderDocumentObjectPy.xml
class ViewProviderDocumentObject(FreeCADGui.ViewProvider):
    """This is the ViewProvider base class"""

    @property
    def Document(self) -> object:
        """Return the document the view provider is part of"""

    @property
    def ForceUpdate(self) -> bool:
        """Reference count to force update visual"""

    @property
    def Object(self) -> object:
        """Set/Get the associated data object"""

    def update(self):
        """Update the view representation of the object"""


# SelectionObjectPy.xml
class SelectionObject(FreeCAD.BaseClass):
    """This class represents selections made by the user. It holds information about the object, document and sub-element of the selection."""

    @property
    def Document(self) -> object:
        """Document of the selected object"""

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
    def PickedPoints(self) -> tuple:
        """Picked points for selection"""

    @property
    def SubElementNames(self) -> tuple:
        """Name of the selected sub-element if any"""

    @property
    def SubObjects(self) -> tuple:
        """Selected sub-element, if any"""

    @property
    def TypeName(self) -> str:
        """Type name of the selected object"""

    def isObjectTypeOf(self, type: str, /):
        """Test for a certain father class.
        isObjectTypeOf(type) -> Bool
        """

    def remove(self):
        """Remove this selection item from the selection.
        remove() -> None
        --
        This object becomes invalid.
        """


# DocumentPy.xml
class Document(FreeCAD.Persistence):
    """This is a Document class"""

    @property
    def ActiveObject(self) -> object:
        """The active object of the document"""

    @ActiveObject.setter
    def ActiveObject(self, value: object): ...

    @property
    def ActiveView(self) -> object:
        """The active view of the document"""

    @ActiveView.setter
    def ActiveView(self, value: object): ...

    @property
    def Document(self) -> object:
        """The related App document to this Gui document"""

    @property
    def EditMode(self) -> int:
        """Current edit mode. Only meaningful when there is a current object in edit"""

    @property
    def EditingTransform(self) -> object:
        """The editing transformation matrix"""

    @property
    def InEditInfo(self) -> object:
        """A tuple(obj,subname,subElement,editMode) of editing object reference, or None if no object is in edit"""

    @property
    def Modified(self) -> bool:
        """Returns True if the document is marked as modified, and False otherwise"""

    @property
    def Transacting(self) -> bool:
        """Indicate whether the document is undoing/redoing"""

    def activeObject(self):
        """deprecated -- use ActiveObject"""

    def activeView(self):
        """deprecated -- use ActiveView"""

    def addAnnotation(self, AnnoName: str, FileName: str, ModName: str = None, /):
        """Add an Inventor object
        addAnnotation(AnnoName,FileName,[ModName]) -> None
        """

    def getInEdit(self):
        """Returns the current object in edit mode or None if there is no such object
        getInEdit() -> Object or None
        """

    def getObject(self, Name: str, /):
        """Return the object with the given name
        getObject(Name) -> Object or None"""

    def hide(self, arg1: str, /):
        """Hide the object
        hide() -> None
        """

    def mdiViewsOfType(self, type: str, /):
        """Return a list if mdi views of a given type
        mdiViewsOfType(type) -> list of MDIView
        """

    def mergeProject(self, filename: str, /):
        """Merges this document with another project file
        mergeProject(filename) -> None
        """

    def resetEdit(self):
        """Reset (end) the current editing.
        resetEdit() -> None
                """

    def scrollToTreeItem(self, ViewObject: FreeCADGui.ViewProviderDocumentObject, /):
        """scroll the tree view to the item of a view object
        scrollToTreeItem(ViewObject) -> None
        """

    def sendMsgToViews(self, msg: str, /):
        """Send a message to all views of the document
        sendMsgToViews(msg) -> None
        """

    @typing.overload
    def setEdit(self, String_Name_ViewProvider_DocumentObject_: str, mod: int = None, subname: str = None, /): ...

    @typing.overload
    def setEdit(self, String_Name_ViewProvider_DocumentObject_: object, mod: int = None, subname: str = None, /):
        """Set the given object in edit mode.
        setEdit([String:Name|ViewProvider|DocumentObject]|,mod,subname=None) -> Bool
        """

    def setPos(self, arg1: str, arg2: FreeCAD.Matrix, /):
        """Set the position
        setPos(matrix) -> None"""

    def show(self, arg1: str, /):
        """Show the object
        show() -> None
        """

    def toggleInSceneGraph(self, ViewObject: FreeCADGui.ViewProvider, /):
        """Add or remove view object from scene graph of all views depending on its canAddToSceneGraph()
        toggleInSceneGraph(ViewObject) -> None
        """

    def toggleTreeItem(self, arg1: FreeCAD.DocumentObject, arg2: int = None, arg3: str = None, /):
        """Change TreeItem of a document object.
        toggleTreeItem(DocObject,[flag=0]) -> None
        --
        flag can be 0:Toggle, 1:Collaps, 2:Expand
        """

    def update(self):
        """Update the view representations of all objects
        update() -> None
        """


# MDIViewPy.cpp
def message(arg1: str, /):
    """message()"""


def fitAll():
    """fitAll()"""


def setActiveObject(arg1: str, arg2: object = None, arg3: str = None, /):
    """setActiveObject(name,object,subname=None)
    add or set a new active object"""


def getActiveObject(arg1: str, arg2: object = None, /):
    """getActiveObject(name,resolve=True)
    returns the active object for the given type"""


# Application.cpp
def subgraphFromObject(arg1: FreeCAD.DocumentObject, /):
    """subgraphFromObject(object) -> Node

    Return the Inventor subgraph to an object"""


def exportSubgraph(arg1: object, arg2: object, arg3: str = None, /):
    """exportSubgraph(Node, File or Buffer, [Format='VRML']) -> None

    Exports the sub-graph in the requested formatThe format string can be VRML or IV"""


def getSoDBVersion():
    """getSoDBVersion() -> String

    Return a text string containing the name
    of the Coin library and version information"""


# View3DPy.cpp
def message(arg1: str, /):
    """message()"""


def fitAll(arg1: float = None, /):
    """fitAll()"""


def viewBottom():
    """viewBottom()"""


def viewFront():
    """viewFront()"""


def viewLeft():
    """viewLeft()"""


def viewRear():
    """viewRear()"""


def viewRight():
    """viewRight()"""


def viewTop():
    """viewTop()"""


def viewAxometric():
    """viewAxonometric()"""


def viewAxonometric():
    """viewAxonometric()"""


def viewIsometric():
    """viewIsometric()"""


def viewDimetric():
    """viewDimetric()"""


def viewTrimetric():
    """viewTrimetric()"""


def viewDefaultOrientation(arg1: str = None, arg2: float = None, /):
    """viewDefaultOrientation(ori_str = '', scale = -1.0): sets camera rotation to a predefined one, 
    and camera position and zoom to show certain amount of model space. 
    ori_string can be 'Top', 'Bottom', 'Front', 'Rear', 'Left', 'Right', 
    'Isometric', 'Dimetric', 'Trimetric', 'Custom'. If empty, the value is 
    fetched from Parameters.
    scale sets distance from camera to origin, and height of the screen in 
    model space, so that a sphere of diameter <scale> fits the height of the
    viewport. If zero, scaling is not done. If negative, the value is 
    fetched from Parameters."""


def viewRotateLeft():
    """viewRotateLeft()"""


def viewRotateRight():
    """viewRotateRight()"""


def zoomIn():
    """zoomIn()"""


def zoomOut():
    """zoomOut()"""


def viewPosition(arg1: FreeCAD.Placement = None, arg2: int = None, arg3: int = None, /):
    """viewPosition()"""


def startAnimating(arg1: float, arg2: float, arg3: float, arg4: float, /):
    """startAnimating()"""


def stopAnimating():
    """stopAnimating()"""


def setAnimationEnabled(arg1: int, /):
    """setAnimationEnabled()"""


def isAnimationEnabled():
    """isAnimationEnabled()"""


def dump(arg1: str, arg2: object = None, /):
    """dump(filename, [onlyVisible=False])"""


def dumpNode(arg1: object, /):
    """dumpNode(node)"""


@typing.overload
def setStereoType(arg1: int, /): ...


@typing.overload
def setStereoType(arg1: str, /):
    """setStereoType()"""


def getStereoType():
    """getStereoType()"""


def listStereoTypes():
    """listStereoTypes()"""


def saveImage(arg1: str, arg2: int = None, arg3: int = None, arg4: str = None, arg5: str = None, arg6: int = None, /):
    """saveImage()"""


def saveVectorGraphic(arg1: str, arg2: int = None, arg3: str = None, /):
    """saveVectorGraphic()"""


def getCamera():
    """getCamera()"""


def getCameraNode():
    """getCameraNode()"""


def getViewDirection():
    """getViewDirection() --> tuple of integers
    returns the direction vector the view is currently pointing at as tuple with xyz values
    """


def setViewDirection(arg1: object, /):
    """setViewDirection(tuple) --> None
    Sets the direction the view is pointing at. The direction must be given as tuple with
    three coordinates xyz"""


def setCamera(arg1: str, /):
    """setCamera()"""


def setCameraOrientation(arg1: object, arg2: bool = None, /):
    """setCameraOrientation()"""


def getCameraOrientation():
    """getCameraOrientation()"""


def getCameraType():
    """getCameraType()"""


@typing.overload
def setCameraType(arg1: int, /): ...


@typing.overload
def setCameraType(arg1: str, /):
    """setCameraType()"""


def listCameraTypes():
    """listCameraTypes()"""


def getCursorPos():
    """getCursorPos() -> tuple of integers

    Return the current cursor position relative to the coordinate system of the
    viewport region.
    """


def getObjectInfo(arg1: object, arg2: float = None, /):
    """getObjectInfo(tuple(int,int), [pick_radius]) -> dictionary or None

    Return a dictionary with the name of document, object and component. The
    dictionary also contains the coordinates of the appropriate 3d point of
    the underlying geometry in the scenegraph.
    If no geometry was found 'None' is returned, instead.
    """


def getObjectsInfo(arg1: object, arg2: float = None, /):
    """getObjectsInfo(tuple(int,int), [pick_radius]) -> dictionary or None

    Does the same as getObjectInfo() but returns a list of dictionaries or None.
    """


def getSize():
    """getSize()"""


def getPoint(arg1: int, arg2: int, /):
    """getPoint(pixel coords (as integer)) -> 3D vector

    Return the according 3D point on the focal plane to the given 2D point (in
    pixel coordinates).
    """


@typing.overload
def getPointOnScreen(arg1: FreeCAD.Vector, /): ...


@typing.overload
def getPointOnScreen(arg1: float, arg2: float, arg3: float, /):
    """getPointOnScreen(3D vector) -> pixel coords (as integer)

    Return the projected 3D point (in pixel coordinates).
    """


def addEventCallback(arg1: str, arg2: object, /):
    """addEventCallback()"""


def removeEventCallback(arg1: str, arg2: object, /):
    """removeEventCallback()"""


def setAnnotation(arg1: str, arg2: str, /):
    """setAnnotation()"""


def removeAnnotation(arg1: str, /):
    """removeAnnotation()"""


def getSceneGraph():
    """getSceneGraph()"""


def getViewer():
    """getViewer()"""


def addEventCallbackPivy(arg1: object, arg2: object, arg3: int = None, /):
    """addEventCallbackPivy()"""


def removeEventCallbackPivy(arg1: object, arg2: object, arg3: int = None, /):
    """removeEventCallbackPivy()"""


def addEventCallbackSWIG(arg1: object, arg2: object, arg3: int = None, /):
    """Deprecated -- use addEventCallbackPivy()"""


def removeEventCallbackSWIG(arg1: object, arg2: object, arg3: int = None, /):
    """Deprecated -- use removeEventCallbackPivy()"""


def setNavigationType(arg1: str, /):
    """setNavigationType()"""


def setAxisCross(arg1: int, /):
    """switch the big axis-cross on and off"""


def hasAxisCross():
    """check if the big axis-cross is on or off()"""


def addDraggerCallback(arg1: object, arg2: str, arg3: object, /):
    """addDraggerCallback(SoDragger, String CallbackType, function)
    Add a DraggerCalback function to the coin node
    Possibles types :
    'addFinishCallback','addStartCallback','addMotionCallback','addValueChangedCallback'
    """


def removeDraggerCallback(arg1: object, arg2: str, arg3: object, /):
    """removeDraggerCallback(SoDragger, String CallbackType, function)
    Remove the DraggerCalback function from the coin node
    Possibles types :
    'addFinishCallback','addStartCallback','addMotionCallback','addValueChangedCallback'
    """


def setActiveObject(arg1: str, arg2: object = None, arg3: str = None, /):
    """setActiveObject(name,object,subname=None)
    add or set a new active object"""


def getActiveObject(arg1: str, arg2: object = None, /):
    """getActiveObject(name,resolve=True)
    returns the active object for the given type"""


def getViewProvidersOfType(arg1: str, /):
    """getViewProvidersOfType(name)
    returns a list of view providers for the given type"""


def redraw():
    """redraw(): renders the scene on screen (useful for animations)"""


def setName(arg1: str, /):
    """setName(str): sets a name to this viewer
    The name sets the widget's windowTitle and appears on the viewer tab"""


def hasClippingPlane():
    """hasClippingPlane(): check whether this clipping plane is active"""


def graphicsView():
    """graphicsView(): Access this view as QGraphicsView"""


def boxZoom(XMin: int, YMin: int, XMax: int, YMax: int):
    """boxZoom()"""


def toggleClippingPlane(toggle: int = None, beforeEditing: object = None, noManip: object = None, pla: FreeCAD.Placement = None):
    """toggleClippingPlane(toggle=-1, beforeEditing=False, noManip=True, pla=App.Placement()
    Toggle a global clipping plane

    toggle: -1 toggle, 1 show, 0 hide
    beforeEditing: whether to insert the clipping node before or after editing root node
    noManip: whether to create a manipulator
    pla: clipping plane placement"""


# WidgetFactory.cpp
def value(arg1: str, arg2: str, /):
    """&PyResource::value"""


def setValue(arg1: str, arg2: str, arg3: object, /):
    """&PyResource::setValue"""


# SplitView3DInventor.cpp
def fitAll():
    """fitAll()"""


def viewBottom():
    """viewBottom()"""


def viewFront():
    """viewFront()"""


def viewLeft():
    """viewLeft()"""


def viewRear():
    """viewRear()"""


def viewRight():
    """viewRight()"""


def viewTop():
    """viewTop()"""


def viewAxometric():
    """viewAxometric()"""


def viewIsometric():
    """viewIsometric()"""


def getViewer(arg1: int, /):
    """getViewer(index)"""


def close():
    """close()"""


# SelectionFilter.cpp
def match():
    """Check if the current selection matches the filter"""


def test(arg1: FreeCAD.DocumentObject, arg2: str = None, /):
    """test(Feature, SubName='')
    Test if a given object is described in the filter.
    If SubName is not empty the sub-element gets also tested."""


def setFilter(arg1: str, /):
    """Set a new selection filter"""


# PythonDebugger.cpp
@typing.overload
def write(arg1: str, /): ...


@typing.overload
def write(arg1: str, /):
    """write to stdout"""


# ApplicationPy.cpp
def activateWorkbench(arg1: str, /):
    """activateWorkbench(string) -> None

    Activate the workbench by name"""


def addWorkbench(arg1: object, /):
    """addWorkbench(string, object) -> None

    Add a workbench under a defined name."""


def removeWorkbench(arg1: str, /):
    """removeWorkbench(string) -> None

    Remove the workbench with name"""


def getWorkbench(arg1: str, /):
    """getWorkbench(string) -> object

    Get the workbench by its name"""


def listWorkbenches():
    """listWorkbenches() -> list

    Show a list of all workbenches"""


def activeWorkbench():
    """activeWorkbench() -> object

    Return the active workbench object"""


def addResourcePath(arg1: str, /):
    """addResourcePath(string) -> None

    Add a new path to the system where to find resource files
    like icons or localization files"""


def addLanguagePath(arg1: str, /):
    """addLanguagePath(string) -> None

    Add a new path to the system where to find language files"""


def addIconPath(arg1: str, /):
    """addIconPath(string) -> None

    Add a new path to the system where to find icon files"""


def addIcon(arg1: str, arg2: str, arg3: str = None, /):
    """addIcon(string, string or list) -> None

    Add an icon as file name or in XPM format to the system"""


def getIcon(arg1: str, /):
    """getIcon(string) -> QIcon

    Get an icon in the system"""


def isIconCached(arg1: str, /):
    """isIconCached(String) -> Bool

    Check if an icon with the given name is cached"""


def getMainWindow():
    """getMainWindow() -> QMainWindow

    Return the main window instance"""


def updateGui():
    """updateGui() -> None

    Update the main window and all its windows"""


def updateLocale():
    """updateLocale() -> None

    Update the localization"""


def getLocale():
    """getLocale() -> string

    Returns the locale currently used by FreeCAD"""


def setLocale(arg1: str, /):
    """getLocale(string) -> None

    Sets the locale used by FreeCAD. You can set it by
    top-level domain (e.g. \"de\") or the language name (e.g. \"German\")"""


def supportedLocales():
    """supportedLocales() -> dict

    Returns a dict of all supported languages/top-level domains"""


def createDialog(arg1: str, /):
    """createDialog(string) -- Open a UI file"""


@typing.overload
def addPreferencePage(arg1: str, arg2: str, /): ...


@typing.overload
def addPreferencePage(arg1: type, arg2: str, /): ...


@typing.overload
def addPreferencePage(arg1: type, arg2: str, /):
    """addPreferencePage(string,string) -- Add a UI form to the
    preferences dialog. The first argument specifies the file nameand the second specifies the group name"""


def addCommand(arg1: str, arg2: object, arg3: str = None, /):
    """addCommand(string, object) -> None

    Add a command object"""


def runCommand(arg1: str, arg2: int = None, /):
    """runCommand(string) -> None

    Run command with name"""


def SendMsgToActiveView(arg1: str, arg2: bool = None, /):
    """deprecated -- use class View"""


def sendMsgToFocusView(arg1: str, arg2: bool = None, /):
    """send message to the focused view"""


def hide(arg1: str, /):
    """deprecated"""


def show(arg1: str, /):
    """deprecated"""


def hideObject(arg1: FreeCAD.DocumentObject, /):
    """hideObject(object) -> None

    Hide the view provider to the given object"""


def showObject(arg1: FreeCAD.DocumentObject, /):
    """showObject(object) -> None

    Show the view provider to the given object"""


def open(arg1: str, /):
    """Open a macro, Inventor or VRML file"""


def insert(arg1: str, arg2: str = None, /):
    """Open a macro, Inventor or VRML file"""


def export(arg1: object, arg2: str, /):
    """save scene to Inventor or VRML file"""


def activeDocument():
    """activeDocument() -> object or None

    Return the active document or None if no one exists"""


@typing.overload
def setActiveDocument(arg1: str, /): ...


@typing.overload
def setActiveDocument(arg1: FreeCAD.Document, /):
    """setActiveDocument(string or App.Document) -> None

    Activate the specified document"""


def activeView(arg1: str = None, /):
    """activeView(typename=None) -> object or None

    Return the active view of the active document or None if no one exists"""


def activateView(arg1: str, arg2: bool, /):
    """activateView(type)

    Activate a view of the given type of the active document"""


def editDocument():
    """editDocument() -> object or None

    Return the current editing document or None if no one exists"""


@typing.overload
def getDocument(arg1: str, /): ...


@typing.overload
def getDocument(arg1: FreeCAD.Document, /):
    """getDocument(string) -> object

    Get a document by its name"""


def doCommand(arg1: str, /):
    """doCommand(string) -> None

    Prints the given string in the python console and runs it"""


def doCommandGui(arg1: str, /):
    """doCommandGui(string) -> None

    Prints the given string in the python console and runs it but doesn't record it in macros"""


def addModule(arg1: str, /):
    """addModule(string) -> None

    Prints the given module import only once in the macro recording"""


def showDownloads():
    """showDownloads() -> None

    Shows the downloads manager window"""


def showPreferences(arg1: str = None, arg2: int = None, /):
    """showPreferences([string,int]) -> None

    Shows the preferences window. If string and int are provided, the given page index in the given group is shown."""


def createViewer(arg1: int = None, arg2: str = None, /):
    """createViewer([int]) -> View3DInventor/SplitView3DInventor

    shows and returns a viewer. If the integer argument is given and > 1: -> splitViewer"""


def getMarkerIndex(arg1: str = None, arg2: int = None, /):
    """Get marker index according to marker size setting"""


def addDocumentObserver(arg1: object, /):
    """addDocumentObserver() -> None

    Add an observer to get notified about changes on documents."""


def removeDocumentObserver(arg1: object, /):
    """removeDocumentObserver() -> None

    Remove an added document observer."""


def reload(arg1: str, /):
    """reload(name) -> doc

    Reload a partial opened document"""


def loadFile(arg1: str, arg2: str = None, /):
    """loadFile(string=filename,[string=module]) -> None

    Loads an arbitrary file by delegating to the given Python module:
    * If no module is given it will be determined by the file extension.
    * If more than one module can load a file the first one will be taken.
    * If no module exists to load the file an exception will be raised."""


def coinRemoveAllChildren(arg1: object, /):
    """Remove all children from a group node"""


# ExpressionBindingPy.cpp
def bind(arg1: FreeCAD.DocumentObject, arg2: str, /):
    """Bind with an expression"""


def isBound():
    """Check if already bound with an expression"""


def apply(arg1: str, /):
    """apply"""


def hasExpression():
    """hasExpression"""


def autoApply():
    """autoApply"""


def setAutoApply(arg1: bool, /):
    """setAutoApply"""


# View3DViewerPy.cpp
def getSoRenderManager():
    """getSoRenderManager() -> SoRenderManager
    Returns the render manager which is used to handle everything related to
    rendering the scene graph. It can be used to get full control over the
    render process
    """


def getSoEventManager():
    """getSoEventManager() -> SoEventManager
    Returns the event manager which is used to handle everything event related in
    the viewer. It can be used to change the event processing. This must however be
    done very carefully to not change the user interaction in an unpredictable manner.
    """


def getSceneGraph():
    """getSceneGraph() -> SoNode"""


def setSceneGraph(arg1: object, /):
    """setSceneGraph(SoNode)"""


def seekToPoint(arg1: object, /):
    """seekToPoint(tuple) -> None
    Initiate a seek action towards the 3D intersection of the scene and the
    ray from the screen coordinate's point and in the same direction as the
    camera is pointing. If the tuple has two entries it is interpreted as the
    screen coordinates xy and the intersection point with the scene is
    calculated. If three entries are given it is interpreted as the intersection
    point xyz and the seek is done towards this point"""


def setFocalDistance(arg1: float, /):
    """setFocalDistance(float) -> None
    """


def getFocalDistance():
    """getFocalDistance() -> float
    """


def getPoint(arg1: int, arg2: int, /):
    """getPoint(x, y) -> Base::Vector(x,y,z)"""


def getPickRadius():
    """getPickRadius(): returns radius of confusion in pixels for picking objects on screen (selection)."""


def setPickRadius(arg1: float, /):
    """setPickRadius(new_radius): sets radius of confusion in pixels for picking objects on screen (selection)."""


def setupEditingRoot(arg1: object = None, arg2: FreeCAD.Matrix = None, /):
    """setupEditingRoot(matrix=None): setup the editing ViewProvider's root node.
    All child coin nodes of the current editing ViewProvider will be transferred to
    an internal editing node of this viewer, with a new transformation node specified
    by 'matrix'. All ViewProviderLink to the editing ViewProvider will be temporary
    hidden. Call resetEditingRoot() to restore everything back to normal"""


def resetEditingRoot(arg1: object = None, /):
    """resetEditingRoot(updateLinks=True): restore the editing ViewProvider's root node"""


def setBackgroundColor(arg1: float, arg2: float, arg3: float, /):
    """setBackgroundColor(r,g,b): sets the background color of the current viewer."""


def setRedirectToSceneGraph(arg1: bool, /):
    """setRedirectToSceneGraph(bool): enables or disables to redirect events directly to the scene graph."""


def isRedirectedToSceneGraph():
    """isRedirectedToSceneGraph() -> bool: check whether event redirection is enabled."""


def setEnabledNaviCube(arg1: bool, /):
    """setEnabledNaviCube(bool): enables or disables the navi cube of the viewer."""


def isEnabledNaviCube():
    """isEnabledNaviCube() -> bool: check whether the navi cube is enabled."""


def setNaviCubeCorner(arg1: int, /):
    """setNaviCubeCorner(int): sets the corner where to show the navi cube:
    0=top left, 1=top right, 2=bottom left, 3=bottom right"""


# TaskDialogPython.cpp
def showDialog(arg1: object, /):
    """show the given dialog in the task panel
    showDialog(dialog)
    --
    if a task is already active a RuntimeError is raised"""


def activeDialog():
    """check if a dialog is active in the task panel
    activeDialog() --> bool"""


def closeDialog():
    """close the active dialog
    closeDialog()"""


def addTaskWatcher(arg1: object, /):
    """install a (list of) TaskWatcher
    addTaskWatcher(TaskWatcher | list)"""


def clearTaskWatcher():
    """remove all TaskWatchers
    clearTaskWatcher()"""


def isAllowedAlterDocument():
    """return the permission to alter the current Document
    isAllowedAlterDocument() --> bool"""


def isAllowedAlterView():
    """return the permission to alter the current View
    isAllowedAlterView() --> bool"""


def isAllowedAlterSelection():
    """return the permission to alter the current Selection
    isAllowedAlterSelection() --> bool"""


def showTaskView():
    """show the Task panel
    showTaskView()"""


def showModelView():
    """show the Model panel
    showModelView()"""


Workbench: FreeCADGui.Workbench
ActiveDocument: Document
