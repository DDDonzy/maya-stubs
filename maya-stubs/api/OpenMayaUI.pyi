# Stub for maya.api.OpenMayaUI - generated from Maya 2024 Python API reference

from typing import Any

from maya.api.OpenMaya import MAngle
from maya.api.OpenMaya import MArgList
from maya.api.OpenMaya import MArgParser
from maya.api.OpenMaya import MBoundingBox
from maya.api.OpenMaya import MColor
from maya.api.OpenMaya import MDGContext
from maya.api.OpenMaya import MDagPath
from maya.api.OpenMaya import MDagPathArray
from maya.api.OpenMaya import MDataBlock
from maya.api.OpenMaya import MDoubleArray
from maya.api.OpenMaya import MEulerRotation
from maya.api.OpenMaya import MEvaluationNode
from maya.api.OpenMaya import MExternalContentInfoTable
from maya.api.OpenMaya import MExternalContentLocationTable
from maya.api.OpenMaya import MImage
from maya.api.OpenMaya import MIntArray
from maya.api.OpenMaya import MMatrix
from maya.api.OpenMaya import MObject
from maya.api.OpenMaya import MObjectArray
from maya.api.OpenMaya import MPlug
from maya.api.OpenMaya import MPlugArray
from maya.api.OpenMaya import MPoint
from maya.api.OpenMaya import MPxNode
from maya.api.OpenMaya import MPxSurfaceShape
from maya.api.OpenMaya import MQuaternion
from maya.api.OpenMayaRender import MRenderProfile
from maya.api.OpenMaya import MSelectionList
from maya.api.OpenMaya import MSelectionMask
from maya.api.OpenMayaRender import MSwatchRenderBase
from maya.api.OpenMaya import MSyntax
from maya.api.OpenMaya import MTimeRange
from maya.api.OpenMaya import MTransformationMatrix
from maya.api.OpenMaya import MTypeId
from maya.api.OpenMayaRender import MUniformParameterList
from maya.api.OpenMaya import MUuid
from maya.api.OpenMayaRender import MVaryingParameterList
from maya.api.OpenMaya import MVector

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
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def active3dView() -> M3dView:
        """Returns the active view in the form of a class (M3dView) that can operate on it."""
    @staticmethod
    def activeAffectedColor() -> MColor:
        """Returns the color for active affected objects."""
    @staticmethod
    def activeTemplateColor() -> MColor:
        """Returns the color for active template objects."""
    @staticmethod
    def applicationShell() -> int:
        """Returns a long containing a C++ 'void' pointer which points to the native handle for Maya's main window."""
    @staticmethod
    def backgroundColor() -> MColor:
        """Returns the value of the background color."""
    @staticmethod
    def backgroundColorBottom() -> MColor:
        """Returns the value of the background gradient bottom color."""
    @staticmethod
    def backgroundColorTop() -> MColor:
        """Returns the value of the background gradient top color."""
    def beginGL(self) -> None:
        """(Deprecated: Please use Viewport 2.0 APIs instead.) beginGL() -> self"""
    def beginProjMatrixOverride(self) -> MMatrix:
        """(Deprecated: Please use MHWRender::MRenderOverride instead.) beginProjMatrixOverride(projectionMatrix) -> self"""
    def beginSelect(self, buffer: Any = None, size: int = 0) -> M3dView:
        """Start selecting. The buffer passed is used to record selection hits."""
    def beginXorDrawing(self, stipplePattern: Any, lineColor: MColor, drawOrthographic: bool = True, disableDepthTesting: bool = True, lineWidth: float = 1.0) -> M3dView:
        """Setup the context for exclusive-or (XOR) drawing."""
    def colorAtIndex(self, index: int, table: Any) -> MColor:
        """Returns the value of the color at the given index in the application's color table."""
    def colorMask(self) -> tuple[Any]:
        """(Deprecated: Please use MHWRender::MUIDrawManager instead.) colorMask() -> [bool, bool, bool, bool]"""
    def deviceContext(self) -> int:
        """Returns a long containing a C++ 'void' pointer which points to the Windows device context for this view."""
    def disallowPolygonOffset(self) -> bool:
        """Returns the current state of the disallow polygon offset bit.  See setDisallowPolygonOffset for more information."""
    def display(self) -> int:
        """Returns a long containing a C++ 'void' pointer which points to the OpenGL context for this view."""
    @staticmethod
    def displayStatus(path: MDagPath) -> int:
        """Returns the display status of the given DAG path."""
    def displayStyle(self) -> int:
        """Return the display style for this 3d view.  kBoundingBox     Bounding box display."""
    def drawText(self, text: Any, position: MPoint, arg: Any = None) -> None:
        """(Deprecated: Please use MHWRender::MUIDrawManager in a MHWRender::MHUDRender operation instead.) drawText(text, position, textPosition=kLeft) -> self"""
    def endGL(self) -> None:
        """(Deprecated: Please use Viewport 2.0 APIs instead.) endGL() -> self"""
    def endProjMatrixOverride(self) -> None:
        """(Deprecated: Please use MHWRender::MRenderOverride instead.) endProjMatrixOverride() -> self"""
    def endSelect(self) -> int:
        """Finish a selection sequence. Result is stored in the buffer passed  in the beginSelect call."""
    def endXorDrawing(self) -> M3dView:
        """Reset the context to non-exclusive-or (non-XOR) screen drawing."""
    def filteredObjectList(self) -> MSelectionList:
        """Returns a selection list containing all of the objects that remain after filtering is applied to the view."""
    @staticmethod
    def get3dView(index: int) -> M3dView:
        """Returns the 3D view at the given index."""
    def getCamera(self) -> MDagPath:
        """Get the camera for this view."""
    def getColorIndexAndTable(self, glindex: int) -> Any:
        """Returns the index and color table representing the given OpenGL color-index value. This method is useful when converting color indices obtained from glReadPixels(GL_COLOR_INDEX) to Maya color-index values suitable for use with the colorAtIndex and setDrawColor methods."""
    def getLightCount(self, visible: bool = True) -> int:
        """Get the number of lights for the view."""
    def getLightIndex(self, lightNumber: int) -> int:
        """Get the internal light index for a given light number"""
    def getLightPath(self, lightNumber: int) -> MDagPath:
        """Get the path to a certain light."""
    def getLightingMode(self) -> int:
        """Get the current lighting mode for the view:"""
    @staticmethod
    def getM3dViewFromModelEditor(name: Any) -> M3dView:
        """Given the name of a model editor, get the M3dView used by that editor. If this fails, then a editor with the given name could not be located."""
    @staticmethod
    def getM3dViewFromModelPanel(name: Any) -> M3dView:
        """Given the name of a model panel, get the M3dView used by that panel. If this fails, then a panel with the given name could not be located."""
    def getRendererName(self) -> int:
        """Get the name of the current renderer being used for drawing to this view:"""
    def getScreenPosition(self) -> Any:
        """Returns the current position of this view window in screen coordinates."""
    @staticmethod
    def hiliteColor() -> MColor:
        """Returns the color for hilited objects."""
    def initNames(self) -> M3dView:
        """Reset the name stack. Valid only when beginSelect() has been called."""
    @staticmethod
    def isBackgroundGradient() -> bool:
        """Returns whether a gradient is being used as the background color."""
    def isLightVisible(self, lightNumber: int) -> bool:
        """Find out if a light is visible in the view"""
    def isShadeActiveOnly(self) -> bool:
        """Returns True if this view's display style is shaded for objects that are active and wireframe otherwise."""
    def isVisible(self) -> bool:
        """Returns True if this viewport is visible."""
    @staticmethod
    def leadColor() -> MColor:
        """Returns the color for lead objects."""
    @staticmethod
    def liveColor() -> MColor:
        """Returns the color for live objects."""
    def loadName(self, int: Any) -> M3dView:
        """Replace the top of the name stack with the given name. Valid only when beginSelect() has been called."""
    def modelViewMatrix(self) -> MMatrix:
        """Returns the modelview matrix currently being used by OpenGL in the current view"""
    def multipleDrawEnabled(self) -> bool:
        """This method returns the multiple draw enable state for this view."""
    def multipleDrawPassCount(self) -> int:
        """(Deprecated: Please use MHWRender::MRenderOverride instead.) multipleDrawPassCount() -> int"""
    def numActiveColors(self) -> int:
        """Returns the number of active object colors in the internal application color table."""
    def numDormantColors(self) -> int:
        """Returns the number of dormant object colors in the internal application color table."""
    def numUserDefinedColors(self) -> int:
        """Returns the number of user defined colors in the internal application color table.  These colors may be changed by the user and assigned to specific objects.  See the methods of MFnDagNode for information on assigning user defined colors to individual objects."""
    @staticmethod
    def numberOf3dViews() -> int:
        """Returns the number of 3D views currently in existance."""
    def objectDisplay(self) -> int:
        """Returns a display object mask that indicates which object types are drawn in the current view:"""
    def objectListFilterName(self) -> Any:
        """Get the current object list filter name. If none then an emptystring will be returned."""
    def playblastPortHeight(self) -> int:
        """Returns the port height of current playblast."""
    def playblastPortWidth(self) -> int:
        """Returns the port width of current playblast."""
    def pluginObjectDisplay(self, pluginDisplayFilter: Any) -> bool:
        """Returns True if the plugin display filter specified by the pluginDisplayFilter is enabled in the current view."""
    def popName(self) -> M3dView:
        """Removes the top of the name stack. Valid only when beginSelect() has been called."""
    def popViewport(self) -> M3dView:
        """Pops the current viewport off of the viewport stack."""
    def portHeight(self) -> int:
        """Returns the height of the current viewport."""
    def portWidth(self) -> int:
        """Returns the width of the current viewport."""
    def projectionMatrix(self) -> MMatrix:
        """Returns the projection matrix currently being used by OpenGL in the current view"""
    def pushName(self, int: Any) -> M3dView:
        """Pushes a new name on the name stack. Valid only when beginSelect() has been called."""
    def pushViewport(self, x: int, y: int, width: int, height: int) -> M3dView:
        """Set the current viewport dimensions. Will keep track of the last viewport dimensions on a stack."""
    def readBufferTo2dTexture(self, x: Any, y: Any, width: int, height: int) -> None:
        """(Deprecated: Please use MHWRender::MRenderTargetManager instead.) readBufferTo2dTexture(x, y, width, height) -> self"""
    def readColorBuffer(self, readRGBA: bool | None = None) -> MImage:
        """(Deprecated: Please use MHWRender::MRenderTargetManager::acquireRenderTarget() instead.)readColorBuffer(image, readRGBA=False) -> self"""
    def readDepthMap(self, x: Any, y: Any, width: int, height: int, depthMapPrecision: Any) -> Any:
        """(Deprecated: Please use MHWRender::MRenderTargetManager::acquireRenderTarget() instead.) readDepthMap(x, y, width, heigth, bufferPtr, depthMapPrecision) -> self"""
    @staticmethod
    def referenceLayerColor() -> MColor:
        """Returns the color for objects which belong to a display layer whose display type is Reference. This color is also used for objects whose display override is set to Reference."""
    def refresh(self, all: bool = False, force: bool = False, offscreen: bool = False) -> M3dView:
        """Refresh the this view."""
    def renderOverrideName(self) -> Any:
        """Get the current render override name. If none then an empty string will be returned."""
    def rendererString(self) -> Any:
        """Get the string name of the current renderer being used for drawing to this view"""
    def scheduleRefresh(self) -> M3dView:
        """Schedule a forced refresh for this 3d-view. This method may be called safely at any time from any thread. The refresh will occur on the main thread when Maya next becomes idle. If a refresh has already been scheduled for this view but has not yet occurred then this method will do nothing."""
    @staticmethod
    def scheduleRefreshAllViews() -> None:
        """Schedule a forced refresh for all 3d-views. This method may be called safely at any time from any thread. The refresh will occur on the main thread when Maya next becomes idle. If a refresh has already been scheduled but has not yet occurred then this method will do nothing."""
    def selectMode(self) -> bool:
        """Tells if this M3dView is in selection mode."""
    def setCamera(self, camera: Any) -> M3dView:
        """Set the camera for this view."""
    def setColorMask(self, r: bool, g: bool, b: bool, a: bool) -> None:
        """(Deprecated: Please use MHWRender::MUIDrawManager instead.) setColorMask(r, g, b, a) -> self"""
    def setDisallowPolygonOffset(self, v: bool) -> M3dView:
        """Certain Maya actions will use glPolygonOffset to offset polygons drawing into the depth buffer.  This method controls this behavior. When True, it prevents Maya from altering the polygon offset parameters."""
    def setDisplayStyle(self, style: Any, activeOnly: bool = False) -> M3dView:
        """Sets the display style for this view."""
    def setDrawColor(self, index: int | MColor, table: Any = None) -> None:
        """(Deprecated: Please use MUIDrawManager::setColorIndex instead.) setDrawColor(index, table=kActiveColors) -> self"""
    def setDrawColorAndAlpha(self, color: MColor) -> None:
        """(Deprecated: Please use MUIDrawManager::setColor instead.) setDrawColorAndAlpha(color) -> self"""
    def setMultipleDrawEnable(self, enable: bool) -> None:
        """(Deprecated: Please use MHWRender::MRenderOverride instead.)setMultipleDrawEnable(enable) -> self"""
    def setMultipleDrawPassCount(self, count: int) -> None:
        """(Deprecated: Please use MHWRender::MRenderOverride instead.) setMultipleDrawPassCount(count) -> self"""
    def setObjectDisplay(self, displayMask: int) -> M3dView:
        """Sets a display object mask that indicates which object types are drawn in current view. By default every thing is displayed."""
    def setObjectListFilterName(self, name: Any) -> M3dView:
        """Set the name of the object list filter (MObjectListFilter) to use."""
    def setPluginObjectDisplay(self, pluginDisplayFilter: Any, on: bool) -> M3dView:
        """Enables or disables a user-defined display filter (i.e. one which was registered using MFnPlugin.registerDisplayFilter() or the 'pluginDisplayFilter' command)."""
    def setRenderOverrideName(self, name: Any) -> M3dView:
        """Set the name of a render override (MRenderOverride) to use."""
    def setShowObjectFilterNameInHUD(self, show: bool) -> M3dView:
        """Sets whether or not to display the object filter UI name in the heads up display when an object filter is active. This string is concatenated with the camera name."""
    def setShowViewSelectedChildren(self, show: Any) -> M3dView:
        """This method changes the way that view selected works. By default, view selected with show all of the children of the objects in the view selected set. If False is passed to this method, then only the obejcts in the view selected set and their shapes will be drawn."""
    def setUserDefinedColor(self, index: int, color: MColor) -> M3dView:
        """Sets the user defined color at the given index.  Valid indices range between zero and the number of user defined colors."""
    def setViewSelectedPrefix(self, prefix: Any) -> M3dView:
        """Sets the prefix for the camera name as displayed in the heads up display when view selected is enabled. The prefix is concatenated with the camera name."""
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
        """Return True if the Two-sided lighting mode is enabled."""
    def updateViewingParameters(self) -> M3dView:
        """This method tells the camera to set the view's transformation matrix."""
    def userDefinedColorIndex(self, index: int) -> int:
        """Returns the index for the given user-defined color.  Valid values for the index argument range between zero and the number of user-defined colors minus one."""
    def usingDefaultMaterial(self) -> bool:
        """Returns True if the view is currently displaying objects using the default material."""
    def usingMipmappedTextures(self) -> bool:
        """Returns if the view is using mipmapped texture display."""
    def viewIsFiltered(self) -> bool:
        """Returns True if the view is filtered."""
    def viewSelectedPrefix(self) -> Any:
        """Returns the prefix used when displaying the camera name in the heads up display when view selected in on"""
    def viewToObjectSpace(self, x_pos: Any, y_pos: Any, localMatrixInverse: MMatrix, oPt: Any, oVector: Any) -> M3dView:
        """Takes a point in port coordinates and returns a corresponding ray in object coordinates."""
    def viewToWorld(self, x_pos: Any, y_pos: Any, worldPt: Any, worldVector: Any) -> M3dView:
        """viewToWorld(x_pos, y_pos, nearClipPt, farClipPt) -> self"""
    def viewport(self) -> Any:
        """Get the current viewport dimensions."""
    def widget(self) -> int:
        """Returns a long containing a C++ 'void' pointer which points to the view's Qt widget."""
    def window(self) -> int:
        """Returns a long containing a C++ 'void' pointer which points to the native window for this view."""
    def wireframeOnShaded(self) -> bool:
        """Return whether we draw wireframe in shaded mode."""
    def wireframeOnlyInShadedMode(self) -> bool:
        """Return whether we are in shaded mode, but that only non shaded drawing should occur (wireframe)."""
    def worldToView(self, worldPt: MPoint) -> Any:
        """Converts a point in world space to port space."""
    def writeColorBuffer(self, image: MImage, x: Any = None, y: Any = None) -> None:
        """(Deprecated: Please use MHWRender::MQuadRender operation inside MHWRender::MRenderOverride instead.) writeColorBuffer(image, x=0, y=0) -> self"""
    def xray(self) -> bool:
        """Return True if the X-Ray mode is enabled."""
    def xrayJoints(self) -> bool:
        """Return True if the X-Ray Joints mode is enabled."""

