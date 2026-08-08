# Stub for maya.OpenMayaUI - OM1, signatures from Maya 2024 C++ API reference
from typing import Any, overload

from maya.OpenMaya import MAngle
from maya.OpenMaya import MCallbackIdArray
from maya.OpenMaya import MColor
from maya.OpenMaya import MDagPath
from maya.OpenMaya import MDagPathArray
from maya.OpenMaya import MDoubleArray
from maya.OpenMaya import MEulerRotation
from maya.OpenMayaMPx import MExternalContentInfoTable
from maya.OpenMayaMPx import MExternalContentLocationTable
from maya.OpenMaya import MImage
from maya.OpenMaya import MIntArray
from maya.OpenMaya import MMatrix
from maya.OpenMaya import MObject
from maya.OpenMaya import MObjectArray
from maya.OpenMaya import MPlug
from maya.OpenMaya import MPlugArray
from maya.OpenMaya import MPoint
from maya.OpenMayaMPx import MPxContext
from maya.OpenMayaMPx import MPxGlBuffer
from maya.OpenMayaMPx import MPxSurfaceShapeUI
from maya.OpenMaya import MQuaternion
from maya.OpenMaya import MSelectionList
from maya.OpenMaya import MSelectionMask
from maya.OpenMaya import MTransformationMatrix
from maya.OpenMaya import MTypeId
from maya.OpenMaya import MUuid
from maya.OpenMaya import MVector

class MStatus:
    ...

class M3dView:
    kActive: Any
    kActiveAffected: Any
    kActiveColors: Any
    kActiveComponent: Any
    kActiveTemplate: Any
    kBackgroundColor: Any
    kBoundingBox: Any
    kCenter: Any
    kDefaultQualityRenderer: Any
    kDepth_8: Any
    kDepth_Float: Any
    kDisplayCVs: Any
    kDisplayCameras: Any
    kDisplayDeformers: Any
    kDisplayDimensions: Any
    kDisplayDynamicConstraints: Any
    kDisplayDynamics: Any
    kDisplayEverything: Any
    kDisplayFluids: Any
    kDisplayFollicles: Any
    kDisplayGrid: Any
    kDisplayHairSystems: Any
    kDisplayHulls: Any
    kDisplayIkHandles: Any
    kDisplayImagePlane: Any
    kDisplayJoints: Any
    kDisplayLights: Any
    kDisplayLocators: Any
    kDisplayManipulators: Any
    kDisplayMeshes: Any
    kDisplayNCloths: Any
    kDisplayNParticles: Any
    kDisplayNRigids: Any
    kDisplayNurbsCurves: Any
    kDisplayNurbsSurfaces: Any
    kDisplayParticleInstancers: Any
    kDisplayPivots: Any
    kDisplayPlanes: Any
    kDisplaySelectHandles: Any
    kDisplayStrokes: Any
    kDisplaySubdivSurfaces: Any
    kDisplayTextures: Any
    kDormant: Any
    kDormantColors: Any
    kExcludeMotionTrails: Any
    kExcludePluginShapes: Any
    kExternalRenderer: Any
    kFlatShaded: Any
    kGouraudShaded: Any
    kHighQualityRenderer: Any
    kHilite: Any
    kIntermediateObject: Any
    kInvisible: Any
    kLead: Any
    kLeft: Any
    kLightActive: Any
    kLightAll: Any
    kLightDefault: Any
    kLightNone: Any
    kLightSelected: Any
    kLive: Any
    kNoStatus: Any
    kPoints: Any
    kRight: Any
    kStippleDashed: Any
    kStippleNone: Any
    kTemplate: Any
    kTemplateColor: Any
    kUnused1: Any
    kViewport2Renderer: Any
    kWireFrame: Any
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @staticmethod
    def active3dView() -> M3dView:
        """Returns the active view in the form of a class ( M3dView ) that can operate on it."""
    @staticmethod
    def activeAffectedColor() -> MColor:
        """Returns the color for active affected objects."""
    @staticmethod
    def activeTemplateColor() -> MColor:
        """Returns the color for active template objects."""
    @staticmethod
    def applicationShell() -> Any:
        """Returns the native handle for Maya's main window."""
    def assign(self, other: M3dView) -> None: ...
    @staticmethod
    def backgroundColor() -> MColor:
        """Returns the value of the background color."""
    @staticmethod
    def backgroundColorBottom() -> MColor:
        """Returns the value of the background gradient bottom color."""
    @staticmethod
    def backgroundColorTop() -> MColor:
        """Returns the value of the background gradient top color."""
    def beginGL(self) -> MStatus:
        """Deprecated in 2019.0"""
    def beginProjMatrixOverride(self, projectionMatrix: MMatrix) -> MStatus:
        """Deprecated in 2019.0"""
    def beginSelect(self, buffer: Any = None, size: Any = 0) -> None:
        """Start selecting."""
    def beginXorDrawing(self, lineWidth: float, stipplePattern: Any, lineColor: MColor, drawOrthographic: bool = True, disableDepthTesting: bool = True) -> MStatus:
        """Setup the context for exclusive-or (XOR) drawing."""
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def colorAtIndex(self, index: int, table: Any) -> MColor:
        """Returns the value of the color at the given index in the application's color table."""
    def colorMask(self, r: bool, g: bool, b: bool, a: bool) -> MStatus:
        """Deprecated in 2019.0"""
    def deviceContext(self, *args: Any, **kwargs: Any) -> Any: ...
    def devicePixelRatio(self) -> float:
        """Introduced in 2023.0"""
    def disallowPolygonOffset(self) -> bool:
        """Returns the current state of the disallow polygon offset bit."""
    def display(self) -> Any:
        """Mac OS X and Windows."""
    @staticmethod
    def displayStatus(path: MDagPath) -> Any:
        """Returns the display status of the given DAG path."""
    def displayStyle(self) -> Any:
        """Return the display style for this 3d view."""
    def drawText(self, text: str, position: MPoint, arg: Any) -> MStatus:
        """Deprecated in 2019.0"""
    def endGL(self) -> MStatus:
        """Deprecated in 2019.0"""
    def endProjMatrixOverride(self) -> MStatus:
        """Deprecated in 2019.0"""
    def endSelect(self) -> Any:
        """Finish a selection sequence."""
    def endXorDrawing(self) -> MStatus:
        """Reset the context to non-exclusive-or (non-XOR) screen drawing."""
    def filteredObjectList(self, list: MSelectionList) -> MStatus:
        """Returns a selection list containing all of the objects that remain after filtering is applied to the view."""
    @staticmethod
    def get3dView(index: int, view: M3dView) -> MStatus:
        """Returns the 3D view at the given index."""
    def getCamera(self, camera: MDagPath) -> MStatus:
        """Get the camera for this view."""
    def getColorIndexAndTable(self, glindex: int, index: int, table: Any) -> MStatus:
        """Returns the color table and index representing the given OpenGL color-index value."""
    def getLightCount(self, count: int, visible: bool = True) -> MStatus:
        """Get the number of lights for the view."""
    def getLightIndex(self, lightNumber: int, lightIndex: int) -> MStatus:
        """Get the internal light index for a given light number."""
    def getLightPath(self, lightNumber: int, light: MDagPath) -> MStatus:
        """Get the path to a certain light."""
    def getLightingMode(self, mode: Any) -> MStatus:
        """Get the current lighting mode for the view."""
    @staticmethod
    def getM3dViewFromModelEditor(modelPaneName: str, view: M3dView) -> MStatus:
        """Given the name of a model editor, get the M3dView used by that editor."""
    @staticmethod
    def getM3dViewFromModelPanel(modelPaneName: str, view: M3dView) -> MStatus:
        """Given the name of a model panel, get the M3dView used by that panel."""
    def getRendererName(self) -> Any:
        """Get the name of the current renderer being used for drawing to this view."""
    def getScreenPosition(self, x: int, y: int) -> None:
        """Returns the current position of this view window in screen coordinates."""
    @staticmethod
    def hiliteColor() -> MColor:
        """Returns the color for hilited objects."""
    def initNames(self) -> None:
        """Reset the name stack."""
    @staticmethod
    def isBackgroundGradient() -> bool:
        """Returns whether a gradient is being used as the background color."""
    def isLightVisible(self, lightNumber: int, visible: bool) -> MStatus:
        """Find out if a light is visible in the view."""
    def isShadeActiveOnly(self) -> bool:
        """Returns true if this view's display style is shaded for objects that are active and wireframe otherwise."""
    def isVisible(self) -> bool:
        """Returns true if this viewport is visible."""
    @staticmethod
    def leadColor() -> MColor:
        """Returns the color for lead objects."""
    @staticmethod
    def liveColor() -> MColor:
        """Returns the color for live objects."""
    def loadName(self, name: Any) -> None:
        """Replace the top of the name stack with the given name."""
    def makeSharedContextCurrent(self) -> MStatus:
        """makes the shared context current."""
    def modelViewMatrix(self, modelViewMatrix: MMatrix) -> MStatus:
        """Returns the modelview matrix currently being used by OpenGL in the current view."""
    def multipleDrawEnabled(self) -> bool:
        """This method returns the multiple draw enable state for this view."""
    def multipleDrawPassCount(self) -> int:
        """Deprecated in 2019.0"""
    def numActiveColors(self) -> int:
        """Returns the number of active object colors in the internal application color table."""
    def numDormantColors(self) -> int:
        """Returns the number of dormant object colors in the internal application color table."""
    def numUserDefinedColors(self) -> int:
        """Returns the number of user defined colors in the internal application color table."""
    @staticmethod
    def numberOf3dViews() -> int:
        """Returns the number of 3D views currently in existance."""
    def objectDisplay(self) -> int:
        """Returns a display object mask that indicates which object types are drawn in the current view."""
    def objectListFilterName(self) -> str:
        """Get the current object list filter name."""
    def playblastPortHeight(self) -> int:
        """Returns the port height of current playblast."""
    def playblastPortWidth(self) -> int:
        """Returns the port width of current playblast."""
    def pluginObjectDisplay(self, pluginDisplayFilter: str) -> bool:
        """Returns true if the plugin display filter specified by the pluginDisplayFilter is enabled in the current view."""
    def popName(self) -> None:
        """Removes the top of the name stack."""
    def popViewport(self) -> MStatus:
        """Pop the current viewport off of the viewport stack."""
    def portHeight(self) -> int:
        """Returns the height of the current viewport."""
    def portWidth(self) -> int:
        """Returns the width of the current viewport."""
    def projectionMatrix(self, projectionMatrix: MMatrix) -> MStatus:
        """Returns the projection matrix currently being used by OpenGL in the current view."""
    def pushName(self, name: Any) -> None:
        """Push a new name on the name stack."""
    def pushViewport(self, x: int, y: int, width: int, height: int) -> MStatus:
        """Set the current viewport dimensions."""
    def readBufferTo2dTexture(self, x: Any, y: Any, width: int, height: int) -> MStatus:
        """Deprecated in 2019.0"""
    def readColorBuffer(self, image: MImage, readRGBA: bool = False) -> MStatus:
        """Deprecated in 2019.0"""
    def readDepthMap(self, x: Any, y: Any, width: int, height: int, bufferPtr: Any, depthMapPrecision: Any) -> MStatus:
        """Deprecated in 2019.0"""
    @staticmethod
    def referenceLayerColor() -> MColor:
        """Returns the color for objects which belong to a display layer whose display type is Reference."""
    @overload
    def refresh(self, all: bool = False, force: bool = False) -> MStatus: ...
    @overload
    def refresh(self, all: bool, force: bool, offscreen: bool) -> MStatus: ...
    @overload
    def refresh(self, buffer: MPxGlBuffer) -> MStatus: ...
    @overload
    def refresh(self, buffer: MPxGlBuffer, offscreen: bool) -> MStatus: ...
    @overload
    def refresh(self, buffer: MPxGlBuffer, offscreen: bool, projectionMatrix: MMatrix) -> MStatus:
        """Refresh the this view."""
    def renderOverrideName(self) -> str:
        """Get the current render override name."""
    def rendererString(self) -> str:
        """Get the string name of the current renderer being used for drawing to this view."""
    def scheduleRefresh(self) -> MStatus:
        """Schedule a forced refresh for this 3d-view."""
    @staticmethod
    def scheduleRefreshAllViews() -> MStatus:
        """Schedule a forced refresh for all 3d-views."""
    def selectMode(self) -> bool:
        """Tells if this M3dView is in selection mode."""
    def setCamera(self, camera: MDagPath) -> MStatus:
        """Set the camera for this view."""
    def setColorMask(self, r: bool, g: bool, b: bool, a: bool) -> MStatus:
        """Deprecated in 2019.0"""
    def setDisallowPolygonOffset(self, v: bool) -> MStatus:
        """Certain Maya actions will use glPolygonOffset to offset polygons drawing into the depth buffer."""
    def setDisplayStyle(self, style: Any, activeOnly: bool = False) -> MStatus:
        """Sets the display style for this view."""
    @overload
    def setDrawColor(self, index: int, table: Any) -> MStatus: ...
    @overload
    def setDrawColor(self, color: MColor) -> MStatus:
        """Deprecated in 2015.0"""
    def setDrawColorAndAlpha(self, color: MColor) -> MStatus:
        """Deprecated in 2015.0"""
    def setMultipleDrawEnable(self, enable: bool) -> None:
        """Deprecated in 2019.0"""
    def setMultipleDrawPassCount(self, count: int) -> None:
        """Deprecated in 2019.0"""
    def setObjectDisplay(self, displayMask: int) -> MStatus:
        """It is assumed in the below accessor methods that M3dView::DisplayObjects enum values can be cast to and from TexcludeObj"""
    def setObjectListFilterName(self, name: str) -> MStatus:
        """Set the name of the object list filter ( MObjectListFilter ) to use."""
    def setPluginObjectDisplay(self, pluginDisplayFilter: str, on: bool) -> MStatus:
        """Enables or disables a user-defined display filter (i.e."""
    def setRenderOverrideName(self, name: str) -> MStatus:
        """Set the name of a render override ( MHWRender::MRenderOverride ) to use."""
    def setShowObjectFilterNameInHUD(self, show: bool) -> MStatus:
        """Sets whether or not to display the object filter UI name in the heads up display when an object filter is active."""
    def setShowViewSelectedChildren(self, arg: Any) -> MStatus:
        """This method changes the way that view selected works."""
    def setUserDefinedColor(self, index: int, color: MColor) -> MStatus:
        """Sets the user defined color at the given index."""
    def setViewSelectedPrefix(self, prefix: str) -> MStatus:
        """Sets the prefix for the camera name as displayed in the heads up display when view selected is enabled."""
    def showObjectFilterNameInHUD(self) -> bool:
        """Returns whether the object filter UI name is shown in the heads up display when an object filter is active."""
    def showViewSelectedChildren(self) -> bool:
        """Returns turn if view selected shows all of the children of the obejcts that are flagged for view selected."""
    @staticmethod
    def templateColor() -> MColor:
        """Returns the value of the template color."""
    def textureMode(self) -> bool:
        """Tells if this M3dView is in texture mode."""
    def twoSidedLighting(self) -> bool:
        """Return true if the Two-sided lighting mode is enabled."""
    def updateViewingParameters(self) -> MStatus:
        """This method tells the camera to set the view's transformation matrix."""
    def userDefinedColorIndex(self, index: int) -> int:
        """Returns the index for the given user-defined color."""
    def usingDefaultMaterial(self) -> bool:
        """Returns true if the view is currently displaying objects using the default material."""
    def usingMipmappedTextures(self) -> bool:
        """Returns if the view is using mipmapped texture display."""
    def viewIsFiltered(self) -> bool:
        """Returns the state of view filtering for this view."""
    def viewSelectedPrefix(self) -> str:
        """Returns the Returns the prefix used when displaying the camera name in the heads up display when view selected in on."""
    def viewToObjectSpace(self, x_pos: Any, y_pos: Any, localMatrixInverse: MMatrix, oPt: MPoint, oVector: MVector) -> MStatus:
        """Takes a point in port coordinates and returns a corresponding ray in object coordinates."""
    @overload
    def viewToWorld(self, x_pos: Any, y_pos: Any, worldPt: MPoint, worldVector: MVector) -> MStatus: ...
    @overload
    def viewToWorld(self, x_pos: Any, y_pos: Any, nearClipPt: MPoint, farClipPt: MPoint) -> MStatus:
        """Takes a point in port coordinates and returns a corresponding ray in world coordinates."""
    def viewport(self, x: int, y: int, width: int, height: int) -> MStatus:
        """Get the current viewport dimensions."""
    def widget(self) -> Any:
        """Returns the view's Qt widget."""
    def window(self) -> Any:
        """Returns the native window for this view."""
    def wireframeOnShaded(self) -> bool:
        """Return whether we draw wireframe in shaded mode."""
    def wireframeOnlyInShadedMode(self) -> bool:
        """Return whether we are in shaded mode, but that only non shaded drawing should occur (wireframe)."""
    def worldToView(self, worldPt: MPoint, x_pos: Any, y_pos: Any) -> bool:
        """converts a point in world space to port space."""
    def writeColorBuffer(self, image: MImage, x: Any = 0, y: Any = 0) -> MStatus:
        """Deprecated in 2019.0"""
    def xray(self) -> bool:
        """Return true if the X-Ray mode is enabled."""
    def xrayJoints(self) -> bool:
        """Return true if the X-Ray Joints mode is enabled."""

class MCursor:
    crossHairCursor: Any
    defaultCursor: Any
    doubleCrossHairCursor: Any
    editCursor: Any
    handCursor: Any
    pencilCursor: Any
    textBeamCursor: Any
    thisown: Any
    @overload
    def __init__(self, width: Any, height: Any, hotSpotX: Any, hotSpotY: Any, bits: Any, mask: Any) -> None: ...
    @overload
    def __init__(self, other: MCursor) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self) -> None:
        """Class constructor."""
    def assign(self, other: MCursor) -> None: ...

class MDeviceChannel:
    thisown: Any
    def __init__(self, arg: Any, arg_: Any = -1) -> None:
        """Constructor."""
    def axisIndex(self) -> int:
        """Returns the device state index corresponding to this device channel."""
    def childByIndex(self, arg: Any) -> MDeviceChannel:
        """Return the specified child of this channel."""
    def hasChildren(self) -> bool:
        """Determine whether this channel has children."""
    def longName(self) -> str:
        """Return the long name of the channel."""
    def name(self) -> str:
        """Return the short name of the channel."""
    def numChildren(self) -> int:
        """Return the number of children of this channel."""
    def parent(self) -> MDeviceChannel:
        """Return the parent of this channel."""

class MDeviceState:
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @overload
    def buttonState(self, button: Any) -> bool: ...
    @overload
    def buttonState(self, buttonName: str) -> bool:
        """Returns the state of the given button."""
    @overload
    def devicePosition(self, axis: Any) -> int: ...
    @overload
    def devicePosition(self, axisName: str) -> int:
        """Returns the position of the device for the specified axis."""
    def isNull(self) -> bool:
        """Returns true if this device state is NULL;."""
    def maxAxis(self) -> int:
        """Return the value of the axis with the largest value."""
    @overload
    def setButtonState(self, state: bool, button: Any) -> None: ...
    @overload
    def setButtonState(self, state: bool, buttonName: str) -> None:
        """Set the state of the specified button."""
    @overload
    def setDevicePosition(self, position: int, axis: Any) -> None: ...
    @overload
    def setDevicePosition(self, position: int, axisName: str) -> None:
        """Sets the position of the device for the specified axis."""

class MDrawData:
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, in_: MDrawData) -> None: ...
    @overload
    def __init__(self) -> None:
        """Constructor."""
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def geometry(self) -> None:
        """Returns the geometry associated with this draw data object."""

class MDrawInfo:
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, in_: MDrawInfo) -> None:
        """Constructor."""
    def canDrawComponent(self, isDisplayOn: bool, compMask: MSelectionMask) -> bool:
        """Convenience method to test if components specified by the given mask can be drawn."""
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def completelyInside(self) -> bool:
        """Returns true if the object being drawn is inside the viewing frustum."""
    def displayStatus(self) -> int:
        """Returns the status of the object to draw."""
    def displayStyle(self) -> int:
        """The display appearance."""
    def getPrototype(self, drawHandler: MPxSurfaceShapeUI) -> MDrawRequest:
        """This method creates a draw request based on the current draw state."""
    def inSelect(self) -> bool:
        """Returns true if this is called from within the select method of MPxSurfaceShapeUI ."""
    def inUserInteraction(self) -> bool:
        """Returns true during any interactive refresh, as when user is interacting with the scene in any way including camera chan"""
    def inclusiveMatrix(self) -> MMatrix:
        """Returns the world space inclusive matrix."""
    def multiPath(self) -> MDagPath:
        """Returns the path to the object to be drawn."""
    def objectDisplayStatus(self, DisplayObjects: int) -> bool:
        """Determines whether the specified objects are allowed to be displayed."""
    def pluginObjectDisplayStatus(self, pluginDisplayFilter: str) -> bool:
        """Determines whether the specified plugin object is allowed to be displayed."""
    def projectionMatrix(self) -> MMatrix:
        """Returns the camera*projection matrix."""
    def setMultiPath(self) -> None:
        """Sets the path of the object to be drawn."""
    def userChangingViewContext(self) -> bool:
        """Returns true during any interactive refresh, as when user is changing the view using view context tools such as tumble, """
    def view(self) -> M3dView:
        """Returns the view that the drawing will take place."""

class MDrawRequest:
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, in_: MDrawRequest) -> None: ...
    @overload
    def __init__(self) -> None:
        """Constructor."""
    def assign(self, other: MDrawRequest) -> None: ...
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @overload
    def color(self, table: int) -> int: ...
    @overload
    def color(self) -> MColor:
        """Returns the wireframe display color."""
    def component(self) -> MObject:
        """An optional component."""
    def displayCullOpposite(self) -> bool:
        """Returns the state of the culling flag for the object."""
    def displayCulling(self) -> bool:
        """Returns the state of the culling flag for the object."""
    def displayStatus(self) -> int:
        """Return the state of object (active, dormant, etc.)."""
    def displayStyle(self) -> int:
        """Returns how the object should be drawn (wireframe, shaded, etc.)."""
    def drawData(self) -> MDrawData:
        """Returns the object specific draw data."""
    def drawLast(self) -> bool:
        """Returns the order in which this object will be drawn."""
    def isTransparent(self) -> bool:
        """Returns the transparency state of the object."""
    def material(self) -> MMaterial:
        """Returns the shaded material."""
    def matrix(self) -> MMatrix:
        """Returns the draw matrix."""
    def multiPath(self) -> MDagPath:
        """Returns the path to the object to be drawn."""
    @overload
    def setColor(self, arg: Any, table: int) -> None: ...
    @overload
    def setColor(self, color: MColor) -> None:
        """Sets the wireframe display color."""
    def setComponent(self) -> None:
        """Set a component to be drawn."""
    def setDisplayCullOpposite(self, arg: Any) -> None:
        """Sets the state of the culling flag for the object."""
    def setDisplayCulling(self, arg: Any) -> None:
        """Sets the state of the culling flag for the object."""
    def setDisplayStatus(self, DisplayStatus: int) -> None:
        """Set the state of object (active, dormant, etc.)."""
    def setDisplayStyle(self, DisplayStyle: int) -> None:
        """Sets how the object should be drawn (wireframe, shaded, etc.)."""
    def setDrawData(self) -> None:
        """Set the object specific draw data."""
    def setDrawLast(self, arg: Any) -> None:
        """Specifies the order in which this object will be drawn."""
    def setIsTransparent(self, arg: Any) -> None:
        """Sets the transparency state of the object."""
    def setMaterial(self) -> None:
        """Returns the shaded material."""
    def setMatrix(self) -> None:
        """Set the draw matrix."""
    def setMultiPath(self) -> None:
        """Sets the path to the object to be drawn."""
    def setToken(self, arg: Any) -> None:
        """Set the user-defined draw token for this request."""
    def setView(self) -> None:
        """Sets the view where drawing will be done."""
    def token(self) -> int:
        """Returns the user-defined draw token for this request."""
    def view(self) -> M3dView:
        """Returns the view where drawing will be done."""

class MDrawRequestQueue:
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self) -> None:
        """Constructor."""
    def add(self) -> None:
        """Adds a draw request to the draw queue."""
    def assign(self, other: MDrawRequestQueue) -> None: ...
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def isEmpty(self) -> bool:
        """Returns true if the queu is empty."""
    def remove(self) -> MDrawRequest:
        """Removes a draw request from the draw queue."""

class MDrawTraversal:
    kActiveItem: Any
    kTemplateItem: Any
    thisown: Any
    def __init__(self) -> None:
        """Default constructor."""
    def enableFiltering(self, val: bool) -> None:
        """Sets whether to use enable usage of the filterNode() method to perform custom filtering."""
    def filterNode(self, traversalItem: MDagPath) -> bool:
        """Method to allow filtering during traversal."""
    def filteringEnabled(self) -> bool:
        """Tells whether custom filtering has been enabled."""
    def frustumValid(self) -> bool:
        """Returns whether the current frustum set is valid or not."""
    def itemHasStatus(self, itemNumber: int, test: int) -> bool:
        """Test the display status for a given item in the list of found items after traversal."""
    def itemPath(self, itemNumber: int, path: MDagPath) -> MStatus:
        """Get the path for a given item in the list of found items after traversal."""
    def leafLevelCulling(self) -> bool:
        """Returns whether the current cull algorithm will cull at the leaf levels, or perform hierarchical culling."""
    def numberOfItems(self) -> int:
        """Return the number of items found after traversal."""
    @overload
    def setFrustum(self, cameraPath: MDagPath, portWidth: int, portHeight: int) -> MStatus: ...
    @overload
    def setFrustum(self, left: float, right: float, bottom: float, top: float, nearpt: float, farpt: float, worldXform: MMatrix) -> MStatus: ...
    @overload
    def setFrustum(self, nearBottomLeft: MPoint, nearBottomRight: MPoint, nearTopLeft: MPoint, nearTopRight: MPoint, farBottomLeft: MPoint, farBottomRight: MPoint, farTopLeft: MPoint, farTopRight: MPoint, worldXform: MMatrix) -> MStatus:
        """Set the frustum to cull with."""
    def setLeafLevelCulling(self, cullAtLeafLevel: bool) -> None:
        """Set whether to cull at the leaf levels, or perform hierarchical culling."""
    def setOrthoFrustum(self, left: float, right: float, bottom: float, top: float, nearpt: float, farpt: float, worldXform: MMatrix) -> MStatus:
        """Set up an orthographic view frustum to cull with."""
    def setPerspFrustum(self, fovX: float, aspectXY: float, nearDist: float, farDist: float, worldXform: MMatrix) -> MStatus:
        """Set up an perspective view frustum to cull with."""
    def traverse(self) -> MStatus:
        """Perform traversal of the current scene from the root of the dag hierarchy."""

class MEvent:
    controlKey: Any
    kLeftMouse: Any
    kMiddleMouse: Any
    shiftKey: Any
    thisown: Any
    def __init__(self) -> None:
        """Constructor."""
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def getPosition(self, x_pos: Any, y_pos: Any) -> MStatus:
        """Get the location of the event in view co-ordinates."""
    def getWindowPosition(self, x_pos: Any, y_pos: Any) -> MStatus:
        """This routine is used by responders to query the position of the pointer when the event occurred."""
    def isModifierControl(self) -> bool:
        """return state of control key."""
    def isModifierKeyRelease(self) -> bool:
        """Was a modifier key released."""
    def isModifierLeftMouseButton(self) -> bool:
        """Return the state of the left mouse button."""
    def isModifierMiddleMouseButton(self) -> bool:
        """Return the state of the middle mouse button."""
    def isModifierNone(self) -> bool:
        """Determines if there are any modifiers for this event."""
    def isModifierShift(self) -> bool:
        """return state of shift key."""
    def modifiers(self) -> Any:
        """This routine is used by responders to find the state of the modifiers during the event."""
    def mouseButton(self) -> Any:
        """Get the mouse button of the last event."""
    def setModifiers(self, modType: Any) -> MStatus:
        """set the event modifiers."""
    def setPosition(self, x_pos: Any, y_pos: Any) -> MStatus:
        """set the location of the event to the specified location."""

class MExternalDropCallback:
    kMayaDefault: Any
    kNoMayaDefaultAndAccept: Any
    kNoMayaDefaultAndNoAccept: Any
    thisown: Any
    def __init__(self) -> None:
        """Constructor."""
    @staticmethod
    def addCallback(priority: int = 0) -> MStatus:
        """Add a callback to the general list."""
    @staticmethod
    def addUFEItemCallback(priority: int = 0) -> MStatus:
        """Add a callback to the list containing UFE item callbacks."""
    def externalDropCallback(self, doDrop: bool, targetName: str, data: MExternalDropData) -> Any:
        """This pure virtual method must be implemented by derived callback classes."""
    @staticmethod
    def removeCallback() -> MStatus:
        """Remove a callback from the general list."""
    @staticmethod
    def removeUFEItemCallback() -> MStatus:
        """Remove a callback from the list containing UFE item callbacks."""

class MExternalDropData:
    kAltModifier: Any
    kControlModifier: Any
    kLeftButton: Any
    kMidButton: Any
    kMiddleButton: Any
    kNoModifier: Any
    kRightButton: Any
    kShiftModifier: Any
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def color(self) -> MColor:
        """Obtain the color data contained in the drop, if any."""
    def dataSize(self, format: str) -> int:
        """Return the size (in bytes) of the data with the given format contained in the drop."""
    def formats(self) -> Any:
        """Obtain the list of data formats contained in the drop."""
    def hasColor(self) -> bool:
        """Query whether the drop contains color data."""
    def hasFormat(self, format: str) -> bool:
        """Query whether the drop contains data in a given format."""
    def hasHtml(self) -> bool:
        """Query whether the drop contains html data."""
    def hasImage(self) -> bool:
        """Query whether the drop contains image data."""
    def hasText(self) -> bool:
        """Query whether the drop contains text data."""
    def hasUrls(self) -> bool:
        """Query whether the drop contains URL data."""
    def html(self) -> str:
        """Obtain the html data contained in the drop, if any."""
    def image(self) -> MImage:
        """Obtain the image data contained in the drop, if any."""
    def keyboardModifiers(self) -> int:
        """Return the modifier state for this drop."""
    def mouseButtons(self, *args: Any, **kwargs: Any) -> Any: ...
    def text(self) -> str:
        """Obtain the text data contained in the drop, if any."""
    def urls(self) -> Any:
        """Obtain the URL data contained in the drop, if any."""

class MFeedbackLine:
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def clear() -> None:
        """Clear whatever is showing in the feedback line."""
    @staticmethod
    def setFormat(format: str) -> MStatus:
        """Set the format string for the feedback line."""
    @staticmethod
    def setShowFeedback(showFeedback: bool) -> None:
        """Set whether the feedback line is supposed to be displaying data."""
    @staticmethod
    def setTitle(title: str) -> MStatus:
        """Set the title string."""
    @staticmethod
    def setValue(index: Any, value: float) -> MStatus:
        """Set the value of a given index in the feedback line."""
    @staticmethod
    def showFeedback() -> bool:
        """Return whether or not the feedback line is is supposed to be displaying data."""

class MFnCircleSweepManip:
    kExtensionAttr: Any
    kInvalidAttr: Any
    kLocalDynamicAttr: Any
    kNextPos: Any
    kNormalAttr: Any
    kRotateMaxX: Any
    kRotateMaxY: Any
    kRotateMaxZ: Any
    kRotateMinX: Any
    kRotateMinY: Any
    kRotateMinZ: Any
    kScaleMaxX: Any
    kScaleMaxY: Any
    kScaleMaxZ: Any
    kScaleMinX: Any
    kScaleMinY: Any
    kScaleMinZ: Any
    kShearMaxXY: Any
    kShearMaxXZ: Any
    kShearMaxYZ: Any
    kShearMinXY: Any
    kShearMinXZ: Any
    kShearMinYZ: Any
    kTimerInvalidState: Any
    kTimerMetric_callback: Any
    kTimerMetric_callbackNotViaAPI: Any
    kTimerMetric_callbackViaAPI: Any
    kTimerMetric_compute: Any
    kTimerMetric_computeDuringCallback: Any
    kTimerMetric_computeNotDuringCallback: Any
    kTimerMetric_dirty: Any
    kTimerMetric_draw: Any
    kTimerMetric_fetch: Any
    kTimerMetrics: Any
    kTimerOff: Any
    kTimerOn: Any
    kTimerType_count: Any
    kTimerType_inclusive: Any
    kTimerType_self: Any
    kTimerTypes: Any
    kTimerUninitialized: Any
    kTranslateMaxX: Any
    kTranslateMaxY: Any
    kTranslateMaxZ: Any
    kTranslateMinX: Any
    kTranslateMinY: Any
    kTranslateMinZ: Any
    kUseDefaultColor: Any
    kUseIndexColor: Any
    kUseRGBColor: Any
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None: ...
    @overload
    def __init__(self, object: MDagPath) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None:
        """Default constructor."""
    def absoluteName(self) -> str:
        """Returns the absolute name of this node."""
    def activeColor(self) -> MColor:
        """Determines the active color used by this node."""
    @overload
    def addAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def addAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Add a new dynamic attibute to this node."""
    def addChild(self, child: MObject, index: int, keepExistingParents: bool = False) -> MStatus:
        """Makes the given DAG Node a child of the DAG Node to which this instance of the Function Set is attached."""
    def addExternalContentForFileAttr(self, table: MExternalContentInfoTable, attr: MObject) -> MStatus:
        """Adds content info to the specified table from a file path attribute."""
    def affectsAnimation(self) -> bool:
        """Introduced in 2019.0"""
    @staticmethod
    def allocateFlag(pluginName: str) -> int:
        """Allocates a node flag for sole use by the caller."""
    def angleIndex(self) -> int:
        """Returns the index for the angle of CircleSweepManip."""
    @overload
    def attribute(self, index: int) -> MObject: ...
    @overload
    def attribute(self, attrName: str) -> MObject:
        """Finds the attribute of this node at the given index."""
    def attributeClass(self, attr: MObject) -> Any:
        """Returns the class (normal, dynamic, extension) of the specified attribute."""
    def attributeCount(self) -> int:
        """Returns the number of attributes that this node has."""
    def axisIndex(self) -> int:
        """Returns the index for the axis of CircleSweepManip."""
    @staticmethod
    def balanceTransformation(identity: int, identity_: int, one: int, kXYZ: int, arg: Any = True) -> None:
        """Balance a transformation when applying a world matrix to a joint."""
    def boundingBox(self) -> Any:
        """Returns the bounding box for the dag node in object space."""
    def canBeWritten(self) -> bool:
        """Returns the do not write state of the node."""
    def centerIndex(self) -> int:
        """Returns the index for the center of the CircleSweepManip."""
    def child(self, i: int) -> MObject:
        """Queries the DAG Node attached to the Function Set for the child Node corresponding to the given index."""
    def childCount(self) -> int:
        """Determines the number of child Nodes of the Node."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def classification(nodeTypeName: str) -> str:
        """Retrieves the classification string for a node type."""
    def clearRestPosition(self) -> MStatus:
        """Clear the saved rest position of this transform."""
    def connectToAnglePlug(self, anglePlug: MPlug) -> MStatus:
        """Connect to the angle plug."""
    @overload
    def create(self) -> MObject: ...
    @overload
    def create(self, manipName: str, angleName: str) -> MObject: ...
    @overload
    def create(self, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, type: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, type: str, name: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str) -> MObject: ...
    @overload
    def create(self, type: str) -> MObject: ...
    @overload
    def create(self, type: str, name: str) -> MObject:
        """Creates a new CircleSweepManip."""
    def dagPath(self) -> MDagPath:
        """Returns the DagPath to which the Function Set is attached."""
    def dagRoot(self) -> MObject:
        """Determines the root of the first DAG Path to the DAG Node attached to the Function Set."""
    @staticmethod
    def deallocateAllFlags(pluginName: str) -> MStatus:
        """Deallocates all of the node flags which are currently allocated to the specified plugin."""
    @staticmethod
    def deallocateFlag(pluginName: str, flag: int) -> MStatus:
        """Deallocates a node flag which was previously allocated by a call to allocateFlag ."""
    @staticmethod
    def deleteManipulator(manip: MObject) -> MStatus:
        """Delete a manipulator."""
    def dgCallbackIds(self, type: Any, callbackName: str, callbackId: MCallbackIdArray, value: MDoubleArray) -> MStatus:
        """This method provides a further breakdown of the per-callback time returned via dgCallbacks() by returning the data on a """
    def dgCallbacks(self, type: Any, callbackName: Any, value: MDoubleArray) -> MStatus:
        """Node callbacks that occur when timing is enabled get logged with the node and can be queried via this method."""
    def dgTimer(self, timerMetric: Any, timerType: Any) -> float:
        """The function returns the specified timer value for the current node."""
    def dgTimerOff(self) -> MStatus:
        """Indicates that this node should no longer collect DG timing data when DG timing is enabled."""
    def dgTimerOn(self) -> MStatus:
        """Indicates that this node should collect DG timing data whenever DG timing is enabled."""
    def dgTimerQueryState(self) -> Any:
        """The function returns the current on/off state of the node's timer."""
    def dgTimerReset(self) -> MStatus:
        """The function resets the dependency graph timers and counters for this node to zero."""
    def dormantColor(self) -> MColor:
        """Determines the dormant color used by this node."""
    def drawOverrideColor(self, color: MColor) -> bool:
        """Determines the draw override color used by this node."""
    def drawOverrideEnabled(self) -> bool:
        """Determines whether or not draw override is turned on for this node."""
    def drawOverrideIsReference(self) -> bool:
        """Determines whether or not Display Type of the draw override is Reference for this node."""
    def drawOverrideIsTemplate(self) -> bool:
        """Determines whether or not Display Type of the draw override is Template for this node."""
    @staticmethod
    def drawPlaneHandles() -> bool:
        """This method returns the global option that says if the planar manipulator handles should be drawn or not."""
    def duplicate(self, instance: bool = False, instanceLeaf: bool = False) -> MObject:
        """This method duplicates the DAG hierarchy rooted at the current node."""
    @staticmethod
    def enableDGTiming(enable: bool) -> None:
        """Globally enables or disables the DG node timing mechanism."""
    def enableLimit(self, type: int, flag: bool) -> MStatus:
        """Enable or disable the limit value for the specified limit type."""
    def endCircleIndex(self) -> int:
        """Returns the index for the end of the circle of CircleSweepManip."""
    def endPoint(self) -> MPoint:
        """Returns the end point."""
    def findAlias(self, alias: str, attrObj: MObject) -> bool:
        """Retrieves the attribute with the given alias."""
    @overload
    def findPlug(self, attr: MObject, wantNetworkedPlug: bool) -> MPlug: ...
    @overload
    def findPlug(self, attrName: str, wantNetworkedPlug: bool) -> MPlug: ...
    @overload
    def findPlug(self, attr: MObject) -> MPlug: ...
    @overload
    def findPlug(self, attrName: str) -> MPlug:
        """Attempt to find a plug for the given attribute."""
    def fullPathName(self) -> str:
        """Return a string representing the full path from the root of the dag to this object."""
    def getAffectedAttributes(self, attr: MObject, affectedAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that are affected by the attribute passed in."""
    def getAffectedByAttributes(self, attr: MObject, affectedByAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that affect the attribute passed in, attr ."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute al"""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns a list of all attribute aliases for this node."""
    def getAllPaths(self, paths: MDagPathArray) -> MStatus:
        """Determines all DAG Paths to the DAG Node attached to the Function Set."""
    def getConnectedSetsAndMembers(self, instanceNumber: int, sets: MObjectArray, comps: MObjectArray, renderableSetsOnly: bool) -> MStatus:
        """Returns all the sets connected to the specified instance of this DAG object."""
    def getConnections(self, array: MPlugArray) -> MStatus:
        """Get all of the current connections to this node as an array of plugs."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> MStatus:
        """Returns the external content (files) that this node depends on."""
    def getPath(self, path: MDagPath) -> MStatus:
        """Returns a DAG Path to the DAG Node attached to the Function Set."""
    @overload
    def getRotation(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def getRotation(self, rotation: MEulerRotation) -> MStatus: ...
    @overload
    def getRotation(self, order: int) -> MStatus: ...
    @overload
    def getRotation(self, order: int, space: int) -> MStatus:
        """Retrieve the rotation component of this transformation as a quaternion."""
    def getRotationQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Retrieve the rotation component of this transformation as a quaternion."""
    def getScale(self) -> MStatus:
        """Retrieve the scaling component of this transformation."""
    def getShear(self) -> MStatus:
        """Retrieve the shearing component of this transformation."""
    def getTranslation(self, space: int) -> MVector:
        """Retrieve the translation component of this transformation in centimeters."""
    @staticmethod
    def globalSize() -> float:
        """Returns the global manipulator size."""
    @staticmethod
    def handleSize() -> float:
        """Returns the manipulator handle size."""
    def hasAttribute(self, name: str) -> bool:
        """Returns true if the node already has an attribute with the given name."""
    def hasChild(self, node: MObject) -> bool:
        """Determines whether or not the given Node is a child of the DAG Node attached to the Function Set."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    def hasParent(self, node: MObject) -> bool:
        """Determines whether or not the given Node is a parent of the DAG Node attached to the Function Set."""
    def hasUniqueName(self) -> bool:
        """Indicates whether or not this node's name is unique within the scene."""
    def hiliteColor(self) -> MColor:
        """Determines the current hilite color used by the node."""
    def icon(self) -> str:
        """Returns the custom icon filename associated with the node."""
    def inModel(self) -> bool:
        """Determines whether or not the DAG Node is in the model."""
    def inUnderWorld(self) -> bool:
        """Determines whether or not the DAG Node is an underworld node."""
    def instanceCount(self, total: bool) -> int:
        """Determines the number of times the Node attached to the Function Set is instanced."""
    def isChildOf(self, node: MObject) -> bool:
        """Determines whether or not the DAG Node attached to the Function Set is a child of the given node."""
    def isDefaultNode(self) -> bool:
        """Returns true if the node is a default node."""
    def isFlagSet(self, flag: int) -> bool:
        """Retrieves the current state of the specified flag for a node."""
    def isFromReferencedFile(self) -> bool:
        """Indicates whether or not this node came from a referenced file."""
    def isInstanceable(self) -> bool:
        """Returns true if the DAG node can be instanced, and false otherwise."""
    def isInstanced(self, indirect: bool = True) -> bool:
        """Determines whether the DAG Node attached to the Function Set is directly or indirectly instanced."""
    def isInstancedAttribute(self, attr: MObject) -> bool:
        """Returns true if the specified attribute is instanced."""
    def isIntermediateObject(self) -> bool:
        """Returns true if this object is an intermediate in a geometry calculation."""
    def isLimited(self, type: int) -> bool:
        """Determine if the specified limit attribute is enabled or disabled."""
    def isLocked(self) -> bool:
        """Indicates whether or not this node is locked."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Indicates whether or not the specified attribute was added to this node within the current scene."""
    def isOptimizePlaybackOn(self) -> bool:
        """Returns whether or not optimize playback is on."""
    def isParentOf(self, node: MObject) -> bool:
        """Determines whether or not the DAG Node attached to the Function Set is a parent of the given node."""
    def isShared(self) -> bool:
        """Indicates whether or not this node is shared."""
    def isTrackingEdits(self) -> bool:
        """Returns whether or not edits on the given node are being tracked by the generalized edit system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def isVisible(self) -> bool:
        """Returns whether or not the manipulator is visible."""
    def limitValue(self, type: int) -> float:
        """Determine the current value of the specified limit."""
    @staticmethod
    def lineSize() -> float:
        """Returns the manipulator line size."""
    def manipScale(self) -> float:
        """Returns the manipulator scale."""
    def model(self) -> MObject:
        """Deprecated in 2016.0"""
    def name(self) -> str:
        """Returns the name of this node."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def objectColor(self) -> int:
        """Deprecated in 2016.0"""
    def objectColorIndex(self) -> int:
        """Determines the index for the current user defined inactive color used by the node."""
    def objectColorRGB(self) -> MColor:
        """Determines the RGB color for the current user defined inactive color used by the node."""
    def objectColorType(self) -> Any:
        """Determines whether or not the user defined inactive color will be used for the node, or whether the default inactive col"""
    def objectGroupComponent(self, *args: Any, **kwargs: Any) -> Any: ...
    def parent(self, i: int) -> MObject:
        """Queries the DAG Node attached to the Function Set for the parent Node corresponding to the given index."""
    def parentCount(self) -> int:
        """Determines the number of parent Nodes of the Node."""
    def parentNamespace(self) -> str:
        """Returns the name of the namespace in which this node resides."""
    def partialPathName(self) -> str:
        """Return a string representing the partial path from the root of the dag to this object."""
    def pluginName(self) -> str:
        """Returns the name of the plug-in this MFnDependendencyNode was defined in."""
    def plugsAlias(self, plug: MPlug) -> str:
        """Returns the alias for the plug's attribute or the empty string if that attribute has no alias."""
    @overload
    def removeAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def removeAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Remove a dynamic attribute from a node."""
    def removeChild(self, child: MObject) -> MStatus:
        """Removes the given DAG Node from the parent."""
    def removeChildAt(self, index: int) -> MStatus:
        """Removes the child at the given index from the parent."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Some nodes, such as the various animCurve nodes, require that their attributes be set in a specific order for proper ope"""
    def resetFromRestPosition(self) -> MStatus:
        """Reset the transform to its rest position."""
    def resetTransformation(self, m: MMatrix) -> MStatus:
        """Reset this transform to equal the given matrix in world space."""
    def restPosition(self) -> MTransformationMatrix:
        """Retrieve the saved rest position of this transform."""
    @overload
    def rotateBy(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def rotateBy(self, rotation: MEulerRotation, Space: int | None = None) -> MStatus: ...
    @overload
    def rotateBy(self, order: int, Space: int | None = None) -> MStatus:
        """Relatively change the rotation of this transformation using a quaternion."""
    def rotateByQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Relatively change the rotation of this transformation using a quaternion."""
    def rotateOrientation(self, space: int) -> MQuaternion:
        """Returns the rotation used to orient the local rotation space."""
    def rotatePivot(self, space: int) -> MPoint:
        """Returns the pivot about which the rotation is applied."""
    def rotatePivotTranslation(self, space: int) -> MVector:
        """Return the rotate pivot translation in centimeters."""
    def rotateXYZValue(self, valIndex: int) -> MEulerRotation:
        """Gets the rotation for the active manipulator."""
    def rotationOrder(self) -> int:
        """Returns the rotation order for the transform matrix - the order in which the Euler angles are applied to create the end """
    def scaleBy(self) -> MStatus:
        """Relatively scale this transformation."""
    def scalePivot(self, space: int) -> MPoint:
        """Returns the pivot around which the scale is applied."""
    def scalePivotTranslation(self, space: int) -> MVector:
        """Returns the scale pivot translation in centimeters."""
    def set(self, transform: MTransformationMatrix) -> MStatus:
        """Change this transform to equal the given matrix."""
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setAngle(self, angle: MAngle) -> MStatus:
        """Sets the angle of the CircleSweepManip."""
    def setCenterPoint(self, centerPoint: MPoint) -> MStatus:
        """Sets the center point of the CircleSweepManip."""
    def setDoNotWrite(self, flag: bool) -> MStatus:
        """Use this method to mark the "do not write" state of this node."""
    def setDrawAsArc(self, state: bool) -> MStatus:
        """Sets whether or not to draw as arc."""
    @staticmethod
    def setDrawPlaneHandles(drawPlaneHandles: bool) -> None:
        """Sets the global option to display planar handles or not on supported manipulators."""
    def setEndPoint(self, endPoint: MPoint) -> MStatus:
        """Sets the end point of the CircleSweepManip."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> MStatus:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> MStatus:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> MStatus:
        """Sets the state of the specified flag for the node."""
    @staticmethod
    def setGlobalSize(size: float) -> None:
        """Sets the global manipulator size."""
    @staticmethod
    def setHandleSize(size: float) -> None:
        """Sets the manipulator handle size."""
    def setIcon(self, filename: str) -> MStatus:
        """Associates a custom icon with the node for display in the Maya UI."""
    def setInstanceable(self, how: bool) -> MStatus:
        """Sets whether or not the DAG node is instanceable."""
    def setIntermediateObject(self, isIntermediate: bool) -> MStatus:
        """Sets whether this object is an intermediate in a geometry calculation."""
    def setLimit(self, type: int, value: float) -> MStatus:
        """Change the limit value for the specified limit type, and automatically enable the limit to be true."""
    @staticmethod
    def setLineSize(size: float) -> None:
        """Sets the manipulator line size."""
    def setLocked(self, locked: bool) -> MStatus:
        """Locks or unlocks this node."""
    def setManipScale(self, size: float) -> MStatus:
        """Sets the manipulator scale."""
    @overload
    def setName(self, name: str, createNamespace: bool = False) -> str: ...
    @overload
    def setName(self, name: str) -> str:
        """Sets the name of this node."""
    def setNormal(self, normal: MVector) -> MStatus:
        """Sets the normal of the CircleSweepManip."""
    @overload
    def setObject(self, path: MDagPath) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches Function Set to the DAG Node that has the given DAG Path."""
    @overload
    def setObjectColor(self, color: int) -> MStatus: ...
    @overload
    def setObjectColor(self, color: MColor) -> MStatus:
        """Sets the index for the current user defined inactive color used by the node."""
    def setObjectColorType(self, type: Any) -> MStatus:
        """Sets whether or not the user defined inactive object color will be used."""
    def setOptimizePlayback(self, optimizePlayback: bool) -> MStatus:
        """Sets whether or not to optimize the playback."""
    def setRadius(self, radius: float) -> MStatus:
        """Sets the radius of the CircleSweepManip."""
    def setRestPosition(self, matrix: MTransformationMatrix) -> MStatus:
        """Change the saved rest position of this transform."""
    def setRotateOrientation(self, quat: MQuaternion, space: int, balance: bool) -> MStatus:
        """Set the rotation used to orient the local rotation space."""
    def setRotatePivot(self, point: MPoint, space: int, balance: bool) -> MStatus:
        """Set the rotate pivot in centimeters about which rotation is applied."""
    def setRotatePivotTranslation(self, vec: MVector, space: int) -> MStatus:
        """Set the rotate pivot translation in centimeters."""
    @overload
    def setRotation(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def setRotation(self, rotation: MEulerRotation) -> MStatus: ...
    @overload
    def setRotation(self, order: int) -> MStatus: ...
    @overload
    def setRotation(self, RotationOrder: int, space: int) -> MStatus:
        """Change the rotation component of this transformation using a quaternion."""
    def setRotationOrder(self, order: int, reorder: bool) -> MStatus:
        """Change the rotation order for the transform - the order in which the Euler angles are applied to create the end rotation"""
    def setRotationQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Change the rotation component of this transformation using a quaternion."""
    def setScale(self) -> MStatus:
        """Set the scaling component of this transformation."""
    def setScalePivot(self, point: MPoint, space: int, balance: bool) -> MStatus:
        """Set the pivot around which the scale is applied in centimeters."""
    def setScalePivotTranslation(self, vec: MVector, space: int) -> MStatus:
        """Set the scale pivot translation in centimeters."""
    def setShear(self) -> MStatus:
        """Set the shearing component of this transformation."""
    def setStartPoint(self, startPoint: MPoint) -> MStatus:
        """Sets the start point of the CircleSweepManip."""
    def setTranslation(self, vec: MVector, space: int) -> MStatus:
        """Change the translation component of this transformation."""
    def setUseObjectColor(self, useObjectColor: bool) -> MStatus:
        """Deprecated in 2016.0"""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def setVisible(self, isVisible: bool) -> MStatus:
        """Sets whether or not the manipulator is visible."""
    def shearBy(self) -> MStatus:
        """Relatively shear this transformation."""
    def startCircleIndex(self) -> int:
        """Returns the index for the start of the circle of CircleSweepManip."""
    def startPoint(self) -> MPoint:
        """Returns the start point."""
    def transformation(self) -> MTransformationMatrix:
        """Retrieve the transformation matrix represented by this transform."""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
    def translateBy(self, vec: MVector, space: int) -> MStatus:
        """Relatively change the translation component of this transformation."""
    def translation(self, Space: int) -> MVector:
        """Deprecated in 2018.0"""
    def type(self) -> int:
        """Function set type."""
    def typeId(self) -> MTypeId:
        """Returns the type id of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""
    @staticmethod
    def typeString(Type: int) -> str:
        """Introduced in 2020.0"""
    def uniqueName(self) -> str:
        """Introduced in 2023.0"""
    def userNode(self) -> Any:
        """If the function set's node is a plug-in node, then this method will extract the MPxNode pointer from it."""
    def usingHiliteColor(self) -> bool:
        """Determines whether or not the hilite color will be used for the node."""
    def usingObjectColor(self) -> bool:
        """Deprecated in 2016.0"""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnCurveSegmentManip:
    kExtensionAttr: Any
    kInvalidAttr: Any
    kLocalDynamicAttr: Any
    kNextPos: Any
    kNormalAttr: Any
    kRotateMaxX: Any
    kRotateMaxY: Any
    kRotateMaxZ: Any
    kRotateMinX: Any
    kRotateMinY: Any
    kRotateMinZ: Any
    kScaleMaxX: Any
    kScaleMaxY: Any
    kScaleMaxZ: Any
    kScaleMinX: Any
    kScaleMinY: Any
    kScaleMinZ: Any
    kShearMaxXY: Any
    kShearMaxXZ: Any
    kShearMaxYZ: Any
    kShearMinXY: Any
    kShearMinXZ: Any
    kShearMinYZ: Any
    kTimerInvalidState: Any
    kTimerMetric_callback: Any
    kTimerMetric_callbackNotViaAPI: Any
    kTimerMetric_callbackViaAPI: Any
    kTimerMetric_compute: Any
    kTimerMetric_computeDuringCallback: Any
    kTimerMetric_computeNotDuringCallback: Any
    kTimerMetric_dirty: Any
    kTimerMetric_draw: Any
    kTimerMetric_fetch: Any
    kTimerMetrics: Any
    kTimerOff: Any
    kTimerOn: Any
    kTimerType_count: Any
    kTimerType_inclusive: Any
    kTimerType_self: Any
    kTimerTypes: Any
    kTimerUninitialized: Any
    kTranslateMaxX: Any
    kTranslateMaxY: Any
    kTranslateMaxZ: Any
    kTranslateMinX: Any
    kTranslateMinY: Any
    kTranslateMinZ: Any
    kUseDefaultColor: Any
    kUseIndexColor: Any
    kUseRGBColor: Any
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None: ...
    @overload
    def __init__(self, object: MDagPath) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None:
        """Default constructor."""
    def absoluteName(self) -> str:
        """Returns the absolute name of this node."""
    def activeColor(self) -> MColor:
        """Determines the active color used by this node."""
    @overload
    def addAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def addAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Add a new dynamic attibute to this node."""
    def addChild(self, child: MObject, index: int, keepExistingParents: bool = False) -> MStatus:
        """Makes the given DAG Node a child of the DAG Node to which this instance of the Function Set is attached."""
    def addExternalContentForFileAttr(self, table: MExternalContentInfoTable, attr: MObject) -> MStatus:
        """Adds content info to the specified table from a file path attribute."""
    def affectsAnimation(self) -> bool:
        """Introduced in 2019.0"""
    @staticmethod
    def allocateFlag(pluginName: str) -> int:
        """Allocates a node flag for sole use by the caller."""
    @overload
    def attribute(self, index: int) -> MObject: ...
    @overload
    def attribute(self, attrName: str) -> MObject:
        """Finds the attribute of this node at the given index."""
    def attributeClass(self, attr: MObject) -> Any:
        """Returns the class (normal, dynamic, extension) of the specified attribute."""
    def attributeCount(self) -> int:
        """Returns the number of attributes that this node has."""
    @staticmethod
    def balanceTransformation(identity: int, identity_: int, one: int, kXYZ: int, arg: Any = True) -> None:
        """Balance a transformation when applying a world matrix to a joint."""
    def boundingBox(self) -> Any:
        """Returns the bounding box for the dag node in object space."""
    def canBeWritten(self) -> bool:
        """Returns the do not write state of the node."""
    def child(self, i: int) -> MObject:
        """Queries the DAG Node attached to the Function Set for the child Node corresponding to the given index."""
    def childCount(self) -> int:
        """Determines the number of child Nodes of the Node."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def classification(nodeTypeName: str) -> str:
        """Retrieves the classification string for a node type."""
    def clearRestPosition(self) -> MStatus:
        """Clear the saved rest position of this transform."""
    def connectToCurvePlug(self, curvePlug: MPlug) -> MStatus:
        """Connect to the curve plug."""
    def connectToEndParamPlug(self, endParamPlug: MPlug) -> MStatus:
        """Connect to the endParam plug."""
    def connectToStartParamPlug(self, startParamPlug: MPlug) -> MStatus:
        """Connect to the startParam plug."""
    @overload
    def create(self) -> MObject: ...
    @overload
    def create(self, manipName: str, startParamName: str, endParamName: str) -> MObject: ...
    @overload
    def create(self, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, type: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, type: str, name: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str) -> MObject: ...
    @overload
    def create(self, type: str) -> MObject: ...
    @overload
    def create(self, type: str, name: str) -> MObject:
        """Creates a new CurveSegmentManip."""
    def curveIndex(self) -> int:
        """Returns the index of the curve."""
    def dagPath(self) -> MDagPath:
        """Returns the DagPath to which the Function Set is attached."""
    def dagRoot(self) -> MObject:
        """Determines the root of the first DAG Path to the DAG Node attached to the Function Set."""
    @staticmethod
    def deallocateAllFlags(pluginName: str) -> MStatus:
        """Deallocates all of the node flags which are currently allocated to the specified plugin."""
    @staticmethod
    def deallocateFlag(pluginName: str, flag: int) -> MStatus:
        """Deallocates a node flag which was previously allocated by a call to allocateFlag ."""
    @staticmethod
    def deleteManipulator(manip: MObject) -> MStatus:
        """Delete a manipulator."""
    def dgCallbackIds(self, type: Any, callbackName: str, callbackId: MCallbackIdArray, value: MDoubleArray) -> MStatus:
        """This method provides a further breakdown of the per-callback time returned via dgCallbacks() by returning the data on a """
    def dgCallbacks(self, type: Any, callbackName: Any, value: MDoubleArray) -> MStatus:
        """Node callbacks that occur when timing is enabled get logged with the node and can be queried via this method."""
    def dgTimer(self, timerMetric: Any, timerType: Any) -> float:
        """The function returns the specified timer value for the current node."""
    def dgTimerOff(self) -> MStatus:
        """Indicates that this node should no longer collect DG timing data when DG timing is enabled."""
    def dgTimerOn(self) -> MStatus:
        """Indicates that this node should collect DG timing data whenever DG timing is enabled."""
    def dgTimerQueryState(self) -> Any:
        """The function returns the current on/off state of the node's timer."""
    def dgTimerReset(self) -> MStatus:
        """The function resets the dependency graph timers and counters for this node to zero."""
    def dormantColor(self) -> MColor:
        """Determines the dormant color used by this node."""
    def drawOverrideColor(self, color: MColor) -> bool:
        """Determines the draw override color used by this node."""
    def drawOverrideEnabled(self) -> bool:
        """Determines whether or not draw override is turned on for this node."""
    def drawOverrideIsReference(self) -> bool:
        """Determines whether or not Display Type of the draw override is Reference for this node."""
    def drawOverrideIsTemplate(self) -> bool:
        """Determines whether or not Display Type of the draw override is Template for this node."""
    @staticmethod
    def drawPlaneHandles() -> bool:
        """This method returns the global option that says if the planar manipulator handles should be drawn or not."""
    def duplicate(self, instance: bool = False, instanceLeaf: bool = False) -> MObject:
        """This method duplicates the DAG hierarchy rooted at the current node."""
    @staticmethod
    def enableDGTiming(enable: bool) -> None:
        """Globally enables or disables the DG node timing mechanism."""
    def enableLimit(self, type: int, flag: bool) -> MStatus:
        """Enable or disable the limit value for the specified limit type."""
    def endParamIndex(self) -> int:
        """Returns the index of the end parameter of the CurveSegmentManip."""
    def endParameter(self) -> float:
        """Returns the end parameter."""
    def findAlias(self, alias: str, attrObj: MObject) -> bool:
        """Retrieves the attribute with the given alias."""
    @overload
    def findPlug(self, attr: MObject, wantNetworkedPlug: bool) -> MPlug: ...
    @overload
    def findPlug(self, attrName: str, wantNetworkedPlug: bool) -> MPlug: ...
    @overload
    def findPlug(self, attr: MObject) -> MPlug: ...
    @overload
    def findPlug(self, attrName: str) -> MPlug:
        """Attempt to find a plug for the given attribute."""
    def fullPathName(self) -> str:
        """Return a string representing the full path from the root of the dag to this object."""
    def getAffectedAttributes(self, attr: MObject, affectedAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that are affected by the attribute passed in."""
    def getAffectedByAttributes(self, attr: MObject, affectedByAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that affect the attribute passed in, attr ."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute al"""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns a list of all attribute aliases for this node."""
    def getAllPaths(self, paths: MDagPathArray) -> MStatus:
        """Determines all DAG Paths to the DAG Node attached to the Function Set."""
    def getConnectedSetsAndMembers(self, instanceNumber: int, sets: MObjectArray, comps: MObjectArray, renderableSetsOnly: bool) -> MStatus:
        """Returns all the sets connected to the specified instance of this DAG object."""
    def getConnections(self, array: MPlugArray) -> MStatus:
        """Get all of the current connections to this node as an array of plugs."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> MStatus:
        """Returns the external content (files) that this node depends on."""
    def getPath(self, path: MDagPath) -> MStatus:
        """Returns a DAG Path to the DAG Node attached to the Function Set."""
    @overload
    def getRotation(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def getRotation(self, rotation: MEulerRotation) -> MStatus: ...
    @overload
    def getRotation(self, order: int) -> MStatus: ...
    @overload
    def getRotation(self, order: int, space: int) -> MStatus:
        """Retrieve the rotation component of this transformation as a quaternion."""
    def getRotationQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Retrieve the rotation component of this transformation as a quaternion."""
    def getScale(self) -> MStatus:
        """Retrieve the scaling component of this transformation."""
    def getShear(self) -> MStatus:
        """Retrieve the shearing component of this transformation."""
    def getTranslation(self, space: int) -> MVector:
        """Retrieve the translation component of this transformation in centimeters."""
    @staticmethod
    def globalSize() -> float:
        """Returns the global manipulator size."""
    @staticmethod
    def handleSize() -> float:
        """Returns the manipulator handle size."""
    def hasAttribute(self, name: str) -> bool:
        """Returns true if the node already has an attribute with the given name."""
    def hasChild(self, node: MObject) -> bool:
        """Determines whether or not the given Node is a child of the DAG Node attached to the Function Set."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    def hasParent(self, node: MObject) -> bool:
        """Determines whether or not the given Node is a parent of the DAG Node attached to the Function Set."""
    def hasUniqueName(self) -> bool:
        """Indicates whether or not this node's name is unique within the scene."""
    def hiliteColor(self) -> MColor:
        """Determines the current hilite color used by the node."""
    def icon(self) -> str:
        """Returns the custom icon filename associated with the node."""
    def inModel(self) -> bool:
        """Determines whether or not the DAG Node is in the model."""
    def inUnderWorld(self) -> bool:
        """Determines whether or not the DAG Node is an underworld node."""
    def instanceCount(self, total: bool) -> int:
        """Determines the number of times the Node attached to the Function Set is instanced."""
    def isChildOf(self, node: MObject) -> bool:
        """Determines whether or not the DAG Node attached to the Function Set is a child of the given node."""
    def isDefaultNode(self) -> bool:
        """Returns true if the node is a default node."""
    def isFlagSet(self, flag: int) -> bool:
        """Retrieves the current state of the specified flag for a node."""
    def isFromReferencedFile(self) -> bool:
        """Indicates whether or not this node came from a referenced file."""
    def isInstanceable(self) -> bool:
        """Returns true if the DAG node can be instanced, and false otherwise."""
    def isInstanced(self, indirect: bool = True) -> bool:
        """Determines whether the DAG Node attached to the Function Set is directly or indirectly instanced."""
    def isInstancedAttribute(self, attr: MObject) -> bool:
        """Returns true if the specified attribute is instanced."""
    def isIntermediateObject(self) -> bool:
        """Returns true if this object is an intermediate in a geometry calculation."""
    def isLimited(self, type: int) -> bool:
        """Determine if the specified limit attribute is enabled or disabled."""
    def isLocked(self) -> bool:
        """Indicates whether or not this node is locked."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Indicates whether or not the specified attribute was added to this node within the current scene."""
    def isOptimizePlaybackOn(self) -> bool:
        """Returns whether or not optimize playback is on."""
    def isParentOf(self, node: MObject) -> bool:
        """Determines whether or not the DAG Node attached to the Function Set is a parent of the given node."""
    def isShared(self) -> bool:
        """Indicates whether or not this node is shared."""
    def isTrackingEdits(self) -> bool:
        """Returns whether or not edits on the given node are being tracked by the generalized edit system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def isVisible(self) -> bool:
        """Returns whether or not the manipulator is visible."""
    def limitValue(self, type: int) -> float:
        """Determine the current value of the specified limit."""
    @staticmethod
    def lineSize() -> float:
        """Returns the manipulator line size."""
    def manipScale(self) -> float:
        """Returns the manipulator scale."""
    def model(self) -> MObject:
        """Deprecated in 2016.0"""
    def name(self) -> str:
        """Returns the name of this node."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def objectColor(self) -> int:
        """Deprecated in 2016.0"""
    def objectColorIndex(self) -> int:
        """Determines the index for the current user defined inactive color used by the node."""
    def objectColorRGB(self) -> MColor:
        """Determines the RGB color for the current user defined inactive color used by the node."""
    def objectColorType(self) -> Any:
        """Determines whether or not the user defined inactive color will be used for the node, or whether the default inactive col"""
    def objectGroupComponent(self, *args: Any, **kwargs: Any) -> Any: ...
    def parent(self, i: int) -> MObject:
        """Queries the DAG Node attached to the Function Set for the parent Node corresponding to the given index."""
    def parentCount(self) -> int:
        """Determines the number of parent Nodes of the Node."""
    def parentNamespace(self) -> str:
        """Returns the name of the namespace in which this node resides."""
    def partialPathName(self) -> str:
        """Return a string representing the partial path from the root of the dag to this object."""
    def pluginName(self) -> str:
        """Returns the name of the plug-in this MFnDependendencyNode was defined in."""
    def plugsAlias(self, plug: MPlug) -> str:
        """Returns the alias for the plug's attribute or the empty string if that attribute has no alias."""
    @overload
    def removeAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def removeAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Remove a dynamic attribute from a node."""
    def removeChild(self, child: MObject) -> MStatus:
        """Removes the given DAG Node from the parent."""
    def removeChildAt(self, index: int) -> MStatus:
        """Removes the child at the given index from the parent."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Some nodes, such as the various animCurve nodes, require that their attributes be set in a specific order for proper ope"""
    def resetFromRestPosition(self) -> MStatus:
        """Reset the transform to its rest position."""
    def resetTransformation(self, m: MMatrix) -> MStatus:
        """Reset this transform to equal the given matrix in world space."""
    def restPosition(self) -> MTransformationMatrix:
        """Retrieve the saved rest position of this transform."""
    @overload
    def rotateBy(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def rotateBy(self, rotation: MEulerRotation, Space: int | None = None) -> MStatus: ...
    @overload
    def rotateBy(self, order: int, Space: int | None = None) -> MStatus:
        """Relatively change the rotation of this transformation using a quaternion."""
    def rotateByQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Relatively change the rotation of this transformation using a quaternion."""
    def rotateOrientation(self, space: int) -> MQuaternion:
        """Returns the rotation used to orient the local rotation space."""
    def rotatePivot(self, space: int) -> MPoint:
        """Returns the pivot about which the rotation is applied."""
    def rotatePivotTranslation(self, space: int) -> MVector:
        """Return the rotate pivot translation in centimeters."""
    def rotateXYZValue(self, valIndex: int) -> MEulerRotation:
        """Gets the rotation for the active manipulator."""
    def rotationOrder(self) -> int:
        """Returns the rotation order for the transform matrix - the order in which the Euler angles are applied to create the end """
    def scaleBy(self) -> MStatus:
        """Relatively scale this transformation."""
    def scalePivot(self, space: int) -> MPoint:
        """Returns the pivot around which the scale is applied."""
    def scalePivotTranslation(self, space: int) -> MVector:
        """Returns the scale pivot translation in centimeters."""
    def set(self, transform: MTransformationMatrix) -> MStatus:
        """Change this transform to equal the given matrix."""
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setDoNotWrite(self, flag: bool) -> MStatus:
        """Use this method to mark the "do not write" state of this node."""
    @staticmethod
    def setDrawPlaneHandles(drawPlaneHandles: bool) -> None:
        """Sets the global option to display planar handles or not on supported manipulators."""
    def setEndParameter(self, endParameter: float) -> MStatus:
        """Sets the end parameter."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> MStatus:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> MStatus:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> MStatus:
        """Sets the state of the specified flag for the node."""
    @staticmethod
    def setGlobalSize(size: float) -> None:
        """Sets the global manipulator size."""
    @staticmethod
    def setHandleSize(size: float) -> None:
        """Sets the manipulator handle size."""
    def setIcon(self, filename: str) -> MStatus:
        """Associates a custom icon with the node for display in the Maya UI."""
    def setInstanceable(self, how: bool) -> MStatus:
        """Sets whether or not the DAG node is instanceable."""
    def setIntermediateObject(self, isIntermediate: bool) -> MStatus:
        """Sets whether this object is an intermediate in a geometry calculation."""
    def setLimit(self, type: int, value: float) -> MStatus:
        """Change the limit value for the specified limit type, and automatically enable the limit to be true."""
    @staticmethod
    def setLineSize(size: float) -> None:
        """Sets the manipulator line size."""
    def setLocked(self, locked: bool) -> MStatus:
        """Locks or unlocks this node."""
    def setManipScale(self, size: float) -> MStatus:
        """Sets the manipulator scale."""
    @overload
    def setName(self, name: str, createNamespace: bool = False) -> str: ...
    @overload
    def setName(self, name: str) -> str:
        """Sets the name of this node."""
    @overload
    def setObject(self, path: MDagPath) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches Function Set to the DAG Node that has the given DAG Path."""
    @overload
    def setObjectColor(self, color: int) -> MStatus: ...
    @overload
    def setObjectColor(self, color: MColor) -> MStatus:
        """Sets the index for the current user defined inactive color used by the node."""
    def setObjectColorType(self, type: Any) -> MStatus:
        """Sets whether or not the user defined inactive object color will be used."""
    def setOptimizePlayback(self, optimizePlayback: bool) -> MStatus:
        """Sets whether or not to optimize the playback."""
    def setRestPosition(self, matrix: MTransformationMatrix) -> MStatus:
        """Change the saved rest position of this transform."""
    def setRotateOrientation(self, quat: MQuaternion, space: int, balance: bool) -> MStatus:
        """Set the rotation used to orient the local rotation space."""
    def setRotatePivot(self, point: MPoint, space: int, balance: bool) -> MStatus:
        """Set the rotate pivot in centimeters about which rotation is applied."""
    def setRotatePivotTranslation(self, vec: MVector, space: int) -> MStatus:
        """Set the rotate pivot translation in centimeters."""
    @overload
    def setRotation(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def setRotation(self, rotation: MEulerRotation) -> MStatus: ...
    @overload
    def setRotation(self, order: int) -> MStatus: ...
    @overload
    def setRotation(self, RotationOrder: int, space: int) -> MStatus:
        """Change the rotation component of this transformation using a quaternion."""
    def setRotationOrder(self, order: int, reorder: bool) -> MStatus:
        """Change the rotation order for the transform - the order in which the Euler angles are applied to create the end rotation"""
    def setRotationQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Change the rotation component of this transformation using a quaternion."""
    def setScale(self) -> MStatus:
        """Set the scaling component of this transformation."""
    def setScalePivot(self, point: MPoint, space: int, balance: bool) -> MStatus:
        """Set the pivot around which the scale is applied in centimeters."""
    def setScalePivotTranslation(self, vec: MVector, space: int) -> MStatus:
        """Set the scale pivot translation in centimeters."""
    def setShear(self) -> MStatus:
        """Set the shearing component of this transformation."""
    def setStartParameter(self, startParameter: float) -> MStatus:
        """Sets the start parameter."""
    def setTranslation(self, vec: MVector, space: int) -> MStatus:
        """Change the translation component of this transformation."""
    def setUseObjectColor(self, useObjectColor: bool) -> MStatus:
        """Deprecated in 2016.0"""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def setVisible(self, isVisible: bool) -> MStatus:
        """Sets whether or not the manipulator is visible."""
    def shearBy(self) -> MStatus:
        """Relatively shear this transformation."""
    def startParamIndex(self) -> int:
        """Returns the index of the start parameter of the CurveSegmentManip."""
    def startParameter(self) -> float:
        """Returns the start parameter."""
    def transformation(self) -> MTransformationMatrix:
        """Retrieve the transformation matrix represented by this transform."""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
    def translateBy(self, vec: MVector, space: int) -> MStatus:
        """Relatively change the translation component of this transformation."""
    def translation(self, Space: int) -> MVector:
        """Deprecated in 2018.0"""
    def type(self) -> int:
        """Function set type."""
    def typeId(self) -> MTypeId:
        """Returns the type id of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""
    @staticmethod
    def typeString(Type: int) -> str:
        """Introduced in 2020.0"""
    def uniqueName(self) -> str:
        """Introduced in 2023.0"""
    def userNode(self) -> Any:
        """If the function set's node is a plug-in node, then this method will extract the MPxNode pointer from it."""
    def usingHiliteColor(self) -> bool:
        """Determines whether or not the hilite color will be used for the node."""
    def usingObjectColor(self) -> bool:
        """Deprecated in 2016.0"""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnDirectionManip:
    kExtensionAttr: Any
    kInvalidAttr: Any
    kLocalDynamicAttr: Any
    kNextPos: Any
    kNormalAttr: Any
    kRotateMaxX: Any
    kRotateMaxY: Any
    kRotateMaxZ: Any
    kRotateMinX: Any
    kRotateMinY: Any
    kRotateMinZ: Any
    kScaleMaxX: Any
    kScaleMaxY: Any
    kScaleMaxZ: Any
    kScaleMinX: Any
    kScaleMinY: Any
    kScaleMinZ: Any
    kShearMaxXY: Any
    kShearMaxXZ: Any
    kShearMaxYZ: Any
    kShearMinXY: Any
    kShearMinXZ: Any
    kShearMinYZ: Any
    kTimerInvalidState: Any
    kTimerMetric_callback: Any
    kTimerMetric_callbackNotViaAPI: Any
    kTimerMetric_callbackViaAPI: Any
    kTimerMetric_compute: Any
    kTimerMetric_computeDuringCallback: Any
    kTimerMetric_computeNotDuringCallback: Any
    kTimerMetric_dirty: Any
    kTimerMetric_draw: Any
    kTimerMetric_fetch: Any
    kTimerMetrics: Any
    kTimerOff: Any
    kTimerOn: Any
    kTimerType_count: Any
    kTimerType_inclusive: Any
    kTimerType_self: Any
    kTimerTypes: Any
    kTimerUninitialized: Any
    kTranslateMaxX: Any
    kTranslateMaxY: Any
    kTranslateMaxZ: Any
    kTranslateMinX: Any
    kTranslateMinY: Any
    kTranslateMinZ: Any
    kUseDefaultColor: Any
    kUseIndexColor: Any
    kUseRGBColor: Any
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None: ...
    @overload
    def __init__(self, object: MDagPath) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None:
        """Default constructor."""
    def absoluteName(self) -> str:
        """Returns the absolute name of this node."""
    def activeColor(self) -> MColor:
        """Determines the active color used by this node."""
    @overload
    def addAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def addAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Add a new dynamic attibute to this node."""
    def addChild(self, child: MObject, index: int, keepExistingParents: bool = False) -> MStatus:
        """Makes the given DAG Node a child of the DAG Node to which this instance of the Function Set is attached."""
    def addExternalContentForFileAttr(self, table: MExternalContentInfoTable, attr: MObject) -> MStatus:
        """Adds content info to the specified table from a file path attribute."""
    def affectsAnimation(self) -> bool:
        """Introduced in 2019.0"""
    @staticmethod
    def allocateFlag(pluginName: str) -> int:
        """Allocates a node flag for sole use by the caller."""
    @overload
    def attribute(self, index: int) -> MObject: ...
    @overload
    def attribute(self, attrName: str) -> MObject:
        """Finds the attribute of this node at the given index."""
    def attributeClass(self, attr: MObject) -> Any:
        """Returns the class (normal, dynamic, extension) of the specified attribute."""
    def attributeCount(self) -> int:
        """Returns the number of attributes that this node has."""
    @staticmethod
    def balanceTransformation(identity: int, identity_: int, one: int, kXYZ: int, arg: Any = True) -> None:
        """Balance a transformation when applying a world matrix to a joint."""
    def boundingBox(self) -> Any:
        """Returns the bounding box for the dag node in object space."""
    def canBeWritten(self) -> bool:
        """Returns the do not write state of the node."""
    def child(self, i: int) -> MObject:
        """Queries the DAG Node attached to the Function Set for the child Node corresponding to the given index."""
    def childCount(self) -> int:
        """Determines the number of child Nodes of the Node."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def classification(nodeTypeName: str) -> str:
        """Retrieves the classification string for a node type."""
    def clearRestPosition(self) -> MStatus:
        """Clear the saved rest position of this transform."""
    def connectToDirectionPlug(self, directionPlug: MPlug) -> MStatus:
        """Connect to the direction plug."""
    @overload
    def create(self) -> MObject: ...
    @overload
    def create(self, manipName: str, directionName: str) -> MObject: ...
    @overload
    def create(self, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, type: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, type: str, name: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str) -> MObject: ...
    @overload
    def create(self, type: str) -> MObject: ...
    @overload
    def create(self, type: str, name: str) -> MObject:
        """Creates a new DirectionManip."""
    def dagPath(self) -> MDagPath:
        """Returns the DagPath to which the Function Set is attached."""
    def dagRoot(self) -> MObject:
        """Determines the root of the first DAG Path to the DAG Node attached to the Function Set."""
    @staticmethod
    def deallocateAllFlags(pluginName: str) -> MStatus:
        """Deallocates all of the node flags which are currently allocated to the specified plugin."""
    @staticmethod
    def deallocateFlag(pluginName: str, flag: int) -> MStatus:
        """Deallocates a node flag which was previously allocated by a call to allocateFlag ."""
    @staticmethod
    def deleteManipulator(manip: MObject) -> MStatus:
        """Delete a manipulator."""
    def dgCallbackIds(self, type: Any, callbackName: str, callbackId: MCallbackIdArray, value: MDoubleArray) -> MStatus:
        """This method provides a further breakdown of the per-callback time returned via dgCallbacks() by returning the data on a """
    def dgCallbacks(self, type: Any, callbackName: Any, value: MDoubleArray) -> MStatus:
        """Node callbacks that occur when timing is enabled get logged with the node and can be queried via this method."""
    def dgTimer(self, timerMetric: Any, timerType: Any) -> float:
        """The function returns the specified timer value for the current node."""
    def dgTimerOff(self) -> MStatus:
        """Indicates that this node should no longer collect DG timing data when DG timing is enabled."""
    def dgTimerOn(self) -> MStatus:
        """Indicates that this node should collect DG timing data whenever DG timing is enabled."""
    def dgTimerQueryState(self) -> Any:
        """The function returns the current on/off state of the node's timer."""
    def dgTimerReset(self) -> MStatus:
        """The function resets the dependency graph timers and counters for this node to zero."""
    def directionIndex(self) -> int:
        """Returns the index of the direction."""
    def dormantColor(self) -> MColor:
        """Determines the dormant color used by this node."""
    def drawOverrideColor(self, color: MColor) -> bool:
        """Determines the draw override color used by this node."""
    def drawOverrideEnabled(self) -> bool:
        """Determines whether or not draw override is turned on for this node."""
    def drawOverrideIsReference(self) -> bool:
        """Determines whether or not Display Type of the draw override is Reference for this node."""
    def drawOverrideIsTemplate(self) -> bool:
        """Determines whether or not Display Type of the draw override is Template for this node."""
    @staticmethod
    def drawPlaneHandles() -> bool:
        """This method returns the global option that says if the planar manipulator handles should be drawn or not."""
    def duplicate(self, instance: bool = False, instanceLeaf: bool = False) -> MObject:
        """This method duplicates the DAG hierarchy rooted at the current node."""
    @staticmethod
    def enableDGTiming(enable: bool) -> None:
        """Globally enables or disables the DG node timing mechanism."""
    def enableLimit(self, type: int, flag: bool) -> MStatus:
        """Enable or disable the limit value for the specified limit type."""
    def endPointIndex(self) -> int:
        """Returns the index of the end point of the DirectionManip."""
    def findAlias(self, alias: str, attrObj: MObject) -> bool:
        """Retrieves the attribute with the given alias."""
    @overload
    def findPlug(self, attr: MObject, wantNetworkedPlug: bool) -> MPlug: ...
    @overload
    def findPlug(self, attrName: str, wantNetworkedPlug: bool) -> MPlug: ...
    @overload
    def findPlug(self, attr: MObject) -> MPlug: ...
    @overload
    def findPlug(self, attrName: str) -> MPlug:
        """Attempt to find a plug for the given attribute."""
    def fullPathName(self) -> str:
        """Return a string representing the full path from the root of the dag to this object."""
    def getAffectedAttributes(self, attr: MObject, affectedAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that are affected by the attribute passed in."""
    def getAffectedByAttributes(self, attr: MObject, affectedByAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that affect the attribute passed in, attr ."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute al"""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns a list of all attribute aliases for this node."""
    def getAllPaths(self, paths: MDagPathArray) -> MStatus:
        """Determines all DAG Paths to the DAG Node attached to the Function Set."""
    def getConnectedSetsAndMembers(self, instanceNumber: int, sets: MObjectArray, comps: MObjectArray, renderableSetsOnly: bool) -> MStatus:
        """Returns all the sets connected to the specified instance of this DAG object."""
    def getConnections(self, array: MPlugArray) -> MStatus:
        """Get all of the current connections to this node as an array of plugs."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> MStatus:
        """Returns the external content (files) that this node depends on."""
    def getPath(self, path: MDagPath) -> MStatus:
        """Returns a DAG Path to the DAG Node attached to the Function Set."""
    @overload
    def getRotation(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def getRotation(self, rotation: MEulerRotation) -> MStatus: ...
    @overload
    def getRotation(self, order: int) -> MStatus: ...
    @overload
    def getRotation(self, order: int, space: int) -> MStatus:
        """Retrieve the rotation component of this transformation as a quaternion."""
    def getRotationQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Retrieve the rotation component of this transformation as a quaternion."""
    def getScale(self) -> MStatus:
        """Retrieve the scaling component of this transformation."""
    def getShear(self) -> MStatus:
        """Retrieve the shearing component of this transformation."""
    def getTranslation(self, space: int) -> MVector:
        """Retrieve the translation component of this transformation in centimeters."""
    @staticmethod
    def globalSize() -> float:
        """Returns the global manipulator size."""
    @staticmethod
    def handleSize() -> float:
        """Returns the manipulator handle size."""
    def hasAttribute(self, name: str) -> bool:
        """Returns true if the node already has an attribute with the given name."""
    def hasChild(self, node: MObject) -> bool:
        """Determines whether or not the given Node is a child of the DAG Node attached to the Function Set."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    def hasParent(self, node: MObject) -> bool:
        """Determines whether or not the given Node is a parent of the DAG Node attached to the Function Set."""
    def hasUniqueName(self) -> bool:
        """Indicates whether or not this node's name is unique within the scene."""
    def hiliteColor(self) -> MColor:
        """Determines the current hilite color used by the node."""
    def icon(self) -> str:
        """Returns the custom icon filename associated with the node."""
    def inModel(self) -> bool:
        """Determines whether or not the DAG Node is in the model."""
    def inUnderWorld(self) -> bool:
        """Determines whether or not the DAG Node is an underworld node."""
    def instanceCount(self, total: bool) -> int:
        """Determines the number of times the Node attached to the Function Set is instanced."""
    def isChildOf(self, node: MObject) -> bool:
        """Determines whether or not the DAG Node attached to the Function Set is a child of the given node."""
    def isDefaultNode(self) -> bool:
        """Returns true if the node is a default node."""
    def isFlagSet(self, flag: int) -> bool:
        """Retrieves the current state of the specified flag for a node."""
    def isFromReferencedFile(self) -> bool:
        """Indicates whether or not this node came from a referenced file."""
    def isInstanceable(self) -> bool:
        """Returns true if the DAG node can be instanced, and false otherwise."""
    def isInstanced(self, indirect: bool = True) -> bool:
        """Determines whether the DAG Node attached to the Function Set is directly or indirectly instanced."""
    def isInstancedAttribute(self, attr: MObject) -> bool:
        """Returns true if the specified attribute is instanced."""
    def isIntermediateObject(self) -> bool:
        """Returns true if this object is an intermediate in a geometry calculation."""
    def isLimited(self, type: int) -> bool:
        """Determine if the specified limit attribute is enabled or disabled."""
    def isLocked(self) -> bool:
        """Indicates whether or not this node is locked."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Indicates whether or not the specified attribute was added to this node within the current scene."""
    def isOptimizePlaybackOn(self) -> bool:
        """Returns whether or not optimize playback is on."""
    def isParentOf(self, node: MObject) -> bool:
        """Determines whether or not the DAG Node attached to the Function Set is a parent of the given node."""
    def isShared(self) -> bool:
        """Indicates whether or not this node is shared."""
    def isTrackingEdits(self) -> bool:
        """Returns whether or not edits on the given node are being tracked by the generalized edit system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def isVisible(self) -> bool:
        """Returns whether or not the manipulator is visible."""
    def limitValue(self, type: int) -> float:
        """Determine the current value of the specified limit."""
    @staticmethod
    def lineSize() -> float:
        """Returns the manipulator line size."""
    def manipScale(self) -> float:
        """Returns the manipulator scale."""
    def model(self) -> MObject:
        """Deprecated in 2016.0"""
    def name(self) -> str:
        """Returns the name of this node."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def objectColor(self) -> int:
        """Deprecated in 2016.0"""
    def objectColorIndex(self) -> int:
        """Determines the index for the current user defined inactive color used by the node."""
    def objectColorRGB(self) -> MColor:
        """Determines the RGB color for the current user defined inactive color used by the node."""
    def objectColorType(self) -> Any:
        """Determines whether or not the user defined inactive color will be used for the node, or whether the default inactive col"""
    def objectGroupComponent(self, *args: Any, **kwargs: Any) -> Any: ...
    def parent(self, i: int) -> MObject:
        """Queries the DAG Node attached to the Function Set for the parent Node corresponding to the given index."""
    def parentCount(self) -> int:
        """Determines the number of parent Nodes of the Node."""
    def parentNamespace(self) -> str:
        """Returns the name of the namespace in which this node resides."""
    def partialPathName(self) -> str:
        """Return a string representing the partial path from the root of the dag to this object."""
    def pluginName(self) -> str:
        """Returns the name of the plug-in this MFnDependendencyNode was defined in."""
    def plugsAlias(self, plug: MPlug) -> str:
        """Returns the alias for the plug's attribute or the empty string if that attribute has no alias."""
    @overload
    def removeAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def removeAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Remove a dynamic attribute from a node."""
    def removeChild(self, child: MObject) -> MStatus:
        """Removes the given DAG Node from the parent."""
    def removeChildAt(self, index: int) -> MStatus:
        """Removes the child at the given index from the parent."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Some nodes, such as the various animCurve nodes, require that their attributes be set in a specific order for proper ope"""
    def resetFromRestPosition(self) -> MStatus:
        """Reset the transform to its rest position."""
    def resetTransformation(self, m: MMatrix) -> MStatus:
        """Reset this transform to equal the given matrix in world space."""
    def restPosition(self) -> MTransformationMatrix:
        """Retrieve the saved rest position of this transform."""
    @overload
    def rotateBy(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def rotateBy(self, rotation: MEulerRotation, Space: int | None = None) -> MStatus: ...
    @overload
    def rotateBy(self, order: int, Space: int | None = None) -> MStatus:
        """Relatively change the rotation of this transformation using a quaternion."""
    def rotateByQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Relatively change the rotation of this transformation using a quaternion."""
    def rotateOrientation(self, space: int) -> MQuaternion:
        """Returns the rotation used to orient the local rotation space."""
    def rotatePivot(self, space: int) -> MPoint:
        """Returns the pivot about which the rotation is applied."""
    def rotatePivotTranslation(self, space: int) -> MVector:
        """Return the rotate pivot translation in centimeters."""
    def rotateXYZValue(self, valIndex: int) -> MEulerRotation:
        """Gets the rotation for the active manipulator."""
    def rotationOrder(self) -> int:
        """Returns the rotation order for the transform matrix - the order in which the Euler angles are applied to create the end """
    def scaleBy(self) -> MStatus:
        """Relatively scale this transformation."""
    def scalePivot(self, space: int) -> MPoint:
        """Returns the pivot around which the scale is applied."""
    def scalePivotTranslation(self, space: int) -> MVector:
        """Returns the scale pivot translation in centimeters."""
    def set(self, transform: MTransformationMatrix) -> MStatus:
        """Change this transform to equal the given matrix."""
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setDirection(self, direction: MVector) -> MStatus:
        """Sets the direction of the DirectionManip."""
    def setDoNotWrite(self, flag: bool) -> MStatus:
        """Use this method to mark the "do not write" state of this node."""
    @staticmethod
    def setDrawPlaneHandles(drawPlaneHandles: bool) -> None:
        """Sets the global option to display planar handles or not on supported manipulators."""
    def setDrawStart(self, state: bool) -> MStatus:
        """Sets whether or not to draw the start of the DirectionManip."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> MStatus:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> MStatus:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> MStatus:
        """Sets the state of the specified flag for the node."""
    @staticmethod
    def setGlobalSize(size: float) -> None:
        """Sets the global manipulator size."""
    @staticmethod
    def setHandleSize(size: float) -> None:
        """Sets the manipulator handle size."""
    def setIcon(self, filename: str) -> MStatus:
        """Associates a custom icon with the node for display in the Maya UI."""
    def setInstanceable(self, how: bool) -> MStatus:
        """Sets whether or not the DAG node is instanceable."""
    def setIntermediateObject(self, isIntermediate: bool) -> MStatus:
        """Sets whether this object is an intermediate in a geometry calculation."""
    def setLimit(self, type: int, value: float) -> MStatus:
        """Change the limit value for the specified limit type, and automatically enable the limit to be true."""
    @staticmethod
    def setLineSize(size: float) -> None:
        """Sets the manipulator line size."""
    def setLocked(self, locked: bool) -> MStatus:
        """Locks or unlocks this node."""
    def setManipScale(self, size: float) -> MStatus:
        """Sets the manipulator scale."""
    @overload
    def setName(self, name: str, createNamespace: bool = False) -> str: ...
    @overload
    def setName(self, name: str) -> str:
        """Sets the name of this node."""
    def setNormalizeDirection(self, state: bool) -> MStatus:
        """Sets whether or not to the direction should be normalized."""
    @overload
    def setObject(self, path: MDagPath) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches Function Set to the DAG Node that has the given DAG Path."""
    @overload
    def setObjectColor(self, color: int) -> MStatus: ...
    @overload
    def setObjectColor(self, color: MColor) -> MStatus:
        """Sets the index for the current user defined inactive color used by the node."""
    def setObjectColorType(self, type: Any) -> MStatus:
        """Sets whether or not the user defined inactive object color will be used."""
    def setOptimizePlayback(self, optimizePlayback: bool) -> MStatus:
        """Sets whether or not to optimize the playback."""
    def setRestPosition(self, matrix: MTransformationMatrix) -> MStatus:
        """Change the saved rest position of this transform."""
    def setRotateOrientation(self, quat: MQuaternion, space: int, balance: bool) -> MStatus:
        """Set the rotation used to orient the local rotation space."""
    def setRotatePivot(self, point: MPoint, space: int, balance: bool) -> MStatus:
        """Set the rotate pivot in centimeters about which rotation is applied."""
    def setRotatePivotTranslation(self, vec: MVector, space: int) -> MStatus:
        """Set the rotate pivot translation in centimeters."""
    @overload
    def setRotation(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def setRotation(self, rotation: MEulerRotation) -> MStatus: ...
    @overload
    def setRotation(self, order: int) -> MStatus: ...
    @overload
    def setRotation(self, RotationOrder: int, space: int) -> MStatus:
        """Change the rotation component of this transformation using a quaternion."""
    def setRotationOrder(self, order: int, reorder: bool) -> MStatus:
        """Change the rotation order for the transform - the order in which the Euler angles are applied to create the end rotation"""
    def setRotationQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Change the rotation component of this transformation using a quaternion."""
    def setScale(self) -> MStatus:
        """Set the scaling component of this transformation."""
    def setScalePivot(self, point: MPoint, space: int, balance: bool) -> MStatus:
        """Set the pivot around which the scale is applied in centimeters."""
    def setScalePivotTranslation(self, vec: MVector, space: int) -> MStatus:
        """Set the scale pivot translation in centimeters."""
    def setShear(self) -> MStatus:
        """Set the shearing component of this transformation."""
    def setStartPoint(self, startPoint: MPoint) -> MStatus:
        """Sets the start point of the DirectionManip."""
    def setTranslation(self, vec: MVector, space: int) -> MStatus:
        """Change the translation component of this transformation."""
    def setUseObjectColor(self, useObjectColor: bool) -> MStatus:
        """Deprecated in 2016.0"""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def setVisible(self, isVisible: bool) -> MStatus:
        """Sets whether or not the manipulator is visible."""
    def shearBy(self) -> MStatus:
        """Relatively shear this transformation."""
    def startPointIndex(self) -> int:
        """Returns the index of the start point of the DirectionManip."""
    def transformation(self) -> MTransformationMatrix:
        """Retrieve the transformation matrix represented by this transform."""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
    def translateBy(self, vec: MVector, space: int) -> MStatus:
        """Relatively change the translation component of this transformation."""
    def translation(self, Space: int) -> MVector:
        """Deprecated in 2018.0"""
    def type(self) -> int:
        """Function set type."""
    def typeId(self) -> MTypeId:
        """Returns the type id of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""
    @staticmethod
    def typeString(Type: int) -> str:
        """Introduced in 2020.0"""
    def uniqueName(self) -> str:
        """Introduced in 2023.0"""
    def userNode(self) -> Any:
        """If the function set's node is a plug-in node, then this method will extract the MPxNode pointer from it."""
    def usingHiliteColor(self) -> bool:
        """Determines whether or not the hilite color will be used for the node."""
    def usingObjectColor(self) -> bool:
        """Deprecated in 2016.0"""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnDiscManip:
    kExtensionAttr: Any
    kInvalidAttr: Any
    kLocalDynamicAttr: Any
    kNextPos: Any
    kNormalAttr: Any
    kRotateMaxX: Any
    kRotateMaxY: Any
    kRotateMaxZ: Any
    kRotateMinX: Any
    kRotateMinY: Any
    kRotateMinZ: Any
    kScaleMaxX: Any
    kScaleMaxY: Any
    kScaleMaxZ: Any
    kScaleMinX: Any
    kScaleMinY: Any
    kScaleMinZ: Any
    kShearMaxXY: Any
    kShearMaxXZ: Any
    kShearMaxYZ: Any
    kShearMinXY: Any
    kShearMinXZ: Any
    kShearMinYZ: Any
    kTimerInvalidState: Any
    kTimerMetric_callback: Any
    kTimerMetric_callbackNotViaAPI: Any
    kTimerMetric_callbackViaAPI: Any
    kTimerMetric_compute: Any
    kTimerMetric_computeDuringCallback: Any
    kTimerMetric_computeNotDuringCallback: Any
    kTimerMetric_dirty: Any
    kTimerMetric_draw: Any
    kTimerMetric_fetch: Any
    kTimerMetrics: Any
    kTimerOff: Any
    kTimerOn: Any
    kTimerType_count: Any
    kTimerType_inclusive: Any
    kTimerType_self: Any
    kTimerTypes: Any
    kTimerUninitialized: Any
    kTranslateMaxX: Any
    kTranslateMaxY: Any
    kTranslateMaxZ: Any
    kTranslateMinX: Any
    kTranslateMinY: Any
    kTranslateMinZ: Any
    kUseDefaultColor: Any
    kUseIndexColor: Any
    kUseRGBColor: Any
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None: ...
    @overload
    def __init__(self, object: MDagPath) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None:
        """Default constructor."""
    def absoluteName(self) -> str:
        """Returns the absolute name of this node."""
    def activeColor(self) -> MColor:
        """Determines the active color used by this node."""
    @overload
    def addAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def addAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Add a new dynamic attibute to this node."""
    def addChild(self, child: MObject, index: int, keepExistingParents: bool = False) -> MStatus:
        """Makes the given DAG Node a child of the DAG Node to which this instance of the Function Set is attached."""
    def addExternalContentForFileAttr(self, table: MExternalContentInfoTable, attr: MObject) -> MStatus:
        """Adds content info to the specified table from a file path attribute."""
    def affectsAnimation(self) -> bool:
        """Introduced in 2019.0"""
    @staticmethod
    def allocateFlag(pluginName: str) -> int:
        """Allocates a node flag for sole use by the caller."""
    def angleIndex(self) -> int:
        """Returns the index of the angle."""
    @overload
    def attribute(self, index: int) -> MObject: ...
    @overload
    def attribute(self, attrName: str) -> MObject:
        """Finds the attribute of this node at the given index."""
    def attributeClass(self, attr: MObject) -> Any:
        """Returns the class (normal, dynamic, extension) of the specified attribute."""
    def attributeCount(self) -> int:
        """Returns the number of attributes that this node has."""
    def axisIndex(self) -> int:
        """Returns the index of the axis of the DiscManip."""
    @staticmethod
    def balanceTransformation(identity: int, identity_: int, one: int, kXYZ: int, arg: Any = True) -> None:
        """Balance a transformation when applying a world matrix to a joint."""
    def boundingBox(self) -> Any:
        """Returns the bounding box for the dag node in object space."""
    def canBeWritten(self) -> bool:
        """Returns the do not write state of the node."""
    def centerIndex(self) -> int:
        """Returns the index of the center of the DiscManip."""
    def child(self, i: int) -> MObject:
        """Queries the DAG Node attached to the Function Set for the child Node corresponding to the given index."""
    def childCount(self) -> int:
        """Determines the number of child Nodes of the Node."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def classification(nodeTypeName: str) -> str:
        """Retrieves the classification string for a node type."""
    def clearRestPosition(self) -> MStatus:
        """Clear the saved rest position of this transform."""
    def connectToAnglePlug(self, anglePlug: MPlug) -> MStatus:
        """Connect to the angle plug."""
    @overload
    def create(self) -> MObject: ...
    @overload
    def create(self, manipName: str, angleName: str) -> MObject: ...
    @overload
    def create(self, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, type: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, type: str, name: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str) -> MObject: ...
    @overload
    def create(self, type: str) -> MObject: ...
    @overload
    def create(self, type: str, name: str) -> MObject:
        """Creates a new DiscManip."""
    def dagPath(self) -> MDagPath:
        """Returns the DagPath to which the Function Set is attached."""
    def dagRoot(self) -> MObject:
        """Determines the root of the first DAG Path to the DAG Node attached to the Function Set."""
    @staticmethod
    def deallocateAllFlags(pluginName: str) -> MStatus:
        """Deallocates all of the node flags which are currently allocated to the specified plugin."""
    @staticmethod
    def deallocateFlag(pluginName: str, flag: int) -> MStatus:
        """Deallocates a node flag which was previously allocated by a call to allocateFlag ."""
    @staticmethod
    def deleteManipulator(manip: MObject) -> MStatus:
        """Delete a manipulator."""
    def dgCallbackIds(self, type: Any, callbackName: str, callbackId: MCallbackIdArray, value: MDoubleArray) -> MStatus:
        """This method provides a further breakdown of the per-callback time returned via dgCallbacks() by returning the data on a """
    def dgCallbacks(self, type: Any, callbackName: Any, value: MDoubleArray) -> MStatus:
        """Node callbacks that occur when timing is enabled get logged with the node and can be queried via this method."""
    def dgTimer(self, timerMetric: Any, timerType: Any) -> float:
        """The function returns the specified timer value for the current node."""
    def dgTimerOff(self) -> MStatus:
        """Indicates that this node should no longer collect DG timing data when DG timing is enabled."""
    def dgTimerOn(self) -> MStatus:
        """Indicates that this node should collect DG timing data whenever DG timing is enabled."""
    def dgTimerQueryState(self) -> Any:
        """The function returns the current on/off state of the node's timer."""
    def dgTimerReset(self) -> MStatus:
        """The function resets the dependency graph timers and counters for this node to zero."""
    def dormantColor(self) -> MColor:
        """Determines the dormant color used by this node."""
    def drawOverrideColor(self, color: MColor) -> bool:
        """Determines the draw override color used by this node."""
    def drawOverrideEnabled(self) -> bool:
        """Determines whether or not draw override is turned on for this node."""
    def drawOverrideIsReference(self) -> bool:
        """Determines whether or not Display Type of the draw override is Reference for this node."""
    def drawOverrideIsTemplate(self) -> bool:
        """Determines whether or not Display Type of the draw override is Template for this node."""
    @staticmethod
    def drawPlaneHandles() -> bool:
        """This method returns the global option that says if the planar manipulator handles should be drawn or not."""
    def duplicate(self, instance: bool = False, instanceLeaf: bool = False) -> MObject:
        """This method duplicates the DAG hierarchy rooted at the current node."""
    @staticmethod
    def enableDGTiming(enable: bool) -> None:
        """Globally enables or disables the DG node timing mechanism."""
    def enableLimit(self, type: int, flag: bool) -> MStatus:
        """Enable or disable the limit value for the specified limit type."""
    def findAlias(self, alias: str, attrObj: MObject) -> bool:
        """Retrieves the attribute with the given alias."""
    @overload
    def findPlug(self, attr: MObject, wantNetworkedPlug: bool) -> MPlug: ...
    @overload
    def findPlug(self, attrName: str, wantNetworkedPlug: bool) -> MPlug: ...
    @overload
    def findPlug(self, attr: MObject) -> MPlug: ...
    @overload
    def findPlug(self, attrName: str) -> MPlug:
        """Attempt to find a plug for the given attribute."""
    def fullPathName(self) -> str:
        """Return a string representing the full path from the root of the dag to this object."""
    def getAffectedAttributes(self, attr: MObject, affectedAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that are affected by the attribute passed in."""
    def getAffectedByAttributes(self, attr: MObject, affectedByAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that affect the attribute passed in, attr ."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute al"""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns a list of all attribute aliases for this node."""
    def getAllPaths(self, paths: MDagPathArray) -> MStatus:
        """Determines all DAG Paths to the DAG Node attached to the Function Set."""
    def getConnectedSetsAndMembers(self, instanceNumber: int, sets: MObjectArray, comps: MObjectArray, renderableSetsOnly: bool) -> MStatus:
        """Returns all the sets connected to the specified instance of this DAG object."""
    def getConnections(self, array: MPlugArray) -> MStatus:
        """Get all of the current connections to this node as an array of plugs."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> MStatus:
        """Returns the external content (files) that this node depends on."""
    def getPath(self, path: MDagPath) -> MStatus:
        """Returns a DAG Path to the DAG Node attached to the Function Set."""
    @overload
    def getRotation(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def getRotation(self, rotation: MEulerRotation) -> MStatus: ...
    @overload
    def getRotation(self, order: int) -> MStatus: ...
    @overload
    def getRotation(self, order: int, space: int) -> MStatus:
        """Retrieve the rotation component of this transformation as a quaternion."""
    def getRotationQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Retrieve the rotation component of this transformation as a quaternion."""
    def getScale(self) -> MStatus:
        """Retrieve the scaling component of this transformation."""
    def getShear(self) -> MStatus:
        """Retrieve the shearing component of this transformation."""
    def getTranslation(self, space: int) -> MVector:
        """Retrieve the translation component of this transformation in centimeters."""
    @staticmethod
    def globalSize() -> float:
        """Returns the global manipulator size."""
    @staticmethod
    def handleSize() -> float:
        """Returns the manipulator handle size."""
    def hasAttribute(self, name: str) -> bool:
        """Returns true if the node already has an attribute with the given name."""
    def hasChild(self, node: MObject) -> bool:
        """Determines whether or not the given Node is a child of the DAG Node attached to the Function Set."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    def hasParent(self, node: MObject) -> bool:
        """Determines whether or not the given Node is a parent of the DAG Node attached to the Function Set."""
    def hasUniqueName(self) -> bool:
        """Indicates whether or not this node's name is unique within the scene."""
    def hiliteColor(self) -> MColor:
        """Determines the current hilite color used by the node."""
    def icon(self) -> str:
        """Returns the custom icon filename associated with the node."""
    def inModel(self) -> bool:
        """Determines whether or not the DAG Node is in the model."""
    def inUnderWorld(self) -> bool:
        """Determines whether or not the DAG Node is an underworld node."""
    def instanceCount(self, total: bool) -> int:
        """Determines the number of times the Node attached to the Function Set is instanced."""
    def isChildOf(self, node: MObject) -> bool:
        """Determines whether or not the DAG Node attached to the Function Set is a child of the given node."""
    def isDefaultNode(self) -> bool:
        """Returns true if the node is a default node."""
    def isFlagSet(self, flag: int) -> bool:
        """Retrieves the current state of the specified flag for a node."""
    def isFromReferencedFile(self) -> bool:
        """Indicates whether or not this node came from a referenced file."""
    def isInstanceable(self) -> bool:
        """Returns true if the DAG node can be instanced, and false otherwise."""
    def isInstanced(self, indirect: bool = True) -> bool:
        """Determines whether the DAG Node attached to the Function Set is directly or indirectly instanced."""
    def isInstancedAttribute(self, attr: MObject) -> bool:
        """Returns true if the specified attribute is instanced."""
    def isIntermediateObject(self) -> bool:
        """Returns true if this object is an intermediate in a geometry calculation."""
    def isLimited(self, type: int) -> bool:
        """Determine if the specified limit attribute is enabled or disabled."""
    def isLocked(self) -> bool:
        """Indicates whether or not this node is locked."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Indicates whether or not the specified attribute was added to this node within the current scene."""
    def isOptimizePlaybackOn(self) -> bool:
        """Returns whether or not optimize playback is on."""
    def isParentOf(self, node: MObject) -> bool:
        """Determines whether or not the DAG Node attached to the Function Set is a parent of the given node."""
    def isShared(self) -> bool:
        """Indicates whether or not this node is shared."""
    def isTrackingEdits(self) -> bool:
        """Returns whether or not edits on the given node are being tracked by the generalized edit system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def isVisible(self) -> bool:
        """Returns whether or not the manipulator is visible."""
    def limitValue(self, type: int) -> float:
        """Determine the current value of the specified limit."""
    @staticmethod
    def lineSize() -> float:
        """Returns the manipulator line size."""
    def manipScale(self) -> float:
        """Returns the manipulator scale."""
    def model(self) -> MObject:
        """Deprecated in 2016.0"""
    def name(self) -> str:
        """Returns the name of this node."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def objectColor(self) -> int:
        """Deprecated in 2016.0"""
    def objectColorIndex(self) -> int:
        """Determines the index for the current user defined inactive color used by the node."""
    def objectColorRGB(self) -> MColor:
        """Determines the RGB color for the current user defined inactive color used by the node."""
    def objectColorType(self) -> Any:
        """Determines whether or not the user defined inactive color will be used for the node, or whether the default inactive col"""
    def objectGroupComponent(self, *args: Any, **kwargs: Any) -> Any: ...
    def parent(self, i: int) -> MObject:
        """Queries the DAG Node attached to the Function Set for the parent Node corresponding to the given index."""
    def parentCount(self) -> int:
        """Determines the number of parent Nodes of the Node."""
    def parentNamespace(self) -> str:
        """Returns the name of the namespace in which this node resides."""
    def partialPathName(self) -> str:
        """Return a string representing the partial path from the root of the dag to this object."""
    def pluginName(self) -> str:
        """Returns the name of the plug-in this MFnDependendencyNode was defined in."""
    def plugsAlias(self, plug: MPlug) -> str:
        """Returns the alias for the plug's attribute or the empty string if that attribute has no alias."""
    @overload
    def removeAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def removeAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Remove a dynamic attribute from a node."""
    def removeChild(self, child: MObject) -> MStatus:
        """Removes the given DAG Node from the parent."""
    def removeChildAt(self, index: int) -> MStatus:
        """Removes the child at the given index from the parent."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Some nodes, such as the various animCurve nodes, require that their attributes be set in a specific order for proper ope"""
    def resetFromRestPosition(self) -> MStatus:
        """Reset the transform to its rest position."""
    def resetTransformation(self, m: MMatrix) -> MStatus:
        """Reset this transform to equal the given matrix in world space."""
    def restPosition(self) -> MTransformationMatrix:
        """Retrieve the saved rest position of this transform."""
    @overload
    def rotateBy(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def rotateBy(self, rotation: MEulerRotation, Space: int | None = None) -> MStatus: ...
    @overload
    def rotateBy(self, order: int, Space: int | None = None) -> MStatus:
        """Relatively change the rotation of this transformation using a quaternion."""
    def rotateByQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Relatively change the rotation of this transformation using a quaternion."""
    def rotateOrientation(self, space: int) -> MQuaternion:
        """Returns the rotation used to orient the local rotation space."""
    def rotatePivot(self, space: int) -> MPoint:
        """Returns the pivot about which the rotation is applied."""
    def rotatePivotTranslation(self, space: int) -> MVector:
        """Return the rotate pivot translation in centimeters."""
    def rotateXYZValue(self, valIndex: int) -> MEulerRotation:
        """Gets the rotation for the active manipulator."""
    def rotationOrder(self) -> int:
        """Returns the rotation order for the transform matrix - the order in which the Euler angles are applied to create the end """
    def scaleBy(self) -> MStatus:
        """Relatively scale this transformation."""
    def scalePivot(self, space: int) -> MPoint:
        """Returns the pivot around which the scale is applied."""
    def scalePivotTranslation(self, space: int) -> MVector:
        """Returns the scale pivot translation in centimeters."""
    def set(self, transform: MTransformationMatrix) -> MStatus:
        """Change this transform to equal the given matrix."""
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setAngle(self, angle: MAngle) -> MStatus:
        """Sets the angle of the DiscManip."""
    def setCenterPoint(self, centerPoint: MPoint) -> MStatus:
        """Sets the center point of the DiscManip."""
    def setDoNotWrite(self, flag: bool) -> MStatus:
        """Use this method to mark the "do not write" state of this node."""
    @staticmethod
    def setDrawPlaneHandles(drawPlaneHandles: bool) -> None:
        """Sets the global option to display planar handles or not on supported manipulators."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> MStatus:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> MStatus:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> MStatus:
        """Sets the state of the specified flag for the node."""
    @staticmethod
    def setGlobalSize(size: float) -> None:
        """Sets the global manipulator size."""
    @staticmethod
    def setHandleSize(size: float) -> None:
        """Sets the manipulator handle size."""
    def setIcon(self, filename: str) -> MStatus:
        """Associates a custom icon with the node for display in the Maya UI."""
    def setInstanceable(self, how: bool) -> MStatus:
        """Sets whether or not the DAG node is instanceable."""
    def setIntermediateObject(self, isIntermediate: bool) -> MStatus:
        """Sets whether this object is an intermediate in a geometry calculation."""
    def setLimit(self, type: int, value: float) -> MStatus:
        """Change the limit value for the specified limit type, and automatically enable the limit to be true."""
    @staticmethod
    def setLineSize(size: float) -> None:
        """Sets the manipulator line size."""
    def setLocked(self, locked: bool) -> MStatus:
        """Locks or unlocks this node."""
    def setManipScale(self, size: float) -> MStatus:
        """Sets the manipulator scale."""
    @overload
    def setName(self, name: str, createNamespace: bool = False) -> str: ...
    @overload
    def setName(self, name: str) -> str:
        """Sets the name of this node."""
    def setNormal(self, normal: MVector) -> MStatus:
        """Sets the normal of the DiscManip."""
    @overload
    def setObject(self, path: MDagPath) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches Function Set to the DAG Node that has the given DAG Path."""
    @overload
    def setObjectColor(self, color: int) -> MStatus: ...
    @overload
    def setObjectColor(self, color: MColor) -> MStatus:
        """Sets the index for the current user defined inactive color used by the node."""
    def setObjectColorType(self, type: Any) -> MStatus:
        """Sets whether or not the user defined inactive object color will be used."""
    def setOptimizePlayback(self, optimizePlayback: bool) -> MStatus:
        """Sets whether or not to optimize the playback."""
    def setRadius(self, radius: float) -> MStatus:
        """Sets the radius of the DiscManip."""
    def setRestPosition(self, matrix: MTransformationMatrix) -> MStatus:
        """Change the saved rest position of this transform."""
    def setRotateOrientation(self, quat: MQuaternion, space: int, balance: bool) -> MStatus:
        """Set the rotation used to orient the local rotation space."""
    def setRotatePivot(self, point: MPoint, space: int, balance: bool) -> MStatus:
        """Set the rotate pivot in centimeters about which rotation is applied."""
    def setRotatePivotTranslation(self, vec: MVector, space: int) -> MStatus:
        """Set the rotate pivot translation in centimeters."""
    @overload
    def setRotation(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def setRotation(self, rotation: MEulerRotation) -> MStatus: ...
    @overload
    def setRotation(self, order: int) -> MStatus: ...
    @overload
    def setRotation(self, RotationOrder: int, space: int) -> MStatus:
        """Change the rotation component of this transformation using a quaternion."""
    def setRotationOrder(self, order: int, reorder: bool) -> MStatus:
        """Change the rotation order for the transform - the order in which the Euler angles are applied to create the end rotation"""
    def setRotationQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Change the rotation component of this transformation using a quaternion."""
    def setScale(self) -> MStatus:
        """Set the scaling component of this transformation."""
    def setScalePivot(self, point: MPoint, space: int, balance: bool) -> MStatus:
        """Set the pivot around which the scale is applied in centimeters."""
    def setScalePivotTranslation(self, vec: MVector, space: int) -> MStatus:
        """Set the scale pivot translation in centimeters."""
    def setShear(self) -> MStatus:
        """Set the shearing component of this transformation."""
    def setTranslation(self, vec: MVector, space: int) -> MStatus:
        """Change the translation component of this transformation."""
    def setUseObjectColor(self, useObjectColor: bool) -> MStatus:
        """Deprecated in 2016.0"""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def setVisible(self, isVisible: bool) -> MStatus:
        """Sets whether or not the manipulator is visible."""
    def shearBy(self) -> MStatus:
        """Relatively shear this transformation."""
    def transformation(self) -> MTransformationMatrix:
        """Retrieve the transformation matrix represented by this transform."""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
    def translateBy(self, vec: MVector, space: int) -> MStatus:
        """Relatively change the translation component of this transformation."""
    def translation(self, Space: int) -> MVector:
        """Deprecated in 2018.0"""
    def type(self) -> int:
        """Function set type."""
    def typeId(self) -> MTypeId:
        """Returns the type id of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""
    @staticmethod
    def typeString(Type: int) -> str:
        """Introduced in 2020.0"""
    def uniqueName(self) -> str:
        """Introduced in 2023.0"""
    def userNode(self) -> Any:
        """If the function set's node is a plug-in node, then this method will extract the MPxNode pointer from it."""
    def usingHiliteColor(self) -> bool:
        """Determines whether or not the hilite color will be used for the node."""
    def usingObjectColor(self) -> bool:
        """Deprecated in 2016.0"""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnDistanceManip:
    kExtensionAttr: Any
    kInvalidAttr: Any
    kLocalDynamicAttr: Any
    kNextPos: Any
    kNormalAttr: Any
    kRotateMaxX: Any
    kRotateMaxY: Any
    kRotateMaxZ: Any
    kRotateMinX: Any
    kRotateMinY: Any
    kRotateMinZ: Any
    kScaleMaxX: Any
    kScaleMaxY: Any
    kScaleMaxZ: Any
    kScaleMinX: Any
    kScaleMinY: Any
    kScaleMinZ: Any
    kShearMaxXY: Any
    kShearMaxXZ: Any
    kShearMaxYZ: Any
    kShearMinXY: Any
    kShearMinXZ: Any
    kShearMinYZ: Any
    kTimerInvalidState: Any
    kTimerMetric_callback: Any
    kTimerMetric_callbackNotViaAPI: Any
    kTimerMetric_callbackViaAPI: Any
    kTimerMetric_compute: Any
    kTimerMetric_computeDuringCallback: Any
    kTimerMetric_computeNotDuringCallback: Any
    kTimerMetric_dirty: Any
    kTimerMetric_draw: Any
    kTimerMetric_fetch: Any
    kTimerMetrics: Any
    kTimerOff: Any
    kTimerOn: Any
    kTimerType_count: Any
    kTimerType_inclusive: Any
    kTimerType_self: Any
    kTimerTypes: Any
    kTimerUninitialized: Any
    kTranslateMaxX: Any
    kTranslateMaxY: Any
    kTranslateMaxZ: Any
    kTranslateMinX: Any
    kTranslateMinY: Any
    kTranslateMinZ: Any
    kUseDefaultColor: Any
    kUseIndexColor: Any
    kUseRGBColor: Any
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None: ...
    @overload
    def __init__(self, object: MDagPath) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None:
        """Default constructor."""
    def absoluteName(self) -> str:
        """Returns the absolute name of this node."""
    def activeColor(self) -> MColor:
        """Determines the active color used by this node."""
    @overload
    def addAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def addAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Add a new dynamic attibute to this node."""
    def addChild(self, child: MObject, index: int, keepExistingParents: bool = False) -> MStatus:
        """Makes the given DAG Node a child of the DAG Node to which this instance of the Function Set is attached."""
    def addExternalContentForFileAttr(self, table: MExternalContentInfoTable, attr: MObject) -> MStatus:
        """Adds content info to the specified table from a file path attribute."""
    def affectsAnimation(self) -> bool:
        """Introduced in 2019.0"""
    @staticmethod
    def allocateFlag(pluginName: str) -> int:
        """Allocates a node flag for sole use by the caller."""
    @overload
    def attribute(self, index: int) -> MObject: ...
    @overload
    def attribute(self, attrName: str) -> MObject:
        """Finds the attribute of this node at the given index."""
    def attributeClass(self, attr: MObject) -> Any:
        """Returns the class (normal, dynamic, extension) of the specified attribute."""
    def attributeCount(self) -> int:
        """Returns the number of attributes that this node has."""
    @staticmethod
    def balanceTransformation(identity: int, identity_: int, one: int, kXYZ: int, arg: Any = True) -> None:
        """Balance a transformation when applying a world matrix to a joint."""
    def boundingBox(self) -> Any:
        """Returns the bounding box for the dag node in object space."""
    def canBeWritten(self) -> bool:
        """Returns the do not write state of the node."""
    def child(self, i: int) -> MObject:
        """Queries the DAG Node attached to the Function Set for the child Node corresponding to the given index."""
    def childCount(self) -> int:
        """Determines the number of child Nodes of the Node."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def classification(nodeTypeName: str) -> str:
        """Retrieves the classification string for a node type."""
    def clearRestPosition(self) -> MStatus:
        """Clear the saved rest position of this transform."""
    def connectToDistancePlug(self, distancePlug: MPlug) -> MStatus:
        """Connect to the distance plug."""
    @overload
    def create(self) -> MObject: ...
    @overload
    def create(self, manipName: str, distanceName: str) -> MObject: ...
    @overload
    def create(self, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, type: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, type: str, name: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str) -> MObject: ...
    @overload
    def create(self, type: str) -> MObject: ...
    @overload
    def create(self, type: str, name: str) -> MObject:
        """Creates a new DistanceManip."""
    def currentPointIndex(self) -> int:
        """Returns the index of the current point of the DistanceManip."""
    def dagPath(self) -> MDagPath:
        """Returns the DagPath to which the Function Set is attached."""
    def dagRoot(self) -> MObject:
        """Determines the root of the first DAG Path to the DAG Node attached to the Function Set."""
    @staticmethod
    def deallocateAllFlags(pluginName: str) -> MStatus:
        """Deallocates all of the node flags which are currently allocated to the specified plugin."""
    @staticmethod
    def deallocateFlag(pluginName: str, flag: int) -> MStatus:
        """Deallocates a node flag which was previously allocated by a call to allocateFlag ."""
    @staticmethod
    def deleteManipulator(manip: MObject) -> MStatus:
        """Delete a manipulator."""
    def dgCallbackIds(self, type: Any, callbackName: str, callbackId: MCallbackIdArray, value: MDoubleArray) -> MStatus:
        """This method provides a further breakdown of the per-callback time returned via dgCallbacks() by returning the data on a """
    def dgCallbacks(self, type: Any, callbackName: Any, value: MDoubleArray) -> MStatus:
        """Node callbacks that occur when timing is enabled get logged with the node and can be queried via this method."""
    def dgTimer(self, timerMetric: Any, timerType: Any) -> float:
        """The function returns the specified timer value for the current node."""
    def dgTimerOff(self) -> MStatus:
        """Indicates that this node should no longer collect DG timing data when DG timing is enabled."""
    def dgTimerOn(self) -> MStatus:
        """Indicates that this node should collect DG timing data whenever DG timing is enabled."""
    def dgTimerQueryState(self) -> Any:
        """The function returns the current on/off state of the node's timer."""
    def dgTimerReset(self) -> MStatus:
        """The function resets the dependency graph timers and counters for this node to zero."""
    def directionIndex(self) -> int:
        """Returns the index of the direction."""
    def distanceIndex(self) -> int:
        """Returns the index of the distance."""
    def dormantColor(self) -> MColor:
        """Determines the dormant color used by this node."""
    def drawOverrideColor(self, color: MColor) -> bool:
        """Determines the draw override color used by this node."""
    def drawOverrideEnabled(self) -> bool:
        """Determines whether or not draw override is turned on for this node."""
    def drawOverrideIsReference(self) -> bool:
        """Determines whether or not Display Type of the draw override is Reference for this node."""
    def drawOverrideIsTemplate(self) -> bool:
        """Determines whether or not Display Type of the draw override is Template for this node."""
    @staticmethod
    def drawPlaneHandles() -> bool:
        """This method returns the global option that says if the planar manipulator handles should be drawn or not."""
    def duplicate(self, instance: bool = False, instanceLeaf: bool = False) -> MObject:
        """This method duplicates the DAG hierarchy rooted at the current node."""
    @staticmethod
    def enableDGTiming(enable: bool) -> None:
        """Globally enables or disables the DG node timing mechanism."""
    def enableLimit(self, type: int, flag: bool) -> MStatus:
        """Enable or disable the limit value for the specified limit type."""
    def findAlias(self, alias: str, attrObj: MObject) -> bool:
        """Retrieves the attribute with the given alias."""
    @overload
    def findPlug(self, attr: MObject, wantNetworkedPlug: bool) -> MPlug: ...
    @overload
    def findPlug(self, attrName: str, wantNetworkedPlug: bool) -> MPlug: ...
    @overload
    def findPlug(self, attr: MObject) -> MPlug: ...
    @overload
    def findPlug(self, attrName: str) -> MPlug:
        """Attempt to find a plug for the given attribute."""
    def fullPathName(self) -> str:
        """Return a string representing the full path from the root of the dag to this object."""
    def getAffectedAttributes(self, attr: MObject, affectedAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that are affected by the attribute passed in."""
    def getAffectedByAttributes(self, attr: MObject, affectedByAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that affect the attribute passed in, attr ."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute al"""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns a list of all attribute aliases for this node."""
    def getAllPaths(self, paths: MDagPathArray) -> MStatus:
        """Determines all DAG Paths to the DAG Node attached to the Function Set."""
    def getConnectedSetsAndMembers(self, instanceNumber: int, sets: MObjectArray, comps: MObjectArray, renderableSetsOnly: bool) -> MStatus:
        """Returns all the sets connected to the specified instance of this DAG object."""
    def getConnections(self, array: MPlugArray) -> MStatus:
        """Get all of the current connections to this node as an array of plugs."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> MStatus:
        """Returns the external content (files) that this node depends on."""
    def getPath(self, path: MDagPath) -> MStatus:
        """Returns a DAG Path to the DAG Node attached to the Function Set."""
    @overload
    def getRotation(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def getRotation(self, rotation: MEulerRotation) -> MStatus: ...
    @overload
    def getRotation(self, order: int) -> MStatus: ...
    @overload
    def getRotation(self, order: int, space: int) -> MStatus:
        """Retrieve the rotation component of this transformation as a quaternion."""
    def getRotationQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Retrieve the rotation component of this transformation as a quaternion."""
    def getScale(self) -> MStatus:
        """Retrieve the scaling component of this transformation."""
    def getShear(self) -> MStatus:
        """Retrieve the shearing component of this transformation."""
    def getTranslation(self, space: int) -> MVector:
        """Retrieve the translation component of this transformation in centimeters."""
    @staticmethod
    def globalSize() -> float:
        """Returns the global manipulator size."""
    @staticmethod
    def handleSize() -> float:
        """Returns the manipulator handle size."""
    def hasAttribute(self, name: str) -> bool:
        """Returns true if the node already has an attribute with the given name."""
    def hasChild(self, node: MObject) -> bool:
        """Determines whether or not the given Node is a child of the DAG Node attached to the Function Set."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    def hasParent(self, node: MObject) -> bool:
        """Determines whether or not the given Node is a parent of the DAG Node attached to the Function Set."""
    def hasUniqueName(self) -> bool:
        """Indicates whether or not this node's name is unique within the scene."""
    def hiliteColor(self) -> MColor:
        """Determines the current hilite color used by the node."""
    def icon(self) -> str:
        """Returns the custom icon filename associated with the node."""
    def inModel(self) -> bool:
        """Determines whether or not the DAG Node is in the model."""
    def inUnderWorld(self) -> bool:
        """Determines whether or not the DAG Node is an underworld node."""
    def instanceCount(self, total: bool) -> int:
        """Determines the number of times the Node attached to the Function Set is instanced."""
    def isChildOf(self, node: MObject) -> bool:
        """Determines whether or not the DAG Node attached to the Function Set is a child of the given node."""
    def isDefaultNode(self) -> bool:
        """Returns true if the node is a default node."""
    def isDrawLineOn(self) -> bool:
        """Returns whether or not a line is being drawn from the start to the end of the DistanceManip."""
    def isDrawStartOn(self) -> bool:
        """Returns whether or not the start of the DistanceManip is being drawn."""
    def isFlagSet(self, flag: int) -> bool:
        """Retrieves the current state of the specified flag for a node."""
    def isFromReferencedFile(self) -> bool:
        """Indicates whether or not this node came from a referenced file."""
    def isInstanceable(self) -> bool:
        """Returns true if the DAG node can be instanced, and false otherwise."""
    def isInstanced(self, indirect: bool = True) -> bool:
        """Determines whether the DAG Node attached to the Function Set is directly or indirectly instanced."""
    def isInstancedAttribute(self, attr: MObject) -> bool:
        """Returns true if the specified attribute is instanced."""
    def isIntermediateObject(self) -> bool:
        """Returns true if this object is an intermediate in a geometry calculation."""
    def isLimited(self, type: int) -> bool:
        """Determine if the specified limit attribute is enabled or disabled."""
    def isLocked(self) -> bool:
        """Indicates whether or not this node is locked."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Indicates whether or not the specified attribute was added to this node within the current scene."""
    def isOptimizePlaybackOn(self) -> bool:
        """Returns whether or not optimize playback is on."""
    def isParentOf(self, node: MObject) -> bool:
        """Determines whether or not the DAG Node attached to the Function Set is a parent of the given node."""
    def isShared(self) -> bool:
        """Indicates whether or not this node is shared."""
    def isTrackingEdits(self) -> bool:
        """Returns whether or not edits on the given node are being tracked by the generalized edit system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def isVisible(self) -> bool:
        """Returns whether or not the manipulator is visible."""
    def limitValue(self, type: int) -> float:
        """Determine the current value of the specified limit."""
    @staticmethod
    def lineSize() -> float:
        """Returns the manipulator line size."""
    def manipScale(self) -> float:
        """Returns the manipulator scale."""
    def model(self) -> MObject:
        """Deprecated in 2016.0"""
    def name(self) -> str:
        """Returns the name of this node."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def objectColor(self) -> int:
        """Deprecated in 2016.0"""
    def objectColorIndex(self) -> int:
        """Determines the index for the current user defined inactive color used by the node."""
    def objectColorRGB(self) -> MColor:
        """Determines the RGB color for the current user defined inactive color used by the node."""
    def objectColorType(self) -> Any:
        """Determines whether or not the user defined inactive color will be used for the node, or whether the default inactive col"""
    def objectGroupComponent(self, *args: Any, **kwargs: Any) -> Any: ...
    def parent(self, i: int) -> MObject:
        """Queries the DAG Node attached to the Function Set for the parent Node corresponding to the given index."""
    def parentCount(self) -> int:
        """Determines the number of parent Nodes of the Node."""
    def parentNamespace(self) -> str:
        """Returns the name of the namespace in which this node resides."""
    def partialPathName(self) -> str:
        """Return a string representing the partial path from the root of the dag to this object."""
    def pluginName(self) -> str:
        """Returns the name of the plug-in this MFnDependendencyNode was defined in."""
    def plugsAlias(self, plug: MPlug) -> str:
        """Returns the alias for the plug's attribute or the empty string if that attribute has no alias."""
    @overload
    def removeAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def removeAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Remove a dynamic attribute from a node."""
    def removeChild(self, child: MObject) -> MStatus:
        """Removes the given DAG Node from the parent."""
    def removeChildAt(self, index: int) -> MStatus:
        """Removes the child at the given index from the parent."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Some nodes, such as the various animCurve nodes, require that their attributes be set in a specific order for proper ope"""
    def resetFromRestPosition(self) -> MStatus:
        """Reset the transform to its rest position."""
    def resetTransformation(self, m: MMatrix) -> MStatus:
        """Reset this transform to equal the given matrix in world space."""
    def restPosition(self) -> MTransformationMatrix:
        """Retrieve the saved rest position of this transform."""
    @overload
    def rotateBy(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def rotateBy(self, rotation: MEulerRotation, Space: int | None = None) -> MStatus: ...
    @overload
    def rotateBy(self, order: int, Space: int | None = None) -> MStatus:
        """Relatively change the rotation of this transformation using a quaternion."""
    def rotateByQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Relatively change the rotation of this transformation using a quaternion."""
    def rotateOrientation(self, space: int) -> MQuaternion:
        """Returns the rotation used to orient the local rotation space."""
    def rotatePivot(self, space: int) -> MPoint:
        """Returns the pivot about which the rotation is applied."""
    def rotatePivotTranslation(self, space: int) -> MVector:
        """Return the rotate pivot translation in centimeters."""
    def rotateXYZValue(self, valIndex: int) -> MEulerRotation:
        """Gets the rotation for the active manipulator."""
    def rotationOrder(self) -> int:
        """Returns the rotation order for the transform matrix - the order in which the Euler angles are applied to create the end """
    def scaleBy(self) -> MStatus:
        """Relatively scale this transformation."""
    def scalePivot(self, space: int) -> MPoint:
        """Returns the pivot around which the scale is applied."""
    def scalePivotTranslation(self, space: int) -> MVector:
        """Returns the scale pivot translation in centimeters."""
    def scalingFactor(self) -> float:
        """Returns the scaling factor."""
    def set(self, transform: MTransformationMatrix) -> MStatus:
        """Change this transform to equal the given matrix."""
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setDirection(self, vector: MVector) -> MStatus:
        """Sets the direction of the DistanceManip."""
    def setDoNotWrite(self, flag: bool) -> MStatus:
        """Use this method to mark the "do not write" state of this node."""
    def setDrawLine(self, state: bool) -> MStatus:
        """Sets whether or not to draw a line from the start to the end of the DistanceManip."""
    @staticmethod
    def setDrawPlaneHandles(drawPlaneHandles: bool) -> None:
        """Sets the global option to display planar handles or not on supported manipulators."""
    def setDrawStart(self, state: bool) -> MStatus:
        """Sets whether or not to draw the start of the DistanceManip."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> MStatus:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> MStatus:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> MStatus:
        """Sets the state of the specified flag for the node."""
    @staticmethod
    def setGlobalSize(size: float) -> None:
        """Sets the global manipulator size."""
    @staticmethod
    def setHandleSize(size: float) -> None:
        """Sets the manipulator handle size."""
    def setIcon(self, filename: str) -> MStatus:
        """Associates a custom icon with the node for display in the Maya UI."""
    def setInstanceable(self, how: bool) -> MStatus:
        """Sets whether or not the DAG node is instanceable."""
    def setIntermediateObject(self, isIntermediate: bool) -> MStatus:
        """Sets whether this object is an intermediate in a geometry calculation."""
    def setLimit(self, type: int, value: float) -> MStatus:
        """Change the limit value for the specified limit type, and automatically enable the limit to be true."""
    @staticmethod
    def setLineSize(size: float) -> None:
        """Sets the manipulator line size."""
    def setLocked(self, locked: bool) -> MStatus:
        """Locks or unlocks this node."""
    def setManipScale(self, size: float) -> MStatus:
        """Sets the manipulator scale."""
    @overload
    def setName(self, name: str, createNamespace: bool = False) -> str: ...
    @overload
    def setName(self, name: str) -> str:
        """Sets the name of this node."""
    @overload
    def setObject(self, path: MDagPath) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches Function Set to the DAG Node that has the given DAG Path."""
    @overload
    def setObjectColor(self, color: int) -> MStatus: ...
    @overload
    def setObjectColor(self, color: MColor) -> MStatus:
        """Sets the index for the current user defined inactive color used by the node."""
    def setObjectColorType(self, type: Any) -> MStatus:
        """Sets whether or not the user defined inactive object color will be used."""
    def setOptimizePlayback(self, optimizePlayback: bool) -> MStatus:
        """Sets whether or not to optimize the playback."""
    def setRestPosition(self, matrix: MTransformationMatrix) -> MStatus:
        """Change the saved rest position of this transform."""
    def setRotateOrientation(self, quat: MQuaternion, space: int, balance: bool) -> MStatus:
        """Set the rotation used to orient the local rotation space."""
    def setRotatePivot(self, point: MPoint, space: int, balance: bool) -> MStatus:
        """Set the rotate pivot in centimeters about which rotation is applied."""
    def setRotatePivotTranslation(self, vec: MVector, space: int) -> MStatus:
        """Set the rotate pivot translation in centimeters."""
    @overload
    def setRotation(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def setRotation(self, rotation: MEulerRotation) -> MStatus: ...
    @overload
    def setRotation(self, order: int) -> MStatus: ...
    @overload
    def setRotation(self, RotationOrder: int, space: int) -> MStatus:
        """Change the rotation component of this transformation using a quaternion."""
    def setRotationOrder(self, order: int, reorder: bool) -> MStatus:
        """Change the rotation order for the transform - the order in which the Euler angles are applied to create the end rotation"""
    def setRotationQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Change the rotation component of this transformation using a quaternion."""
    def setScale(self) -> MStatus:
        """Set the scaling component of this transformation."""
    def setScalePivot(self, point: MPoint, space: int, balance: bool) -> MStatus:
        """Set the pivot around which the scale is applied in centimeters."""
    def setScalePivotTranslation(self, vec: MVector, space: int) -> MStatus:
        """Set the scale pivot translation in centimeters."""
    def setScalingFactor(self, scalingFactor: float) -> MStatus:
        """Sets the scaling factor."""
    def setShear(self) -> MStatus:
        """Set the shearing component of this transformation."""
    def setStartPoint(self, point: MPoint) -> MStatus:
        """Sets the start point of the DistanceManip."""
    def setTranslation(self, vec: MVector, space: int) -> MStatus:
        """Change the translation component of this transformation."""
    def setUseObjectColor(self, useObjectColor: bool) -> MStatus:
        """Deprecated in 2016.0"""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def setVisible(self, isVisible: bool) -> MStatus:
        """Sets whether or not the manipulator is visible."""
    def shearBy(self) -> MStatus:
        """Relatively shear this transformation."""
    def startPointIndex(self) -> int:
        """Returns the index of the start point of the DistanceManip."""
    def transformation(self) -> MTransformationMatrix:
        """Retrieve the transformation matrix represented by this transform."""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
    def translateBy(self, vec: MVector, space: int) -> MStatus:
        """Relatively change the translation component of this transformation."""
    def translation(self, Space: int) -> MVector:
        """Deprecated in 2018.0"""
    def type(self) -> int:
        """Function set type."""
    def typeId(self) -> MTypeId:
        """Returns the type id of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""
    @staticmethod
    def typeString(Type: int) -> str:
        """Introduced in 2020.0"""
    def uniqueName(self) -> str:
        """Introduced in 2023.0"""
    def userNode(self) -> Any:
        """If the function set's node is a plug-in node, then this method will extract the MPxNode pointer from it."""
    def usingHiliteColor(self) -> bool:
        """Determines whether or not the hilite color will be used for the node."""
    def usingObjectColor(self) -> bool:
        """Deprecated in 2016.0"""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnFreePointTriadManip:
    kExtensionAttr: Any
    kInvalidAttr: Any
    kLocalDynamicAttr: Any
    kNextPos: Any
    kNormalAttr: Any
    kRotateMaxX: Any
    kRotateMaxY: Any
    kRotateMaxZ: Any
    kRotateMinX: Any
    kRotateMinY: Any
    kRotateMinZ: Any
    kScaleMaxX: Any
    kScaleMaxY: Any
    kScaleMaxZ: Any
    kScaleMinX: Any
    kScaleMinY: Any
    kScaleMinZ: Any
    kShearMaxXY: Any
    kShearMaxXZ: Any
    kShearMaxYZ: Any
    kShearMinXY: Any
    kShearMinXZ: Any
    kShearMinYZ: Any
    kTimerInvalidState: Any
    kTimerMetric_callback: Any
    kTimerMetric_callbackNotViaAPI: Any
    kTimerMetric_callbackViaAPI: Any
    kTimerMetric_compute: Any
    kTimerMetric_computeDuringCallback: Any
    kTimerMetric_computeNotDuringCallback: Any
    kTimerMetric_dirty: Any
    kTimerMetric_draw: Any
    kTimerMetric_fetch: Any
    kTimerMetrics: Any
    kTimerOff: Any
    kTimerOn: Any
    kTimerType_count: Any
    kTimerType_inclusive: Any
    kTimerType_self: Any
    kTimerTypes: Any
    kTimerUninitialized: Any
    kTranslateMaxX: Any
    kTranslateMaxY: Any
    kTranslateMaxZ: Any
    kTranslateMinX: Any
    kTranslateMinY: Any
    kTranslateMinZ: Any
    kUseDefaultColor: Any
    kUseIndexColor: Any
    kUseRGBColor: Any
    kViewPlane: Any
    kXYPlane: Any
    kXZPlane: Any
    kYZPlane: Any
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None: ...
    @overload
    def __init__(self, object: MDagPath) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None:
        """Default constructor."""
    def absoluteName(self) -> str:
        """Returns the absolute name of this node."""
    def activeColor(self) -> MColor:
        """Determines the active color used by this node."""
    @overload
    def addAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def addAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Add a new dynamic attibute to this node."""
    def addChild(self, child: MObject, index: int, keepExistingParents: bool = False) -> MStatus:
        """Makes the given DAG Node a child of the DAG Node to which this instance of the Function Set is attached."""
    def addExternalContentForFileAttr(self, table: MExternalContentInfoTable, attr: MObject) -> MStatus:
        """Adds content info to the specified table from a file path attribute."""
    def affectsAnimation(self) -> bool:
        """Introduced in 2019.0"""
    @staticmethod
    def allocateFlag(pluginName: str) -> int:
        """Allocates a node flag for sole use by the caller."""
    @overload
    def attribute(self, index: int) -> MObject: ...
    @overload
    def attribute(self, attrName: str) -> MObject:
        """Finds the attribute of this node at the given index."""
    def attributeClass(self, attr: MObject) -> Any:
        """Returns the class (normal, dynamic, extension) of the specified attribute."""
    def attributeCount(self) -> int:
        """Returns the number of attributes that this node has."""
    @staticmethod
    def balanceTransformation(identity: int, identity_: int, one: int, kXYZ: int, arg: Any = True) -> None:
        """Balance a transformation when applying a world matrix to a joint."""
    def boundingBox(self) -> Any:
        """Returns the bounding box for the dag node in object space."""
    def canBeWritten(self) -> bool:
        """Returns the do not write state of the node."""
    def child(self, i: int) -> MObject:
        """Queries the DAG Node attached to the Function Set for the child Node corresponding to the given index."""
    def childCount(self) -> int:
        """Determines the number of child Nodes of the Node."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def classification(nodeTypeName: str) -> str:
        """Retrieves the classification string for a node type."""
    def clearRestPosition(self) -> MStatus:
        """Clear the saved rest position of this transform."""
    def connectToPointPlug(self, pointPlug: MPlug) -> MStatus:
        """Connect to the point plug."""
    @overload
    def create(self) -> MObject: ...
    @overload
    def create(self, manipName: str, pointName: str) -> MObject: ...
    @overload
    def create(self, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, type: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, type: str, name: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str) -> MObject: ...
    @overload
    def create(self, type: str) -> MObject: ...
    @overload
    def create(self, type: str, name: str) -> MObject:
        """Creates a new FreePointTriadManip."""
    def dagPath(self) -> MDagPath:
        """Returns the DagPath to which the Function Set is attached."""
    def dagRoot(self) -> MObject:
        """Determines the root of the first DAG Path to the DAG Node attached to the Function Set."""
    @staticmethod
    def deallocateAllFlags(pluginName: str) -> MStatus:
        """Deallocates all of the node flags which are currently allocated to the specified plugin."""
    @staticmethod
    def deallocateFlag(pluginName: str, flag: int) -> MStatus:
        """Deallocates a node flag which was previously allocated by a call to allocateFlag ."""
    @staticmethod
    def deleteManipulator(manip: MObject) -> MStatus:
        """Delete a manipulator."""
    def dgCallbackIds(self, type: Any, callbackName: str, callbackId: MCallbackIdArray, value: MDoubleArray) -> MStatus:
        """This method provides a further breakdown of the per-callback time returned via dgCallbacks() by returning the data on a """
    def dgCallbacks(self, type: Any, callbackName: Any, value: MDoubleArray) -> MStatus:
        """Node callbacks that occur when timing is enabled get logged with the node and can be queried via this method."""
    def dgTimer(self, timerMetric: Any, timerType: Any) -> float:
        """The function returns the specified timer value for the current node."""
    def dgTimerOff(self) -> MStatus:
        """Indicates that this node should no longer collect DG timing data when DG timing is enabled."""
    def dgTimerOn(self) -> MStatus:
        """Indicates that this node should collect DG timing data whenever DG timing is enabled."""
    def dgTimerQueryState(self) -> Any:
        """The function returns the current on/off state of the node's timer."""
    def dgTimerReset(self) -> MStatus:
        """The function resets the dependency graph timers and counters for this node to zero."""
    def dormantColor(self) -> MColor:
        """Determines the dormant color used by this node."""
    def drawOverrideColor(self, color: MColor) -> bool:
        """Determines the draw override color used by this node."""
    def drawOverrideEnabled(self) -> bool:
        """Determines whether or not draw override is turned on for this node."""
    def drawOverrideIsReference(self) -> bool:
        """Determines whether or not Display Type of the draw override is Reference for this node."""
    def drawOverrideIsTemplate(self) -> bool:
        """Determines whether or not Display Type of the draw override is Template for this node."""
    @staticmethod
    def drawPlaneHandles() -> bool:
        """This method returns the global option that says if the planar manipulator handles should be drawn or not."""
    def duplicate(self, instance: bool = False, instanceLeaf: bool = False) -> MObject:
        """This method duplicates the DAG hierarchy rooted at the current node."""
    @staticmethod
    def enableDGTiming(enable: bool) -> None:
        """Globally enables or disables the DG node timing mechanism."""
    def enableLimit(self, type: int, flag: bool) -> MStatus:
        """Enable or disable the limit value for the specified limit type."""
    def findAlias(self, alias: str, attrObj: MObject) -> bool:
        """Retrieves the attribute with the given alias."""
    @overload
    def findPlug(self, attr: MObject, wantNetworkedPlug: bool) -> MPlug: ...
    @overload
    def findPlug(self, attrName: str, wantNetworkedPlug: bool) -> MPlug: ...
    @overload
    def findPlug(self, attr: MObject) -> MPlug: ...
    @overload
    def findPlug(self, attrName: str) -> MPlug:
        """Attempt to find a plug for the given attribute."""
    def fullPathName(self) -> str:
        """Return a string representing the full path from the root of the dag to this object."""
    def getAffectedAttributes(self, attr: MObject, affectedAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that are affected by the attribute passed in."""
    def getAffectedByAttributes(self, attr: MObject, affectedByAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that affect the attribute passed in, attr ."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute al"""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns a list of all attribute aliases for this node."""
    def getAllPaths(self, paths: MDagPathArray) -> MStatus:
        """Determines all DAG Paths to the DAG Node attached to the Function Set."""
    def getConnectedSetsAndMembers(self, instanceNumber: int, sets: MObjectArray, comps: MObjectArray, renderableSetsOnly: bool) -> MStatus:
        """Returns all the sets connected to the specified instance of this DAG object."""
    def getConnections(self, array: MPlugArray) -> MStatus:
        """Get all of the current connections to this node as an array of plugs."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> MStatus:
        """Returns the external content (files) that this node depends on."""
    def getPath(self, path: MDagPath) -> MStatus:
        """Returns a DAG Path to the DAG Node attached to the Function Set."""
    @overload
    def getRotation(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def getRotation(self, rotation: MEulerRotation) -> MStatus: ...
    @overload
    def getRotation(self, order: int) -> MStatus: ...
    @overload
    def getRotation(self, order: int, space: int) -> MStatus:
        """Retrieve the rotation component of this transformation as a quaternion."""
    def getRotationQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Retrieve the rotation component of this transformation as a quaternion."""
    def getScale(self) -> MStatus:
        """Retrieve the scaling component of this transformation."""
    def getShear(self) -> MStatus:
        """Retrieve the shearing component of this transformation."""
    def getTranslation(self, space: int) -> MVector:
        """Retrieve the translation component of this transformation in centimeters."""
    @staticmethod
    def globalSize() -> float:
        """Returns the global manipulator size."""
    @staticmethod
    def handleSize() -> float:
        """Returns the manipulator handle size."""
    def hasAttribute(self, name: str) -> bool:
        """Returns true if the node already has an attribute with the given name."""
    def hasChild(self, node: MObject) -> bool:
        """Determines whether or not the given Node is a child of the DAG Node attached to the Function Set."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    def hasParent(self, node: MObject) -> bool:
        """Determines whether or not the given Node is a parent of the DAG Node attached to the Function Set."""
    def hasUniqueName(self) -> bool:
        """Indicates whether or not this node's name is unique within the scene."""
    def hiliteColor(self) -> MColor:
        """Determines the current hilite color used by the node."""
    def icon(self) -> str:
        """Returns the custom icon filename associated with the node."""
    def inModel(self) -> bool:
        """Determines whether or not the DAG Node is in the model."""
    def inUnderWorld(self) -> bool:
        """Determines whether or not the DAG Node is an underworld node."""
    def instanceCount(self, total: bool) -> int:
        """Determines the number of times the Node attached to the Function Set is instanced."""
    def isChildOf(self, node: MObject) -> bool:
        """Determines whether or not the DAG Node attached to the Function Set is a child of the given node."""
    def isDefaultNode(self) -> bool:
        """Returns true if the node is a default node."""
    def isDrawAxesOn(self) -> bool:
        """Returns whether or not the axes of the FreePointTriadManip are being drawn."""
    def isFlagSet(self, flag: int) -> bool:
        """Retrieves the current state of the specified flag for a node."""
    def isFromReferencedFile(self) -> bool:
        """Indicates whether or not this node came from a referenced file."""
    def isInstanceable(self) -> bool:
        """Returns true if the DAG node can be instanced, and false otherwise."""
    def isInstanced(self, indirect: bool = True) -> bool:
        """Determines whether the DAG Node attached to the Function Set is directly or indirectly instanced."""
    def isInstancedAttribute(self, attr: MObject) -> bool:
        """Returns true if the specified attribute is instanced."""
    def isIntermediateObject(self) -> bool:
        """Returns true if this object is an intermediate in a geometry calculation."""
    def isKeyframeAllOn(self) -> bool:
        """Returns whether or not the FreePointTriadManip is in keyframeAll mode."""
    def isLimited(self, type: int) -> bool:
        """Determine if the specified limit attribute is enabled or disabled."""
    def isLocked(self) -> bool:
        """Indicates whether or not this node is locked."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Indicates whether or not the specified attribute was added to this node within the current scene."""
    def isOptimizePlaybackOn(self) -> bool:
        """Returns whether or not optimize playback is on."""
    def isParentOf(self, node: MObject) -> bool:
        """Determines whether or not the DAG Node attached to the Function Set is a parent of the given node."""
    def isShared(self) -> bool:
        """Indicates whether or not this node is shared."""
    def isSnapModeOn(self) -> bool:
        """Returns whether or not the FreePointTriadManip is in snap mode."""
    def isTrackingEdits(self) -> bool:
        """Returns whether or not edits on the given node are being tracked by the generalized edit system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def isVisible(self) -> bool:
        """Returns whether or not the manipulator is visible."""
    def limitValue(self, type: int) -> float:
        """Determine the current value of the specified limit."""
    @staticmethod
    def lineSize() -> float:
        """Returns the manipulator line size."""
    def manipScale(self) -> float:
        """Returns the manipulator scale."""
    def model(self) -> MObject:
        """Deprecated in 2016.0"""
    def name(self) -> str:
        """Returns the name of this node."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def objectColor(self) -> int:
        """Deprecated in 2016.0"""
    def objectColorIndex(self) -> int:
        """Determines the index for the current user defined inactive color used by the node."""
    def objectColorRGB(self) -> MColor:
        """Determines the RGB color for the current user defined inactive color used by the node."""
    def objectColorType(self) -> Any:
        """Determines whether or not the user defined inactive color will be used for the node, or whether the default inactive col"""
    def objectGroupComponent(self, *args: Any, **kwargs: Any) -> Any: ...
    def parent(self, i: int) -> MObject:
        """Queries the DAG Node attached to the Function Set for the parent Node corresponding to the given index."""
    def parentCount(self) -> int:
        """Determines the number of parent Nodes of the Node."""
    def parentNamespace(self) -> str:
        """Returns the name of the namespace in which this node resides."""
    def partialPathName(self) -> str:
        """Return a string representing the partial path from the root of the dag to this object."""
    def pluginName(self) -> str:
        """Returns the name of the plug-in this MFnDependendencyNode was defined in."""
    def plugsAlias(self, plug: MPlug) -> str:
        """Returns the alias for the plug's attribute or the empty string if that attribute has no alias."""
    def pointIndex(self) -> int:
        """Returns the index of the point of the FreePointTriadManip."""
    @overload
    def removeAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def removeAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Remove a dynamic attribute from a node."""
    def removeChild(self, child: MObject) -> MStatus:
        """Removes the given DAG Node from the parent."""
    def removeChildAt(self, index: int) -> MStatus:
        """Removes the child at the given index from the parent."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Some nodes, such as the various animCurve nodes, require that their attributes be set in a specific order for proper ope"""
    def resetFromRestPosition(self) -> MStatus:
        """Reset the transform to its rest position."""
    def resetTransformation(self, m: MMatrix) -> MStatus:
        """Reset this transform to equal the given matrix in world space."""
    def restPosition(self) -> MTransformationMatrix:
        """Retrieve the saved rest position of this transform."""
    @overload
    def rotateBy(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def rotateBy(self, rotation: MEulerRotation, Space: int | None = None) -> MStatus: ...
    @overload
    def rotateBy(self, order: int, Space: int | None = None) -> MStatus:
        """Relatively change the rotation of this transformation using a quaternion."""
    def rotateByQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Relatively change the rotation of this transformation using a quaternion."""
    def rotateOrientation(self, space: int) -> MQuaternion:
        """Returns the rotation used to orient the local rotation space."""
    def rotatePivot(self, space: int) -> MPoint:
        """Returns the pivot about which the rotation is applied."""
    def rotatePivotTranslation(self, space: int) -> MVector:
        """Return the rotate pivot translation in centimeters."""
    def rotateXYZValue(self, valIndex: int) -> MEulerRotation:
        """Gets the rotation for the active manipulator."""
    def rotationOrder(self) -> int:
        """Returns the rotation order for the transform matrix - the order in which the Euler angles are applied to create the end """
    def scaleBy(self) -> MStatus:
        """Relatively scale this transformation."""
    def scalePivot(self, space: int) -> MPoint:
        """Returns the pivot around which the scale is applied."""
    def scalePivotTranslation(self, space: int) -> MVector:
        """Returns the scale pivot translation in centimeters."""
    def set(self, transform: MTransformationMatrix) -> MStatus:
        """Change this transform to equal the given matrix."""
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setDirection(self, direction: MVector) -> MStatus:
        """Sets the orientation of the FreePointTriadManip."""
    def setDoNotWrite(self, flag: bool) -> MStatus:
        """Use this method to mark the "do not write" state of this node."""
    def setDrawArrowHead(self, state: bool) -> MStatus:
        """Sets whether or not drawArrowHead is on."""
    def setDrawAxes(self, state: bool) -> MStatus:
        """Sets whether or not to draw the axes of the FreePointTriadManip."""
    @staticmethod
    def setDrawPlaneHandles(drawPlaneHandles: bool) -> None:
        """Sets the global option to display planar handles or not on supported manipulators."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> MStatus:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> MStatus:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> MStatus:
        """Sets the state of the specified flag for the node."""
    @staticmethod
    def setGlobalSize(size: float) -> None:
        """Sets the global manipulator size."""
    def setGlobalTriadPlane(self, whichPlane: Any) -> MStatus:
        """Sets which plane to use as the global triad plane."""
    @staticmethod
    def setHandleSize(size: float) -> None:
        """Sets the manipulator handle size."""
    def setIcon(self, filename: str) -> MStatus:
        """Associates a custom icon with the node for display in the Maya UI."""
    def setInstanceable(self, how: bool) -> MStatus:
        """Sets whether or not the DAG node is instanceable."""
    def setIntermediateObject(self, isIntermediate: bool) -> MStatus:
        """Sets whether this object is an intermediate in a geometry calculation."""
    def setKeyframeAll(self, state: bool) -> MStatus:
        """Sets whether or not keyframeAll is on."""
    def setLimit(self, type: int, value: float) -> MStatus:
        """Change the limit value for the specified limit type, and automatically enable the limit to be true."""
    @staticmethod
    def setLineSize(size: float) -> None:
        """Sets the manipulator line size."""
    def setLocked(self, locked: bool) -> MStatus:
        """Locks or unlocks this node."""
    def setManipScale(self, size: float) -> MStatus:
        """Sets the manipulator scale."""
    @overload
    def setName(self, name: str, createNamespace: bool = False) -> str: ...
    @overload
    def setName(self, name: str) -> str:
        """Sets the name of this node."""
    @overload
    def setObject(self, path: MDagPath) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches Function Set to the DAG Node that has the given DAG Path."""
    @overload
    def setObjectColor(self, color: int) -> MStatus: ...
    @overload
    def setObjectColor(self, color: MColor) -> MStatus:
        """Sets the index for the current user defined inactive color used by the node."""
    def setObjectColorType(self, type: Any) -> MStatus:
        """Sets whether or not the user defined inactive object color will be used."""
    def setOptimizePlayback(self, optimizePlayback: bool) -> MStatus:
        """Sets whether or not to optimize the playback."""
    def setPoint(self, pointValue: MPoint) -> MStatus:
        """Set the point manipulator value to the given vector."""
    def setRestPosition(self, matrix: MTransformationMatrix) -> MStatus:
        """Change the saved rest position of this transform."""
    def setRotateOrientation(self, quat: MQuaternion, space: int, balance: bool) -> MStatus:
        """Set the rotation used to orient the local rotation space."""
    def setRotatePivot(self, point: MPoint, space: int, balance: bool) -> MStatus:
        """Set the rotate pivot in centimeters about which rotation is applied."""
    def setRotatePivotTranslation(self, vec: MVector, space: int) -> MStatus:
        """Set the rotate pivot translation in centimeters."""
    @overload
    def setRotation(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def setRotation(self, rotation: MEulerRotation) -> MStatus: ...
    @overload
    def setRotation(self, order: int) -> MStatus: ...
    @overload
    def setRotation(self, RotationOrder: int, space: int) -> MStatus:
        """Change the rotation component of this transformation using a quaternion."""
    def setRotationOrder(self, order: int, reorder: bool) -> MStatus:
        """Change the rotation order for the transform - the order in which the Euler angles are applied to create the end rotation"""
    def setRotationQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Change the rotation component of this transformation using a quaternion."""
    def setScale(self) -> MStatus:
        """Set the scaling component of this transformation."""
    def setScalePivot(self, point: MPoint, space: int, balance: bool) -> MStatus:
        """Set the pivot around which the scale is applied in centimeters."""
    def setScalePivotTranslation(self, vec: MVector, space: int) -> MStatus:
        """Set the scale pivot translation in centimeters."""
    def setShear(self) -> MStatus:
        """Set the shearing component of this transformation."""
    def setSnapMode(self, state: bool) -> MStatus:
        """Sets whether or not to the FreePointTriadManip should be in snap mode."""
    def setTranslation(self, vec: MVector, space: int) -> MStatus:
        """Change the translation component of this transformation."""
    def setUseObjectColor(self, useObjectColor: bool) -> MStatus:
        """Deprecated in 2016.0"""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def setVisible(self, isVisible: bool) -> MStatus:
        """Sets whether or not the manipulator is visible."""
    def shearBy(self) -> MStatus:
        """Relatively shear this transformation."""
    def transformation(self) -> MTransformationMatrix:
        """Retrieve the transformation matrix represented by this transform."""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
    def translateBy(self, vec: MVector, space: int) -> MStatus:
        """Relatively change the translation component of this transformation."""
    def translation(self, Space: int) -> MVector:
        """Deprecated in 2018.0"""
    def type(self) -> int:
        """Function set type."""
    def typeId(self) -> MTypeId:
        """Returns the type id of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""
    @staticmethod
    def typeString(Type: int) -> str:
        """Introduced in 2020.0"""
    def uniqueName(self) -> str:
        """Introduced in 2023.0"""
    def userNode(self) -> Any:
        """If the function set's node is a plug-in node, then this method will extract the MPxNode pointer from it."""
    def usingHiliteColor(self) -> bool:
        """Determines whether or not the hilite color will be used for the node."""
    def usingObjectColor(self) -> bool:
        """Deprecated in 2016.0"""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnManip3D:
    kExtensionAttr: Any
    kInvalidAttr: Any
    kLocalDynamicAttr: Any
    kNextPos: Any
    kNormalAttr: Any
    kRotateMaxX: Any
    kRotateMaxY: Any
    kRotateMaxZ: Any
    kRotateMinX: Any
    kRotateMinY: Any
    kRotateMinZ: Any
    kScaleMaxX: Any
    kScaleMaxY: Any
    kScaleMaxZ: Any
    kScaleMinX: Any
    kScaleMinY: Any
    kScaleMinZ: Any
    kShearMaxXY: Any
    kShearMaxXZ: Any
    kShearMaxYZ: Any
    kShearMinXY: Any
    kShearMinXZ: Any
    kShearMinYZ: Any
    kTimerInvalidState: Any
    kTimerMetric_callback: Any
    kTimerMetric_callbackNotViaAPI: Any
    kTimerMetric_callbackViaAPI: Any
    kTimerMetric_compute: Any
    kTimerMetric_computeDuringCallback: Any
    kTimerMetric_computeNotDuringCallback: Any
    kTimerMetric_dirty: Any
    kTimerMetric_draw: Any
    kTimerMetric_fetch: Any
    kTimerMetrics: Any
    kTimerOff: Any
    kTimerOn: Any
    kTimerType_count: Any
    kTimerType_inclusive: Any
    kTimerType_self: Any
    kTimerTypes: Any
    kTimerUninitialized: Any
    kTranslateMaxX: Any
    kTranslateMaxY: Any
    kTranslateMaxZ: Any
    kTranslateMinX: Any
    kTranslateMinY: Any
    kTranslateMinZ: Any
    kUseDefaultColor: Any
    kUseIndexColor: Any
    kUseRGBColor: Any
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def absoluteName(self, *args: Any, **kwargs: Any) -> Any: ...
    def activeColor(self, *args: Any, **kwargs: Any) -> Any: ...
    def addAttribute(self, *args: Any, **kwargs: Any) -> Any: ...
    def addChild(self, *args: Any, **kwargs: Any) -> Any: ...
    def addExternalContentForFileAttr(self, *args: Any, **kwargs: Any) -> Any: ...
    def affectsAnimation(self, *args: Any, **kwargs: Any) -> Any: ...
    def allocateFlag(self, *args: Any, **kwargs: Any) -> Any: ...
    def attribute(self, *args: Any, **kwargs: Any) -> Any: ...
    def attributeClass(self, *args: Any, **kwargs: Any) -> Any: ...
    def attributeCount(self, *args: Any, **kwargs: Any) -> Any: ...
    def balanceTransformation(self, *args: Any, **kwargs: Any) -> Any: ...
    def boundingBox(self, *args: Any, **kwargs: Any) -> Any: ...
    def canBeWritten(self, *args: Any, **kwargs: Any) -> Any: ...
    def child(self, *args: Any, **kwargs: Any) -> Any: ...
    def childCount(self, *args: Any, **kwargs: Any) -> Any: ...
    def className(self, *args: Any, **kwargs: Any) -> Any: ...
    def classification(self, *args: Any, **kwargs: Any) -> Any: ...
    def clearRestPosition(self, *args: Any, **kwargs: Any) -> Any: ...
    def create(self, *args: Any, **kwargs: Any) -> Any: ...
    def dagPath(self, *args: Any, **kwargs: Any) -> Any: ...
    def dagRoot(self, *args: Any, **kwargs: Any) -> Any: ...
    def deallocateAllFlags(self, *args: Any, **kwargs: Any) -> Any: ...
    def deallocateFlag(self, *args: Any, **kwargs: Any) -> Any: ...
    def deleteManipulator(self, *args: Any, **kwargs: Any) -> Any: ...
    def dgCallbackIds(self, *args: Any, **kwargs: Any) -> Any: ...
    def dgCallbacks(self, *args: Any, **kwargs: Any) -> Any: ...
    def dgTimer(self, *args: Any, **kwargs: Any) -> Any: ...
    def dgTimerOff(self, *args: Any, **kwargs: Any) -> Any: ...
    def dgTimerOn(self, *args: Any, **kwargs: Any) -> Any: ...
    def dgTimerQueryState(self, *args: Any, **kwargs: Any) -> Any: ...
    def dgTimerReset(self, *args: Any, **kwargs: Any) -> Any: ...
    def dormantColor(self, *args: Any, **kwargs: Any) -> Any: ...
    def drawOverrideColor(self, *args: Any, **kwargs: Any) -> Any: ...
    def drawOverrideEnabled(self, *args: Any, **kwargs: Any) -> Any: ...
    def drawOverrideIsReference(self, *args: Any, **kwargs: Any) -> Any: ...
    def drawOverrideIsTemplate(self, *args: Any, **kwargs: Any) -> Any: ...
    def drawPlaneHandles(self, *args: Any, **kwargs: Any) -> Any: ...
    def duplicate(self, *args: Any, **kwargs: Any) -> Any: ...
    def enableDGTiming(self, *args: Any, **kwargs: Any) -> Any: ...
    def enableLimit(self, *args: Any, **kwargs: Any) -> Any: ...
    def findAlias(self, *args: Any, **kwargs: Any) -> Any: ...
    def findPlug(self, *args: Any, **kwargs: Any) -> Any: ...
    def fullPathName(self, *args: Any, **kwargs: Any) -> Any: ...
    def getAffectedAttributes(self, *args: Any, **kwargs: Any) -> Any: ...
    def getAffectedByAttributes(self, *args: Any, **kwargs: Any) -> Any: ...
    def getAliasAttr(self, *args: Any, **kwargs: Any) -> Any: ...
    def getAliasList(self, *args: Any, **kwargs: Any) -> Any: ...
    def getAllPaths(self, *args: Any, **kwargs: Any) -> Any: ...
    def getConnectedSetsAndMembers(self, *args: Any, **kwargs: Any) -> Any: ...
    def getConnections(self, *args: Any, **kwargs: Any) -> Any: ...
    def getExternalContent(self, *args: Any, **kwargs: Any) -> Any: ...
    def getPath(self, *args: Any, **kwargs: Any) -> Any: ...
    def getRotation(self, *args: Any, **kwargs: Any) -> Any: ...
    def getRotationQuaternion(self, *args: Any, **kwargs: Any) -> Any: ...
    def getScale(self, *args: Any, **kwargs: Any) -> Any: ...
    def getShear(self, *args: Any, **kwargs: Any) -> Any: ...
    def getTranslation(self, *args: Any, **kwargs: Any) -> Any: ...
    def globalSize(self, *args: Any, **kwargs: Any) -> Any: ...
    def handleSize(self, *args: Any, **kwargs: Any) -> Any: ...
    def hasAttribute(self, *args: Any, **kwargs: Any) -> Any: ...
    def hasChild(self, *args: Any, **kwargs: Any) -> Any: ...
    def hasObj(self, *args: Any, **kwargs: Any) -> Any: ...
    def hasParent(self, *args: Any, **kwargs: Any) -> Any: ...
    def hasUniqueName(self, *args: Any, **kwargs: Any) -> Any: ...
    def hiliteColor(self, *args: Any, **kwargs: Any) -> Any: ...
    def icon(self, *args: Any, **kwargs: Any) -> Any: ...
    def inModel(self, *args: Any, **kwargs: Any) -> Any: ...
    def inUnderWorld(self, *args: Any, **kwargs: Any) -> Any: ...
    def instanceCount(self, *args: Any, **kwargs: Any) -> Any: ...
    def isChildOf(self, *args: Any, **kwargs: Any) -> Any: ...
    def isDefaultNode(self, *args: Any, **kwargs: Any) -> Any: ...
    def isFlagSet(self, *args: Any, **kwargs: Any) -> Any: ...
    def isFromReferencedFile(self, *args: Any, **kwargs: Any) -> Any: ...
    def isInstanceable(self, *args: Any, **kwargs: Any) -> Any: ...
    def isInstanced(self, *args: Any, **kwargs: Any) -> Any: ...
    def isInstancedAttribute(self, *args: Any, **kwargs: Any) -> Any: ...
    def isIntermediateObject(self, *args: Any, **kwargs: Any) -> Any: ...
    def isLimited(self, *args: Any, **kwargs: Any) -> Any: ...
    def isLocked(self, *args: Any, **kwargs: Any) -> Any: ...
    def isNewAttribute(self, *args: Any, **kwargs: Any) -> Any: ...
    def isOptimizePlaybackOn(self, *args: Any, **kwargs: Any) -> Any: ...
    def isParentOf(self, *args: Any, **kwargs: Any) -> Any: ...
    def isShared(self, *args: Any, **kwargs: Any) -> Any: ...
    def isTrackingEdits(self, *args: Any, **kwargs: Any) -> Any: ...
    def isValid(self, *args: Any, **kwargs: Any) -> Any: ...
    def isVisible(self, *args: Any, **kwargs: Any) -> Any: ...
    def limitValue(self, *args: Any, **kwargs: Any) -> Any: ...
    def lineSize(self, *args: Any, **kwargs: Any) -> Any: ...
    def manipScale(self, *args: Any, **kwargs: Any) -> Any: ...
    def model(self, *args: Any, **kwargs: Any) -> Any: ...
    def name(self, *args: Any, **kwargs: Any) -> Any: ...
    def object(self, *args: Any, **kwargs: Any) -> Any: ...
    def objectColor(self, *args: Any, **kwargs: Any) -> Any: ...
    def objectColorIndex(self, *args: Any, **kwargs: Any) -> Any: ...
    def objectColorRGB(self, *args: Any, **kwargs: Any) -> Any: ...
    def objectColorType(self, *args: Any, **kwargs: Any) -> Any: ...
    def objectGroupComponent(self, *args: Any, **kwargs: Any) -> Any: ...
    def parent(self, *args: Any, **kwargs: Any) -> Any: ...
    def parentCount(self, *args: Any, **kwargs: Any) -> Any: ...
    def parentNamespace(self, *args: Any, **kwargs: Any) -> Any: ...
    def partialPathName(self, *args: Any, **kwargs: Any) -> Any: ...
    def pluginName(self, *args: Any, **kwargs: Any) -> Any: ...
    def plugsAlias(self, *args: Any, **kwargs: Any) -> Any: ...
    def removeAttribute(self, *args: Any, **kwargs: Any) -> Any: ...
    def removeChild(self, *args: Any, **kwargs: Any) -> Any: ...
    def removeChildAt(self, *args: Any, **kwargs: Any) -> Any: ...
    def reorderedAttribute(self, *args: Any, **kwargs: Any) -> Any: ...
    def resetFromRestPosition(self, *args: Any, **kwargs: Any) -> Any: ...
    def resetTransformation(self, *args: Any, **kwargs: Any) -> Any: ...
    def restPosition(self, *args: Any, **kwargs: Any) -> Any: ...
    def rotateBy(self, *args: Any, **kwargs: Any) -> Any: ...
    def rotateByQuaternion(self, *args: Any, **kwargs: Any) -> Any: ...
    def rotateOrientation(self, *args: Any, **kwargs: Any) -> Any: ...
    def rotatePivot(self, *args: Any, **kwargs: Any) -> Any: ...
    def rotatePivotTranslation(self, *args: Any, **kwargs: Any) -> Any: ...
    def rotateXYZValue(self, *args: Any, **kwargs: Any) -> Any: ...
    def rotationOrder(self, *args: Any, **kwargs: Any) -> Any: ...
    def scaleBy(self, *args: Any, **kwargs: Any) -> Any: ...
    def scalePivot(self, *args: Any, **kwargs: Any) -> Any: ...
    def scalePivotTranslation(self, *args: Any, **kwargs: Any) -> Any: ...
    def set(self, *args: Any, **kwargs: Any) -> Any: ...
    def setAffectsAnimation(self, *args: Any, **kwargs: Any) -> Any: ...
    def setAlias(self, *args: Any, **kwargs: Any) -> Any: ...
    def setDoNotWrite(self, *args: Any, **kwargs: Any) -> Any: ...
    def setDrawPlaneHandles(self, *args: Any, **kwargs: Any) -> Any: ...
    def setExternalContent(self, *args: Any, **kwargs: Any) -> Any: ...
    def setExternalContentForFileAttr(self, *args: Any, **kwargs: Any) -> Any: ...
    def setFlag(self, *args: Any, **kwargs: Any) -> Any: ...
    def setGlobalSize(self, *args: Any, **kwargs: Any) -> Any: ...
    def setHandleSize(self, *args: Any, **kwargs: Any) -> Any: ...
    def setIcon(self, *args: Any, **kwargs: Any) -> Any: ...
    def setInstanceable(self, *args: Any, **kwargs: Any) -> Any: ...
    def setIntermediateObject(self, *args: Any, **kwargs: Any) -> Any: ...
    def setLimit(self, *args: Any, **kwargs: Any) -> Any: ...
    def setLineSize(self, *args: Any, **kwargs: Any) -> Any: ...
    def setLocked(self, *args: Any, **kwargs: Any) -> Any: ...
    def setManipScale(self, *args: Any, **kwargs: Any) -> Any: ...
    def setName(self, *args: Any, **kwargs: Any) -> Any: ...
    def setObject(self, *args: Any, **kwargs: Any) -> Any: ...
    def setObjectColor(self, *args: Any, **kwargs: Any) -> Any: ...
    def setObjectColorType(self, *args: Any, **kwargs: Any) -> Any: ...
    def setOptimizePlayback(self, *args: Any, **kwargs: Any) -> Any: ...
    def setRestPosition(self, *args: Any, **kwargs: Any) -> Any: ...
    def setRotateOrientation(self, *args: Any, **kwargs: Any) -> Any: ...
    def setRotatePivot(self, *args: Any, **kwargs: Any) -> Any: ...
    def setRotatePivotTranslation(self, *args: Any, **kwargs: Any) -> Any: ...
    def setRotation(self, *args: Any, **kwargs: Any) -> Any: ...
    def setRotationOrder(self, *args: Any, **kwargs: Any) -> Any: ...
    def setRotationQuaternion(self, *args: Any, **kwargs: Any) -> Any: ...
    def setScale(self, *args: Any, **kwargs: Any) -> Any: ...
    def setScalePivot(self, *args: Any, **kwargs: Any) -> Any: ...
    def setScalePivotTranslation(self, *args: Any, **kwargs: Any) -> Any: ...
    def setShear(self, *args: Any, **kwargs: Any) -> Any: ...
    def setTranslation(self, *args: Any, **kwargs: Any) -> Any: ...
    def setUseObjectColor(self, *args: Any, **kwargs: Any) -> Any: ...
    def setUuid(self, *args: Any, **kwargs: Any) -> Any: ...
    def setVisible(self, *args: Any, **kwargs: Any) -> Any: ...
    def shearBy(self, *args: Any, **kwargs: Any) -> Any: ...
    def transformation(self, *args: Any, **kwargs: Any) -> Any: ...
    def transformationMatrix(self, *args: Any, **kwargs: Any) -> Any: ...
    def translateBy(self, *args: Any, **kwargs: Any) -> Any: ...
    def translation(self, *args: Any, **kwargs: Any) -> Any: ...
    def type(self, *args: Any, **kwargs: Any) -> Any: ...
    def typeId(self, *args: Any, **kwargs: Any) -> Any: ...
    def typeName(self, *args: Any, **kwargs: Any) -> Any: ...
    def typeString(self, *args: Any, **kwargs: Any) -> Any: ...
    def uniqueName(self, *args: Any, **kwargs: Any) -> Any: ...
    def userNode(self, *args: Any, **kwargs: Any) -> Any: ...
    def usingHiliteColor(self, *args: Any, **kwargs: Any) -> Any: ...
    def usingObjectColor(self, *args: Any, **kwargs: Any) -> Any: ...
    def uuid(self, *args: Any, **kwargs: Any) -> Any: ...

class MFnPointOnCurveManip:
    kExtensionAttr: Any
    kInvalidAttr: Any
    kLocalDynamicAttr: Any
    kNextPos: Any
    kNormalAttr: Any
    kRotateMaxX: Any
    kRotateMaxY: Any
    kRotateMaxZ: Any
    kRotateMinX: Any
    kRotateMinY: Any
    kRotateMinZ: Any
    kScaleMaxX: Any
    kScaleMaxY: Any
    kScaleMaxZ: Any
    kScaleMinX: Any
    kScaleMinY: Any
    kScaleMinZ: Any
    kShearMaxXY: Any
    kShearMaxXZ: Any
    kShearMaxYZ: Any
    kShearMinXY: Any
    kShearMinXZ: Any
    kShearMinYZ: Any
    kTimerInvalidState: Any
    kTimerMetric_callback: Any
    kTimerMetric_callbackNotViaAPI: Any
    kTimerMetric_callbackViaAPI: Any
    kTimerMetric_compute: Any
    kTimerMetric_computeDuringCallback: Any
    kTimerMetric_computeNotDuringCallback: Any
    kTimerMetric_dirty: Any
    kTimerMetric_draw: Any
    kTimerMetric_fetch: Any
    kTimerMetrics: Any
    kTimerOff: Any
    kTimerOn: Any
    kTimerType_count: Any
    kTimerType_inclusive: Any
    kTimerType_self: Any
    kTimerTypes: Any
    kTimerUninitialized: Any
    kTranslateMaxX: Any
    kTranslateMaxY: Any
    kTranslateMaxZ: Any
    kTranslateMinX: Any
    kTranslateMinY: Any
    kTranslateMinZ: Any
    kUseDefaultColor: Any
    kUseIndexColor: Any
    kUseRGBColor: Any
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None: ...
    @overload
    def __init__(self, object: MDagPath) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None:
        """Default constructor."""
    def absoluteName(self) -> str:
        """Returns the absolute name of this node."""
    def activeColor(self) -> MColor:
        """Determines the active color used by this node."""
    @overload
    def addAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def addAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Add a new dynamic attibute to this node."""
    def addChild(self, child: MObject, index: int, keepExistingParents: bool = False) -> MStatus:
        """Makes the given DAG Node a child of the DAG Node to which this instance of the Function Set is attached."""
    def addExternalContentForFileAttr(self, table: MExternalContentInfoTable, attr: MObject) -> MStatus:
        """Adds content info to the specified table from a file path attribute."""
    def affectsAnimation(self) -> bool:
        """Introduced in 2019.0"""
    @staticmethod
    def allocateFlag(pluginName: str) -> int:
        """Allocates a node flag for sole use by the caller."""
    @overload
    def attribute(self, index: int) -> MObject: ...
    @overload
    def attribute(self, attrName: str) -> MObject:
        """Finds the attribute of this node at the given index."""
    def attributeClass(self, attr: MObject) -> Any:
        """Returns the class (normal, dynamic, extension) of the specified attribute."""
    def attributeCount(self) -> int:
        """Returns the number of attributes that this node has."""
    @staticmethod
    def balanceTransformation(identity: int, identity_: int, one: int, kXYZ: int, arg: Any = True) -> None:
        """Balance a transformation when applying a world matrix to a joint."""
    def boundingBox(self) -> Any:
        """Returns the bounding box for the dag node in object space."""
    def canBeWritten(self) -> bool:
        """Returns the do not write state of the node."""
    def child(self, i: int) -> MObject:
        """Queries the DAG Node attached to the Function Set for the child Node corresponding to the given index."""
    def childCount(self) -> int:
        """Determines the number of child Nodes of the Node."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def classification(nodeTypeName: str) -> str:
        """Retrieves the classification string for a node type."""
    def clearRestPosition(self) -> MStatus:
        """Clear the saved rest position of this transform."""
    def connectToCurvePlug(self, curvePlug: MPlug) -> MStatus:
        """Connect to the curve plug."""
    def connectToParamPlug(self, paramPlug: MPlug) -> MStatus:
        """Connect to the param plug."""
    @overload
    def create(self) -> MObject: ...
    @overload
    def create(self, manipName: str, paramName: str) -> MObject: ...
    @overload
    def create(self, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, type: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, type: str, name: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str) -> MObject: ...
    @overload
    def create(self, type: str) -> MObject: ...
    @overload
    def create(self, type: str, name: str) -> MObject:
        """Creates a new PointOnCurveManip."""
    def curveIndex(self) -> int:
        """Returns the index of the curve."""
    def curvePoint(self) -> MPoint:
        """Returns the curve point."""
    def dagPath(self) -> MDagPath:
        """Returns the DagPath to which the Function Set is attached."""
    def dagRoot(self) -> MObject:
        """Determines the root of the first DAG Path to the DAG Node attached to the Function Set."""
    @staticmethod
    def deallocateAllFlags(pluginName: str) -> MStatus:
        """Deallocates all of the node flags which are currently allocated to the specified plugin."""
    @staticmethod
    def deallocateFlag(pluginName: str, flag: int) -> MStatus:
        """Deallocates a node flag which was previously allocated by a call to allocateFlag ."""
    @staticmethod
    def deleteManipulator(manip: MObject) -> MStatus:
        """Delete a manipulator."""
    def dgCallbackIds(self, type: Any, callbackName: str, callbackId: MCallbackIdArray, value: MDoubleArray) -> MStatus:
        """This method provides a further breakdown of the per-callback time returned via dgCallbacks() by returning the data on a """
    def dgCallbacks(self, type: Any, callbackName: Any, value: MDoubleArray) -> MStatus:
        """Node callbacks that occur when timing is enabled get logged with the node and can be queried via this method."""
    def dgTimer(self, timerMetric: Any, timerType: Any) -> float:
        """The function returns the specified timer value for the current node."""
    def dgTimerOff(self) -> MStatus:
        """Indicates that this node should no longer collect DG timing data when DG timing is enabled."""
    def dgTimerOn(self) -> MStatus:
        """Indicates that this node should collect DG timing data whenever DG timing is enabled."""
    def dgTimerQueryState(self) -> Any:
        """The function returns the current on/off state of the node's timer."""
    def dgTimerReset(self) -> MStatus:
        """The function resets the dependency graph timers and counters for this node to zero."""
    def dormantColor(self) -> MColor:
        """Determines the dormant color used by this node."""
    def drawOverrideColor(self, color: MColor) -> bool:
        """Determines the draw override color used by this node."""
    def drawOverrideEnabled(self) -> bool:
        """Determines whether or not draw override is turned on for this node."""
    def drawOverrideIsReference(self) -> bool:
        """Determines whether or not Display Type of the draw override is Reference for this node."""
    def drawOverrideIsTemplate(self) -> bool:
        """Determines whether or not Display Type of the draw override is Template for this node."""
    @staticmethod
    def drawPlaneHandles() -> bool:
        """This method returns the global option that says if the planar manipulator handles should be drawn or not."""
    def duplicate(self, instance: bool = False, instanceLeaf: bool = False) -> MObject:
        """This method duplicates the DAG hierarchy rooted at the current node."""
    @staticmethod
    def enableDGTiming(enable: bool) -> None:
        """Globally enables or disables the DG node timing mechanism."""
    def enableLimit(self, type: int, flag: bool) -> MStatus:
        """Enable or disable the limit value for the specified limit type."""
    def findAlias(self, alias: str, attrObj: MObject) -> bool:
        """Retrieves the attribute with the given alias."""
    @overload
    def findPlug(self, attr: MObject, wantNetworkedPlug: bool) -> MPlug: ...
    @overload
    def findPlug(self, attrName: str, wantNetworkedPlug: bool) -> MPlug: ...
    @overload
    def findPlug(self, attr: MObject) -> MPlug: ...
    @overload
    def findPlug(self, attrName: str) -> MPlug:
        """Attempt to find a plug for the given attribute."""
    def fullPathName(self) -> str:
        """Return a string representing the full path from the root of the dag to this object."""
    def getAffectedAttributes(self, attr: MObject, affectedAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that are affected by the attribute passed in."""
    def getAffectedByAttributes(self, attr: MObject, affectedByAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that affect the attribute passed in, attr ."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute al"""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns a list of all attribute aliases for this node."""
    def getAllPaths(self, paths: MDagPathArray) -> MStatus:
        """Determines all DAG Paths to the DAG Node attached to the Function Set."""
    def getConnectedSetsAndMembers(self, instanceNumber: int, sets: MObjectArray, comps: MObjectArray, renderableSetsOnly: bool) -> MStatus:
        """Returns all the sets connected to the specified instance of this DAG object."""
    def getConnections(self, array: MPlugArray) -> MStatus:
        """Get all of the current connections to this node as an array of plugs."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> MStatus:
        """Returns the external content (files) that this node depends on."""
    def getPath(self, path: MDagPath) -> MStatus:
        """Returns a DAG Path to the DAG Node attached to the Function Set."""
    @overload
    def getRotation(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def getRotation(self, rotation: MEulerRotation) -> MStatus: ...
    @overload
    def getRotation(self, order: int) -> MStatus: ...
    @overload
    def getRotation(self, order: int, space: int) -> MStatus:
        """Retrieve the rotation component of this transformation as a quaternion."""
    def getRotationQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Retrieve the rotation component of this transformation as a quaternion."""
    def getScale(self) -> MStatus:
        """Retrieve the scaling component of this transformation."""
    def getShear(self) -> MStatus:
        """Retrieve the shearing component of this transformation."""
    def getTranslation(self, space: int) -> MVector:
        """Retrieve the translation component of this transformation in centimeters."""
    @staticmethod
    def globalSize() -> float:
        """Returns the global manipulator size."""
    @staticmethod
    def handleSize() -> float:
        """Returns the manipulator handle size."""
    def hasAttribute(self, name: str) -> bool:
        """Returns true if the node already has an attribute with the given name."""
    def hasChild(self, node: MObject) -> bool:
        """Determines whether or not the given Node is a child of the DAG Node attached to the Function Set."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    def hasParent(self, node: MObject) -> bool:
        """Determines whether or not the given Node is a parent of the DAG Node attached to the Function Set."""
    def hasUniqueName(self) -> bool:
        """Indicates whether or not this node's name is unique within the scene."""
    def hiliteColor(self) -> MColor:
        """Determines the current hilite color used by the node."""
    def icon(self) -> str:
        """Returns the custom icon filename associated with the node."""
    def inModel(self) -> bool:
        """Determines whether or not the DAG Node is in the model."""
    def inUnderWorld(self) -> bool:
        """Determines whether or not the DAG Node is an underworld node."""
    def instanceCount(self, total: bool) -> int:
        """Determines the number of times the Node attached to the Function Set is instanced."""
    def isChildOf(self, node: MObject) -> bool:
        """Determines whether or not the DAG Node attached to the Function Set is a child of the given node."""
    def isDefaultNode(self) -> bool:
        """Returns true if the node is a default node."""
    def isDrawCurveOn(self) -> bool:
        """Returns whether or not the curve is drawn."""
    def isFlagSet(self, flag: int) -> bool:
        """Retrieves the current state of the specified flag for a node."""
    def isFromReferencedFile(self) -> bool:
        """Indicates whether or not this node came from a referenced file."""
    def isInstanceable(self) -> bool:
        """Returns true if the DAG node can be instanced, and false otherwise."""
    def isInstanced(self, indirect: bool = True) -> bool:
        """Determines whether the DAG Node attached to the Function Set is directly or indirectly instanced."""
    def isInstancedAttribute(self, attr: MObject) -> bool:
        """Returns true if the specified attribute is instanced."""
    def isIntermediateObject(self) -> bool:
        """Returns true if this object is an intermediate in a geometry calculation."""
    def isLimited(self, type: int) -> bool:
        """Determine if the specified limit attribute is enabled or disabled."""
    def isLocked(self) -> bool:
        """Indicates whether or not this node is locked."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Indicates whether or not the specified attribute was added to this node within the current scene."""
    def isOptimizePlaybackOn(self) -> bool:
        """Returns whether or not optimize playback is on."""
    def isParentOf(self, node: MObject) -> bool:
        """Determines whether or not the DAG Node attached to the Function Set is a parent of the given node."""
    def isShared(self) -> bool:
        """Indicates whether or not this node is shared."""
    def isTrackingEdits(self) -> bool:
        """Returns whether or not edits on the given node are being tracked by the generalized edit system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def isVisible(self) -> bool:
        """Returns whether or not the manipulator is visible."""
    def limitValue(self, type: int) -> float:
        """Determine the current value of the specified limit."""
    @staticmethod
    def lineSize() -> float:
        """Returns the manipulator line size."""
    def manipScale(self) -> float:
        """Returns the manipulator scale."""
    def model(self) -> MObject:
        """Deprecated in 2016.0"""
    def name(self) -> str:
        """Returns the name of this node."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def objectColor(self) -> int:
        """Deprecated in 2016.0"""
    def objectColorIndex(self) -> int:
        """Determines the index for the current user defined inactive color used by the node."""
    def objectColorRGB(self) -> MColor:
        """Determines the RGB color for the current user defined inactive color used by the node."""
    def objectColorType(self) -> Any:
        """Determines whether or not the user defined inactive color will be used for the node, or whether the default inactive col"""
    def objectGroupComponent(self, *args: Any, **kwargs: Any) -> Any: ...
    def paramIndex(self) -> int:
        """Returns the index of the parameter of the PointOnCurveManip."""
    def parameter(self) -> float:
        """Returns the parameter."""
    def parent(self, i: int) -> MObject:
        """Queries the DAG Node attached to the Function Set for the parent Node corresponding to the given index."""
    def parentCount(self) -> int:
        """Determines the number of parent Nodes of the Node."""
    def parentNamespace(self) -> str:
        """Returns the name of the namespace in which this node resides."""
    def partialPathName(self) -> str:
        """Return a string representing the partial path from the root of the dag to this object."""
    def pluginName(self) -> str:
        """Returns the name of the plug-in this MFnDependendencyNode was defined in."""
    def plugsAlias(self, plug: MPlug) -> str:
        """Returns the alias for the plug's attribute or the empty string if that attribute has no alias."""
    @overload
    def removeAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def removeAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Remove a dynamic attribute from a node."""
    def removeChild(self, child: MObject) -> MStatus:
        """Removes the given DAG Node from the parent."""
    def removeChildAt(self, index: int) -> MStatus:
        """Removes the child at the given index from the parent."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Some nodes, such as the various animCurve nodes, require that their attributes be set in a specific order for proper ope"""
    def resetFromRestPosition(self) -> MStatus:
        """Reset the transform to its rest position."""
    def resetTransformation(self, m: MMatrix) -> MStatus:
        """Reset this transform to equal the given matrix in world space."""
    def restPosition(self) -> MTransformationMatrix:
        """Retrieve the saved rest position of this transform."""
    @overload
    def rotateBy(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def rotateBy(self, rotation: MEulerRotation, Space: int | None = None) -> MStatus: ...
    @overload
    def rotateBy(self, order: int, Space: int | None = None) -> MStatus:
        """Relatively change the rotation of this transformation using a quaternion."""
    def rotateByQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Relatively change the rotation of this transformation using a quaternion."""
    def rotateOrientation(self, space: int) -> MQuaternion:
        """Returns the rotation used to orient the local rotation space."""
    def rotatePivot(self, space: int) -> MPoint:
        """Returns the pivot about which the rotation is applied."""
    def rotatePivotTranslation(self, space: int) -> MVector:
        """Return the rotate pivot translation in centimeters."""
    def rotateXYZValue(self, valIndex: int) -> MEulerRotation:
        """Gets the rotation for the active manipulator."""
    def rotationOrder(self) -> int:
        """Returns the rotation order for the transform matrix - the order in which the Euler angles are applied to create the end """
    def scaleBy(self) -> MStatus:
        """Relatively scale this transformation."""
    def scalePivot(self, space: int) -> MPoint:
        """Returns the pivot around which the scale is applied."""
    def scalePivotTranslation(self, space: int) -> MVector:
        """Returns the scale pivot translation in centimeters."""
    def set(self, transform: MTransformationMatrix) -> MStatus:
        """Change this transform to equal the given matrix."""
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setDoNotWrite(self, flag: bool) -> MStatus:
        """Use this method to mark the "do not write" state of this node."""
    def setDrawCurve(self, state: bool) -> MStatus:
        """Sets whether or not the curve is drawn."""
    @staticmethod
    def setDrawPlaneHandles(drawPlaneHandles: bool) -> None:
        """Sets the global option to display planar handles or not on supported manipulators."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> MStatus:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> MStatus:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> MStatus:
        """Sets the state of the specified flag for the node."""
    @staticmethod
    def setGlobalSize(size: float) -> None:
        """Sets the global manipulator size."""
    @staticmethod
    def setHandleSize(size: float) -> None:
        """Sets the manipulator handle size."""
    def setIcon(self, filename: str) -> MStatus:
        """Associates a custom icon with the node for display in the Maya UI."""
    def setInstanceable(self, how: bool) -> MStatus:
        """Sets whether or not the DAG node is instanceable."""
    def setIntermediateObject(self, isIntermediate: bool) -> MStatus:
        """Sets whether this object is an intermediate in a geometry calculation."""
    def setLimit(self, type: int, value: float) -> MStatus:
        """Change the limit value for the specified limit type, and automatically enable the limit to be true."""
    @staticmethod
    def setLineSize(size: float) -> None:
        """Sets the manipulator line size."""
    def setLocked(self, locked: bool) -> MStatus:
        """Locks or unlocks this node."""
    def setManipScale(self, size: float) -> MStatus:
        """Sets the manipulator scale."""
    @overload
    def setName(self, name: str, createNamespace: bool = False) -> str: ...
    @overload
    def setName(self, name: str) -> str:
        """Sets the name of this node."""
    @overload
    def setObject(self, path: MDagPath) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches Function Set to the DAG Node that has the given DAG Path."""
    @overload
    def setObjectColor(self, color: int) -> MStatus: ...
    @overload
    def setObjectColor(self, color: MColor) -> MStatus:
        """Sets the index for the current user defined inactive color used by the node."""
    def setObjectColorType(self, type: Any) -> MStatus:
        """Sets whether or not the user defined inactive object color will be used."""
    def setOptimizePlayback(self, optimizePlayback: bool) -> MStatus:
        """Sets whether or not to optimize the playback."""
    def setParameter(self, parameter: float) -> MStatus:
        """Sets the parameter."""
    def setRestPosition(self, matrix: MTransformationMatrix) -> MStatus:
        """Change the saved rest position of this transform."""
    def setRotateOrientation(self, quat: MQuaternion, space: int, balance: bool) -> MStatus:
        """Set the rotation used to orient the local rotation space."""
    def setRotatePivot(self, point: MPoint, space: int, balance: bool) -> MStatus:
        """Set the rotate pivot in centimeters about which rotation is applied."""
    def setRotatePivotTranslation(self, vec: MVector, space: int) -> MStatus:
        """Set the rotate pivot translation in centimeters."""
    @overload
    def setRotation(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def setRotation(self, rotation: MEulerRotation) -> MStatus: ...
    @overload
    def setRotation(self, order: int) -> MStatus: ...
    @overload
    def setRotation(self, RotationOrder: int, space: int) -> MStatus:
        """Change the rotation component of this transformation using a quaternion."""
    def setRotationOrder(self, order: int, reorder: bool) -> MStatus:
        """Change the rotation order for the transform - the order in which the Euler angles are applied to create the end rotation"""
    def setRotationQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Change the rotation component of this transformation using a quaternion."""
    def setScale(self) -> MStatus:
        """Set the scaling component of this transformation."""
    def setScalePivot(self, point: MPoint, space: int, balance: bool) -> MStatus:
        """Set the pivot around which the scale is applied in centimeters."""
    def setScalePivotTranslation(self, vec: MVector, space: int) -> MStatus:
        """Set the scale pivot translation in centimeters."""
    def setShear(self) -> MStatus:
        """Set the shearing component of this transformation."""
    def setTranslation(self, vec: MVector, space: int) -> MStatus:
        """Change the translation component of this transformation."""
    def setUseObjectColor(self, useObjectColor: bool) -> MStatus:
        """Deprecated in 2016.0"""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def setVisible(self, isVisible: bool) -> MStatus:
        """Sets whether or not the manipulator is visible."""
    def shearBy(self) -> MStatus:
        """Relatively shear this transformation."""
    def transformation(self) -> MTransformationMatrix:
        """Retrieve the transformation matrix represented by this transform."""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
    def translateBy(self, vec: MVector, space: int) -> MStatus:
        """Relatively change the translation component of this transformation."""
    def translation(self, Space: int) -> MVector:
        """Deprecated in 2018.0"""
    def type(self) -> int:
        """Function set type."""
    def typeId(self) -> MTypeId:
        """Returns the type id of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""
    @staticmethod
    def typeString(Type: int) -> str:
        """Introduced in 2020.0"""
    def uniqueName(self) -> str:
        """Introduced in 2023.0"""
    def userNode(self) -> Any:
        """If the function set's node is a plug-in node, then this method will extract the MPxNode pointer from it."""
    def usingHiliteColor(self) -> bool:
        """Determines whether or not the hilite color will be used for the node."""
    def usingObjectColor(self) -> bool:
        """Deprecated in 2016.0"""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnPointOnSurfaceManip:
    kExtensionAttr: Any
    kInvalidAttr: Any
    kLocalDynamicAttr: Any
    kNextPos: Any
    kNormalAttr: Any
    kRotateMaxX: Any
    kRotateMaxY: Any
    kRotateMaxZ: Any
    kRotateMinX: Any
    kRotateMinY: Any
    kRotateMinZ: Any
    kScaleMaxX: Any
    kScaleMaxY: Any
    kScaleMaxZ: Any
    kScaleMinX: Any
    kScaleMinY: Any
    kScaleMinZ: Any
    kShearMaxXY: Any
    kShearMaxXZ: Any
    kShearMaxYZ: Any
    kShearMinXY: Any
    kShearMinXZ: Any
    kShearMinYZ: Any
    kTimerInvalidState: Any
    kTimerMetric_callback: Any
    kTimerMetric_callbackNotViaAPI: Any
    kTimerMetric_callbackViaAPI: Any
    kTimerMetric_compute: Any
    kTimerMetric_computeDuringCallback: Any
    kTimerMetric_computeNotDuringCallback: Any
    kTimerMetric_dirty: Any
    kTimerMetric_draw: Any
    kTimerMetric_fetch: Any
    kTimerMetrics: Any
    kTimerOff: Any
    kTimerOn: Any
    kTimerType_count: Any
    kTimerType_inclusive: Any
    kTimerType_self: Any
    kTimerTypes: Any
    kTimerUninitialized: Any
    kTranslateMaxX: Any
    kTranslateMaxY: Any
    kTranslateMaxZ: Any
    kTranslateMinX: Any
    kTranslateMinY: Any
    kTranslateMinZ: Any
    kUseDefaultColor: Any
    kUseIndexColor: Any
    kUseRGBColor: Any
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None: ...
    @overload
    def __init__(self, object: MDagPath) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None:
        """Default constructor."""
    def absoluteName(self) -> str:
        """Returns the absolute name of this node."""
    def activeColor(self) -> MColor:
        """Determines the active color used by this node."""
    @overload
    def addAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def addAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Add a new dynamic attibute to this node."""
    def addChild(self, child: MObject, index: int, keepExistingParents: bool = False) -> MStatus:
        """Makes the given DAG Node a child of the DAG Node to which this instance of the Function Set is attached."""
    def addExternalContentForFileAttr(self, table: MExternalContentInfoTable, attr: MObject) -> MStatus:
        """Adds content info to the specified table from a file path attribute."""
    def affectsAnimation(self) -> bool:
        """Introduced in 2019.0"""
    @staticmethod
    def allocateFlag(pluginName: str) -> int:
        """Allocates a node flag for sole use by the caller."""
    @overload
    def attribute(self, index: int) -> MObject: ...
    @overload
    def attribute(self, attrName: str) -> MObject:
        """Finds the attribute of this node at the given index."""
    def attributeClass(self, attr: MObject) -> Any:
        """Returns the class (normal, dynamic, extension) of the specified attribute."""
    def attributeCount(self) -> int:
        """Returns the number of attributes that this node has."""
    @staticmethod
    def balanceTransformation(identity: int, identity_: int, one: int, kXYZ: int, arg: Any = True) -> None:
        """Balance a transformation when applying a world matrix to a joint."""
    def boundingBox(self) -> Any:
        """Returns the bounding box for the dag node in object space."""
    def canBeWritten(self) -> bool:
        """Returns the do not write state of the node."""
    def child(self, i: int) -> MObject:
        """Queries the DAG Node attached to the Function Set for the child Node corresponding to the given index."""
    def childCount(self) -> int:
        """Determines the number of child Nodes of the Node."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def classification(nodeTypeName: str) -> str:
        """Retrieves the classification string for a node type."""
    def clearRestPosition(self) -> MStatus:
        """Clear the saved rest position of this transform."""
    def connectToParamPlug(self, paramPlug: MPlug) -> MStatus:
        """Connect to the param plug."""
    def connectToSurfacePlug(self, surfacePlug: MPlug) -> MStatus:
        """Connect to the surface plug."""
    @overload
    def create(self) -> MObject: ...
    @overload
    def create(self, manipName: str, paramName: str) -> MObject: ...
    @overload
    def create(self, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, type: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, type: str, name: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str) -> MObject: ...
    @overload
    def create(self, type: str) -> MObject: ...
    @overload
    def create(self, type: str, name: str) -> MObject:
        """Creates a new PointOnSurfaceManip."""
    def dagPath(self) -> MDagPath:
        """Returns the DagPath to which the Function Set is attached."""
    def dagRoot(self) -> MObject:
        """Determines the root of the first DAG Path to the DAG Node attached to the Function Set."""
    @staticmethod
    def deallocateAllFlags(pluginName: str) -> MStatus:
        """Deallocates all of the node flags which are currently allocated to the specified plugin."""
    @staticmethod
    def deallocateFlag(pluginName: str, flag: int) -> MStatus:
        """Deallocates a node flag which was previously allocated by a call to allocateFlag ."""
    @staticmethod
    def deleteManipulator(manip: MObject) -> MStatus:
        """Delete a manipulator."""
    def dgCallbackIds(self, type: Any, callbackName: str, callbackId: MCallbackIdArray, value: MDoubleArray) -> MStatus:
        """This method provides a further breakdown of the per-callback time returned via dgCallbacks() by returning the data on a """
    def dgCallbacks(self, type: Any, callbackName: Any, value: MDoubleArray) -> MStatus:
        """Node callbacks that occur when timing is enabled get logged with the node and can be queried via this method."""
    def dgTimer(self, timerMetric: Any, timerType: Any) -> float:
        """The function returns the specified timer value for the current node."""
    def dgTimerOff(self) -> MStatus:
        """Indicates that this node should no longer collect DG timing data when DG timing is enabled."""
    def dgTimerOn(self) -> MStatus:
        """Indicates that this node should collect DG timing data whenever DG timing is enabled."""
    def dgTimerQueryState(self) -> Any:
        """The function returns the current on/off state of the node's timer."""
    def dgTimerReset(self) -> MStatus:
        """The function resets the dependency graph timers and counters for this node to zero."""
    def dormantColor(self) -> MColor:
        """Determines the dormant color used by this node."""
    def drawOverrideColor(self, color: MColor) -> bool:
        """Determines the draw override color used by this node."""
    def drawOverrideEnabled(self) -> bool:
        """Determines whether or not draw override is turned on for this node."""
    def drawOverrideIsReference(self) -> bool:
        """Determines whether or not Display Type of the draw override is Reference for this node."""
    def drawOverrideIsTemplate(self) -> bool:
        """Determines whether or not Display Type of the draw override is Template for this node."""
    @staticmethod
    def drawPlaneHandles() -> bool:
        """This method returns the global option that says if the planar manipulator handles should be drawn or not."""
    def duplicate(self, instance: bool = False, instanceLeaf: bool = False) -> MObject:
        """This method duplicates the DAG hierarchy rooted at the current node."""
    @staticmethod
    def enableDGTiming(enable: bool) -> None:
        """Globally enables or disables the DG node timing mechanism."""
    def enableLimit(self, type: int, flag: bool) -> MStatus:
        """Enable or disable the limit value for the specified limit type."""
    def findAlias(self, alias: str, attrObj: MObject) -> bool:
        """Retrieves the attribute with the given alias."""
    @overload
    def findPlug(self, attr: MObject, wantNetworkedPlug: bool) -> MPlug: ...
    @overload
    def findPlug(self, attrName: str, wantNetworkedPlug: bool) -> MPlug: ...
    @overload
    def findPlug(self, attr: MObject) -> MPlug: ...
    @overload
    def findPlug(self, attrName: str) -> MPlug:
        """Attempt to find a plug for the given attribute."""
    def fullPathName(self) -> str:
        """Return a string representing the full path from the root of the dag to this object."""
    def getAffectedAttributes(self, attr: MObject, affectedAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that are affected by the attribute passed in."""
    def getAffectedByAttributes(self, attr: MObject, affectedByAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that affect the attribute passed in, attr ."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute al"""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns a list of all attribute aliases for this node."""
    def getAllPaths(self, paths: MDagPathArray) -> MStatus:
        """Determines all DAG Paths to the DAG Node attached to the Function Set."""
    def getConnectedSetsAndMembers(self, instanceNumber: int, sets: MObjectArray, comps: MObjectArray, renderableSetsOnly: bool) -> MStatus:
        """Returns all the sets connected to the specified instance of this DAG object."""
    def getConnections(self, array: MPlugArray) -> MStatus:
        """Get all of the current connections to this node as an array of plugs."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> MStatus:
        """Returns the external content (files) that this node depends on."""
    def getParameters(self, u: float, v: float) -> MStatus:
        """Returns the parameter."""
    def getPath(self, path: MDagPath) -> MStatus:
        """Returns a DAG Path to the DAG Node attached to the Function Set."""
    @overload
    def getRotation(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def getRotation(self, rotation: MEulerRotation) -> MStatus: ...
    @overload
    def getRotation(self, order: int) -> MStatus: ...
    @overload
    def getRotation(self, order: int, space: int) -> MStatus:
        """Retrieve the rotation component of this transformation as a quaternion."""
    def getRotationQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Retrieve the rotation component of this transformation as a quaternion."""
    def getScale(self) -> MStatus:
        """Retrieve the scaling component of this transformation."""
    def getShear(self) -> MStatus:
        """Retrieve the shearing component of this transformation."""
    def getTranslation(self, space: int) -> MVector:
        """Retrieve the translation component of this transformation in centimeters."""
    @staticmethod
    def globalSize() -> float:
        """Returns the global manipulator size."""
    @staticmethod
    def handleSize() -> float:
        """Returns the manipulator handle size."""
    def hasAttribute(self, name: str) -> bool:
        """Returns true if the node already has an attribute with the given name."""
    def hasChild(self, node: MObject) -> bool:
        """Determines whether or not the given Node is a child of the DAG Node attached to the Function Set."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    def hasParent(self, node: MObject) -> bool:
        """Determines whether or not the given Node is a parent of the DAG Node attached to the Function Set."""
    def hasUniqueName(self) -> bool:
        """Indicates whether or not this node's name is unique within the scene."""
    def hiliteColor(self) -> MColor:
        """Determines the current hilite color used by the node."""
    def icon(self) -> str:
        """Returns the custom icon filename associated with the node."""
    def inModel(self) -> bool:
        """Determines whether or not the DAG Node is in the model."""
    def inUnderWorld(self) -> bool:
        """Determines whether or not the DAG Node is an underworld node."""
    def instanceCount(self, total: bool) -> int:
        """Determines the number of times the Node attached to the Function Set is instanced."""
    def isChildOf(self, node: MObject) -> bool:
        """Determines whether or not the DAG Node attached to the Function Set is a child of the given node."""
    def isDefaultNode(self) -> bool:
        """Returns true if the node is a default node."""
    def isDrawSurfaceOn(self) -> bool:
        """Returns whether or not the surface is drawn."""
    def isFlagSet(self, flag: int) -> bool:
        """Retrieves the current state of the specified flag for a node."""
    def isFromReferencedFile(self) -> bool:
        """Indicates whether or not this node came from a referenced file."""
    def isInstanceable(self) -> bool:
        """Returns true if the DAG node can be instanced, and false otherwise."""
    def isInstanced(self, indirect: bool = True) -> bool:
        """Determines whether the DAG Node attached to the Function Set is directly or indirectly instanced."""
    def isInstancedAttribute(self, attr: MObject) -> bool:
        """Returns true if the specified attribute is instanced."""
    def isIntermediateObject(self) -> bool:
        """Returns true if this object is an intermediate in a geometry calculation."""
    def isLimited(self, type: int) -> bool:
        """Determine if the specified limit attribute is enabled or disabled."""
    def isLocked(self) -> bool:
        """Indicates whether or not this node is locked."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Indicates whether or not the specified attribute was added to this node within the current scene."""
    def isOptimizePlaybackOn(self) -> bool:
        """Returns whether or not optimize playback is on."""
    def isParentOf(self, node: MObject) -> bool:
        """Determines whether or not the DAG Node attached to the Function Set is a parent of the given node."""
    def isShared(self) -> bool:
        """Indicates whether or not this node is shared."""
    def isTrackingEdits(self) -> bool:
        """Returns whether or not edits on the given node are being tracked by the generalized edit system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def isVisible(self) -> bool:
        """Returns whether or not the manipulator is visible."""
    def limitValue(self, type: int) -> float:
        """Determine the current value of the specified limit."""
    @staticmethod
    def lineSize() -> float:
        """Returns the manipulator line size."""
    def manipScale(self) -> float:
        """Returns the manipulator scale."""
    def model(self) -> MObject:
        """Deprecated in 2016.0"""
    def name(self) -> str:
        """Returns the name of this node."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def objectColor(self) -> int:
        """Deprecated in 2016.0"""
    def objectColorIndex(self) -> int:
        """Determines the index for the current user defined inactive color used by the node."""
    def objectColorRGB(self) -> MColor:
        """Determines the RGB color for the current user defined inactive color used by the node."""
    def objectColorType(self) -> Any:
        """Determines whether or not the user defined inactive color will be used for the node, or whether the default inactive col"""
    def objectGroupComponent(self, *args: Any, **kwargs: Any) -> Any: ...
    def paramIndex(self) -> int:
        """Returns the index of the parameter of the PointOnSurfaceManip."""
    def parent(self, i: int) -> MObject:
        """Queries the DAG Node attached to the Function Set for the parent Node corresponding to the given index."""
    def parentCount(self) -> int:
        """Determines the number of parent Nodes of the Node."""
    def parentNamespace(self) -> str:
        """Returns the name of the namespace in which this node resides."""
    def partialPathName(self) -> str:
        """Return a string representing the partial path from the root of the dag to this object."""
    def pluginName(self) -> str:
        """Returns the name of the plug-in this MFnDependendencyNode was defined in."""
    def plugsAlias(self, plug: MPlug) -> str:
        """Returns the alias for the plug's attribute or the empty string if that attribute has no alias."""
    @overload
    def removeAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def removeAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Remove a dynamic attribute from a node."""
    def removeChild(self, child: MObject) -> MStatus:
        """Removes the given DAG Node from the parent."""
    def removeChildAt(self, index: int) -> MStatus:
        """Removes the child at the given index from the parent."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Some nodes, such as the various animCurve nodes, require that their attributes be set in a specific order for proper ope"""
    def resetFromRestPosition(self) -> MStatus:
        """Reset the transform to its rest position."""
    def resetTransformation(self, m: MMatrix) -> MStatus:
        """Reset this transform to equal the given matrix in world space."""
    def restPosition(self) -> MTransformationMatrix:
        """Retrieve the saved rest position of this transform."""
    @overload
    def rotateBy(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def rotateBy(self, rotation: MEulerRotation, Space: int | None = None) -> MStatus: ...
    @overload
    def rotateBy(self, order: int, Space: int | None = None) -> MStatus:
        """Relatively change the rotation of this transformation using a quaternion."""
    def rotateByQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Relatively change the rotation of this transformation using a quaternion."""
    def rotateOrientation(self, space: int) -> MQuaternion:
        """Returns the rotation used to orient the local rotation space."""
    def rotatePivot(self, space: int) -> MPoint:
        """Returns the pivot about which the rotation is applied."""
    def rotatePivotTranslation(self, space: int) -> MVector:
        """Return the rotate pivot translation in centimeters."""
    def rotateXYZValue(self, valIndex: int) -> MEulerRotation:
        """Gets the rotation for the active manipulator."""
    def rotationOrder(self) -> int:
        """Returns the rotation order for the transform matrix - the order in which the Euler angles are applied to create the end """
    def scaleBy(self) -> MStatus:
        """Relatively scale this transformation."""
    def scalePivot(self, space: int) -> MPoint:
        """Returns the pivot around which the scale is applied."""
    def scalePivotTranslation(self, space: int) -> MVector:
        """Returns the scale pivot translation in centimeters."""
    def set(self, transform: MTransformationMatrix) -> MStatus:
        """Change this transform to equal the given matrix."""
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setDoNotWrite(self, flag: bool) -> MStatus:
        """Use this method to mark the "do not write" state of this node."""
    def setDrawArrows(self, state: bool) -> MStatus:
        """Sets whether or not the arrows should be drawn."""
    @staticmethod
    def setDrawPlaneHandles(drawPlaneHandles: bool) -> None:
        """Sets the global option to display planar handles or not on supported manipulators."""
    def setDrawSurface(self, state: bool) -> MStatus:
        """Sets whether or not the surface is drawn."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> MStatus:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> MStatus:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> MStatus:
        """Sets the state of the specified flag for the node."""
    @staticmethod
    def setGlobalSize(size: float) -> None:
        """Sets the global manipulator size."""
    @staticmethod
    def setHandleSize(size: float) -> None:
        """Sets the manipulator handle size."""
    def setIcon(self, filename: str) -> MStatus:
        """Associates a custom icon with the node for display in the Maya UI."""
    def setInstanceable(self, how: bool) -> MStatus:
        """Sets whether or not the DAG node is instanceable."""
    def setIntermediateObject(self, isIntermediate: bool) -> MStatus:
        """Sets whether this object is an intermediate in a geometry calculation."""
    def setLimit(self, type: int, value: float) -> MStatus:
        """Change the limit value for the specified limit type, and automatically enable the limit to be true."""
    @staticmethod
    def setLineSize(size: float) -> None:
        """Sets the manipulator line size."""
    def setLocked(self, locked: bool) -> MStatus:
        """Locks or unlocks this node."""
    def setManipScale(self, size: float) -> MStatus:
        """Sets the manipulator scale."""
    @overload
    def setName(self, name: str, createNamespace: bool = False) -> str: ...
    @overload
    def setName(self, name: str) -> str:
        """Sets the name of this node."""
    @overload
    def setObject(self, path: MDagPath) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches Function Set to the DAG Node that has the given DAG Path."""
    @overload
    def setObjectColor(self, color: int) -> MStatus: ...
    @overload
    def setObjectColor(self, color: MColor) -> MStatus:
        """Sets the index for the current user defined inactive color used by the node."""
    def setObjectColorType(self, type: Any) -> MStatus:
        """Sets whether or not the user defined inactive object color will be used."""
    def setOptimizePlayback(self, optimizePlayback: bool) -> MStatus:
        """Sets whether or not to optimize the playback."""
    def setParameters(self, u: float, v: float) -> MStatus:
        """Sets the u and v parameters."""
    def setRestPosition(self, matrix: MTransformationMatrix) -> MStatus:
        """Change the saved rest position of this transform."""
    def setRotateOrientation(self, quat: MQuaternion, space: int, balance: bool) -> MStatus:
        """Set the rotation used to orient the local rotation space."""
    def setRotatePivot(self, point: MPoint, space: int, balance: bool) -> MStatus:
        """Set the rotate pivot in centimeters about which rotation is applied."""
    def setRotatePivotTranslation(self, vec: MVector, space: int) -> MStatus:
        """Set the rotate pivot translation in centimeters."""
    @overload
    def setRotation(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def setRotation(self, rotation: MEulerRotation) -> MStatus: ...
    @overload
    def setRotation(self, order: int) -> MStatus: ...
    @overload
    def setRotation(self, RotationOrder: int, space: int) -> MStatus:
        """Change the rotation component of this transformation using a quaternion."""
    def setRotationOrder(self, order: int, reorder: bool) -> MStatus:
        """Change the rotation order for the transform - the order in which the Euler angles are applied to create the end rotation"""
    def setRotationQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Change the rotation component of this transformation using a quaternion."""
    def setScale(self) -> MStatus:
        """Set the scaling component of this transformation."""
    def setScalePivot(self, point: MPoint, space: int, balance: bool) -> MStatus:
        """Set the pivot around which the scale is applied in centimeters."""
    def setScalePivotTranslation(self, vec: MVector, space: int) -> MStatus:
        """Set the scale pivot translation in centimeters."""
    def setShear(self) -> MStatus:
        """Set the shearing component of this transformation."""
    def setTranslation(self, vec: MVector, space: int) -> MStatus:
        """Change the translation component of this transformation."""
    def setUseObjectColor(self, useObjectColor: bool) -> MStatus:
        """Deprecated in 2016.0"""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def setVisible(self, isVisible: bool) -> MStatus:
        """Sets whether or not the manipulator is visible."""
    def shearBy(self) -> MStatus:
        """Relatively shear this transformation."""
    def surfaceIndex(self) -> int:
        """Returns the index of the surface."""
    def transformation(self) -> MTransformationMatrix:
        """Retrieve the transformation matrix represented by this transform."""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
    def translateBy(self, vec: MVector, space: int) -> MStatus:
        """Relatively change the translation component of this transformation."""
    def translation(self, Space: int) -> MVector:
        """Deprecated in 2018.0"""
    def type(self) -> int:
        """Function set type."""
    def typeId(self) -> MTypeId:
        """Returns the type id of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""
    @staticmethod
    def typeString(Type: int) -> str:
        """Introduced in 2020.0"""
    def uniqueName(self) -> str:
        """Introduced in 2023.0"""
    def userNode(self) -> Any:
        """If the function set's node is a plug-in node, then this method will extract the MPxNode pointer from it."""
    def usingHiliteColor(self) -> bool:
        """Determines whether or not the hilite color will be used for the node."""
    def usingObjectColor(self) -> bool:
        """Deprecated in 2016.0"""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnRotateManip:
    kExtensionAttr: Any
    kGimbal: Any
    kInvalidAttr: Any
    kLocalDynamicAttr: Any
    kNextPos: Any
    kNormalAttr: Any
    kObjectSpace: Any
    kRotateMaxX: Any
    kRotateMaxY: Any
    kRotateMaxZ: Any
    kRotateMinX: Any
    kRotateMinY: Any
    kRotateMinZ: Any
    kScaleMaxX: Any
    kScaleMaxY: Any
    kScaleMaxZ: Any
    kScaleMinX: Any
    kScaleMinY: Any
    kScaleMinZ: Any
    kShearMaxXY: Any
    kShearMaxXZ: Any
    kShearMaxYZ: Any
    kShearMinXY: Any
    kShearMinXZ: Any
    kShearMinYZ: Any
    kTimerInvalidState: Any
    kTimerMetric_callback: Any
    kTimerMetric_callbackNotViaAPI: Any
    kTimerMetric_callbackViaAPI: Any
    kTimerMetric_compute: Any
    kTimerMetric_computeDuringCallback: Any
    kTimerMetric_computeNotDuringCallback: Any
    kTimerMetric_dirty: Any
    kTimerMetric_draw: Any
    kTimerMetric_fetch: Any
    kTimerMetrics: Any
    kTimerOff: Any
    kTimerOn: Any
    kTimerType_count: Any
    kTimerType_inclusive: Any
    kTimerType_self: Any
    kTimerTypes: Any
    kTimerUninitialized: Any
    kTranslateMaxX: Any
    kTranslateMaxY: Any
    kTranslateMaxZ: Any
    kTranslateMinX: Any
    kTranslateMinY: Any
    kTranslateMinZ: Any
    kUseDefaultColor: Any
    kUseIndexColor: Any
    kUseRGBColor: Any
    kWorldSpace: Any
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None: ...
    @overload
    def __init__(self, object: MDagPath) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None:
        """Default constructor."""
    def absoluteName(self) -> str:
        """Returns the absolute name of this node."""
    def activeColor(self) -> MColor:
        """Determines the active color used by this node."""
    @overload
    def addAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def addAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Add a new dynamic attibute to this node."""
    def addChild(self, child: MObject, index: int, keepExistingParents: bool = False) -> MStatus:
        """Makes the given DAG Node a child of the DAG Node to which this instance of the Function Set is attached."""
    def addExternalContentForFileAttr(self, table: MExternalContentInfoTable, attr: MObject) -> MStatus:
        """Adds content info to the specified table from a file path attribute."""
    def affectsAnimation(self) -> bool:
        """Introduced in 2019.0"""
    @staticmethod
    def allocateFlag(pluginName: str) -> int:
        """Allocates a node flag for sole use by the caller."""
    @overload
    def attribute(self, index: int) -> MObject: ...
    @overload
    def attribute(self, attrName: str) -> MObject:
        """Finds the attribute of this node at the given index."""
    def attributeClass(self, attr: MObject) -> Any:
        """Returns the class (normal, dynamic, extension) of the specified attribute."""
    def attributeCount(self) -> int:
        """Returns the number of attributes that this node has."""
    @staticmethod
    def balanceTransformation(identity: int, identity_: int, one: int, kXYZ: int, arg: Any = True) -> None:
        """Balance a transformation when applying a world matrix to a joint."""
    def boundingBox(self) -> Any:
        """Returns the bounding box for the dag node in object space."""
    def canBeWritten(self) -> bool:
        """Returns the do not write state of the node."""
    def child(self, i: int) -> MObject:
        """Queries the DAG Node attached to the Function Set for the child Node corresponding to the given index."""
    def childCount(self) -> int:
        """Determines the number of child Nodes of the Node."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def classification(nodeTypeName: str) -> str:
        """Retrieves the classification string for a node type."""
    def clearRestPosition(self) -> MStatus:
        """Clear the saved rest position of this transform."""
    def connectToRotationCenterPlug(self, rotationCenterPlug: MPlug) -> MStatus:
        """Create a 1-1 association of the rotation center on the manipulator and the rotationCenterPlug parameter."""
    def connectToRotationPlug(self, rotationPlug: MPlug) -> MStatus:
        """Create a 1-1 connection from the rotation manipVal to the rotationPlug parameter."""
    @overload
    def create(self) -> MObject: ...
    @overload
    def create(self, manipName: str, rotationName: str) -> MObject: ...
    @overload
    def create(self, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, type: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, type: str, name: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str) -> MObject: ...
    @overload
    def create(self, type: str) -> MObject: ...
    @overload
    def create(self, type: str, name: str) -> MObject:
        """Creates a new RotateManip, and attaches this function set to the new manipulator."""
    def dagPath(self) -> MDagPath:
        """Returns the DagPath to which the Function Set is attached."""
    def dagRoot(self) -> MObject:
        """Determines the root of the first DAG Path to the DAG Node attached to the Function Set."""
    @staticmethod
    def deallocateAllFlags(pluginName: str) -> MStatus:
        """Deallocates all of the node flags which are currently allocated to the specified plugin."""
    @staticmethod
    def deallocateFlag(pluginName: str, flag: int) -> MStatus:
        """Deallocates a node flag which was previously allocated by a call to allocateFlag ."""
    @staticmethod
    def deleteManipulator(manip: MObject) -> MStatus:
        """Delete a manipulator."""
    def dgCallbackIds(self, type: Any, callbackName: str, callbackId: MCallbackIdArray, value: MDoubleArray) -> MStatus:
        """This method provides a further breakdown of the per-callback time returned via dgCallbacks() by returning the data on a """
    def dgCallbacks(self, type: Any, callbackName: Any, value: MDoubleArray) -> MStatus:
        """Node callbacks that occur when timing is enabled get logged with the node and can be queried via this method."""
    def dgTimer(self, timerMetric: Any, timerType: Any) -> float:
        """The function returns the specified timer value for the current node."""
    def dgTimerOff(self) -> MStatus:
        """Indicates that this node should no longer collect DG timing data when DG timing is enabled."""
    def dgTimerOn(self) -> MStatus:
        """Indicates that this node should collect DG timing data whenever DG timing is enabled."""
    def dgTimerQueryState(self) -> Any:
        """The function returns the current on/off state of the node's timer."""
    def dgTimerReset(self) -> MStatus:
        """The function resets the dependency graph timers and counters for this node to zero."""
    def displayWithNode(self, node: MObject) -> MStatus:
        """Configures the manipulator to display with the node, causing the position of the manipulator to follow the position of t"""
    def dormantColor(self) -> MColor:
        """Determines the dormant color used by this node."""
    def drawOverrideColor(self, color: MColor) -> bool:
        """Determines the draw override color used by this node."""
    def drawOverrideEnabled(self) -> bool:
        """Determines whether or not draw override is turned on for this node."""
    def drawOverrideIsReference(self) -> bool:
        """Determines whether or not Display Type of the draw override is Reference for this node."""
    def drawOverrideIsTemplate(self) -> bool:
        """Determines whether or not Display Type of the draw override is Template for this node."""
    @staticmethod
    def drawPlaneHandles() -> bool:
        """This method returns the global option that says if the planar manipulator handles should be drawn or not."""
    def duplicate(self, instance: bool = False, instanceLeaf: bool = False) -> MObject:
        """This method duplicates the DAG hierarchy rooted at the current node."""
    @staticmethod
    def enableDGTiming(enable: bool) -> None:
        """Globally enables or disables the DG node timing mechanism."""
    def enableLimit(self, type: int, flag: bool) -> MStatus:
        """Enable or disable the limit value for the specified limit type."""
    def findAlias(self, alias: str, attrObj: MObject) -> bool:
        """Retrieves the attribute with the given alias."""
    @overload
    def findPlug(self, attr: MObject, wantNetworkedPlug: bool) -> MPlug: ...
    @overload
    def findPlug(self, attrName: str, wantNetworkedPlug: bool) -> MPlug: ...
    @overload
    def findPlug(self, attr: MObject) -> MPlug: ...
    @overload
    def findPlug(self, attrName: str) -> MPlug:
        """Attempt to find a plug for the given attribute."""
    def fullPathName(self) -> str:
        """Return a string representing the full path from the root of the dag to this object."""
    def getAffectedAttributes(self, attr: MObject, affectedAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that are affected by the attribute passed in."""
    def getAffectedByAttributes(self, attr: MObject, affectedByAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that affect the attribute passed in, attr ."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute al"""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns a list of all attribute aliases for this node."""
    def getAllPaths(self, paths: MDagPathArray) -> MStatus:
        """Determines all DAG Paths to the DAG Node attached to the Function Set."""
    def getConnectedSetsAndMembers(self, instanceNumber: int, sets: MObjectArray, comps: MObjectArray, renderableSetsOnly: bool) -> MStatus:
        """Returns all the sets connected to the specified instance of this DAG object."""
    def getConnections(self, array: MPlugArray) -> MStatus:
        """Get all of the current connections to this node as an array of plugs."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> MStatus:
        """Returns the external content (files) that this node depends on."""
    def getPath(self, path: MDagPath) -> MStatus:
        """Returns a DAG Path to the DAG Node attached to the Function Set."""
    @overload
    def getRotation(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def getRotation(self, rotation: MEulerRotation) -> MStatus: ...
    @overload
    def getRotation(self, order: int) -> MStatus: ...
    @overload
    def getRotation(self, order: int, space: int) -> MStatus:
        """Retrieve the rotation component of this transformation as a quaternion."""
    def getRotationQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Retrieve the rotation component of this transformation as a quaternion."""
    def getScale(self) -> MStatus:
        """Retrieve the scaling component of this transformation."""
    def getShear(self) -> MStatus:
        """Retrieve the shearing component of this transformation."""
    def getTranslation(self, space: int) -> MVector:
        """Retrieve the translation component of this transformation in centimeters."""
    @staticmethod
    def globalSize() -> float:
        """Returns the global manipulator size."""
    @staticmethod
    def handleSize() -> float:
        """Returns the manipulator handle size."""
    def hasAttribute(self, name: str) -> bool:
        """Returns true if the node already has an attribute with the given name."""
    def hasChild(self, node: MObject) -> bool:
        """Determines whether or not the given Node is a child of the DAG Node attached to the Function Set."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    def hasParent(self, node: MObject) -> bool:
        """Determines whether or not the given Node is a parent of the DAG Node attached to the Function Set."""
    def hasUniqueName(self) -> bool:
        """Indicates whether or not this node's name is unique within the scene."""
    def hiliteColor(self) -> MColor:
        """Determines the current hilite color used by the node."""
    def icon(self) -> str:
        """Returns the custom icon filename associated with the node."""
    def inModel(self) -> bool:
        """Determines whether or not the DAG Node is in the model."""
    def inUnderWorld(self) -> bool:
        """Determines whether or not the DAG Node is an underworld node."""
    def instanceCount(self, total: bool) -> int:
        """Determines the number of times the Node attached to the Function Set is instanced."""
    def isChildOf(self, node: MObject) -> bool:
        """Determines whether or not the DAG Node attached to the Function Set is a child of the given node."""
    def isDefaultNode(self) -> bool:
        """Returns true if the node is a default node."""
    def isFlagSet(self, flag: int) -> bool:
        """Retrieves the current state of the specified flag for a node."""
    def isFromReferencedFile(self) -> bool:
        """Indicates whether or not this node came from a referenced file."""
    def isInstanceable(self) -> bool:
        """Returns true if the DAG node can be instanced, and false otherwise."""
    def isInstanced(self, indirect: bool = True) -> bool:
        """Determines whether the DAG Node attached to the Function Set is directly or indirectly instanced."""
    def isInstancedAttribute(self, attr: MObject) -> bool:
        """Returns true if the specified attribute is instanced."""
    def isIntermediateObject(self) -> bool:
        """Returns true if this object is an intermediate in a geometry calculation."""
    def isLimited(self, type: int) -> bool:
        """Determine if the specified limit attribute is enabled or disabled."""
    def isLocked(self) -> bool:
        """Indicates whether or not this node is locked."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Indicates whether or not the specified attribute was added to this node within the current scene."""
    def isOptimizePlaybackOn(self) -> bool:
        """Returns whether or not optimize playback is on."""
    def isParentOf(self, node: MObject) -> bool:
        """Determines whether or not the DAG Node attached to the Function Set is a parent of the given node."""
    def isShared(self) -> bool:
        """Indicates whether or not this node is shared."""
    def isSnapModeOn(self) -> bool:
        """Returns true when snap mode is on."""
    def isTrackingEdits(self) -> bool:
        """Returns whether or not edits on the given node are being tracked by the generalized edit system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def isVisible(self) -> bool:
        """Returns whether or not the manipulator is visible."""
    def limitValue(self, type: int) -> float:
        """Determine the current value of the specified limit."""
    @staticmethod
    def lineSize() -> float:
        """Returns the manipulator line size."""
    def manipScale(self) -> float:
        """Returns the manipulator scale."""
    def model(self) -> MObject:
        """Deprecated in 2016.0"""
    def name(self) -> str:
        """Returns the name of this node."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def objectColor(self) -> int:
        """Deprecated in 2016.0"""
    def objectColorIndex(self) -> int:
        """Determines the index for the current user defined inactive color used by the node."""
    def objectColorRGB(self) -> MColor:
        """Determines the RGB color for the current user defined inactive color used by the node."""
    def objectColorType(self) -> Any:
        """Determines whether or not the user defined inactive color will be used for the node, or whether the default inactive col"""
    def objectGroupComponent(self, *args: Any, **kwargs: Any) -> Any: ...
    def parent(self, i: int) -> MObject:
        """Queries the DAG Node attached to the Function Set for the parent Node corresponding to the given index."""
    def parentCount(self) -> int:
        """Determines the number of parent Nodes of the Node."""
    def parentNamespace(self) -> str:
        """Returns the name of the namespace in which this node resides."""
    def partialPathName(self) -> str:
        """Return a string representing the partial path from the root of the dag to this object."""
    def pluginName(self) -> str:
        """Returns the name of the plug-in this MFnDependendencyNode was defined in."""
    def plugsAlias(self, plug: MPlug) -> str:
        """Returns the alias for the plug's attribute or the empty string if that attribute has no alias."""
    @overload
    def removeAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def removeAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Remove a dynamic attribute from a node."""
    def removeChild(self, child: MObject) -> MStatus:
        """Removes the given DAG Node from the parent."""
    def removeChildAt(self, index: int) -> MStatus:
        """Removes the child at the given index from the parent."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Some nodes, such as the various animCurve nodes, require that their attributes be set in a specific order for proper ope"""
    def resetFromRestPosition(self) -> MStatus:
        """Reset the transform to its rest position."""
    def resetTransformation(self, m: MMatrix) -> MStatus:
        """Reset this transform to equal the given matrix in world space."""
    def restPosition(self) -> MTransformationMatrix:
        """Retrieve the saved rest position of this transform."""
    @overload
    def rotateBy(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def rotateBy(self, rotation: MEulerRotation, Space: int | None = None) -> MStatus: ...
    @overload
    def rotateBy(self, order: int, Space: int | None = None) -> MStatus:
        """Relatively change the rotation of this transformation using a quaternion."""
    def rotateByQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Relatively change the rotation of this transformation using a quaternion."""
    def rotateMode(self) -> Any:
        """Returns the current rotation mode."""
    def rotateOrientation(self, space: int) -> MQuaternion:
        """Returns the rotation used to orient the local rotation space."""
    def rotatePivot(self, space: int) -> MPoint:
        """Returns the pivot about which the rotation is applied."""
    def rotatePivotTranslation(self, space: int) -> MVector:
        """Return the rotate pivot translation in centimeters."""
    def rotateXYZValue(self, valIndex: int) -> MEulerRotation:
        """Gets the rotation for the active manipulator."""
    def rotationCenterIndex(self) -> int:
        """Returns the index of the rotation center for the manipulator."""
    def rotationIndex(self) -> int:
        """Returns the index of the rotation manipVal for the manipulator."""
    def rotationOrder(self) -> int:
        """Returns the rotation order for the transform matrix - the order in which the Euler angles are applied to create the end """
    def scaleBy(self) -> MStatus:
        """Relatively scale this transformation."""
    def scalePivot(self, space: int) -> MPoint:
        """Returns the pivot around which the scale is applied."""
    def scalePivotTranslation(self, space: int) -> MVector:
        """Returns the scale pivot translation in centimeters."""
    def set(self, transform: MTransformationMatrix) -> MStatus:
        """Change this transform to equal the given matrix."""
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setDoNotWrite(self, flag: bool) -> MStatus:
        """Use this method to mark the "do not write" state of this node."""
    @staticmethod
    def setDrawPlaneHandles(drawPlaneHandles: bool) -> None:
        """Sets the global option to display planar handles or not on supported manipulators."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> MStatus:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> MStatus:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> MStatus:
        """Sets the state of the specified flag for the node."""
    @staticmethod
    def setGlobalSize(size: float) -> None:
        """Sets the global manipulator size."""
    @staticmethod
    def setHandleSize(size: float) -> None:
        """Sets the manipulator handle size."""
    def setIcon(self, filename: str) -> MStatus:
        """Associates a custom icon with the node for display in the Maya UI."""
    def setInitialRotation(self, rotation: MEulerRotation) -> MStatus:
        """Sets the initial rotation for the rotate manipulator."""
    def setInstanceable(self, how: bool) -> MStatus:
        """Sets whether or not the DAG node is instanceable."""
    def setIntermediateObject(self, isIntermediate: bool) -> MStatus:
        """Sets whether this object is an intermediate in a geometry calculation."""
    def setLimit(self, type: int, value: float) -> MStatus:
        """Change the limit value for the specified limit type, and automatically enable the limit to be true."""
    @staticmethod
    def setLineSize(size: float) -> None:
        """Sets the manipulator line size."""
    def setLocked(self, locked: bool) -> MStatus:
        """Locks or unlocks this node."""
    def setManipScale(self, size: float) -> MStatus:
        """Sets the manipulator scale."""
    @overload
    def setName(self, name: str, createNamespace: bool = False) -> str: ...
    @overload
    def setName(self, name: str) -> str:
        """Sets the name of this node."""
    @overload
    def setObject(self, path: MDagPath) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches Function Set to the DAG Node that has the given DAG Path."""
    @overload
    def setObjectColor(self, color: int) -> MStatus: ...
    @overload
    def setObjectColor(self, color: MColor) -> MStatus:
        """Sets the index for the current user defined inactive color used by the node."""
    def setObjectColorType(self, type: Any) -> MStatus:
        """Sets whether or not the user defined inactive object color will be used."""
    def setOptimizePlayback(self, optimizePlayback: bool) -> MStatus:
        """Sets whether or not to optimize the playback."""
    def setRestPosition(self, matrix: MTransformationMatrix) -> MStatus:
        """Change the saved rest position of this transform."""
    def setRotateMode(self, mode: Any) -> MStatus:
        """Sets the mode for the rotation manipulator."""
    def setRotateOrientation(self, quat: MQuaternion, space: int, balance: bool) -> MStatus:
        """Set the rotation used to orient the local rotation space."""
    def setRotatePivot(self, point: MPoint, space: int, balance: bool) -> MStatus:
        """Set the rotate pivot in centimeters about which rotation is applied."""
    def setRotatePivotTranslation(self, vec: MVector, space: int) -> MStatus:
        """Set the rotate pivot translation in centimeters."""
    @overload
    def setRotation(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def setRotation(self, rotation: MEulerRotation) -> MStatus: ...
    @overload
    def setRotation(self, order: int) -> MStatus: ...
    @overload
    def setRotation(self, RotationOrder: int, space: int) -> MStatus:
        """Change the rotation component of this transformation using a quaternion."""
    def setRotationCenter(self, rotationCenter: MPoint) -> MStatus:
        """Sets the position of the rotation center for the manipulator."""
    def setRotationOrder(self, order: int, reorder: bool) -> MStatus:
        """Change the rotation order for the transform - the order in which the Euler angles are applied to create the end rotation"""
    def setRotationQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Change the rotation component of this transformation using a quaternion."""
    def setScale(self) -> MStatus:
        """Set the scaling component of this transformation."""
    def setScalePivot(self, point: MPoint, space: int, balance: bool) -> MStatus:
        """Set the pivot around which the scale is applied in centimeters."""
    def setScalePivotTranslation(self, vec: MVector, space: int) -> MStatus:
        """Set the scale pivot translation in centimeters."""
    def setShear(self) -> MStatus:
        """Set the shearing component of this transformation."""
    def setSnapIncrement(self, snapInc: float) -> MStatus:
        """Sets the snap increment."""
    def setSnapMode(self, snapEnabled: bool) -> MStatus:
        """Sets the snap mode."""
    def setTranslation(self, vec: MVector, space: int) -> MStatus:
        """Change the translation component of this transformation."""
    def setUseObjectColor(self, useObjectColor: bool) -> MStatus:
        """Deprecated in 2016.0"""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def setVisible(self, isVisible: bool) -> MStatus:
        """Sets whether or not the manipulator is visible."""
    def shearBy(self) -> MStatus:
        """Relatively shear this transformation."""
    def snapIncrement(self) -> float:
        """Returns the snapping increment in degrees."""
    def transformation(self) -> MTransformationMatrix:
        """Retrieve the transformation matrix represented by this transform."""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
    def translateBy(self, vec: MVector, space: int) -> MStatus:
        """Relatively change the translation component of this transformation."""
    def translation(self, Space: int) -> MVector:
        """Deprecated in 2018.0"""
    def type(self) -> int:
        """Function set type."""
    def typeId(self) -> MTypeId:
        """Returns the type id of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""
    @staticmethod
    def typeString(Type: int) -> str:
        """Introduced in 2020.0"""
    def uniqueName(self) -> str:
        """Introduced in 2023.0"""
    def userNode(self) -> Any:
        """If the function set's node is a plug-in node, then this method will extract the MPxNode pointer from it."""
    def usingHiliteColor(self) -> bool:
        """Determines whether or not the hilite color will be used for the node."""
    def usingObjectColor(self) -> bool:
        """Deprecated in 2016.0"""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnScaleManip:
    kArbitraryOrientation: Any
    kDefaultOrientation: Any
    kExtensionAttr: Any
    kInvalidAttr: Any
    kLocalDynamicAttr: Any
    kNextPos: Any
    kNormalAttr: Any
    kRotateMaxX: Any
    kRotateMaxY: Any
    kRotateMaxZ: Any
    kRotateMinX: Any
    kRotateMinY: Any
    kRotateMinZ: Any
    kScaleMaxX: Any
    kScaleMaxY: Any
    kScaleMaxZ: Any
    kScaleMinX: Any
    kScaleMinY: Any
    kScaleMinZ: Any
    kShearMaxXY: Any
    kShearMaxXZ: Any
    kShearMaxYZ: Any
    kShearMinXY: Any
    kShearMinXZ: Any
    kShearMinYZ: Any
    kTimerInvalidState: Any
    kTimerMetric_callback: Any
    kTimerMetric_callbackNotViaAPI: Any
    kTimerMetric_callbackViaAPI: Any
    kTimerMetric_compute: Any
    kTimerMetric_computeDuringCallback: Any
    kTimerMetric_computeNotDuringCallback: Any
    kTimerMetric_dirty: Any
    kTimerMetric_draw: Any
    kTimerMetric_fetch: Any
    kTimerMetrics: Any
    kTimerOff: Any
    kTimerOn: Any
    kTimerType_count: Any
    kTimerType_inclusive: Any
    kTimerType_self: Any
    kTimerTypes: Any
    kTimerUninitialized: Any
    kTranslateMaxX: Any
    kTranslateMaxY: Any
    kTranslateMaxZ: Any
    kTranslateMinX: Any
    kTranslateMinY: Any
    kTranslateMinZ: Any
    kUseDefaultColor: Any
    kUseIndexColor: Any
    kUseRGBColor: Any
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None: ...
    @overload
    def __init__(self, object: MDagPath) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None:
        """Default constructor."""
    def absoluteName(self) -> str:
        """Returns the absolute name of this node."""
    def activeColor(self) -> MColor:
        """Determines the active color used by this node."""
    @overload
    def addAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def addAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Add a new dynamic attibute to this node."""
    def addChild(self, child: MObject, index: int, keepExistingParents: bool = False) -> MStatus:
        """Makes the given DAG Node a child of the DAG Node to which this instance of the Function Set is attached."""
    def addExternalContentForFileAttr(self, table: MExternalContentInfoTable, attr: MObject) -> MStatus:
        """Adds content info to the specified table from a file path attribute."""
    def affectsAnimation(self) -> bool:
        """Introduced in 2019.0"""
    @staticmethod
    def allocateFlag(pluginName: str) -> int:
        """Allocates a node flag for sole use by the caller."""
    @overload
    def attribute(self, index: int) -> MObject: ...
    @overload
    def attribute(self, attrName: str) -> MObject:
        """Finds the attribute of this node at the given index."""
    def attributeClass(self, attr: MObject) -> Any:
        """Returns the class (normal, dynamic, extension) of the specified attribute."""
    def attributeCount(self) -> int:
        """Returns the number of attributes that this node has."""
    @staticmethod
    def balanceTransformation(identity: int, identity_: int, one: int, kXYZ: int, arg: Any = True) -> None:
        """Balance a transformation when applying a world matrix to a joint."""
    def boundingBox(self) -> Any:
        """Returns the bounding box for the dag node in object space."""
    def canBeWritten(self) -> bool:
        """Returns the do not write state of the node."""
    def child(self, i: int) -> MObject:
        """Queries the DAG Node attached to the Function Set for the child Node corresponding to the given index."""
    def childCount(self) -> int:
        """Determines the number of child Nodes of the Node."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def classification(nodeTypeName: str) -> str:
        """Retrieves the classification string for a node type."""
    def clearRestPosition(self) -> MStatus:
        """Clear the saved rest position of this transform."""
    def connectToScaleCenterPlug(self, scaleCenterPlug: MPlug) -> MStatus:
        """Create a 1-1 association of the scale center on the manipulator and the scaleCenterPlug parameter."""
    def connectToScalePlug(self, scalePlug: MPlug) -> MStatus:
        """Create a 1-1 connection from the scale manipVal to the scalePlug parameter."""
    @overload
    def create(self) -> MObject: ...
    @overload
    def create(self, manipName: str, scaleName: str) -> MObject: ...
    @overload
    def create(self, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, type: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, type: str, name: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str) -> MObject: ...
    @overload
    def create(self, type: str) -> MObject: ...
    @overload
    def create(self, type: str, name: str) -> MObject:
        """Creates a new ScaleManip, and attaches this function set to the new manipulator."""
    def dagPath(self) -> MDagPath:
        """Returns the DagPath to which the Function Set is attached."""
    def dagRoot(self) -> MObject:
        """Determines the root of the first DAG Path to the DAG Node attached to the Function Set."""
    @staticmethod
    def deallocateAllFlags(pluginName: str) -> MStatus:
        """Deallocates all of the node flags which are currently allocated to the specified plugin."""
    @staticmethod
    def deallocateFlag(pluginName: str, flag: int) -> MStatus:
        """Deallocates a node flag which was previously allocated by a call to allocateFlag ."""
    @staticmethod
    def deleteManipulator(manip: MObject) -> MStatus:
        """Delete a manipulator."""
    def dgCallbackIds(self, type: Any, callbackName: str, callbackId: MCallbackIdArray, value: MDoubleArray) -> MStatus:
        """This method provides a further breakdown of the per-callback time returned via dgCallbacks() by returning the data on a """
    def dgCallbacks(self, type: Any, callbackName: Any, value: MDoubleArray) -> MStatus:
        """Node callbacks that occur when timing is enabled get logged with the node and can be queried via this method."""
    def dgTimer(self, timerMetric: Any, timerType: Any) -> float:
        """The function returns the specified timer value for the current node."""
    def dgTimerOff(self) -> MStatus:
        """Indicates that this node should no longer collect DG timing data when DG timing is enabled."""
    def dgTimerOn(self) -> MStatus:
        """Indicates that this node should collect DG timing data whenever DG timing is enabled."""
    def dgTimerQueryState(self) -> Any:
        """The function returns the current on/off state of the node's timer."""
    def dgTimerReset(self) -> MStatus:
        """The function resets the dependency graph timers and counters for this node to zero."""
    def displayWithNode(self, node: MObject) -> MStatus:
        """Configures the manipulator to display with the node, causing the position of the manipulator to follow the position of t"""
    def dormantColor(self) -> MColor:
        """Determines the dormant color used by this node."""
    def drawOverrideColor(self, color: MColor) -> bool:
        """Determines the draw override color used by this node."""
    def drawOverrideEnabled(self) -> bool:
        """Determines whether or not draw override is turned on for this node."""
    def drawOverrideIsReference(self) -> bool:
        """Determines whether or not Display Type of the draw override is Reference for this node."""
    def drawOverrideIsTemplate(self) -> bool:
        """Determines whether or not Display Type of the draw override is Template for this node."""
    @staticmethod
    def drawPlaneHandles() -> bool:
        """This method returns the global option that says if the planar manipulator handles should be drawn or not."""
    def duplicate(self, instance: bool = False, instanceLeaf: bool = False) -> MObject:
        """This method duplicates the DAG hierarchy rooted at the current node."""
    @staticmethod
    def enableDGTiming(enable: bool) -> None:
        """Globally enables or disables the DG node timing mechanism."""
    def enableLimit(self, type: int, flag: bool) -> MStatus:
        """Enable or disable the limit value for the specified limit type."""
    def findAlias(self, alias: str, attrObj: MObject) -> bool:
        """Retrieves the attribute with the given alias."""
    @overload
    def findPlug(self, attr: MObject, wantNetworkedPlug: bool) -> MPlug: ...
    @overload
    def findPlug(self, attrName: str, wantNetworkedPlug: bool) -> MPlug: ...
    @overload
    def findPlug(self, attr: MObject) -> MPlug: ...
    @overload
    def findPlug(self, attrName: str) -> MPlug:
        """Attempt to find a plug for the given attribute."""
    def fullPathName(self) -> str:
        """Return a string representing the full path from the root of the dag to this object."""
    def getAffectedAttributes(self, attr: MObject, affectedAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that are affected by the attribute passed in."""
    def getAffectedByAttributes(self, attr: MObject, affectedByAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that affect the attribute passed in, attr ."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute al"""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns a list of all attribute aliases for this node."""
    def getAllPaths(self, paths: MDagPathArray) -> MStatus:
        """Determines all DAG Paths to the DAG Node attached to the Function Set."""
    def getConnectedSetsAndMembers(self, instanceNumber: int, sets: MObjectArray, comps: MObjectArray, renderableSetsOnly: bool) -> MStatus:
        """Returns all the sets connected to the specified instance of this DAG object."""
    def getConnections(self, array: MPlugArray) -> MStatus:
        """Get all of the current connections to this node as an array of plugs."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> MStatus:
        """Returns the external content (files) that this node depends on."""
    def getOrientation(self) -> MEulerRotation:
        """Returns the orientation used by the manip when its orientationMode is set to kArbitraryOrientation."""
    def getOrientationMode(self) -> Any:
        """Gets the orientation mode of the MFnScaleManip ."""
    def getPath(self, path: MDagPath) -> MStatus:
        """Returns a DAG Path to the DAG Node attached to the Function Set."""
    @overload
    def getRotation(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def getRotation(self, rotation: MEulerRotation) -> MStatus: ...
    @overload
    def getRotation(self, order: int) -> MStatus: ...
    @overload
    def getRotation(self, order: int, space: int) -> MStatus:
        """Retrieve the rotation component of this transformation as a quaternion."""
    def getRotationQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Retrieve the rotation component of this transformation as a quaternion."""
    def getScale(self) -> MStatus:
        """Retrieve the scaling component of this transformation."""
    def getShear(self) -> MStatus:
        """Retrieve the shearing component of this transformation."""
    def getTranslation(self, space: int) -> MVector:
        """Retrieve the translation component of this transformation in centimeters."""
    @staticmethod
    def globalSize() -> float:
        """Returns the global manipulator size."""
    @staticmethod
    def handleSize() -> float:
        """Returns the manipulator handle size."""
    def hasAttribute(self, name: str) -> bool:
        """Returns true if the node already has an attribute with the given name."""
    def hasChild(self, node: MObject) -> bool:
        """Determines whether or not the given Node is a child of the DAG Node attached to the Function Set."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    def hasParent(self, node: MObject) -> bool:
        """Determines whether or not the given Node is a parent of the DAG Node attached to the Function Set."""
    def hasUniqueName(self) -> bool:
        """Indicates whether or not this node's name is unique within the scene."""
    def hiliteColor(self) -> MColor:
        """Determines the current hilite color used by the node."""
    def icon(self) -> str:
        """Returns the custom icon filename associated with the node."""
    def inModel(self) -> bool:
        """Determines whether or not the DAG Node is in the model."""
    def inUnderWorld(self) -> bool:
        """Determines whether or not the DAG Node is an underworld node."""
    def instanceCount(self, total: bool) -> int:
        """Determines the number of times the Node attached to the Function Set is instanced."""
    def isChildOf(self, node: MObject) -> bool:
        """Determines whether or not the DAG Node attached to the Function Set is a child of the given node."""
    def isDefaultNode(self) -> bool:
        """Returns true if the node is a default node."""
    def isFlagSet(self, flag: int) -> bool:
        """Retrieves the current state of the specified flag for a node."""
    def isFromReferencedFile(self) -> bool:
        """Indicates whether or not this node came from a referenced file."""
    def isInstanceable(self) -> bool:
        """Returns true if the DAG node can be instanced, and false otherwise."""
    def isInstanced(self, indirect: bool = True) -> bool:
        """Determines whether the DAG Node attached to the Function Set is directly or indirectly instanced."""
    def isInstancedAttribute(self, attr: MObject) -> bool:
        """Returns true if the specified attribute is instanced."""
    def isIntermediateObject(self) -> bool:
        """Returns true if this object is an intermediate in a geometry calculation."""
    def isLimited(self, type: int) -> bool:
        """Determine if the specified limit attribute is enabled or disabled."""
    def isLocked(self) -> bool:
        """Indicates whether or not this node is locked."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Indicates whether or not the specified attribute was added to this node within the current scene."""
    def isOptimizePlaybackOn(self) -> bool:
        """Returns whether or not optimize playback is on."""
    def isParentOf(self, node: MObject) -> bool:
        """Determines whether or not the DAG Node attached to the Function Set is a parent of the given node."""
    def isShared(self) -> bool:
        """Indicates whether or not this node is shared."""
    def isSnapModeOn(self) -> bool:
        """Returns true when snap mode is on."""
    def isTrackingEdits(self) -> bool:
        """Returns whether or not edits on the given node are being tracked by the generalized edit system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def isVisible(self) -> bool:
        """Returns whether or not the manipulator is visible."""
    def limitValue(self, type: int) -> float:
        """Determine the current value of the specified limit."""
    @staticmethod
    def lineSize() -> float:
        """Returns the manipulator line size."""
    def manipScale(self) -> float:
        """Returns the manipulator scale."""
    def model(self) -> MObject:
        """Deprecated in 2016.0"""
    def name(self) -> str:
        """Returns the name of this node."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def objectColor(self) -> int:
        """Deprecated in 2016.0"""
    def objectColorIndex(self) -> int:
        """Determines the index for the current user defined inactive color used by the node."""
    def objectColorRGB(self) -> MColor:
        """Determines the RGB color for the current user defined inactive color used by the node."""
    def objectColorType(self) -> Any:
        """Determines whether or not the user defined inactive color will be used for the node, or whether the default inactive col"""
    def objectGroupComponent(self, *args: Any, **kwargs: Any) -> Any: ...
    def parent(self, i: int) -> MObject:
        """Queries the DAG Node attached to the Function Set for the parent Node corresponding to the given index."""
    def parentCount(self) -> int:
        """Determines the number of parent Nodes of the Node."""
    def parentNamespace(self) -> str:
        """Returns the name of the namespace in which this node resides."""
    def partialPathName(self) -> str:
        """Return a string representing the partial path from the root of the dag to this object."""
    def pluginName(self) -> str:
        """Returns the name of the plug-in this MFnDependendencyNode was defined in."""
    def plugsAlias(self, plug: MPlug) -> str:
        """Returns the alias for the plug's attribute or the empty string if that attribute has no alias."""
    @overload
    def removeAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def removeAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Remove a dynamic attribute from a node."""
    def removeChild(self, child: MObject) -> MStatus:
        """Removes the given DAG Node from the parent."""
    def removeChildAt(self, index: int) -> MStatus:
        """Removes the child at the given index from the parent."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Some nodes, such as the various animCurve nodes, require that their attributes be set in a specific order for proper ope"""
    def resetFromRestPosition(self) -> MStatus:
        """Reset the transform to its rest position."""
    def resetTransformation(self, m: MMatrix) -> MStatus:
        """Reset this transform to equal the given matrix in world space."""
    def restPosition(self) -> MTransformationMatrix:
        """Retrieve the saved rest position of this transform."""
    @overload
    def rotateBy(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def rotateBy(self, rotation: MEulerRotation, Space: int | None = None) -> MStatus: ...
    @overload
    def rotateBy(self, order: int, Space: int | None = None) -> MStatus:
        """Relatively change the rotation of this transformation using a quaternion."""
    def rotateByQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Relatively change the rotation of this transformation using a quaternion."""
    def rotateOrientation(self, space: int) -> MQuaternion:
        """Returns the rotation used to orient the local rotation space."""
    def rotatePivot(self, space: int) -> MPoint:
        """Returns the pivot about which the rotation is applied."""
    def rotatePivotTranslation(self, space: int) -> MVector:
        """Return the rotate pivot translation in centimeters."""
    def rotateXYZValue(self, valIndex: int) -> MEulerRotation:
        """Gets the rotation for the active manipulator."""
    def rotationOrder(self) -> int:
        """Returns the rotation order for the transform matrix - the order in which the Euler angles are applied to create the end """
    def scaleBy(self) -> MStatus:
        """Relatively scale this transformation."""
    def scaleCenterIndex(self) -> int:
        """Returns the index of the scale center manipVal for this manipulator."""
    def scaleIndex(self) -> int:
        """Returns the index of the scale manipVal for this manipulator."""
    def scalePivot(self, space: int) -> MPoint:
        """Returns the pivot around which the scale is applied."""
    def scalePivotTranslation(self, space: int) -> MVector:
        """Returns the scale pivot translation in centimeters."""
    def set(self, transform: MTransformationMatrix) -> MStatus:
        """Change this transform to equal the given matrix."""
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setDoNotWrite(self, flag: bool) -> MStatus:
        """Use this method to mark the "do not write" state of this node."""
    @staticmethod
    def setDrawPlaneHandles(drawPlaneHandles: bool) -> None:
        """Sets the global option to display planar handles or not on supported manipulators."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> MStatus:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> MStatus:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> MStatus:
        """Sets the state of the specified flag for the node."""
    @staticmethod
    def setGlobalSize(size: float) -> None:
        """Sets the global manipulator size."""
    @staticmethod
    def setHandleSize(size: float) -> None:
        """Sets the manipulator handle size."""
    def setIcon(self, filename: str) -> MStatus:
        """Associates a custom icon with the node for display in the Maya UI."""
    def setInitialScale(self, scale: MVector) -> MStatus:
        """Sets the initial scale for the scale manipulator."""
    def setInstanceable(self, how: bool) -> MStatus:
        """Sets whether or not the DAG node is instanceable."""
    def setIntermediateObject(self, isIntermediate: bool) -> MStatus:
        """Sets whether this object is an intermediate in a geometry calculation."""
    def setLimit(self, type: int, value: float) -> MStatus:
        """Change the limit value for the specified limit type, and automatically enable the limit to be true."""
    @staticmethod
    def setLineSize(size: float) -> None:
        """Sets the manipulator line size."""
    def setLocked(self, locked: bool) -> MStatus:
        """Locks or unlocks this node."""
    def setManipScale(self, size: float) -> MStatus:
        """Sets the manipulator scale."""
    @overload
    def setName(self, name: str, createNamespace: bool = False) -> str: ...
    @overload
    def setName(self, name: str) -> str:
        """Sets the name of this node."""
    @overload
    def setObject(self, path: MDagPath) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches Function Set to the DAG Node that has the given DAG Path."""
    @overload
    def setObjectColor(self, color: int) -> MStatus: ...
    @overload
    def setObjectColor(self, color: MColor) -> MStatus:
        """Sets the index for the current user defined inactive color used by the node."""
    def setObjectColorType(self, type: Any) -> MStatus:
        """Sets whether or not the user defined inactive object color will be used."""
    def setOptimizePlayback(self, optimizePlayback: bool) -> MStatus:
        """Sets whether or not to optimize the playback."""
    def setOrientation(self, direction: MEulerRotation) -> MStatus:
        """Sets the arbitrary orientation of the MFnScaleManip ."""
    def setOrientationMode(self, mode: Any) -> MStatus:
        """Sets the orientation mode of the MFnScaleManip ."""
    def setRestPosition(self, matrix: MTransformationMatrix) -> MStatus:
        """Change the saved rest position of this transform."""
    def setRotateOrientation(self, quat: MQuaternion, space: int, balance: bool) -> MStatus:
        """Set the rotation used to orient the local rotation space."""
    def setRotatePivot(self, point: MPoint, space: int, balance: bool) -> MStatus:
        """Set the rotate pivot in centimeters about which rotation is applied."""
    def setRotatePivotTranslation(self, vec: MVector, space: int) -> MStatus:
        """Set the rotate pivot translation in centimeters."""
    @overload
    def setRotation(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def setRotation(self, rotation: MEulerRotation) -> MStatus: ...
    @overload
    def setRotation(self, order: int) -> MStatus: ...
    @overload
    def setRotation(self, RotationOrder: int, space: int) -> MStatus:
        """Change the rotation component of this transformation using a quaternion."""
    def setRotationOrder(self, order: int, reorder: bool) -> MStatus:
        """Change the rotation order for the transform - the order in which the Euler angles are applied to create the end rotation"""
    def setRotationQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Change the rotation component of this transformation using a quaternion."""
    def setScale(self) -> MStatus:
        """Set the scaling component of this transformation."""
    def setScalePivot(self, point: MPoint, space: int, balance: bool) -> MStatus:
        """Set the pivot around which the scale is applied in centimeters."""
    def setScalePivotTranslation(self, vec: MVector, space: int) -> MStatus:
        """Set the scale pivot translation in centimeters."""
    def setShear(self) -> MStatus:
        """Set the shearing component of this transformation."""
    def setSnapIncrement(self, snapInc: float) -> MStatus:
        """Sets the snap increment."""
    def setSnapMode(self, snapEnabled: bool) -> MStatus:
        """Sets the snap mode."""
    def setTranslation(self, vec: MVector, space: int) -> MStatus:
        """Change the translation component of this transformation."""
    def setUseObjectColor(self, useObjectColor: bool) -> MStatus:
        """Deprecated in 2016.0"""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def setVisible(self, isVisible: bool) -> MStatus:
        """Sets whether or not the manipulator is visible."""
    def shearBy(self) -> MStatus:
        """Relatively shear this transformation."""
    def snapIncrement(self) -> float:
        """Returns the snapping increment in working units."""
    def transformation(self) -> MTransformationMatrix:
        """Retrieve the transformation matrix represented by this transform."""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
    def translateBy(self, vec: MVector, space: int) -> MStatus:
        """Relatively change the translation component of this transformation."""
    def translation(self, Space: int) -> MVector:
        """Deprecated in 2018.0"""
    def type(self) -> int:
        """Function set type."""
    def typeId(self) -> MTypeId:
        """Returns the type id of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""
    @staticmethod
    def typeString(Type: int) -> str:
        """Introduced in 2020.0"""
    def uniqueName(self) -> str:
        """Introduced in 2023.0"""
    def userNode(self) -> Any:
        """If the function set's node is a plug-in node, then this method will extract the MPxNode pointer from it."""
    def usingHiliteColor(self) -> bool:
        """Determines whether or not the hilite color will be used for the node."""
    def usingObjectColor(self) -> bool:
        """Deprecated in 2016.0"""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnStateManip:
    kExtensionAttr: Any
    kInvalidAttr: Any
    kLocalDynamicAttr: Any
    kNextPos: Any
    kNormalAttr: Any
    kRotateMaxX: Any
    kRotateMaxY: Any
    kRotateMaxZ: Any
    kRotateMinX: Any
    kRotateMinY: Any
    kRotateMinZ: Any
    kScaleMaxX: Any
    kScaleMaxY: Any
    kScaleMaxZ: Any
    kScaleMinX: Any
    kScaleMinY: Any
    kScaleMinZ: Any
    kShearMaxXY: Any
    kShearMaxXZ: Any
    kShearMaxYZ: Any
    kShearMinXY: Any
    kShearMinXZ: Any
    kShearMinYZ: Any
    kTimerInvalidState: Any
    kTimerMetric_callback: Any
    kTimerMetric_callbackNotViaAPI: Any
    kTimerMetric_callbackViaAPI: Any
    kTimerMetric_compute: Any
    kTimerMetric_computeDuringCallback: Any
    kTimerMetric_computeNotDuringCallback: Any
    kTimerMetric_dirty: Any
    kTimerMetric_draw: Any
    kTimerMetric_fetch: Any
    kTimerMetrics: Any
    kTimerOff: Any
    kTimerOn: Any
    kTimerType_count: Any
    kTimerType_inclusive: Any
    kTimerType_self: Any
    kTimerTypes: Any
    kTimerUninitialized: Any
    kTranslateMaxX: Any
    kTranslateMaxY: Any
    kTranslateMaxZ: Any
    kTranslateMinX: Any
    kTranslateMinY: Any
    kTranslateMinZ: Any
    kUseDefaultColor: Any
    kUseIndexColor: Any
    kUseRGBColor: Any
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None: ...
    @overload
    def __init__(self, object: MDagPath) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None:
        """Default constructor."""
    def absoluteName(self) -> str:
        """Returns the absolute name of this node."""
    def activeColor(self) -> MColor:
        """Determines the active color used by this node."""
    @overload
    def addAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def addAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Add a new dynamic attibute to this node."""
    def addChild(self, child: MObject, index: int, keepExistingParents: bool = False) -> MStatus:
        """Makes the given DAG Node a child of the DAG Node to which this instance of the Function Set is attached."""
    def addExternalContentForFileAttr(self, table: MExternalContentInfoTable, attr: MObject) -> MStatus:
        """Adds content info to the specified table from a file path attribute."""
    def affectsAnimation(self) -> bool:
        """Introduced in 2019.0"""
    @staticmethod
    def allocateFlag(pluginName: str) -> int:
        """Allocates a node flag for sole use by the caller."""
    @overload
    def attribute(self, index: int) -> MObject: ...
    @overload
    def attribute(self, attrName: str) -> MObject:
        """Finds the attribute of this node at the given index."""
    def attributeClass(self, attr: MObject) -> Any:
        """Returns the class (normal, dynamic, extension) of the specified attribute."""
    def attributeCount(self) -> int:
        """Returns the number of attributes that this node has."""
    @staticmethod
    def balanceTransformation(identity: int, identity_: int, one: int, kXYZ: int, arg: Any = True) -> None:
        """Balance a transformation when applying a world matrix to a joint."""
    def boundingBox(self) -> Any:
        """Returns the bounding box for the dag node in object space."""
    def canBeWritten(self) -> bool:
        """Returns the do not write state of the node."""
    def child(self, i: int) -> MObject:
        """Queries the DAG Node attached to the Function Set for the child Node corresponding to the given index."""
    def childCount(self) -> int:
        """Determines the number of child Nodes of the Node."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def classification(nodeTypeName: str) -> str:
        """Retrieves the classification string for a node type."""
    def clearRestPosition(self) -> MStatus:
        """Clear the saved rest position of this transform."""
    def connectToStatePlug(self, statePlug: MPlug) -> MStatus:
        """Connect to the state plug."""
    @overload
    def create(self) -> MObject: ...
    @overload
    def create(self, manipName: str, stateName: str) -> MObject: ...
    @overload
    def create(self, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, type: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, type: str, name: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str) -> MObject: ...
    @overload
    def create(self, type: str) -> MObject: ...
    @overload
    def create(self, type: str, name: str) -> MObject:
        """Creates a new StateManip."""
    def dagPath(self) -> MDagPath:
        """Returns the DagPath to which the Function Set is attached."""
    def dagRoot(self) -> MObject:
        """Determines the root of the first DAG Path to the DAG Node attached to the Function Set."""
    @staticmethod
    def deallocateAllFlags(pluginName: str) -> MStatus:
        """Deallocates all of the node flags which are currently allocated to the specified plugin."""
    @staticmethod
    def deallocateFlag(pluginName: str, flag: int) -> MStatus:
        """Deallocates a node flag which was previously allocated by a call to allocateFlag ."""
    @staticmethod
    def deleteManipulator(manip: MObject) -> MStatus:
        """Delete a manipulator."""
    def dgCallbackIds(self, type: Any, callbackName: str, callbackId: MCallbackIdArray, value: MDoubleArray) -> MStatus:
        """This method provides a further breakdown of the per-callback time returned via dgCallbacks() by returning the data on a """
    def dgCallbacks(self, type: Any, callbackName: Any, value: MDoubleArray) -> MStatus:
        """Node callbacks that occur when timing is enabled get logged with the node and can be queried via this method."""
    def dgTimer(self, timerMetric: Any, timerType: Any) -> float:
        """The function returns the specified timer value for the current node."""
    def dgTimerOff(self) -> MStatus:
        """Indicates that this node should no longer collect DG timing data when DG timing is enabled."""
    def dgTimerOn(self) -> MStatus:
        """Indicates that this node should collect DG timing data whenever DG timing is enabled."""
    def dgTimerQueryState(self) -> Any:
        """The function returns the current on/off state of the node's timer."""
    def dgTimerReset(self) -> MStatus:
        """The function resets the dependency graph timers and counters for this node to zero."""
    def dormantColor(self) -> MColor:
        """Determines the dormant color used by this node."""
    def drawOverrideColor(self, color: MColor) -> bool:
        """Determines the draw override color used by this node."""
    def drawOverrideEnabled(self) -> bool:
        """Determines whether or not draw override is turned on for this node."""
    def drawOverrideIsReference(self) -> bool:
        """Determines whether or not Display Type of the draw override is Reference for this node."""
    def drawOverrideIsTemplate(self) -> bool:
        """Determines whether or not Display Type of the draw override is Template for this node."""
    @staticmethod
    def drawPlaneHandles() -> bool:
        """This method returns the global option that says if the planar manipulator handles should be drawn or not."""
    def duplicate(self, instance: bool = False, instanceLeaf: bool = False) -> MObject:
        """This method duplicates the DAG hierarchy rooted at the current node."""
    @staticmethod
    def enableDGTiming(enable: bool) -> None:
        """Globally enables or disables the DG node timing mechanism."""
    def enableLimit(self, type: int, flag: bool) -> MStatus:
        """Enable or disable the limit value for the specified limit type."""
    def findAlias(self, alias: str, attrObj: MObject) -> bool:
        """Retrieves the attribute with the given alias."""
    @overload
    def findPlug(self, attr: MObject, wantNetworkedPlug: bool) -> MPlug: ...
    @overload
    def findPlug(self, attrName: str, wantNetworkedPlug: bool) -> MPlug: ...
    @overload
    def findPlug(self, attr: MObject) -> MPlug: ...
    @overload
    def findPlug(self, attrName: str) -> MPlug:
        """Attempt to find a plug for the given attribute."""
    def fullPathName(self) -> str:
        """Return a string representing the full path from the root of the dag to this object."""
    def getAffectedAttributes(self, attr: MObject, affectedAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that are affected by the attribute passed in."""
    def getAffectedByAttributes(self, attr: MObject, affectedByAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that affect the attribute passed in, attr ."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute al"""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns a list of all attribute aliases for this node."""
    def getAllPaths(self, paths: MDagPathArray) -> MStatus:
        """Determines all DAG Paths to the DAG Node attached to the Function Set."""
    def getConnectedSetsAndMembers(self, instanceNumber: int, sets: MObjectArray, comps: MObjectArray, renderableSetsOnly: bool) -> MStatus:
        """Returns all the sets connected to the specified instance of this DAG object."""
    def getConnections(self, array: MPlugArray) -> MStatus:
        """Get all of the current connections to this node as an array of plugs."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> MStatus:
        """Returns the external content (files) that this node depends on."""
    def getPath(self, path: MDagPath) -> MStatus:
        """Returns a DAG Path to the DAG Node attached to the Function Set."""
    @overload
    def getRotation(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def getRotation(self, rotation: MEulerRotation) -> MStatus: ...
    @overload
    def getRotation(self, order: int) -> MStatus: ...
    @overload
    def getRotation(self, order: int, space: int) -> MStatus:
        """Retrieve the rotation component of this transformation as a quaternion."""
    def getRotationQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Retrieve the rotation component of this transformation as a quaternion."""
    def getScale(self) -> MStatus:
        """Retrieve the scaling component of this transformation."""
    def getShear(self) -> MStatus:
        """Retrieve the shearing component of this transformation."""
    def getTranslation(self, space: int) -> MVector:
        """Retrieve the translation component of this transformation in centimeters."""
    @staticmethod
    def globalSize() -> float:
        """Returns the global manipulator size."""
    @staticmethod
    def handleSize() -> float:
        """Returns the manipulator handle size."""
    def hasAttribute(self, name: str) -> bool:
        """Returns true if the node already has an attribute with the given name."""
    def hasChild(self, node: MObject) -> bool:
        """Determines whether or not the given Node is a child of the DAG Node attached to the Function Set."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    def hasParent(self, node: MObject) -> bool:
        """Determines whether or not the given Node is a parent of the DAG Node attached to the Function Set."""
    def hasUniqueName(self) -> bool:
        """Indicates whether or not this node's name is unique within the scene."""
    def hiliteColor(self) -> MColor:
        """Determines the current hilite color used by the node."""
    def icon(self) -> str:
        """Returns the custom icon filename associated with the node."""
    def inModel(self) -> bool:
        """Determines whether or not the DAG Node is in the model."""
    def inUnderWorld(self) -> bool:
        """Determines whether or not the DAG Node is an underworld node."""
    def instanceCount(self, total: bool) -> int:
        """Determines the number of times the Node attached to the Function Set is instanced."""
    def isChildOf(self, node: MObject) -> bool:
        """Determines whether or not the DAG Node attached to the Function Set is a child of the given node."""
    def isDefaultNode(self) -> bool:
        """Returns true if the node is a default node."""
    def isFlagSet(self, flag: int) -> bool:
        """Retrieves the current state of the specified flag for a node."""
    def isFromReferencedFile(self) -> bool:
        """Indicates whether or not this node came from a referenced file."""
    def isInstanceable(self) -> bool:
        """Returns true if the DAG node can be instanced, and false otherwise."""
    def isInstanced(self, indirect: bool = True) -> bool:
        """Determines whether the DAG Node attached to the Function Set is directly or indirectly instanced."""
    def isInstancedAttribute(self, attr: MObject) -> bool:
        """Returns true if the specified attribute is instanced."""
    def isIntermediateObject(self) -> bool:
        """Returns true if this object is an intermediate in a geometry calculation."""
    def isLimited(self, type: int) -> bool:
        """Determine if the specified limit attribute is enabled or disabled."""
    def isLocked(self) -> bool:
        """Indicates whether or not this node is locked."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Indicates whether or not the specified attribute was added to this node within the current scene."""
    def isOptimizePlaybackOn(self) -> bool:
        """Returns whether or not optimize playback is on."""
    def isParentOf(self, node: MObject) -> bool:
        """Determines whether or not the DAG Node attached to the Function Set is a parent of the given node."""
    def isShared(self) -> bool:
        """Indicates whether or not this node is shared."""
    def isTrackingEdits(self) -> bool:
        """Returns whether or not edits on the given node are being tracked by the generalized edit system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def isVisible(self) -> bool:
        """Returns whether or not the manipulator is visible."""
    def limitValue(self, type: int) -> float:
        """Determine the current value of the specified limit."""
    @staticmethod
    def lineSize() -> float:
        """Returns the manipulator line size."""
    def manipScale(self) -> float:
        """Returns the manipulator scale."""
    def maxStates(self) -> int:
        """Returns the number of maximum states."""
    def model(self) -> MObject:
        """Deprecated in 2016.0"""
    def name(self) -> str:
        """Returns the name of this node."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def objectColor(self) -> int:
        """Deprecated in 2016.0"""
    def objectColorIndex(self) -> int:
        """Determines the index for the current user defined inactive color used by the node."""
    def objectColorRGB(self) -> MColor:
        """Determines the RGB color for the current user defined inactive color used by the node."""
    def objectColorType(self) -> Any:
        """Determines whether or not the user defined inactive color will be used for the node, or whether the default inactive col"""
    def objectGroupComponent(self, *args: Any, **kwargs: Any) -> Any: ...
    def parent(self, i: int) -> MObject:
        """Queries the DAG Node attached to the Function Set for the parent Node corresponding to the given index."""
    def parentCount(self) -> int:
        """Determines the number of parent Nodes of the Node."""
    def parentNamespace(self) -> str:
        """Returns the name of the namespace in which this node resides."""
    def partialPathName(self) -> str:
        """Return a string representing the partial path from the root of the dag to this object."""
    def pluginName(self) -> str:
        """Returns the name of the plug-in this MFnDependendencyNode was defined in."""
    def plugsAlias(self, plug: MPlug) -> str:
        """Returns the alias for the plug's attribute or the empty string if that attribute has no alias."""
    def positionIndex(self) -> int:
        """Returns the index of the position of the StateManip."""
    @overload
    def removeAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def removeAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Remove a dynamic attribute from a node."""
    def removeChild(self, child: MObject) -> MStatus:
        """Removes the given DAG Node from the parent."""
    def removeChildAt(self, index: int) -> MStatus:
        """Removes the child at the given index from the parent."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Some nodes, such as the various animCurve nodes, require that their attributes be set in a specific order for proper ope"""
    def resetFromRestPosition(self) -> MStatus:
        """Reset the transform to its rest position."""
    def resetTransformation(self, m: MMatrix) -> MStatus:
        """Reset this transform to equal the given matrix in world space."""
    def restPosition(self) -> MTransformationMatrix:
        """Retrieve the saved rest position of this transform."""
    @overload
    def rotateBy(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def rotateBy(self, rotation: MEulerRotation, Space: int | None = None) -> MStatus: ...
    @overload
    def rotateBy(self, order: int, Space: int | None = None) -> MStatus:
        """Relatively change the rotation of this transformation using a quaternion."""
    def rotateByQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Relatively change the rotation of this transformation using a quaternion."""
    def rotateOrientation(self, space: int) -> MQuaternion:
        """Returns the rotation used to orient the local rotation space."""
    def rotatePivot(self, space: int) -> MPoint:
        """Returns the pivot about which the rotation is applied."""
    def rotatePivotTranslation(self, space: int) -> MVector:
        """Return the rotate pivot translation in centimeters."""
    def rotateXYZValue(self, valIndex: int) -> MEulerRotation:
        """Gets the rotation for the active manipulator."""
    def rotationOrder(self) -> int:
        """Returns the rotation order for the transform matrix - the order in which the Euler angles are applied to create the end """
    def scaleBy(self) -> MStatus:
        """Relatively scale this transformation."""
    def scalePivot(self, space: int) -> MPoint:
        """Returns the pivot around which the scale is applied."""
    def scalePivotTranslation(self, space: int) -> MVector:
        """Returns the scale pivot translation in centimeters."""
    def set(self, transform: MTransformationMatrix) -> MStatus:
        """Change this transform to equal the given matrix."""
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setDoNotWrite(self, flag: bool) -> MStatus:
        """Use this method to mark the "do not write" state of this node."""
    @staticmethod
    def setDrawPlaneHandles(drawPlaneHandles: bool) -> None:
        """Sets the global option to display planar handles or not on supported manipulators."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> MStatus:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> MStatus:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> MStatus:
        """Sets the state of the specified flag for the node."""
    @staticmethod
    def setGlobalSize(size: float) -> None:
        """Sets the global manipulator size."""
    @staticmethod
    def setHandleSize(size: float) -> None:
        """Sets the manipulator handle size."""
    def setIcon(self, filename: str) -> MStatus:
        """Associates a custom icon with the node for display in the Maya UI."""
    def setInitialState(self, initialState: int) -> MStatus:
        """Sets the initial state of the StateManip."""
    def setInstanceable(self, how: bool) -> MStatus:
        """Sets whether or not the DAG node is instanceable."""
    def setIntermediateObject(self, isIntermediate: bool) -> MStatus:
        """Sets whether this object is an intermediate in a geometry calculation."""
    def setLimit(self, type: int, value: float) -> MStatus:
        """Change the limit value for the specified limit type, and automatically enable the limit to be true."""
    @staticmethod
    def setLineSize(size: float) -> None:
        """Sets the manipulator line size."""
    def setLocked(self, locked: bool) -> MStatus:
        """Locks or unlocks this node."""
    def setManipScale(self, size: float) -> MStatus:
        """Sets the manipulator scale."""
    def setMaxStates(self, numStates: int) -> MStatus:
        """Sets the maximum number of states that the StateManip will have."""
    @overload
    def setName(self, name: str, createNamespace: bool = False) -> str: ...
    @overload
    def setName(self, name: str) -> str:
        """Sets the name of this node."""
    @overload
    def setObject(self, path: MDagPath) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches Function Set to the DAG Node that has the given DAG Path."""
    @overload
    def setObjectColor(self, color: int) -> MStatus: ...
    @overload
    def setObjectColor(self, color: MColor) -> MStatus:
        """Sets the index for the current user defined inactive color used by the node."""
    def setObjectColorType(self, type: Any) -> MStatus:
        """Sets whether or not the user defined inactive object color will be used."""
    def setOptimizePlayback(self, optimizePlayback: bool) -> MStatus:
        """Sets whether or not to optimize the playback."""
    def setRestPosition(self, matrix: MTransformationMatrix) -> MStatus:
        """Change the saved rest position of this transform."""
    def setRotateOrientation(self, quat: MQuaternion, space: int, balance: bool) -> MStatus:
        """Set the rotation used to orient the local rotation space."""
    def setRotatePivot(self, point: MPoint, space: int, balance: bool) -> MStatus:
        """Set the rotate pivot in centimeters about which rotation is applied."""
    def setRotatePivotTranslation(self, vec: MVector, space: int) -> MStatus:
        """Set the rotate pivot translation in centimeters."""
    @overload
    def setRotation(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def setRotation(self, rotation: MEulerRotation) -> MStatus: ...
    @overload
    def setRotation(self, order: int) -> MStatus: ...
    @overload
    def setRotation(self, RotationOrder: int, space: int) -> MStatus:
        """Change the rotation component of this transformation using a quaternion."""
    def setRotationOrder(self, order: int, reorder: bool) -> MStatus:
        """Change the rotation order for the transform - the order in which the Euler angles are applied to create the end rotation"""
    def setRotationQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Change the rotation component of this transformation using a quaternion."""
    def setScale(self) -> MStatus:
        """Set the scaling component of this transformation."""
    def setScalePivot(self, point: MPoint, space: int, balance: bool) -> MStatus:
        """Set the pivot around which the scale is applied in centimeters."""
    def setScalePivotTranslation(self, vec: MVector, space: int) -> MStatus:
        """Set the scale pivot translation in centimeters."""
    def setShear(self) -> MStatus:
        """Set the shearing component of this transformation."""
    def setTranslation(self, vec: MVector, space: int) -> MStatus:
        """Change the translation component of this transformation."""
    def setUseObjectColor(self, useObjectColor: bool) -> MStatus:
        """Deprecated in 2016.0"""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def setVisible(self, isVisible: bool) -> MStatus:
        """Sets whether or not the manipulator is visible."""
    def shearBy(self) -> MStatus:
        """Relatively shear this transformation."""
    def state(self) -> int:
        """Returns the current state."""
    def stateIndex(self) -> int:
        """Returns the index of the state."""
    def transformation(self) -> MTransformationMatrix:
        """Retrieve the transformation matrix represented by this transform."""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
    def translateBy(self, vec: MVector, space: int) -> MStatus:
        """Relatively change the translation component of this transformation."""
    def translation(self, Space: int) -> MVector:
        """Deprecated in 2018.0"""
    def type(self) -> int:
        """Function set type."""
    def typeId(self) -> MTypeId:
        """Returns the type id of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""
    @staticmethod
    def typeString(Type: int) -> str:
        """Introduced in 2020.0"""
    def uniqueName(self) -> str:
        """Introduced in 2023.0"""
    def userNode(self) -> Any:
        """If the function set's node is a plug-in node, then this method will extract the MPxNode pointer from it."""
    def usingHiliteColor(self) -> bool:
        """Determines whether or not the hilite color will be used for the node."""
    def usingObjectColor(self) -> bool:
        """Deprecated in 2016.0"""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnToggleManip:
    kExtensionAttr: Any
    kInvalidAttr: Any
    kLocalDynamicAttr: Any
    kNextPos: Any
    kNormalAttr: Any
    kRotateMaxX: Any
    kRotateMaxY: Any
    kRotateMaxZ: Any
    kRotateMinX: Any
    kRotateMinY: Any
    kRotateMinZ: Any
    kScaleMaxX: Any
    kScaleMaxY: Any
    kScaleMaxZ: Any
    kScaleMinX: Any
    kScaleMinY: Any
    kScaleMinZ: Any
    kShearMaxXY: Any
    kShearMaxXZ: Any
    kShearMaxYZ: Any
    kShearMinXY: Any
    kShearMinXZ: Any
    kShearMinYZ: Any
    kTimerInvalidState: Any
    kTimerMetric_callback: Any
    kTimerMetric_callbackNotViaAPI: Any
    kTimerMetric_callbackViaAPI: Any
    kTimerMetric_compute: Any
    kTimerMetric_computeDuringCallback: Any
    kTimerMetric_computeNotDuringCallback: Any
    kTimerMetric_dirty: Any
    kTimerMetric_draw: Any
    kTimerMetric_fetch: Any
    kTimerMetrics: Any
    kTimerOff: Any
    kTimerOn: Any
    kTimerType_count: Any
    kTimerType_inclusive: Any
    kTimerType_self: Any
    kTimerTypes: Any
    kTimerUninitialized: Any
    kTranslateMaxX: Any
    kTranslateMaxY: Any
    kTranslateMaxZ: Any
    kTranslateMinX: Any
    kTranslateMinY: Any
    kTranslateMinZ: Any
    kUseDefaultColor: Any
    kUseIndexColor: Any
    kUseRGBColor: Any
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None: ...
    @overload
    def __init__(self, object: MDagPath) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None:
        """Default constructor."""
    def absoluteName(self) -> str:
        """Returns the absolute name of this node."""
    def activeColor(self) -> MColor:
        """Determines the active color used by this node."""
    @overload
    def addAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def addAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Add a new dynamic attibute to this node."""
    def addChild(self, child: MObject, index: int, keepExistingParents: bool = False) -> MStatus:
        """Makes the given DAG Node a child of the DAG Node to which this instance of the Function Set is attached."""
    def addExternalContentForFileAttr(self, table: MExternalContentInfoTable, attr: MObject) -> MStatus:
        """Adds content info to the specified table from a file path attribute."""
    def affectsAnimation(self) -> bool:
        """Introduced in 2019.0"""
    @staticmethod
    def allocateFlag(pluginName: str) -> int:
        """Allocates a node flag for sole use by the caller."""
    @overload
    def attribute(self, index: int) -> MObject: ...
    @overload
    def attribute(self, attrName: str) -> MObject:
        """Finds the attribute of this node at the given index."""
    def attributeClass(self, attr: MObject) -> Any:
        """Returns the class (normal, dynamic, extension) of the specified attribute."""
    def attributeCount(self) -> int:
        """Returns the number of attributes that this node has."""
    @staticmethod
    def balanceTransformation(identity: int, identity_: int, one: int, kXYZ: int, arg: Any = True) -> None:
        """Balance a transformation when applying a world matrix to a joint."""
    def boundingBox(self) -> Any:
        """Returns the bounding box for the dag node in object space."""
    def canBeWritten(self) -> bool:
        """Returns the do not write state of the node."""
    def child(self, i: int) -> MObject:
        """Queries the DAG Node attached to the Function Set for the child Node corresponding to the given index."""
    def childCount(self) -> int:
        """Determines the number of child Nodes of the Node."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def classification(nodeTypeName: str) -> str:
        """Retrieves the classification string for a node type."""
    def clearRestPosition(self) -> MStatus:
        """Clear the saved rest position of this transform."""
    def connectToTogglePlug(self, togglePlug: MPlug) -> MStatus:
        """Connect to the toggle plug."""
    @overload
    def create(self) -> MObject: ...
    @overload
    def create(self, manipName: str, toggleName: str) -> MObject: ...
    @overload
    def create(self, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, type: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, type: str, name: str, parent: MObject | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str) -> MObject: ...
    @overload
    def create(self, type: str) -> MObject: ...
    @overload
    def create(self, type: str, name: str) -> MObject:
        """Creates a new ToggleManip."""
    def dagPath(self) -> MDagPath:
        """Returns the DagPath to which the Function Set is attached."""
    def dagRoot(self) -> MObject:
        """Determines the root of the first DAG Path to the DAG Node attached to the Function Set."""
    @staticmethod
    def deallocateAllFlags(pluginName: str) -> MStatus:
        """Deallocates all of the node flags which are currently allocated to the specified plugin."""
    @staticmethod
    def deallocateFlag(pluginName: str, flag: int) -> MStatus:
        """Deallocates a node flag which was previously allocated by a call to allocateFlag ."""
    @staticmethod
    def deleteManipulator(manip: MObject) -> MStatus:
        """Delete a manipulator."""
    def dgCallbackIds(self, type: Any, callbackName: str, callbackId: MCallbackIdArray, value: MDoubleArray) -> MStatus:
        """This method provides a further breakdown of the per-callback time returned via dgCallbacks() by returning the data on a """
    def dgCallbacks(self, type: Any, callbackName: Any, value: MDoubleArray) -> MStatus:
        """Node callbacks that occur when timing is enabled get logged with the node and can be queried via this method."""
    def dgTimer(self, timerMetric: Any, timerType: Any) -> float:
        """The function returns the specified timer value for the current node."""
    def dgTimerOff(self) -> MStatus:
        """Indicates that this node should no longer collect DG timing data when DG timing is enabled."""
    def dgTimerOn(self) -> MStatus:
        """Indicates that this node should collect DG timing data whenever DG timing is enabled."""
    def dgTimerQueryState(self) -> Any:
        """The function returns the current on/off state of the node's timer."""
    def dgTimerReset(self) -> MStatus:
        """The function resets the dependency graph timers and counters for this node to zero."""
    def direction(self) -> MVector:
        """Returns the direction."""
    def directionIndex(self) -> int:
        """Returns the index of the direction."""
    def dormantColor(self) -> MColor:
        """Determines the dormant color used by this node."""
    def drawOverrideColor(self, color: MColor) -> bool:
        """Determines the draw override color used by this node."""
    def drawOverrideEnabled(self) -> bool:
        """Determines whether or not draw override is turned on for this node."""
    def drawOverrideIsReference(self) -> bool:
        """Determines whether or not Display Type of the draw override is Reference for this node."""
    def drawOverrideIsTemplate(self) -> bool:
        """Determines whether or not Display Type of the draw override is Template for this node."""
    @staticmethod
    def drawPlaneHandles() -> bool:
        """This method returns the global option that says if the planar manipulator handles should be drawn or not."""
    def duplicate(self, instance: bool = False, instanceLeaf: bool = False) -> MObject:
        """This method duplicates the DAG hierarchy rooted at the current node."""
    @staticmethod
    def enableDGTiming(enable: bool) -> None:
        """Globally enables or disables the DG node timing mechanism."""
    def enableLimit(self, type: int, flag: bool) -> MStatus:
        """Enable or disable the limit value for the specified limit type."""
    def findAlias(self, alias: str, attrObj: MObject) -> bool:
        """Retrieves the attribute with the given alias."""
    @overload
    def findPlug(self, attr: MObject, wantNetworkedPlug: bool) -> MPlug: ...
    @overload
    def findPlug(self, attrName: str, wantNetworkedPlug: bool) -> MPlug: ...
    @overload
    def findPlug(self, attr: MObject) -> MPlug: ...
    @overload
    def findPlug(self, attrName: str) -> MPlug:
        """Attempt to find a plug for the given attribute."""
    def fullPathName(self) -> str:
        """Return a string representing the full path from the root of the dag to this object."""
    def getAffectedAttributes(self, attr: MObject, affectedAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that are affected by the attribute passed in."""
    def getAffectedByAttributes(self, attr: MObject, affectedByAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that affect the attribute passed in, attr ."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute al"""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns a list of all attribute aliases for this node."""
    def getAllPaths(self, paths: MDagPathArray) -> MStatus:
        """Determines all DAG Paths to the DAG Node attached to the Function Set."""
    def getConnectedSetsAndMembers(self, instanceNumber: int, sets: MObjectArray, comps: MObjectArray, renderableSetsOnly: bool) -> MStatus:
        """Returns all the sets connected to the specified instance of this DAG object."""
    def getConnections(self, array: MPlugArray) -> MStatus:
        """Get all of the current connections to this node as an array of plugs."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> MStatus:
        """Returns the external content (files) that this node depends on."""
    def getPath(self, path: MDagPath) -> MStatus:
        """Returns a DAG Path to the DAG Node attached to the Function Set."""
    @overload
    def getRotation(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def getRotation(self, rotation: MEulerRotation) -> MStatus: ...
    @overload
    def getRotation(self, order: int) -> MStatus: ...
    @overload
    def getRotation(self, order: int, space: int) -> MStatus:
        """Retrieve the rotation component of this transformation as a quaternion."""
    def getRotationQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Retrieve the rotation component of this transformation as a quaternion."""
    def getScale(self) -> MStatus:
        """Retrieve the scaling component of this transformation."""
    def getShear(self) -> MStatus:
        """Retrieve the shearing component of this transformation."""
    def getTranslation(self, space: int) -> MVector:
        """Retrieve the translation component of this transformation in centimeters."""
    @staticmethod
    def globalSize() -> float:
        """Returns the global manipulator size."""
    @staticmethod
    def handleSize() -> float:
        """Returns the manipulator handle size."""
    def hasAttribute(self, name: str) -> bool:
        """Returns true if the node already has an attribute with the given name."""
    def hasChild(self, node: MObject) -> bool:
        """Determines whether or not the given Node is a child of the DAG Node attached to the Function Set."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    def hasParent(self, node: MObject) -> bool:
        """Determines whether or not the given Node is a parent of the DAG Node attached to the Function Set."""
    def hasUniqueName(self) -> bool:
        """Indicates whether or not this node's name is unique within the scene."""
    def hiliteColor(self) -> MColor:
        """Determines the current hilite color used by the node."""
    def icon(self) -> str:
        """Returns the custom icon filename associated with the node."""
    def inModel(self) -> bool:
        """Determines whether or not the DAG Node is in the model."""
    def inUnderWorld(self) -> bool:
        """Determines whether or not the DAG Node is an underworld node."""
    def instanceCount(self, total: bool) -> int:
        """Determines the number of times the Node attached to the Function Set is instanced."""
    def isChildOf(self, node: MObject) -> bool:
        """Determines whether or not the DAG Node attached to the Function Set is a child of the given node."""
    def isDefaultNode(self) -> bool:
        """Returns true if the node is a default node."""
    def isFlagSet(self, flag: int) -> bool:
        """Retrieves the current state of the specified flag for a node."""
    def isFromReferencedFile(self) -> bool:
        """Indicates whether or not this node came from a referenced file."""
    def isInstanceable(self) -> bool:
        """Returns true if the DAG node can be instanced, and false otherwise."""
    def isInstanced(self, indirect: bool = True) -> bool:
        """Determines whether the DAG Node attached to the Function Set is directly or indirectly instanced."""
    def isInstancedAttribute(self, attr: MObject) -> bool:
        """Returns true if the specified attribute is instanced."""
    def isIntermediateObject(self) -> bool:
        """Returns true if this object is an intermediate in a geometry calculation."""
    def isLimited(self, type: int) -> bool:
        """Determine if the specified limit attribute is enabled or disabled."""
    def isLocked(self) -> bool:
        """Indicates whether or not this node is locked."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Indicates whether or not the specified attribute was added to this node within the current scene."""
    def isOptimizePlaybackOn(self) -> bool:
        """Returns whether or not optimize playback is on."""
    def isParentOf(self, node: MObject) -> bool:
        """Determines whether or not the DAG Node attached to the Function Set is a parent of the given node."""
    def isShared(self) -> bool:
        """Indicates whether or not this node is shared."""
    def isTrackingEdits(self) -> bool:
        """Returns whether or not edits on the given node are being tracked by the generalized edit system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def isVisible(self) -> bool:
        """Returns whether or not the manipulator is visible."""
    def length(self) -> float:
        """Returns the length."""
    def lengthIndex(self) -> int:
        """Returns the index of the length of the ToggleManip."""
    def limitValue(self, type: int) -> float:
        """Determine the current value of the specified limit."""
    @staticmethod
    def lineSize() -> float:
        """Returns the manipulator line size."""
    def manipScale(self) -> float:
        """Returns the manipulator scale."""
    def model(self) -> MObject:
        """Deprecated in 2016.0"""
    def name(self) -> str:
        """Returns the name of this node."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def objectColor(self) -> int:
        """Deprecated in 2016.0"""
    def objectColorIndex(self) -> int:
        """Determines the index for the current user defined inactive color used by the node."""
    def objectColorRGB(self) -> MColor:
        """Determines the RGB color for the current user defined inactive color used by the node."""
    def objectColorType(self) -> Any:
        """Determines whether or not the user defined inactive color will be used for the node, or whether the default inactive col"""
    def objectGroupComponent(self, *args: Any, **kwargs: Any) -> Any: ...
    def parent(self, i: int) -> MObject:
        """Queries the DAG Node attached to the Function Set for the parent Node corresponding to the given index."""
    def parentCount(self) -> int:
        """Determines the number of parent Nodes of the Node."""
    def parentNamespace(self) -> str:
        """Returns the name of the namespace in which this node resides."""
    def partialPathName(self) -> str:
        """Return a string representing the partial path from the root of the dag to this object."""
    def pluginName(self) -> str:
        """Returns the name of the plug-in this MFnDependendencyNode was defined in."""
    def plugsAlias(self, plug: MPlug) -> str:
        """Returns the alias for the plug's attribute or the empty string if that attribute has no alias."""
    @overload
    def removeAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def removeAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Remove a dynamic attribute from a node."""
    def removeChild(self, child: MObject) -> MStatus:
        """Removes the given DAG Node from the parent."""
    def removeChildAt(self, index: int) -> MStatus:
        """Removes the child at the given index from the parent."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Some nodes, such as the various animCurve nodes, require that their attributes be set in a specific order for proper ope"""
    def resetFromRestPosition(self) -> MStatus:
        """Reset the transform to its rest position."""
    def resetTransformation(self, m: MMatrix) -> MStatus:
        """Reset this transform to equal the given matrix in world space."""
    def restPosition(self) -> MTransformationMatrix:
        """Retrieve the saved rest position of this transform."""
    @overload
    def rotateBy(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def rotateBy(self, rotation: MEulerRotation, Space: int | None = None) -> MStatus: ...
    @overload
    def rotateBy(self, order: int, Space: int | None = None) -> MStatus:
        """Relatively change the rotation of this transformation using a quaternion."""
    def rotateByQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Relatively change the rotation of this transformation using a quaternion."""
    def rotateOrientation(self, space: int) -> MQuaternion:
        """Returns the rotation used to orient the local rotation space."""
    def rotatePivot(self, space: int) -> MPoint:
        """Returns the pivot about which the rotation is applied."""
    def rotatePivotTranslation(self, space: int) -> MVector:
        """Return the rotate pivot translation in centimeters."""
    def rotateXYZValue(self, valIndex: int) -> MEulerRotation:
        """Gets the rotation for the active manipulator."""
    def rotationOrder(self) -> int:
        """Returns the rotation order for the transform matrix - the order in which the Euler angles are applied to create the end """
    def scaleBy(self) -> MStatus:
        """Relatively scale this transformation."""
    def scalePivot(self, space: int) -> MPoint:
        """Returns the pivot around which the scale is applied."""
    def scalePivotTranslation(self, space: int) -> MVector:
        """Returns the scale pivot translation in centimeters."""
    def set(self, transform: MTransformationMatrix) -> MStatus:
        """Change this transform to equal the given matrix."""
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setDirection(self, direction: MVector) -> MStatus:
        """Sets the direction of the ToggleManip."""
    def setDoNotWrite(self, flag: bool) -> MStatus:
        """Use this method to mark the "do not write" state of this node."""
    @staticmethod
    def setDrawPlaneHandles(drawPlaneHandles: bool) -> None:
        """Sets the global option to display planar handles or not on supported manipulators."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> MStatus:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> MStatus:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> MStatus:
        """Sets the state of the specified flag for the node."""
    @staticmethod
    def setGlobalSize(size: float) -> None:
        """Sets the global manipulator size."""
    @staticmethod
    def setHandleSize(size: float) -> None:
        """Sets the manipulator handle size."""
    def setIcon(self, filename: str) -> MStatus:
        """Associates a custom icon with the node for display in the Maya UI."""
    def setInstanceable(self, how: bool) -> MStatus:
        """Sets whether or not the DAG node is instanceable."""
    def setIntermediateObject(self, isIntermediate: bool) -> MStatus:
        """Sets whether this object is an intermediate in a geometry calculation."""
    def setLength(self, length: float) -> MStatus:
        """Sets the length of the ToggleManip."""
    def setLimit(self, type: int, value: float) -> MStatus:
        """Change the limit value for the specified limit type, and automatically enable the limit to be true."""
    @staticmethod
    def setLineSize(size: float) -> None:
        """Sets the manipulator line size."""
    def setLocked(self, locked: bool) -> MStatus:
        """Locks or unlocks this node."""
    def setManipScale(self, size: float) -> MStatus:
        """Sets the manipulator scale."""
    @overload
    def setName(self, name: str, createNamespace: bool = False) -> str: ...
    @overload
    def setName(self, name: str) -> str:
        """Sets the name of this node."""
    @overload
    def setObject(self, path: MDagPath) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches Function Set to the DAG Node that has the given DAG Path."""
    @overload
    def setObjectColor(self, color: int) -> MStatus: ...
    @overload
    def setObjectColor(self, color: MColor) -> MStatus:
        """Sets the index for the current user defined inactive color used by the node."""
    def setObjectColorType(self, type: Any) -> MStatus:
        """Sets whether or not the user defined inactive object color will be used."""
    def setOptimizePlayback(self, optimizePlayback: bool) -> MStatus:
        """Sets whether or not to optimize the playback."""
    def setRestPosition(self, matrix: MTransformationMatrix) -> MStatus:
        """Change the saved rest position of this transform."""
    def setRotateOrientation(self, quat: MQuaternion, space: int, balance: bool) -> MStatus:
        """Set the rotation used to orient the local rotation space."""
    def setRotatePivot(self, point: MPoint, space: int, balance: bool) -> MStatus:
        """Set the rotate pivot in centimeters about which rotation is applied."""
    def setRotatePivotTranslation(self, vec: MVector, space: int) -> MStatus:
        """Set the rotate pivot translation in centimeters."""
    @overload
    def setRotation(self, quaternion: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def setRotation(self, rotation: MEulerRotation) -> MStatus: ...
    @overload
    def setRotation(self, order: int) -> MStatus: ...
    @overload
    def setRotation(self, RotationOrder: int, space: int) -> MStatus:
        """Change the rotation component of this transformation using a quaternion."""
    def setRotationOrder(self, order: int, reorder: bool) -> MStatus:
        """Change the rotation order for the transform - the order in which the Euler angles are applied to create the end rotation"""
    def setRotationQuaternion(self, x: float, y: float, z: float, w: float, Space: int | None = None) -> MStatus:
        """Change the rotation component of this transformation using a quaternion."""
    def setScale(self) -> MStatus:
        """Set the scaling component of this transformation."""
    def setScalePivot(self, point: MPoint, space: int, balance: bool) -> MStatus:
        """Set the pivot around which the scale is applied in centimeters."""
    def setScalePivotTranslation(self, vec: MVector, space: int) -> MStatus:
        """Set the scale pivot translation in centimeters."""
    def setShear(self) -> MStatus:
        """Set the shearing component of this transformation."""
    def setStartPoint(self, startPoint: MPoint) -> MStatus:
        """Sets the start point of the ToggleManip."""
    def setToggle(self, toggle: bool) -> MStatus:
        """Sets the toggle of the ToggleManip."""
    def setTranslation(self, vec: MVector, space: int) -> MStatus:
        """Change the translation component of this transformation."""
    def setUseObjectColor(self, useObjectColor: bool) -> MStatus:
        """Deprecated in 2016.0"""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def setVisible(self, isVisible: bool) -> MStatus:
        """Sets whether or not the manipulator is visible."""
    def shearBy(self) -> MStatus:
        """Relatively shear this transformation."""
    def startPoint(self) -> MPoint:
        """Returns the start point."""
    def startPointIndex(self) -> int:
        """Returns the index of the start point of the ToggleManip."""
    def toggle(self) -> bool:
        """Returns the toggle."""
    def toggleIndex(self) -> int:
        """Returns the index of the toggle of the ToggleManip."""
    def transformation(self) -> MTransformationMatrix:
        """Retrieve the transformation matrix represented by this transform."""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
    def translateBy(self, vec: MVector, space: int) -> MStatus:
        """Relatively change the translation component of this transformation."""
    def translation(self, Space: int) -> MVector:
        """Deprecated in 2018.0"""
    def type(self) -> int:
        """Function set type."""
    def typeId(self) -> MTypeId:
        """Returns the type id of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""
    @staticmethod
    def typeString(Type: int) -> str:
        """Introduced in 2020.0"""
    def uniqueName(self) -> str:
        """Introduced in 2023.0"""
    def userNode(self) -> Any:
        """If the function set's node is a plug-in node, then this method will extract the MPxNode pointer from it."""
    def usingHiliteColor(self) -> bool:
        """Determines whether or not the hilite color will be used for the node."""
    def usingObjectColor(self) -> bool:
        """Deprecated in 2016.0"""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnToolContext:
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None:
        """Default constructor."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def name(self) -> str:
        """Returns the tool context's name."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches the Function Set to the specified Maya Object."""
    def title(self) -> str:
        """Returns the tool context's title."""
    def type(self) -> int:
        """Function set type."""
    @staticmethod
    def typeString(Type: int) -> str:
        """Introduced in 2020.0"""

class MGraphEditorInfo:
    kAnimCurveAllKnown: Any
    kAnimCurveHighlighted: Any
    kAnimCurveOutlinerOnly: Any
    kAnimCurveSelected: Any
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, graphEditorName: str) -> None:
        """Constructor."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def getAnimCurveNodes(self, animCurveNodeArray: MObjectArray, arg: Any) -> MStatus:
        """Returns an array of animCurve nodes, based on the attached Graph Editor's state information, which captures:"""
    @overload
    def getViewportBounds(self, left: float, right: float, bottom: float, top: float) -> MStatus: ...
    @overload
    def getViewportBounds(self, boundsArray: MDoubleArray) -> MStatus:
        """Return the viewport bounds."""
    def getViewportSize(self, width: int, height: int) -> MStatus:
        """Return the viewport size."""
    def isNormalizedViewportMode(self) -> bool:
        """Returns whether or not the Graph Editor is in Normalized view mode."""
    def isStackedViewportMode(self) -> bool:
        """Returns whether or not the Graph Editor is in Stacked view mode."""
    def name(self) -> str:
        """Return the name of the currently attached panel."""
    def reset(self) -> None:
        """Resets all stored state information to be empty, thereby detaching from the currently attached Graph Editor (if any)"""
    @overload
    def setViewportBounds(self, left: float, right: float, bottom: float, top: float) -> MStatus: ...
    @overload
    def setViewportBounds(self, boundsArray: MDoubleArray) -> MStatus:
        """Set the viewport bounds."""
    def supportsUIDrawing(self) -> bool:
        """Returns whether the attached panel control supports drawing primitives in screen space."""

class MHWShaderSwatchGenerator:
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def cancelCurrentSwatchRender(self, *args: Any, **kwargs: Any) -> Any: ...
    def cancelParallelRendering(self, *args: Any, **kwargs: Any) -> Any: ...
    def createObj(self, *args: Any, **kwargs: Any) -> Any: ...
    def doIteration(self, *args: Any, **kwargs: Any) -> Any: ...
    def enableSwatchRender(self, *args: Any, **kwargs: Any) -> Any: ...
    def getSwatchBackgroundColor(self, *args: Any, **kwargs: Any) -> Any: ...
    def image(self, *args: Any, **kwargs: Any) -> Any: ...
    def initialize(self, *args: Any, **kwargs: Any) -> Any: ...
    def node(self, *args: Any, **kwargs: Any) -> Any: ...
    def renderParallel(self, *args: Any, **kwargs: Any) -> Any: ...
    def renderQuality(self, *args: Any, **kwargs: Any) -> Any: ...
    def resolution(self, *args: Any, **kwargs: Any) -> Any: ...
    def setRenderQuality(self, *args: Any, **kwargs: Any) -> Any: ...
    def swatchNode(self, *args: Any, **kwargs: Any) -> Any: ...

class MManipData:
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg: Any) -> None: ...
    @overload
    def __init__(self, arg: Any) -> None: ...
    @overload
    def __init__(self, arg: Any) -> None: ...
    @overload
    def __init__(self, arg: int) -> None: ...
    @overload
    def __init__(self, arg: Any) -> None: ...
    @overload
    def __init__(self, arg: Any) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self) -> None:
        """The default class constructor."""
    def asBool(self) -> bool:
        """Returns the manipulator data as a bool."""
    def asDouble(self) -> float:
        """Returns the manipulator data as a double."""
    def asFloat(self) -> float:
        """Returns the manipulator data as a float."""
    def asLong(self) -> int:
        """Returns the manipulator data as a int."""
    def asMObject(self) -> MObject:
        """Returns the manipulator data as an MObject ."""
    def asShort(self) -> Any:
        """Returns the manipulator data as a short."""
    def asUnsigned(self) -> int:
        """Returns the manipulator data as an unsigned int."""
    def assign(self, other: MManipData) -> None: ...
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def isSimple(self) -> bool:
        """Returns whether or not the manipulator data is simple or complex."""

class MMaterial:
    kAmbientColor: Any
    kBumpMap: Any
    kColor: Any
    kCosinePower: Any
    kDiffuse: Any
    kEccentricity: Any
    kHighlightSize: Any
    kIncandescence: Any
    kReflectedColor: Any
    kReflectivity: Any
    kRoughness: Any
    kSpecularColor: Any
    kSpecularRollOff: Any
    kTransluscence: Any
    kTransparency: Any
    kWhiteness: Any
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, in_: MMaterial) -> None: ...
    @overload
    def __init__(self) -> None:
        """Constructor."""
    def applyTexture(self) -> None:
        """For materials that have texture, this method must be used before the OpenGL drawing to apply the texture to the current """
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def defaultMaterial() -> MMaterial:
        """Get the default material."""
    def evaluateDiffuse(self) -> MStatus:
        """Perform necessary evaluation to be able to get diffuse back."""
    def evaluateEmission(self) -> MStatus:
        """Perform necessary evaluation to be able to get emission back."""
    def evaluateMaterial(self) -> MStatus:
        """Evaluate a material."""
    def evaluateShininess(self) -> MStatus:
        """Perform necessary evaluation to be able to get shininess back."""
    def evaluateSpecular(self) -> MStatus:
        """Perform necessary evaluation to be able to get specular back."""
    def evaluateTexture(self, data: MDrawData) -> MStatus:
        """Evaluate texturing related information."""
    def evaluateTextureTransformation(self) -> MStatus:
        """Deprecated in 2019.0"""
    def getDiffuse(self) -> MStatus:
        """Get the GL diffuse color."""
    def getEmission(self) -> MStatus:
        """Get the GL emission color."""
    def getHasTransparency(self) -> MStatus:
        """Determine if material or texture has transparency."""
    def getHwShaderNode(self) -> Any:
        """Get the hardware shader node."""
    def getShininess(self) -> MStatus:
        """Get the GL shininess."""
    def getSpecular(self) -> MStatus:
        """Get the GL specular color."""
    @overload
    def getTextureTransformation(self, data: MDrawData, texXform: MMatrix) -> MStatus: ...
    @overload
    def getTextureTransformation(self, data: MDrawData, rotateUV: float, scaleU: float, scaleV: float, translateU: float, translateV: float, rotateFrame: float) -> MStatus: ...
    @overload
    def getTextureTransformation(self, scaleU: float, scaleV: float, translateU: float, translateV: float, rotate: float) -> MStatus:
        """Get the current textures transformation."""
    def materialIsTextured(self) -> bool:
        """Do we have a texture (evaluated or not)."""
    def setMaterial(self, hasTransparency: bool) -> MStatus:
        """Set the current GL material."""
    def shadingEngine(self) -> MObject:
        """Get the shading engined associated with this material."""
    def textureImage(self, image: MImage, color: MColor, chan: Any, mapped: bool, dagPath: MDagPath, xRes: int = -1, yRes: int = -1) -> MStatus:
        """For materials that have texture, this method will attempt to retrieve the pixel map for a given mapped channel of that m"""

class MMaterialArray:
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: MMaterialArray) -> None: ...
    @overload
    def __init__(self) -> None:
        """Default constructor."""
    def append(self, element: MMaterial) -> MStatus:
        """Adds a new element to the end of the array."""
    def assign(self, other: MMaterialArray) -> None: ...
    @staticmethod
    def className() -> str:
        """NO SCRIPT SUPPORT."""
    def clear(self) -> MStatus:
        """Clear the contents of the array."""
    def copy(self, source: MMaterialArray) -> MStatus:
        """Copy the contents of the source array to this array."""
    def insert(self, element: MMaterial, index: int) -> MStatus:
        """Inserts a new value into the array at the given index."""
    def length(self) -> int:
        """Returns the number of elements in the instance."""
    def remove(self, index: int) -> MStatus:
        """Remove the array element at the given index."""
    def set(self, element: MMaterial, index: int) -> MStatus:
        """Sets the value of the indicated element to the indicated MMaterial value."""
    def setLength(self, length: int) -> MStatus:
        """Set the length of the array."""
    def setSizeIncrement(self, newIncrement: int) -> None:
        """Set the size by which the array will be expanded whenever expansion is necessary."""
    def sizeIncrement(self) -> int:
        """Return the size by which the array will be expanded whenever expansion is necessary."""

class MObjectListFilter:
    kAddRemoveObjects: Any
    kExclusionList: Any
    kInclusionList: Any
    kNone: Any
    kNumberOfFilterTypes: Any
    thisown: Any
    def UIname(self) -> str:
        """Query the UI name."""
    def __init__(self, name: str) -> None:
        """Constructor for a filter."""
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def dependentOnSceneUpdates(self) -> Any:
        """Return whether the update of the filter list is dependent on scene updates."""
    @staticmethod
    def deregisterFilter(filter: MObjectListFilter) -> MStatus:
        """Deregister the object filter from the list of available filters."""
    def filterType(self) -> Any:
        """Query the filter type."""
    def getList(self, list: MSelectionList) -> MStatus:
        """This method will return the selection list to use for filtering scene rendering."""
    def name(self) -> str:
        """Query the name identifier."""
    @staticmethod
    def registerFilter(filter: MObjectListFilter) -> MStatus:
        """Register the object filter as one of an available set of filters."""
    def requireListUpdate(self) -> bool:
        """This method is called by Maya to determine whether the contents of the object list for the filter has changed since the """
    def setFilterType(self, filterType: Any) -> None:
        """Set the filter type."""
    def setUIName(self, name: str) -> None:
        """Set the UI name."""

class MPaintMessage:
    kDefaultAction: Any
    kDoAction: Any
    kDoNotDoAction: Any
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @staticmethod
    def addVertexColorCallback(func: Any, clientData: None = None) -> Any:
        """Adds a new callback on vertex color paint."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def currentCallbackId() -> Any:
        """Return the callback ID of the currently executing callback."""
    @staticmethod
    def getCallableInfo() -> Any:
        """Introduced in 2020.0"""
    @overload
    @staticmethod
    def nodeCallbacks(node: MObject, ids: MCallbackIdArray) -> MStatus: ...
    @overload
    @staticmethod
    def nodeCallbacks(node: MObject, ids: MIntArray) -> MStatus:
        """Returns a list of callback IDs associated registered to a given node."""
    @staticmethod
    def registeringCallableScript() -> bool:
        """Return true if this MMessage object has its callbacks defined in script."""
    @staticmethod
    def removeCallback(id: Any) -> MStatus:
        """Remove the specified callback from maya."""
    @overload
    @staticmethod
    def removeCallbacks(ids: MCallbackIdArray) -> MStatus: ...
    @overload
    @staticmethod
    def removeCallbacks(ids: MIntArray) -> MStatus:
        """Remove all of the specified callbacks from maya."""
    @staticmethod
    def setCallableInfo(info: Any) -> None:
        """Introduced in 2020.0"""
    @staticmethod
    def setRegisteringCallableScript() -> None:
        """Mark this MMessage object as one that will be passed callbacks defined in script."""
    @staticmethod
    def stealCallableInfo() -> Any:
        """Introduced in 2020.0"""
    @staticmethod
    def stopRegisteringCallableScript() -> None:
        """Introduced in 2019.0"""

class MPanelCanvasInfo:
    thisown: Any
    def __init__(self, editorName: str) -> None:
        """The constructor."""
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @overload
    def getViewportBounds(self, left: float, right: float, bottom: float, top: float) -> MStatus: ...
    @overload
    def getViewportBounds(self, boundsArray: MDoubleArray) -> MStatus:
        """Return the viewport bounds."""
    def getViewportSize(self, width: int, height: int) -> MStatus:
        """Return the viewport size."""
    def name(self) -> str:
        """Return the name of the currently attached panel."""
    def reset(self) -> None:
        """Resets all stored state information to be empty, thereby detaching from the currently attached Graph Editor (if any)"""
    @overload
    def setViewportBounds(self, left: float, right: float, bottom: float, top: float) -> MStatus: ...
    @overload
    def setViewportBounds(self, boundsArray: MDoubleArray) -> MStatus:
        """Set the viewport bounds."""
    def supportsUIDrawing(self) -> bool:
        """Returns whether the attached panel control supports drawing primitives in screen space."""

class MProgressWindow:
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @staticmethod
    def advanceProgress(amount: int) -> MStatus:
        """Increases the progress value by amount."""
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def endProgress() -> MStatus:
        """Destroys the progress window and removes it from the screen."""
    @staticmethod
    def isCancelled() -> bool:
        """Determine whether the user has tried to cancel an interruptable progress window."""
    @staticmethod
    def isInterruptable() -> bool:
        """Determine whether the progress window is interruptable."""
    @staticmethod
    def progress() -> int:
        """Get the progress value."""
    @staticmethod
    def progressMax() -> int:
        """Get the maximum progress value."""
    @staticmethod
    def progressMin() -> int:
        """Get the minimum progress value."""
    @staticmethod
    def progressStatus() -> str:
        """Get the progress status string."""
    @staticmethod
    def reserve() -> bool:
        """Reserves a progress window for use through this class."""
    @staticmethod
    def setInterruptable(value: bool) -> MStatus:
        """Sets whether the progress window is interruptable."""
    @staticmethod
    def setProgress(progress: int) -> MStatus:
        """Sets the progress value."""
    @staticmethod
    def setProgressMax(maxValue: int) -> MStatus:
        """Sets the maximum value for the progress."""
    @staticmethod
    def setProgressMin(minValue: int) -> MStatus:
        """Sets the minimum value for the progress."""
    @staticmethod
    def setProgressRange(minValue: int, maxValue: int) -> MStatus:
        """Sets the range (minValue, maxValue) of the progress indicator."""
    @staticmethod
    def setProgressStatus(progressStatus: str) -> MStatus:
        """Sets the progress status string."""
    @staticmethod
    def setTitle(title: str) -> MStatus:
        """Sets the title of the progress window."""
    @staticmethod
    def startProgress() -> MStatus:
        """Displays the progress window on the screen."""
    @staticmethod
    def title() -> str:
        """Get the window title."""

class MQtUtil:
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @staticmethod
    def addWidgetToMayaLayout(control: Any, layout: Any, uiType: str) -> str:
        """Adds a QWidget to an existing Maya layout, such as that returned by getCurrentParent() or getLayout()."""
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def createCursor(cursorName: str, autoScale: bool = True) -> Any:
        """Looks for a cursor first in the Qt resources, and then in a file on disk."""
    @staticmethod
    def createIcon(iconName: str, autoScale: bool = True) -> Any:
        """Looks for a icon first in the Qt resources, and then in a file on disk."""
    @staticmethod
    def createPixmap(imageName: str, autoScale: bool = True) -> Any:
        """Looks for a pixmap first in the Qt resources, and then in a file on disk."""
    @staticmethod
    def deregisterUIType(className: str) -> bool:
        """De-registers a widget class (UI-type) which has been previously registered with registerUIType() ."""
    @overload
    @staticmethod
    def dpiScale(size: int) -> int: ...
    @overload
    @staticmethod
    def dpiScale(size: float) -> float:
        """Get the scaled size for Maya interface scaling."""
    @staticmethod
    def findControl(controlName: str, ancestor: Any = None) -> Any:
        """Returns the QWidget for the named Maya control."""
    @staticmethod
    def findLayout(layoutName: str, ancestor: Any = None) -> Any:
        """Returns the QWidget for the named Maya layout."""
    @staticmethod
    def findMenuItem(itemName: str) -> Any:
        """Returns the QAction for the named Maya menuItem."""
    @staticmethod
    def findWindow(windowName: str) -> Any:
        """Returns the QWidget for the named Maya window."""
    @staticmethod
    def fullName(uiElement: Any) -> str:
        """Returns the full, hierarchical name of a UI element."""
    @staticmethod
    def getCurrentParent() -> Any:
        """Returns the placeholder widget for the current layout if there is one."""
    @staticmethod
    def getLayoutChildren(layout: Any) -> Any:
        """Returns a list of all the Maya UI elements parented directly beneath the specified Maya layout."""
    @staticmethod
    def getParent(uiElement: Any) -> Any:
        """Returns a pointer to a UI element's parent element within Maya's UI hierarchy."""
    @staticmethod
    def mainWindow() -> Any:
        """Returns Maya's main window."""
    @staticmethod
    def nativeWindow(control: Any) -> Any:
        """/*! Returns a platform-specific native window handle for the specified control."""
    @overload
    @staticmethod
    def newClocaleValidator(bottom: float, top: float, decimals: int, parent: Any = None) -> Any: ...
    @overload
    @staticmethod
    def newClocaleValidator(parent: Any = None) -> Any:
        """Introduced in 2022.0"""
    @staticmethod
    def registerUIType(className: str, UITypeCreatorFn: Any, command: str) -> bool:
        """Registers a class name (UI-type) with a function to create the QWidget of that type, and a command to edit it with."""
    @staticmethod
    def resourceGLContext() -> Any:
        """Returns Maya internal QGLContext that the plug-in may use to create resource-sharing OpenGL context."""
    @staticmethod
    def toMString(qstr: Any) -> str:
        """Convenience utility to convert a QString to an MString ."""
    @staticmethod
    def toQString(mstr: str) -> Any:
        """Convenience utility to convert an MString to a QString."""

class MSelectInfo:
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def addSelection(self, *args: Any, **kwargs: Any) -> Any: ...
    def canDrawComponent(self, *args: Any, **kwargs: Any) -> Any: ...
    def className(self, *args: Any, **kwargs: Any) -> Any: ...
    def completelyInside(self, *args: Any, **kwargs: Any) -> Any: ...
    def displayStatus(self, *args: Any, **kwargs: Any) -> Any: ...
    def displayStyle(self, *args: Any, **kwargs: Any) -> Any: ...
    def getAlignmentMatrix(self, *args: Any, **kwargs: Any) -> Any: ...
    def getLocalRay(self, *args: Any, **kwargs: Any) -> Any: ...
    def getPrototype(self, *args: Any, **kwargs: Any) -> Any: ...
    def highestPriority(self, *args: Any, **kwargs: Any) -> Any: ...
    def inSelect(self, *args: Any, **kwargs: Any) -> Any: ...
    def inUserInteraction(self, *args: Any, **kwargs: Any) -> Any: ...
    def inclusiveMatrix(self, *args: Any, **kwargs: Any) -> Any: ...
    def isRay(self, *args: Any, **kwargs: Any) -> Any: ...
    def multiPath(self, *args: Any, **kwargs: Any) -> Any: ...
    def objectDisplayStatus(self, *args: Any, **kwargs: Any) -> Any: ...
    def pluginObjectDisplayStatus(self, *args: Any, **kwargs: Any) -> Any: ...
    def projectionMatrix(self, *args: Any, **kwargs: Any) -> Any: ...
    def selectClosest(self, *args: Any, **kwargs: Any) -> Any: ...
    def selectForHilite(self, *args: Any, **kwargs: Any) -> Any: ...
    def selectOnHilitedOnly(self, *args: Any, **kwargs: Any) -> Any: ...
    def selectPath(self, *args: Any, **kwargs: Any) -> Any: ...
    def selectRect(self, *args: Any, **kwargs: Any) -> Any: ...
    def selectable(self, *args: Any, **kwargs: Any) -> Any: ...
    def selectableComponent(self, *args: Any, **kwargs: Any) -> Any: ...
    def setHighestPriority(self, *args: Any, **kwargs: Any) -> Any: ...
    def setMultiPath(self, *args: Any, **kwargs: Any) -> Any: ...
    def setSnapPoint(self, *args: Any, **kwargs: Any) -> Any: ...
    def singleSelection(self, *args: Any, **kwargs: Any) -> Any: ...
    def userChangingViewContext(self, *args: Any, **kwargs: Any) -> Any: ...
    def view(self, *args: Any, **kwargs: Any) -> Any: ...

class MTextureEditorDrawInfo:
    kDrawEdgeForSelect: Any
    kDrawEverything: Any
    kDrawFacetForSelect: Any
    kDrawFunctionFirst: Any
    kDrawFunctionLast: Any
    kDrawUVForSelect: Any
    kDrawVertexForSelect: Any
    kDrawWireframe: Any
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, in_: MTextureEditorDrawInfo) -> None:
        """Constructor."""
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def drawingFunction(self) -> Any:
        """Indicates the current drawing state for a drawUV method call."""
    def setDrawingFunction(self, func: Any) -> None:
        """Sets the current drawing state."""

class MToolsInfo:
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def isDirty() -> bool:
        """This method returns whether or not the dirty flag is set."""
    @staticmethod
    def resetDirtyFlag() -> None:
        """This method resets the dirty flag, such that the state becomes clean."""
    @staticmethod
    def setDirtyFlag(context: MPxContext) -> None:
        """This method should be called by a tool when the value of a tool property sheet option has changed."""

class MUiMessage:
    kDefaultAction: Any
    kDoAction: Any
    kDoNotDoAction: Any
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @staticmethod
    def add3dViewDestroyMsgCallback(panelName: str, func: int, clientData: None = None) -> Any:
        """This method registers a callback for when a particular 3d view gets destroyed."""
    @staticmethod
    def add3dViewPostMultipleDrawPassMsgCallback(panelName: str, func: int, clientData: None = None) -> Any:
        """This method registers a callback for when a particular 3d view's specified pass is finshed when multiple drawing is enab"""
    @staticmethod
    def add3dViewPostRenderMsgCallback(panelName: str, func: int, clientData: None = None) -> Any:
        """This method registers a callback for when the 3d view is about to display it's rendered contents to the viewport."""
    @staticmethod
    def add3dViewPreMultipleDrawPassMsgCallback(panelName: str, func: int, clientData: None = None) -> Any:
        """This method registers a callback for when a particular 3d view's specific pass is about to be drawn when multiple drawin"""
    @staticmethod
    def add3dViewPreRenderMsgCallback(panelName: str, func: int, clientData: None = None) -> Any:
        """This method registers a callback for when a particular 3d view is about to render it's contents."""
    @staticmethod
    def add3dViewRenderOverrideChangedCallback(panelName: str, func: int, clientData: None = None) -> Any:
        """This method registers a callback for when the render override for a particular 3d view changes."""
    @staticmethod
    def add3dViewRendererChangedCallback(panelName: str, func: int, clientData: None = None) -> Any:
        """This method registers a callback for when the renderer for a particular 3d view changes."""
    @staticmethod
    def addCameraChangedCallback(panelName: str, func: int, clientData: None = None) -> Any:
        """This method registers a callback for cameras being changed in 3d views."""
    @staticmethod
    def addUiDeletedCallback(uiName: str, func: int, clientData: None = None) -> Any:
        """This method registers a callback for UI deleted messages."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def currentCallbackId() -> Any:
        """Return the callback ID of the currently executing callback."""
    @staticmethod
    def getCallableInfo() -> Any:
        """Introduced in 2020.0"""
    @overload
    @staticmethod
    def nodeCallbacks(node: MObject, ids: MCallbackIdArray) -> MStatus: ...
    @overload
    @staticmethod
    def nodeCallbacks(node: MObject, ids: MIntArray) -> MStatus:
        """Returns a list of callback IDs associated registered to a given node."""
    @staticmethod
    def registeringCallableScript() -> bool:
        """Return true if this MMessage object has its callbacks defined in script."""
    @staticmethod
    def removeCallback(id: Any) -> MStatus:
        """Remove the specified callback from maya."""
    @overload
    @staticmethod
    def removeCallbacks(ids: MCallbackIdArray) -> MStatus: ...
    @overload
    @staticmethod
    def removeCallbacks(ids: MIntArray) -> MStatus:
        """Remove all of the specified callbacks from maya."""
    @staticmethod
    def setCallableInfo(info: Any) -> None:
        """Introduced in 2020.0"""
    @staticmethod
    def setRegisteringCallableScript() -> None:
        """Mark this MMessage object as one that will be passed callbacks defined in script."""
    @staticmethod
    def stealCallableInfo() -> Any:
        """Introduced in 2020.0"""
    @staticmethod
    def stopRegisteringCallableScript() -> None:
        """Introduced in 2019.0"""

class boolPtr:
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def assign(self, other: boolPtr) -> None: ...
    def cast(self, *args: Any, **kwargs: Any) -> Any: ...
    def frompointer(self, *args: Any, **kwargs: Any) -> Any: ...
    def value(self, *args: Any, **kwargs: Any) -> Any: ...

class charPtr:
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def assign(self, other: charPtr) -> None: ...
    def cast(self, *args: Any, **kwargs: Any) -> Any: ...
    def frompointer(self, *args: Any, **kwargs: Any) -> Any: ...
    def value(self, *args: Any, **kwargs: Any) -> Any: ...

class doublePtr:
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def assign(self, other: doublePtr) -> None: ...
    def cast(self, *args: Any, **kwargs: Any) -> Any: ...
    def frompointer(self, *args: Any, **kwargs: Any) -> Any: ...
    def value(self, *args: Any, **kwargs: Any) -> Any: ...

class floatPtr:
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def assign(self, other: floatPtr) -> None: ...
    def cast(self, *args: Any, **kwargs: Any) -> Any: ...
    def frompointer(self, *args: Any, **kwargs: Any) -> Any: ...
    def value(self, *args: Any, **kwargs: Any) -> Any: ...

class intPtr:
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def assign(self, other: intPtr) -> None: ...
    def cast(self, *args: Any, **kwargs: Any) -> Any: ...
    def frompointer(self, *args: Any, **kwargs: Any) -> Any: ...
    def value(self, *args: Any, **kwargs: Any) -> Any: ...

class shortPtr:
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def assign(self, other: shortPtr) -> None: ...
    def cast(self, *args: Any, **kwargs: Any) -> Any: ...
    def frompointer(self, *args: Any, **kwargs: Any) -> Any: ...
    def value(self, *args: Any, **kwargs: Any) -> Any: ...

class uCharPtr:
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def assign(self, other: uCharPtr) -> None: ...
    def cast(self, *args: Any, **kwargs: Any) -> Any: ...
    def frompointer(self, *args: Any, **kwargs: Any) -> Any: ...
    def value(self, *args: Any, **kwargs: Any) -> Any: ...

class uIntPtr:
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def assign(self, other: uIntPtr) -> None: ...
    def cast(self, *args: Any, **kwargs: Any) -> Any: ...
    def frompointer(self, *args: Any, **kwargs: Any) -> Any: ...
    def value(self, *args: Any, **kwargs: Any) -> Any: ...