class MCursor:
    kCrossHairCursor: Any
    kDefaultCursor: Any
    kDoubleCrossHairCursor: Any
    kEditCursor: Any
    kHandCursor: Any
    kPencilCursor: Any
    def __init__(self, width: Any = None, height: Any = None, hotSpotX: Any = None, hotSpotY: Any = None, bits: Any = None, mask: Any = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MDrawData:
    def __init__(self, in_: MDrawData | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def geometry(self) -> int:
        """Returns a long containing a C++ 'void' pointer which points to the geometry associated with this draw data object."""

class MDrawInfo:
    def __init__(self, in_: MDrawInfo | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def canDrawComponent(self, isDisplayOn: bool, compMask: MSelectionMask) -> bool:
        """Convenience method to test if components specified by the given mask can be drawn."""
    def completelyInside(self) -> bool:
        """Returns True if the object being drawn is inside the viewing frustum."""
    def displayStatus(self) -> int:
        """Returns the status of the object to draw."""
    def displayStyle(self) -> int:
        """Returns the display appearance."""
    def getPrototype(self, drawHandler: MPxSurfaceShapeUI) -> MDrawRequest:
        """This method creates a draw request based on the current draw state."""
    def inSelect(self) -> bool:
        """Returns True during any interactive refresh, as when user is interacting with the scene in any way including camera changes, object or component TRS changes, etc. Use userChangingViewContext for determining whether user is changing the view using view context tools such as tumble, dolly or track."""
    def inUserInteraction(self) -> bool:
        """Returns True during any interactive refresh, as when user is changing the view using view context tools such as tumble, dolly or track.  Useful for changing drawing mode to something simpler to speed up interaction re-draw.  Use inUserInteraction for determining whether user is interacting with the scene in any way."""
    def inclusiveMatrix(self) -> MMatrix:
        """Returns the world space inclusive matrix."""
    def multiPath(self) -> MDagPath:
        """Returns the path to the object to be drawn."""
    def objectDisplayStatus(self, displayObj: int) -> bool:
        """Determines whether the specified objects are allowed to be displayed."""
    def pluginObjectDisplayStatus(self, pluginDisplayFilter: Any) -> bool:
        """Determines whether the specified plugin object is allowed to be displayed."""
    def projectionMatrix(self) -> MMatrix:
        """Returns the camera*projection matrix."""
    def setMultiPath(self, path: Any) -> MDrawInfo:
        """Sets the path of the object to be drawn."""
    def userChangingViewContext(self) -> bool:
        """Returns True during any interactive refresh, as when user is interacting with the scene in any way including camera changes, object or component TRS changes, etc. Use userChangingViewContext for determining whether user is changing the view using view context tools such as tumble, dolly or track."""
    def view(self) -> M3dView:
        """Returns the view that the drawing will take place."""

class MDrawProperties:
    color: Any
    lineStyle: Any
    lineWidth: Any
    pointSize: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MDrawRequest:
    color: Any
    component: Any
    displayCullOpposite: Any
    displayCulling: Any
    displayStatus: Any
    displayStyle: Any
    drawData: Any
    drawLast: Any
    isTransparent: Any
    material: Any
    matrix: Any
    multiPath: Any
    token: Any
    view: Any
    def __init__(self, in_: MDrawRequest | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def planeColor(self, table: Any) -> int:
        """Get which color is used for the specified color table."""
    def setPlaneColor(self, value: Any, table: Any) -> MDrawRequest:
        """Set which color to use for the specified color table."""

class MEvent:
    controlKey: Any
    kLeftMouse: Any
    kMiddleMouse: Any
    modifiers: Any
    position: Any
    shiftKey: Any
    def __init__(self) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getWindowPosition(self, arg: Any, y: Any) -> Any:
        """This routine is used by responders to query the position of the"""
    def isModifierControl(self) -> bool:
        """Return the state of the control key."""
    def isModifierKeyRelease(self) -> bool:
        """Was a modifier key released."""
    def isModifierLeftMouseButton(self) -> bool:
        """Return the state of the left mouse button."""
    def isModifierMiddleMouseButton(self) -> bool:
        """Return the state of the middle mouse button."""
    def isModifierNone(self) -> bool:
        """Determines if there are any modifiers for this event."""
    def isModifierShift(self) -> bool:
        """Return the state of the shift key."""
    def mouseButton(self) -> Any:
        """Get the mouse button of the last event."""

class MFnCircleSweepManip:
    boundingBox: Any
    endPoint: Any
    inModel: Any
    inUnderWorld: Any
    isDefaultNode: Any
    isFromReferencedFile: Any
    isInstanceable: Any
    isIntermediateObject: Any
    isLocked: Any
    isOptimizePlaybackOn: Any
    isShared: Any
    isVisible: Any
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
    manipScale: Any
    namespace: Any
    objectColor: Any
    objectColorRGB: Any
    objectColorType: Any
    pluginName: Any
    startPoint: Any
    typeId: Any
    typeName: Any
    useObjectColor: Any
    def __init__(self, object: MObject | MDagPath | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def absoluteName(self) -> Any:
        """Returns the absolute name of this node.  The absolute name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself.  Regardless of relative name mode, absoluteName() will always return a full namespace path prefixed with a leading colon (the root namespace).  If the underlying node is a DAG node, then absoluteName() does not guarantee uniqueness, that is, two dependency nodes could have the same absoluteName().  In cases like this the uniqueName() method will guarantee that the name uniquely identifies the node."""
    def addAttribute(self, attr: MObject, type: Any) -> None:
        """Adds a new dynamic attribute to the node."""
    def addChild(self, node: int, index: bool, keepExistingParents: bool = False) -> MFnCircleSweepManip:
        """Makes a node a child of this one."""
    def addExternalContentForFileAttr(self, attr: MObject) -> MExternalContentInfoTable:
        """Adds content info to the specified table from a file path attribute."""
    def affectsAnimation(self) -> bool:
        """Returns true if the changes to the node may affect animation."""
    @staticmethod
    def allocateFlag(pluginName: Any) -> int:
        """Allocates a flag on all nodes for use by the named plugin and returns the flag's index."""
    def angleIndex(self) -> int:
        """Returns the index for the angle of CircleSweepManip. The data type corresponding to this index is a double."""
    def attribute(self, index: Any) -> MObject:
        """Returns an attribute of the node, given either its index or name."""
    def attributeClass(self, attr: MObject) -> Any:
        """Returns the class of the specified attribute."""
    def attributeCount(self) -> int:
        """Returns the number of attributes on the node."""
    def axisIndex(self) -> int:
        """Returns the index for the axis of CircleSweepManip. The data type corresponding to this index is MFnNumericData.k3Double."""
    @staticmethod
    def balanceTransformation(identity: int, identity_: int, one: int, kXYZ: int, arg: Any = None) -> None:
        """Balance a transformation when applying a world matrix to a joint. Thisaccesses the same underlying functionality as the xform command."""
    def canBeWritten(self) -> bool:
        """Returns true if the node will be written to file."""
    def centerIndex(self) -> int:
        """Returns the index for the center of the CircleSweepManip. The data type corresponding to this index is MFnNumericData.k3Double."""
    def child(self, index: int) -> MObject:
        """Returns the specified child of this node."""
    def childCount(self) -> int:
        """Returns the number of nodes which are children of this one."""
    @staticmethod
    def classification(nodeTypeName: Any) -> Any:
        """Returns the classification string for the named node type."""
    def clearRestPosition(self) -> None:
        """Clears the transform's rest position matrix."""
    def connectToAnglePlug(self, anglePlug: Any) -> MFnCircleSweepManip:
        """Connect to the angle plug. The data type corresponding to the anglePlug is a double. (Note that MFnUnitAttribute.kAngle is used to specify an angle attribute.)"""
    def create(self, manipName: Any = None, angleName: Any = None) -> MObject:
        """Creates a new CircleSweepManip."""
    def dagPath(self) -> MDagPath:
        """Returns the DAG path to which this function set is attached. Raises a TypeError if the function set is attached to an MObject rather than a path."""
    def dagRoot(self) -> MObject:
        """Returns the root node of the first path leading to this node."""
    @staticmethod
    def deallocateAllFlags(pluginName: Any) -> None:
        """Deallocates all node flags which are currently allocated to the named plugin."""
    @staticmethod
    def deallocateFlag(pluginName: Any, flag: int) -> None:
        """Deallocates the specified node flag, which was previously allocated by the named plugin using allocateFlag()."""
    @staticmethod
    def deleteManipulator(manip: Any) -> None:
        """Delete a manipulator.  This method should be used to delete manipulators that have been created using base manipulator create() methods."""
    def dgCallbackIds(self, type: Any, callbackName: Any) -> tuple[Any]:
        """Returns DG timing information for a specific callback type, broken down by callbackId."""
    def dgCallbacks(self, type: Any) -> tuple[Any]:
        """Returns DG timing information broken down by callback type."""
    def dgTimer(self, timerMetric: Any, timerType: Any) -> float:
        """Returns a specific DG timer metric for a given timer type."""
    def dgTimerOff(self) -> None:
        """Turns DG timing off for this node."""
    def dgTimerOn(self) -> None:
        """Turns DG timing on for this node."""
    def dgTimerQueryState(self) -> Any:
        """Returns the current DG timer state for this node."""
    def dgTimerReset(self) -> None:
        """Resets all DG timers for this node."""
    @staticmethod
    def drawPlaneHandles() -> bool:
        """This method returns the global option that says if the planar manipulator handles should be drawn or not.Setting this will affect the drawing of all manipulators that support the planar handles."""
    def duplicate(self, instance: bool = False, instanceLeaf: bool = False) -> MObject:
        """Duplicates the DAG hierarchy rooted at the current node."""
    def enableLimit(self, type: int, flag: bool) -> None:
        """Enables or disables a specified limit type."""
    def endCircleIndex(self) -> int:
        """Returns the index for the end of the circle of CircleSweepManip. The data type corresponding to this index is a double."""
    def findAlias(self, alias: Any, attrObj: MObject) -> bool:
        """Returns the attribute which has the given alias."""
    def findPlug(self, attr: Any, wantNetworkedPlug: bool) -> MPlug:
        """Returns a plug for the given attribute."""
    def fullPathName(self) -> Any:
        """Returns the full path of the attached object, from the root of the DAG on down."""
    def getAffectedAttributes(self, attr: MObject) -> MObjectArray:
        """Returns all of the attributes which are affected by the specified attribute."""
    def getAffectingAttributes(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all of the attributes which affect the specified attribute."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute aliases."""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns all of the node's attribute aliases."""
    def getAllPaths(self) -> MDagPathArray:
        """Returns all of the DAG paths which lead to the object to which this function set is attached."""
    def getConnectedSetsAndMembers(self, instance: int, arg: bool, MObjectArray: Any) -> Any:
        """Returns a tuple containing an array of sets and an array of the"""
    def getConnections(self) -> MPlugArray:
        """Returns all the plugs which are connected to attributes of this node."""
    def getExternalContent(self) -> MExternalContentInfoTable:
        """Gets the external content (files) that this node depends on."""
    def getPath(self) -> MDagPath:
        """Returns the DAG path to which this function set is attached, or the first path to the node if the function set is attached to an MObject."""
    @staticmethod
    def globalSize() -> float:
        """Returns the global manipulator size."""
    @staticmethod
    def handleSize() -> float:
        """Returns the manipulator handle size."""
    def hasAttribute(self, name: Any) -> bool:
        """Returns True if the node has an attribute with the given name."""
    def hasChild(self, node: MObject) -> bool:
        """Returns True if the specified node is a child of this one."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def hasParent(self, node: MObject) -> bool:
        """Returns True if the specified node is a parent of this one."""
    def hasUniqueName(self) -> bool:
        """Returns True if the node's name is unique."""
    def instanceCount(self, indirect: bool) -> int:
        """Returns the number of instances for this node."""
    def isChildOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a parent of this one."""
    def isFlagSet(self, flag: int) -> bool:
        """Returns the state of the specified node flag."""
    def isInstanced(self, indirect: bool = True) -> bool:
        """Returns True if this node is instanced."""
    def isInstancedAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute is an instanced attribute of this node."""
    def isLimited(self, type: int) -> bool:
        """Returns True if the specified limit type is enabled."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files."""
    def isParentOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a child of this one."""
    def isTrackingEdits(self) -> bool:
        """Returns True if the node is referenced or in an assembly that is tracking edits."""
    def limitValue(self, type: int) -> float:
        """Returns the value of the specified limit."""
    @staticmethod
    def lineSize() -> float:
        """Returns the manipulator line size."""
    def name(self) -> Any:
        """Returns the node's name."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def parent(self, index: int) -> MObject:
        """Returns the specified parent of this node."""
    def parentCount(self) -> int:
        """Returns the number of parents this node has."""
    def partialPathName(self) -> Any:
        """Returns the minimum path string necessary to uniquely identify the attached object."""
    def plugsAlias(self, plug: MPlug) -> Any:
        """Returns the alias for a plug's attribute."""
    def removeAttribute(self, attr: MObject, type: Any) -> None:
        """Removes a dynamic attribute from the node."""
    def removeChild(self, node: Any) -> MFnCircleSweepManip:
        """Removes the child, specified by MObject, reparenting it under the world."""
    def removeChildAt(self, index: int) -> MFnCircleSweepManip:
        """Removes the child, specified by index, reparenting it under the world."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Returns one of the node's attribute, based on the order in which they are written to file."""
    def resetFromRestPosition(self) -> None:
        """Resets the transform from its rest position matrix."""
    def resetTransformation(self, m: MMatrix) -> None:
        """Resets the transform's attribute values to represent the given transformation matrix in world space."""
    def restPosition(self) -> MTransformationMatrix:
        """Returns the transform's rest position matrix."""
    def rotateBy(self, quaternion: MQuaternion | MEulerRotation | int, Space: int | None = None) -> None:
        """Adds an MEulerRotation or MQuaternion to the transform's rotation."""
    def rotateByComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Adds to the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""
    def rotateOrientation(self, space: int) -> MQuaternion:
        """Returns the MQuaternion which orients the local rotation space."""
    def rotatePivot(self, space: int) -> MPoint:
        """Returns the transform's rotate pivot."""
    def rotatePivotTranslation(self, space: int) -> MVector:
        """Returns the transform's rotate pivot translation."""
    def rotateXYZValue(self, valIndex: int) -> MEulerRotation:
        """Gets the rotation for the active manipulator."""
    def rotation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotation as an MEulerRotation or MQuaternion."""
    def rotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotation as the individual components of an MEulerRotation or MQuaternion."""
    def rotationOrder(self) -> int:
        """Returns the order of rotations when the transform's rotation is expressed as an MEulerRotation."""
    def scale(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transform's XYZ scale components."""
    def scaleBy(self) -> None:
        """Multiplies the transform's XYZ scale components by a sequence of three floats."""
    def scalePivot(self, space: int) -> MPoint:
        """Returns the transform's scale pivot."""
    def scalePivotTranslation(self, space: int) -> MVector:
        """Returns the transform's scale pivot translation."""
    def setAffectsAnimation(self) -> None:
        """Specifies that modifications to a node could potentially affect the animation."""
    def setAlias(self, alias: Any, name: Any, plug: MPlug, add: bool | None = None) -> bool:
        """Adds or removes an attribute alias."""
    def setAngle(self, angle: MAngle) -> MFnCircleSweepManip:
        """Sets the angle of the CircleSweepManip."""
    def setCenterPoint(self, centerPoint: MPoint) -> MFnCircleSweepManip:
        """Sets the center point of the CircleSweepManip."""
    def setDoNotWrite(self, flag: bool) -> None:
        """Used to prevent the node from being written to file."""
    def setDrawAsArc(self, state: bool) -> MFnCircleSweepManip:
        """Sets whether or not to draw as arc."""
    @staticmethod
    def setDrawPlaneHandles(bool: bool) -> None:
        """Sets the global option to display planar handles or not on supported manipulators."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> None:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> None:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> None:
        """Sets the state of the specified node flag."""
    @staticmethod
    def setGlobalSize(float: float) -> None:
        """Sets the global manipulator size."""
    @staticmethod
    def setHandleSize(float: float) -> None:
        """Sets the manipulator handle size."""
    def setLimit(self, type: int, value: float) -> None:
        """Sets the value of the specified limit."""
    @staticmethod
    def setLineSize(float: float) -> None:
        """Sets the manipulator line size."""
    def setName(self, name: Any, createNamespace: bool | None = None) -> Any:
        """Sets the node's name."""
    def setNormal(self, normal: MVector) -> MFnCircleSweepManip:
        """Sets the normal of the CircleSweepManip."""
    def setObject(self, arg: MDagPath | MObject) -> MFnCircleSweepManip:
        """Attaches the function set to the specified node or DAG path."""
    def setRadius(self, radius: float) -> MFnCircleSweepManip:
        """Sets the radius of the CircleSweepManip."""
    def setRestPosition(self, matrix: MTransformationMatrix) -> None:
        """Sets the transform's rest position matrix."""
    def setRotateOrientation(self, quat: MQuaternion, space: int, balance: bool) -> None:
        """Sets the MQuaternion which orients the local rotation space."""
    def setRotatePivot(self, point: MPoint, space: int, balance: bool) -> None:
        """Sets the transform's rotate pivot."""
    def setRotatePivotTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's rotate pivot translation."""
    def setRotation(self, quaternion: MQuaternion | MEulerRotation | int, Space: int | None = None) -> None:
        """Sets the transform's rotation using an MEulerRotation or MQuaternion."""
    def setRotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""
    def setRotationOrder(self, order: int, reorder: bool) -> None:
        """Sets the transform's rotation order."""
    def setScale(self) -> None:
        """Sets the transform's scale components."""
    def setScalePivot(self, point: MPoint, space: int, balance: bool) -> None:
        """Sets the transform's scale pivot."""
    def setScalePivotTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's scale pivot translation."""
    def setShear(self) -> None:
        """Sets the transform's shear."""
    def setTransformation(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's attribute values to represent the given transformation matrix."""
    def setTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's translation."""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def shear(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transform's shear components."""
    def shearBy(self) -> None:
        """Multiplies the transform's shear components by a sequence of three floats."""
    def startCircleIndex(self) -> int:
        """Returns the index for the start of the circle of CircleSweepManip. The data type corresponding to this index is a double."""
    def transformation(self) -> MTransformationMatrix:
        """Returns the transformation matrix represented by this transform."""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
    def translateBy(self, vec: MVector, space: int) -> None:
        """Adds an MVector to the transform's translation."""
    def translation(self, Space: int) -> MVector:
        """Returns the transform's translation as an MVector."""
    def type(self) -> int:
        """Returns the type of the function set."""
    def uniqueName(self) -> Any:
        """For a DAG node, the unique name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself. For a non-DAG node, the uniqueName is just its name."""
    def userNode(self) -> MPxNode:
        """Returns the MPxNode object for a plugin node."""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnCurveSegmentManip:
    boundingBox: Any
    endParameter: Any
    inModel: Any
    inUnderWorld: Any
    isDefaultNode: Any
    isFromReferencedFile: Any
    isInstanceable: Any
    isIntermediateObject: Any
    isLocked: Any
    isOptimizePlaybackOn: Any
    isShared: Any
    isVisible: Any
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
    manipScale: Any
    namespace: Any
    objectColor: Any
    objectColorRGB: Any
    objectColorType: Any
    pluginName: Any
    startParameter: Any
    typeId: Any
    typeName: Any
    useObjectColor: Any
    def __init__(self, object: MObject | MDagPath | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def absoluteName(self) -> Any:
        """Returns the absolute name of this node.  The absolute name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself.  Regardless of relative name mode, absoluteName() will always return a full namespace path prefixed with a leading colon (the root namespace).  If the underlying node is a DAG node, then absoluteName() does not guarantee uniqueness, that is, two dependency nodes could have the same absoluteName().  In cases like this the uniqueName() method will guarantee that the name uniquely identifies the node."""
    def addAttribute(self, attr: MObject, type: Any) -> None:
        """Adds a new dynamic attribute to the node."""
    def addChild(self, node: int, index: bool, keepExistingParents: bool = False) -> MFnCurveSegmentManip:
        """Makes a node a child of this one."""
    def addExternalContentForFileAttr(self, attr: MObject) -> MExternalContentInfoTable:
        """Adds content info to the specified table from a file path attribute."""
    def affectsAnimation(self) -> bool:
        """Returns true if the changes to the node may affect animation."""
    @staticmethod
    def allocateFlag(pluginName: Any) -> int:
        """Allocates a flag on all nodes for use by the named plugin and returns the flag's index."""
    def attribute(self, index: Any) -> MObject:
        """Returns an attribute of the node, given either its index or name."""
    def attributeClass(self, attr: MObject) -> Any:
        """Returns the class of the specified attribute."""
    def attributeCount(self) -> int:
        """Returns the number of attributes on the node."""
    @staticmethod
    def balanceTransformation(identity: int, identity_: int, one: int, kXYZ: int, arg: Any = None) -> None:
        """Balance a transformation when applying a world matrix to a joint. Thisaccesses the same underlying functionality as the xform command."""
    def canBeWritten(self) -> bool:
        """Returns true if the node will be written to file."""
    def child(self, index: int) -> MObject:
        """Returns the specified child of this node."""
    def childCount(self) -> int:
        """Returns the number of nodes which are children of this one."""
    @staticmethod
    def classification(nodeTypeName: Any) -> Any:
        """Returns the classification string for the named node type."""
    def clearRestPosition(self) -> None:
        """Clears the transform's rest position matrix."""
    def connectToCurvePlug(self, curvePlug: Any) -> MFnCurveSegmentManip:
        """Connect to the curve plug. The data type corresponding to the curvePlug is MFnData.kNurbsCurve."""
    def connectToEndParamPlug(self, endParamPlug: Any) -> MFnCurveSegmentManip:
        """Connect to the endParam plug. The data type corresponding to the endParamPlug is a double."""
    def connectToStartParamPlug(self, startParamPlug: Any) -> MFnCurveSegmentManip:
        """Connect to the startParam plug. The data type corresponding to the startParamPlug is a double."""
    def create(self, manipName: Any = None, startParamName: Any = None, endParamName: Any = None) -> MObject:
        """Creates a new CurveSegmentManip."""
    def curveIndex(self) -> int:
        """Returns the index of the curve. The data type corresponding to this index is MFnData.kNurbsCurve."""
    def dagPath(self) -> MDagPath:
        """Returns the DAG path to which this function set is attached. Raises a TypeError if the function set is attached to an MObject rather than a path."""
    def dagRoot(self) -> MObject:
        """Returns the root node of the first path leading to this node."""
    @staticmethod
    def deallocateAllFlags(pluginName: Any) -> None:
        """Deallocates all node flags which are currently allocated to the named plugin."""
    @staticmethod
    def deallocateFlag(pluginName: Any, flag: int) -> None:
        """Deallocates the specified node flag, which was previously allocated by the named plugin using allocateFlag()."""
    @staticmethod
    def deleteManipulator(manip: Any) -> None:
        """Delete a manipulator.  This method should be used to delete manipulators that have been created using base manipulator create() methods."""
    def dgCallbackIds(self, type: Any, callbackName: Any) -> tuple[Any]:
        """Returns DG timing information for a specific callback type, broken down by callbackId."""
    def dgCallbacks(self, type: Any) -> tuple[Any]:
        """Returns DG timing information broken down by callback type."""
    def dgTimer(self, timerMetric: Any, timerType: Any) -> float:
        """Returns a specific DG timer metric for a given timer type."""
    def dgTimerOff(self) -> None:
        """Turns DG timing off for this node."""
    def dgTimerOn(self) -> None:
        """Turns DG timing on for this node."""
    def dgTimerQueryState(self) -> Any:
        """Returns the current DG timer state for this node."""
    def dgTimerReset(self) -> None:
        """Resets all DG timers for this node."""
    @staticmethod
    def drawPlaneHandles() -> bool:
        """This method returns the global option that says if the planar manipulator handles should be drawn or not.Setting this will affect the drawing of all manipulators that support the planar handles."""
    def duplicate(self, instance: bool = False, instanceLeaf: bool = False) -> MObject:
        """Duplicates the DAG hierarchy rooted at the current node."""
    def enableLimit(self, type: int, flag: bool) -> None:
        """Enables or disables a specified limit type."""
    def endParamIndex(self) -> int:
        """Returns the index of the end parameter of the CurveSegmentManip. The data type corresponding this index is a double."""
    def findAlias(self, alias: Any, attrObj: MObject) -> bool:
        """Returns the attribute which has the given alias."""
    def findPlug(self, attr: Any, wantNetworkedPlug: bool) -> MPlug:
        """Returns a plug for the given attribute."""
    def fullPathName(self) -> Any:
        """Returns the full path of the attached object, from the root of the DAG on down."""
    def getAffectedAttributes(self, attr: MObject) -> MObjectArray:
        """Returns all of the attributes which are affected by the specified attribute."""
    def getAffectingAttributes(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all of the attributes which affect the specified attribute."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute aliases."""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns all of the node's attribute aliases."""
    def getAllPaths(self) -> MDagPathArray:
        """Returns all of the DAG paths which lead to the object to which this function set is attached."""
    def getConnectedSetsAndMembers(self, instance: int, arg: bool, MObjectArray: Any) -> Any:
        """Returns a tuple containing an array of sets and an array of the"""
    def getConnections(self) -> MPlugArray:
        """Returns all the plugs which are connected to attributes of this node."""
    def getExternalContent(self) -> MExternalContentInfoTable:
        """Gets the external content (files) that this node depends on."""
    def getPath(self) -> MDagPath:
        """Returns the DAG path to which this function set is attached, or the first path to the node if the function set is attached to an MObject."""
    @staticmethod
    def globalSize() -> float:
        """Returns the global manipulator size."""
    @staticmethod
    def handleSize() -> float:
        """Returns the manipulator handle size."""
    def hasAttribute(self, name: Any) -> bool:
        """Returns True if the node has an attribute with the given name."""
    def hasChild(self, node: MObject) -> bool:
        """Returns True if the specified node is a child of this one."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def hasParent(self, node: MObject) -> bool:
        """Returns True if the specified node is a parent of this one."""
    def hasUniqueName(self) -> bool:
        """Returns True if the node's name is unique."""
    def instanceCount(self, indirect: bool) -> int:
        """Returns the number of instances for this node."""
    def isChildOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a parent of this one."""
    def isFlagSet(self, flag: int) -> bool:
        """Returns the state of the specified node flag."""
    def isInstanced(self, indirect: bool = True) -> bool:
        """Returns True if this node is instanced."""
    def isInstancedAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute is an instanced attribute of this node."""
    def isLimited(self, type: int) -> bool:
        """Returns True if the specified limit type is enabled."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files."""
    def isParentOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a child of this one."""
    def isTrackingEdits(self) -> bool:
        """Returns True if the node is referenced or in an assembly that is tracking edits."""
    def limitValue(self, type: int) -> float:
        """Returns the value of the specified limit."""
    @staticmethod
    def lineSize() -> float:
        """Returns the manipulator line size."""
    def name(self) -> Any:
        """Returns the node's name."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def parent(self, index: int) -> MObject:
        """Returns the specified parent of this node."""
    def parentCount(self) -> int:
        """Returns the number of parents this node has."""
    def partialPathName(self) -> Any:
        """Returns the minimum path string necessary to uniquely identify the attached object."""
    def plugsAlias(self, plug: MPlug) -> Any:
        """Returns the alias for a plug's attribute."""
    def removeAttribute(self, attr: MObject, type: Any) -> None:
        """Removes a dynamic attribute from the node."""
    def removeChild(self, node: Any) -> MFnCurveSegmentManip:
        """Removes the child, specified by MObject, reparenting it under the world."""
    def removeChildAt(self, index: int) -> MFnCurveSegmentManip:
        """Removes the child, specified by index, reparenting it under the world."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Returns one of the node's attribute, based on the order in which they are written to file."""
    def resetFromRestPosition(self) -> None:
        """Resets the transform from its rest position matrix."""
    def resetTransformation(self, m: MMatrix) -> None:
        """Resets the transform's attribute values to represent the given transformation matrix in world space."""
    def restPosition(self) -> MTransformationMatrix:
        """Returns the transform's rest position matrix."""
    def rotateBy(self, quaternion: MQuaternion | MEulerRotation | int, Space: int | None = None) -> None:
        """Adds an MEulerRotation or MQuaternion to the transform's rotation."""
    def rotateByComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Adds to the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""
    def rotateOrientation(self, space: int) -> MQuaternion:
        """Returns the MQuaternion which orients the local rotation space."""
    def rotatePivot(self, space: int) -> MPoint:
        """Returns the transform's rotate pivot."""
    def rotatePivotTranslation(self, space: int) -> MVector:
        """Returns the transform's rotate pivot translation."""
    def rotateXYZValue(self, valIndex: int) -> MEulerRotation:
        """Gets the rotation for the active manipulator."""
    def rotation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotation as an MEulerRotation or MQuaternion."""
    def rotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotation as the individual components of an MEulerRotation or MQuaternion."""
    def rotationOrder(self) -> int:
        """Returns the order of rotations when the transform's rotation is expressed as an MEulerRotation."""
    def scale(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transform's XYZ scale components."""
    def scaleBy(self) -> None:
        """Multiplies the transform's XYZ scale components by a sequence of three floats."""
    def scalePivot(self, space: int) -> MPoint:
        """Returns the transform's scale pivot."""
    def scalePivotTranslation(self, space: int) -> MVector:
        """Returns the transform's scale pivot translation."""
    def setAffectsAnimation(self) -> None:
        """Specifies that modifications to a node could potentially affect the animation."""
    def setAlias(self, alias: Any, name: Any, plug: MPlug, add: bool | None = None) -> bool:
        """Adds or removes an attribute alias."""
    def setDoNotWrite(self, flag: bool) -> None:
        """Used to prevent the node from being written to file."""
    @staticmethod
    def setDrawPlaneHandles(bool: bool) -> None:
        """Sets the global option to display planar handles or not on supported manipulators."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> None:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> None:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> None:
        """Sets the state of the specified node flag."""
    @staticmethod
    def setGlobalSize(float: float) -> None:
        """Sets the global manipulator size."""
    @staticmethod
    def setHandleSize(float: float) -> None:
        """Sets the manipulator handle size."""
    def setLimit(self, type: int, value: float) -> None:
        """Sets the value of the specified limit."""
    @staticmethod
    def setLineSize(float: float) -> None:
        """Sets the manipulator line size."""
    def setName(self, name: Any, createNamespace: bool | None = None) -> Any:
        """Sets the node's name."""
    def setObject(self, arg: MDagPath | MObject) -> MFnCurveSegmentManip:
        """Attaches the function set to the specified node or DAG path."""
    def setRestPosition(self, matrix: MTransformationMatrix) -> None:
        """Sets the transform's rest position matrix."""
    def setRotateOrientation(self, quat: MQuaternion, space: int, balance: bool) -> None:
        """Sets the MQuaternion which orients the local rotation space."""
    def setRotatePivot(self, point: MPoint, space: int, balance: bool) -> None:
        """Sets the transform's rotate pivot."""
    def setRotatePivotTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's rotate pivot translation."""
    def setRotation(self, quaternion: MQuaternion | MEulerRotation | int, Space: int | None = None) -> None:
        """Sets the transform's rotation using an MEulerRotation or MQuaternion."""
    def setRotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""
    def setRotationOrder(self, order: int, reorder: bool) -> None:
        """Sets the transform's rotation order."""
    def setScale(self) -> None:
        """Sets the transform's scale components."""
    def setScalePivot(self, point: MPoint, space: int, balance: bool) -> None:
        """Sets the transform's scale pivot."""
    def setScalePivotTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's scale pivot translation."""
    def setShear(self) -> None:
        """Sets the transform's shear."""
    def setTransformation(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's attribute values to represent the given transformation matrix."""
    def setTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's translation."""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def shear(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transform's shear components."""
    def shearBy(self) -> None:
        """Multiplies the transform's shear components by a sequence of three floats."""
    def startParamIndex(self) -> int:
        """Returns the index of the start parameter of the CurveSegmentManip. The data type corresponding to this index is a double."""
    def transformation(self) -> MTransformationMatrix:
        """Returns the transformation matrix represented by this transform."""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
    def translateBy(self, vec: MVector, space: int) -> None:
        """Adds an MVector to the transform's translation."""
    def translation(self, Space: int) -> MVector:
        """Returns the transform's translation as an MVector."""
    def type(self) -> int:
        """Returns the type of the function set."""
    def uniqueName(self) -> Any:
        """For a DAG node, the unique name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself. For a non-DAG node, the uniqueName is just its name."""
    def userNode(self) -> MPxNode:
        """Returns the MPxNode object for a plugin node."""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnDirectionManip:
    boundingBox: Any
    inModel: Any
    inUnderWorld: Any
    isDefaultNode: Any
    isFromReferencedFile: Any
    isInstanceable: Any
    isIntermediateObject: Any
    isLocked: Any
    isOptimizePlaybackOn: Any
    isShared: Any
    isVisible: Any
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
    manipScale: Any
    namespace: Any
    objectColor: Any
    objectColorRGB: Any
    objectColorType: Any
    pluginName: Any
    typeId: Any
    typeName: Any
    useObjectColor: Any
    def __init__(self, object: MObject | MDagPath | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def absoluteName(self) -> Any:
        """Returns the absolute name of this node.  The absolute name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself.  Regardless of relative name mode, absoluteName() will always return a full namespace path prefixed with a leading colon (the root namespace).  If the underlying node is a DAG node, then absoluteName() does not guarantee uniqueness, that is, two dependency nodes could have the same absoluteName().  In cases like this the uniqueName() method will guarantee that the name uniquely identifies the node."""
    def addAttribute(self, attr: MObject, type: Any) -> None:
        """Adds a new dynamic attribute to the node."""
    def addChild(self, node: int, index: bool, keepExistingParents: bool = False) -> MFnDirectionManip:
        """Makes a node a child of this one."""
    def addExternalContentForFileAttr(self, attr: MObject) -> MExternalContentInfoTable:
        """Adds content info to the specified table from a file path attribute."""
    def affectsAnimation(self) -> bool:
        """Returns true if the changes to the node may affect animation."""
    @staticmethod
    def allocateFlag(pluginName: Any) -> int:
        """Allocates a flag on all nodes for use by the named plugin and returns the flag's index."""
    def attribute(self, index: Any) -> MObject:
        """Returns an attribute of the node, given either its index or name."""
    def attributeClass(self, attr: MObject) -> Any:
        """Returns the class of the specified attribute."""
    def attributeCount(self) -> int:
        """Returns the number of attributes on the node."""
    @staticmethod
    def balanceTransformation(identity: int, identity_: int, one: int, kXYZ: int, arg: Any = None) -> None:
        """Balance a transformation when applying a world matrix to a joint. Thisaccesses the same underlying functionality as the xform command."""
    def canBeWritten(self) -> bool:
        """Returns true if the node will be written to file."""
    def child(self, index: int) -> MObject:
        """Returns the specified child of this node."""
    def childCount(self) -> int:
        """Returns the number of nodes which are children of this one."""
    @staticmethod
    def classification(nodeTypeName: Any) -> Any:
        """Returns the classification string for the named node type."""
    def clearRestPosition(self) -> None:
        """Clears the transform's rest position matrix."""
    def connectToDirectionPlug(self, directionPlug: Any) -> MFnDirectionManip:
        """Connect to the direction plug. The data type corresponding to the directionPlug is MFnNumericData.k3Double."""
    def create(self, manipName: Any = None, directionName: Any = None) -> MObject:
        """Creates a new DirectionManip."""
    def dagPath(self) -> MDagPath:
        """Returns the DAG path to which this function set is attached. Raises a TypeError if the function set is attached to an MObject rather than a path."""
    def dagRoot(self) -> MObject:
        """Returns the root node of the first path leading to this node."""
    @staticmethod
    def deallocateAllFlags(pluginName: Any) -> None:
        """Deallocates all node flags which are currently allocated to the named plugin."""
    @staticmethod
    def deallocateFlag(pluginName: Any, flag: int) -> None:
        """Deallocates the specified node flag, which was previously allocated by the named plugin using allocateFlag()."""
    @staticmethod
    def deleteManipulator(manip: Any) -> None:
        """Delete a manipulator.  This method should be used to delete manipulators that have been created using base manipulator create() methods."""
    def dgCallbackIds(self, type: Any, callbackName: Any) -> tuple[Any]:
        """Returns DG timing information for a specific callback type, broken down by callbackId."""
    def dgCallbacks(self, type: Any) -> tuple[Any]:
        """Returns DG timing information broken down by callback type."""
    def dgTimer(self, timerMetric: Any, timerType: Any) -> float:
        """Returns a specific DG timer metric for a given timer type."""
    def dgTimerOff(self) -> None:
        """Turns DG timing off for this node."""
    def dgTimerOn(self) -> None:
        """Turns DG timing on for this node."""
    def dgTimerQueryState(self) -> Any:
        """Returns the current DG timer state for this node."""
    def dgTimerReset(self) -> None:
        """Resets all DG timers for this node."""
    def directionIndex(self) -> int:
        """Returns the index of the direction. The data type corresponding to this index is MFnNumericData.k3Double."""
    @staticmethod
    def drawPlaneHandles() -> bool:
        """This method returns the global option that says if the planar manipulator handles should be drawn or not.Setting this will affect the drawing of all manipulators that support the planar handles."""
    def duplicate(self, instance: bool = False, instanceLeaf: bool = False) -> MObject:
        """Duplicates the DAG hierarchy rooted at the current node."""
    def enableLimit(self, type: int, flag: bool) -> None:
        """Enables or disables a specified limit type."""
    def endPointIndex(self) -> int:
        """Returns the index of the end point of the DirectionManip. The data type corresponding to this index is MFnNumericData.k3Double."""
    def findAlias(self, alias: Any, attrObj: MObject) -> bool:
        """Returns the attribute which has the given alias."""
    def findPlug(self, attr: Any, wantNetworkedPlug: bool) -> MPlug:
        """Returns a plug for the given attribute."""
    def fullPathName(self) -> Any:
        """Returns the full path of the attached object, from the root of the DAG on down."""
    def getAffectedAttributes(self, attr: MObject) -> MObjectArray:
        """Returns all of the attributes which are affected by the specified attribute."""
    def getAffectingAttributes(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all of the attributes which affect the specified attribute."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute aliases."""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns all of the node's attribute aliases."""
    def getAllPaths(self) -> MDagPathArray:
        """Returns all of the DAG paths which lead to the object to which this function set is attached."""
    def getConnectedSetsAndMembers(self, instance: int, arg: bool, MObjectArray: Any) -> Any:
        """Returns a tuple containing an array of sets and an array of the"""
    def getConnections(self) -> MPlugArray:
        """Returns all the plugs which are connected to attributes of this node."""
    def getExternalContent(self) -> MExternalContentInfoTable:
        """Gets the external content (files) that this node depends on."""
    def getPath(self) -> MDagPath:
        """Returns the DAG path to which this function set is attached, or the first path to the node if the function set is attached to an MObject."""
    @staticmethod
    def globalSize() -> float:
        """Returns the global manipulator size."""
    @staticmethod
    def handleSize() -> float:
        """Returns the manipulator handle size."""
    def hasAttribute(self, name: Any) -> bool:
        """Returns True if the node has an attribute with the given name."""
    def hasChild(self, node: MObject) -> bool:
        """Returns True if the specified node is a child of this one."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def hasParent(self, node: MObject) -> bool:
        """Returns True if the specified node is a parent of this one."""
    def hasUniqueName(self) -> bool:
        """Returns True if the node's name is unique."""
    def instanceCount(self, indirect: bool) -> int:
        """Returns the number of instances for this node."""
    def isChildOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a parent of this one."""
    def isFlagSet(self, flag: int) -> bool:
        """Returns the state of the specified node flag."""
    def isInstanced(self, indirect: bool = True) -> bool:
        """Returns True if this node is instanced."""
    def isInstancedAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute is an instanced attribute of this node."""
    def isLimited(self, type: int) -> bool:
        """Returns True if the specified limit type is enabled."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files."""
    def isParentOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a child of this one."""
    def isTrackingEdits(self) -> bool:
        """Returns True if the node is referenced or in an assembly that is tracking edits."""
    def limitValue(self, type: int) -> float:
        """Returns the value of the specified limit."""
    @staticmethod
    def lineSize() -> float:
        """Returns the manipulator line size."""
    def name(self) -> Any:
        """Returns the node's name."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def parent(self, index: int) -> MObject:
        """Returns the specified parent of this node."""
    def parentCount(self) -> int:
        """Returns the number of parents this node has."""
    def partialPathName(self) -> Any:
        """Returns the minimum path string necessary to uniquely identify the attached object."""
    def plugsAlias(self, plug: MPlug) -> Any:
        """Returns the alias for a plug's attribute."""
    def removeAttribute(self, attr: MObject, type: Any) -> None:
        """Removes a dynamic attribute from the node."""
    def removeChild(self, node: Any) -> MFnDirectionManip:
        """Removes the child, specified by MObject, reparenting it under the world."""
    def removeChildAt(self, index: int) -> MFnDirectionManip:
        """Removes the child, specified by index, reparenting it under the world."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Returns one of the node's attribute, based on the order in which they are written to file."""
    def resetFromRestPosition(self) -> None:
        """Resets the transform from its rest position matrix."""
    def resetTransformation(self, m: MMatrix) -> None:
        """Resets the transform's attribute values to represent the given transformation matrix in world space."""
    def restPosition(self) -> MTransformationMatrix:
        """Returns the transform's rest position matrix."""
    def rotateBy(self, quaternion: MQuaternion | MEulerRotation | int, Space: int | None = None) -> None:
        """Adds an MEulerRotation or MQuaternion to the transform's rotation."""
    def rotateByComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Adds to the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""
    def rotateOrientation(self, space: int) -> MQuaternion:
        """Returns the MQuaternion which orients the local rotation space."""
    def rotatePivot(self, space: int) -> MPoint:
        """Returns the transform's rotate pivot."""
    def rotatePivotTranslation(self, space: int) -> MVector:
        """Returns the transform's rotate pivot translation."""
    def rotateXYZValue(self, valIndex: int) -> MEulerRotation:
        """Gets the rotation for the active manipulator."""
    def rotation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotation as an MEulerRotation or MQuaternion."""
    def rotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotation as the individual components of an MEulerRotation or MQuaternion."""
    def rotationOrder(self) -> int:
        """Returns the order of rotations when the transform's rotation is expressed as an MEulerRotation."""
    def scale(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transform's XYZ scale components."""
    def scaleBy(self) -> None:
        """Multiplies the transform's XYZ scale components by a sequence of three floats."""
    def scalePivot(self, space: int) -> MPoint:
        """Returns the transform's scale pivot."""
    def scalePivotTranslation(self, space: int) -> MVector:
        """Returns the transform's scale pivot translation."""
    def setAffectsAnimation(self) -> None:
        """Specifies that modifications to a node could potentially affect the animation."""
    def setAlias(self, alias: Any, name: Any, plug: MPlug, add: bool | None = None) -> bool:
        """Adds or removes an attribute alias."""
    def setDirection(self, direction: Any) -> MFnDirectionManip:
        """Sets the direction of the DirectionManip."""
    def setDoNotWrite(self, flag: bool) -> None:
        """Used to prevent the node from being written to file."""
    @staticmethod
    def setDrawPlaneHandles(bool: bool) -> None:
        """Sets the global option to display planar handles or not on supported manipulators."""
    def setDrawStart(self, bool: bool) -> MFnDirectionManip:
        """Sets whether or not to draw the start of the DirectionManip."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> None:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> None:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> None:
        """Sets the state of the specified node flag."""
    @staticmethod
    def setGlobalSize(float: float) -> None:
        """Sets the global manipulator size."""
    @staticmethod
    def setHandleSize(float: float) -> None:
        """Sets the manipulator handle size."""
    def setLimit(self, type: int, value: float) -> None:
        """Sets the value of the specified limit."""
    @staticmethod
    def setLineSize(float: float) -> None:
        """Sets the manipulator line size."""
    def setName(self, name: Any, createNamespace: bool | None = None) -> Any:
        """Sets the node's name."""
    def setNormalizeDirection(self, bool: bool) -> MFnDirectionManip:
        """Sets whether or not to the direction should be normalized."""
    def setObject(self, arg: MDagPath | MObject) -> MFnDirectionManip:
        """Attaches the function set to the specified node or DAG path."""
    def setRestPosition(self, matrix: MTransformationMatrix) -> None:
        """Sets the transform's rest position matrix."""
    def setRotateOrientation(self, quat: MQuaternion, space: int, balance: bool) -> None:
        """Sets the MQuaternion which orients the local rotation space."""
    def setRotatePivot(self, point: MPoint, space: int, balance: bool) -> None:
        """Sets the transform's rotate pivot."""
    def setRotatePivotTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's rotate pivot translation."""
    def setRotation(self, quaternion: MQuaternion | MEulerRotation | int, Space: int | None = None) -> None:
        """Sets the transform's rotation using an MEulerRotation or MQuaternion."""
    def setRotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""
    def setRotationOrder(self, order: int, reorder: bool) -> None:
        """Sets the transform's rotation order."""
    def setScale(self) -> None:
        """Sets the transform's scale components."""
    def setScalePivot(self, point: MPoint, space: int, balance: bool) -> None:
        """Sets the transform's scale pivot."""
    def setScalePivotTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's scale pivot translation."""
    def setShear(self) -> None:
        """Sets the transform's shear."""
    def setStartPoint(self, startPoint: Any) -> MFnDirectionManip:
        """Sets the start point of the DirectionManip."""
    def setTransformation(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's attribute values to represent the given transformation matrix."""
    def setTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's translation."""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def shear(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transform's shear components."""
    def shearBy(self) -> None:
        """Multiplies the transform's shear components by a sequence of three floats."""
    def startPointIndex(self) -> int:
        """Returns the index of the start point of the DirectionManip. The data type corresponding to this index is MFnNumericData.k3Double."""
    def transformation(self) -> MTransformationMatrix:
        """Returns the transformation matrix represented by this transform."""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
    def translateBy(self, vec: MVector, space: int) -> None:
        """Adds an MVector to the transform's translation."""
    def translation(self, Space: int) -> MVector:
        """Returns the transform's translation as an MVector."""
    def type(self) -> int:
        """Returns the type of the function set."""
    def uniqueName(self) -> Any:
        """For a DAG node, the unique name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself. For a non-DAG node, the uniqueName is just its name."""
    def userNode(self) -> MPxNode:
        """Returns the MPxNode object for a plugin node."""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnDiscManip:
    boundingBox: Any
    inModel: Any
    inUnderWorld: Any
    isDefaultNode: Any
    isFromReferencedFile: Any
    isInstanceable: Any
    isIntermediateObject: Any
    isLocked: Any
    isOptimizePlaybackOn: Any
    isShared: Any
    isVisible: Any
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
    manipScale: Any
    namespace: Any
    objectColor: Any
    objectColorRGB: Any
    objectColorType: Any
    pluginName: Any
    typeId: Any
    typeName: Any
    useObjectColor: Any
    def __init__(self, object: MObject | MDagPath | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def absoluteName(self) -> Any:
        """Returns the absolute name of this node.  The absolute name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself.  Regardless of relative name mode, absoluteName() will always return a full namespace path prefixed with a leading colon (the root namespace).  If the underlying node is a DAG node, then absoluteName() does not guarantee uniqueness, that is, two dependency nodes could have the same absoluteName().  In cases like this the uniqueName() method will guarantee that the name uniquely identifies the node."""
    def addAttribute(self, attr: MObject, type: Any) -> None:
        """Adds a new dynamic attribute to the node."""
    def addChild(self, node: int, index: bool, keepExistingParents: bool = False) -> MFnDiscManip:
        """Makes a node a child of this one."""
    def addExternalContentForFileAttr(self, attr: MObject) -> MExternalContentInfoTable:
        """Adds content info to the specified table from a file path attribute."""
    def affectsAnimation(self) -> bool:
        """Returns true if the changes to the node may affect animation."""
    @staticmethod
    def allocateFlag(pluginName: Any) -> int:
        """Allocates a flag on all nodes for use by the named plugin and returns the flag's index."""
    def angleIndex(self) -> int:
        """Returns the index of the angle. The data type corresponding to this index is a double."""
    def attribute(self, index: Any) -> MObject:
        """Returns an attribute of the node, given either its index or name."""
    def attributeClass(self, attr: MObject) -> Any:
        """Returns the class of the specified attribute."""
    def attributeCount(self) -> int:
        """Returns the number of attributes on the node."""
    def axisIndex(self) -> int:
        """Returns the index of the axis of the DiscManip. The data type corresponding to this index is MFnNumericData.k3Double."""
    @staticmethod
    def balanceTransformation(identity: int, identity_: int, one: int, kXYZ: int, arg: Any = None) -> None:
        """Balance a transformation when applying a world matrix to a joint. Thisaccesses the same underlying functionality as the xform command."""
    def canBeWritten(self) -> bool:
        """Returns true if the node will be written to file."""
    def centerIndex(self) -> int:
        """Returns the index of the center of the DiscManip. The data type corresponding to this index is MFnNumericData.k3Double."""
    def child(self, index: int) -> MObject:
        """Returns the specified child of this node."""
    def childCount(self) -> int:
        """Returns the number of nodes which are children of this one."""
    @staticmethod
    def classification(nodeTypeName: Any) -> Any:
        """Returns the classification string for the named node type."""
    def clearRestPosition(self) -> None:
        """Clears the transform's rest position matrix."""
    def connectToAnglePlug(self, directionPlug: Any) -> MFnDiscManip:
        """Connect to the angle plug. The data type corresponding to the anglePlug is a double. (Note that MFnUnitAttribute.kAngle is used to specify an angle attribute.)"""
    def create(self, manipName: Any = None, angleName: Any = None) -> MObject:
        """Creates a new DiscManip."""
    def dagPath(self) -> MDagPath:
        """Returns the DAG path to which this function set is attached. Raises a TypeError if the function set is attached to an MObject rather than a path."""
    def dagRoot(self) -> MObject:
        """Returns the root node of the first path leading to this node."""
    @staticmethod
    def deallocateAllFlags(pluginName: Any) -> None:
        """Deallocates all node flags which are currently allocated to the named plugin."""
    @staticmethod
    def deallocateFlag(pluginName: Any, flag: int) -> None:
        """Deallocates the specified node flag, which was previously allocated by the named plugin using allocateFlag()."""
    @staticmethod
    def deleteManipulator(manip: Any) -> None:
        """Delete a manipulator.  This method should be used to delete manipulators that have been created using base manipulator create() methods."""
    def dgCallbackIds(self, type: Any, callbackName: Any) -> tuple[Any]:
        """Returns DG timing information for a specific callback type, broken down by callbackId."""
    def dgCallbacks(self, type: Any) -> tuple[Any]:
        """Returns DG timing information broken down by callback type."""
    def dgTimer(self, timerMetric: Any, timerType: Any) -> float:
        """Returns a specific DG timer metric for a given timer type."""
    def dgTimerOff(self) -> None:
        """Turns DG timing off for this node."""
    def dgTimerOn(self) -> None:
        """Turns DG timing on for this node."""
    def dgTimerQueryState(self) -> Any:
        """Returns the current DG timer state for this node."""
    def dgTimerReset(self) -> None:
        """Resets all DG timers for this node."""
    @staticmethod
    def drawPlaneHandles() -> bool:
        """This method returns the global option that says if the planar manipulator handles should be drawn or not.Setting this will affect the drawing of all manipulators that support the planar handles."""
    def duplicate(self, instance: bool = False, instanceLeaf: bool = False) -> MObject:
        """Duplicates the DAG hierarchy rooted at the current node."""
    def enableLimit(self, type: int, flag: bool) -> None:
        """Enables or disables a specified limit type."""
    def findAlias(self, alias: Any, attrObj: MObject) -> bool:
        """Returns the attribute which has the given alias."""
    def findPlug(self, attr: Any, wantNetworkedPlug: bool) -> MPlug:
        """Returns a plug for the given attribute."""
    def fullPathName(self) -> Any:
        """Returns the full path of the attached object, from the root of the DAG on down."""
    def getAffectedAttributes(self, attr: MObject) -> MObjectArray:
        """Returns all of the attributes which are affected by the specified attribute."""
    def getAffectingAttributes(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all of the attributes which affect the specified attribute."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute aliases."""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns all of the node's attribute aliases."""
    def getAllPaths(self) -> MDagPathArray:
        """Returns all of the DAG paths which lead to the object to which this function set is attached."""
    def getConnectedSetsAndMembers(self, instance: int, arg: bool, MObjectArray: Any) -> Any:
        """Returns a tuple containing an array of sets and an array of the"""
    def getConnections(self) -> MPlugArray:
        """Returns all the plugs which are connected to attributes of this node."""
    def getExternalContent(self) -> MExternalContentInfoTable:
        """Gets the external content (files) that this node depends on."""
    def getPath(self) -> MDagPath:
        """Returns the DAG path to which this function set is attached, or the first path to the node if the function set is attached to an MObject."""
    @staticmethod
    def globalSize() -> float:
        """Returns the global manipulator size."""
    @staticmethod
    def handleSize() -> float:
        """Returns the manipulator handle size."""
    def hasAttribute(self, name: Any) -> bool:
        """Returns True if the node has an attribute with the given name."""
    def hasChild(self, node: MObject) -> bool:
        """Returns True if the specified node is a child of this one."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def hasParent(self, node: MObject) -> bool:
        """Returns True if the specified node is a parent of this one."""
    def hasUniqueName(self) -> bool:
        """Returns True if the node's name is unique."""
    def instanceCount(self, indirect: bool) -> int:
        """Returns the number of instances for this node."""
    def isChildOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a parent of this one."""
    def isFlagSet(self, flag: int) -> bool:
        """Returns the state of the specified node flag."""
    def isInstanced(self, indirect: bool = True) -> bool:
        """Returns True if this node is instanced."""
    def isInstancedAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute is an instanced attribute of this node."""
    def isLimited(self, type: int) -> bool:
        """Returns True if the specified limit type is enabled."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files."""
    def isParentOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a child of this one."""
    def isTrackingEdits(self) -> bool:
        """Returns True if the node is referenced or in an assembly that is tracking edits."""
    def limitValue(self, type: int) -> float:
        """Returns the value of the specified limit."""
    @staticmethod
    def lineSize() -> float:
        """Returns the manipulator line size."""
    def name(self) -> Any:
        """Returns the node's name."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def parent(self, index: int) -> MObject:
        """Returns the specified parent of this node."""
    def parentCount(self) -> int:
        """Returns the number of parents this node has."""
    def partialPathName(self) -> Any:
        """Returns the minimum path string necessary to uniquely identify the attached object."""
    def plugsAlias(self, plug: MPlug) -> Any:
        """Returns the alias for a plug's attribute."""
    def removeAttribute(self, attr: MObject, type: Any) -> None:
        """Removes a dynamic attribute from the node."""
    def removeChild(self, node: Any) -> MFnDiscManip:
        """Removes the child, specified by MObject, reparenting it under the world."""
    def removeChildAt(self, index: int) -> MFnDiscManip:
        """Removes the child, specified by index, reparenting it under the world."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Returns one of the node's attribute, based on the order in which they are written to file."""
    def resetFromRestPosition(self) -> None:
        """Resets the transform from its rest position matrix."""
    def resetTransformation(self, m: MMatrix) -> None:
        """Resets the transform's attribute values to represent the given transformation matrix in world space."""
    def restPosition(self) -> MTransformationMatrix:
        """Returns the transform's rest position matrix."""
    def rotateBy(self, quaternion: MQuaternion | MEulerRotation | int, Space: int | None = None) -> None:
        """Adds an MEulerRotation or MQuaternion to the transform's rotation."""
    def rotateByComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Adds to the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""
    def rotateOrientation(self, space: int) -> MQuaternion:
        """Returns the MQuaternion which orients the local rotation space."""
    def rotatePivot(self, space: int) -> MPoint:
        """Returns the transform's rotate pivot."""
    def rotatePivotTranslation(self, space: int) -> MVector:
        """Returns the transform's rotate pivot translation."""
    def rotateXYZValue(self, valIndex: int) -> MEulerRotation:
        """Gets the rotation for the active manipulator."""
    def rotation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotation as an MEulerRotation or MQuaternion."""
    def rotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotation as the individual components of an MEulerRotation or MQuaternion."""
    def rotationOrder(self) -> int:
        """Returns the order of rotations when the transform's rotation is expressed as an MEulerRotation."""
    def scale(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transform's XYZ scale components."""
    def scaleBy(self) -> None:
        """Multiplies the transform's XYZ scale components by a sequence of three floats."""
    def scalePivot(self, space: int) -> MPoint:
        """Returns the transform's scale pivot."""
    def scalePivotTranslation(self, space: int) -> MVector:
        """Returns the transform's scale pivot translation."""
    def setAffectsAnimation(self) -> None:
        """Specifies that modifications to a node could potentially affect the animation."""
    def setAlias(self, alias: Any, name: Any, plug: MPlug, add: bool | None = None) -> bool:
        """Adds or removes an attribute alias."""
    def setAngle(self, angle: MAngle) -> MFnDiscManip:
        """Sets the angle of the DiscManip."""
    def setCenterPoint(self, centerPoint: MPoint) -> MFnDiscManip:
        """Sets the center point of the DiscManip."""
    def setDoNotWrite(self, flag: bool) -> None:
        """Used to prevent the node from being written to file."""
    @staticmethod
    def setDrawPlaneHandles(bool: bool) -> None:
        """Sets the global option to display planar handles or not on supported manipulators."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> None:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> None:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> None:
        """Sets the state of the specified node flag."""
    @staticmethod
    def setGlobalSize(float: float) -> None:
        """Sets the global manipulator size."""
    @staticmethod
    def setHandleSize(float: float) -> None:
        """Sets the manipulator handle size."""
    def setLimit(self, type: int, value: float) -> None:
        """Sets the value of the specified limit."""
    @staticmethod
    def setLineSize(float: float) -> None:
        """Sets the manipulator line size."""
    def setName(self, name: Any, createNamespace: bool | None = None) -> Any:
        """Sets the node's name."""
    def setNormal(self, normal: MVector) -> MFnDiscManip:
        """Sets the normal of the DiscManip."""
    def setObject(self, arg: MDagPath | MObject) -> MFnDiscManip:
        """Attaches the function set to the specified node or DAG path."""
    def setRadius(self, radius: float) -> MFnDiscManip:
        """Sets the radius of the DiscManip."""
    def setRestPosition(self, matrix: MTransformationMatrix) -> None:
        """Sets the transform's rest position matrix."""
    def setRotateOrientation(self, quat: MQuaternion, space: int, balance: bool) -> None:
        """Sets the MQuaternion which orients the local rotation space."""
    def setRotatePivot(self, point: MPoint, space: int, balance: bool) -> None:
        """Sets the transform's rotate pivot."""
    def setRotatePivotTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's rotate pivot translation."""
    def setRotation(self, quaternion: MQuaternion | MEulerRotation | int, Space: int | None = None) -> None:
        """Sets the transform's rotation using an MEulerRotation or MQuaternion."""
    def setRotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""
    def setRotationOrder(self, order: int, reorder: bool) -> None:
        """Sets the transform's rotation order."""
    def setScale(self) -> None:
        """Sets the transform's scale components."""
    def setScalePivot(self, point: MPoint, space: int, balance: bool) -> None:
        """Sets the transform's scale pivot."""
    def setScalePivotTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's scale pivot translation."""
    def setShear(self) -> None:
        """Sets the transform's shear."""
    def setTransformation(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's attribute values to represent the given transformation matrix."""
    def setTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's translation."""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def shear(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transform's shear components."""
    def shearBy(self) -> None:
        """Multiplies the transform's shear components by a sequence of three floats."""
    def transformation(self) -> MTransformationMatrix:
        """Returns the transformation matrix represented by this transform."""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
    def translateBy(self, vec: MVector, space: int) -> None:
        """Adds an MVector to the transform's translation."""
    def translation(self, Space: int) -> MVector:
        """Returns the transform's translation as an MVector."""
    def type(self) -> int:
        """Returns the type of the function set."""
    def uniqueName(self) -> Any:
        """For a DAG node, the unique name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself. For a non-DAG node, the uniqueName is just its name."""
    def userNode(self) -> MPxNode:
        """Returns the MPxNode object for a plugin node."""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnDistanceManip:
    boundingBox: Any
    inModel: Any
    inUnderWorld: Any
    isDefaultNode: Any
    isDrawLineOn: Any
    isDrawStartOn: Any
    isFromReferencedFile: Any
    isInstanceable: Any
    isIntermediateObject: Any
    isLocked: Any
    isOptimizePlaybackOn: Any
    isShared: Any
    isVisible: Any
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
    manipScale: Any
    namespace: Any
    objectColor: Any
    objectColorRGB: Any
    objectColorType: Any
    pluginName: Any
    scalingFactor: Any
    typeId: Any
    typeName: Any
    useObjectColor: Any
    def __init__(self, object: MObject | MDagPath | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def absoluteName(self) -> Any:
        """Returns the absolute name of this node.  The absolute name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself.  Regardless of relative name mode, absoluteName() will always return a full namespace path prefixed with a leading colon (the root namespace).  If the underlying node is a DAG node, then absoluteName() does not guarantee uniqueness, that is, two dependency nodes could have the same absoluteName().  In cases like this the uniqueName() method will guarantee that the name uniquely identifies the node."""
    def addAttribute(self, attr: MObject, type: Any) -> None:
        """Adds a new dynamic attribute to the node."""
    def addChild(self, node: int, index: bool, keepExistingParents: bool = False) -> MFnDistanceManip:
        """Makes a node a child of this one."""
    def addExternalContentForFileAttr(self, attr: MObject) -> MExternalContentInfoTable:
        """Adds content info to the specified table from a file path attribute."""
    def affectsAnimation(self) -> bool:
        """Returns true if the changes to the node may affect animation."""
    @staticmethod
    def allocateFlag(pluginName: Any) -> int:
        """Allocates a flag on all nodes for use by the named plugin and returns the flag's index."""
    def attribute(self, index: Any) -> MObject:
        """Returns an attribute of the node, given either its index or name."""
    def attributeClass(self, attr: MObject) -> Any:
        """Returns the class of the specified attribute."""
    def attributeCount(self) -> int:
        """Returns the number of attributes on the node."""
    @staticmethod
    def balanceTransformation(identity: int, identity_: int, one: int, kXYZ: int, arg: Any = None) -> None:
        """Balance a transformation when applying a world matrix to a joint. Thisaccesses the same underlying functionality as the xform command."""
    def canBeWritten(self) -> bool:
        """Returns true if the node will be written to file."""
    def child(self, index: int) -> MObject:
        """Returns the specified child of this node."""
    def childCount(self) -> int:
        """Returns the number of nodes which are children of this one."""
    @staticmethod
    def classification(nodeTypeName: Any) -> Any:
        """Returns the classification string for the named node type."""
    def clearRestPosition(self) -> None:
        """Clears the transform's rest position matrix."""
    def connectToDistancePlug(self, directionPlug: Any) -> MFnDistanceManip:
        """Connect to the distance plug. The data type corresponding to the distancePlug is a double. (Note that MFnUnitAttribute.kDistance is used to specify a distance attribute.)"""
    def create(self, manipName: Any = None, distanceName: Any = None) -> MObject:
        """Creates a new DistanceManip."""
    def currentPointIndex(self) -> int:
        """Returns the index of the current point of the DistanceManip. The data type corresponding to this index is MFnNumericData.k3Double."""
    def dagPath(self) -> MDagPath:
        """Returns the DAG path to which this function set is attached. Raises a TypeError if the function set is attached to an MObject rather than a path."""
    def dagRoot(self) -> MObject:
        """Returns the root node of the first path leading to this node."""
    @staticmethod
    def deallocateAllFlags(pluginName: Any) -> None:
        """Deallocates all node flags which are currently allocated to the named plugin."""
    @staticmethod
    def deallocateFlag(pluginName: Any, flag: int) -> None:
        """Deallocates the specified node flag, which was previously allocated by the named plugin using allocateFlag()."""
    @staticmethod
    def deleteManipulator(manip: Any) -> None:
        """Delete a manipulator.  This method should be used to delete manipulators that have been created using base manipulator create() methods."""
    def dgCallbackIds(self, type: Any, callbackName: Any) -> tuple[Any]:
        """Returns DG timing information for a specific callback type, broken down by callbackId."""
    def dgCallbacks(self, type: Any) -> tuple[Any]:
        """Returns DG timing information broken down by callback type."""
    def dgTimer(self, timerMetric: Any, timerType: Any) -> float:
        """Returns a specific DG timer metric for a given timer type."""
    def dgTimerOff(self) -> None:
        """Turns DG timing off for this node."""
    def dgTimerOn(self) -> None:
        """Turns DG timing on for this node."""
    def dgTimerQueryState(self) -> Any:
        """Returns the current DG timer state for this node."""
    def dgTimerReset(self) -> None:
        """Resets all DG timers for this node."""
    def directionIndex(self) -> int:
        """Returns the index of the direction. The data type corresponding to this index is MFnNumericData.k3Double."""
    def distanceIndex(self) -> int:
        """Returns the index of the distance. The data type corresponding to this index is a double."""
    @staticmethod
    def drawPlaneHandles() -> bool:
        """This method returns the global option that says if the planar manipulator handles should be drawn or not.Setting this will affect the drawing of all manipulators that support the planar handles."""
    def duplicate(self, instance: bool = False, instanceLeaf: bool = False) -> MObject:
        """Duplicates the DAG hierarchy rooted at the current node."""
    def enableLimit(self, type: int, flag: bool) -> None:
        """Enables or disables a specified limit type."""
    def findAlias(self, alias: Any, attrObj: MObject) -> bool:
        """Returns the attribute which has the given alias."""
    def findPlug(self, attr: Any, wantNetworkedPlug: bool) -> MPlug:
        """Returns a plug for the given attribute."""
    def fullPathName(self) -> Any:
        """Returns the full path of the attached object, from the root of the DAG on down."""
    def getAffectedAttributes(self, attr: MObject) -> MObjectArray:
        """Returns all of the attributes which are affected by the specified attribute."""
    def getAffectingAttributes(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all of the attributes which affect the specified attribute."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute aliases."""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns all of the node's attribute aliases."""
    def getAllPaths(self) -> MDagPathArray:
        """Returns all of the DAG paths which lead to the object to which this function set is attached."""
    def getConnectedSetsAndMembers(self, instance: int, arg: bool, MObjectArray: Any) -> Any:
        """Returns a tuple containing an array of sets and an array of the"""
    def getConnections(self) -> MPlugArray:
        """Returns all the plugs which are connected to attributes of this node."""
    def getExternalContent(self) -> MExternalContentInfoTable:
        """Gets the external content (files) that this node depends on."""
    def getPath(self) -> MDagPath:
        """Returns the DAG path to which this function set is attached, or the first path to the node if the function set is attached to an MObject."""
    @staticmethod
    def globalSize() -> float:
        """Returns the global manipulator size."""
    @staticmethod
    def handleSize() -> float:
        """Returns the manipulator handle size."""
    def hasAttribute(self, name: Any) -> bool:
        """Returns True if the node has an attribute with the given name."""
    def hasChild(self, node: MObject) -> bool:
        """Returns True if the specified node is a child of this one."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def hasParent(self, node: MObject) -> bool:
        """Returns True if the specified node is a parent of this one."""
    def hasUniqueName(self) -> bool:
        """Returns True if the node's name is unique."""
    def instanceCount(self, indirect: bool) -> int:
        """Returns the number of instances for this node."""
    def isChildOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a parent of this one."""
    def isFlagSet(self, flag: int) -> bool:
        """Returns the state of the specified node flag."""
    def isInstanced(self, indirect: bool = True) -> bool:
        """Returns True if this node is instanced."""
    def isInstancedAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute is an instanced attribute of this node."""
    def isLimited(self, type: int) -> bool:
        """Returns True if the specified limit type is enabled."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files."""
    def isParentOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a child of this one."""
    def isTrackingEdits(self) -> bool:
        """Returns True if the node is referenced or in an assembly that is tracking edits."""
    def limitValue(self, type: int) -> float:
        """Returns the value of the specified limit."""
    @staticmethod
    def lineSize() -> float:
        """Returns the manipulator line size."""
    def name(self) -> Any:
        """Returns the node's name."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def parent(self, index: int) -> MObject:
        """Returns the specified parent of this node."""
    def parentCount(self) -> int:
        """Returns the number of parents this node has."""
    def partialPathName(self) -> Any:
        """Returns the minimum path string necessary to uniquely identify the attached object."""
    def plugsAlias(self, plug: MPlug) -> Any:
        """Returns the alias for a plug's attribute."""
    def removeAttribute(self, attr: MObject, type: Any) -> None:
        """Removes a dynamic attribute from the node."""
    def removeChild(self, node: Any) -> MFnDistanceManip:
        """Removes the child, specified by MObject, reparenting it under the world."""
    def removeChildAt(self, index: int) -> MFnDistanceManip:
        """Removes the child, specified by index, reparenting it under the world."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Returns one of the node's attribute, based on the order in which they are written to file."""
    def resetFromRestPosition(self) -> None:
        """Resets the transform from its rest position matrix."""
    def resetTransformation(self, m: MMatrix) -> None:
        """Resets the transform's attribute values to represent the given transformation matrix in world space."""
    def restPosition(self) -> MTransformationMatrix:
        """Returns the transform's rest position matrix."""
    def rotateBy(self, quaternion: MQuaternion | MEulerRotation | int, Space: int | None = None) -> None:
        """Adds an MEulerRotation or MQuaternion to the transform's rotation."""
    def rotateByComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Adds to the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""
    def rotateOrientation(self, space: int) -> MQuaternion:
        """Returns the MQuaternion which orients the local rotation space."""
    def rotatePivot(self, space: int) -> MPoint:
        """Returns the transform's rotate pivot."""
    def rotatePivotTranslation(self, space: int) -> MVector:
        """Returns the transform's rotate pivot translation."""
    def rotateXYZValue(self, valIndex: int) -> MEulerRotation:
        """Gets the rotation for the active manipulator."""
    def rotation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotation as an MEulerRotation or MQuaternion."""
    def rotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotation as the individual components of an MEulerRotation or MQuaternion."""
    def rotationOrder(self) -> int:
        """Returns the order of rotations when the transform's rotation is expressed as an MEulerRotation."""
    def scale(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transform's XYZ scale components."""
    def scaleBy(self) -> None:
        """Multiplies the transform's XYZ scale components by a sequence of three floats."""
    def scalePivot(self, space: int) -> MPoint:
        """Returns the transform's scale pivot."""
    def scalePivotTranslation(self, space: int) -> MVector:
        """Returns the transform's scale pivot translation."""
    def setAffectsAnimation(self) -> None:
        """Specifies that modifications to a node could potentially affect the animation."""
    def setAlias(self, alias: Any, name: Any, plug: MPlug, add: bool | None = None) -> bool:
        """Adds or removes an attribute alias."""
    def setDirection(self, direction: MVector) -> MFnDistanceManip:
        """Sets the direction of the DistanceManip."""
    def setDoNotWrite(self, flag: bool) -> None:
        """Used to prevent the node from being written to file."""
    @staticmethod
    def setDrawPlaneHandles(bool: bool) -> None:
        """Sets the global option to display planar handles or not on supported manipulators."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> None:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> None:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> None:
        """Sets the state of the specified node flag."""
    @staticmethod
    def setGlobalSize(float: float) -> None:
        """Sets the global manipulator size."""
    @staticmethod
    def setHandleSize(float: float) -> None:
        """Sets the manipulator handle size."""
    def setLimit(self, type: int, value: float) -> None:
        """Sets the value of the specified limit."""
    @staticmethod
    def setLineSize(float: float) -> None:
        """Sets the manipulator line size."""
    def setName(self, name: Any, createNamespace: bool | None = None) -> Any:
        """Sets the node's name."""
    def setObject(self, arg: MDagPath | MObject) -> MFnDistanceManip:
        """Attaches the function set to the specified node or DAG path."""
    def setRestPosition(self, matrix: MTransformationMatrix) -> None:
        """Sets the transform's rest position matrix."""
    def setRotateOrientation(self, quat: MQuaternion, space: int, balance: bool) -> None:
        """Sets the MQuaternion which orients the local rotation space."""
    def setRotatePivot(self, point: MPoint, space: int, balance: bool) -> None:
        """Sets the transform's rotate pivot."""
    def setRotatePivotTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's rotate pivot translation."""
    def setRotation(self, quaternion: MQuaternion | MEulerRotation | int, Space: int | None = None) -> None:
        """Sets the transform's rotation using an MEulerRotation or MQuaternion."""
    def setRotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""
    def setRotationOrder(self, order: int, reorder: bool) -> None:
        """Sets the transform's rotation order."""
    def setScale(self) -> None:
        """Sets the transform's scale components."""
    def setScalePivot(self, point: MPoint, space: int, balance: bool) -> None:
        """Sets the transform's scale pivot."""
    def setScalePivotTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's scale pivot translation."""
    def setShear(self) -> None:
        """Sets the transform's shear."""
    def setStartPoint(self, startPoint: MPoint) -> MFnDistanceManip:
        """Sets the start point of the DistanceManip."""
    def setTransformation(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's attribute values to represent the given transformation matrix."""
    def setTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's translation."""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def shear(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transform's shear components."""
    def shearBy(self) -> None:
        """Multiplies the transform's shear components by a sequence of three floats."""
    def startPointIndex(self) -> int:
        """Returns the index of the start point of the DistanceManip. The data type corresponding to this index is MFnNumericData.k3Double."""
    def transformation(self) -> MTransformationMatrix:
        """Returns the transformation matrix represented by this transform."""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
    def translateBy(self, vec: MVector, space: int) -> None:
        """Adds an MVector to the transform's translation."""
    def translation(self, Space: int) -> MVector:
        """Returns the transform's translation as an MVector."""
    def type(self) -> int:
        """Returns the type of the function set."""
    def uniqueName(self) -> Any:
        """For a DAG node, the unique name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself. For a non-DAG node, the uniqueName is just its name."""
    def userNode(self) -> MPxNode:
        """Returns the MPxNode object for a plugin node."""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnFreePointTriadManip:
    boundingBox: Any
    inModel: Any
    inUnderWorld: Any
    isDefaultNode: Any
    isDrawAxesOn: Any
    isFromReferencedFile: Any
    isInstanceable: Any
    isIntermediateObject: Any
    isKeyframeAllOn: Any
    isLocked: Any
    isOptimizePlaybackOn: Any
    isShared: Any
    isSnapModeOn: Any
    isVisible: Any
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
    kViewPlane: Any
    kXYPlane: Any
    kXZPlane: Any
    kYZPlane: Any
    manipScale: Any
    namespace: Any
    objectColor: Any
    objectColorRGB: Any
    objectColorType: Any
    pluginName: Any
    typeId: Any
    typeName: Any
    useObjectColor: Any
    def __init__(self, object: MObject | MDagPath | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def absoluteName(self) -> Any:
        """Returns the absolute name of this node.  The absolute name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself.  Regardless of relative name mode, absoluteName() will always return a full namespace path prefixed with a leading colon (the root namespace).  If the underlying node is a DAG node, then absoluteName() does not guarantee uniqueness, that is, two dependency nodes could have the same absoluteName().  In cases like this the uniqueName() method will guarantee that the name uniquely identifies the node."""
    def addAttribute(self, attr: MObject, type: Any) -> None:
        """Adds a new dynamic attribute to the node."""
    def addChild(self, node: int, index: bool, keepExistingParents: bool = False) -> MFnFreePointTriadManip:
        """Makes a node a child of this one."""
    def addExternalContentForFileAttr(self, attr: MObject) -> MExternalContentInfoTable:
        """Adds content info to the specified table from a file path attribute."""
    def affectsAnimation(self) -> bool:
        """Returns true if the changes to the node may affect animation."""
    @staticmethod
    def allocateFlag(pluginName: Any) -> int:
        """Allocates a flag on all nodes for use by the named plugin and returns the flag's index."""
    def attribute(self, index: Any) -> MObject:
        """Returns an attribute of the node, given either its index or name."""
    def attributeClass(self, attr: MObject) -> Any:
        """Returns the class of the specified attribute."""
    def attributeCount(self) -> int:
        """Returns the number of attributes on the node."""
    @staticmethod
    def balanceTransformation(identity: int, identity_: int, one: int, kXYZ: int, arg: Any = None) -> None:
        """Balance a transformation when applying a world matrix to a joint. Thisaccesses the same underlying functionality as the xform command."""
    def canBeWritten(self) -> bool:
        """Returns true if the node will be written to file."""
    def child(self, index: int) -> MObject:
        """Returns the specified child of this node."""
    def childCount(self) -> int:
        """Returns the number of nodes which are children of this one."""
    @staticmethod
    def classification(nodeTypeName: Any) -> Any:
        """Returns the classification string for the named node type."""
    def clearRestPosition(self) -> None:
        """Clears the transform's rest position matrix."""
    def connectToPointPlug(self, pointPlug: Any) -> MFnFreePointTriadManip:
        """Connect to the point plug. The data type corresponding to the pointPlug is MFnNumericData.k3Double."""
    def create(self, manipName: Any = None, pointName: Any = None) -> MObject:
        """Creates a new FreePointTriadManip."""
    def dagPath(self) -> MDagPath:
        """Returns the DAG path to which this function set is attached. Raises a TypeError if the function set is attached to an MObject rather than a path."""
    def dagRoot(self) -> MObject:
        """Returns the root node of the first path leading to this node."""
    @staticmethod
    def deallocateAllFlags(pluginName: Any) -> None:
        """Deallocates all node flags which are currently allocated to the named plugin."""
    @staticmethod
    def deallocateFlag(pluginName: Any, flag: int) -> None:
        """Deallocates the specified node flag, which was previously allocated by the named plugin using allocateFlag()."""
    @staticmethod
    def deleteManipulator(manip: Any) -> None:
        """Delete a manipulator.  This method should be used to delete manipulators that have been created using base manipulator create() methods."""
    def dgCallbackIds(self, type: Any, callbackName: Any) -> tuple[Any]:
        """Returns DG timing information for a specific callback type, broken down by callbackId."""
    def dgCallbacks(self, type: Any) -> tuple[Any]:
        """Returns DG timing information broken down by callback type."""
    def dgTimer(self, timerMetric: Any, timerType: Any) -> float:
        """Returns a specific DG timer metric for a given timer type."""
    def dgTimerOff(self) -> None:
        """Turns DG timing off for this node."""
    def dgTimerOn(self) -> None:
        """Turns DG timing on for this node."""
    def dgTimerQueryState(self) -> Any:
        """Returns the current DG timer state for this node."""
    def dgTimerReset(self) -> None:
        """Resets all DG timers for this node."""
    @staticmethod
    def drawPlaneHandles() -> bool:
        """This method returns the global option that says if the planar manipulator handles should be drawn or not.Setting this will affect the drawing of all manipulators that support the planar handles."""
    def duplicate(self, instance: bool = False, instanceLeaf: bool = False) -> MObject:
        """Duplicates the DAG hierarchy rooted at the current node."""
    def enableLimit(self, type: int, flag: bool) -> None:
        """Enables or disables a specified limit type."""
    def findAlias(self, alias: Any, attrObj: MObject) -> bool:
        """Returns the attribute which has the given alias."""
    def findPlug(self, attr: Any, wantNetworkedPlug: bool) -> MPlug:
        """Returns a plug for the given attribute."""
    def fullPathName(self) -> Any:
        """Returns the full path of the attached object, from the root of the DAG on down."""
    def getAffectedAttributes(self, attr: MObject) -> MObjectArray:
        """Returns all of the attributes which are affected by the specified attribute."""
    def getAffectingAttributes(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all of the attributes which affect the specified attribute."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute aliases."""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns all of the node's attribute aliases."""
    def getAllPaths(self) -> MDagPathArray:
        """Returns all of the DAG paths which lead to the object to which this function set is attached."""
    def getConnectedSetsAndMembers(self, instance: int, arg: bool, MObjectArray: Any) -> Any:
        """Returns a tuple containing an array of sets and an array of the"""
    def getConnections(self) -> MPlugArray:
        """Returns all the plugs which are connected to attributes of this node."""
    def getExternalContent(self) -> MExternalContentInfoTable:
        """Gets the external content (files) that this node depends on."""
    def getPath(self) -> MDagPath:
        """Returns the DAG path to which this function set is attached, or the first path to the node if the function set is attached to an MObject."""
    @staticmethod
    def globalSize() -> float:
        """Returns the global manipulator size."""
    @staticmethod
    def handleSize() -> float:
        """Returns the manipulator handle size."""
    def hasAttribute(self, name: Any) -> bool:
        """Returns True if the node has an attribute with the given name."""
    def hasChild(self, node: MObject) -> bool:
        """Returns True if the specified node is a child of this one."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def hasParent(self, node: MObject) -> bool:
        """Returns True if the specified node is a parent of this one."""
    def hasUniqueName(self) -> bool:
        """Returns True if the node's name is unique."""
    def instanceCount(self, indirect: bool) -> int:
        """Returns the number of instances for this node."""
    def isChildOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a parent of this one."""
    def isFlagSet(self, flag: int) -> bool:
        """Returns the state of the specified node flag."""
    def isInstanced(self, indirect: bool = True) -> bool:
        """Returns True if this node is instanced."""
    def isInstancedAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute is an instanced attribute of this node."""
    def isLimited(self, type: int) -> bool:
        """Returns True if the specified limit type is enabled."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files."""
    def isParentOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a child of this one."""
    def isTrackingEdits(self) -> bool:
        """Returns True if the node is referenced or in an assembly that is tracking edits."""
    def limitValue(self, type: int) -> float:
        """Returns the value of the specified limit."""
    @staticmethod
    def lineSize() -> float:
        """Returns the manipulator line size."""
    def name(self) -> Any:
        """Returns the node's name."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def parent(self, index: int) -> MObject:
        """Returns the specified parent of this node."""
    def parentCount(self) -> int:
        """Returns the number of parents this node has."""
    def partialPathName(self) -> Any:
        """Returns the minimum path string necessary to uniquely identify the attached object."""
    def plugsAlias(self, plug: MPlug) -> Any:
        """Returns the alias for a plug's attribute."""
    def pointIndex(self) -> int:
        """Returns the index of the point of the FreePointTriadManip. The data type corresponding to this index is MFnNumericData.k3Double."""
    def removeAttribute(self, attr: MObject, type: Any) -> None:
        """Removes a dynamic attribute from the node."""
    def removeChild(self, node: Any) -> MFnFreePointTriadManip:
        """Removes the child, specified by MObject, reparenting it under the world."""
    def removeChildAt(self, index: int) -> MFnFreePointTriadManip:
        """Removes the child, specified by index, reparenting it under the world."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Returns one of the node's attribute, based on the order in which they are written to file."""
    def resetFromRestPosition(self) -> None:
        """Resets the transform from its rest position matrix."""
    def resetTransformation(self, m: MMatrix) -> None:
        """Resets the transform's attribute values to represent the given transformation matrix in world space."""
    def restPosition(self) -> MTransformationMatrix:
        """Returns the transform's rest position matrix."""
    def rotateBy(self, quaternion: MQuaternion | MEulerRotation | int, Space: int | None = None) -> None:
        """Adds an MEulerRotation or MQuaternion to the transform's rotation."""
    def rotateByComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Adds to the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""
    def rotateOrientation(self, space: int) -> MQuaternion:
        """Returns the MQuaternion which orients the local rotation space."""
    def rotatePivot(self, space: int) -> MPoint:
        """Returns the transform's rotate pivot."""
    def rotatePivotTranslation(self, space: int) -> MVector:
        """Returns the transform's rotate pivot translation."""
    def rotateXYZValue(self, valIndex: int) -> MEulerRotation:
        """Gets the rotation for the active manipulator."""
    def rotation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotation as an MEulerRotation or MQuaternion."""
    def rotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotation as the individual components of an MEulerRotation or MQuaternion."""
    def rotationOrder(self) -> int:
        """Returns the order of rotations when the transform's rotation is expressed as an MEulerRotation."""
    def scale(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transform's XYZ scale components."""
    def scaleBy(self) -> None:
        """Multiplies the transform's XYZ scale components by a sequence of three floats."""
    def scalePivot(self, space: int) -> MPoint:
        """Returns the transform's scale pivot."""
    def scalePivotTranslation(self, space: int) -> MVector:
        """Returns the transform's scale pivot translation."""
    def setAffectsAnimation(self) -> None:
        """Specifies that modifications to a node could potentially affect the animation."""
    def setAlias(self, alias: Any, name: Any, plug: MPlug, add: bool | None = None) -> bool:
        """Adds or removes an attribute alias."""
    def setDirection(self, direction: MVector) -> MFnFreePointTriadManip:
        """Sets the orientation of the FreePointTriadManip."""
    def setDoNotWrite(self, flag: bool) -> None:
        """Used to prevent the node from being written to file."""
    def setDrawArrowHead(self, state: bool) -> MFnFreePointTriadManip:
        """Sets whether or not drawArrowHead is on."""
    @staticmethod
    def setDrawPlaneHandles(bool: bool) -> None:
        """Sets the global option to display planar handles or not on supported manipulators."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> None:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> None:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> None:
        """Sets the state of the specified node flag."""
    @staticmethod
    def setGlobalSize(float: float) -> None:
        """Sets the global manipulator size."""
    def setGlobalTriadPlane(self, whichPlane: Any) -> MFnFreePointTriadManip:
        """Sets which plane to use as the global triad plane. The global triad plane does not change until the context switches."""
    @staticmethod
    def setHandleSize(float: float) -> None:
        """Sets the manipulator handle size."""
    def setLimit(self, type: int, value: float) -> None:
        """Sets the value of the specified limit."""
    @staticmethod
    def setLineSize(float: float) -> None:
        """Sets the manipulator line size."""
    def setName(self, name: Any, createNamespace: bool | None = None) -> Any:
        """Sets the node's name."""
    def setObject(self, arg: MDagPath | MObject) -> MFnFreePointTriadManip:
        """Attaches the function set to the specified node or DAG path."""
    def setPoint(self, pointValue: MPoint) -> MFnFreePointTriadManip:
        """Set the point manipulator value to the given vector.  This method can be called in the MPxManipContainer.connectToDependNode() method to set the initial position for the manipulator."""
    def setRestPosition(self, matrix: MTransformationMatrix) -> None:
        """Sets the transform's rest position matrix."""
    def setRotateOrientation(self, quat: MQuaternion, space: int, balance: bool) -> None:
        """Sets the MQuaternion which orients the local rotation space."""
    def setRotatePivot(self, point: MPoint, space: int, balance: bool) -> None:
        """Sets the transform's rotate pivot."""
    def setRotatePivotTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's rotate pivot translation."""
    def setRotation(self, quaternion: MQuaternion | MEulerRotation | int, Space: int | None = None) -> None:
        """Sets the transform's rotation using an MEulerRotation or MQuaternion."""
    def setRotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""
    def setRotationOrder(self, order: int, reorder: bool) -> None:
        """Sets the transform's rotation order."""
    def setScale(self) -> None:
        """Sets the transform's scale components."""
    def setScalePivot(self, point: MPoint, space: int, balance: bool) -> None:
        """Sets the transform's scale pivot."""
    def setScalePivotTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's scale pivot translation."""
    def setShear(self) -> None:
        """Sets the transform's shear."""
    def setTransformation(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's attribute values to represent the given transformation matrix."""
    def setTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's translation."""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def shear(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transform's shear components."""
    def shearBy(self) -> None:
        """Multiplies the transform's shear components by a sequence of three floats."""
    def transformation(self) -> MTransformationMatrix:
        """Returns the transformation matrix represented by this transform."""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
    def translateBy(self, vec: MVector, space: int) -> None:
        """Adds an MVector to the transform's translation."""
    def translation(self, Space: int) -> MVector:
        """Returns the transform's translation as an MVector."""
    def type(self) -> int:
        """Returns the type of the function set."""
    def uniqueName(self) -> Any:
        """For a DAG node, the unique name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself. For a non-DAG node, the uniqueName is just its name."""
    def userNode(self) -> MPxNode:
        """Returns the MPxNode object for a plugin node."""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnManip3D:
    boundingBox: Any
    inModel: Any
    inUnderWorld: Any
    isDefaultNode: Any
    isFromReferencedFile: Any
    isInstanceable: Any
    isIntermediateObject: Any
    isLocked: Any
    isOptimizePlaybackOn: Any
    isShared: Any
    isVisible: Any
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
    manipScale: Any
    namespace: Any
    objectColor: Any
    objectColorRGB: Any
    objectColorType: Any
    pluginName: Any
    typeId: Any
    typeName: Any
    useObjectColor: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def absoluteName(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the absolute name of this node.  The absolute name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself.  Regardless of relative name mode, absoluteName() will always return a full namespace path prefixed with a leading colon (the root namespace).  If the underlying node is a DAG node, then absoluteName() does not guarantee uniqueness, that is, two dependency nodes could have the same absoluteName().  In cases like this the uniqueName() method will guarantee that the name uniquely identifies the node."""
    def addAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """Adds a new dynamic attribute to the node."""
    def addChild(self, node: Any, index: Any, keepExistingParents: bool = False) -> MFnManip3D:
        """Makes a node a child of this one."""
    def addExternalContentForFileAttr(self, *args: Any, **kwargs: Any) -> Any:
        """Adds content info to the specified table from a file path attribute."""
    def affectsAnimation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns true if the changes to the node may affect animation."""
    @staticmethod
    def allocateFlag(*args: Any, **kwargs: Any) -> Any:
        """Allocates a flag on all nodes for use by the named plugin and returns the flag's index."""
    def attribute(self, *args: Any, **kwargs: Any) -> Any:
        """Returns an attribute of the node, given either its index or name."""
    def attributeClass(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the class of the specified attribute."""
    def attributeCount(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the number of attributes on the node."""
    @staticmethod
    def balanceTransformation(*args: Any, **kwargs: Any) -> Any:
        """Balance a transformation when applying a world matrix to a joint. Thisaccesses the same underlying functionality as the xform command."""
    def canBeWritten(self, *args: Any, **kwargs: Any) -> Any:
        """Returns true if the node will be written to file."""
    def child(self, index: Any) -> MObject:
        """Returns the specified child of this node."""
    def childCount(self) -> int:
        """Returns the number of nodes which are children of this one."""
    @staticmethod
    def classification(*args: Any, **kwargs: Any) -> Any:
        """Returns the classification string for the named node type."""
    def clearRestPosition(self, *args: Any, **kwargs: Any) -> Any:
        """Clears the transform's rest position matrix."""
    def create(self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new transform node and attaches it to the function set."""
    def dagPath(self) -> MDagPath:
        """Returns the DAG path to which this function set is attached. Raises a TypeError if the function set is attached to an MObject rather than a path."""
    def dagRoot(self) -> MObject:
        """Returns the root node of the first path leading to this node."""
    @staticmethod
    def deallocateAllFlags(*args: Any, **kwargs: Any) -> Any:
        """Deallocates all node flags which are currently allocated to the named plugin."""
    @staticmethod
    def deallocateFlag(*args: Any, **kwargs: Any) -> Any:
        """Deallocates the specified node flag, which was previously allocated by the named plugin using allocateFlag()."""
    @staticmethod
    def deleteManipulator(manip: Any) -> None:
        """Delete a manipulator.  This method should be used to delete manipulators that have been created using base manipulator create() methods."""
    def dgCallbackIds(self, *args: Any, **kwargs: Any) -> Any:
        """Returns DG timing information for a specific callback type, broken down by callbackId."""
    def dgCallbacks(self, *args: Any, **kwargs: Any) -> Any:
        """Returns DG timing information broken down by callback type."""
    def dgTimer(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a specific DG timer metric for a given timer type."""
    def dgTimerOff(self, *args: Any, **kwargs: Any) -> Any:
        """Turns DG timing off for this node."""
    def dgTimerOn(self, *args: Any, **kwargs: Any) -> Any:
        """Turns DG timing on for this node."""
    def dgTimerQueryState(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the current DG timer state for this node."""
    def dgTimerReset(self, *args: Any, **kwargs: Any) -> Any:
        """Resets all DG timers for this node."""
    @staticmethod
    def drawPlaneHandles() -> bool:
        """This method returns the global option that says if the planar manipulator handles should be drawn or not.Setting this will affect the drawing of all manipulators that support the planar handles."""
    def duplicate(self, instance: bool = False, instanceLeaf: bool = False) -> MObject:
        """Duplicates the DAG hierarchy rooted at the current node."""
    def enableLimit(self, *args: Any, **kwargs: Any) -> Any:
        """Enables or disables a specified limit type."""
    def findAlias(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the attribute which has the given alias."""
    def findPlug(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a plug for the given attribute."""
    def fullPathName(self) -> Any:
        """Returns the full path of the attached object, from the root of the DAG on down."""
    def getAffectedAttributes(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all of the attributes which are affected by the specified attribute."""
    def getAffectingAttributes(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all of the attributes which affect the specified attribute."""
    def getAliasAttr(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute aliases."""
    def getAliasList(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all of the node's attribute aliases."""
    def getAllPaths(self) -> MDagPathArray:
        """Returns all of the DAG paths which lead to the object to which this function set is attached."""
    def getConnectedSetsAndMembers(self, instance: Any, arg: Any, MObjectArray: Any) -> Any:
        """Returns a tuple containing an array of sets and an array of the"""
    def getConnections(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all the plugs which are connected to attributes of this node."""
    def getExternalContent(self, *args: Any, **kwargs: Any) -> Any:
        """Gets the external content (files) that this node depends on."""
    def getPath(self) -> MDagPath:
        """Returns the DAG path to which this function set is attached, or the first path to the node if the function set is attached to an MObject."""
    @staticmethod
    def globalSize() -> float:
        """Returns the global manipulator size."""
    @staticmethod
    def handleSize() -> float:
        """Returns the manipulator handle size."""
    def hasAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the node has an attribute with the given name."""
    def hasChild(self, node: Any) -> bool:
        """Returns True if the specified node is a child of this one."""
    def hasObj(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the function set is compatible with the specified Maya object."""
    def hasParent(self, node: Any) -> bool:
        """Returns True if the specified node is a parent of this one."""
    def hasUniqueName(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the node's name is unique."""
    def instanceCount(self, indirect: Any) -> int:
        """Returns the number of instances for this node."""
    def isChildOf(self, node: Any) -> bool:
        """Returns True if the specified node is a parent of this one."""
    def isFlagSet(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the state of the specified node flag."""
    def isInstanced(self, indirect: bool = True) -> bool:
        """Returns True if this node is instanced."""
    def isInstancedAttribute(self, attr: Any) -> bool:
        """Returns True if the specified attribute is an instanced attribute of this node."""
    def isLimited(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the specified limit type is enabled."""
    def isNewAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files."""
    def isParentOf(self, node: Any) -> bool:
        """Returns True if the specified node is a child of this one."""
    def isTrackingEdits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the node is referenced or in an assembly that is tracking edits."""
    def limitValue(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the value of the specified limit."""
    @staticmethod
    def lineSize() -> float:
        """Returns the manipulator line size."""
    def name(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the node's name."""
    def object(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def parent(self, index: Any) -> MObject:
        """Returns the specified parent of this node."""
    def parentCount(self) -> int:
        """Returns the number of parents this node has."""
    def partialPathName(self) -> Any:
        """Returns the minimum path string necessary to uniquely identify the attached object."""
    def plugsAlias(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the alias for a plug's attribute."""
    def removeAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """Removes a dynamic attribute from the node."""
    def removeChild(self, node: Any) -> MFnManip3D:
        """Removes the child, specified by MObject, reparenting it under the world."""
    def removeChildAt(self, index: Any) -> MFnManip3D:
        """Removes the child, specified by index, reparenting it under the world."""
    def reorderedAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """Returns one of the node's attribute, based on the order in which they are written to file."""
    def resetFromRestPosition(self, *args: Any, **kwargs: Any) -> Any:
        """Resets the transform from its rest position matrix."""
    def resetTransformation(self, *args: Any, **kwargs: Any) -> Any:
        """Resets the transform's attribute values to represent the given transformation matrix in world space."""
    def restPosition(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rest position matrix."""
    def rotateBy(self, *args: Any, **kwargs: Any) -> Any:
        """Adds an MEulerRotation or MQuaternion to the transform's rotation."""
    def rotateByComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Adds to the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""
    def rotateOrientation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the MQuaternion which orients the local rotation space."""
    def rotatePivot(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotate pivot."""
    def rotatePivotTranslation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotate pivot translation."""
    def rotateXYZValue(self, valIndex: Any) -> MEulerRotation:
        """Gets the rotation for the active manipulator."""
    def rotation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotation as an MEulerRotation or MQuaternion."""
    def rotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotation as the individual components of an MEulerRotation or MQuaternion."""
    def rotationOrder(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the order of rotations when the transform's rotation is expressed as an MEulerRotation."""
    def scale(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transform's XYZ scale components."""
    def scaleBy(self, *args: Any, **kwargs: Any) -> Any:
        """Multiplies the transform's XYZ scale components by a sequence of three floats."""
    def scalePivot(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's scale pivot."""
    def scalePivotTranslation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's scale pivot translation."""
    def setAffectsAnimation(self, *args: Any, **kwargs: Any) -> Any:
        """Specifies that modifications to a node could potentially affect the animation."""
    def setAlias(self, *args: Any, **kwargs: Any) -> Any:
        """Adds or removes an attribute alias."""
    def setDoNotWrite(self, *args: Any, **kwargs: Any) -> Any:
        """Used to prevent the node from being written to file."""
    @staticmethod
    def setDrawPlaneHandles(bool: Any) -> None:
        """Sets the global option to display planar handles or not on supported manipulators."""
    def setExternalContent(self, *args: Any, **kwargs: Any) -> Any:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, *args: Any, **kwargs: Any) -> Any:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the state of the specified node flag."""
    @staticmethod
    def setGlobalSize(float: Any) -> None:
        """Sets the global manipulator size."""
    @staticmethod
    def setHandleSize(float: Any) -> None:
        """Sets the manipulator handle size."""
    def setLimit(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the value of the specified limit."""
    @staticmethod
    def setLineSize(float: Any) -> None:
        """Sets the manipulator line size."""
    def setName(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the node's name."""
    def setObject(self, arg: Any) -> MFnManip3D:
        """Attaches the function set to the specified node or DAG path."""
    def setRestPosition(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's rest position matrix."""
    def setRotateOrientation(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the MQuaternion which orients the local rotation space."""
    def setRotatePivot(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's rotate pivot."""
    def setRotatePivotTranslation(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's rotate pivot translation."""
    def setRotation(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's rotation using an MEulerRotation or MQuaternion."""
    def setRotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""
    def setRotationOrder(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's rotation order."""
    def setScale(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's scale components."""
    def setScalePivot(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's scale pivot."""
    def setScalePivotTranslation(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's scale pivot translation."""
    def setShear(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's shear."""
    def setTransformation(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's attribute values to represent the given transformation matrix."""
    def setTranslation(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's translation."""
    def setUuid(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the node's UUID."""
    def shear(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transform's shear components."""
    def shearBy(self, *args: Any, **kwargs: Any) -> Any:
        """Multiplies the transform's shear components by a sequence of three floats."""
    def transformation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transformation matrix represented by this transform."""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
    def translateBy(self, *args: Any, **kwargs: Any) -> Any:
        """Adds an MVector to the transform's translation."""
    def translation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's translation as an MVector."""
    def type(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the type of the function set."""
    def uniqueName(self, *args: Any, **kwargs: Any) -> Any:
        """For a DAG node, the unique name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself. For a non-DAG node, the uniqueName is just its name."""
    def userNode(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the MPxNode object for a plugin node."""
    def uuid(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the node's UUID."""

class MFnPointOnCurveManip:
    boundingBox: Any
    inModel: Any
    inUnderWorld: Any
    isDefaultNode: Any
    isDrawCurveOn: Any
    isFromReferencedFile: Any
    isInstanceable: Any
    isIntermediateObject: Any
    isLocked: Any
    isOptimizePlaybackOn: Any
    isShared: Any
    isVisible: Any
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
    manipScale: Any
    namespace: Any
    objectColor: Any
    objectColorRGB: Any
    objectColorType: Any
    parameter: Any
    pluginName: Any
    typeId: Any
    typeName: Any
    useObjectColor: Any
    def __init__(self, object: MObject | MDagPath | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def absoluteName(self) -> Any:
        """Returns the absolute name of this node.  The absolute name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself.  Regardless of relative name mode, absoluteName() will always return a full namespace path prefixed with a leading colon (the root namespace).  If the underlying node is a DAG node, then absoluteName() does not guarantee uniqueness, that is, two dependency nodes could have the same absoluteName().  In cases like this the uniqueName() method will guarantee that the name uniquely identifies the node."""
    def addAttribute(self, attr: MObject, type: Any) -> None:
        """Adds a new dynamic attribute to the node."""
    def addChild(self, node: int, index: bool, keepExistingParents: bool = False) -> MFnPointOnCurveManip:
        """Makes a node a child of this one."""
    def addExternalContentForFileAttr(self, attr: MObject) -> MExternalContentInfoTable:
        """Adds content info to the specified table from a file path attribute."""
    def affectsAnimation(self) -> bool:
        """Returns true if the changes to the node may affect animation."""
    @staticmethod
    def allocateFlag(pluginName: Any) -> int:
        """Allocates a flag on all nodes for use by the named plugin and returns the flag's index."""
    def attribute(self, index: Any) -> MObject:
        """Returns an attribute of the node, given either its index or name."""
    def attributeClass(self, attr: MObject) -> Any:
        """Returns the class of the specified attribute."""
    def attributeCount(self) -> int:
        """Returns the number of attributes on the node."""
    @staticmethod
    def balanceTransformation(identity: int, identity_: int, one: int, kXYZ: int, arg: Any = None) -> None:
        """Balance a transformation when applying a world matrix to a joint. Thisaccesses the same underlying functionality as the xform command."""
    def canBeWritten(self) -> bool:
        """Returns true if the node will be written to file."""
    def child(self, index: int) -> MObject:
        """Returns the specified child of this node."""
    def childCount(self) -> int:
        """Returns the number of nodes which are children of this one."""
    @staticmethod
    def classification(nodeTypeName: Any) -> Any:
        """Returns the classification string for the named node type."""
    def clearRestPosition(self) -> None:
        """Clears the transform's rest position matrix."""
    def connectToCurvePlug(self, curvePlug: Any) -> MFnPointOnCurveManip:
        """Connect to the curve plug. The data type corresponding to the curvePlug is MFnData::kNurbsCurve."""
    def connectToParamPlug(self, paramPlug: Any) -> MFnPointOnCurveManip:
        """Connect to the param plug. The data type corresponding to the paramPlug is a double."""
    def create(self, manipName: Any = None, paramName: Any = None) -> MObject:
        """Creates a new PointOnCurveManip."""
    def curveIndex(self) -> int:
        """Returns the index of the curve. The data type corresponding to this index is MFnData::kNurbsCurve."""
    def curvePoint(self) -> MPoint:
        """Returns the curve point."""
    def dagPath(self) -> MDagPath:
        """Returns the DAG path to which this function set is attached. Raises a TypeError if the function set is attached to an MObject rather than a path."""
    def dagRoot(self) -> MObject:
        """Returns the root node of the first path leading to this node."""
    @staticmethod
    def deallocateAllFlags(pluginName: Any) -> None:
        """Deallocates all node flags which are currently allocated to the named plugin."""
    @staticmethod
    def deallocateFlag(pluginName: Any, flag: int) -> None:
        """Deallocates the specified node flag, which was previously allocated by the named plugin using allocateFlag()."""
    @staticmethod
    def deleteManipulator(manip: Any) -> None:
        """Delete a manipulator.  This method should be used to delete manipulators that have been created using base manipulator create() methods."""
    def dgCallbackIds(self, type: Any, callbackName: Any) -> tuple[Any]:
        """Returns DG timing information for a specific callback type, broken down by callbackId."""
    def dgCallbacks(self, type: Any) -> tuple[Any]:
        """Returns DG timing information broken down by callback type."""
    def dgTimer(self, timerMetric: Any, timerType: Any) -> float:
        """Returns a specific DG timer metric for a given timer type."""
    def dgTimerOff(self) -> None:
        """Turns DG timing off for this node."""
    def dgTimerOn(self) -> None:
        """Turns DG timing on for this node."""
    def dgTimerQueryState(self) -> Any:
        """Returns the current DG timer state for this node."""
    def dgTimerReset(self) -> None:
        """Resets all DG timers for this node."""
    @staticmethod
    def drawPlaneHandles() -> bool:
        """This method returns the global option that says if the planar manipulator handles should be drawn or not.Setting this will affect the drawing of all manipulators that support the planar handles."""
    def duplicate(self, instance: bool = False, instanceLeaf: bool = False) -> MObject:
        """Duplicates the DAG hierarchy rooted at the current node."""
    def enableLimit(self, type: int, flag: bool) -> None:
        """Enables or disables a specified limit type."""
    def findAlias(self, alias: Any, attrObj: MObject) -> bool:
        """Returns the attribute which has the given alias."""
    def findPlug(self, attr: Any, wantNetworkedPlug: bool) -> MPlug:
        """Returns a plug for the given attribute."""
    def fullPathName(self) -> Any:
        """Returns the full path of the attached object, from the root of the DAG on down."""
    def getAffectedAttributes(self, attr: MObject) -> MObjectArray:
        """Returns all of the attributes which are affected by the specified attribute."""
    def getAffectingAttributes(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all of the attributes which affect the specified attribute."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute aliases."""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns all of the node's attribute aliases."""
    def getAllPaths(self) -> MDagPathArray:
        """Returns all of the DAG paths which lead to the object to which this function set is attached."""
    def getConnectedSetsAndMembers(self, instance: int, arg: bool, MObjectArray: Any) -> Any:
        """Returns a tuple containing an array of sets and an array of the"""
    def getConnections(self) -> MPlugArray:
        """Returns all the plugs which are connected to attributes of this node."""
    def getExternalContent(self) -> MExternalContentInfoTable:
        """Gets the external content (files) that this node depends on."""
    def getPath(self) -> MDagPath:
        """Returns the DAG path to which this function set is attached, or the first path to the node if the function set is attached to an MObject."""
    @staticmethod
    def globalSize() -> float:
        """Returns the global manipulator size."""
    @staticmethod
    def handleSize() -> float:
        """Returns the manipulator handle size."""
    def hasAttribute(self, name: Any) -> bool:
        """Returns True if the node has an attribute with the given name."""
    def hasChild(self, node: MObject) -> bool:
        """Returns True if the specified node is a child of this one."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def hasParent(self, node: MObject) -> bool:
        """Returns True if the specified node is a parent of this one."""
    def hasUniqueName(self) -> bool:
        """Returns True if the node's name is unique."""
    def instanceCount(self, indirect: bool) -> int:
        """Returns the number of instances for this node."""
    def isChildOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a parent of this one."""
    def isFlagSet(self, flag: int) -> bool:
        """Returns the state of the specified node flag."""
    def isInstanced(self, indirect: bool = True) -> bool:
        """Returns True if this node is instanced."""
    def isInstancedAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute is an instanced attribute of this node."""
    def isLimited(self, type: int) -> bool:
        """Returns True if the specified limit type is enabled."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files."""
    def isParentOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a child of this one."""
    def isTrackingEdits(self) -> bool:
        """Returns True if the node is referenced or in an assembly that is tracking edits."""
    def limitValue(self, type: int) -> float:
        """Returns the value of the specified limit."""
    @staticmethod
    def lineSize() -> float:
        """Returns the manipulator line size."""
    def name(self) -> Any:
        """Returns the node's name."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def paramIndex(self) -> int:
        """Returns the index of the parameter of the PointOnCurveManip. The data type corresponding to this index is a double."""
    def parent(self, index: int) -> MObject:
        """Returns the specified parent of this node."""
    def parentCount(self) -> int:
        """Returns the number of parents this node has."""
    def partialPathName(self) -> Any:
        """Returns the minimum path string necessary to uniquely identify the attached object."""
    def plugsAlias(self, plug: MPlug) -> Any:
        """Returns the alias for a plug's attribute."""
    def removeAttribute(self, attr: MObject, type: Any) -> None:
        """Removes a dynamic attribute from the node."""
    def removeChild(self, node: Any) -> MFnPointOnCurveManip:
        """Removes the child, specified by MObject, reparenting it under the world."""
    def removeChildAt(self, index: int) -> MFnPointOnCurveManip:
        """Removes the child, specified by index, reparenting it under the world."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Returns one of the node's attribute, based on the order in which they are written to file."""
    def resetFromRestPosition(self) -> None:
        """Resets the transform from its rest position matrix."""
    def resetTransformation(self, m: MMatrix) -> None:
        """Resets the transform's attribute values to represent the given transformation matrix in world space."""
    def restPosition(self) -> MTransformationMatrix:
        """Returns the transform's rest position matrix."""
    def rotateBy(self, quaternion: MQuaternion | MEulerRotation | int, Space: int | None = None) -> None:
        """Adds an MEulerRotation or MQuaternion to the transform's rotation."""
    def rotateByComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Adds to the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""
    def rotateOrientation(self, space: int) -> MQuaternion:
        """Returns the MQuaternion which orients the local rotation space."""
    def rotatePivot(self, space: int) -> MPoint:
        """Returns the transform's rotate pivot."""
    def rotatePivotTranslation(self, space: int) -> MVector:
        """Returns the transform's rotate pivot translation."""
    def rotateXYZValue(self, valIndex: int) -> MEulerRotation:
        """Gets the rotation for the active manipulator."""
    def rotation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotation as an MEulerRotation or MQuaternion."""
    def rotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotation as the individual components of an MEulerRotation or MQuaternion."""
    def rotationOrder(self) -> int:
        """Returns the order of rotations when the transform's rotation is expressed as an MEulerRotation."""
    def scale(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transform's XYZ scale components."""
    def scaleBy(self) -> None:
        """Multiplies the transform's XYZ scale components by a sequence of three floats."""
    def scalePivot(self, space: int) -> MPoint:
        """Returns the transform's scale pivot."""
    def scalePivotTranslation(self, space: int) -> MVector:
        """Returns the transform's scale pivot translation."""
    def setAffectsAnimation(self) -> None:
        """Specifies that modifications to a node could potentially affect the animation."""
    def setAlias(self, alias: Any, name: Any, plug: MPlug, add: bool | None = None) -> bool:
        """Adds or removes an attribute alias."""
    def setDoNotWrite(self, flag: bool) -> None:
        """Used to prevent the node from being written to file."""
    @staticmethod
    def setDrawPlaneHandles(bool: bool) -> None:
        """Sets the global option to display planar handles or not on supported manipulators."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> None:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> None:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> None:
        """Sets the state of the specified node flag."""
    @staticmethod
    def setGlobalSize(float: float) -> None:
        """Sets the global manipulator size."""
    @staticmethod
    def setHandleSize(float: float) -> None:
        """Sets the manipulator handle size."""
    def setLimit(self, type: int, value: float) -> None:
        """Sets the value of the specified limit."""
    @staticmethod
    def setLineSize(float: float) -> None:
        """Sets the manipulator line size."""
    def setName(self, name: Any, createNamespace: bool | None = None) -> Any:
        """Sets the node's name."""
    def setObject(self, arg: MDagPath | MObject) -> MFnPointOnCurveManip:
        """Attaches the function set to the specified node or DAG path."""
    def setRestPosition(self, matrix: MTransformationMatrix) -> None:
        """Sets the transform's rest position matrix."""
    def setRotateOrientation(self, quat: MQuaternion, space: int, balance: bool) -> None:
        """Sets the MQuaternion which orients the local rotation space."""
    def setRotatePivot(self, point: MPoint, space: int, balance: bool) -> None:
        """Sets the transform's rotate pivot."""
    def setRotatePivotTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's rotate pivot translation."""
    def setRotation(self, quaternion: MQuaternion | MEulerRotation | int, Space: int | None = None) -> None:
        """Sets the transform's rotation using an MEulerRotation or MQuaternion."""
    def setRotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""
    def setRotationOrder(self, order: int, reorder: bool) -> None:
        """Sets the transform's rotation order."""
    def setScale(self) -> None:
        """Sets the transform's scale components."""
    def setScalePivot(self, point: MPoint, space: int, balance: bool) -> None:
        """Sets the transform's scale pivot."""
    def setScalePivotTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's scale pivot translation."""
    def setShear(self) -> None:
        """Sets the transform's shear."""
    def setTransformation(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's attribute values to represent the given transformation matrix."""
    def setTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's translation."""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def shear(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transform's shear components."""
    def shearBy(self) -> None:
        """Multiplies the transform's shear components by a sequence of three floats."""
    def transformation(self) -> MTransformationMatrix:
        """Returns the transformation matrix represented by this transform."""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
    def translateBy(self, vec: MVector, space: int) -> None:
        """Adds an MVector to the transform's translation."""
    def translation(self, Space: int) -> MVector:
        """Returns the transform's translation as an MVector."""
    def type(self) -> int:
        """Returns the type of the function set."""
    def uniqueName(self) -> Any:
        """For a DAG node, the unique name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself. For a non-DAG node, the uniqueName is just its name."""
    def userNode(self) -> MPxNode:
        """Returns the MPxNode object for a plugin node."""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnPointOnSurfaceManip:
    boundingBox: Any
    inModel: Any
    inUnderWorld: Any
    isDefaultNode: Any
    isDrawSurfaceOn: Any
    isFromReferencedFile: Any
    isInstanceable: Any
    isIntermediateObject: Any
    isLocked: Any
    isOptimizePlaybackOn: Any
    isShared: Any
    isVisible: Any
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
    manipScale: Any
    namespace: Any
    objectColor: Any
    objectColorRGB: Any
    objectColorType: Any
    pluginName: Any
    typeId: Any
    typeName: Any
    uParam: Any
    useObjectColor: Any
    vParam: Any
    def __init__(self, object: MObject | MDagPath | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def absoluteName(self) -> Any:
        """Returns the absolute name of this node.  The absolute name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself.  Regardless of relative name mode, absoluteName() will always return a full namespace path prefixed with a leading colon (the root namespace).  If the underlying node is a DAG node, then absoluteName() does not guarantee uniqueness, that is, two dependency nodes could have the same absoluteName().  In cases like this the uniqueName() method will guarantee that the name uniquely identifies the node."""
    def addAttribute(self, attr: MObject, type: Any) -> None:
        """Adds a new dynamic attribute to the node."""
    def addChild(self, node: int, index: bool, keepExistingParents: bool = False) -> MFnPointOnSurfaceManip:
        """Makes a node a child of this one."""
    def addExternalContentForFileAttr(self, attr: MObject) -> MExternalContentInfoTable:
        """Adds content info to the specified table from a file path attribute."""
    def affectsAnimation(self) -> bool:
        """Returns true if the changes to the node may affect animation."""
    @staticmethod
    def allocateFlag(pluginName: Any) -> int:
        """Allocates a flag on all nodes for use by the named plugin and returns the flag's index."""
    def attribute(self, index: Any) -> MObject:
        """Returns an attribute of the node, given either its index or name."""
    def attributeClass(self, attr: MObject) -> Any:
        """Returns the class of the specified attribute."""
    def attributeCount(self) -> int:
        """Returns the number of attributes on the node."""
    @staticmethod
    def balanceTransformation(identity: int, identity_: int, one: int, kXYZ: int, arg: Any = None) -> None:
        """Balance a transformation when applying a world matrix to a joint. Thisaccesses the same underlying functionality as the xform command."""
    def canBeWritten(self) -> bool:
        """Returns true if the node will be written to file."""
    def child(self, index: int) -> MObject:
        """Returns the specified child of this node."""
    def childCount(self) -> int:
        """Returns the number of nodes which are children of this one."""
    @staticmethod
    def classification(nodeTypeName: Any) -> Any:
        """Returns the classification string for the named node type."""
    def clearRestPosition(self) -> None:
        """Clears the transform's rest position matrix."""
    def connectToParamPlug(self, paramPlug: Any) -> MFnPointOnSurfaceManip:
        """Connect to the param plug. The data type corresponding to the paramPlug is MFnNumericData.k2Double."""
    def connectToSurfacePlug(self, surfacePlug: Any) -> MFnPointOnSurfaceManip:
        """Connect to the surface plug. The data type corresponding to the surfacePlug is MFnData.kNurbsSurface."""
    def create(self, manipName: Any = None, paramName: Any = None) -> MObject:
        """Creates a new PointOnSurfaceManip."""
    def dagPath(self) -> MDagPath:
        """Returns the DAG path to which this function set is attached. Raises a TypeError if the function set is attached to an MObject rather than a path."""
    def dagRoot(self) -> MObject:
        """Returns the root node of the first path leading to this node."""
    @staticmethod
    def deallocateAllFlags(pluginName: Any) -> None:
        """Deallocates all node flags which are currently allocated to the named plugin."""
    @staticmethod
    def deallocateFlag(pluginName: Any, flag: int) -> None:
        """Deallocates the specified node flag, which was previously allocated by the named plugin using allocateFlag()."""
    @staticmethod
    def deleteManipulator(manip: Any) -> None:
        """Delete a manipulator.  This method should be used to delete manipulators that have been created using base manipulator create() methods."""
    def dgCallbackIds(self, type: Any, callbackName: Any) -> tuple[Any]:
        """Returns DG timing information for a specific callback type, broken down by callbackId."""
    def dgCallbacks(self, type: Any) -> tuple[Any]:
        """Returns DG timing information broken down by callback type."""
    def dgTimer(self, timerMetric: Any, timerType: Any) -> float:
        """Returns a specific DG timer metric for a given timer type."""
    def dgTimerOff(self) -> None:
        """Turns DG timing off for this node."""
    def dgTimerOn(self) -> None:
        """Turns DG timing on for this node."""
    def dgTimerQueryState(self) -> Any:
        """Returns the current DG timer state for this node."""
    def dgTimerReset(self) -> None:
        """Resets all DG timers for this node."""
    @staticmethod
    def drawPlaneHandles() -> bool:
        """This method returns the global option that says if the planar manipulator handles should be drawn or not.Setting this will affect the drawing of all manipulators that support the planar handles."""
    def duplicate(self, instance: bool = False, instanceLeaf: bool = False) -> MObject:
        """Duplicates the DAG hierarchy rooted at the current node."""
    def enableLimit(self, type: int, flag: bool) -> None:
        """Enables or disables a specified limit type."""
    def findAlias(self, alias: Any, attrObj: MObject) -> bool:
        """Returns the attribute which has the given alias."""
    def findPlug(self, attr: Any, wantNetworkedPlug: bool) -> MPlug:
        """Returns a plug for the given attribute."""
    def fullPathName(self) -> Any:
        """Returns the full path of the attached object, from the root of the DAG on down."""
    def getAffectedAttributes(self, attr: MObject) -> MObjectArray:
        """Returns all of the attributes which are affected by the specified attribute."""
    def getAffectingAttributes(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all of the attributes which affect the specified attribute."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute aliases."""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns all of the node's attribute aliases."""
    def getAllPaths(self) -> MDagPathArray:
        """Returns all of the DAG paths which lead to the object to which this function set is attached."""
    def getConnectedSetsAndMembers(self, instance: int, arg: bool, MObjectArray: Any) -> Any:
        """Returns a tuple containing an array of sets and an array of the"""
    def getConnections(self) -> MPlugArray:
        """Returns all the plugs which are connected to attributes of this node."""
    def getExternalContent(self) -> MExternalContentInfoTable:
        """Gets the external content (files) that this node depends on."""
    def getPath(self) -> MDagPath:
        """Returns the DAG path to which this function set is attached, or the first path to the node if the function set is attached to an MObject."""
    @staticmethod
    def globalSize() -> float:
        """Returns the global manipulator size."""
    @staticmethod
    def handleSize() -> float:
        """Returns the manipulator handle size."""
    def hasAttribute(self, name: Any) -> bool:
        """Returns True if the node has an attribute with the given name."""
    def hasChild(self, node: MObject) -> bool:
        """Returns True if the specified node is a child of this one."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def hasParent(self, node: MObject) -> bool:
        """Returns True if the specified node is a parent of this one."""
    def hasUniqueName(self) -> bool:
        """Returns True if the node's name is unique."""
    def instanceCount(self, indirect: bool) -> int:
        """Returns the number of instances for this node."""
    def isChildOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a parent of this one."""
    def isFlagSet(self, flag: int) -> bool:
        """Returns the state of the specified node flag."""
    def isInstanced(self, indirect: bool = True) -> bool:
        """Returns True if this node is instanced."""
    def isInstancedAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute is an instanced attribute of this node."""
    def isLimited(self, type: int) -> bool:
        """Returns True if the specified limit type is enabled."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files."""
    def isParentOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a child of this one."""
    def isTrackingEdits(self) -> bool:
        """Returns True if the node is referenced or in an assembly that is tracking edits."""
    def limitValue(self, type: int) -> float:
        """Returns the value of the specified limit."""
    @staticmethod
    def lineSize() -> float:
        """Returns the manipulator line size."""
    def name(self) -> Any:
        """Returns the node's name."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def paramIndex(self) -> int:
        """Returns the index of the parameter of the PointOnSurfaceManip. The data type corresponding to this index is MFnNumericData.k2Double."""
    def parent(self, index: int) -> MObject:
        """Returns the specified parent of this node."""
    def parentCount(self) -> int:
        """Returns the number of parents this node has."""
    def partialPathName(self) -> Any:
        """Returns the minimum path string necessary to uniquely identify the attached object."""
    def plugsAlias(self, plug: MPlug) -> Any:
        """Returns the alias for a plug's attribute."""
    def removeAttribute(self, attr: MObject, type: Any) -> None:
        """Removes a dynamic attribute from the node."""
    def removeChild(self, node: Any) -> MFnPointOnSurfaceManip:
        """Removes the child, specified by MObject, reparenting it under the world."""
    def removeChildAt(self, index: int) -> MFnPointOnSurfaceManip:
        """Removes the child, specified by index, reparenting it under the world."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Returns one of the node's attribute, based on the order in which they are written to file."""
    def resetFromRestPosition(self) -> None:
        """Resets the transform from its rest position matrix."""
    def resetTransformation(self, m: MMatrix) -> None:
        """Resets the transform's attribute values to represent the given transformation matrix in world space."""
    def restPosition(self) -> MTransformationMatrix:
        """Returns the transform's rest position matrix."""
    def rotateBy(self, quaternion: MQuaternion | MEulerRotation | int, Space: int | None = None) -> None:
        """Adds an MEulerRotation or MQuaternion to the transform's rotation."""
    def rotateByComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Adds to the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""
    def rotateOrientation(self, space: int) -> MQuaternion:
        """Returns the MQuaternion which orients the local rotation space."""
    def rotatePivot(self, space: int) -> MPoint:
        """Returns the transform's rotate pivot."""
    def rotatePivotTranslation(self, space: int) -> MVector:
        """Returns the transform's rotate pivot translation."""
    def rotateXYZValue(self, valIndex: int) -> MEulerRotation:
        """Gets the rotation for the active manipulator."""
    def rotation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotation as an MEulerRotation or MQuaternion."""
    def rotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotation as the individual components of an MEulerRotation or MQuaternion."""
    def rotationOrder(self) -> int:
        """Returns the order of rotations when the transform's rotation is expressed as an MEulerRotation."""
    def scale(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transform's XYZ scale components."""
    def scaleBy(self) -> None:
        """Multiplies the transform's XYZ scale components by a sequence of three floats."""
    def scalePivot(self, space: int) -> MPoint:
        """Returns the transform's scale pivot."""
    def scalePivotTranslation(self, space: int) -> MVector:
        """Returns the transform's scale pivot translation."""
    def setAffectsAnimation(self) -> None:
        """Specifies that modifications to a node could potentially affect the animation."""
    def setAlias(self, alias: Any, name: Any, plug: MPlug, add: bool | None = None) -> bool:
        """Adds or removes an attribute alias."""
    def setDoNotWrite(self, flag: bool) -> None:
        """Used to prevent the node from being written to file."""
    def setDrawArrows(self, state: bool) -> MFnPointOnSurfaceManip:
        """Sets whether or not the arrows should be drawn."""
    @staticmethod
    def setDrawPlaneHandles(bool: bool) -> None:
        """Sets the global option to display planar handles or not on supported manipulators."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> None:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> None:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> None:
        """Sets the state of the specified node flag."""
    @staticmethod
    def setGlobalSize(float: float) -> None:
        """Sets the global manipulator size."""
    @staticmethod
    def setHandleSize(float: float) -> None:
        """Sets the manipulator handle size."""
    def setLimit(self, type: int, value: float) -> None:
        """Sets the value of the specified limit."""
    @staticmethod
    def setLineSize(float: float) -> None:
        """Sets the manipulator line size."""
    def setName(self, name: Any, createNamespace: bool | None = None) -> Any:
        """Sets the node's name."""
    def setObject(self, arg: MDagPath | MObject) -> MFnPointOnSurfaceManip:
        """Attaches the function set to the specified node or DAG path."""
    def setRestPosition(self, matrix: MTransformationMatrix) -> None:
        """Sets the transform's rest position matrix."""
    def setRotateOrientation(self, quat: MQuaternion, space: int, balance: bool) -> None:
        """Sets the MQuaternion which orients the local rotation space."""
    def setRotatePivot(self, point: MPoint, space: int, balance: bool) -> None:
        """Sets the transform's rotate pivot."""
    def setRotatePivotTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's rotate pivot translation."""
    def setRotation(self, quaternion: MQuaternion | MEulerRotation | int, Space: int | None = None) -> None:
        """Sets the transform's rotation using an MEulerRotation or MQuaternion."""
    def setRotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""
    def setRotationOrder(self, order: int, reorder: bool) -> None:
        """Sets the transform's rotation order."""
    def setScale(self) -> None:
        """Sets the transform's scale components."""
    def setScalePivot(self, point: MPoint, space: int, balance: bool) -> None:
        """Sets the transform's scale pivot."""
    def setScalePivotTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's scale pivot translation."""
    def setShear(self) -> None:
        """Sets the transform's shear."""
    def setTransformation(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's attribute values to represent the given transformation matrix."""
    def setTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's translation."""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def shear(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transform's shear components."""
    def shearBy(self) -> None:
        """Multiplies the transform's shear components by a sequence of three floats."""
    def surfaceIndex(self) -> int:
        """Returns the index of the surface. The data type corresponding to this index is MFnData.kNurbsSurface."""
    def transformation(self) -> MTransformationMatrix:
        """Returns the transformation matrix represented by this transform."""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
    def translateBy(self, vec: MVector, space: int) -> None:
        """Adds an MVector to the transform's translation."""
    def translation(self, Space: int) -> MVector:
        """Returns the transform's translation as an MVector."""
    def type(self) -> int:
        """Returns the type of the function set."""
    def uniqueName(self) -> Any:
        """For a DAG node, the unique name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself. For a non-DAG node, the uniqueName is just its name."""
    def userNode(self) -> MPxNode:
        """Returns the MPxNode object for a plugin node."""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnRotateManip:
    boundingBox: Any
    inModel: Any
    inUnderWorld: Any
    isDefaultNode: Any
    isFromReferencedFile: Any
    isInstanceable: Any
    isIntermediateObject: Any
    isLocked: Any
    isOptimizePlaybackOn: Any
    isShared: Any
    isSnapModeOn: Any
    isVisible: Any
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
    kWorldSpace: Any
    manipScale: Any
    namespace: Any
    objectColor: Any
    objectColorRGB: Any
    objectColorType: Any
    pluginName: Any
    rotateMode: Any
    snapIncrement: Any
    typeId: Any
    typeName: Any
    useObjectColor: Any
    def __init__(self, object: MObject | MDagPath | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def absoluteName(self) -> Any:
        """Returns the absolute name of this node.  The absolute name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself.  Regardless of relative name mode, absoluteName() will always return a full namespace path prefixed with a leading colon (the root namespace).  If the underlying node is a DAG node, then absoluteName() does not guarantee uniqueness, that is, two dependency nodes could have the same absoluteName().  In cases like this the uniqueName() method will guarantee that the name uniquely identifies the node."""
    def addAttribute(self, attr: MObject, type: Any) -> None:
        """Adds a new dynamic attribute to the node."""
    def addChild(self, node: int, index: bool, keepExistingParents: bool = False) -> MFnRotateManip:
        """Makes a node a child of this one."""
    def addExternalContentForFileAttr(self, attr: MObject) -> MExternalContentInfoTable:
        """Adds content info to the specified table from a file path attribute."""
    def affectsAnimation(self) -> bool:
        """Returns true if the changes to the node may affect animation."""
    @staticmethod
    def allocateFlag(pluginName: Any) -> int:
        """Allocates a flag on all nodes for use by the named plugin and returns the flag's index."""
    def attribute(self, index: Any) -> MObject:
        """Returns an attribute of the node, given either its index or name."""
    def attributeClass(self, attr: MObject) -> Any:
        """Returns the class of the specified attribute."""
    def attributeCount(self) -> int:
        """Returns the number of attributes on the node."""
    @staticmethod
    def balanceTransformation(identity: int, identity_: int, one: int, kXYZ: int, arg: Any = None) -> None:
        """Balance a transformation when applying a world matrix to a joint. Thisaccesses the same underlying functionality as the xform command."""
    def canBeWritten(self) -> bool:
        """Returns true if the node will be written to file."""
    def child(self, index: int) -> MObject:
        """Returns the specified child of this node."""
    def childCount(self) -> int:
        """Returns the number of nodes which are children of this one."""
    @staticmethod
    def classification(nodeTypeName: Any) -> Any:
        """Returns the classification string for the named node type."""
    def clearRestPosition(self) -> None:
        """Clears the transform's rest position matrix."""
    def connectToRotationCenterPlug(self, rotationCenterPlug: MPlug) -> MFnRotateManip:
        """Create a 1-1 association of the rotation center on the manipulator and the rotationCenterPlug parameter.  When both the rotation center is attached to a plug and the displayWithNode() method has been called, the manipulator will display with the node regardless of the connection made to the rotation center."""
    def connectToRotationPlug(self, rotationPlug: MPlug) -> MFnRotateManip:
        """Create a 1-1 connection from the rotation manipVal to the rotationPlug parameter.  Any changes to the rotation manipVal will be immediately reflected in the connected plug.  Connecting to the "rotation" plug on a transform node will produce similar behavior to the built-in rotation manipulator."""
    def create(self, manipName: Any = None, rotationName: Any = None) -> MObject:
        """Creates a new RotateManip, and attaches this function set to the new manipulator."""
    def dagPath(self) -> MDagPath:
        """Returns the DAG path to which this function set is attached. Raises a TypeError if the function set is attached to an MObject rather than a path."""
    def dagRoot(self) -> MObject:
        """Returns the root node of the first path leading to this node."""
    @staticmethod
    def deallocateAllFlags(pluginName: Any) -> None:
        """Deallocates all node flags which are currently allocated to the named plugin."""
    @staticmethod
    def deallocateFlag(pluginName: Any, flag: int) -> None:
        """Deallocates the specified node flag, which was previously allocated by the named plugin using allocateFlag()."""
    @staticmethod
    def deleteManipulator(manip: Any) -> None:
        """Delete a manipulator.  This method should be used to delete manipulators that have been created using base manipulator create() methods."""
    def dgCallbackIds(self, type: Any, callbackName: Any) -> tuple[Any]:
        """Returns DG timing information for a specific callback type, broken down by callbackId."""
    def dgCallbacks(self, type: Any) -> tuple[Any]:
        """Returns DG timing information broken down by callback type."""
    def dgTimer(self, timerMetric: Any, timerType: Any) -> float:
        """Returns a specific DG timer metric for a given timer type."""
    def dgTimerOff(self) -> None:
        """Turns DG timing off for this node."""
    def dgTimerOn(self) -> None:
        """Turns DG timing on for this node."""
    def dgTimerQueryState(self) -> Any:
        """Returns the current DG timer state for this node."""
    def dgTimerReset(self) -> None:
        """Resets all DG timers for this node."""
    def displayWithNode(self, node: MObject) -> MFnRotateManip:
        """Configures the manipulator to display with the node, causing the position of the manipulator to follow the position of the node whenever the node is moved.  The node must be a DAG object."""
    @staticmethod
    def drawPlaneHandles() -> bool:
        """This method returns the global option that says if the planar manipulator handles should be drawn or not.Setting this will affect the drawing of all manipulators that support the planar handles."""
    def duplicate(self, instance: bool = False, instanceLeaf: bool = False) -> MObject:
        """Duplicates the DAG hierarchy rooted at the current node."""
    def enableLimit(self, type: int, flag: bool) -> None:
        """Enables or disables a specified limit type."""
    def findAlias(self, alias: Any, attrObj: MObject) -> bool:
        """Returns the attribute which has the given alias."""
    def findPlug(self, attr: Any, wantNetworkedPlug: bool) -> MPlug:
        """Returns a plug for the given attribute."""
    def fullPathName(self) -> Any:
        """Returns the full path of the attached object, from the root of the DAG on down."""
    def getAffectedAttributes(self, attr: MObject) -> MObjectArray:
        """Returns all of the attributes which are affected by the specified attribute."""
    def getAffectingAttributes(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all of the attributes which affect the specified attribute."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute aliases."""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns all of the node's attribute aliases."""
    def getAllPaths(self) -> MDagPathArray:
        """Returns all of the DAG paths which lead to the object to which this function set is attached."""
    def getConnectedSetsAndMembers(self, instance: int, arg: bool, MObjectArray: Any) -> Any:
        """Returns a tuple containing an array of sets and an array of the"""
    def getConnections(self) -> MPlugArray:
        """Returns all the plugs which are connected to attributes of this node."""
    def getExternalContent(self) -> MExternalContentInfoTable:
        """Gets the external content (files) that this node depends on."""
    def getPath(self) -> MDagPath:
        """Returns the DAG path to which this function set is attached, or the first path to the node if the function set is attached to an MObject."""
    @staticmethod
    def globalSize() -> float:
        """Returns the global manipulator size."""
    @staticmethod
    def handleSize() -> float:
        """Returns the manipulator handle size."""
    def hasAttribute(self, name: Any) -> bool:
        """Returns True if the node has an attribute with the given name."""
    def hasChild(self, node: MObject) -> bool:
        """Returns True if the specified node is a child of this one."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def hasParent(self, node: MObject) -> bool:
        """Returns True if the specified node is a parent of this one."""
    def hasUniqueName(self) -> bool:
        """Returns True if the node's name is unique."""
    def instanceCount(self, indirect: bool) -> int:
        """Returns the number of instances for this node."""
    def isChildOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a parent of this one."""
    def isFlagSet(self, flag: int) -> bool:
        """Returns the state of the specified node flag."""
    def isInstanced(self, indirect: bool = True) -> bool:
        """Returns True if this node is instanced."""
    def isInstancedAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute is an instanced attribute of this node."""
    def isLimited(self, type: int) -> bool:
        """Returns True if the specified limit type is enabled."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files."""
    def isParentOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a child of this one."""
    def isTrackingEdits(self) -> bool:
        """Returns True if the node is referenced or in an assembly that is tracking edits."""
    def limitValue(self, type: int) -> float:
        """Returns the value of the specified limit."""
    @staticmethod
    def lineSize() -> float:
        """Returns the manipulator line size."""
    def name(self) -> Any:
        """Returns the node's name."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def parent(self, index: int) -> MObject:
        """Returns the specified parent of this node."""
    def parentCount(self) -> int:
        """Returns the number of parents this node has."""
    def partialPathName(self) -> Any:
        """Returns the minimum path string necessary to uniquely identify the attached object."""
    def plugsAlias(self, plug: MPlug) -> Any:
        """Returns the alias for a plug's attribute."""
    def removeAttribute(self, attr: MObject, type: Any) -> None:
        """Removes a dynamic attribute from the node."""
    def removeChild(self, node: Any) -> MFnRotateManip:
        """Removes the child, specified by MObject, reparenting it under the world."""
    def removeChildAt(self, index: int) -> MFnRotateManip:
        """Removes the child, specified by index, reparenting it under the world."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Returns one of the node's attribute, based on the order in which they are written to file."""
    def resetFromRestPosition(self) -> None:
        """Resets the transform from its rest position matrix."""
    def resetTransformation(self, m: MMatrix) -> None:
        """Resets the transform's attribute values to represent the given transformation matrix in world space."""
    def restPosition(self) -> MTransformationMatrix:
        """Returns the transform's rest position matrix."""
    def rotateBy(self, quaternion: MQuaternion | MEulerRotation | int, Space: int | None = None) -> None:
        """Adds an MEulerRotation or MQuaternion to the transform's rotation."""
    def rotateByComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Adds to the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""
    def rotateOrientation(self, space: int) -> MQuaternion:
        """Returns the MQuaternion which orients the local rotation space."""
    def rotatePivot(self, space: int) -> MPoint:
        """Returns the transform's rotate pivot."""
    def rotatePivotTranslation(self, space: int) -> MVector:
        """Returns the transform's rotate pivot translation."""
    def rotateXYZValue(self, valIndex: int) -> MEulerRotation:
        """Gets the rotation for the active manipulator."""
    def rotation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotation as an MEulerRotation or MQuaternion."""
    def rotationCenterIndex(self) -> int:
        """Returns the index of the rotation center for this manipulator."""
    def rotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotation as the individual components of an MEulerRotation or MQuaternion."""
    def rotationIndex(self) -> int:
        """Returns the index of the rotation manipVal for the manipulator.  When plugToManip conversion functions are used to produce the rotation manipVal, the manipulator data must be of the type MFnNumericData.k3Double, with X,Y, and Z rotations given in radians.  This is easily accomplished by using the MEulerRotation class to manage the rotations."""
    def rotationOrder(self) -> int:
        """Returns the order of rotations when the transform's rotation is expressed as an MEulerRotation."""
    def scale(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transform's XYZ scale components."""
    def scaleBy(self) -> None:
        """Multiplies the transform's XYZ scale components by a sequence of three floats."""
    def scalePivot(self, space: int) -> MPoint:
        """Returns the transform's scale pivot."""
    def scalePivotTranslation(self, space: int) -> MVector:
        """Returns the transform's scale pivot translation."""
    def setAffectsAnimation(self) -> None:
        """Specifies that modifications to a node could potentially affect the animation."""
    def setAlias(self, alias: Any, name: Any, plug: MPlug, add: bool | None = None) -> bool:
        """Adds or removes an attribute alias."""
    def setDoNotWrite(self, flag: bool) -> None:
        """Used to prevent the node from being written to file."""
    @staticmethod
    def setDrawPlaneHandles(bool: bool) -> None:
        """Sets the global option to display planar handles or not on supported manipulators."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> None:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> None:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> None:
        """Sets the state of the specified node flag."""
    @staticmethod
    def setGlobalSize(float: float) -> None:
        """Sets the global manipulator size."""
    @staticmethod
    def setHandleSize(float: float) -> None:
        """Sets the manipulator handle size."""
    def setInitialRotation(self, rotation: MEulerRotation) -> MFnRotateManip:
        """Sets the initial rotation for the rotate manipulator.  Setting the initial rotation will prevent the manipulator from jumping back to the default rotation when there is already an existing rotation on the target plug."""
    def setLimit(self, type: int, value: float) -> None:
        """Sets the value of the specified limit."""
    @staticmethod
    def setLineSize(float: float) -> None:
        """Sets the manipulator line size."""
    def setName(self, name: Any, createNamespace: bool | None = None) -> Any:
        """Sets the node's name."""
    def setObject(self, arg: MDagPath | MObject) -> MFnRotateManip:
        """Attaches the function set to the specified node or DAG path."""
    def setRestPosition(self, matrix: MTransformationMatrix) -> None:
        """Sets the transform's rest position matrix."""
    def setRotateOrientation(self, quat: MQuaternion, space: int, balance: bool) -> None:
        """Sets the MQuaternion which orients the local rotation space."""
    def setRotatePivot(self, point: MPoint, space: int, balance: bool) -> None:
        """Sets the transform's rotate pivot."""
    def setRotatePivotTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's rotate pivot translation."""
    def setRotation(self, quaternion: MQuaternion | MEulerRotation | int, Space: int | None = None) -> None:
        """Sets the transform's rotation using an MEulerRotation or MQuaternion."""
    def setRotationCenter(self, rotationCenter: MPoint) -> MFnRotateManip:
        """Sets the position of the rotation center for the manipulator."""
    def setRotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""
    def setRotationOrder(self, order: int, reorder: bool) -> None:
        """Sets the transform's rotation order."""
    def setScale(self) -> None:
        """Sets the transform's scale components."""
    def setScalePivot(self, point: MPoint, space: int, balance: bool) -> None:
        """Sets the transform's scale pivot."""
    def setScalePivotTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's scale pivot translation."""
    def setShear(self) -> None:
        """Sets the transform's shear."""
    def setTransformation(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's attribute values to represent the given transformation matrix."""
    def setTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's translation."""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def shear(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transform's shear components."""
    def shearBy(self) -> None:
        """Multiplies the transform's shear components by a sequence of three floats."""
    def transformation(self) -> MTransformationMatrix:
        """Returns the transformation matrix represented by this transform."""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
    def translateBy(self, vec: MVector, space: int) -> None:
        """Adds an MVector to the transform's translation."""
    def translation(self, Space: int) -> MVector:
        """Returns the transform's translation as an MVector."""
    def type(self) -> int:
        """Returns the type of the function set."""
    def uniqueName(self) -> Any:
        """For a DAG node, the unique name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself. For a non-DAG node, the uniqueName is just its name."""
    def userNode(self) -> MPxNode:
        """Returns the MPxNode object for a plugin node."""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnScaleManip:
    boundingBox: Any
    inModel: Any
    inUnderWorld: Any
    isDefaultNode: Any
    isFromReferencedFile: Any
    isInstanceable: Any
    isIntermediateObject: Any
    isLocked: Any
    isOptimizePlaybackOn: Any
    isShared: Any
    isSnapModeOn: Any
    isVisible: Any
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
    manipScale: Any
    namespace: Any
    objectColor: Any
    objectColorRGB: Any
    objectColorType: Any
    orientation: Any
    orientationMode: Any
    pluginName: Any
    snapIncrement: Any
    typeId: Any
    typeName: Any
    useObjectColor: Any
    def __init__(self, object: MObject | MDagPath | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def absoluteName(self) -> Any:
        """Returns the absolute name of this node.  The absolute name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself.  Regardless of relative name mode, absoluteName() will always return a full namespace path prefixed with a leading colon (the root namespace).  If the underlying node is a DAG node, then absoluteName() does not guarantee uniqueness, that is, two dependency nodes could have the same absoluteName().  In cases like this the uniqueName() method will guarantee that the name uniquely identifies the node."""
    def addAttribute(self, attr: MObject, type: Any) -> None:
        """Adds a new dynamic attribute to the node."""
    def addChild(self, node: int, index: bool, keepExistingParents: bool = False) -> MFnScaleManip:
        """Makes a node a child of this one."""
    def addExternalContentForFileAttr(self, attr: MObject) -> MExternalContentInfoTable:
        """Adds content info to the specified table from a file path attribute."""
    def affectsAnimation(self) -> bool:
        """Returns true if the changes to the node may affect animation."""
    @staticmethod
    def allocateFlag(pluginName: Any) -> int:
        """Allocates a flag on all nodes for use by the named plugin and returns the flag's index."""
    def attribute(self, index: Any) -> MObject:
        """Returns an attribute of the node, given either its index or name."""
    def attributeClass(self, attr: MObject) -> Any:
        """Returns the class of the specified attribute."""
    def attributeCount(self) -> int:
        """Returns the number of attributes on the node."""
    @staticmethod
    def balanceTransformation(identity: int, identity_: int, one: int, kXYZ: int, arg: Any = None) -> None:
        """Balance a transformation when applying a world matrix to a joint. Thisaccesses the same underlying functionality as the xform command."""
    def canBeWritten(self) -> bool:
        """Returns true if the node will be written to file."""
    def child(self, index: int) -> MObject:
        """Returns the specified child of this node."""
    def childCount(self) -> int:
        """Returns the number of nodes which are children of this one."""
    @staticmethod
    def classification(nodeTypeName: Any) -> Any:
        """Returns the classification string for the named node type."""
    def clearRestPosition(self) -> None:
        """Clears the transform's rest position matrix."""
    def connectToScaleCenterPlug(self, scaleCenterPlug: MPlug) -> MFnScaleManip:
        """Create a 1-1 association of the scale center on the manipulator and the scaleCenterPlug parameter.  When both the scale center is attached to a plug and the displayWithNode() method has been called, the manipulator will display with the node regardless of the connection made to the scale center."""
    def connectToScalePlug(self, scalePlug: MPlug) -> MFnScaleManip:
        """Create a 1-1 connection from the scale manipVal to the scalePlug parameter.  Any changes to the scale manipVal will be immediately reflected in the connected plug.  Connecting to the "scale" plug on a transform node will produce similar behavior to the built-in scale manipulator."""
    def create(self, manipName: Any = None, scaleName: Any = None) -> MObject:
        """Creates a new ScaleManip, and attaches this function set to the new manipulator."""
    def dagPath(self) -> MDagPath:
        """Returns the DAG path to which this function set is attached. Raises a TypeError if the function set is attached to an MObject rather than a path."""
    def dagRoot(self) -> MObject:
        """Returns the root node of the first path leading to this node."""
    @staticmethod
    def deallocateAllFlags(pluginName: Any) -> None:
        """Deallocates all node flags which are currently allocated to the named plugin."""
    @staticmethod
    def deallocateFlag(pluginName: Any, flag: int) -> None:
        """Deallocates the specified node flag, which was previously allocated by the named plugin using allocateFlag()."""
    @staticmethod
    def deleteManipulator(manip: Any) -> None:
        """Delete a manipulator.  This method should be used to delete manipulators that have been created using base manipulator create() methods."""
    def dgCallbackIds(self, type: Any, callbackName: Any) -> tuple[Any]:
        """Returns DG timing information for a specific callback type, broken down by callbackId."""
    def dgCallbacks(self, type: Any) -> tuple[Any]:
        """Returns DG timing information broken down by callback type."""
    def dgTimer(self, timerMetric: Any, timerType: Any) -> float:
        """Returns a specific DG timer metric for a given timer type."""
    def dgTimerOff(self) -> None:
        """Turns DG timing off for this node."""
    def dgTimerOn(self) -> None:
        """Turns DG timing on for this node."""
    def dgTimerQueryState(self) -> Any:
        """Returns the current DG timer state for this node."""
    def dgTimerReset(self) -> None:
        """Resets all DG timers for this node."""
    def displayWithNode(self, node: MObject) -> MFnScaleManip:
        """Configures the manipulator to display with the node, causing the position of the manipulator to follow the position of the node whenever the node is moved.  The node must be a DAG object."""
    @staticmethod
    def drawPlaneHandles() -> bool:
        """This method returns the global option that says if the planar manipulator handles should be drawn or not.Setting this will affect the drawing of all manipulators that support the planar handles."""
    def duplicate(self, instance: bool = False, instanceLeaf: bool = False) -> MObject:
        """Duplicates the DAG hierarchy rooted at the current node."""
    def enableLimit(self, type: int, flag: bool) -> None:
        """Enables or disables a specified limit type."""
    def findAlias(self, alias: Any, attrObj: MObject) -> bool:
        """Returns the attribute which has the given alias."""
    def findPlug(self, attr: Any, wantNetworkedPlug: bool) -> MPlug:
        """Returns a plug for the given attribute."""
    def fullPathName(self) -> Any:
        """Returns the full path of the attached object, from the root of the DAG on down."""
    def getAffectedAttributes(self, attr: MObject) -> MObjectArray:
        """Returns all of the attributes which are affected by the specified attribute."""
    def getAffectingAttributes(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all of the attributes which affect the specified attribute."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute aliases."""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns all of the node's attribute aliases."""
    def getAllPaths(self) -> MDagPathArray:
        """Returns all of the DAG paths which lead to the object to which this function set is attached."""
    def getConnectedSetsAndMembers(self, instance: int, arg: bool, MObjectArray: Any) -> Any:
        """Returns a tuple containing an array of sets and an array of the"""
    def getConnections(self) -> MPlugArray:
        """Returns all the plugs which are connected to attributes of this node."""
    def getExternalContent(self) -> MExternalContentInfoTable:
        """Gets the external content (files) that this node depends on."""
    def getPath(self) -> MDagPath:
        """Returns the DAG path to which this function set is attached, or the first path to the node if the function set is attached to an MObject."""
    @staticmethod
    def globalSize() -> float:
        """Returns the global manipulator size."""
    @staticmethod
    def handleSize() -> float:
        """Returns the manipulator handle size."""
    def hasAttribute(self, name: Any) -> bool:
        """Returns True if the node has an attribute with the given name."""
    def hasChild(self, node: MObject) -> bool:
        """Returns True if the specified node is a child of this one."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def hasParent(self, node: MObject) -> bool:
        """Returns True if the specified node is a parent of this one."""
    def hasUniqueName(self) -> bool:
        """Returns True if the node's name is unique."""
    def instanceCount(self, indirect: bool) -> int:
        """Returns the number of instances for this node."""
    def isChildOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a parent of this one."""
    def isFlagSet(self, flag: int) -> bool:
        """Returns the state of the specified node flag."""
    def isInstanced(self, indirect: bool = True) -> bool:
        """Returns True if this node is instanced."""
    def isInstancedAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute is an instanced attribute of this node."""
    def isLimited(self, type: int) -> bool:
        """Returns True if the specified limit type is enabled."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files."""
    def isParentOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a child of this one."""
    def isTrackingEdits(self) -> bool:
        """Returns True if the node is referenced or in an assembly that is tracking edits."""
    def limitValue(self, type: int) -> float:
        """Returns the value of the specified limit."""
    @staticmethod
    def lineSize() -> float:
        """Returns the manipulator line size."""
    def name(self) -> Any:
        """Returns the node's name."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def parent(self, index: int) -> MObject:
        """Returns the specified parent of this node."""
    def parentCount(self) -> int:
        """Returns the number of parents this node has."""
    def partialPathName(self) -> Any:
        """Returns the minimum path string necessary to uniquely identify the attached object."""
    def plugsAlias(self, plug: MPlug) -> Any:
        """Returns the alias for a plug's attribute."""
    def removeAttribute(self, attr: MObject, type: Any) -> None:
        """Removes a dynamic attribute from the node."""
    def removeChild(self, node: Any) -> MFnScaleManip:
        """Removes the child, specified by MObject, reparenting it under the world."""
    def removeChildAt(self, index: int) -> MFnScaleManip:
        """Removes the child, specified by index, reparenting it under the world."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Returns one of the node's attribute, based on the order in which they are written to file."""
    def resetFromRestPosition(self) -> None:
        """Resets the transform from its rest position matrix."""
    def resetTransformation(self, m: MMatrix) -> None:
        """Resets the transform's attribute values to represent the given transformation matrix in world space."""
    def restPosition(self) -> MTransformationMatrix:
        """Returns the transform's rest position matrix."""
    def rotateBy(self, quaternion: MQuaternion | MEulerRotation | int, Space: int | None = None) -> None:
        """Adds an MEulerRotation or MQuaternion to the transform's rotation."""
    def rotateByComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Adds to the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""
    def rotateOrientation(self, space: int) -> MQuaternion:
        """Returns the MQuaternion which orients the local rotation space."""
    def rotatePivot(self, space: int) -> MPoint:
        """Returns the transform's rotate pivot."""
    def rotatePivotTranslation(self, space: int) -> MVector:
        """Returns the transform's rotate pivot translation."""
    def rotateXYZValue(self, valIndex: int) -> MEulerRotation:
        """Gets the rotation for the active manipulator."""
    def rotation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotation as an MEulerRotation or MQuaternion."""
    def rotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotation as the individual components of an MEulerRotation or MQuaternion."""
    def rotationOrder(self) -> int:
        """Returns the order of rotations when the transform's rotation is expressed as an MEulerRotation."""
    def scale(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transform's XYZ scale components."""
    def scaleBy(self) -> None:
        """Multiplies the transform's XYZ scale components by a sequence of three floats."""
    def scaleCenterIndex(self) -> int:
        """Returns the index of the scale center manipVal for this manipulator."""
    def scaleIndex(self) -> int:
        """Returns the index of the scale manipVal for this manipulator."""
    def scalePivot(self, space: int) -> MPoint:
        """Returns the transform's scale pivot."""
    def scalePivotTranslation(self, space: int) -> MVector:
        """Returns the transform's scale pivot translation."""
    def setAffectsAnimation(self) -> None:
        """Specifies that modifications to a node could potentially affect the animation."""
    def setAlias(self, alias: Any, name: Any, plug: MPlug, add: bool | None = None) -> bool:
        """Adds or removes an attribute alias."""
    def setDoNotWrite(self, flag: bool) -> None:
        """Used to prevent the node from being written to file."""
    @staticmethod
    def setDrawPlaneHandles(bool: bool) -> None:
        """Sets the global option to display planar handles or not on supported manipulators."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> None:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> None:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> None:
        """Sets the state of the specified node flag."""
    @staticmethod
    def setGlobalSize(float: float) -> None:
        """Sets the global manipulator size."""
    @staticmethod
    def setHandleSize(float: float) -> None:
        """Sets the manipulator handle size."""
    def setInitialScale(self, scale: MVector) -> MFnScaleManip:
        """Sets the initial scale for the scale manipulator.  Setting the initial scale will prevent the manipulator from jumping back to the default scale when there is already an existing scale on the target plug."""
    def setLimit(self, type: int, value: float) -> None:
        """Sets the value of the specified limit."""
    @staticmethod
    def setLineSize(float: float) -> None:
        """Sets the manipulator line size."""
    def setName(self, name: Any, createNamespace: bool | None = None) -> Any:
        """Sets the node's name."""
    def setObject(self, arg: MDagPath | MObject) -> MFnScaleManip:
        """Attaches the function set to the specified node or DAG path."""
    def setRestPosition(self, matrix: MTransformationMatrix) -> None:
        """Sets the transform's rest position matrix."""
    def setRotateOrientation(self, quat: MQuaternion, space: int, balance: bool) -> None:
        """Sets the MQuaternion which orients the local rotation space."""
    def setRotatePivot(self, point: MPoint, space: int, balance: bool) -> None:
        """Sets the transform's rotate pivot."""
    def setRotatePivotTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's rotate pivot translation."""
    def setRotation(self, quaternion: MQuaternion | MEulerRotation | int, Space: int | None = None) -> None:
        """Sets the transform's rotation using an MEulerRotation or MQuaternion."""
    def setRotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""
    def setRotationOrder(self, order: int, reorder: bool) -> None:
        """Sets the transform's rotation order."""
    def setScale(self) -> None:
        """Sets the transform's scale components."""
    def setScalePivot(self, point: MPoint, space: int, balance: bool) -> None:
        """Sets the transform's scale pivot."""
    def setScalePivotTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's scale pivot translation."""
    def setShear(self) -> None:
        """Sets the transform's shear."""
    def setTransformation(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's attribute values to represent the given transformation matrix."""
    def setTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's translation."""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def shear(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transform's shear components."""
    def shearBy(self) -> None:
        """Multiplies the transform's shear components by a sequence of three floats."""
    def transformation(self) -> MTransformationMatrix:
        """Returns the transformation matrix represented by this transform."""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
    def translateBy(self, vec: MVector, space: int) -> None:
        """Adds an MVector to the transform's translation."""
    def translation(self, Space: int) -> MVector:
        """Returns the transform's translation as an MVector."""
    def type(self) -> int:
        """Returns the type of the function set."""
    def uniqueName(self) -> Any:
        """For a DAG node, the unique name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself. For a non-DAG node, the uniqueName is just its name."""
    def userNode(self) -> MPxNode:
        """Returns the MPxNode object for a plugin node."""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnStateManip:
    boundingBox: Any
    inModel: Any
    inUnderWorld: Any
    isDefaultNode: Any
    isFromReferencedFile: Any
    isInstanceable: Any
    isIntermediateObject: Any
    isLocked: Any
    isOptimizePlaybackOn: Any
    isShared: Any
    isVisible: Any
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
    manipScale: Any
    maxStates: Any
    namespace: Any
    objectColor: Any
    objectColorRGB: Any
    objectColorType: Any
    pluginName: Any
    typeId: Any
    typeName: Any
    useObjectColor: Any
    def __init__(self, object: MObject | MDagPath | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def absoluteName(self) -> Any:
        """Returns the absolute name of this node.  The absolute name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself.  Regardless of relative name mode, absoluteName() will always return a full namespace path prefixed with a leading colon (the root namespace).  If the underlying node is a DAG node, then absoluteName() does not guarantee uniqueness, that is, two dependency nodes could have the same absoluteName().  In cases like this the uniqueName() method will guarantee that the name uniquely identifies the node."""
    def addAttribute(self, attr: MObject, type: Any) -> None:
        """Adds a new dynamic attribute to the node."""
    def addChild(self, node: int, index: bool, keepExistingParents: bool = False) -> MFnStateManip:
        """Makes a node a child of this one."""
    def addExternalContentForFileAttr(self, attr: MObject) -> MExternalContentInfoTable:
        """Adds content info to the specified table from a file path attribute."""
    def affectsAnimation(self) -> bool:
        """Returns true if the changes to the node may affect animation."""
    @staticmethod
    def allocateFlag(pluginName: Any) -> int:
        """Allocates a flag on all nodes for use by the named plugin and returns the flag's index."""
    def attribute(self, index: Any) -> MObject:
        """Returns an attribute of the node, given either its index or name."""
    def attributeClass(self, attr: MObject) -> Any:
        """Returns the class of the specified attribute."""
    def attributeCount(self) -> int:
        """Returns the number of attributes on the node."""
    @staticmethod
    def balanceTransformation(identity: int, identity_: int, one: int, kXYZ: int, arg: Any = None) -> None:
        """Balance a transformation when applying a world matrix to a joint. Thisaccesses the same underlying functionality as the xform command."""
    def canBeWritten(self) -> bool:
        """Returns true if the node will be written to file."""
    def child(self, index: int) -> MObject:
        """Returns the specified child of this node."""
    def childCount(self) -> int:
        """Returns the number of nodes which are children of this one."""
    @staticmethod
    def classification(nodeTypeName: Any) -> Any:
        """Returns the classification string for the named node type."""
    def clearRestPosition(self) -> None:
        """Clears the transform's rest position matrix."""
    def connectToStatePlug(self, statePlug: Any) -> MFnStateManip:
        """Connect to the state plug. The data type corresponding to the statePlug is a int integer."""
    def create(self, manipName: Any = None, stateName: Any = None) -> MObject:
        """Creates a new StateManip."""
    def dagPath(self) -> MDagPath:
        """Returns the DAG path to which this function set is attached. Raises a TypeError if the function set is attached to an MObject rather than a path."""
    def dagRoot(self) -> MObject:
        """Returns the root node of the first path leading to this node."""
    @staticmethod
    def deallocateAllFlags(pluginName: Any) -> None:
        """Deallocates all node flags which are currently allocated to the named plugin."""
    @staticmethod
    def deallocateFlag(pluginName: Any, flag: int) -> None:
        """Deallocates the specified node flag, which was previously allocated by the named plugin using allocateFlag()."""
    @staticmethod
    def deleteManipulator(manip: Any) -> None:
        """Delete a manipulator.  This method should be used to delete manipulators that have been created using base manipulator create() methods."""
    def dgCallbackIds(self, type: Any, callbackName: Any) -> tuple[Any]:
        """Returns DG timing information for a specific callback type, broken down by callbackId."""
    def dgCallbacks(self, type: Any) -> tuple[Any]:
        """Returns DG timing information broken down by callback type."""
    def dgTimer(self, timerMetric: Any, timerType: Any) -> float:
        """Returns a specific DG timer metric for a given timer type."""
    def dgTimerOff(self) -> None:
        """Turns DG timing off for this node."""
    def dgTimerOn(self) -> None:
        """Turns DG timing on for this node."""
    def dgTimerQueryState(self) -> Any:
        """Returns the current DG timer state for this node."""
    def dgTimerReset(self) -> None:
        """Resets all DG timers for this node."""
    @staticmethod
    def drawPlaneHandles() -> bool:
        """This method returns the global option that says if the planar manipulator handles should be drawn or not.Setting this will affect the drawing of all manipulators that support the planar handles."""
    def duplicate(self, instance: bool = False, instanceLeaf: bool = False) -> MObject:
        """Duplicates the DAG hierarchy rooted at the current node."""
    def enableLimit(self, type: int, flag: bool) -> None:
        """Enables or disables a specified limit type."""
    def findAlias(self, alias: Any, attrObj: MObject) -> bool:
        """Returns the attribute which has the given alias."""
    def findPlug(self, attr: Any, wantNetworkedPlug: bool) -> MPlug:
        """Returns a plug for the given attribute."""
    def fullPathName(self) -> Any:
        """Returns the full path of the attached object, from the root of the DAG on down."""
    def getAffectedAttributes(self, attr: MObject) -> MObjectArray:
        """Returns all of the attributes which are affected by the specified attribute."""
    def getAffectingAttributes(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all of the attributes which affect the specified attribute."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute aliases."""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns all of the node's attribute aliases."""
    def getAllPaths(self) -> MDagPathArray:
        """Returns all of the DAG paths which lead to the object to which this function set is attached."""
    def getConnectedSetsAndMembers(self, instance: int, arg: bool, MObjectArray: Any) -> Any:
        """Returns a tuple containing an array of sets and an array of the"""
    def getConnections(self) -> MPlugArray:
        """Returns all the plugs which are connected to attributes of this node."""
    def getExternalContent(self) -> MExternalContentInfoTable:
        """Gets the external content (files) that this node depends on."""
    def getPath(self) -> MDagPath:
        """Returns the DAG path to which this function set is attached, or the first path to the node if the function set is attached to an MObject."""
    @staticmethod
    def globalSize() -> float:
        """Returns the global manipulator size."""
    @staticmethod
    def handleSize() -> float:
        """Returns the manipulator handle size."""
    def hasAttribute(self, name: Any) -> bool:
        """Returns True if the node has an attribute with the given name."""
    def hasChild(self, node: MObject) -> bool:
        """Returns True if the specified node is a child of this one."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def hasParent(self, node: MObject) -> bool:
        """Returns True if the specified node is a parent of this one."""
    def hasUniqueName(self) -> bool:
        """Returns True if the node's name is unique."""
    def instanceCount(self, indirect: bool) -> int:
        """Returns the number of instances for this node."""
    def isChildOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a parent of this one."""
    def isFlagSet(self, flag: int) -> bool:
        """Returns the state of the specified node flag."""
    def isInstanced(self, indirect: bool = True) -> bool:
        """Returns True if this node is instanced."""
    def isInstancedAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute is an instanced attribute of this node."""
    def isLimited(self, type: int) -> bool:
        """Returns True if the specified limit type is enabled."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files."""
    def isParentOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a child of this one."""
    def isTrackingEdits(self) -> bool:
        """Returns True if the node is referenced or in an assembly that is tracking edits."""
    def limitValue(self, type: int) -> float:
        """Returns the value of the specified limit."""
    @staticmethod
    def lineSize() -> float:
        """Returns the manipulator line size."""
    def name(self) -> Any:
        """Returns the node's name."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def parent(self, index: int) -> MObject:
        """Returns the specified parent of this node."""
    def parentCount(self) -> int:
        """Returns the number of parents this node has."""
    def partialPathName(self) -> Any:
        """Returns the minimum path string necessary to uniquely identify the attached object."""
    def plugsAlias(self, plug: MPlug) -> Any:
        """Returns the alias for a plug's attribute."""
    def positionIndex(self) -> int:
        """Returns the index of the position of the StateManip. The data type corresponding to this index is MFnNumericData.k3Double."""
    def removeAttribute(self, attr: MObject, type: Any) -> None:
        """Removes a dynamic attribute from the node."""
    def removeChild(self, node: Any) -> MFnStateManip:
        """Removes the child, specified by MObject, reparenting it under the world."""
    def removeChildAt(self, index: int) -> MFnStateManip:
        """Removes the child, specified by index, reparenting it under the world."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Returns one of the node's attribute, based on the order in which they are written to file."""
    def resetFromRestPosition(self) -> None:
        """Resets the transform from its rest position matrix."""
    def resetTransformation(self, m: MMatrix) -> None:
        """Resets the transform's attribute values to represent the given transformation matrix in world space."""
    def restPosition(self) -> MTransformationMatrix:
        """Returns the transform's rest position matrix."""
    def rotateBy(self, quaternion: MQuaternion | MEulerRotation | int, Space: int | None = None) -> None:
        """Adds an MEulerRotation or MQuaternion to the transform's rotation."""
    def rotateByComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Adds to the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""
    def rotateOrientation(self, space: int) -> MQuaternion:
        """Returns the MQuaternion which orients the local rotation space."""
    def rotatePivot(self, space: int) -> MPoint:
        """Returns the transform's rotate pivot."""
    def rotatePivotTranslation(self, space: int) -> MVector:
        """Returns the transform's rotate pivot translation."""
    def rotateXYZValue(self, valIndex: int) -> MEulerRotation:
        """Gets the rotation for the active manipulator."""
    def rotation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotation as an MEulerRotation or MQuaternion."""
    def rotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotation as the individual components of an MEulerRotation or MQuaternion."""
    def rotationOrder(self) -> int:
        """Returns the order of rotations when the transform's rotation is expressed as an MEulerRotation."""
    def scale(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transform's XYZ scale components."""
    def scaleBy(self) -> None:
        """Multiplies the transform's XYZ scale components by a sequence of three floats."""
    def scalePivot(self, space: int) -> MPoint:
        """Returns the transform's scale pivot."""
    def scalePivotTranslation(self, space: int) -> MVector:
        """Returns the transform's scale pivot translation."""
    def setAffectsAnimation(self) -> None:
        """Specifies that modifications to a node could potentially affect the animation."""
    def setAlias(self, alias: Any, name: Any, plug: MPlug, add: bool | None = None) -> bool:
        """Adds or removes an attribute alias."""
    def setDoNotWrite(self, flag: bool) -> None:
        """Used to prevent the node from being written to file."""
    @staticmethod
    def setDrawPlaneHandles(bool: bool) -> None:
        """Sets the global option to display planar handles or not on supported manipulators."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> None:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> None:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> None:
        """Sets the state of the specified node flag."""
    @staticmethod
    def setGlobalSize(float: float) -> None:
        """Sets the global manipulator size."""
    @staticmethod
    def setHandleSize(float: float) -> None:
        """Sets the manipulator handle size."""
    def setInitialState(self, initialState: int) -> MFnStateManip:
        """Sets the initial state of the StateManip."""
    def setLimit(self, type: int, value: float) -> None:
        """Sets the value of the specified limit."""
    @staticmethod
    def setLineSize(float: float) -> None:
        """Sets the manipulator line size."""
    def setName(self, name: Any, createNamespace: bool | None = None) -> Any:
        """Sets the node's name."""
    def setObject(self, arg: MDagPath | MObject) -> MFnStateManip:
        """Attaches the function set to the specified node or DAG path."""
    def setRestPosition(self, matrix: MTransformationMatrix) -> None:
        """Sets the transform's rest position matrix."""
    def setRotateOrientation(self, quat: MQuaternion, space: int, balance: bool) -> None:
        """Sets the MQuaternion which orients the local rotation space."""
    def setRotatePivot(self, point: MPoint, space: int, balance: bool) -> None:
        """Sets the transform's rotate pivot."""
    def setRotatePivotTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's rotate pivot translation."""
    def setRotation(self, quaternion: MQuaternion | MEulerRotation | int, Space: int | None = None) -> None:
        """Sets the transform's rotation using an MEulerRotation or MQuaternion."""
    def setRotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""
    def setRotationOrder(self, order: int, reorder: bool) -> None:
        """Sets the transform's rotation order."""
    def setScale(self) -> None:
        """Sets the transform's scale components."""
    def setScalePivot(self, point: MPoint, space: int, balance: bool) -> None:
        """Sets the transform's scale pivot."""
    def setScalePivotTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's scale pivot translation."""
    def setShear(self) -> None:
        """Sets the transform's shear."""
    def setTransformation(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's attribute values to represent the given transformation matrix."""
    def setTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's translation."""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def shear(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transform's shear components."""
    def shearBy(self) -> None:
        """Multiplies the transform's shear components by a sequence of three floats."""
    def state(self) -> int:
        """Returns the current state."""
    def stateIndex(self) -> int:
        """Returns the index of the state. The data type corresponding to this index is a int integer."""
    def transformation(self) -> MTransformationMatrix:
        """Returns the transformation matrix represented by this transform."""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
    def translateBy(self, vec: MVector, space: int) -> None:
        """Adds an MVector to the transform's translation."""
    def translation(self, Space: int) -> MVector:
        """Returns the transform's translation as an MVector."""
    def type(self) -> int:
        """Returns the type of the function set."""
    def uniqueName(self) -> Any:
        """For a DAG node, the unique name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself. For a non-DAG node, the uniqueName is just its name."""
    def userNode(self) -> MPxNode:
        """Returns the MPxNode object for a plugin node."""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnToggleManip:
    boundingBox: Any
    direction: Any
    inModel: Any
    inUnderWorld: Any
    isDefaultNode: Any
    isFromReferencedFile: Any
    isInstanceable: Any
    isIntermediateObject: Any
    isLocked: Any
    isOptimizePlaybackOn: Any
    isShared: Any
    isVisible: Any
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
    length: Any
    manipScale: Any
    namespace: Any
    objectColor: Any
    objectColorRGB: Any
    objectColorType: Any
    pluginName: Any
    startPoint: Any
    toggle: Any
    typeId: Any
    typeName: Any
    useObjectColor: Any
    def __init__(self, object: MObject | MDagPath | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def absoluteName(self) -> Any:
        """Returns the absolute name of this node.  The absolute name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself.  Regardless of relative name mode, absoluteName() will always return a full namespace path prefixed with a leading colon (the root namespace).  If the underlying node is a DAG node, then absoluteName() does not guarantee uniqueness, that is, two dependency nodes could have the same absoluteName().  In cases like this the uniqueName() method will guarantee that the name uniquely identifies the node."""
    def addAttribute(self, attr: MObject, type: Any) -> None:
        """Adds a new dynamic attribute to the node."""
    def addChild(self, node: int, index: bool, keepExistingParents: bool = False) -> MFnToggleManip:
        """Makes a node a child of this one."""
    def addExternalContentForFileAttr(self, attr: MObject) -> MExternalContentInfoTable:
        """Adds content info to the specified table from a file path attribute."""
    def affectsAnimation(self) -> bool:
        """Returns true if the changes to the node may affect animation."""
    @staticmethod
    def allocateFlag(pluginName: Any) -> int:
        """Allocates a flag on all nodes for use by the named plugin and returns the flag's index."""
    def attribute(self, index: Any) -> MObject:
        """Returns an attribute of the node, given either its index or name."""
    def attributeClass(self, attr: MObject) -> Any:
        """Returns the class of the specified attribute."""
    def attributeCount(self) -> int:
        """Returns the number of attributes on the node."""
    @staticmethod
    def balanceTransformation(identity: int, identity_: int, one: int, kXYZ: int, arg: Any = None) -> None:
        """Balance a transformation when applying a world matrix to a joint. Thisaccesses the same underlying functionality as the xform command."""
    def canBeWritten(self) -> bool:
        """Returns true if the node will be written to file."""
    def child(self, index: int) -> MObject:
        """Returns the specified child of this node."""
    def childCount(self) -> int:
        """Returns the number of nodes which are children of this one."""
    @staticmethod
    def classification(nodeTypeName: Any) -> Any:
        """Returns the classification string for the named node type."""
    def clearRestPosition(self) -> None:
        """Clears the transform's rest position matrix."""
    def connectToTogglePlug(self, togglePlug: Any) -> MFnToggleManip:
        """Connect to the toggle plug. The data type corresponding to the togglePlug is a boolean value."""
    def create(self, manipName: Any = None, toggleName: Any = None) -> MObject:
        """Creates a new ToggleManip."""
    def dagPath(self) -> MDagPath:
        """Returns the DAG path to which this function set is attached. Raises a TypeError if the function set is attached to an MObject rather than a path."""
    def dagRoot(self) -> MObject:
        """Returns the root node of the first path leading to this node."""
    @staticmethod
    def deallocateAllFlags(pluginName: Any) -> None:
        """Deallocates all node flags which are currently allocated to the named plugin."""
    @staticmethod
    def deallocateFlag(pluginName: Any, flag: int) -> None:
        """Deallocates the specified node flag, which was previously allocated by the named plugin using allocateFlag()."""
    @staticmethod
    def deleteManipulator(manip: Any) -> None:
        """Delete a manipulator.  This method should be used to delete manipulators that have been created using base manipulator create() methods."""
    def dgCallbackIds(self, type: Any, callbackName: Any) -> tuple[Any]:
        """Returns DG timing information for a specific callback type, broken down by callbackId."""
    def dgCallbacks(self, type: Any) -> tuple[Any]:
        """Returns DG timing information broken down by callback type."""
    def dgTimer(self, timerMetric: Any, timerType: Any) -> float:
        """Returns a specific DG timer metric for a given timer type."""
    def dgTimerOff(self) -> None:
        """Turns DG timing off for this node."""
    def dgTimerOn(self) -> None:
        """Turns DG timing on for this node."""
    def dgTimerQueryState(self) -> Any:
        """Returns the current DG timer state for this node."""
    def dgTimerReset(self) -> None:
        """Resets all DG timers for this node."""
    def directionIndex(self) -> int:
        """Returns the index of the direction. The data type corresponding to this index is MFnNumericData.k3Double."""
    @staticmethod
    def drawPlaneHandles() -> bool:
        """This method returns the global option that says if the planar manipulator handles should be drawn or not.Setting this will affect the drawing of all manipulators that support the planar handles."""
    def duplicate(self, instance: bool = False, instanceLeaf: bool = False) -> MObject:
        """Duplicates the DAG hierarchy rooted at the current node."""
    def enableLimit(self, type: int, flag: bool) -> None:
        """Enables or disables a specified limit type."""
    def findAlias(self, alias: Any, attrObj: MObject) -> bool:
        """Returns the attribute which has the given alias."""
    def findPlug(self, attr: Any, wantNetworkedPlug: bool) -> MPlug:
        """Returns a plug for the given attribute."""
    def fullPathName(self) -> Any:
        """Returns the full path of the attached object, from the root of the DAG on down."""
    def getAffectedAttributes(self, attr: MObject) -> MObjectArray:
        """Returns all of the attributes which are affected by the specified attribute."""
    def getAffectingAttributes(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all of the attributes which affect the specified attribute."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute aliases."""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns all of the node's attribute aliases."""
    def getAllPaths(self) -> MDagPathArray:
        """Returns all of the DAG paths which lead to the object to which this function set is attached."""
    def getConnectedSetsAndMembers(self, instance: int, arg: bool, MObjectArray: Any) -> Any:
        """Returns a tuple containing an array of sets and an array of the"""
    def getConnections(self) -> MPlugArray:
        """Returns all the plugs which are connected to attributes of this node."""
    def getExternalContent(self) -> MExternalContentInfoTable:
        """Gets the external content (files) that this node depends on."""
    def getPath(self) -> MDagPath:
        """Returns the DAG path to which this function set is attached, or the first path to the node if the function set is attached to an MObject."""
    @staticmethod
    def globalSize() -> float:
        """Returns the global manipulator size."""
    @staticmethod
    def handleSize() -> float:
        """Returns the manipulator handle size."""
    def hasAttribute(self, name: Any) -> bool:
        """Returns True if the node has an attribute with the given name."""
    def hasChild(self, node: MObject) -> bool:
        """Returns True if the specified node is a child of this one."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def hasParent(self, node: MObject) -> bool:
        """Returns True if the specified node is a parent of this one."""
    def hasUniqueName(self) -> bool:
        """Returns True if the node's name is unique."""
    def instanceCount(self, indirect: bool) -> int:
        """Returns the number of instances for this node."""
    def isChildOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a parent of this one."""
    def isFlagSet(self, flag: int) -> bool:
        """Returns the state of the specified node flag."""
    def isInstanced(self, indirect: bool = True) -> bool:
        """Returns True if this node is instanced."""
    def isInstancedAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute is an instanced attribute of this node."""
    def isLimited(self, type: int) -> bool:
        """Returns True if the specified limit type is enabled."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files."""
    def isParentOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a child of this one."""
    def isTrackingEdits(self) -> bool:
        """Returns True if the node is referenced or in an assembly that is tracking edits."""
    def lengthIndex(self) -> int:
        """Returns the index of the length of the ToggleManip. The data type corresponding to this index is a double."""
    def limitValue(self, type: int) -> float:
        """Returns the value of the specified limit."""
    @staticmethod
    def lineSize() -> float:
        """Returns the manipulator line size."""
    def name(self) -> Any:
        """Returns the node's name."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def parent(self, index: int) -> MObject:
        """Returns the specified parent of this node."""
    def parentCount(self) -> int:
        """Returns the number of parents this node has."""
    def partialPathName(self) -> Any:
        """Returns the minimum path string necessary to uniquely identify the attached object."""
    def plugsAlias(self, plug: MPlug) -> Any:
        """Returns the alias for a plug's attribute."""
    def removeAttribute(self, attr: MObject, type: Any) -> None:
        """Removes a dynamic attribute from the node."""
    def removeChild(self, node: Any) -> MFnToggleManip:
        """Removes the child, specified by MObject, reparenting it under the world."""
    def removeChildAt(self, index: int) -> MFnToggleManip:
        """Removes the child, specified by index, reparenting it under the world."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Returns one of the node's attribute, based on the order in which they are written to file."""
    def resetFromRestPosition(self) -> None:
        """Resets the transform from its rest position matrix."""
    def resetTransformation(self, m: MMatrix) -> None:
        """Resets the transform's attribute values to represent the given transformation matrix in world space."""
    def restPosition(self) -> MTransformationMatrix:
        """Returns the transform's rest position matrix."""
    def rotateBy(self, quaternion: MQuaternion | MEulerRotation | int, Space: int | None = None) -> None:
        """Adds an MEulerRotation or MQuaternion to the transform's rotation."""
    def rotateByComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Adds to the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""
    def rotateOrientation(self, space: int) -> MQuaternion:
        """Returns the MQuaternion which orients the local rotation space."""
    def rotatePivot(self, space: int) -> MPoint:
        """Returns the transform's rotate pivot."""
    def rotatePivotTranslation(self, space: int) -> MVector:
        """Returns the transform's rotate pivot translation."""
    def rotateXYZValue(self, valIndex: int) -> MEulerRotation:
        """Gets the rotation for the active manipulator."""
    def rotation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotation as an MEulerRotation or MQuaternion."""
    def rotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotation as the individual components of an MEulerRotation or MQuaternion."""
    def rotationOrder(self) -> int:
        """Returns the order of rotations when the transform's rotation is expressed as an MEulerRotation."""
    def scale(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transform's XYZ scale components."""
    def scaleBy(self) -> None:
        """Multiplies the transform's XYZ scale components by a sequence of three floats."""
    def scalePivot(self, space: int) -> MPoint:
        """Returns the transform's scale pivot."""
    def scalePivotTranslation(self, space: int) -> MVector:
        """Returns the transform's scale pivot translation."""
    def setAffectsAnimation(self) -> None:
        """Specifies that modifications to a node could potentially affect the animation."""
    def setAlias(self, alias: Any, name: Any, plug: MPlug, add: bool | None = None) -> bool:
        """Adds or removes an attribute alias."""
    def setDoNotWrite(self, flag: bool) -> None:
        """Used to prevent the node from being written to file."""
    @staticmethod
    def setDrawPlaneHandles(bool: bool) -> None:
        """Sets the global option to display planar handles or not on supported manipulators."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> None:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> None:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> None:
        """Sets the state of the specified node flag."""
    @staticmethod
    def setGlobalSize(float: float) -> None:
        """Sets the global manipulator size."""
    @staticmethod
    def setHandleSize(float: float) -> None:
        """Sets the manipulator handle size."""
    def setLimit(self, type: int, value: float) -> None:
        """Sets the value of the specified limit."""
    @staticmethod
    def setLineSize(float: float) -> None:
        """Sets the manipulator line size."""
    def setName(self, name: Any, createNamespace: bool | None = None) -> Any:
        """Sets the node's name."""
    def setObject(self, arg: MDagPath | MObject) -> MFnToggleManip:
        """Attaches the function set to the specified node or DAG path."""
    def setRestPosition(self, matrix: MTransformationMatrix) -> None:
        """Sets the transform's rest position matrix."""
    def setRotateOrientation(self, quat: MQuaternion, space: int, balance: bool) -> None:
        """Sets the MQuaternion which orients the local rotation space."""
    def setRotatePivot(self, point: MPoint, space: int, balance: bool) -> None:
        """Sets the transform's rotate pivot."""
    def setRotatePivotTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's rotate pivot translation."""
    def setRotation(self, quaternion: MQuaternion | MEulerRotation | int, Space: int | None = None) -> None:
        """Sets the transform's rotation using an MEulerRotation or MQuaternion."""
    def setRotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""
    def setRotationOrder(self, order: int, reorder: bool) -> None:
        """Sets the transform's rotation order."""
    def setScale(self) -> None:
        """Sets the transform's scale components."""
    def setScalePivot(self, point: MPoint, space: int, balance: bool) -> None:
        """Sets the transform's scale pivot."""
    def setScalePivotTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's scale pivot translation."""
    def setShear(self) -> None:
        """Sets the transform's shear."""
    def setTransformation(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's attribute values to represent the given transformation matrix."""
    def setTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's translation."""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def shear(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transform's shear components."""
    def shearBy(self) -> None:
        """Multiplies the transform's shear components by a sequence of three floats."""
    def startPointIndex(self) -> int:
        """Returns the index of the start point of the ToggleManip. The data type corresponding to this index is MFnNumericData.k3Double."""
    def toggleIndex(self) -> int:
        """Returns the index of the toggle of the ToggleManip. The data type corresponding to this index is a boolean."""
    def transformation(self) -> MTransformationMatrix:
        """Returns the transformation matrix represented by this transform."""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
    def translateBy(self, vec: MVector, space: int) -> None:
        """Adds an MVector to the transform's translation."""
    def translation(self, Space: int) -> MVector:
        """Returns the transform's translation as an MVector."""
    def type(self) -> int:
        """Returns the type of the function set."""
    def uniqueName(self) -> Any:
        """For a DAG node, the unique name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself. For a non-DAG node, the uniqueName is just its name."""
    def userNode(self) -> MPxNode:
        """Returns the MPxNode object for a plugin node."""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MHWShaderSwatchGenerator:
    renderQuality: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def cancelCurrentSwatchRender() -> None:
        """The method cancels the swatch which is being rendered in parallel, and push the swatch render item back to the render queue after. """
    def cancelParallelRendering(self) -> MHWShaderSwatchGenerator:
        """Method to cancel the parallel rendering."""
    @staticmethod
    def createObj(obj: Any, renderObj: Any, res: Any) -> MSwatchRenderBase:
        """Class constructor."""
    def doIteration(self) -> bool:
        """Method called from the MSwatchRenderRegister for generation of swatch image. The doIteration function is called repeatedly (during idle events) until it returns true. Using this swatch image can be generated in stages."""
    def finishParallelRender(self) -> MHWShaderSwatchGenerator:
        """Method to update the swatch image when the parallel rendering is finished."""
    @staticmethod
    def getSwatchBackgroundColor() -> MColor:
        """Returns the default background color for the hardware rendered swatch."""
    def image(self) -> MImage:
        """This method returns the render swatch as an image."""
    @staticmethod
    def initialize() -> Any:
        """This method sets a swatch name, and registers a new swatch generator creation function for the swatch name."""
    def node(self) -> MObject:
        """This method returns the node that is used to compute the swatch."""
    def renderParallel(self) -> bool:
        """Method indicates if the swatch is rendered parallel."""
    def resolution(self) -> int:
        """This method returns the expected resolution of the swatch."""
    def swatchNode(self) -> MObject:
        """This method returns the node for which the swatch is required to be generated."""

class MManipData:
    def __init__(self, arg: Any = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def asBool(self) -> bool:
        """Returns the manipulator data as a bool"""
    def asDouble(self) -> float:
        """Returns the manipulator data as a double"""
    def asFloat(self) -> float:
        """Returns the manipulator data as a float"""
    def asLong(self) -> int:
        """Returns the manipulator data as a long"""
    def asMObject(self) -> int:
        """Returns the manipulator data as an MObject."""
    def asShort(self) -> int:
        """Returns the manipulator data as a short"""
    def asUnsigned(self) -> int:
        """Returns the manipulator data as a unsigned"""
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
    def __init__(self, in_: MMaterial | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def applyTexture(self, view: Any, data: Any) -> MMaterial:
        """For materials that have texture, this method must be used before the OpenGL drawing to apply the texture to the current view."""
    @staticmethod
    def defaultMaterial() -> MMaterial:
        """Get the default material. There will always be a default material in the scene and therefore the result of this function should always succeed.  The default material will correspond to the initialShadingGroup node that is in the scene."""
    def evaluateDiffuse(self) -> MMaterial:
        """Perform necessary evaluation to be able to get diffuse back."""
    def evaluateEmission(self) -> MMaterial:
        """Perform necessary evaluation to be able to get emission back."""
    def evaluateMaterial(self, view: Any, path: Any) -> MMaterial:
        """Evaluate a material. Must be called before evaluating or getting any material properties."""
    def evaluateShininess(self) -> MMaterial:
        """Perform necessary evaluation to be able to get shininess back."""
    def evaluateSpecular(self) -> MMaterial:
        """Perform necessary evaluation to be able to get specular back."""
    def evaluateTexture(self, data: Any) -> MMaterial:
        """Evaluate texturing related information. Must be called before getting any texture properties such as getHasTransparency(), getTextureTransformation() and applyTexture()."""
    def getDiffuse(self) -> MColor:
        """Get the GL diffuse color."""
    def getEmission(self) -> MColor:
        """Get the GL emission color."""
    def getHasTransparency(self) -> bool:
        """Returns True if material or texture has transparency, False otherwise."""
    def getHwShaderNode(self) -> MPxHwShaderNode:
        """Get the hardware shader node."""
    def getShininess(self) -> float:
        """Get the GL shininess."""
    def getSpecular(self) -> MColor:
        """Get the GL specular color."""
    def getTextureTransformation(self, data: MDrawData, texXform: Any) -> MMaterial:
        """getTextureTransformation(data) -> [float, float, float, float, float, float]"""
    def materialIsTextured(self) -> bool:
        """Returns True if the material is textured, False otherwise."""
    def setMaterial(self, path: bool, hasTransparency: Any) -> MMaterial:
        """Set the current GL material."""
    def shadingEngine(self) -> MObject:
        """Get the shading engined associated with this material."""
    def textureImage(self, image: Any, color: int, chan: int, dagPath: Any, xRes: int = -1, yRes: int = -1) -> MMaterial:
        """For materials that have texture, this method will attempt to retrieve the pixel map for a given mapped channel of that material."""

class MMaterialArray:
    sizeIncrement: Any
    def __init__(self, other: MMaterialArray | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def append(self, element: MMaterial) -> MMaterialArray:
        """Adds a new element to the end of the array."""
    def clear(self) -> MMaterialArray:
        """Clear the contents of the array. After this operation the length will be 0.  This does not change the amount of memory allocated to the array, only the number of valid elements in it."""
    def copy(self, source: MMaterialArray) -> MMaterialArray:
        """Copy the contents of the source array to this array."""
    def insert(self, element: MMaterial, index: int) -> MMaterialArray:
        """Inserts a new value into the array at the given index. The initial element at that index, and all following elements, are shifted towards the last."""
    def remove(self, index: int) -> MMaterialArray:
        """Removes the element in the array at the given index."""
    def set(self, element: MMaterial, index: int) -> MMaterialArray:
        """Sets the value of the specified element to the given attribute spec."""
    def setLength(self, length: int) -> MMaterialArray:
        """Set the length of the array. This will grow and shrink the array as desired. Elements that are grown have uninitialized values, while those which are shrunk will lose the data contained in the deleted elements"""

class MPaintMessage:
    kDefaultAction: Any
    kDoAction: Any
    kDoNotDoAction: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def addVertexColorCallback(function: Any, clientData: None = None) -> int:
        """Adds a new callback on vertex color paint."""
    @staticmethod
    def currentCallbackId() -> int:
        """Returns the callback ID of the currently executing callback. If called"""
    @staticmethod
    def nodeCallbacks(node: Any) -> int:
        """Returns a list of callback IDs registered to a given node."""
    @staticmethod
    def removeCallback(id: Any) -> None:
        """Removes the specified callback from Maya."""
    @staticmethod
    def removeCallbacks(ids: Any) -> None:
        """Removes all of the specified callbacks from Maya."""

class MPanelCanvas:
    kGraphEditorAxisLabels: Any
    kGraphEditorBackground: Any
    kGraphEditorCurveNames: Any
    kGraphEditorCurves: Any
    kGraphEditorFirstDefaultDraw: Any
    kGraphEditorGrid: Any
    kGraphEditorLastDefaultDraw: Any
    kGraphEditorOverlayTexture: Any
    kGraphEditorRetimeToolText: Any
    kGraphEditorTimeMarker: Any
    kGraphEditorUndefined: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addPrimitive(self, int: Any, int_: Any) -> Any:
        """Add the primitive referred to by the given id to the list of"""
    def createFloatVertexBuffer(self, tVals: Any, yVals: Any, colors: Any) -> int:
        """Create a vertex buffer with float values as the x-coordinate."""
    def createPrimitive(self, primType: Any, bufferId: Any, startIndex: Any, numVertices: Any, props: Any) -> int:
        """Create a primitive of the given type using the vertex buffer"""
    def createTimeVertexBuffer(self, tVals: Any, yVals: Any, colors: Any) -> int:
        """Create a vertex buffer with time values as the x-coordinate."""
    def destroyPrimitive(self, primitiveId: Any) -> Any:
        """Destroy the primitive referred to by the given id."""
    def destroyVertexBuffer(self, bufferId: Any) -> Any:
        """Destroy the vertex buffer referred to by the given id.  If the."""
    def isAutoRefresh(self) -> bool:
        """Returns whether the associated editor will automatically refresh."""
    def isLayerVisible(self, int: Any) -> bool:
        """Return whether the given layer is visible."""
    def isValid(self) -> bool:
        """Returns True if MPanelCanvas has a valid pointer to a Graph"""
    def refresh(self) -> Any:
        """Force the associated Graph Editor to refresh"""
    def registerDrawUICallback(self, layer: Any, cb: Any, clientData: Any) -> Any:
        """Register a callback to be called when the given panel is drawing"""
    def removePrimitive(self, int: Any, int_: Any) -> Any:
        """Remove the primitive referred to by the given id from the list of"""
    def setAutoRefresh(self) -> Any:
        """Set whether the associated editor will be automatically refreshed."""
    def setLayerVisible(self, int: Any, bool: Any) -> Any:
        """Set whether the given layer will be drawn. All layers are"""
    def supportsUIDrawing(self) -> bool:
        """Returns whether the attached panel control supports drawing"""
    def unregisterDrawUICallback(self, callbackId: Any) -> Any:
        """Unregister the callback specified by the given id."""

class MPanelCanvasInfo:
    def __init__(self, editorName: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getViewportBounds(self) -> Any:
        """Returns an array of four values representing the corners of the"""
    def getViewportSize(self) -> Any:
        """Returns an array of two values representing the size of the"""
    def name(self) -> str:
        """Return the name of the currently attached panel."""
    def setViewportBounds(self, bounds: float | MDoubleArray) -> Any:
        """Set the bounds of the editor's viewing region. The passed."""
    def supportsUIDrawing(self) -> bool:
        """Returns whether the attached panel control supports drawing"""

class MPxContext:
    kImage1: Any
    kImage2: Any
    kImage3: Any
    def __init__(self) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def abortAction(self) -> None:
        """This method is called when the abort key is pressed."""
    def addManipulator(self, manipulator: MObject) -> None:
        """This method adds a manipulator to the context."""
    def argTypeNumericalInput(self, index: int) -> Any:
        """This method is used by the feedback line to determine what units to display."""
    def beginMarquee(self, event: Any) -> MPxContext:
        """Start drawing a dragged out marquee box."""
    def completeAction(self) -> None:
        """This method is called when the complete key is pressed."""
    def deleteAction(self) -> None:
        """This method is called when the delete or backspace key is pressed."""
    def deleteManipulators(self) -> None:
        """This method deletes all the manipulators that belong"""
    def doDrag(self, event: int, drawMgr: Any, context: Any) -> None:
        """This method is called when a mouse drag event occurs."""
    def doDragLegacy(self, event: Any) -> None:
        """This method is called when a mouse drag event occurs."""
    def doEnterRegion(self, event: Any) -> None:
        """This method is called when a mouse enters the viewport."""
    def doExitRegion(self, event: Any) -> None:
        """This method is called when a mouse exits the viewport."""
    def doHold(self, event: int, drawMgr: Any, context: Any) -> None:
        """This method is called when a mouse button is pressed but"""
    def doHoldLegacy(self, event: Any) -> None:
        """This method is called when a mouse button is pressed but"""
    def doPress(self, event: int, drawMgr: Any, context: Any) -> None:
        """This method is called when any mouse button is pressed."""
    def doPressLegacy(self, event: Any) -> None:
        """This method is called when any mouse button is pressed."""
    def doPtrMoved(self, event: int, drawMgr: Any, context: Any) -> None:
        """This method is called when a mouse move event occurs."""
    def doPtrMovedLegacy(self, event: Any) -> None:
        """This method is called when a mouse drag event occurs."""
    def doRelease(self, event: int, drawMgr: Any, context: Any) -> None:
        """This method is called when any mouse button is released."""
    def doReleaseLegacy(self, event: Any) -> None:
        """This method is called when any mouse button is released."""
    def dragMarquee(self, event: Any) -> MPxContext:
        """Draws a rectangle representing the dragged out area initiated with"""
    def drawFeedback(self, event: int, drawMgr: Any, context: Any) -> None:
        """This method is called to draw primitives when your context is activated"""
    def feedbackNumericalInput(self) -> bool:
        """This method is called to update the numerical feedback."""
    def helpStateHasChanged(self, event: Any) -> None:
        """This method is called whenever the help state may need to be"""
    def image(self, index: Any) -> Any:
        """This method is used to retrieve an XPM icon image that has"""
    def inAlternateContext(self) -> bool:
        """This method is called to determine if an alternate context is active."""
    def newToolCommand(self) -> MPxToolCommand:
        """Create a new instance of the tool command associated with this context."""
    def processNumericalInput(self, values: MDoubleArray, flags: MIntArray, isAbsolute: bool) -> bool:
        """This method processes the input from the numerical input field."""
    def releaseMarquee(self, arg: Any, left: Any, bottom: Any, right: Any) -> Any:
        """End the marquee drawing cycle and return the coordinates corresponding to"""
    def setCursor(self, newCursor: MCursor) -> MPxContext:
        """Set the cursor used by the context to the MCursor that is passed in."""
    def setHelpString(self, str: Any) -> MPxContext:
        """Set the help string to the given MString."""
    def setImage(self, image: Any, index: Any) -> MPxContext:
        """This method is used to set an XPM icon image that is to be"""
    def setTitleString(self, str: Any) -> MPxContext:
        """Set the title of the context to the MString that is passed in."""
    def stringClassName(self) -> Any:
        """This method is called to determine the name that uniquely identifies"""
    def toolOffCleanup(self) -> None:
        """This method is called when the context is deactivated, i.e when"""
    def toolOnSetup(self, event: Any) -> None:
        """This method is called when the context is activated, i.e when"""

class MPxContextCommand:
    def __init__(self) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def appendSyntax(self) -> None:
        """This method should be overridden to append syntax"""
    def doEditFlags(self) -> None:
        """This method is called when the command is called in edit mode."""
    def doQueryFlags(self) -> None:
        """This method is called when the command is called in query mode."""
    def makeObj(self) -> MPxContext:
        """This function is used to instantiate a proxy context."""
    def parser(self) -> MArgParser:
        """Returns the context command's MArgParser object, if it has one."""
    def setResult(self, result: Any) -> None:
        """Set the value of the result to be returned by the command.  The value can be"""
    def syntax(self) -> MSyntax:
        """Returns the context command's MSyntax object, if it has one."""

class MPxDragAndDropBehavior:
    def __init__(self, init: None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def connectAttrToAttr(self, sourcePlug: bool, destinationPlug: Any, force: Any) -> None:
        """This method is called by the defaultNavigation command to connect a source attribute to a destination attribute."""
    def connectAttrToNode(self, sourcePlug: bool, destinationNode: Any, force: Any) -> None:
        """This method is called by the defaultNavigation command to connect a source attribute to a destination node."""
    def connectNodeToAttr(self, sourceNode: bool, destinationPlug: Any, force: Any) -> None:
        """This method is called by the defaultNavigation command to connect a source node to a destination attribute."""
    def connectNodeToNode(self, sourceNode: bool, destinationNode: Any, force: Any) -> None:
        """This method is called by the defaultNavigation command to connect a source node to a destination node."""
    def shouldBeUsedFor(self, sourceNode: MObject, destinationNode: MObject, sourcePlug: MPlug, destinationPlug: MPlug) -> bool:
        """This method must be overridden in order to use a drag and drop behavior."""

class MPxHardwareShader:
    kAssembly: Any
    kBlendShape: Any
    kCameraSetNode: Any
    kClientDeviceNode: Any
    kConstraintNode: Any
    kDeformerNode: Any
    kDependNode: Any
    kEmitterNode: Any
    kEvaluatedDirectly: Any
    kEvaluatedIndirectly: Any
    kFieldNode: Any
    kFluidEmitterNode: Any
    kGeometryFilter: Any
    kHardwareShader: Any
    kHwShaderNode: Any
    kIkSolverNode: Any
    kImagePlaneNode: Any
    kIsTransparent: Any
    kLast: Any
    kLeaveDirty: Any
    kLocatorNode: Any
    kManipContainer: Any
    kManipulatorNode: Any
    kMotionPathNode: Any
    kNoTransparencyFrontBackCull: Any
    kNoTransparencyPolygonSort: Any
    kObjectSet: Any
    kParticleAttributeMapperNode: Any
    kPostEvaluationTypeLast: Any
    kSkinCluster: Any
    kSpringNode: Any
    kSurfaceShape: Any
    kThreadedDeviceNode: Any
    kTransformNode: Any
    outColor: Any
    outColorB: Any
    outColorG: Any
    outColorR: Any
    def __init__(self) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def addAttribute(attr: MObject) -> None:
        """This method adds a new attribute to a user defined node type during the type's initialization."""
    def addExternalContentForFileAttr(self, table: MObject, attr: Any) -> bool:
        """This method is a helper for derived clases implementing getExternalContent().  It augments the external content info table passed in with an entry describing external content whose location is described by the specified attribute."""
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> None:
        """This method specifies that a particular input attribute affects a specific output attribute.  This is required to make evaluation efficient.  When an input changes, only the affected outputs will be computed. Output attributes cannot be keyable - if they are keyable, this method will fail."""
    def compute(self, plug: Any, dataBlock: Any) -> MPxHardwareShader:
        """This method should be overridden in user defined nodes."""
    def configCache(self, evalNode: Any, schema: Any) -> None:
        """Defines the node's behavior when participating in Cached Playback."""
    def connectionBroken(self, plug: bool, otherPlug: Any, asSrc: Any) -> MPxHardwareShader:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, plug: bool, otherPlug: Any, asSrc: Any) -> MPxHardwareShader:
        """This method gets called when connections are made to attributes of this node."""
    def copyInternalData(self, node: Any) -> MPxHardwareShader:
        """This method is overriden by nodes that store attribute data in some internal format."""
    def dependsOn(self, plug: Any, otherPlug: Any) -> Any:
        """This method may be overridden by the user defined node. It should only be required to override this on rare occasions."""
    def doNotWrite(self) -> bool:
        """use this method to query the "do not write" state of this proxy node. True is returned if this node will not be saved when the maya model is written out."""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    @staticmethod
    def findResource(name: Any, shaderPath: Any) -> Any:
        """This is a static utility to find the full path to a shader resource (typically a texture). This method will search the list of paths in the MAYA_HW_SHADER_RESOURCE_PATH environment variable, resolving relative paths based on the directory containing the shader."""
    def forceCache(self, ctx: Any) -> MDataBlock:
        """Get the datablock for this node. If there is no datablock then one will be created."""
    def getAvailableImages(self, context: int, uvSetName: Any) -> list[Any]:
        """Maya will call this method to get your shader's list of images which are available for use in the UV texture editor for the UV set specified. Typically, this list will include one entry for each texture using the specified UV set, however, your shader is free to return as many images as you wish (for example, blending between two textures, texture alpha masks, artificially shaded views of bump/normal maps, etc). Your shader's renderImage() method will be used to render the images themselves."""
    def getCacheSetup(self, evalNode: Any, disablingInfo: Any, setupInfo: Any, objectArray: Any) -> None:
        """Provide node-specific setup info for the Cached Playback system."""
    def getExternalContent(self, table: Any) -> MPxHardwareShader:
        """The table populated by this method must include the location of all the content (files) used by this node, including those that do not exist.  See MExternalContentInfoTable for details."""
    def getFilesToArchive(self, shortName: bool = False, unresolvedName: bool = False, markCouldBeImageSequence: bool = False) -> list[str]:
        """Use this method to return all external files used by this node. This file list will be used by the File > Archive zip feature, maya.exe -archive and the `file -q -list` mel command."""
    @staticmethod
    def getHardwareShader(object: Any) -> Any:
        """This is a static convenience method to be able to get an MPxHardwareShader from an MObject provided by a swatch generator class (Class derived from MSwatchRenderRegister)."""
    def getInternalValue(self, plug: Any, dataHandle: Any) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def getInternalValueInContext(self, plug: Any, dataHandle: Any, ctx: Any) -> Any:
        """This method is obsolete. Override MPxNode.getInternalValue instead."""
    def hasInvalidationRangeTransformation(self) -> bool:
        """Checks if this MPxNode derived node overrides the MPxNode::transformInvalidationRange method"""
    @staticmethod
    def inheritAttributesFrom(parentClassName: Any) -> None:
        """This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node."""
    def internalArrayCount(self, plug: Any) -> int:
        """internalArrayCount(plug, ctx) -> int  [OBSOLETE]"""
    def isAbstractClass(self) -> bool:
        """Override this class to return True if this node is an abstract node. An abstract node can only be used as a base class.  It cannot be created using the 'createNode' command."""
    def isPassiveOutput(self, plug: Any) -> bool:
        """This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent value modifications to the destination attribute. For example, output plugs on animation curve nodes are passive. This allows the attributes driven by the animation curves to be set to new values by the user."""
    def legalConnection(self, plug: bool, otherPlug: Any, asSrc: Any) -> Any:
        """This method allows you to check for legal connections being made to attributes of this node."""
    def legalDisconnection(self, plug: bool, otherPlug: Any, arsSrc: Any) -> Any:
        """This method allows you to check for legal disconnections being made to attributes of this node."""
    def name(self) -> Any:
        """Returns the name of this particular instance of this class.  Each objectin the dependency graph has a name.  This name will be used by the UIand by MEL."""
    def passThroughToMany(self, plug: Any, plugArray: Any) -> bool:
        """This method is overriden by nodes that want to control the traversal behavior of some Maya search algorithms which traverse the history/future of shape nodes looking for directly related nodes. In particular, the Artisan paint code uses this method when searching for paintable nodes, and the disk cache code uses this method when searching for upstream cacheFile nodes."""
    def passThroughToOne(self, plug: Any) -> Any:
        """This method may be overriden by nodes that have a one-to-one relationship between an input attribute and a corresponding output attribute. This method is used by Maya to perform the following capabilities:"""
    def postConstructor(self) -> MPxHardwareShader:
        """Internally maya creates two objects when a user defined node is created, the internal MObject and the user derived object."""
    def postEvaluation(self, context: MDGContext, evalNode: MEvaluationNode, evalType: Any) -> None:
        """Clean up node's internal state after threaded evaluation."""
    def preEvaluation(self, context: MDGContext, evalNode: MEvaluationNode) -> None:
        """Prepare a node's internal state for threaded evaluation."""
    def profile(self) -> MRenderProfile:
        """Override this method to specify the renderers your shader supports. If this method is not overridden, Maya will assume your shader supports only Maya's iternal OpenGL based renderer."""
    def renderImage(self, context: int, imageName: Any, region: Any, parameters: int) -> Any:
        """renderImage(context, uiDrawManager, imageName, region, parameters) -> [int, int]/None"""
    def renderSwatchImage(self, image: Any) -> MPxHardwareShader:
        """If the shader specifies to override swatch rendering, then this method must be overridden in order to draw anything into a swatch."""
    def setDependentsDirty(self, plug: MPlug, plugArray: Any) -> MPxHardwareShader:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug which Maya is marking dirty. The list of plugs for Maya to mark dirty is returned by the plug array. This method handles both dynamic as well as non-dynamic plugs and is useful in the following ways:"""
    def setDoNotWrite(self, bool: bool) -> MPxHardwareShader:
        """Use this method to mark the "do not write" state of this proxy node.  If set, this node will not be saved when the Maya model is written out. """
    def setExistWithoutInConnections(self, bool: bool) -> bool:
        """This method specifies whether or not the node can exist without input"""
    def setExistWithoutOutConnections(self, bool: bool) -> bool:
        """This method specifies whether or not the node can exist without"""
    def setExternalContent(self, table: Any) -> MPxHardwareShader:
        """This is useful in the context of content relocation.  This will be called while the scene is being loaded to apply path changes performed externally. Consequently, interaction with the rest of the scene must be kept to a minimum.  It is however valid to call this method outside of scene loading contexts."""
    def setExternalContentForFileAttr(self, attr: MObject, table: Any) -> bool:
        """This method is a helper for derived clases implementing setExternalContent().  It assigns a value to a plug with the one from the table whose key is the same as the passed in attribute name."""
    def setInternalValue(self, plug: Any, dataHandle: Any) -> bool:
        """This method is overriden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self, plug: Any, dataHandle: Any, ctx: Any) -> Any:
        """This method is obsolete. Override MPxNode.setInternalValue instead."""
    def setMPSafe(self, bool: bool) -> MPxHardwareShader:
        """This method is obsolete. Override MPxNode.setSchedulingType instead."""
    def setUniformParameters(self, parameters: MUniformParameterList, remapCurrentValues: bool = True, dagModifier: Any = None) -> MPxHardwareShader:
        """Call this method to set the list of uniform parameters this shader uses. Once set, you can use these parameters to access the cached values of shader parameters, including testing when the value has been updated (to minimise the shader state changes). When using this method to manage uniform parameters, Maya will handle the underlyintg attributes, serialization and user interface for you.It is important to call this method whenever the shader parameters are modified (including at load time).This is an optional method - shader implementations are still free to manage uniform (i.e. shader-level) parameters independently if they wish.* parameters (MUniformParameterList) - the list of uniform parameters for this shader"""
    def setVaryingParameters(self, parameters: MVaryingParameterList, remapCurrentValues: bool = True, dagModifier: Any = None) -> MPxHardwareShader:
        """Call this method to set the list of varying parameters this shader uses. Once set, you can use these parameters directly to access geometry data for surfaces being shaded. When using this method to manage shader varying parameters, there is no need to override populateRequirements or handle the node interface as Maya will handle parameter setup, presentation and configuration for you."""
    def shouldSave(self, plug: Any) -> Any:
        """This method may be overridden by the user defined node.  It should only be required to override this on rare occasions."""
    def thisMObject(self) -> MObject:
        """Returns the MObject associated with this user defined node.  This makes it possible to use MFnDependencyNode or to construct plugs to this node's attributes."""
    def transformInvalidationRange(self, plug: MPlug, timeRange: MTimeRange) -> float:
        """Override this method to register this node as an Invalidation-Range-Transformation kernel (IRT kernel) An IRT kernel node will change the invalidation time range for its downstream nodes For example, Dynamics-solver will transform invalidation time range [a,b] to [a,+inf) And Clip-Time-Editor will send out the invalidation range for each of the clip [a,b] to ( [t0+a,t0+b] U [t1+a,t1+b] U [t2+a,t2+b] U ... ) """
    def transparencyOptions(self) -> int:
        """This method returns transparency options for usage as hints for Maya's internal draw during a given rendering pass. Parameters are returned via an integer containing masked out bits. By default the mask is set to 0, meaning that the drawing should be treated as regular opaque object drawing. This will generally mean one call per draw pass."""
    def type(self) -> int:
        """Returns the type of node that this is.  This is used to differentiate user defined nodes that are derived off different MPx base classes."""
    def typeId(self) -> MTypeId:
        """Returns the TYPEID of this node."""
    def typeName(self) -> Any:
        """Returns the type name of this node.  The type name identifies the node type to the ASCII file format"""

class MPxHwShaderNode:
    kAssembly: Any
    kBlendShape: Any
    kCameraSetNode: Any
    kClientDeviceNode: Any
    kConstraintNode: Any
    kDeformerNode: Any
    kDependNode: Any
    kDirtyAll: Any
    kDirtyColorArrays: Any
    kDirtyNone: Any
    kDirtyNormalArray: Any
    kDirtyTexCoordArrays: Any
    kDirtyVertexArray: Any
    kEmitterNode: Any
    kEvaluatedDirectly: Any
    kEvaluatedIndirectly: Any
    kFieldNode: Any
    kFluidEmitterNode: Any
    kGeometryFilter: Any
    kHardwareShader: Any
    kHwShaderNode: Any
    kIkSolverNode: Any
    kImagePlaneNode: Any
    kIsTransparent: Any
    kLast: Any
    kLeaveDirty: Any
    kLocatorNode: Any
    kManipContainer: Any
    kManipulatorNode: Any
    kMotionPathNode: Any
    kNoTransparencyFrontBackCull: Any
    kNoTransparencyPolygonSort: Any
    kObjectSet: Any
    kParticleAttributeMapperNode: Any
    kPostEvaluationTypeLast: Any
    kSkinCluster: Any
    kSpringNode: Any
    kSurfaceShape: Any
    kThreadedDeviceNode: Any
    kTransformNode: Any
    kWriteAll: Any
    kWriteColorArrays: Any
    kWriteNone: Any
    kWriteNormalArray: Any
    kWriteTexCoordArrays: Any
    kWriteVertexArray: Any
    outColor: Any
    outColorB: Any
    outColorG: Any
    outColorR: Any
    outGlowColor: Any
    outGlowColorB: Any
    outGlowColorG: Any
    outGlowColorR: Any
    outMatteOpacity: Any
    outMatteOpacityB: Any
    outMatteOpacityG: Any
    outMatteOpacityR: Any
    outTransparency: Any
    outTransparencyB: Any
    outTransparencyG: Any
    outTransparencyR: Any
    def __init__(self) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def addAttribute(attr: MObject) -> None:
        """This method adds a new attribute to a user defined node type during the type's initialization."""
    def addExternalContentForFileAttr(self, table: MObject, attr: Any) -> bool:
        """This method is a helper for derived clases implementing getExternalContent().  It augments the external content info table passed in with an entry describing external content whose location is described by the specified attribute."""
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> None:
        """This method specifies that a particular input attribute affects a specific output attribute.  This is required to make evaluation efficient.  When an input changes, only the affected outputs will be computed. Output attributes cannot be keyable - if they are keyable, this method will fail."""
    def bind(self, request: MDrawRequest, view: Any) -> MPxHwShaderNode:
        """This method is invoked for hardware rendering to Maya's 3D view."""
    def colorsPerVertex(self) -> int:
        """This method returns the number of color values per vertex that the hw shader node would like to receive from Maya.  Maya will attempt to provide all the color data that the shader would like but it will never provide more data that is actually available in the shape.  The color sets returned by getColorSetNames() will override the number of color sets specified by colorsPerVertex(). If you do not override this method or getColorSetNames(), Maya will provide no colors per vertex."""
    def compute(self, plug: Any, dataBlock: Any) -> MPxHwShaderNode:
        """This method should be overridden in user defined nodes."""
    def configCache(self, evalNode: Any, schema: Any) -> None:
        """Defines the node's behavior when participating in Cached Playback."""
    def connectionBroken(self, plug: bool, otherPlug: Any, asSrc: Any) -> MPxHwShaderNode:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, plug: bool, otherPlug: Any, asSrc: Any) -> MPxHwShaderNode:
        """This method gets called when connections are made to attributes of this node."""
    def copyInternalData(self, node: Any) -> MPxHwShaderNode:
        """This method is overriden by nodes that store attribute data in some internal format."""
    def currentPath(self) -> MDagPath:
        """This method returns a reference to the current path that the shader is invoked for."""
    def currentShadingEngine(self) -> MObject:
        """This method returns an MObject to the shading engine that is currently being rendered. This method will only return a valid MObject during the following calls:"""
    def dependsOn(self, plug: Any, otherPlug: Any) -> Any:
        """This method may be overridden by the user defined node. It should only be required to override this on rare occasions."""
    def dirtyMask(self) -> int:
        """This method returns a "dirty" mask that indicates which geometry items have changed from the last invocation of the plugin to draw. The mask is valid at the time that geometry() or glGeometry() is called and at no other time."""
    def doNotWrite(self) -> bool:
        """use this method to query the "do not write" state of this proxy node. True is returned if this node will not be saved when the maya model is written out."""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    def forceCache(self, ctx: Any) -> MDataBlock:
        """Get the datablock for this node. If there is no datablock then one will be created."""
    def geometry(self, request: MDrawRequest, view: int, prim: int, writable: int, indexCount: int, indexArray: int, vertexCount: int, vertexIDs: float, vertexArray: int, normalCount: Any, normalArrays: int, colorCount: Any, colorArrays: int, texCoordCount: Any, texCoordArrays: int) -> MPxHwShaderNode:
        """This method is invoked for hardware rendering to Maya's 3D view."""
    def getAvailableImages(self, uvSetName: Any) -> list[Any]:
        """Maya will call this method to get your shader's list of images which are available for use in the UV texture editor for the UV set specified. Typically, this list will include one entry for each texture using the specified UV set, however, your shader is free to return as many images as you wish (for example, blending between two textures, texture alpha masks, artificially shaded views of bump/normal maps, etc). Your shader's renderImage() method will be used to render the images themselves."""
    def getCacheSetup(self, evalNode: Any, disablingInfo: Any, setupInfo: Any, objectArray: Any) -> None:
        """Provide node-specific setup info for the Cached Playback system."""
    def getColorSetNames(self, names: Any) -> int:
        """This method returns an array of color per vertex set names. Maya will attempt to provide color per vertex data from these maps in the corresponding array element in the colorArrays argument to the geometry method.  For example, if the names[2] is "cpv56" then colorArrays[2] will be the array of values from cpv56, or None if the shape being rendered does not have a color set of that name. Ifthis method is not overridden an empty list of names will be returned,and Maya will use colorsPerVertex() to determine how many color setsto provide."""
    def getExternalContent(self, table: Any) -> MPxHwShaderNode:
        """The table populated by this method must include the location of all the content (files) used by this node, including those that do not exist.  See MExternalContentInfoTable for details."""
    def getFilesToArchive(self, shortName: bool = False, unresolvedName: bool = False, markCouldBeImageSequence: bool = False) -> list[str]:
        """Use this method to return all external files used by this node. This file list will be used by the File > Archive zip feature, maya.exe -archive and the `file -q -list` mel command."""
    @staticmethod
    def getHwShaderNode(object: Any) -> MPxHwShaderNode:
        """This is a static convenience method to be able to get an MPxHwShaderNode from an MObject provided by a swatch generator class (Class derived from MSwatchRenderRegister)."""
    def getInternalValue(self, plug: Any, dataHandle: Any) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def getInternalValueInContext(self, plug: Any, dataHandle: Any, ctx: Any) -> Any:
        """This method is obsolete. Override MPxNode.getInternalValue instead."""
    def getTexCoordSetNames(self, names: Any) -> int:
        """This method returns an array of texture coordinate set names. Maya will attempt to provide texture coordinates from these maps in the corresponding array element in the texCoordArrays argument to the geometry method.  For example, if the names[2] is "uvSet3" then texCoordArrays[2] will be the array of values from uvSet3. If this method is not overridden an empty list of names will be returned, and Maya will use texCoordsPerVertex() to determine how many uv sets to provide."""
    def glBind(self, shapePath: MDagPath) -> MPxHwShaderNode:
        """This method should only be overridden for hardware rendering."""
    def glGeometry(self, shapePath: MDagPath, prim: int, writable: int, indexCount: int, indexArray: int, vertexCount: int, vertexIDs: int, vertexArray: float, normalCount: int, normalArrays: Any, colorCount: int, colorArrays: Any, texCoordCount: int, texCoordArrays: Any) -> MPxHwShaderNode:
        """This method should only be overridden for hardware rendering."""
    def glUnbind(self, shapePath: MDagPath) -> MPxHwShaderNode:
        """This method should only be overridden for hardware rendering."""
    def hasInvalidationRangeTransformation(self) -> bool:
        """Checks if this MPxNode derived node overrides the MPxNode::transformInvalidationRange method"""
    def hasTransparency(self) -> bool:
        """This method returns a boolean value that indicates whether the object will be drawn transparently or not.  Transparent objects must be drawn after all the opaque objects in the scene or they will not display correctly.  Maya uses the return value to determine when it can draw this shape."""
    @staticmethod
    def inheritAttributesFrom(parentClassName: Any) -> None:
        """This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node."""
    def internalArrayCount(self, plug: Any) -> int:
        """internalArrayCount(plug, ctx) -> int  [OBSOLETE]"""
    def invertTexCoords(self) -> bool:
        """Specifies whether this shader requires inverted texture coordinates. (i.e. where the top-left hand corner of UV space is (0,0) instead of the bottom-left corner)."""
    def isAbstractClass(self) -> bool:
        """Override this class to return True if this node is an abstract node. An abstract node can only be used as a base class.  It cannot be created using the 'createNode' command."""
    def isPassiveOutput(self, plug: Any) -> bool:
        """This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent value modifications to the destination attribute. For example, output plugs on animation curve nodes are passive. This allows the attributes driven by the animation curves to be set to new values by the user."""
    def legalConnection(self, plug: bool, otherPlug: Any, asSrc: Any) -> Any:
        """This method allows you to check for legal connections being made to attributes of this node."""
    def legalDisconnection(self, plug: bool, otherPlug: Any, arsSrc: Any) -> Any:
        """This method allows you to check for legal disconnections being made to attributes of this node."""
    def name(self) -> Any:
        """Returns the name of this particular instance of this class.  Each objectin the dependency graph has a name.  This name will be used by the UIand by MEL."""
    def normalsPerVertex(self) -> int:
        """Specifies how many normals per vertex the HW shader would like Maya to provide.  This can range from 0 to 3.  The first normal is the surface normal.  The second "normal" is the primary tangent (generally the "u" direction).  The third "normal" is the secondary tangent or the binormal (generally the "v" direction). Together, the normal, tangent and binormal form an orthogonal basis frequently named "tangent space basis"."""
    def passThroughToMany(self, plug: Any, plugArray: Any) -> bool:
        """This method is overriden by nodes that want to control the traversal behavior of some Maya search algorithms which traverse the history/future of shape nodes looking for directly related nodes. In particular, the Artisan paint code uses this method when searching for paintable nodes, and the disk cache code uses this method when searching for upstream cacheFile nodes."""
    def passThroughToOne(self, plug: Any) -> Any:
        """This method may be overriden by nodes that have a one-to-one relationship between an input attribute and a corresponding output attribute. This method is used by Maya to perform the following capabilities:"""
    def postConstructor(self) -> MPxHwShaderNode:
        """Internally maya creates two objects when a user defined node is created, the internal MObject and the user derived object."""
    def postEvaluation(self, context: MDGContext, evalNode: MEvaluationNode, evalType: Any) -> None:
        """Clean up node's internal state after threaded evaluation."""
    def preEvaluation(self, context: MDGContext, evalNode: MEvaluationNode) -> None:
        """Prepare a node's internal state for threaded evaluation."""
    def provideVertexIDs(self) -> bool:
        """This method returns a boolean value that indicates whether a map of the vertex IDs will be provided to the geometry method."""
    def renderImage(self, imageName: Any, region: Any, parameters: int) -> Any:
        """renderImage(uiDrawManager, imageName, region, parameters) -> [int, int]/None"""
    def renderSwatchImage(self, image: Any) -> Any:
        """If the shader specifies to override swatch rendering, then this method must be overridden in order to draw anything into a swatch."""
    def setDependentsDirty(self, plug: MPlug, plugArray: Any) -> MPxHwShaderNode:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug which Maya is marking dirty. The list of plugs for Maya to mark dirty is returned by the plug array. This method handles both dynamic as well as non-dynamic plugs and is useful in the following ways:"""
    def setDoNotWrite(self, bool: bool) -> MPxHwShaderNode:
        """Use this method to mark the "do not write" state of this proxy node.  If set, this node will not be saved when the Maya model is written out. """
    def setExistWithoutInConnections(self, bool: bool) -> bool:
        """This method specifies whether or not the node can exist without input"""
    def setExistWithoutOutConnections(self, bool: bool) -> bool:
        """This method specifies whether or not the node can exist without"""
    def setExternalContent(self, table: Any) -> MPxHwShaderNode:
        """This is useful in the context of content relocation.  This will be called while the scene is being loaded to apply path changes performed externally. Consequently, interaction with the rest of the scene must be kept to a minimum.  It is however valid to call this method outside of scene loading contexts."""
    def setExternalContentForFileAttr(self, attr: MObject, table: Any) -> bool:
        """This method is a helper for derived clases implementing setExternalContent().  It assigns a value to a plug with the one from the table whose key is the same as the passed in attribute name."""
    def setInternalValue(self, plug: Any, dataHandle: Any) -> bool:
        """This method is overriden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self, plug: Any, dataHandle: Any, ctx: Any) -> Any:
        """This method is obsolete. Override MPxNode.setInternalValue instead."""
    def setMPSafe(self, bool: bool) -> MPxHwShaderNode:
        """This method is obsolete. Override MPxNode.setSchedulingType instead."""
    def shouldSave(self, plug: Any) -> Any:
        """This method may be overridden by the user defined node.  It should only be required to override this on rare occasions."""
    def supportsBatching(self) -> bool:
        """Specifies whether or not this shader supports batched rendering of shapes."""
    def texCoordsPerVertex(self) -> int:
        """This method returns the number of texture coordinate values per vertex that the hw shader node would like to receive from Maya. Maya will attempt to provide all the texture coordinate data that the shader would like but it will never provide more data than is actually available in the shape.  The uv sets returned by getTexCoordSetNames() will override the number of uv sets specified by texCoordsPerVertex(). If you do not override this method or getTexCoordSetNames(), Maya will provide no texture coordinates per vertex."""
    def thisMObject(self) -> MObject:
        """Returns the MObject associated with this user defined node.  This makes it possible to use MFnDependencyNode or to construct plugs to this node's attributes."""
    def transformInvalidationRange(self, plug: MPlug, timeRange: MTimeRange) -> float:
        """Override this method to register this node as an Invalidation-Range-Transformation kernel (IRT kernel) An IRT kernel node will change the invalidation time range for its downstream nodes For example, Dynamics-solver will transform invalidation time range [a,b] to [a,+inf) And Clip-Time-Editor will send out the invalidation range for each of the clip [a,b] to ( [t0+a,t0+b] U [t1+a,t1+b] U [t2+a,t2+b] U ... ) """
    def transparencyOptions(self) -> int:
        """This method returns transparency options for usage as hints for Maya's internal draw during a given rendering pass. Parameters are returned via an integer containing masked out bits. By default the mask is set to 0, meaning that the drawing should be treated as regular opaque object drawing. This will generally mean one call per draw pass."""
    def type(self) -> int:
        """Returns the type of node that this is.  This is used to differentiate user defined nodes that are derived off different MPx base classes."""
    def typeId(self) -> MTypeId:
        """Returns the TYPEID of this node."""
    def typeName(self) -> Any:
        """Returns the type name of this node.  The type name identifies the node type to the ASCII file format"""
    def unbind(self, request: MDrawRequest, view: Any) -> MPxHwShaderNode:
        """This method is invoked for hardware rendering to Maya's 3D view."""

class MPxLocatorNode:
    boundingBoxCenterX: Any
    boundingBoxCenterY: Any
    boundingBoxCenterZ: Any
    center: Any
    instObjGroups: Any
    intermediateObject: Any
    inverseMatrix: Any
    isTemplated: Any
    kAssembly: Any
    kBlendShape: Any
    kCameraSetNode: Any
    kClientDeviceNode: Any
    kConstraintNode: Any
    kDeformerNode: Any
    kDependNode: Any
    kEmitterNode: Any
    kEvaluatedDirectly: Any
    kEvaluatedIndirectly: Any
    kFieldNode: Any
    kFluidEmitterNode: Any
    kGeometryFilter: Any
    kHardwareShader: Any
    kHwShaderNode: Any
    kIkSolverNode: Any
    kImagePlaneNode: Any
    kLast: Any
    kLeaveDirty: Any
    kLocatorNode: Any
    kManipContainer: Any
    kManipulatorNode: Any
    kMotionPathNode: Any
    kObjectSet: Any
    kParticleAttributeMapperNode: Any
    kPostEvaluationTypeLast: Any
    kSkinCluster: Any
    kSpringNode: Any
    kSurfaceShape: Any
    kThreadedDeviceNode: Any
    kTransformNode: Any
    localPosition: Any
    localPositionX: Any
    localPositionY: Any
    localPositionZ: Any
    localScale: Any
    localScaleX: Any
    localScaleY: Any
    localScaleZ: Any
    matrix: Any
    nodeBoundingBox: Any
    nodeBoundingBoxMax: Any
    nodeBoundingBoxMaxX: Any
    nodeBoundingBoxMaxY: Any
    nodeBoundingBoxMaxZ: Any
    nodeBoundingBoxMin: Any
    nodeBoundingBoxMinX: Any
    nodeBoundingBoxMinY: Any
    nodeBoundingBoxMinZ: Any
    nodeBoundingBoxSize: Any
    nodeBoundingBoxSizeX: Any
    nodeBoundingBoxSizeY: Any
    nodeBoundingBoxSizeZ: Any
    objectColor: Any
    objectGroupColor: Any
    objectGroupId: Any
    objectGroups: Any
    objectGrpCompList: Any
    parentInverseMatrix: Any
    parentMatrix: Any
    underWorldObject: Any
    useObjectColor: Any
    visibility: Any
    worldInverseMatrix: Any
    worldMatrix: Any
    worldPosition: Any
    worldPositionX: Any
    worldPositionY: Any
    worldPositionZ: Any
    def __init__(self) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def addAttribute(attr: MObject) -> None:
        """This method adds a new attribute to a user defined node type during the type's initialization."""
    def addExternalContentForFileAttr(self, table: MObject, attr: Any) -> bool:
        """This method is a helper for derived clases implementing getExternalContent().  It augments the external content info table passed in with an entry describing external content whose location is described by the specified attribute."""
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> None:
        """This method specifies that a particular input attribute affects a specific output attribute.  This is required to make evaluation efficient.  When an input changes, only the affected outputs will be computed. Output attributes cannot be keyable - if they are keyable, this method will fail."""
    def boundingBox(self) -> MBoundingBox:
        """This method should be overridden to return a bounding box for the locator."""
    def closestPoint(self, rayPoint: MPoint, rayDir: MVector) -> MPoint:
        """Returns the point on the locator, in the locator's local space, which is closest along the specified ray."""
    def color(self, status: int) -> int:
        """This method returns the index of the color that is the default draw color for the given display status.  The index should be used with the methods of M3dView.  The value is not an index into the OpenGL color table. """
    def colorRGB(self, status: int) -> MColor:
        """This method returns the RGB values of the default draw color for the given display status."""
    def compute(self, plug: Any, dataBlock: Any) -> MPxLocatorNode:
        """This method should be overridden in user defined nodes."""
    def configCache(self, evalNode: Any, schema: Any) -> None:
        """Defines the node's behavior when participating in Cached Playback."""
    def connectionBroken(self, plug: bool, otherPlug: Any, asSrc: Any) -> MPxLocatorNode:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, plug: bool, otherPlug: Any, asSrc: Any) -> MPxLocatorNode:
        """This method gets called when connections are made to attributes of this node."""
    def copyInternalData(self, node: Any) -> MPxLocatorNode:
        """This method is overriden by nodes that store attribute data in some internal format."""
    def dependsOn(self, plug: Any, otherPlug: Any) -> Any:
        """This method may be overridden by the user defined node. It should only be required to override this on rare occasions."""
    def doNotWrite(self) -> bool:
        """use this method to query the "do not write" state of this proxy node. True is returned if this node will not be saved when the maya model is written out."""
    def draw(self, view: MDagPath, path: int, style: int, status: Any) -> MPxLocatorNode:
        """Overriding this method allows the drawing of custom geometry using standard OpenGL calls.  The OpenGL state should be left in the same state that it was in previously.  The OpenGL routine glPushAttrib may be used to make this easier."""
    def drawLast(self) -> bool:
        """Indicates that this locator should be the last item draw in a given refresh cycle.  Objects drawn out-of-order will not preserve the proper transparency sorting.  Conflicts among multiple objects with the drawLast indicator set to TRUE will be resolved by their order in the Outliner, where they will be drawn top-to-bottom."""
    def excludeAsLocator(self) -> bool:
        """When the modelPanel is set to not draw locators, returing True will also not draw the custom locator. If False is returned, the custom locator will also be drawn."""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    def forceCache(self, ctx: Any) -> MDataBlock:
        """Get the datablock for this node. If there is no datablock then one will be created."""
    def getCacheSetup(self, evalNode: MEvaluationNode, disablingInfo: Any, setupInfo: Any, objectArray: Any) -> None:
        """Provide node-specific setup info for the Cached Playback system."""
    def getExternalContent(self, table: Any) -> MPxLocatorNode:
        """The table populated by this method must include the location of all the content (files) used by this node, including those that do not exist.  See MExternalContentInfoTable for details."""
    def getFilesToArchive(self, shortName: bool = False, unresolvedName: bool = False, markCouldBeImageSequence: bool = False) -> list[str]:
        """Use this method to return all external files used by this node. This file list will be used by the File > Archive zip feature, maya.exe -archive and the `file -q -list` mel command."""
    def getInternalValue(self, plug: Any, dataHandle: Any) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def getInternalValueInContext(self, plug: Any, dataHandle: Any, ctx: Any) -> Any:
        """This method is obsolete. Override MPxNode.getInternalValue instead."""
    def getShapeSelectionMask(self) -> MSelectionMask:
        """This routine can be overridden to provide information aboutthe selection mask of the locator. By default the selection maskfor locators is returned."""
    def hasInvalidationRangeTransformation(self) -> bool:
        """Checks if this MPxNode derived node overrides the MPxNode::transformInvalidationRange method"""
    @staticmethod
    def inheritAttributesFrom(parentClassName: Any) -> None:
        """This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node."""
    def internalArrayCount(self, plug: Any) -> int:
        """internalArrayCount(plug, ctx) -> int  [OBSOLETE]"""
    def isAbstractClass(self) -> bool:
        """Override this class to return True if this node is an abstract node. An abstract node can only be used as a base class.  It cannot be created using the 'createNode' command."""
    def isBounded(self) -> bool:
        """This method should be overridden to return True if the user supplies a bounding box routine.  Supplying a bounding box routine makes refresh and selection more efficient."""
    def isPassiveOutput(self, plug: Any) -> bool:
        """This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent value modifications to the destination attribute. For example, output plugs on animation curve nodes are passive. This allows the attributes driven by the animation curves to be set to new values by the user."""
    def isTransparent(self) -> bool:
        """Indicates that this locator uses transparency during ::draw method calls. Objects with transparency must be drawn in a special queue, i.e. after all opaque objects are drawn."""
    def legalConnection(self, plug: bool, otherPlug: Any, asSrc: Any) -> Any:
        """This method allows you to check for legal connections being made to attributes of this node."""
    def legalDisconnection(self, plug: bool, otherPlug: Any, arsSrc: Any) -> Any:
        """This method allows you to check for legal disconnections being made to attributes of this node."""
    def name(self) -> Any:
        """Returns the name of this particular instance of this class.  Each objectin the dependency graph has a name.  This name will be used by the UIand by MEL."""
    def passThroughToMany(self, plug: Any, plugArray: Any) -> bool:
        """This method is overriden by nodes that want to control the traversal behavior of some Maya search algorithms which traverse the history/future of shape nodes looking for directly related nodes. In particular, the Artisan paint code uses this method when searching for paintable nodes, and the disk cache code uses this method when searching for upstream cacheFile nodes."""
    def passThroughToOne(self, plug: Any) -> Any:
        """This method may be overriden by nodes that have a one-to-one relationship between an input attribute and a corresponding output attribute. This method is used by Maya to perform the following capabilities:"""
    def postConstructor(self) -> MPxLocatorNode:
        """Internally maya creates two objects when a user defined node is created, the internal MObject and the user derived object."""
    def postEvaluation(self, context: MDGContext, evalNode: MEvaluationNode, evalType: Any) -> None:
        """Clean up node's internal state after threaded evaluation."""
    def preEvaluation(self, context: MDGContext, evalNode: MEvaluationNode) -> None:
        """Prepare a node's internal state for threaded evaluation."""
    def setDependentsDirty(self, plug: MPlug, plugArray: Any) -> MPxLocatorNode:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug which Maya is marking dirty. The list of plugs for Maya to mark dirty is returned by the plug array. This method handles both dynamic as well as non-dynamic plugs and is useful in the following ways:"""
    def setDoNotWrite(self, bool: bool) -> MPxLocatorNode:
        """Use this method to mark the "do not write" state of this proxy node.  If set, this node will not be saved when the Maya model is written out. """
    def setExistWithoutInConnections(self, bool: bool) -> bool:
        """This method specifies whether or not the node can exist without input"""
    def setExistWithoutOutConnections(self, bool: bool) -> bool:
        """This method specifies whether or not the node can exist without"""
    def setExternalContent(self, table: Any) -> MPxLocatorNode:
        """This is useful in the context of content relocation.  This will be called while the scene is being loaded to apply path changes performed externally. Consequently, interaction with the rest of the scene must be kept to a minimum.  It is however valid to call this method outside of scene loading contexts."""
    def setExternalContentForFileAttr(self, attr: MObject, table: Any) -> bool:
        """This method is a helper for derived clases implementing setExternalContent().  It assigns a value to a plug with the one from the table whose key is the same as the passed in attribute name."""
    def setInternalValue(self, plug: Any, dataHandle: Any) -> bool:
        """This method is overriden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self, plug: Any, dataHandle: Any, ctx: Any) -> Any:
        """This method is obsolete. Override MPxNode.setInternalValue instead."""
    def setMPSafe(self, bool: bool) -> MPxLocatorNode:
        """This method is obsolete. Override MPxNode.setSchedulingType instead."""
    def shouldSave(self, plug: Any) -> Any:
        """This method may be overridden by the user defined node.  It should only be required to override this on rare occasions."""
    def thisMObject(self) -> MObject:
        """Returns the MObject associated with this user defined node.  This makes it possible to use MFnDependencyNode or to construct plugs to this node's attributes."""
    def transformInvalidationRange(self, plug: MPlug, timeRange: MTimeRange) -> float:
        """Override this method to register this node as an Invalidation-Range-Transformation kernel (IRT kernel) An IRT kernel node will change the invalidation time range for its downstream nodes For example, Dynamics-solver will transform invalidation time range [a,b] to [a,+inf) And Clip-Time-Editor will send out the invalidation range for each of the clip [a,b] to ( [t0+a,t0+b] U [t1+a,t1+b] U [t2+a,t2+b] U ... ) """
    def type(self) -> int:
        """Returns the type of node that this is.  This is used to differentiate user defined nodes that are derived off different MPx base classes."""
    def typeId(self) -> MTypeId:
        """Returns the TYPEID of this node."""
    def typeName(self) -> Any:
        """Returns the type name of this node.  The type name identifies the node type to the ASCII file format"""
    def useClosestPointForSelection(self) -> bool:
        """Determines whether Maya should call closestPoint() when doing single selection."""

class MPxManipContainer:
    kAssembly: Any
    kBlendShape: Any
    kCameraSetNode: Any
    kClientDeviceNode: Any
    kConstraintNode: Any
    kDeformerNode: Any
    kDependNode: Any
    kEmitterNode: Any
    kEvaluatedDirectly: Any
    kEvaluatedIndirectly: Any
    kFieldNode: Any
    kFluidEmitterNode: Any
    kGeometryFilter: Any
    kHardwareShader: Any
    kHwShaderNode: Any
    kIkSolverNode: Any
    kImagePlaneNode: Any
    kLast: Any
    kLeaveDirty: Any
    kLocatorNode: Any
    kManipContainer: Any
    kManipulatorNode: Any
    kMotionPathNode: Any
    kObjectSet: Any
    kParticleAttributeMapperNode: Any
    kPostEvaluationTypeLast: Any
    kSkinCluster: Any
    kSpringNode: Any
    kSurfaceShape: Any
    kThreadedDeviceNode: Any
    kTransformNode: Any
    def __init__(self) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def addAttribute(attr: MObject) -> None:
        """This method adds a new attribute to a user defined node type during the type's initialization."""
    def addCircleSweepManip(self, manipName: Any, angleName: Any) -> MDagPath:
        """This method creates a CircleSweepManip and adds it to"""
    def addCurveSegmentManip(self, manipName: Any, startParamName: Any, endParamName: Any) -> MDagPath:
        """This method creates a CurveSegmentManip and adds it to"""
    def addDirectionManip(self, manipName: Any, directionName: Any) -> MDagPath:
        """This method creates a DirectionManip and adds it to"""
    def addDiscManip(self, manipName: Any, angleName: Any) -> MDagPath:
        """This method creates a DiscManip and adds it to"""
    def addDistanceManip(self, manipName: Any, distanceName: Any) -> MDagPath:
        """This method creates a DistanceManip and adds it to"""
    def addExternalContentForFileAttr(self, table: MObject, attr: Any) -> bool:
        """This method is a helper for derived clases implementing getExternalContent().  It augments the external content info table passed in with an entry describing external content whose location is described by the specified attribute."""
    def addFreePointTriadManip(self, manipName: Any, pointName: Any) -> MDagPath:
        """This method creates a FreePointTriadManip and adds it to"""
    def addMPxManipulatorNode(self, manipTypeName: Any, manipName: Any, proxyManip: Any) -> None:
        """This method creates a custom MPxManipulatorNode and adds it to the"""
    def addManipToPlugConversion(self, plug: MPlug) -> int:
        """This method adds a manipulator to plug converter for the specified"""
    def addPlugToInViewEditor(self, plug: MPlug) -> Any:
        """Adds a plug to the In-View Editor."""
    def addPlugToManipConversion(self, manipIndex: int) -> Any:
        """This method adds a plug to manipulator converter for the specified"""
    def addPointOnCurveManip(self, manipName: Any, paramName: Any) -> MDagPath:
        """This method creates a PointOnCurveManip and adds it to"""
    def addPointOnSurfaceManip(self, manipName: Any, paramName: Any) -> MDagPath:
        """This method creates a PointOnSurfaceManip and adds it to"""
    def addRotateManip(self, manipName: Any, rotationName: Any) -> MDagPath:
        """This method creates a RotateManip and adds it to"""
    def addScaleManip(self, manipName: Any, scaleName: Any) -> MDagPath:
        """This method creates a ScaleManip and adds it to"""
    def addStateManip(self, manipName: Any, stateName: Any) -> MDagPath:
        """This method creates a StateManip and adds it to"""
    @staticmethod
    def addToManipConnectTable(typeId: Any) -> Any:
        """This method adds the user defined node as an entry in the"""
    def addToggleManip(self, manipName: Any, toggleName: Any) -> MDagPath:
        """This method creates a ToggleManip and adds it to"""
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> None:
        """This method specifies that a particular input attribute affects a specific output attribute.  This is required to make evaluation efficient.  When an input changes, only the affected outputs will be computed. Output attributes cannot be keyable - if they are keyable, this method will fail."""
    def compute(self, plug: Any, dataBlock: Any) -> MPxManipContainer:
        """This method should be overridden in user defined nodes."""
    def configCache(self, evalNode: Any, schema: Any) -> None:
        """Defines the node's behavior when participating in Cached Playback."""
    def connectToDependNode(self, node: MObject) -> None:
        """This method connects the manipulator to the dependency node. This"""
    def connectionBroken(self, plug: bool, otherPlug: Any, asSrc: Any) -> MPxManipContainer:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, plug: bool, otherPlug: Any, asSrc: Any) -> MPxManipContainer:
        """This method gets called when connections are made to attributes of this node."""
    def copyInternalData(self, node: Any) -> MPxManipContainer:
        """This method is overriden by nodes that store attribute data in some internal format."""
    def createChildren(self) -> None:
        """This method should be overridden in user defined manipulators."""
    def dependsOn(self, plug: Any, otherPlug: Any) -> Any:
        """This method may be overridden by the user defined node. It should only be required to override this on rare occasions."""
    def doDrag(self) -> None:
        """This method gets called when the manipulator receives a mouse drag event."""
    def doNotWrite(self) -> bool:
        """use this method to query the "do not write" state of this proxy node. True is returned if this node will not be saved when the maya model is written out."""
    def doPress(self) -> None:
        """This method gets called when the manipulator receives a mouse down event."""
    def doRelease(self) -> None:
        """This method gets called when the manipulator receives a mouse release"""
    def draw(self, view: MDagPath, path: int, style: int, status: Any) -> None:
        """This method can be overloaded to customize the drawing of the"""
    def drawUI(self, drawManager: int, frameContext: Any) -> None:
        """This is the primary method for doing custom drawing for the"""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    def finishAddingManips(self) -> Any:
        """This method should be called from the user-defined manipulator"""
    def forceCache(self, ctx: Any) -> MDataBlock:
        """Get the datablock for this node. If there is no datablock then one will be created."""
    def getCacheSetup(self, evalNode: Any, disablingInfo: Any, setupInfo: Any, objectArray: Any) -> None:
        """Provide node-specific setup info for the Cached Playback system."""
    def getConverterManipDoubleValue(self) -> float:
        """This method retrieves the value of a converterManipValue of type"""
    def getConverterManipMEulerRotationValue(self) -> Any:
        """This method retrieves the value of a converterManipValue of type"""
    def getConverterManipMMatrixValue(self) -> MMatrix:
        """This method retrieves the value of a converterManipValue of type"""
    def getConverterManipMPointValue(self) -> MPoint:
        """This method retrieves the value of a converterManipValue of type"""
    def getConverterManipMTransformationMatrixValue(self) -> MTransformationMatrix:
        """This method retrieves the value of a converterManipValue of type"""
    def getConverterManipMVectorValue(self) -> MVector:
        """This method retrieves the value of a converterManipValue of type"""
    def getConverterManipUIntValue(self) -> int:
        """This method retrieves the value of a converterManipValue of type"""
    def getConverterManipValues(self) -> Any:
        """This method retrieves the value of a converterManipValue of type"""
    def getConverterPlugDoubleValue(self) -> float:
        """This method retrieves the value of a converterPlugValue of type"""
    def getConverterPlugMEulerRotationValue(self) -> MEulerRotation:
        """This method retrieves the value of a converterPlugValue of type"""
    def getConverterPlugMMatrixValue(self) -> MMatrix:
        """This method retrieves the value of a converterPlugValue of type"""
    def getConverterPlugMPointValue(self) -> MPoint:
        """This method retrieves the value of a converterPlugValue of type"""
    def getConverterPlugMVectorValue(self) -> MVector:
        """This method retrieves the value of a converterPlugValue of type"""
    def getConverterPlugValues(self) -> Any:
        """This method retrieves the value of a converterPlugValue of type"""
    def getExternalContent(self, table: Any) -> MPxManipContainer:
        """The table populated by this method must include the location of all the content (files) used by this node, including those that do not exist.  See MExternalContentInfoTable for details."""
    def getFilesToArchive(self, shortName: bool = False, unresolvedName: bool = False, markCouldBeImageSequence: bool = False) -> list[str]:
        """Use this method to return all external files used by this node. This file list will be used by the File > Archive zip feature, maya.exe -archive and the `file -q -list` mel command."""
    def getInternalValue(self, plug: Any, dataHandle: Any) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def getInternalValueInContext(self, plug: Any, dataHandle: Any, ctx: Any) -> Any:
        """This method is obsolete. Override MPxNode.getInternalValue instead."""
    def hasInvalidationRangeTransformation(self) -> bool:
        """Checks if this MPxNode derived node overrides the MPxNode::transformInvalidationRange method"""
    @staticmethod
    def inheritAttributesFrom(parentClassName: Any) -> None:
        """This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node."""
    @staticmethod
    def initialize() -> None:
        """This method initializes the manipulator,"""
    def internalArrayCount(self, plug: Any) -> int:
        """internalArrayCount(plug, ctx) -> int  [OBSOLETE]"""
    def isAbstractClass(self) -> bool:
        """Override this class to return True if this node is an abstract node. An abstract node can only be used as a base class.  It cannot be created using the 'createNode' command."""
    def isManipActive(self, manipName: int, stateName: MObject) -> MDagPath:
        """This method returns if custom manip is active & gets the"""
    def isPassiveOutput(self, plug: Any) -> bool:
        """This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent value modifications to the destination attribute. For example, output plugs on animation curve nodes are passive. This allows the attributes driven by the animation curves to be set to new values by the user."""
    def legalConnection(self, plug: bool, otherPlug: Any, asSrc: Any) -> Any:
        """This method allows you to check for legal connections being made to attributes of this node."""
    def legalDisconnection(self, plug: bool, otherPlug: Any, arsSrc: Any) -> Any:
        """This method allows you to check for legal disconnections being made to attributes of this node."""
    def manipToPlugConversion(self, manipIndex: int) -> MManipData:
        """This virtual method calculates and returns the requested manipulator"""
    def name(self) -> Any:
        """Returns the name of this particular instance of this class.  Each objectin the dependency graph has a name.  This name will be used by the UIand by MEL."""
    @staticmethod
    def newManipulator(arg: Any, MObject: MObject) -> Any:
        """This static function is used to create a user-defined manipulator."""
    def passThroughToMany(self, plug: Any, plugArray: Any) -> bool:
        """This method is overriden by nodes that want to control the traversal behavior of some Maya search algorithms which traverse the history/future of shape nodes looking for directly related nodes. In particular, the Artisan paint code uses this method when searching for paintable nodes, and the disk cache code uses this method when searching for upstream cacheFile nodes."""
    def passThroughToOne(self, plug: Any) -> Any:
        """This method may be overriden by nodes that have a one-to-one relationship between an input attribute and a corresponding output attribute. This method is used by Maya to perform the following capabilities:"""
    def plugToManipConversion(self, manipIndex: int) -> MManipData:
        """This virtual method calculates and returns the requested"""
    def postConstructor(self) -> MPxManipContainer:
        """Internally maya creates two objects when a user defined node is created, the internal MObject and the user derived object."""
    def postEvaluation(self, context: MDGContext, evalNode: MEvaluationNode, evalType: Any) -> None:
        """Clean up node's internal state after threaded evaluation."""
    def preDrawUI(self, view: M3dView) -> None:
        """This function is used to setup some drawing data for drawing the"""
    def preEvaluation(self, context: MDGContext, evalNode: MEvaluationNode) -> None:
        """Prepare a node's internal state for threaded evaluation."""
    @staticmethod
    def removeFromManipConnectTable(typeId: Any) -> Any:
        """This method adds the user defined node as an entry in the"""
    def setDependentsDirty(self, plug: MPlug, plugArray: Any) -> MPxManipContainer:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug which Maya is marking dirty. The list of plugs for Maya to mark dirty is returned by the plug array. This method handles both dynamic as well as non-dynamic plugs and is useful in the following ways:"""
    def setDoNotWrite(self, bool: bool) -> MPxManipContainer:
        """Use this method to mark the "do not write" state of this proxy node.  If set, this node will not be saved when the Maya model is written out. """
    def setExistWithoutInConnections(self, bool: bool) -> bool:
        """This method specifies whether or not the node can exist without input"""
    def setExistWithoutOutConnections(self, bool: bool) -> bool:
        """This method specifies whether or not the node can exist without"""
    def setExternalContent(self, table: Any) -> MPxManipContainer:
        """This is useful in the context of content relocation.  This will be called while the scene is being loaded to apply path changes performed externally. Consequently, interaction with the rest of the scene must be kept to a minimum.  It is however valid to call this method outside of scene loading contexts."""
    def setExternalContentForFileAttr(self, attr: MObject, table: Any) -> bool:
        """This method is a helper for derived clases implementing setExternalContent().  It assigns a value to a plug with the one from the table whose key is the same as the passed in attribute name."""
    def setInternalValue(self, plug: Any, dataHandle: Any) -> bool:
        """This method is overriden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self, plug: Any, dataHandle: Any, ctx: Any) -> Any:
        """This method is obsolete. Override MPxNode.setInternalValue instead."""
    def setMPSafe(self, bool: bool) -> MPxManipContainer:
        """This method is obsolete. Override MPxNode.setSchedulingType instead."""
    def shouldSave(self, plug: Any) -> Any:
        """This method may be overridden by the user defined node.  It should only be required to override this on rare occasions."""
    def thisMObject(self) -> MObject:
        """Returns the MObject associated with this user defined node.  This makes it possible to use MFnDependencyNode or to construct plugs to this node's attributes."""
    def transformInvalidationRange(self, plug: MPlug, timeRange: MTimeRange) -> float:
        """Override this method to register this node as an Invalidation-Range-Transformation kernel (IRT kernel) An IRT kernel node will change the invalidation time range for its downstream nodes For example, Dynamics-solver will transform invalidation time range [a,b] to [a,+inf) And Clip-Time-Editor will send out the invalidation range for each of the clip [a,b] to ( [t0+a,t0+b] U [t1+a,t1+b] U [t2+a,t2+b] U ... ) """
    def type(self) -> int:
        """Returns the type of node that this is.  This is used to differentiate user defined nodes that are derived off different MPx base classes."""
    def typeId(self) -> MTypeId:
        """Returns the TYPEID of this node."""
    def typeName(self) -> Any:
        """Returns the type name of this node.  The type name identifies the node type to the ASCII file format"""

class MPxManipulatorNode:
    kAssembly: Any
    kBlendShape: Any
    kCameraSetNode: Any
    kClientDeviceNode: Any
    kConstraintNode: Any
    kDeformerNode: Any
    kDependNode: Any
    kEmitterNode: Any
    kEvaluatedDirectly: Any
    kEvaluatedIndirectly: Any
    kFieldNode: Any
    kFluidEmitterNode: Any
    kGeometryFilter: Any
    kHardwareShader: Any
    kHwShaderNode: Any
    kIkSolverNode: Any
    kImagePlaneNode: Any
    kLast: Any
    kLeaveDirty: Any
    kLocatorNode: Any
    kManipContainer: Any
    kManipulatorNode: Any
    kMotionPathNode: Any
    kObjectSet: Any
    kParticleAttributeMapperNode: Any
    kPostEvaluationTypeLast: Any
    kSkinCluster: Any
    kSpringNode: Any
    kSurfaceShape: Any
    kThreadedDeviceNode: Any
    kTransformNode: Any
    def __init__(self) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def addAttribute(attr: MObject) -> None:
        """This method adds a new attribute to a user defined node type during the type's initialization."""
    def addDependentPlug(self, plug: MPlug) -> None:
        """This method adds the plug to the list of those to be keyframed."""
    def addDoubleValue(self, valueName: Any, defaultValue: float) -> int:
        """Manipulators which call connectPlugToValue() must first create"""
    def addExternalContentForFileAttr(self, table: MObject, attr: Any) -> bool:
        """This method is a helper for derived clases implementing getExternalContent().  It augments the external content info table passed in with an entry describing external content whose location is described by the specified attribute."""
    def addPointValue(self, valueName: Any, defaultValue: MPoint) -> int:
        """Manipulators which call connectPlugToValue() must first create"""
    def addVectorValue(self, valueName: Any, defaultValue: MVector) -> int:
        """Manipulators which call connectPlugToValue() must first create"""
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> None:
        """This method specifies that a particular input attribute affects a specific output attribute.  This is required to make evaluation efficient.  When an input changes, only the affected outputs will be computed. Output attributes cannot be keyable - if they are keyable, this method will fail."""
    def colorAndName(self, view: int, glName: bool, glNameIsPickable: Any, colorIndex: Any) -> None:
        """This method is used to set the color of the GL component that is"""
    def compute(self, plug: Any, dataBlock: Any) -> MPxManipulatorNode:
        """This method should be overridden in user defined nodes."""
    def configCache(self, evalNode: Any, schema: Any) -> None:
        """Defines the node's behavior when participating in Cached Playback."""
    def connectPlugToValue(self, plug: MPlug, valueIndex: int) -> int:
        """This method is called in the connectToDependNode() virtual if"""
    def connectToDependNode(self, node: MObject) -> None:
        """This method connects the manipulator to the dependency node. This"""
    def connectionBroken(self, plug: bool, otherPlug: Any, asSrc: Any) -> MPxManipulatorNode:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, plug: bool, otherPlug: Any, asSrc: Any) -> MPxManipulatorNode:
        """This method gets called when connections are made to attributes of this node."""
    def copyInternalData(self, node: Any) -> MPxManipulatorNode:
        """This method is overriden by nodes that store attribute data in some internal format."""
    def dependentPlugsReset(self) -> None:
        """This method resets the list of dependent plugs for this manipulator."""
    def dependsOn(self, plug: Any, otherPlug: Any) -> Any:
        """This method may be overridden by the user defined node. It should only be required to override this on rare occasions."""
    def deregisterForMouseMove(self) -> None:
        """This method deregisters this manipulator from receiving"""
    def dimmedColor(self) -> float:
        """This method returns the color index for a dimmed or unselectable component."""
    def doDrag(self, view: Any) -> None:
        """This method gets called when the manipulator receives a mouse drag event."""
    def doMove(self, view: Any, refresh: Any) -> None:
        """This method gets called when the manipulator receives a mouse move event,"""
    def doNotWrite(self) -> bool:
        """use this method to query the "do not write" state of this proxy node. True is returned if this node will not be saved when the maya model is written out."""
    def doPress(self, view: Any) -> None:
        """This method gets called when the manipulator receives a mouse down event."""
    def doRelease(self, view: Any) -> None:
        """This method gets called when the manipulator receives a mouse release event."""
    def draw(self, view: MDagPath, path: int, style: int, status: Any) -> None:
        """This method is overloaded to draw the manipulators. Selection"""
    def drawUI(self, drawManager: int, frameContext: Any) -> None:
        """This is the primary method for drawing the manipulator in Viewport 2.0."""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    def finishAddingManips(self) -> None:
        """This method should be called from the user-defined manipulator"""
    def forceCache(self, ctx: Any) -> MDataBlock:
        """Get the datablock for this node. If there is no datablock then one will be created."""
    def getCacheSetup(self, evalNode: Any, disablingInfo: Any, setupInfo: Any, objectArray: Any) -> None:
        """Provide node-specific setup info for the Cached Playback system."""
    def getDoubleValue(self, valueIndex: int, previousValue: bool) -> float:
        """This method is used for getting a floating point value associated with the manipulator."""
    def getExternalContent(self, table: Any) -> MPxManipulatorNode:
        """The table populated by this method must include the location of all the content (files) used by this node, including those that do not exist.  See MExternalContentInfoTable for details."""
    def getFilesToArchive(self, shortName: bool = False, unresolvedName: bool = False, markCouldBeImageSequence: bool = False) -> list[str]:
        """Use this method to return all external files used by this node. This file list will be used by the File > Archive zip feature, maya.exe -archive and the `file -q -list` mel command."""
    def getInternalValue(self, plug: Any, dataHandle: Any) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def getInternalValueInContext(self, plug: Any, dataHandle: Any, ctx: Any) -> Any:
        """This method is obsolete. Override MPxNode.getInternalValue instead."""
    def getPointValue(self, valueIndex: int, previousValue: bool) -> MPoint:
        """This method is used for getting an MPoint value associated with the manipulator."""
    def getVectorValue(self, valueIndex: int, previousValue: bool) -> float:
        """This method is used for getting an MVector value associated with the manipulator."""
    def glActiveName(self) -> int:
        """This method returns the unsigned int value which"""
    def glFirstHandle(self) -> int:
        """This method is used to find the unsigned int value that should"""
    def hasInvalidationRangeTransformation(self) -> bool:
        """Checks if this MPxNode derived node overrides the MPxNode::transformInvalidationRange method"""
    @staticmethod
    def inheritAttributesFrom(parentClassName: Any) -> None:
        """This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node."""
    def internalArrayCount(self, plug: Any) -> int:
        """internalArrayCount(plug, ctx) -> int  [OBSOLETE]"""
    def isAbstractClass(self) -> bool:
        """Override this class to return True if this node is an abstract node. An abstract node can only be used as a base class.  It cannot be created using the 'createNode' command."""
    def isPassiveOutput(self, plug: Any) -> bool:
        """This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent value modifications to the destination attribute. For example, output plugs on animation curve nodes are passive. This allows the attributes driven by the animation curves to be set to new values by the user."""
    def labelBackgroundColor(self) -> float:
        """This method returns the color index of a label background."""
    def labelColor(self) -> float:
        """This method returns the color index of a label."""
    def legalConnection(self, plug: bool, otherPlug: Any, asSrc: Any) -> Any:
        """This method allows you to check for legal connections being made to attributes of this node."""
    def legalDisconnection(self, plug: bool, otherPlug: Any, arsSrc: Any) -> Any:
        """This method allows you to check for legal disconnections being made to attributes of this node."""
    def lineColor(self) -> float:
        """This method returns the color index of a line"""
    def mainColor(self) -> float:
        """This method returns the main color index."""
    def mouseDown(self, arg: Any, half: Any) -> Any:
        """This method returns the mouse down position within"""
    def mousePosition(self, arg: Any, half: Any) -> Any:
        """This method returns the current mouse position within"""
    def mouseRay(self, arg: Any, MVector: Any) -> Any:
        """This method returns the location of the mouse within"""
    def mouseRayWorld(self, arg: Any, MVector: Any) -> Any:
        """This method returns the location of the mouse within"""
    def mouseUp(self, arg: Any, half: Any) -> Any:
        """This method returns the mouse up position within"""
    def name(self) -> Any:
        """Returns the name of this particular instance of this class.  Each objectin the dependency graph has a name.  This name will be used by the UIand by MEL."""
    @staticmethod
    def newManipulator(arg: Any, MObject: MObject) -> Any:
        """This static function is used to create a user-defined manipulator node."""
    def passThroughToMany(self, plug: Any, plugArray: Any) -> bool:
        """This method is overriden by nodes that want to control the traversal behavior of some Maya search algorithms which traverse the history/future of shape nodes looking for directly related nodes. In particular, the Artisan paint code uses this method when searching for paintable nodes, and the disk cache code uses this method when searching for upstream cacheFile nodes."""
    def passThroughToOne(self, plug: Any) -> Any:
        """This method may be overriden by nodes that have a one-to-one relationship between an input attribute and a corresponding output attribute. This method is used by Maya to perform the following capabilities:"""
    def postConstructor(self) -> MPxManipulatorNode:
        """Internally maya creates two objects when a user defined node is created, the internal MObject and the user derived object."""
    def postEvaluation(self, context: MDGContext, evalNode: MEvaluationNode, evalType: Any) -> None:
        """Clean up node's internal state after threaded evaluation."""
    def preDrawUI(self, view: M3dView) -> None:
        """This method is used to setup some drawing data for drawing the manipulator"""
    def preEvaluation(self, context: MDGContext, evalNode: MEvaluationNode) -> None:
        """Prepare a node's internal state for threaded evaluation."""
    def prevColor(self) -> float:
        """This method returns the previously color used by the colorAndName() method."""
    def registerForMouseMove(self) -> None:
        """This method registers this manipulator to receive mouse"""
    def selectedColor(self) -> float:
        """This method returns the color index of a selected component."""
    def setDependentsDirty(self, plug: MPlug, plugArray: Any) -> MPxManipulatorNode:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug which Maya is marking dirty. The list of plugs for Maya to mark dirty is returned by the plug array. This method handles both dynamic as well as non-dynamic plugs and is useful in the following ways:"""
    def setDoNotWrite(self, bool: bool) -> MPxManipulatorNode:
        """Use this method to mark the "do not write" state of this proxy node.  If set, this node will not be saved when the Maya model is written out. """
    def setDoubleValue(self, valueIndex: int, value: float) -> None:
        """This method is used for setting a floating point value associated with the"""
    def setExistWithoutInConnections(self, bool: bool) -> bool:
        """This method specifies whether or not the node can exist without input"""
    def setExistWithoutOutConnections(self, bool: bool) -> bool:
        """This method specifies whether or not the node can exist without"""
    def setExternalContent(self, table: Any) -> MPxManipulatorNode:
        """This is useful in the context of content relocation.  This will be called while the scene is being loaded to apply path changes performed externally. Consequently, interaction with the rest of the scene must be kept to a minimum.  It is however valid to call this method outside of scene loading contexts."""
    def setExternalContentForFileAttr(self, attr: MObject, table: Any) -> bool:
        """This method is a helper for derived clases implementing setExternalContent().  It assigns a value to a plug with the one from the table whose key is the same as the passed in attribute name."""
    def setHandleColor(self, drawManager: int, handleName: Any, colorIndex: Any) -> None:
        """This method is used to set the color of component that is being drawn next."""
    def setInternalValue(self, plug: Any, dataHandle: Any) -> bool:
        """This method is overriden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self, plug: Any, dataHandle: Any, ctx: Any) -> Any:
        """This method is obsolete. Override MPxNode.setInternalValue instead."""
    def setMPSafe(self, bool: bool) -> MPxManipulatorNode:
        """This method is obsolete. Override MPxNode.setSchedulingType instead."""
    def setPointValue(self, valueIndex: int, value: MPoint) -> None:
        """This method is used for setting an MPoint value associated with the"""
    def setVectorValue(self, valueIndex: int, value: MVector) -> None:
        """This method is used for setting an MVector value associated with the"""
    def shouldDrawHandleAsSelected(self, name: int) -> bool:
        """This function is obsolete, please use 'setHandleColor' instead"""
    def shouldSave(self, plug: Any) -> Any:
        """This method may be overridden by the user defined node.  It should only be required to override this on rare occasions."""
    def thisMObject(self) -> MObject:
        """Returns the MObject associated with this user defined node.  This makes it possible to use MFnDependencyNode or to construct plugs to this node's attributes."""
    def transformInvalidationRange(self, plug: MPlug, timeRange: MTimeRange) -> float:
        """Override this method to register this node as an Invalidation-Range-Transformation kernel (IRT kernel) An IRT kernel node will change the invalidation time range for its downstream nodes For example, Dynamics-solver will transform invalidation time range [a,b] to [a,+inf) And Clip-Time-Editor will send out the invalidation range for each of the clip [a,b] to ( [t0+a,t0+b] U [t1+a,t1+b] U [t2+a,t2+b] U ... ) """
    def type(self) -> int:
        """Returns the type of node that this is.  This is used to differentiate user defined nodes that are derived off different MPx base classes."""
    def typeId(self) -> MTypeId:
        """Returns the TYPEID of this node."""
    def typeName(self) -> Any:
        """Returns the type name of this node.  The type name identifies the node type to the ASCII file format"""
    def xColor(self) -> float:
        """This method returns the color index of the x axis."""
    def yColor(self) -> float:
        """This method returns the color index of the y axis."""
    def zColor(self) -> float:
        """This method returns the color index of the z axis."""

class MPxSelectionContext:
    kImage1: Any
    kImage2: Any
    kImage3: Any
    def __init__(self) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def abortAction(self) -> None:
        """This method is called when the abort key is pressed."""
    def addManipulator(self, manipulator: MObject) -> None:
        """This method adds a manipulator to the context."""
    def argTypeNumericalInput(self, index: int) -> Any:
        """This method is used by the feedback line to determine what units to display."""
    def beginMarquee(self, event: Any) -> MPxSelectionContext:
        """Start drawing a dragged out marquee box."""
    def completeAction(self) -> None:
        """This method is called when the complete key is pressed."""
    def deleteAction(self) -> None:
        """This method is called when the delete or backspace key is pressed."""
    def deleteManipulators(self) -> None:
        """This method deletes all the manipulators that belong"""
    def doDrag(self, event: int, drawManager: Any, frameContext: Any) -> None:
        """This method is called when a mouse drag event occurs."""
    def doDragLegacy(self, event: Any) -> None:
        """This method is called when a mouse drag event occurs."""
    def doEnterRegion(self, event: Any) -> None:
        """This method is called when a mouse enters the viewport."""
    def doExitRegion(self, event: Any) -> None:
        """This method is called when a mouse exits the viewport."""
    def doHold(self, event: int, drawManager: Any, frameContext: Any) -> None:
        """This method is called when a mouse button is pressed but"""
    def doHoldLegacy(self, event: Any) -> None:
        """This method is called when a mouse button is pressed but"""
    def doPress(self, event: int, drawManager: Any, frameContext: Any) -> None:
        """This method is called when any mouse button is pressed."""
    def doPressLegacy(self, event: Any) -> None:
        """This method is called when any mouse button is pressed."""
    def doPtrMoved(self, event: int, drawMgr: Any, context: Any) -> None:
        """This method is called when a mouse move event occurs."""
    def doPtrMovedLegacy(self, event: Any) -> None:
        """This method is called when a mouse drag event occurs."""
    def doRelease(self, event: int, drawManager: Any, frameContext: Any) -> None:
        """This method is called when any mouse button is released."""
    def doReleaseLegacy(self, event: Any) -> None:
        """This method is called when any mouse button is released."""
    def dragMarquee(self, event: Any) -> MPxSelectionContext:
        """Draws a rectangle representing the dragged out area initiated with"""
    def drawFeedback(self, event: int, drawMgr: Any, context: Any) -> None:
        """This method is called to draw primitives when your context is activated"""
    def feedbackNumericalInput(self) -> bool:
        """This method is called to update the numerical feedback."""
    def helpStateHasChanged(self, event: Any) -> None:
        """This method is called whenever the help state may need to be"""
    def image(self, index: Any) -> Any:
        """This method is used to retrieve an XPM icon image that has"""
    def inAlternateContext(self) -> bool:
        """This method is called to determine if an alternate context is active."""
    def isSelecting(self) -> bool:
        """Determines whether an object is selected."""
    def lastDragPoint(self) -> MPoint:
        """Returns the position of the last drag point."""
    def newToolCommand(self) -> MPxToolCommand:
        """Create a new instance of the tool command associated with this context."""
    def processNumericalInput(self, values: MDoubleArray, flags: MIntArray, isAbsolute: bool) -> bool:
        """This method processes the input from the numerical input field."""
    def releaseMarquee(self, arg: Any, left: Any, bottom: Any, right: Any) -> Any:
        """End the marquee drawing cycle and return the coordinates corresponding to"""
    def setAllowDoubleClickAction(self) -> None:
        """This method enables the support of double click smart selection for this context."""
    def setAllowPaintSelect(self) -> None:
        """This method enables drag selection mode for this context."""
    def setAllowPreSelectHilight(self) -> None:
        """This method enables the support of pre-selection highlight for this context."""
    def setAllowSoftSelect(self) -> None:
        """This method enables the support of soft selection for this context."""
    def setAllowSymmetry(self) -> None:
        """This method enables the support of symmetrical selection for this context."""
    def setCursor(self, newCursor: MCursor) -> MPxSelectionContext:
        """Set the cursor used by the context to the MCursor that is passed in."""
    def setHelpString(self, str: Any) -> MPxSelectionContext:
        """Set the help string to the given MString."""
    def setImage(self, image: Any, index: Any) -> MPxSelectionContext:
        """This method is used to set an XPM icon image that is to be"""
    def setTitleString(self, str: Any) -> MPxSelectionContext:
        """Set the title of the context to the MString that is passed in."""
    def startPoint(self) -> MPoint:
        """Returns the position of the button press."""
    def stringClassName(self) -> Any:
        """This method is called to determine the name that uniquely identifies"""
    def toolOffCleanup(self) -> None:
        """This method is called when the context is deactivated, i.e when"""
    def toolOnSetup(self, event: Any) -> None:
        """This method is called when the context is activated, i.e when"""

class MPxSurfaceShapeUI:
    kSelectMeshEdges: Any
    kSelectMeshFaces: Any
    kSelectMeshUVs: Any
    kSelectMeshVerts: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def canDrawUV(self) -> bool:
        """Called by Maya to determine if this surface shape supports UV drawing."""
    def drawUV(self, view: Any, info: Any) -> MPxSurfaceShapeUI:
        """This method is called when the surface shape is selected and the texture view is open.  Users should override this method if their custom shape supports UVs."""
    def material(self, path: Any) -> MMaterial:
        """COMMENT"""
    def materials(self, path: Any, componentFilter: Any, materials: Any, componentSet: Any = None) -> MPxSurfaceShapeUI:
        """Returns the material associated with this shape."""
    def select(self, selectInfo: Any, selectionList: Any, worldSpaceSelectPts: Any) -> bool:
        """This routine must be overriden if the shape is to support interactive object and/or component selection. The implementation of this method should call selectInfo.addSelection with information about the selected item and its selection mask. For single click selection, detected using the selectInfo.singleSection() method, the hit point should also be passed as an argument to selectInfo.addSelection()."""
    def selectUV(self, view: Any, selType: Any, xmin: Any, ymin: Any, xmax: Any, ymax: Any, singleSelect: Any, selList: Any) -> bool:
        """This method is called when the user performs a selection within the texture view.  The method is called only when the surface shape is member of the active selection list."""
    def snap(self, snapInfo: Any) -> bool:
        """Maya calls this method when snapping to the shape's vertices."""
    def surfaceShape(self) -> MPxSurfaceShape:
        """Returns the non-ui shape associated with current instance."""
    @staticmethod
    def surfaceShapeUI(path: Any) -> MPxSurfaceShapeUI:
        """This is a static method that can be used to find the corresponding MPxSurfaceShapeUI for the specified path.  If an MPxSurfaceShapeUI does not exist then one is created."""

class MPxToolCommand:
    commandString: Any
    historyOn: Any
    kDouble: Any
    kLong: Any
    kNoArg: Any
    kString: Any
    def __init__(self) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def appendToResult(val: Any) -> None:
        """Append a value to the result to be returned by the command."""
    def cancel(self) -> None:
        """This method cancels the command."""
    @staticmethod
    def clearResult() -> None:
        """Clears the command's result."""
    @staticmethod
    def currentResult(*args: Any, **kwargs: Any) -> Any:
        """Returns the command's current result."""
    @staticmethod
    def currentResultType() -> Any:
        """Returns the type of the current result."""
    @staticmethod
    def displayError(theError: Any, showLineNumber: bool | None = None) -> None:
        """Display an error message."""
    @staticmethod
    def displayInfo(theInfo: Any) -> None:
        """Display an informational message."""
    @staticmethod
    def displayWarning(theWarning: Any, showLineNumber: bool | None = None) -> None:
        """Display a warning message."""
    def doFinalize(self) -> None:
        """Call this method with an MArgList representing your command."""
    def doIt(self, args: MArgList) -> None:
        """Called by Maya to execute the command."""
    def finalize(self) -> None:
        """This method is used to create a string representing the command"""
    def hasSyntax(self) -> bool:
        """Called by Maya to determine if the command provides an MSyntax object describing its syntax."""
    @staticmethod
    def isCurrentResultArray() -> bool:
        """Returns true if the command's current result is an array of values."""
    def isUndoable(self) -> bool:
        """Called by Maya to determine if the command supports undo."""
    def redoIt(self) -> None:
        """Called by Maya to redo a previously undone command."""
    @staticmethod
    def setResult(val: Any) -> None:
        """Set the value of the result to be returned by the command."""
    def syntax(self) -> MSyntax:
        """Returns the command's MSyntax object, if it has one."""
    def undoIt(self) -> None:
        """Called by Maya to undo a previously executed command."""

class MSelectInfo:
    highestPriority: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addSelection(self, item: Any, point: Any, list: Any, points: Any, mask: Any, isComponent: Any) -> MSelectInfo:
        """Adds components or objects to the active selection list."""
    def canDrawComponent(self, isDisplayOn: Any, compMask: Any) -> bool:
        """Convenience method to test if components specified by the given mask can be drawn."""
    def completelyInside(self) -> bool:
        """Returns True if the object being drawn is inside the viewing frustum."""
    def displayStatus(self) -> int:
        """Returns the status of the object to draw."""
    def displayStyle(self) -> int:
        """Returns the display appearance."""
    def getAlignmentMatrix(self) -> MMatrix:
        """Returns the alignment matrix."""
    def getLocalRay(self) -> Any:
        """Returns the selection ray defined by its starting point (MPoint) and its direction (MVector)."""
    def getPrototype(self, drawHandler: Any) -> MDrawRequest:
        """This method creates a draw request based on the current draw state."""
    def inSelect(self) -> bool:
        """Returns True during any interactive refresh, as when user is interacting with the scene in any way including camera changes, object or component TRS changes, etc. Use userChangingViewContext for determining whether user is changing the view using view context tools such as tumble, dolly or track."""
    def inUserInteraction(self) -> bool:
        """Returns True during any interactive refresh, as when user is changing the view using view context tools such as tumble, dolly or track.  Useful for changing drawing mode to something simpler to speed up interaction re-draw.  Use inUserInteraction for determining whether user is interacting with the scene in any way."""
    def inclusiveMatrix(self) -> MMatrix:
        """Returns the world space inclusive matrix."""
    def isRay(self) -> bool:
        """Returns True if there is a selection ray."""
    def multiPath(self) -> MDagPath:
        """Returns the path to the object to be drawn."""
    def objectDisplayStatus(self, displayObj: Any) -> bool:
        """Determines whether the specified objects are allowed to be displayed."""
    def pluginObjectDisplayStatus(self, pluginDisplayFilter: Any) -> bool:
        """Determines whether the specified plugin object is allowed to be displayed."""
    def projectionMatrix(self) -> MMatrix:
        """Returns the camera*projection matrix."""
    def selectClosest(self) -> bool:
        """Returns True if we want to select the closest object."""
    def selectForHilite(self, mask: Any) -> bool:
        """Given the selection mask, can this object be selected for the hilite list."""
    def selectOnHilitedOnly(self) -> bool:
        """Returns True if you can only select components if the object is hilited."""
    def selectPath(self) -> MDagPath:
        """Returns a path to the item that is being selected."""
    def selectRect(self) -> Any:
        """Get the current selection rectangle dimensions, defined by:"""
    def selectable(self, mask: Any) -> bool:
        """Given the selection mask, this method determines if the object is selectable."""
    def selectableComponent(self, displayed: Any, mask: Any) -> bool:
        """Given the selection mask, this method determines if the component is selectable."""
    def setMultiPath(self, path: Any) -> MSelectInfo:
        """Sets the path of the object to be drawn."""
    def setSnapPoint(self, point: Any) -> bool:
        """When a snapping operation is being performed the shape's overridden MPxSurfaceShapeUI.snap() method can call this method to set the point to be snapped to. If setSnapPoint() is called multiple times then the point passed in which is nearest to the current cursor location will be used. So the shape can either compute the snap point itself and call setSnapPoint() once or it can make a series of calls and let setSnapPoint() determine the closest of those for itself."""
    def singleSelection(self) -> bool:
        """This method determines if we want to select a single object."""
    def userChangingViewContext(self) -> bool:
        """Returns True during any interactive refresh, as when user is interacting with the scene in any way including camera changes, object or component TRS changes, etc. Use userChangingViewContext for determining whether user is changing the view using view context tools such as tumble, dolly or track."""
    def view(self) -> M3dView:
        """Returns the view that the current selection is taking place in."""

class MTextureEditorDrawInfo:
    drawingFunction: Any
    kDrawEdgeForSelect: Any
    kDrawEverything: Any
    kDrawFacetForSelect: Any
    kDrawFunctionFirst: Any
    kDrawFunctionLast: Any
    kDrawUVForSelect: Any
    kDrawVertexForSelect: Any
    kDrawWireframe: Any
    def __init__(self, in_: MTextureEditorDrawInfo | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MTimeSliderCustomDrawManager:
    kAbove: Any
    kBelow: Any
    kOn: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def clearDrawPrimitives(self, *args: Any, **kwargs: Any) -> Any: ...
    def deregisterCustomDraw(self, *args: Any, **kwargs: Any) -> Any: ...
    def registerCustomDrawOn(self, *args: Any, **kwargs: Any) -> Any: ...
    def registerCustomDrawOutside(self, *args: Any, **kwargs: Any) -> Any: ...
    def requestTimeSliderRedraw(self, *args: Any, **kwargs: Any) -> Any: ...
    def setBackgroundColor(self, *args: Any, **kwargs: Any) -> Any: ...
    def setDrawHeight(self, *args: Any, **kwargs: Any) -> Any: ...
    def setDrawLayer(self, *args: Any, **kwargs: Any) -> Any: ...
    def setDrawLocation(self, *args: Any, **kwargs: Any) -> Any: ...
    def setDrawPrimitives(self, *args: Any, **kwargs: Any) -> Any: ...
    def setDrawPriority(self, *args: Any, **kwargs: Any) -> Any: ...
    def setDrawVisible(self, *args: Any, **kwargs: Any) -> Any: ...
    def setEditPrimitiveFunction(self, *args: Any, **kwargs: Any) -> Any: ...
    def setSetCopyPrimitivesFunction(self, *args: Any, **kwargs: Any) -> Any: ...
    def setStartPrimitiveEditFunction(self, *args: Any, **kwargs: Any) -> Any: ...
    def setStopPrimitiveEditFunction(self, *args: Any, **kwargs: Any) -> Any: ...
    def setTooltip(self, *args: Any, **kwargs: Any) -> Any: ...

class MTimeSliderDrawPrimitive:
    bottom: Any
    color: Any
    drawType: Any
    endTime: Any
    height: Any
    kBracket: Any
    kFilledRect: Any
    kFrameFlag: Any
    kFullOutline: Any
    kMoveEndTime: Any
    kMovePrimitive: Any
    kMoveStartTime: Any
    kNone: Any
    kUpperOutline: Any
    kVerticalLine: Any
    label: Any
    priority: Any
    startTime: Any
    tooltip: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MUiMessage:
    kDefaultAction: Any
    kDoAction: Any
    kDoNotDoAction: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def add3dViewDestroyMsgCallback(panelName: Any, function: int, clientData: None = None) -> int:
        """This method registers a callback for when a particular 3d view gets"""
    @staticmethod
    def add3dViewPostRenderMsgCallback(panelName: Any, function: int, clientData: None = None) -> int:
        """This method registers a callback for when the 3d view is"""
    @staticmethod
    def add3dViewPreRenderMsgCallback(panelName: Any, function: int, clientData: None = None) -> int:
        """This method registers a callback for when a particular 3d view is"""
    @staticmethod
    def add3dViewRenderOverrideChangedCallback(panelName: Any, function: int, clientData: None = None) -> int:
        """This method registers a callback for when the render override for a"""
    @staticmethod
    def add3dViewRendererChangedCallback(panelName: Any, function: int, clientData: None = None) -> int:
        """This method registers a callback for when the renderer for a particular 3d"""
    @staticmethod
    def addCameraChangedCallback(panelName: Any, function: int, clientData: None = None) -> int:
        """This method registers a callback for cameras being changed in"""
    @staticmethod
    def addUiDeletedCallback(uiName: Any, function: int, clientData: None = None) -> int:
        """This method registers a callback for UI deleted messages."""
    @staticmethod
    def currentCallbackId() -> int:
        """Returns the callback ID of the currently executing callback. If called"""
    @staticmethod
    def nodeCallbacks(node: Any) -> int:
        """Returns a list of callback IDs registered to a given node."""
    @staticmethod
    def removeCallback(id: Any) -> None:
        """Removes the specified callback from Maya."""
    @staticmethod
    def removeCallbacks(ids: Any) -> None:
        """Removes all of the specified callbacks from Maya."""

class RenderParameters:
    baseColor: Any
    showAlphaMask: Any
    unfiltered: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class ShaderContext:
    path: Any
    shadingEngine: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""