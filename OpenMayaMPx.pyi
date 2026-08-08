# Stub for maya.OpenMayaMPx - OM1, signatures from Maya 2024 C++ API reference
from typing import Any, overload

from maya.OpenMayaUI import M3dView
from maya.OpenMaya import MArgList
from maya.OpenMaya import MArrayDataHandle
from maya.OpenMaya import MAttributePatternArray
from maya.OpenMaya import MAttributeSpecArray
from maya.OpenMaya import MBoundingBox
from maya.OpenMaya import MCacheFormatDescription
from maya.OpenMaya import MColor
from maya.OpenMaya import MDGContext
from maya.OpenMaya import MDGModifier
from maya.OpenMaya import MDagModifier
from maya.OpenMaya import MDagPath
from maya.OpenMaya import MDataBlock
from maya.OpenMaya import MDataHandle
from maya.OpenMaya import MDoubleArray
from maya.OpenMayaUI import MDrawRequest
from maya.OpenMaya import MEulerRotation
from maya.OpenMaya import MEvaluationNode
from maya.OpenMayaUI import MEvent
from maya.OpenMaya import MFileObject
from maya.OpenMaya import MFloatArray
from maya.OpenMaya import MFloatVectorArray
from maya.OpenMayaRender import MGeometryList
from maya.OpenMaya import MImage
from maya.OpenMaya import MImageFileInfo
from maya.OpenMaya import MIntArray
from maya.OpenMaya import MItGeometry
from maya.OpenMaya import MMatrix
from maya.OpenMaya import MNodeCacheDisablingInfo
from maya.OpenMaya import MNodeCacheSetupInfo
from maya.OpenMaya import MObject
from maya.OpenMaya import MObjectArray
from maya.OpenMaya import MPlane
from maya.OpenMaya import MPlug
from maya.OpenMaya import MPlugArray
from maya.OpenMaya import MPoint
from maya.OpenMaya import MPointArray
from maya.OpenMaya import MQuaternion
from maya.OpenMaya import MRenderPassDef
from maya.OpenMaya import MSelectionList
from maya.OpenMaya import MSelectionMask
from maya.OpenMaya import MTime
from maya.OpenMaya import MTimeRange
from maya.OpenMaya import MTransformationMatrix
from maya.OpenMaya import MTypeId
from maya.OpenMaya import MURI
from maya.OpenMayaRender import MUniformParameterList
from maya.OpenMayaRender import MVaryingParameterList
from maya.OpenMaya import MVector
from maya.OpenMaya import MVectorArray

class MStatus:
    ...

class MExternalContentInfoTable:
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, data: None) -> None:
        """Class constructor."""
    @overload
    def addResolvedEntry(self, key: str, unresolvedLocation: str, resolvedLocation: str, roles: Any) -> MStatus: ...
    @overload
    def addResolvedEntry(self, key: str, unresolvedLocation: str, resolvedLocation: str, contextNodeFullName: str, roles: Any) -> MStatus:
        """Deprecated in 2019.0"""
    @overload
    def addUnresolvedEntry(self, key: str, unresolvedLocation: str, roles: Any) -> MStatus: ...
    @overload
    def addUnresolvedEntry(self, key: str, unresolvedLocation: str, contextNodeFullName: str, roles: Any) -> MStatus:
        """Deprecated in 2016.0"""
    def getEntryByIndex(self, *args: Any, **kwargs: Any) -> Any: ...
    def getInfoByKey(self, *args: Any, **kwargs: Any) -> Any: ...
    def length(self) -> int:
        """Retrieves the number of entries in the table."""

class MExternalContentLocationTable:
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, data: Any) -> None:
        """Class constructor."""
    def addEntry(self, key: str, location: str) -> MStatus:
        """Adds an external content location and its key to the table."""
    def getEntryByIndex(self, *args: Any, **kwargs: Any) -> Any: ...
    def getLocationByKey(self, *args: Any, **kwargs: Any) -> Any: ...
    def length(self) -> int:
        """Retrieves the number of entries in the table."""

class MFnPlugin:
    kDefaultDataLocation: Any
    kImageFilePriorityDefault: Any
    kImageFilePriorityHigh: Any
    kImageFilePriorityHighest: Any
    kImageFilePriorityLow: Any
    kImageFilePriorityLowest: Any
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, object: MObject, vendor: str, version: str, requiredApiVersion: str) -> None:
        """Default class constructor."""
    @overload
    def addMenuItem(self, menuItemName: str, parentName: str, commandName: str, commandParams: str, needOptionBox: bool = False, optBoxFunction: str | None = None, extraMenuItemParams: str | None = None) -> Any: ...
    @overload
    def addMenuItem(self, menuItemName: str, menuItemLabel: str, parentName: str, commandName: str, commandParams: str, needOptionBox: bool = False, optBoxFunction: str | None = None, extraMenuItemParams: str | None = None) -> Any:
        """Deprecated in 2022.0"""
    def apiVersion(self) -> str:
        """Return the required API version string supplied in the MFnPlugin constructor."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def deregisterAnimCurveInterpolator(self, typeName: str) -> MStatus:
        """Deregister the given user defined animation curve interpolator from Maya."""
    def deregisterAttributePatternFactory(self, typeName: str) -> MStatus:
        """Deregister the attribute pattern factory type with Maya."""
    def deregisterCacheFormat(self, cacheFormatName: str) -> MStatus:
        """Deregister the specified cache format with Maya."""
    def deregisterCommand(self, commandName: str) -> MStatus:
        """Deregister the user defined command from Maya."""
    def deregisterConstraintCommand(self, commandName: str) -> MStatus:
        """Deregister the user defined constraint command from Maya."""
    @overload
    def deregisterContextCommand(self, commandName: str) -> MStatus: ...
    @overload
    def deregisterContextCommand(self, commandName: str, toolCmdName: str) -> MStatus:
        """Deregister the given user defined context command from Maya."""
    def deregisterControlCommand(self, commandName: str) -> MStatus:
        """Deregister the user defined control command from Maya."""
    def deregisterData(self, typeId: MTypeId) -> MStatus:
        """Deregister the given user defined data type from Maya."""
    def deregisterDevice(self, deviceName: str) -> MStatus:
        """Deregister the given user defined input device from Maya."""
    def deregisterDisplayFilter(self, name: str) -> MStatus:
        """Deregister a display filter with Maya."""
    def deregisterDragAndDropBehavior(self, behaviorName: str) -> MStatus:
        """Deregister the given drag and drop behavior from Maya."""
    def deregisterEvaluator(self, evaluatorName: str) -> MStatus:
        """Deregister the given user defined evaluator."""
    def deregisterFileTranslator(self, translatorName: str) -> MStatus:
        """Deregister the specified file translator with Maya."""
    def deregisterIkSolver(self, ikSolverName: str) -> MStatus:
        """Deregister the specified ik-solver with Maya."""
    def deregisterImageFile(self, imageFormatName: str) -> MStatus:
        """Deregister the specified image file translator with Maya."""
    def deregisterModelEditorCommand(self, commandName: str) -> MStatus:
        """Deregister the user defined editor command from Maya."""
    def deregisterNode(self, typeId: MTypeId) -> MStatus:
        """Deregister the given user defined dependency node type Maya."""
    def deregisterRenderPassImpl(self, passImplId: str) -> MStatus:
        """Deregister the specified render pass implementation with Maya."""
    def deregisterRenderer(self, name: str) -> MStatus:
        """Deregisters an renderer identified by name."""
    def deregisterTopologyEvaluator(self, evaluatorName: str) -> MStatus:
        """Introduced in 2019.0"""
    def deregisterURIFileResolver(self, fileResolverName: str) -> MStatus:
        """Deregister the specified URI file resolver with Maya."""
    @staticmethod
    def findPlugin(pluginName: str) -> MObject:
        """Returns an MObject corresponding to the named plugin."""
    def getCallableInfo(self) -> Any:
        """Get callback info to be passed as ClientData to scripts."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    @staticmethod
    def isNodeRegistered(typeName: str) -> bool:
        """Queries if the given typeName has been registered by maya or plugins."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def loadPath(self) -> str:
        """Determine the path where the plugin was loaded."""
    def matrixTypeIdFromXformId(self, xformTypeId: MTypeId) -> MTypeId:
        """The function returns the MTypeId of the matrix when the MTypeId of the corresponding xform is given."""
    def name(self) -> str:
        """Return the name by which Maya knows this plug-in."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def registerAnimCurveInterpolator(self, typeName: str, typeId: int, creatorFunction: Any, flags: int = 0) -> MStatus:
        """Register a new animation curve interpolator with Maya."""
    def registerAttributePatternFactory(self, typeName: str, fnPtr: Any) -> MStatus:
        """Registers a new attribute pattern factory type with Maya."""
    def registerBakeEngine(self, typeName: str, fnPtr: Any) -> MStatus:
        """Registers a new bake engine type with Maya."""
    def registerCacheFormat(self, cacheFormatName: str, creatorFunction: Any) -> MStatus:
        """Register a new cache format with Maya."""
    def registerCommand(self, commandName: str, creatorFunction: Any, createSyntaxFunction: Any = None) -> MStatus:
        """Register a new command with Maya."""
    def registerConstraintCommand(self, commandName: str, creatorFunction: Any) -> MStatus:
        """Register a new constraint command with Maya."""
    @overload
    def registerContextCommand(self, commandName: str, creatorFunction: Any) -> MStatus: ...
    @overload
    def registerContextCommand(self, commandName: str, creatorFunction: Any, toolCmdName: str, toolCmdCreator: Any, toolCmdSyntax: Any = None) -> MStatus:
        """Register a new context command with Maya."""
    def registerControlCommand(self, commandName: str, creatorFunction: Any) -> MStatus:
        """Register a new control command with Maya."""
    def registerData(self, typeName: str, typeId: MTypeId, creatorFunction: Any, type: int | None = None) -> MStatus:
        """Register a new data type with Maya."""
    def registerDevice(self, deviceName: str, creatorFunction: Any) -> MStatus:
        """Register a new input device with Maya."""
    def registerDisplayFilter(self, name: str, label: str, classification: str) -> MStatus:
        """Register a new display filter with Maya."""
    def registerDragAndDropBehavior(self, behaviorName: str, creatorFunction: Any) -> MStatus:
        """Register a new drag and drop behavior with Maya."""
    @overload
    def registerEvaluator(self, evaluatorName: str, uniquePriority: int, creatorFunction: Any) -> MStatus: ...
    @overload
    def registerEvaluator(self, evaluatorName: str, uniquePriority: int, creatorFunction: Any) -> MStatus:
        """Register a new evaluator with Maya."""
    def registerFileTranslator(self, translatorName: str, pixmapName: str, creatorFunction: Any, optionsScriptName: str | None = None, defaultOptionsString: str | None = None, requiresFullMel: bool = False, dataStorageLocation: str | None = None) -> MStatus:
        """Register a new file translator with Maya."""
    def registerIkSolver(self, ikSolverName: str, creatorFunction: Any) -> MStatus:
        """Register a new ik-solver with Maya."""
    def registerImageFile(self, imageFormatName: str, creatorFunction: Any, imageFileExtensions: Any, priority: Any) -> MStatus:
        """Changed in 2020.0"""
    def registerMaterialInfo(self, type: str, fnPtr: Any) -> MStatus:
        """Registers a new material information type with Maya."""
    def registerModelEditorCommand(self, commandName: str, creatorFunction: Any, paneCreatorFunction: Any) -> MStatus:
        """Register a new model editor command with Maya."""
    def registerNode(self, typeName: str, typeId: MTypeId, creatorFunction: Any, initFunction: Any, type: int | None = None, classification: str | None = None) -> MStatus:
        """Register a new dependency node with Maya."""
    def registerRenderPassImpl(self, passImplId: str, passDef: MRenderPassDef, creatorFunction: Any, overload: bool = False) -> MStatus:
        """Register a new render pass implementation with Maya and associate with the given render pass definition."""
    def registerRenderer(self, name: str, creatorFunction: Any) -> MStatus:
        """Registers a new renderer identified by name."""
    @overload
    def registerShape(self, typeName: str, typeId: MTypeId, creatorFunction: Any, initFunction: Any, uiCreatorFunction: Any, classification: str | None = None) -> MStatus: ...
    @overload
    def registerShape(self, typeName: str, typeId: MTypeId, creatorFunction: Any, initFunction: Any, classification: str | None = None) -> MStatus:
        """Registers the given user defined shape node with Maya."""
    @overload
    def registerTopologyEvaluator(self, evaluatorName: str, uniquePriority: int, creatorFunction: Any) -> MStatus: ...
    @overload
    def registerTopologyEvaluator(self, evaluatorName: str, uniquePriority: int, creatorFunction: Any) -> MStatus:
        """Introduced in 2019.0"""
    @overload
    def registerTransform(self, typeName: str, typeId: MTypeId, creatorFunction: Any, initFunction: Any, xformCreatorFunction: Any, xformId: MTypeId, classification: str | None = None) -> MStatus: ...
    @overload
    def registerTransform(self, typeName: str, typeId: MTypeId, creatorFunction: Any, initFunction: Any, xformCreatorFunction: Any, xformId: MTypeId, classification: str | None = None) -> MStatus:
        """Registers the given user defined transform node with Maya."""
    @overload
    def registerUI(self, creationProc: Any, deletionProc: Any, creationBatchProc: Any = None, deletionBatchProc: Any = None) -> MStatus: ...
    @overload
    def registerUI(self, creationProc: str, deletionProc: str, creationBatchProc: str, deletionBatchProc: str) -> MStatus:
        """Sets the Python callable objects to be called to create and destroy any UI associated with the plugin."""
    def registerUIStrings(self, registerMStringResources: Any, pluginStringsProc: str) -> MStatus:
        """Set the callback and procedure names of routines that register plugin string resources and optionally load localized val"""
    def registerURIFileResolver(self, fileResolverName: str, uriScheme: str, creatorFunction: Any) -> MStatus:
        """Register a Custom URI File Resolver with Maya."""
    @staticmethod
    def registeringCallableScript() -> bool:
        """Return true if this MFnPlugin object has its callbacks defined in script."""
    def removeMenuItem(self, menuItemNames: Any) -> MStatus:
        """The function removes the menuItem and the corresponding option box, if exists, from the UI."""
    def setCallableInfo(self, info: Any) -> None:
        """Set callback info to be passed as ClientData to scripts."""
    def setName(self, newName: str, allowRename: bool = True) -> MStatus:
        """Set the name by which Maya knows this plug-in."""
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches the Function Set to the specified Maya Object."""
    @staticmethod
    def setRegisteringCallableScript() -> None:
        """Mark this MFnPlugin object as one that will be passed callbacks defined in script."""
    def setVersion(self, newVersion: str) -> MStatus:
        """Set the version name for this plug-in."""
    def type(self) -> int:
        """Return the type of this function set."""
    @staticmethod
    def typeString(Type: int) -> str:
        """Introduced in 2020.0"""
    def unregisterBakeEngine(self, typeName: str) -> MStatus:
        """Deregister the bake engine type with Maya."""
    def unregisterMaterialInfo(self, typeName: str) -> MStatus:
        """Deregister the specified material info type with Maya."""
    def vendor(self) -> str:
        """Return the vendor string supplied in the MFnPlugin constructor."""
    def version(self) -> str:
        """Return the version string supplied in the MFnPlugin constructor."""

class MPx3dModelView:
    kFogCoordinate: Any
    kFogExponential: Any
    kFogExponentialSquared: Any
    kFogFragment: Any
    kFogLinear: Any
    kLightActive: Any
    kLightAll: Any
    kLightDefault: Any
    kLightNone: Any
    kLightQuality: Any
    kLightSelected: Any
    thisown: Any
    def __init__(self) -> None:
        """class constructor"""
    def backgroundColor(self) -> MColor:
        """Returns the value of the background color."""
    def backgroundColorBottom(self) -> MColor:
        """Returns the value of the background gradient bottom color."""
    def backgroundColorTop(self) -> MColor:
        """Returns the value of the background gradient top color."""
    def beginGL(self) -> MStatus:
        """Setup port for native OpenGL drawing calls."""
    def beginXorDrawing(self, lineWidth: float, lineColor: MColor, drawOrthographic: bool = True, disableDepthTesting: bool = True, stipplePattern: int | None = None) -> MStatus:
        """Setup the context for exclusive-or (XOR) drawing."""
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def colorAtIndex(self, index: int, table: int | None = None) -> MColor:
        """Returns the value of the color at the given index in the application's color table."""
    def customDraw(self, *args: Any, **kwargs: Any) -> Any: ...
    def customDrawEnabled(self, *args: Any, **kwargs: Any) -> Any: ...
    def destroyOnPanelDestruction(self) -> bool:
        """This method queries the destruction setting for this MPx3dModelView which is employed when the panel associated with thi"""
    def displayAxisAtOriginOn(self) -> bool:
        """Returns the origin axis display state for this MPx3dModelView ."""
    def displayAxisOn(self) -> bool:
        """Returns the axis display state for this MPx3dModelView ."""
    def displayCameraAnnotationOn(self) -> bool:
        """Returns the camera annotation display state for this MPx3dModelView ."""
    def displayHUD(self) -> bool:
        """Returns the heads up display state for this view."""
    def displayStyle(self) -> int:
        """Return the display style for this 3d view."""
    def doUpdateOnMove(self) -> bool:
        """Returns the state of the doUpdateOnMove flag."""
    def drawAdornments(self) -> bool:
        """Returns the state of the adornment drawing for this view."""
    def drawAdornmentsNow(self) -> MStatus:
        """Forces the adornment viewport elements to be drawn immediately."""
    def drawHUDNow(self) -> MStatus:
        """Forces the HUD viewport elements to be drawn immediately."""
    def drawInterrupt(self, *args: Any, **kwargs: Any) -> Any: ...
    def drawOnePass(self, *args: Any, **kwargs: Any) -> Any: ...
    def drawText(self, text: str, position: MPoint, textPosition: int | None = None) -> MStatus:
        """Draws the given text at the given spot in the default font."""
    def endGL(self) -> MStatus:
        """End OpenGL drawing."""
    def endXorDrawing(self) -> MStatus:
        """Reset the context to non-exclusive-or (non-XOR) screen drawing."""
    def filteredObjectList(self, list: MSelectionList) -> MStatus:
        """Returns a selection list containing all of the objects that remain after filtering is applied to the view."""
    def fogColor(self) -> MColor:
        """Returns the fog color."""
    def fogDensity(self) -> float:
        """Returns the fog density."""
    def fogEnd(self) -> float:
        """Returns the fog end position."""
    def fogMode(self) -> int:
        """Return the type of drop off used with fog."""
    def fogSource(self) -> int:
        """Returns the algorithm used to compute fog."""
    def fogStart(self) -> float:
        """Returns the fog start position."""
    def getAsM3dView(self, view: M3dView) -> MStatus:
        """Get this MPx3dModelView as a M3dView ."""
    def getCamera(self, camera: MDagPath) -> MStatus:
        """Get the camera for this view."""
    def getCameraHUDName(self) -> str:
        """Return the name to use for the camera in the heads up display."""
    def getCameraSet(self, cameraSet: MObject) -> MStatus:
        """Get the cameraSet for this view."""
    def getColorIndexAndTable(self, glindex: int, index: int, table: int) -> MStatus:
        """Returns the color table and index representing the given OpenGL color-index value."""
    def getCurrentCameraSetCamera(self, cameraName: str) -> MStatus:
        """Get the cameraSet for this view."""
    @staticmethod
    def getModelView(name: str) -> MPx3dModelView:
        """Returns a pointer to a MPx3dModelView that has the passed name with the specified type (the same typed when registering """
    def getObjectsToView(self, list: MSelectionList) -> MStatus:
        """Returns a selection list containing all of the objects on the view selected list."""
    def handleDraw(self, *args: Any, **kwargs: Any) -> Any: ...
    def hasStereoBufferSupport(self) -> bool:
        """Returns true if this 3dModelView is running in stereo buffer mode."""
    def includeInvisible(self, *args: Any, **kwargs: Any) -> Any: ...
    def isBackfaceCulling(self) -> bool:
        """Returns the state of backface culling."""
    def isBackgroundFogEnabled(self) -> bool:
        """Returns true if the background fog is enabled."""
    def isBackgroundGradient(self) -> bool:
        """Returns whether a gradient is being used as the background color."""
    def isFogEnabled(self) -> bool:
        """Returns true if fog is enabled."""
    def isShadeActiveOnly(self) -> bool:
        """Returns true if this view's display style is shaded for objects that are active and wireframe otherwise."""
    def isTextureDisplayEnabled(self) -> bool:
        """Returns the enable state of texture display."""
    def isTwoSidedLighting(self) -> bool:
        """Returns the state of two sided lighting."""
    def isVisible(self) -> bool:
        """This method returns true if this view is visible, otherwise false is returned."""
    def isWireframeOnShaded(self) -> bool:
        """Returns the state of wireframe on shaded."""
    def isXrayEnabled(self) -> bool:
        """Returns the state of xray display."""
    def lightingMode(self) -> int:
        """Returns the lighting mode."""
    def multipleDrawEnabled(self) -> bool:
        """This method returns the multiple draw enable state for this view."""
    def multipleDrawPassCount(self) -> int:
        """This method returns the number of multiple draw passes that are going to be made."""
    def name(self) -> str:
        """Returns the name of the view."""
    def numActiveColors(self) -> int:
        """Returns the number of active object colors in the internal application color table."""
    def numDormantColors(self) -> int:
        """Returns the number of dormant object colors in the internal application color table."""
    def numUserDefinedColors(self) -> int:
        """Returns the number of user defined colors in the internal application color table."""
    def objectDisplay(self, DisplayObjects: int) -> bool:
        """Test whether specific types of objects are to be displayed."""
    def okForMultipleDraw(self) -> bool:
        """This method provides some filter capabilities as to what is drawn."""
    def portHeight(self) -> int:
        """Returns the height of the current viewport."""
    def portWidth(self) -> int:
        """Returns the width of the current viewport."""
    def postMultipleDraw(self) -> None:
        """This method is called after the drawing is finished."""
    def postMultipleDrawPass(self, index: int) -> None:
        """This method is called when a specified pass is finshed."""
    def preMultipleDraw(self) -> None:
        """This method is called before any drawing is performed in the model view."""
    def preMultipleDrawPass(self, index: int) -> None:
        """This method is called immediately before a specific pass is about to be drawn."""
    def processDraw(self, *args: Any, **kwargs: Any) -> Any: ...
    def refresh(self, all: bool = False, force: bool = False) -> MStatus:
        """Refresh the this view."""
    def removingCamera(self, cameraPath: MDagPath) -> None:
        """This method should be overloaded in MPx3dModelView derived classes."""
    def requestOkForDraw(self) -> bool:
        """This method provides some filter capabilities as to what is drawn."""
    def setBackfaceCulling(self, cull: bool) -> MStatus:
        """Sets backface culling."""
    def setBackgroundFogEnabled(self, enable: bool) -> MStatus:
        """Enables and disables background fog."""
    def setCamera(self, camera: MDagPath) -> MStatus:
        """Set the camera for this view."""
    def setCameraInDraw(self, camera: MDagPath) -> MStatus:
        """Sets the camera during a draw."""
    def setCameraSet(self, cameraSet: MObject) -> MStatus:
        """Set the cameraSet for this view."""
    def setCurrentCameraSetCamera(self, cameraName: str) -> MStatus:
        """Set a camera used by the currently specified cameraSet as the controlled camera for this view."""
    def setCustomDrawEnable(self, *args: Any, **kwargs: Any) -> Any: ...
    def setDestroyOnPanelDestruction(self, how: bool) -> None:
        """This method enables/disables destruction of the MPx3dModelView object when the panel is destroyed."""
    def setDisplayAxis(self, display: bool) -> MStatus:
        """Sets the axis display in the MPx3dModelView ."""
    def setDisplayAxisAtOrigin(self, display: bool) -> MStatus:
        """Sets the origin axis display in the MPx3dModelView ."""
    def setDisplayCameraAnnotation(self, display: bool) -> MStatus:
        """Sets the camera annotation display in the MPx3dModelView ."""
    def setDisplayHUD(self, display: bool) -> MStatus:
        """Enables or disables the drawing the heads up display in this view."""
    def setDisplayStyle(self, style: int, activeOnly: bool = False) -> MStatus:
        """Sets the display style for this view."""
    def setDoUpdateOnMove(self, value: bool) -> MStatus:
        """Some viewports require a refresh when the user has moved the top level window."""
    def setDrawAdornments(self, display: bool) -> MStatus:
        """Toggles the control of how adornments are drawn in the view."""
    @overload
    def setDrawCameraOverride(self, worldMatrix: MMatrix, projectionMatrix: MMatrix, left: float, right: float, bottom: float, top: float, nearpt: float, farpt: float, isOrtho: bool = False) -> MStatus: ...
    @overload
    def setDrawCameraOverride(self, worldMatrix: MMatrix, projectionMatrix: MMatrix, frustum: MPointArray) -> MStatus:
        """Sets the camera during a draw."""
    @overload
    def setDrawColor(self, index: int, table: int | None = None) -> MStatus: ...
    @overload
    def setDrawColor(self, color: MColor) -> MStatus:
        """Set the color to draw in."""
    def setDrawInterrupt(self, *args: Any, **kwargs: Any) -> Any: ...
    def setFogColor(self) -> MStatus:
        """Sets the color used for hardware fogging."""
    def setFogDensity(self, arg: Any) -> MStatus:
        """Determines the density of hardware fogging."""
    def setFogEnabled(self, state: bool) -> MStatus:
        """Enables and disables fog."""
    def setFogEnd(self, arg: Any) -> MStatus:
        """Determines the end location of hardware fogging."""
    def setFogMode(self, FogMode: int) -> MStatus:
        """Sets the drop-off mode for fog."""
    def setFogSource(self, FogSource: int) -> MStatus:
        """Sets the type of fog algorithm to use."""
    def setFogStart(self, arg: Any) -> MStatus:
        """Determines the start location of hardware fogging."""
    def setInStereoDrawMode(self, flag: bool) -> MStatus:
        """Derived classes should call this method to indicate to Maya whether the view is currently drawing in stereo."""
    def setIncludeInvisible(self, *args: Any, **kwargs: Any) -> Any: ...
    def setLightingMode(self, LightingMode: int) -> MStatus:
        """Sets the lighting mode."""
    def setMultipleDrawEnable(self, enable: bool) -> None:
        """This method turns enables/disables multiple camera drawing for this view."""
    def setObjectDisplay(self, DisplayObjects: int, arg: Any) -> MStatus:
        """Sets the display option for various types of objects."""
    def setObjectsToView(self, list: MSelectionList) -> MStatus:
        """Sets the list of objects used by view selected as a selection list."""
    def setTextureDisplayEnabled(self, texture: bool) -> MStatus:
        """Enables texture display."""
    def setTwoSidedLighting(self, twoSided: bool) -> MStatus:
        """Enables two sided lighting."""
    def setUserDefinedColor(self, index: int, color: MColor) -> MStatus:
        """Sets the user defined color at the given index."""
    def setViewSelected(self, viewSelected: bool) -> MStatus:
        """Enables the view selected mode."""
    def setViewSelectedPrefix(self, prefix: str) -> MStatus:
        """Sets the prefix for the camera name as displayed in the heads up display when view selected is enabled."""
    def setViewSelectedSet(self, set: MObject) -> MStatus:
        """Sets the list of objects used by view selected as an object set."""
    def setWireframeOnShaded(self, on: bool) -> MStatus:
        """Displays as wireframe on shaded."""
    def setXrayEnabled(self, xray: bool) -> MStatus:
        """Sets xray display state."""
    def templateColor(self) -> MColor:
        """Returns the value of the template color."""
    def updateViewingParameters(self) -> MStatus:
        """This method tells the camera to set the view's transformation matrix."""
    def userDefinedColorIndex(self, index: int) -> int:
        """Returns the index for the given user-defined color."""
    def viewIsFiltered(self) -> bool:
        """Returns the state of view filtering for this view."""
    def viewSelected(self) -> bool:
        """Returns the state of view selected for this view."""
    def viewSelectedPrefix(self) -> str:
        """Returns the prefix used when displaying the camera name in the heads up display when view selected in on."""
    def viewSelectedSet(self) -> MObject:
        """Returns an MObject for the set used by view selected."""
    def viewToObjectSpace(self, x_pos: Any, y_pos: Any, localMatrixInverse: MMatrix, oPt: MPoint, oVector: MVector) -> MStatus:
        """Takes a point in port coordinates and returns a corresponding ray in object coordinates."""
    @overload
    def viewToWorld(self, x_pos: Any, y_pos: Any, worldPt: MPoint, worldVector: MVector) -> MStatus: ...
    @overload
    def viewToWorld(self, x_pos: Any, y_pos: Any, nearClipPt: MPoint, farClipPt: MPoint) -> MStatus:
        """Takes a point in port coordinates and returns a corresponding ray in world coordinates."""
    def viewType(self) -> str:
        """Returns a string specifying the view type."""
    def wantStereoGLBuffer(self) -> bool:
        """Users should override this method if they want a stereo buffer enabled MPx3dModelView ."""
    def worldToView(self, worldPt: MPoint, x_pos: Any, y_pos: Any) -> bool:
        """converts a point in world space to port space."""

class MPxAnimCurveInterpolator:
    kEvaluateAtKey: Any
    kLockType: Any
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def evaluate(self, val: MTime) -> float:
        """Compute an interpolated keyframe value at the given time, which is an absolute time between the start and end times."""
    def initialize(self, animCurve: MObject, keyIndex: int) -> None:
        """Initialize the interpolator to evaluate keyframe values within the time span of the given interval."""
    def typeId(self) -> int:
        """Returns the tangent type of this curve."""
    def typeName(self) -> str:
        """Returns the name under which the interpolator type was registered."""

class MPxAssembly:
    caching: Any
    frozen: Any
    isHistoricallyInteresting: Any
    kAssembly: Any
    kBlendShape: Any
    kCameraSetNode: Any
    kClientDeviceNode: Any
    kConstraintNode: Any
    kDefaultScheduling: Any
    kDeformerNode: Any
    kDependNode: Any
    kEmitterNode: Any
    kEvaluatedDirectly: Any
    kEvaluatedIndirectly: Any
    kFieldNode: Any
    kFluidEmitterNode: Any
    kGeometryFilter: Any
    kGloballySerial: Any
    kGloballySerialize: Any
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
    kParallel: Any
    kParticleAttributeMapperNode: Any
    kPostEvaluationTypeLast: Any
    kSchedulingTypeLast: Any
    kSerial: Any
    kSerialize: Any
    kSkinCluster: Any
    kSpringNode: Any
    kSurfaceShape: Any
    kThreadedDeviceNode: Any
    kTransformNode: Any
    kUntrusted: Any
    message: Any
    state: Any
    thisown: Any
    def __init__(self) -> None:
        """Class constructor."""
    def activate(self, rep: str) -> bool:
        """Activate a representation in the list of representations."""
    def activateRep(self, representation: str) -> bool:
        """Called during activation to activate the new active representation."""
    def activating(self) -> bool:
        """Return true when this assembly is activating a representation, within a call to activate() or activateNonRecursive()."""
    def addAddAttrEdit(self, targetAssembly: str, nodeName: str, longAttributeName: str, shortAttributeName: str, parameters: str, editData: MPxEditData | None = None) -> MStatus:
        """Add an add attribute edit to be applied by Maya when switching representations."""
    @staticmethod
    def addAttribute(attr: MObject) -> MStatus:
        """This method adds a new attribute to a user defined node type during the type's initialization."""
    def addConnectAttrEdit(self, targetAssembly: str, srcPlugName: str, dstPlugName: str, editData: MPxEditData | None = None) -> MStatus:
        """Add a connect attribute edit to be applied by Maya when switching representations."""
    def addDeleteAttrEdit(self, targetAssembly: str, nodeName: str, attributeName: str, editData: MPxEditData | None = None) -> MStatus:
        """Add a delete attribute edit to be applied by Maya when switching representations."""
    def addDisconnectAttrEdit(self, targetAssembly: str, srcPlugName: str, dstPlugName: str, editData: MPxEditData | None = None) -> MStatus:
        """Add a disconnect attribute edit to be applied by Maya when switching representations."""
    def addEdits(self) -> MStatus:
        """Add edits so they can be applied by Maya when switching representations."""
    def addExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Adds content info to the specified table from a file path attribute."""
    def addParentEdit(self, targetAssembly: str, childNodeName: str, parentNodeName: str, parameters: str, editData: MPxEditData | None = None) -> MStatus:
        """Add a parent edit to be applied by Maya when switching representations."""
    def addSetAttrEdit(self, targetAssembly: str, plugName: str, parameters: str, editData: MPxEditData | None = None) -> MStatus:
        """Add a set attribute edit to be applied by Maya when switching representations."""
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> MStatus: ...
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject, affectsTopology: bool) -> MStatus:
        """This method specifies that a particular input attribute affects a specific output attribute."""
    def beforeSave(self) -> None:
        """Method called by Maya to allow assemblies to do any required preparation before file save."""
    def canRepApplyEdits(self, representation: str) -> bool:
        """Determines whether the given representation can apply edits to its data."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def compute(self) -> MStatus:
        """This method should be overridden in user defined nodes."""
    def configCache(self) -> None:
        """Introduced in 2020.0"""
    def connectionBroken(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are made to attributes of this node."""
    def copyInternalData(self) -> None:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def createRepresentation(self, input: str, type: str, representation: str, undoRedo: MDagModifier | None = None) -> str:
        """Create a representation and add it to the list of representations."""
    def deleteAllRepresentations(self) -> MStatus:
        """Delete all representations managed by this node."""
    def deleteRepresentation(self, rep: str) -> MStatus:
        """Delete a representation managed by the node."""
    def dependsOn(self, depends: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    def getActive(self) -> str:
        """Get the active representation in the list of representations."""
    def getCacheSetup(self) -> None:
        """Introduced in 2020.0"""
    def getExternalContent(self, table: MExternalContentInfoTable) -> None:
        """Returns the external content (files) that this node depends on."""
    def getFilesToArchive(self, shortName: bool = False, unresolvedName: bool = False, markCouldBeImageSequence: bool = False) -> Any:
        """Use this method to return all external files used by this node."""
    @overload
    def getInitialRep(self, assembly: MObject, hasInitialRep: bool) -> str: ...
    @overload
    def getInitialRep(self, assembly: MObject) -> str:
        """Get the initial representation to use when the specified assembly is first loaded."""
    def getInstancePtr(self, *args: Any, **kwargs: Any) -> Any: ...
    def getInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def getInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def getRepLabel(self, rep: str) -> str:
        """Get the label of the argument representation."""
    def getRepNamespace(self) -> str:
        """Get the representations namespace of this assembly node."""
    def getRepType(self, rep: str) -> str:
        """Get the type of the argument representation."""
    def getRepresentations(self) -> Any:
        """Returns an array of the representations managed by the node attached to this function set."""
    def handlesAddEdits(self) -> bool:
        """Determines whether the assembly is responsible for supplying edits to its data."""
    def hasInvalidationRangeTransformation(self) -> bool:
        """Introduced in 2020.0"""
    def inactivateRep(self) -> bool:
        """Called during activation to inactivate the currently active representation."""
    @staticmethod
    def inheritAttributesFrom(parentClassName: str) -> MStatus:
        """This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node."""
    @overload
    def internalArrayCount(self) -> int: ...
    @overload
    def internalArrayCount(self) -> int:
        """This method is overridden by nodes that have internal array attributes which are not stored in Maya's datablock."""
    def isAbstractClass(self) -> bool:
        """Override this class to return true if this node is an abstract node."""
    def isActive(self, rep: str) -> bool:
        """Determines whether the argument representation is the active representation."""
    def isPassiveOutput(self) -> bool:
        """This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent val"""
    def isTrackingTopology(self) -> bool:
        """Introduced in 2019.0"""
    def legalConnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal connections being made to attributes of this node."""
    def legalDisconnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal disconnections being made to attributes of this node."""
    def memberAdded(self, member: MObject) -> None:
        """Called immediately after the argument node has been added to this assembly."""
    def memberRemoved(self, member: MObject) -> None:
        """Called immediately after the argument node has been removed from this assembly."""
    def name(self) -> str:
        """Returns the name of this particular instance of this class."""
    def passThroughToMany(self) -> bool:
        """This method is overridden by nodes that want to control the traversal behavior of some Maya search algorithms which trav"""
    def passThroughToOne(self) -> MPlug:
        """This method may be overridden by nodes that have a one-to-one relationship between an input attribute and a correspondin"""
    def performActivate(self, representation: str) -> bool:
        """Provide access to the Maya core representation activation functionality."""
    def performInactivate(self) -> bool:
        """Provide access to the Maya core representation inactivation functionality."""
    def postActivateRep(self, representation: str) -> None:
        """Called after activation of a representation including the load, activation and edits of any created sub-assemblies but p"""
    def postApplyEdits(self) -> None:
        """Method called by performActivate() just after edits are applied."""
    def postConstructor(self) -> None:
        """Post constructor."""
    def postEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode, evalType: Any) -> MStatus:
        """Clean up node's internal state after threaded evaluation."""
    def postLoad(self) -> None:
        """Method called by Maya to initialize assemblies after their creation."""
    def postUnapplyEdits(self) -> None:
        """Method called by performInactivate() just after edits are unapplied."""
    def preApplyEdits(self) -> None:
        """Method called by performActivate() just before edits are applied."""
    def preEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode) -> MStatus:
        """Prepare a node's internal state for threaded evaluation."""
    def preUnapplyEdits(self) -> None:
        """Method called by performInactivate() just before edits are unapplied."""
    def repTypes(self) -> Any:
        """Return the list of representation types that can be created for this assembly node."""
    def schedulingType(self) -> Any:
        """When overridden this method controls the degree of parallelism supported by the node during threaded evaluation."""
    def setDependentsDirty(self, plug: MPlug, plugArray: MPlugArray) -> MStatus:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug """
    def setExistWithoutInConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without input connections."""
    def setExistWithoutOutConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without output connections."""
    def setExternalContent(self) -> None:
        """Changes the location of external content in batch."""
    def setExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Sets content info in the specified attribute from the table."""
    def setInstancePtr(self, *args: Any, **kwargs: Any) -> Any: ...
    def setInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def setRepLabel(self, rep: str, label: str) -> MStatus:
        """Change the representation label."""
    def setRepName(self, rep: str, newName: str) -> str:
        """Rename a representation."""
    def shouldSave(self, isSaving: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def supportsEdits(self) -> bool:
        """Opt in/out of Maya's edit tracking system."""
    def supportsMemberChanges(self) -> bool:
        """Can members of the assembly be changed?"""
    def thisMObject(self) -> MObject:
        """Returns the MObject associated with this user defined node."""
    def transformInvalidationRange(self, source: MPlug, input: MTimeRange) -> MTimeRange:
        """Introduced in 2020.0"""
    def type(self) -> int:
        """Returns the type of node that this is."""
    def typeId(self) -> MTypeId:
        """Returns the TYPEID of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""
    def updateRepNamespace(self, repNamespace: str) -> None:
        """This method is called by Maya to tell the assembly that the base representation namespace specified by getRepNamespace()"""

class MPxAttributePatternFactory:
    thisown: Any
    def __init__(self) -> None:
        """Class constructor."""
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def createPatternsFromFile(self, patternFile: str, createdPatterns: MAttributePatternArray) -> MStatus:
        """Call this to define a new attribute pattern using the pattern factory format definition passed in through the contents o"""
    def createPatternsFromString(self, patternString: str, createdPatterns: MAttributePatternArray) -> MStatus:
        """Call this to define a new attribute pattern using the pattern factory format definition passed in through the string par"""
    def name(self) -> str:
        """Return the name of the pattern factory."""

class MPxBakeEngine:
    thisown: Any
    def __init__(self) -> None:
        """Constructor."""
    def bake(self, objectPath: MDagPath, cameraPath: MDagPath, samplePlug: MPlug, bakeResult: MImage) -> MStatus:
        """Bake the texture Maya will use to approximate shading properties."""
    def getUVRange(self, minUV: MFloatArray, maxUV: MFloatArray) -> None:
        """Tells Maya the UV range the baked texture should cover."""
    def setNeedTransparency(self, t: bool) -> None:
        """Set whether the bake engine needs to produce an image with transparency."""

class MPxBlendShape:
    caching: Any
    componentTagExpression: Any
    envelope: Any
    frozen: Any
    groupId: Any
    input: Any
    inputComponentsTarget: Any
    inputGeom: Any
    inputGeomTarget: Any
    inputPointsTarget: Any
    inputTarget: Any
    inputTargetGroup: Any
    inputTargetItem: Any
    isHistoricallyInteresting: Any
    kAssembly: Any
    kBlendShape: Any
    kCameraSetNode: Any
    kClientDeviceNode: Any
    kConstraintNode: Any
    kDefaultScheduling: Any
    kDeformerNode: Any
    kDeformsAll: Any
    kDeformsColors: Any
    kDeformsUVs: Any
    kDependNode: Any
    kEmitterNode: Any
    kEvaluatedDirectly: Any
    kEvaluatedIndirectly: Any
    kFieldNode: Any
    kFluidEmitterNode: Any
    kGeometryFilter: Any
    kGloballySerial: Any
    kGloballySerialize: Any
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
    kParallel: Any
    kParticleAttributeMapperNode: Any
    kPostEvaluationTypeLast: Any
    kSchedulingTypeLast: Any
    kSerial: Any
    kSerialize: Any
    kSkinCluster: Any
    kSpringNode: Any
    kSurfaceShape: Any
    kThreadedDeviceNode: Any
    kTransformNode: Any
    kUntrusted: Any
    message: Any
    outputGeom: Any
    state: Any
    targetWeights: Any
    thisown: Any
    weight: Any
    def __init__(self) -> None:
        """Class constructor."""
    def accessoryAttribute(self) -> MObject:
        """This method returns an MObject for the attribute to which an accessory shape is connected."""
    def accessoryNodeSetup(self, cmd: MDagModifier) -> MStatus:
        """This method is called by the "deformer -type" command when your node is specified."""
    @staticmethod
    def addAttribute(attr: MObject) -> MStatus:
        """This method adds a new attribute to a user defined node type during the type's initialization."""
    def addExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Adds content info to the specified table from a file path attribute."""
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> MStatus: ...
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject, affectsTopology: bool) -> MStatus:
        """This method specifies that a particular input attribute affects a specific output attribute."""
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
    def compute(self) -> MStatus:
        """This method should be overridden in user defined nodes."""
    def configCache(self) -> None:
        """Introduced in 2020.0"""
    def connectionBroken(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are made to attributes of this node."""
    def copyInternalData(self) -> None:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def deform(self, block: MDataBlock, iter: MItGeometry, mat: MMatrix, multiIndex: int) -> MStatus:
        """This method performs the deformation algorithm."""
    def deformData(self, block: MDataBlock, geomData: MDataHandle, groupId: int, mat: MMatrix, multiIndex: int) -> MStatus:
        """This method performs the deformation algorithm."""
    def dependsOn(self, depends: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    def getCacheSetup(self) -> None:
        """Introduced in 2020.0"""
    def getDeformationDetails(self) -> int:
        """Retrieves the value set by setDeformationDetails() ."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> None:
        """Returns the external content (files) that this node depends on."""
    def getFilesToArchive(self, shortName: bool = False, unresolvedName: bool = False, markCouldBeImageSequence: bool = False) -> Any:
        """Use this method to return all external files used by this node."""
    def getFixedSetupData(self, name: str) -> MObject:
        """Introduced in 2022.0"""
    def getGeometryIterator(self, iter: MItGeometry, block: MDataBlock, dataHandle: MDataHandle, multiIndex: int, readOnly: bool = True) -> int:
        """Introduced in 2022.0"""
    def getInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def getInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def hasInvalidationRangeTransformation(self) -> bool:
        """Introduced in 2020.0"""
    def indexMapper(self, multiIndex: int) -> Any:
        """Introduced in 2024.0"""
    @staticmethod
    def inheritAttributesFrom(parentClassName: str) -> MStatus:
        """This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node."""
    @overload
    def internalArrayCount(self) -> int: ...
    @overload
    def internalArrayCount(self) -> int:
        """This method is overridden by nodes that have internal array attributes which are not stored in Maya's datablock."""
    def isAbstractClass(self) -> bool:
        """Override this class to return true if this node is an abstract node."""
    def isPassiveOutput(self) -> bool:
        """This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent val"""
    def isTrackingTopology(self) -> bool:
        """Introduced in 2019.0"""
    def legalConnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal connections being made to attributes of this node."""
    def legalDisconnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal disconnections being made to attributes of this node."""
    def name(self) -> str:
        """Returns the name of this particular instance of this class."""
    def passThroughToMany(self) -> bool:
        """This method is overridden by nodes that want to control the traversal behavior of some Maya search algorithms which trav"""
    def passThroughToOne(self) -> MPlug:
        """This method may be overridden by nodes that have a one-to-one relationship between an input attribute and a correspondin"""
    def postConstructor(self) -> None:
        """Post constructor."""
    def postEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode, evalType: Any) -> MStatus:
        """Clean up node's internal state after threaded evaluation."""
    def preEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode) -> MStatus:
        """Prepare a node's internal state for threaded evaluation."""
    def schedulingType(self) -> Any:
        """When overridden this method controls the degree of parallelism supported by the node during threaded evaluation."""
    def setDeformationDetails(self, flags: int) -> MStatus:
        """This method allows the plug-in node to inform the system that it intends to deform components other than just positions."""
    def setDependentsDirty(self, plug: MPlug, plugArray: MPlugArray) -> MStatus:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug """
    def setExistWithoutInConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without input connections."""
    def setExistWithoutOutConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without output connections."""
    def setExternalContent(self) -> None:
        """Changes the location of external content in batch."""
    def setExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Sets content info in the specified attribute from the table."""
    def setInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def setModifiedCallback(self, list: MSelectionList, listAdded: bool) -> None:
        """This callback method can be overriden and is called whenever the set this deformer is operating on is modified."""
    def setUseExistingConnectionWhenSetEditing(self, state: bool) -> None:
        """This method allows the plugin node to request special treatment during set editing."""
    def shouldSave(self, isSaving: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def thisMObject(self) -> MObject:
        """Returns the MObject associated with this user defined node."""
    def transformInvalidationRange(self, source: MPlug, input: MTimeRange) -> MTimeRange:
        """Introduced in 2020.0"""
    @overload
    def type(self) -> int: ...
    @overload
    def type(self) -> int:
        """This method returns the type of the node."""
    def typeId(self) -> MTypeId:
        """Returns the TYPEID of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""

class MPxCacheConfigRuleFilter:
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def isMatch(self, evalNode: MEvaluationNode) -> bool:
        """Will be called for each evaluation node when filter/action rules are applied for the cache configuration."""
    def postRulesExecution(self) -> None:
        """Called when cache configuration rule application stops."""
    def preRulesExecution(self) -> None:
        """Called when cache configuration rule application starts."""

class MPxCacheFormat:
    kRead: Any
    kReadWrite: Any
    kWrite: Any
    thisown: Any
    def __init__(self) -> None:
        """The default class constructor."""
    def beginReadChunk(self) -> MStatus:
        """Start the read process for this chunk."""
    def beginWriteChunk(self) -> None:
        """Perform any actions required prior to writing a chunk's information."""
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def close(self) -> None:
        """Close the current current cache file."""
    def endReadChunk(self) -> None:
        """End the read process for this chunk."""
    def endWriteChunk(self) -> None:
        """Perform any actions required after writing a chunk's information."""
    def extension(self) -> str:
        """Returns the extension used by this format."""
    def findChannelName(self, name: str) -> MStatus:
        """Seek to a specific channel in the cache."""
    def findTime(self, time: MTime, foundTime: MTime) -> MStatus:
        """Find a specific time in the cache."""
    def handlesDescription(self) -> bool:
        """Report whether this format handles the format description itself (usually provided by the default xml description file)."""
    def isValid(self) -> MStatus:
        """Confirm whether the current cache file is valid."""
    def open(self, fileName: str, mode: Any) -> MStatus:
        """Attempt to open the specified cache format."""
    def readArraySize(self) -> int:
        """Read the size of an array in the cache."""
    def readChannelName(self, name: str) -> MStatus:
        """Find the next channel name."""
    def readDescription(self, description: MCacheFormatDescription, descriptionFileLocation: str, baseFileName: str) -> MStatus:
        """Obtain the format description information."""
    def readDoubleArray(self, size: int) -> MStatus:
        """Read an array of doubles from the cache."""
    def readDoubleVectorArray(self, arraySize: int) -> MStatus:
        """Read an array of double-precision vectors from the cache."""
    def readFloatArray(self, size: int) -> MStatus:
        """Read an array of floats from the cache."""
    def readFloatVectorArray(self, array: MFloatVectorArray, arraySize: int) -> MStatus:
        """Read an array of single-precision vectors from the cache."""
    def readHeader(self) -> MStatus:
        """Read the header from the current cache file, and store any data that may be required."""
    def readInt32(self) -> int:
        """Read an integer from the cache."""
    def readIntArray(self, size: int) -> MStatus:
        """Read an array of ints from the cache."""
    def readNextTime(self, foundTime: MTime) -> MStatus:
        """Read the next time from the cache."""
    def readTime(self, time: MTime) -> MStatus:
        """Read the current time from the cache."""
    def rewind(self) -> MStatus:
        """Rewind the current cache pointer to the start of the cache."""
    def writeChannelName(self, name: str) -> MStatus:
        """Write a channel to the cache."""
    def writeDescription(self, description: MCacheFormatDescription, descriptionFileLocation: str, baseFileName: str) -> MStatus:
        """Store the format description information."""
    def writeDoubleArray(self) -> MStatus:
        """Write an array of doubles to the cache."""
    def writeDoubleVectorArray(self, array: MVectorArray) -> MStatus:
        """Write an array of double-precision vectors to the cache."""
    def writeFloatArray(self) -> MStatus:
        """Write a array of floats to the cache."""
    def writeFloatVectorArray(self, array: MFloatVectorArray) -> MStatus:
        """Write an array of single-precision vectors to the cache."""
    def writeHeader(self, version: str, startTime: MTime, endTime: MTime) -> MStatus:
        """Write the header for the current cache."""
    def writeInt32(self, arg: Any) -> MStatus:
        """Write an integer to the cache."""
    def writeIntArray(self) -> MStatus:
        """Write a array of int to the cache."""
    def writeTime(self, time: MTime) -> MStatus:
        """Write the current time to the cache."""

class MPxCameraSet:
    active: Any
    caching: Any
    camera: Any
    cameraLayer: Any
    frozen: Any
    isHistoricallyInteresting: Any
    kAssembly: Any
    kBlendShape: Any
    kCameraSetNode: Any
    kClientDeviceNode: Any
    kConstraintNode: Any
    kDefaultScheduling: Any
    kDeformerNode: Any
    kDependNode: Any
    kEmitterNode: Any
    kEvaluatedDirectly: Any
    kEvaluatedIndirectly: Any
    kFieldNode: Any
    kFluidEmitterNode: Any
    kGeometryFilter: Any
    kGloballySerial: Any
    kGloballySerialize: Any
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
    kParallel: Any
    kParticleAttributeMapperNode: Any
    kPostEvaluationTypeLast: Any
    kSchedulingTypeLast: Any
    kSerial: Any
    kSerialize: Any
    kSkinCluster: Any
    kSpringNode: Any
    kSurfaceShape: Any
    kThreadedDeviceNode: Any
    kTransformNode: Any
    kUntrusted: Any
    message: Any
    order: Any
    sceneData: Any
    state: Any
    thisown: Any
    def __init__(self) -> None:
        """Constructor."""
    @staticmethod
    def addAttribute(attr: MObject) -> MStatus:
        """This method adds a new attribute to a user defined node type during the type's initialization."""
    def addExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Adds content info to the specified table from a file path attribute."""
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> MStatus: ...
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject, affectsTopology: bool) -> MStatus:
        """This method specifies that a particular input attribute affects a specific output attribute."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def compute(self) -> MStatus:
        """This method should be overridden in user defined nodes."""
    def configCache(self) -> None:
        """Introduced in 2020.0"""
    def connectionBroken(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are made to attributes of this node."""
    def copyInternalData(self) -> None:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def dependsOn(self, depends: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    def getCacheSetup(self) -> None:
        """Introduced in 2020.0"""
    def getExternalContent(self, table: MExternalContentInfoTable) -> None:
        """Returns the external content (files) that this node depends on."""
    def getFilesToArchive(self, shortName: bool = False, unresolvedName: bool = False, markCouldBeImageSequence: bool = False) -> Any:
        """Use this method to return all external files used by this node."""
    def getInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def getInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def hasInvalidationRangeTransformation(self) -> bool:
        """Introduced in 2020.0"""
    @staticmethod
    def inheritAttributesFrom(parentClassName: str) -> MStatus:
        """This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node."""
    @overload
    def internalArrayCount(self) -> int: ...
    @overload
    def internalArrayCount(self) -> int:
        """This method is overridden by nodes that have internal array attributes which are not stored in Maya's datablock."""
    def isAbstractClass(self) -> bool:
        """Override this class to return true if this node is an abstract node."""
    def isPassiveOutput(self) -> bool:
        """This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent val"""
    def isTrackingTopology(self) -> bool:
        """Introduced in 2019.0"""
    def legalConnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal connections being made to attributes of this node."""
    def legalDisconnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal disconnections being made to attributes of this node."""
    def name(self) -> str:
        """Returns the name of this particular instance of this class."""
    def passThroughToMany(self) -> bool:
        """This method is overridden by nodes that want to control the traversal behavior of some Maya search algorithms which trav"""
    def passThroughToOne(self) -> MPlug:
        """This method may be overridden by nodes that have a one-to-one relationship between an input attribute and a correspondin"""
    def postConstructor(self) -> None:
        """Post constructor."""
    def postEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode, evalType: Any) -> MStatus:
        """Clean up node's internal state after threaded evaluation."""
    def preEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode) -> MStatus:
        """Prepare a node's internal state for threaded evaluation."""
    def schedulingType(self) -> Any:
        """When overridden this method controls the degree of parallelism supported by the node during threaded evaluation."""
    def setDependentsDirty(self, plug: MPlug, plugArray: MPlugArray) -> MStatus:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug """
    def setExistWithoutInConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without input connections."""
    def setExistWithoutOutConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without output connections."""
    def setExternalContent(self) -> None:
        """Changes the location of external content in batch."""
    def setExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Sets content info in the specified attribute from the table."""
    def setInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def shouldSave(self, isSaving: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def thisMObject(self) -> MObject:
        """Returns the MObject associated with this user defined node."""
    def transformInvalidationRange(self, source: MPlug, input: MTimeRange) -> MTimeRange:
        """Introduced in 2020.0"""
    def type(self) -> int:
        """Returns the type of node that this is."""
    def typeId(self) -> MTypeId:
        """Returns the TYPEID of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""

class MPxCommand:
    kDouble: Any
    kLong: Any
    kNoArg: Any
    kString: Any
    thisown: Any
    def __init__(self) -> None:
        """Constructor."""
    @overload
    @staticmethod
    def appendToResult(val: int) -> None: ...
    @overload
    @staticmethod
    def appendToResult(val: float) -> None: ...
    @overload
    @staticmethod
    def appendToResult(val: bool) -> None: ...
    @overload
    @staticmethod
    def appendToResult(val: str) -> None: ...
    @overload
    @staticmethod
    def appendToResult(val: str) -> None: ...
    @overload
    @staticmethod
    def appendToResult(val: Any) -> None:
        """This method will add the given value to the end of the result array of integers."""
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def clearResult() -> None:
        """Initializes the place where results from Maya commands get stored."""
    def commandString(self) -> str:
        """This method returns the command string that is associated with this command."""
    @staticmethod
    def currentDoubleResult() -> float:
        """This method gets the current node's result as a double, if possible."""
    @staticmethod
    def currentIntResult() -> int:
        """This method gets the current node's result as a int, if possible."""
    @staticmethod
    def currentResultType() -> Any:
        """This method will return the type of the current result for the command."""
    @staticmethod
    def currentStringResult() -> str:
        """This method gets the current node's result as a MString , if possible."""
    @staticmethod
    def displayError(theError: str, showLineNumber: bool = False) -> None:
        """This method is used to display an error in the script editor."""
    @staticmethod
    def displayInfo(theInfo: str) -> None:
        """This method is used to display information in the script editor."""
    @staticmethod
    def displayWarning(theWarning: str, showLineNumber: bool = False) -> None:
        """This method is used to display a warning in the script editor."""
    def doIt(self, args: MArgList) -> MStatus:
        """This method should perform a command by setting up internal class data and then calling the redoIt method."""
    @overload
    @staticmethod
    def getCurrentResult(val: int) -> MStatus: ...
    @overload
    @staticmethod
    def getCurrentResult(val: float) -> MStatus: ...
    @overload
    @staticmethod
    def getCurrentResult(val: str) -> MStatus: ...
    @overload
    @staticmethod
    def getCurrentResult(val: MIntArray) -> MStatus: ...
    @overload
    @staticmethod
    def getCurrentResult(val: MDoubleArray) -> MStatus: ...
    @overload
    @staticmethod
    def getCurrentResult(val: Any) -> MStatus:
        """Not available in Python."""
    def hasSyntax(self) -> bool:
        """This method specifies whether or not the command has a syntax object."""
    @staticmethod
    def isCurrentResultArray() -> bool:
        """This method will return whether the return result for the command is an array or not."""
    def isHistoryOn(self) -> bool:
        """Returns whether history is on."""
    def isUndoable(self) -> bool:
        """This method is used to specify whether or not the command is undoable."""
    def redoIt(self) -> MStatus:
        """This method should do the actual work of the command based on the internal class data only."""
    def setCommandString(self) -> MStatus:
        """Sets the command string that is associated with this command object."""
    def setHistoryOn(self, state: bool) -> MStatus:
        """This method specifies if history for this command is on."""
    @overload
    @staticmethod
    def setResult(val: int) -> None: ...
    @overload
    @staticmethod
    def setResult(val: int) -> None: ...
    @overload
    @staticmethod
    def setResult(val: float) -> None: ...
    @overload
    @staticmethod
    def setResult(val: bool) -> None: ...
    @overload
    @staticmethod
    def setResult(val: str) -> None: ...
    @overload
    @staticmethod
    def setResult(val: str) -> None: ...
    @overload
    @staticmethod
    def setResult(val: MIntArray) -> None: ...
    @overload
    @staticmethod
    def setResult(val: MDoubleArray) -> None: ...
    @overload
    @staticmethod
    def setResult(val: Any) -> None:
        """This method puts the given value into the return value area for a command."""
    def setUndoable(self, state: bool) -> MStatus:
        """Deprecated in 2019.0"""
    def syntax(self) -> Any:
        """This method is intended to be used in an MArgDataBase or MArgParser contructor when the plugin command's syntax is being"""
    def undoIt(self) -> MStatus:
        """This method should undo the work done by the redoIt method based on the internal class data only."""

class MPxComponentShape:
    boundingBoxCenterX: Any
    boundingBoxCenterY: Any
    boundingBoxCenterZ: Any
    caching: Any
    center: Any
    frozen: Any
    instObjGroups: Any
    intermediateObject: Any
    inverseMatrix: Any
    isHistoricallyInteresting: Any
    isTemplated: Any
    kAssembly: Any
    kBlendShape: Any
    kBoundingBoxChanged: Any
    kCameraSetNode: Any
    kClientDeviceNode: Any
    kConstraintNode: Any
    kDefaultScheduling: Any
    kDeformerNode: Any
    kDependNode: Any
    kEmitterNode: Any
    kEvaluatedDirectly: Any
    kEvaluatedIndirectly: Any
    kFieldNode: Any
    kFluidEmitterNode: Any
    kGeometryFilter: Any
    kGloballySerial: Any
    kGloballySerialize: Any
    kHardwareShader: Any
    kHwShaderNode: Any
    kIkSolverNode: Any
    kImagePlaneNode: Any
    kLast: Any
    kLeaveDirty: Any
    kLocatorNode: Any
    kManipContainer: Any
    kManipulatorNode: Any
    kMatchInvalidAttribute: Any
    kMatchInvalidAttributeDim: Any
    kMatchInvalidAttributeIndex: Any
    kMatchInvalidAttributeRange: Any
    kMatchInvalidName: Any
    kMatchNone: Any
    kMatchOk: Any
    kMatchTooMany: Any
    kMotionPathNode: Any
    kNoPointCaching: Any
    kNormal: Any
    kObjectChanged: Any
    kObjectSet: Any
    kParallel: Any
    kParticleAttributeMapperNode: Any
    kPostEvaluationTypeLast: Any
    kRestorePoints: Any
    kSavePoints: Any
    kSchedulingTypeLast: Any
    kSerial: Any
    kSerialize: Any
    kSkinCluster: Any
    kSpringNode: Any
    kSurfaceShape: Any
    kThreadedDeviceNode: Any
    kTransformNode: Any
    kTransformOriginalPoints: Any
    kUTangent: Any
    kUVNTriad: Any
    kUntrusted: Any
    kUpdatePoints: Any
    kVTangent: Any
    mControlPoints: Any
    mControlValueX: Any
    mControlValueY: Any
    mControlValueZ: Any
    mHasHistoryOnCreate: Any
    matrix: Any
    message: Any
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
    state: Any
    thisown: Any
    useObjectColor: Any
    visibility: Any
    worldInverseMatrix: Any
    worldMatrix: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @overload
    def acceptsGeometryIterator(self, writeable: bool = True) -> bool: ...
    @overload
    def acceptsGeometryIterator(self, writeable: bool = True, forReadOnly: bool = False) -> bool:
        """If the shape can supply a component iterator then then this method should be overridden to return true."""
    def activeComponents(self) -> MObjectArray:
        """Returns a list of active (selected) components for the shape."""
    @staticmethod
    def addAttribute(attr: MObject) -> MStatus:
        """This method adds a new attribute to a user defined node type during the type's initialization."""
    def addExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Adds content info to the specified table from a file path attribute."""
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> MStatus: ...
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject, affectsTopology: bool) -> MStatus:
        """This method specifies that a particular input attribute affects a specific output attribute."""
    def boundingBox(self) -> MBoundingBox:
        """This method should be overridden to return a bounding box for the shape."""
    def cachedShapeAttr(self) -> MObject:
        """Returns the attribute containing the shape's cached geometry, if it has one."""
    def canMakeLive(self) -> bool:
        """This method is used by Maya to determine whether a surface can be made live."""
    def childChanged(self, MChildChanged: Any) -> None:
        """This method can be used to trigger the shape to recalculate its bounding box."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @overload
    def closestPoint(self, raySource: MPoint, rayDirection: MVector, theClosestPoint: MPoint, theClosestNormal: MVector, findClosestOnMiss: bool, tolerance: float) -> bool: ...
    @overload
    def closestPoint(self, toThisPoint: MPoint, theClosestPoint: MPoint, tolerance: float) -> None:
        """This method is used by Maya for snapping queries when your surface is live."""
    def componentToPlugs(self, component: MObject, list: MSelectionList) -> None:
        """Converts the given component into a selection list of plugs."""
    def compute(self) -> MStatus:
        """This method should be overridden in user defined nodes."""
    def configCache(self) -> None:
        """Introduced in 2020.0"""
    def connectionBroken(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are made to attributes of this node."""
    def convertToTweakNodePlug(self, plug: MPlug) -> bool:
        """Check if a tweak node is connected to this node."""
    def copyInternalData(self) -> None:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def createFullRenderGroup(self) -> MObject:
        """This method is used to create a component containing every renderable element in the object."""
    def createFullVertexGroup(self) -> MObject:
        """This method is used to create a component containing every vertex/CV in the object."""
    def deleteComponents(self, componentList: MObjectArray, undoInfo: MDoubleArray) -> bool:
        """This method should be overridden if the shape is to support deletion of components."""
    def dependsOn(self, depends: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def evalNodeAffectsDrawDb(self, evaluationNode: MEvaluationNode) -> bool:
        """This method should be overridden to return true if the evaluationNode contains any dirty plugs that will affect the draw"""
    def excludeAsPluginShape(self) -> bool:
        """A Maya viewport can be set to not display "Plugin Shapes", which means shapes derived from MPxSurfaceShape ."""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    def geometryData(self) -> MObject:
        """Returns the geometry data of the shape."""
    def geometryIteratorSetup(self, forReadOnly: bool = False) -> MPxGeometryIterator:
        """This method should be overridden by the user to return a geometry iterator compatible with the user's geometry."""
    def getCacheSetup(self) -> None:
        """Introduced in 2020.0"""
    def getComponentSelectionMask(self) -> MSelectionMask:
        """This routine must be overridden if the shape is to support interactive component selection in Viewport 2.0 and should pr"""
    def getControlPoints(self) -> MVectorArray:
        """Extract the control points from the data block and store them locally."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> None:
        """Returns the external content (files) that this node depends on."""
    def getFilesToArchive(self, shortName: bool = False, unresolvedName: bool = False, markCouldBeImageSequence: bool = False) -> Any:
        """Use this method to return all external files used by this node."""
    def getInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def getInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def getShapeSelectionMask(self) -> MSelectionMask:
        """This routine must be overridden if the shape is to support interactive object selection in Viewport 2.0 and should provi"""
    def getWorldMatrix(self, arg: int) -> MMatrix:
        """Returns MMatrix which takes a point from local object space to world space."""
    def hasActiveComponents(self) -> bool:
        """This method is used to determine whether or not the shape has active (selected) components."""
    def hasInvalidationRangeTransformation(self) -> bool:
        """Introduced in 2020.0"""
    @staticmethod
    def inheritAttributesFrom(parentClassName: str) -> MStatus:
        """This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node."""
    @overload
    def internalArrayCount(self) -> int: ...
    @overload
    def internalArrayCount(self) -> int:
        """This method is overridden by nodes that have internal array attributes which are not stored in Maya's datablock."""
    def isAbstractClass(self) -> bool:
        """Override this class to return true if this node is an abstract node."""
    def isBounded(self) -> bool:
        """This method should be overridden to return true if the user supplies a bounding box routine."""
    def isPassiveOutput(self) -> bool:
        """This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent val"""
    def isRenderable(self) -> bool:
        """Returns true if the shape is a renderable shape."""
    def isTrackingTopology(self) -> bool:
        """Introduced in 2019.0"""
    def legalConnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal connections being made to attributes of this node."""
    def legalDisconnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal disconnections being made to attributes of this node."""
    def localShapeInAttr(self) -> MObject:
        """Returns the input attribute of the shape, which are the control points."""
    def localShapeOutAttr(self) -> MObject:
        """Returns the attribute containing the shape's output geometry in local space."""
    def match(self, mask: MSelectionMask, componentList: MObjectArray) -> bool:
        """This method is used to check for matches between a selection type (or mask) and a given component."""
    def matchComponent(self, item: MSelectionList, spec: MAttributeSpecArray, list: MSelectionList) -> Any:
        """This method is used to convert the string representation of a component into a component object and to validate that the"""
    def name(self) -> str:
        """Returns the name of this particular instance of this class."""
    def newControlPointComponent(self) -> MObject:
        """The default action of this method is to return an MFnSingleIndexedComponent (of type MFn::kMeshVertComponent ) in order """
    def passThroughToMany(self) -> bool:
        """This method is overridden by nodes that want to control the traversal behavior of some Maya search algorithms which trav"""
    def passThroughToOne(self) -> MPlug:
        """This method may be overridden by nodes that have a one-to-one relationship between an input attribute and a correspondin"""
    def pointAtParm(self, atThisParm: MPoint, evaluatedPoint: MPoint) -> bool:
        """This method is used by Maya in functions (such as select) that require point at parameter values."""
    def postConstructor(self) -> None:
        """Post constructor."""
    def postEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode, evalType: Any) -> MStatus:
        """Clean up node's internal state after threaded evaluation."""
    def preEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode) -> MStatus:
        """Prepare a node's internal state for threaded evaluation."""
    def renderGroupComponentType(self) -> int:
        """This method is used to return the type of renderable components for this shape."""
    def schedulingType(self) -> Any:
        """When overridden this method controls the degree of parallelism supported by the node during threaded evaluation."""
    def setControlPoints(self, cps: MVectorArray) -> MStatus:
        """Push the given control points into the node's data block."""
    def setDependentsDirty(self, plug: MPlug, plugArray: MPlugArray) -> MStatus:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug """
    def setExistWithoutInConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without input connections."""
    def setExistWithoutOutConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without output connections."""
    def setExternalContent(self) -> None:
        """Changes the location of external content in batch."""
    def setExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Sets content info in the specified attribute from the table."""
    def setInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def setRenderable(self, arg: Any) -> None:
        """Specifies whether the shape is a renderable shape."""
    def shouldSave(self, isSaving: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def thisMObject(self) -> MObject:
        """Returns the MObject associated with this user defined node."""
    def transformInvalidationRange(self, source: MPlug, input: MTimeRange) -> MTimeRange:
        """Introduced in 2020.0"""
    @overload
    def transformUsing(self, matrix: MMatrix, componentList: MObjectArray) -> None: ...
    @overload
    def transformUsing(self, mat: MMatrix, componentList: MObjectArray, cachingMode: int, pointCache: MPointArray) -> None:
        """Transform the given components using the specified transformation matrix."""
    def tweakUsing(self, mat: MMatrix, componentList: MObjectArray, cachingMode: Any, pointCache: MPointArray, handle: MArrayDataHandle) -> None:
        """Transform the given components using the specified transformation matrix."""
    def type(self) -> int:
        """Returns the type of node that this is."""
    def typeId(self) -> MTypeId:
        """Returns the TYPEID of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""
    def undeleteComponents(self, componentList: MObjectArray, undoInfo: MDoubleArray) -> bool:
        """This method should be overridden if the shape is to support undeletion of components."""
    def vertexOffsetDirection(self, component: MObject, direction: MVectorArray, mode: Any, normalize: bool) -> bool:
        """This method should be overridden if the shape supports components that can be moved in the direction of the normal or UV"""
    def weightedTransformUsing(self, xform: MTransformationMatrix, space: MMatrix, componentList: MObjectArray, cachingMode: Any, pointCache: MPointArray, freezePlane: MPlane) -> None:
        """Transform the given components with interpolation using the specified transformation matrix."""
    def weightedTweakUsing(self, xform: MTransformationMatrix, space: MMatrix, componentList: MObjectArray, cachingMode: Any, pointCache: MPointArray, freezePlane: MPlane, handle: MArrayDataHandle) -> None:
        """Transform the given components with interpolation using the specified transformation matrix."""
    def worldShapeOutAttr(self) -> MObject:
        """Returns the attribute containing the shape's output geometry in world space."""

class MPxConstraint:
    caching: Any
    enableRestPosition: Any
    frozen: Any
    isHistoricallyInteresting: Any
    kAssembly: Any
    kBlendShape: Any
    kCameraSetNode: Any
    kClientDeviceNode: Any
    kConstraintNode: Any
    kDefaultScheduling: Any
    kDeformerNode: Any
    kDependNode: Any
    kEmitterNode: Any
    kEvaluatedDirectly: Any
    kEvaluatedIndirectly: Any
    kFieldNode: Any
    kFluidEmitterNode: Any
    kGeometryFilter: Any
    kGloballySerial: Any
    kGloballySerialize: Any
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
    kObject: Any
    kObjectRotation: Any
    kObjectSet: Any
    kParallel: Any
    kParticleAttributeMapperNode: Any
    kPostEvaluationTypeLast: Any
    kScene: Any
    kSchedulingTypeLast: Any
    kSerial: Any
    kSerialize: Any
    kSkinCluster: Any
    kSpringNode: Any
    kSurfaceShape: Any
    kThreadedDeviceNode: Any
    kTransformNode: Any
    kUntrusted: Any
    kVector: Any
    lockOutput: Any
    message: Any
    state: Any
    thisown: Any
    def __init__(self) -> None:
        """Constructor."""
    @staticmethod
    def addAttribute(attr: MObject) -> MStatus:
        """This method adds a new attribute to a user defined node type during the type's initialization."""
    def addExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Adds content info to the specified table from a file path attribute."""
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> MStatus: ...
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject, affectsTopology: bool) -> MStatus:
        """This method specifies that a particular input attribute affects a specific output attribute."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def compute(self) -> MStatus:
        """This method should be overridden in user defined nodes."""
    def configCache(self) -> None:
        """Introduced in 2020.0"""
    def connectionBroken(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are made to attributes of this node."""
    def constraintRotateOrderAttribute(self) -> MObject:
        """Returns the rotate order attribute for the constraint."""
    def copyInternalData(self) -> None:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def dependsOn(self, depends: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    def getCacheSetup(self) -> None:
        """Introduced in 2020.0"""
    def getExternalContent(self, table: MExternalContentInfoTable) -> None:
        """Returns the external content (files) that this node depends on."""
    def getFilesToArchive(self, shortName: bool = False, unresolvedName: bool = False, markCouldBeImageSequence: bool = False) -> Any:
        """Use this method to return all external files used by this node."""
    def getInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def getInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def getOutputAttributes(self, attributeArray: MObjectArray) -> None:
        """Returns output attributes for the constraint."""
    def hasInvalidationRangeTransformation(self) -> bool:
        """Introduced in 2020.0"""
    @staticmethod
    def inheritAttributesFrom(parentClassName: str) -> MStatus:
        """This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node."""
    @overload
    def internalArrayCount(self) -> int: ...
    @overload
    def internalArrayCount(self) -> int:
        """This method is overridden by nodes that have internal array attributes which are not stored in Maya's datablock."""
    def isAbstractClass(self) -> bool:
        """Override this class to return true if this node is an abstract node."""
    def isPassiveOutput(self) -> bool:
        """This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent val"""
    def isTrackingTopology(self) -> bool:
        """Introduced in 2019.0"""
    def legalConnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal connections being made to attributes of this node."""
    def legalDisconnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal disconnections being made to attributes of this node."""
    def name(self) -> str:
        """Returns the name of this particular instance of this class."""
    def passThroughToMany(self) -> bool:
        """This method is overridden by nodes that want to control the traversal behavior of some Maya search algorithms which trav"""
    def passThroughToOne(self) -> MPlug:
        """This method may be overridden by nodes that have a one-to-one relationship between an input attribute and a correspondin"""
    def passiveOutputAttribute(self) -> MObject:
        """Returns the passive output attribute for the constraint."""
    def postConstructor(self) -> None:
        """Post constructor."""
    def postEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode, evalType: Any) -> MStatus:
        """Clean up node's internal state after threaded evaluation."""
    def preEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode) -> MStatus:
        """Prepare a node's internal state for threaded evaluation."""
    def schedulingType(self) -> Any:
        """When overridden this method controls the degree of parallelism supported by the node during threaded evaluation."""
    def setDependentsDirty(self, plug: MPlug, plugArray: MPlugArray) -> MStatus:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug """
    def setExistWithoutInConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without input connections."""
    def setExistWithoutOutConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without output connections."""
    def setExternalContent(self) -> None:
        """Changes the location of external content in batch."""
    def setExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Sets content info in the specified attribute from the table."""
    def setInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def shouldSave(self, isSaving: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def targetAttribute(self) -> MObject:
        """Returns the target attribute for the constraint."""
    def thisMObject(self) -> MObject:
        """Returns the MObject associated with this user defined node."""
    def transformInvalidationRange(self, source: MPlug, input: MTimeRange) -> MTimeRange:
        """Introduced in 2020.0"""
    def type(self) -> Any:
        """Returns the type of node that this is."""
    def typeId(self) -> MTypeId:
        """Returns the TYPEID of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""
    def weightAttribute(self) -> MObject:
        """Returns the weight attribute for the constraint."""

class MPxConstraintCommand:
    kDouble: Any
    kGeometryShape: Any
    kLast: Any
    kLong: Any
    kNoArg: Any
    kString: Any
    kTransform: Any
    thisown: Any
    def __init__(self) -> None:
        """Constructor."""
    def aimVectorAttribute(self) -> MObject:
        """This method returns an attribute which defines the aim vector of a constraint."""
    def appendSyntax(self) -> MStatus:
        """This method should be overridden to append syntax to the constraint command."""
    @overload
    @staticmethod
    def appendToResult(val: int) -> None: ...
    @overload
    @staticmethod
    def appendToResult(val: float) -> None: ...
    @overload
    @staticmethod
    def appendToResult(val: bool) -> None: ...
    @overload
    @staticmethod
    def appendToResult(val: str) -> None: ...
    @overload
    @staticmethod
    def appendToResult(val: str) -> None: ...
    @overload
    @staticmethod
    def appendToResult(val: Any) -> None:
        """This method will add the given value to the end of the result array of integers."""
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def clearResult() -> None:
        """Initializes the place where results from Maya commands get stored."""
    def commandString(self) -> str:
        """This method returns the command string that is associated with this command."""
    def connectObjectAndConstraint(self, modifier: MDGModifier) -> MStatus:
        """This method is used for connecting the constraint and constrained object."""
    @overload
    def connectTarget(self, opaqueTarget: None, index: int) -> MStatus: ...
    @overload
    def connectTarget(self, targetPath: MDagPath, index: int) -> MStatus:
        """Deprecated in 2016.0"""
    def constraintEnableRestAttribute(self) -> MObject:
        """This method returns the attribute used to enable and disable the rest state at runtime."""
    def constraintInstancedAttribute(self) -> MObject:
        """This method returns the attribute on the constraint node that connects to an instanced constraint attribute of the const"""
    def constraintNode(self) -> MPxConstraint:
        """Returns the custom MPxConstraint-derived node created by this instance of the command."""
    def constraintOutputAttribute(self) -> MObject:
        """This method returns the attribute this constraint will connect to the constrained attribute of the constrained object."""
    def constraintRestAttribute(self) -> MObject:
        """This method returns the attribute used to store the constraint's rest state."""
    def constraintTargetAttribute(self) -> MObject:
        """This method returns the constraintTarget attribute for the constraint."""
    def constraintTargetInstancedAttribute(self) -> MObject:
        """This method returns the constraintTargetInstanced attribute for the constraint."""
    def constraintTargetWeightAttribute(self) -> MObject:
        """This method returns the constraintTargetWeight attribute for the constraint."""
    def constraintTypeId(self) -> MTypeId:
        """This method is used to return the MTypeId of the MPxConstraint node that is used with this command."""
    def createdConstraint(self, constraint: MPxConstraint) -> None:
        """This method is called when an MPxConstraintCommand creates a new MPxConstraint node."""
    @staticmethod
    def currentDoubleResult() -> float:
        """This method gets the current node's result as a double, if possible."""
    @staticmethod
    def currentIntResult() -> int:
        """This method gets the current node's result as a int, if possible."""
    @staticmethod
    def currentResultType() -> Any:
        """This method will return the type of the current result for the command."""
    @staticmethod
    def currentStringResult() -> str:
        """This method gets the current node's result as a MString , if possible."""
    @staticmethod
    def displayError(theError: str, showLineNumber: bool = False) -> None:
        """This method is used to display an error in the script editor."""
    @staticmethod
    def displayInfo(theInfo: str) -> None:
        """This method is used to display information in the script editor."""
    @staticmethod
    def displayWarning(theWarning: str, showLineNumber: bool = False) -> None:
        """This method is used to display a warning in the script editor."""
    def doCreate(self) -> MStatus:
        """This virtual method is called by the default behaviour of doIt() when the command is being executed in create mode."""
    def doEdit(self) -> MStatus:
        """This virtual method is called by the default behaviour of doIt() if the command was executed in create or edit mode (i.e"""
    def doIt(self, argList: MArgList) -> MStatus:
        """This virtual method is called when the command is intially executed (i.e."""
    def doQuery(self) -> MStatus:
        """This virtual method is called by the default behaviour of doIt() when the command is being executed in query mode."""
    @overload
    @staticmethod
    def getCurrentResult(val: int) -> MStatus: ...
    @overload
    @staticmethod
    def getCurrentResult(val: float) -> MStatus: ...
    @overload
    @staticmethod
    def getCurrentResult(val: str) -> MStatus: ...
    @overload
    @staticmethod
    def getCurrentResult(val: MIntArray) -> MStatus: ...
    @overload
    @staticmethod
    def getCurrentResult(val: MDoubleArray) -> MStatus: ...
    @overload
    @staticmethod
    def getCurrentResult(val: Any) -> MStatus:
        """Not available in Python."""
    def getObjectAttributesArray(self, array: MObjectArray) -> None:
        """This method returns the list of attributes this particular constraint considers when inserting a pair blend."""
    @overload
    def handleNewTargets(self, dagObject: MObject) -> None: ...
    @overload
    def handleNewTargets(self, dagObject: MDagPath) -> MStatus:
        """Deprecated in 2016.0"""
    def hasSyntax(self) -> bool:
        """This method specifies whether or not the command has a syntax object."""
    def hasVectorFlags(self) -> bool:
        """This method is used to control if the constraint supports the base class vector flags."""
    @staticmethod
    def isCurrentResultArray() -> bool:
        """This method will return whether the return result for the command is an array or not."""
    def isHistoryOn(self) -> bool:
        """Returns whether history is on."""
    def isUndoable(self) -> bool:
        """This method is used to specify whether or not the command is undoable."""
    def objectAttribute(self) -> MObject:
        """This method returns the attribute this constraint will drive on the constrained object."""
    def offsetAttribute(self) -> MObject:
        """This method returns the offset attribute and must be implemented if supportsOffset() returns true."""
    def parseArgs(self, argList: MArgList) -> MStatus:
        """This virtual method is called by the default behaviour of doIt() to parse the command's arguments."""
    def redoIt(self) -> MStatus:
        """This virtual method is called when the command is being redone."""
    def setCommandString(self) -> MStatus:
        """Sets the command string that is associated with this command object."""
    def setHistoryOn(self, state: bool) -> MStatus:
        """This method specifies if history for this command is on."""
    def setRestPosition(self, modifier: MDGModifier) -> MStatus:
        """Override this method if you want to control the value to which the constraint node's rest position attribute (i.e."""
    @overload
    @staticmethod
    def setResult(val: int) -> None: ...
    @overload
    @staticmethod
    def setResult(val: int) -> None: ...
    @overload
    @staticmethod
    def setResult(val: float) -> None: ...
    @overload
    @staticmethod
    def setResult(val: bool) -> None: ...
    @overload
    @staticmethod
    def setResult(val: str) -> None: ...
    @overload
    @staticmethod
    def setResult(val: str) -> None: ...
    @overload
    @staticmethod
    def setResult(val: MIntArray) -> None: ...
    @overload
    @staticmethod
    def setResult(val: MDoubleArray) -> None: ...
    @overload
    @staticmethod
    def setResult(val: Any) -> None:
        """This method puts the given value into the return value area for a command."""
    def setUndoable(self, state: bool) -> MStatus:
        """Deprecated in 2019.0"""
    def supportsOffset(self) -> bool:
        """This method is used to control if the constraint supports offset."""
    @overload
    def syntax(self) -> Any: ...
    @overload
    def syntax(self) -> Any:
        """This method is intended to be used in an MArgDataBase or MArgParser contructor when the plugin command's syntax is being"""
    def targetType(self) -> int:
        """Maya supports constraints targets which are either transforms or nodes derived from "geometryShape"."""
    def undoIt(self) -> MStatus:
        """This virtual method is called when the command is being undone."""
    def upVectorAttribute(self) -> MObject:
        """This method returns an upVector attribute that is used in conjunction with the aimVector."""
    def worldUpMatrixAttribute(self) -> MObject:
        """This method returns an worldUpMatrix attribute that is used in conjunction with the aimVector."""
    def worldUpTypeAttribute(self) -> MObject:
        """This method returns an worldUpType attribute that is used in conjunction with the aimVector."""
    def worldUpVectorAttribute(self) -> MObject:
        """This method returns an worldUpVector attribute that is used in conjunction with the aimVector."""

class MPxContext:
    kImage1: Any
    kImage2: Any
    kImage3: Any
    thisown: Any
    def __init__(self) -> None:
        """Class contstructor."""
    def abortAction(self) -> None:
        """This method is called when the abort key is pressed."""
    def addManipulator(self, manipulator: MObject) -> MStatus:
        """This method adds a manipulator to the context."""
    def argTypeNumericalInput(self, index: int) -> int:
        """This method is used by the feedback line to determine what units to display."""
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def completeAction(self) -> None:
        """This method is called when the complete key is pressed."""
    def deleteAction(self) -> None:
        """This method is called when the delete or backspace key is pressed."""
    def deleteManipulators(self) -> MStatus:
        """This method deletes all the manipulators that belong to the context."""
    @overload
    def doDrag(self, event: MEvent, drawMgr: int, context: int) -> MStatus: ...
    @overload
    def doDrag(self, event: MEvent) -> MStatus:
        """Not available in Python."""
    def doEnterRegion(self, event: MEvent) -> MStatus:
        """This method is called when the mouse pointer enters a screen panel region."""
    def doExitRegion(self, event: MEvent) -> MStatus:
        """Introduced in 2024.0"""
    @overload
    def doHold(self, event: MEvent, drawMgr: int, context: int) -> MStatus: ...
    @overload
    def doHold(self, event: MEvent) -> MStatus:
        """Not available in Python."""
    @overload
    def doPress(self, event: MEvent, drawMgr: int, context: int) -> MStatus: ...
    @overload
    def doPress(self, event: MEvent) -> MStatus:
        """Not available in Python."""
    @overload
    def doPtrMoved(self, event: MEvent, drawMgr: int, context: int) -> MStatus: ...
    @overload
    def doPtrMoved(self, event: MEvent) -> MStatus:
        """Not available in Python."""
    @overload
    def doRelease(self, event: MEvent, drawMgr: int, context: int) -> MStatus: ...
    @overload
    def doRelease(self, event: MEvent) -> MStatus:
        """Not available in Python."""
    def feedbackNumericalInput(self) -> bool:
        """This method is called to update the numerical feedback."""
    def helpStateHasChanged(self, event: MEvent) -> MStatus:
        """This method is called whenever the help state may need to be updated."""
    def image(self, index: Any) -> str:
        """This method is used to retrieve an XPM icon image that has previously been set for this tool context."""
    def inAlternateContext(self) -> bool:
        """Introduced in 2024.0"""
    def newToolCommand(self) -> MPxToolCommand:
        """CALL _newToolCommand() IN SCRIPT."""
    def processNumericalInput(self, values: MDoubleArray, flags: MIntArray, isAbsolute: bool) -> bool:
        """This method processes the input from the numerical input field."""
    def setImage(self, image: str, index: Any) -> MStatus:
        """This method is used to set an XPM icon image that is to be used to represent this tool context in various places includi"""
    def stringClassName(self) -> str:
        """This method is called to determine the name that uniquely identifies the context."""
    def toolOffCleanup(self) -> None:
        """This method is called when the context is deactivated, i.e when another context is activated."""
    def toolOnSetup(self, event: MEvent) -> None:
        """This method is called when the context is activated, i.e when the toolButton for the context is pressed."""

class MPxContextCommand:
    thisown: Any
    def __init__(self) -> None:
        """Class constructor."""
    def appendSyntax(self) -> MStatus:
        """This method should be overridden to append syntax to the context command."""
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def doEditFlags(self) -> MStatus:
        """This method is called when the command is called in edit mode."""
    def doQueryFlags(self) -> MStatus:
        """This method is called when the command is called in query mode."""
    def makeObj(self) -> MPxContext:
        """This function is used to instantiate a proxy context."""
    @overload
    def setResult(self, result: bool) -> MStatus: ...
    @overload
    def setResult(self, result: int) -> MStatus: ...
    @overload
    def setResult(self, result: float) -> MStatus: ...
    @overload
    def setResult(self, result: str) -> MStatus:
        """This method should be called when the result of the context command is a boolean."""

class MPxControlCommand:
    thisown: Any
    def __init__(self) -> None:
        """Class constructor."""
    def appendSyntax(self) -> MStatus:
        """This method should be overridden to append syntax to the control command."""
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def clearResult(self) -> None:
        """This method should be called to clear the result to be output by the command."""
    def doEditFlags(self) -> MStatus:
        """This method is called when the command is called in edit mode."""
    def doQueryFlags(self) -> MStatus:
        """This method is invoked during query mode, and the default method should be overridden in user-defined control commands t"""
    def makeControl(self) -> MPxUIControl:
        """This method is called when the UI control should be created."""
    @overload
    def setResult(self, result: bool) -> MStatus: ...
    @overload
    def setResult(self, result: int) -> MStatus: ...
    @overload
    def setResult(self, result: float) -> MStatus: ...
    @overload
    def setResult(self, result: str) -> MStatus: ...
    @overload
    def setResult(self, result: Any) -> MStatus: ...
    @overload
    def setResult(self, result: MIntArray) -> MStatus:
        """This method should be called when the result of the control command is a boolean."""
    def skipFlagForCreate(self, longFlag: str) -> bool:
        """Returns true if the passed long flag name should be skipped during the creation portion of the command."""

class MPxData:
    kData: Any
    kGeometryData: Any
    kLast: Any
    thisown: Any
    def __init__(self) -> None:
        """Class Constructor."""
    def copy(self, src: MPxData) -> None:
        """This method initializes an instance of an MPxData derived class from another existing instance."""
    def name(self) -> str:
        """Determines the type name of the Data object."""
    def readASCII(self, argList: MArgList, endOfTheLastParsedElement: int) -> MStatus:
        """Creates Data in Data Block as specified by input from ASCII file record."""
    def readBinary(self, in_: int, length: int) -> MStatus:
        """Creates Data in Data Block as specified by binary data from the given stream."""
    def typeId(self) -> MTypeId:
        """Determines the type id of the Data object."""
    def writeASCII(self, out: int) -> MStatus:
        """Encodes Data in accordance with the ASCII file format and outputs it to the given stream."""
    def writeBinary(self, out: int) -> MStatus:
        """Encodes Data in accordance with the binary file format and outputs it to the given stream."""

class MPxDeformerNode:
    caching: Any
    componentTagExpression: Any
    envelope: Any
    frozen: Any
    groupId: Any
    input: Any
    inputGeom: Any
    isHistoricallyInteresting: Any
    kAssembly: Any
    kBlendShape: Any
    kCameraSetNode: Any
    kClientDeviceNode: Any
    kConstraintNode: Any
    kDefaultScheduling: Any
    kDeformerNode: Any
    kDeformsAll: Any
    kDeformsColors: Any
    kDeformsUVs: Any
    kDependNode: Any
    kEmitterNode: Any
    kEvaluatedDirectly: Any
    kEvaluatedIndirectly: Any
    kFieldNode: Any
    kFluidEmitterNode: Any
    kGeometryFilter: Any
    kGloballySerial: Any
    kGloballySerialize: Any
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
    kParallel: Any
    kParticleAttributeMapperNode: Any
    kPostEvaluationTypeLast: Any
    kSchedulingTypeLast: Any
    kSerial: Any
    kSerialize: Any
    kSkinCluster: Any
    kSpringNode: Any
    kSurfaceShape: Any
    kThreadedDeviceNode: Any
    kTransformNode: Any
    kUntrusted: Any
    message: Any
    outputGeom: Any
    state: Any
    thisown: Any
    weightList: Any
    weights: Any
    def __init__(self) -> None:
        """Class constructor."""
    def accessoryAttribute(self) -> MObject:
        """This method returns an MObject for the attribute to which an accessory shape is connected."""
    def accessoryNodeSetup(self, cmd: MDagModifier) -> MStatus:
        """This method is called by the "deformer -type" command when your node is specified."""
    @staticmethod
    def addAttribute(attr: MObject) -> MStatus:
        """This method adds a new attribute to a user defined node type during the type's initialization."""
    def addExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Adds content info to the specified table from a file path attribute."""
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> MStatus: ...
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject, affectsTopology: bool) -> MStatus:
        """This method specifies that a particular input attribute affects a specific output attribute."""
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
    def compute(self) -> MStatus:
        """This method should be overridden in user defined nodes."""
    def configCache(self) -> None:
        """Introduced in 2020.0"""
    def connectionBroken(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are made to attributes of this node."""
    def copyInternalData(self) -> None:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def deform(self, block: MDataBlock, iter: MItGeometry, mat: MMatrix, multiIndex: int) -> MStatus:
        """This method performs the deformation algorithm."""
    def dependsOn(self, depends: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def envelopeWeights(self, mblock: MDataBlock, multiIndex: int, numWeights: int | None = None) -> float:
        """Introduced in 2024.0"""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    def getCacheSetup(self) -> None:
        """Introduced in 2020.0"""
    @overload
    def getDeformationDetails(self) -> int: ...
    @overload
    def getDeformationDetails(self) -> int:
        """Introduced in 2019.0"""
    def getExternalContent(self, table: MExternalContentInfoTable) -> None:
        """Returns the external content (files) that this node depends on."""
    def getFilesToArchive(self, shortName: bool = False, unresolvedName: bool = False, markCouldBeImageSequence: bool = False) -> Any:
        """Use this method to return all external files used by this node."""
    def getFixedSetupData(self, name: str) -> MObject:
        """Introduced in 2022.0"""
    def getGeometryIterator(self, iter: MItGeometry, block: MDataBlock, dataHandle: MDataHandle, multiIndex: int, readOnly: bool = True) -> int:
        """Introduced in 2022.0"""
    def getInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def getInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def hasInvalidationRangeTransformation(self) -> bool:
        """Introduced in 2020.0"""
    def indexMapper(self, multiIndex: int) -> Any:
        """Introduced in 2024.0"""
    @staticmethod
    def inheritAttributesFrom(parentClassName: str) -> MStatus:
        """This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node."""
    @overload
    def internalArrayCount(self) -> int: ...
    @overload
    def internalArrayCount(self) -> int:
        """This method is overridden by nodes that have internal array attributes which are not stored in Maya's datablock."""
    def isAbstractClass(self) -> bool:
        """Override this class to return true if this node is an abstract node."""
    def isPassiveOutput(self) -> bool:
        """This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent val"""
    def isTrackingTopology(self) -> bool:
        """Introduced in 2019.0"""
    def legalConnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal connections being made to attributes of this node."""
    def legalDisconnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal disconnections being made to attributes of this node."""
    def name(self) -> str:
        """Returns the name of this particular instance of this class."""
    def passThroughToMany(self) -> bool:
        """This method is overridden by nodes that want to control the traversal behavior of some Maya search algorithms which trav"""
    def passThroughToOne(self) -> MPlug:
        """This method may be overridden by nodes that have a one-to-one relationship between an input attribute and a correspondin"""
    def postConstructor(self) -> None:
        """Post constructor."""
    def postEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode, evalType: Any) -> MStatus:
        """Clean up node's internal state after threaded evaluation."""
    def preEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode) -> MStatus:
        """Prepare a node's internal state for threaded evaluation."""
    def schedulingType(self) -> Any:
        """When overridden this method controls the degree of parallelism supported by the node during threaded evaluation."""
    @overload
    def setDeformationDetails(self, flags: int) -> MStatus: ...
    @overload
    def setDeformationDetails(self, flags: int) -> MStatus:
        """Introduced in 2019.0"""
    def setDependentsDirty(self, plug: MPlug, plugArray: MPlugArray) -> MStatus:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug """
    def setExistWithoutInConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without input connections."""
    def setExistWithoutOutConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without output connections."""
    def setExternalContent(self) -> None:
        """Changes the location of external content in batch."""
    def setExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Sets content info in the specified attribute from the table."""
    def setInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def setModifiedCallback(self, list: MSelectionList, listAdded: bool) -> None:
        """This callback method can be overriden and is called whenever the set this deformer is operating on is modified."""
    @overload
    def setUseExistingConnectionWhenSetEditing(self, state: bool) -> None: ...
    @overload
    def setUseExistingConnectionWhenSetEditing(self, state: bool) -> None:
        """Introduced in 2019.0"""
    def shouldSave(self, isSaving: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def thisMObject(self) -> MObject:
        """Returns the MObject associated with this user defined node."""
    def transformInvalidationRange(self, source: MPlug, input: MTimeRange) -> MTimeRange:
        """Introduced in 2020.0"""
    @overload
    def type(self) -> int: ...
    @overload
    def type(self) -> int:
        """This method returns the type of the node."""
    def typeId(self) -> MTypeId:
        """Returns the TYPEID of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""
    def weightValue(self, mblock: MDataBlock, multiIndex: int, wtIndex: int) -> float:
        """This method returns the weightValue stored in the datablock for the given geometry's lattice point/CV/vertex."""

class MPxDragAndDropBehavior:
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, init: None) -> None:
        """Class constructor."""
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def connectAttrToAttr(self, sourcePlug: MPlug, destinationPlug: MPlug, force: bool) -> MStatus:
        """This method is called by the defaultNavigation command to connect a source attribute to a destination attribute."""
    def connectAttrToNode(self, sourcePlug: MPlug, destinationNode: MObject, force: bool) -> MStatus:
        """This method is called by the defaultNavigation command to connect a source attribute to a destination node.You should ov"""
    def connectNodeToAttr(self, sourceNode: MObject, destinationPlug: MPlug, force: bool) -> MStatus:
        """This method is called by the defaultNavigation command to connect a source node to a destination attribute."""
    def connectNodeToNode(self, sourceNode: MObject, destinationNode: MObject, force: bool) -> MStatus:
        """This method is called by the defaultNavigation command to connect a source node to a destination node.You should overrid"""
    def shouldBeUsedFor(self, sourceNode: MObject, destinationNode: MObject, sourcePlug: MPlug, destinationPlug: MPlug) -> bool:
        """This method must be overridden in order to use a drag and drop behavior."""

class MPxEditData:
    thisown: Any
    def __init__(self) -> None:
        """Class constructor."""
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def isEqual(self, other: MPxEditData) -> bool:
        """Compares two MPxEditData objects for equality."""
    def isLessThan(self, other: MPxEditData) -> bool:
        """Compares two MPxEditData objects to determine their relative order for sorting purposes."""
    def performIsEqual(self, other: MPxEditData) -> bool:
        """This member function must be implemented by derived classes."""
    def performIsLessThan(self, other: MPxEditData) -> bool:
        """This member function must be implemented by derived classes."""

class MPxEmitterNode:
    caching: Any
    frozen: Any
    isHistoricallyInteresting: Any
    kAssembly: Any
    kBlendShape: Any
    kCameraSetNode: Any
    kClientDeviceNode: Any
    kConstraintNode: Any
    kCurve: Any
    kDefaultScheduling: Any
    kDeformerNode: Any
    kDependNode: Any
    kDirectional: Any
    kEmitterNode: Any
    kEvaluatedDirectly: Any
    kEvaluatedIndirectly: Any
    kFieldNode: Any
    kFluidEmitterNode: Any
    kGeometryFilter: Any
    kGloballySerial: Any
    kGloballySerialize: Any
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
    kOmni: Any
    kParallel: Any
    kParticleAttributeMapperNode: Any
    kPostEvaluationTypeLast: Any
    kSchedulingTypeLast: Any
    kSerial: Any
    kSerialize: Any
    kSkinCluster: Any
    kSpringNode: Any
    kSurface: Any
    kSurfaceShape: Any
    kThreadedDeviceNode: Any
    kTransformNode: Any
    kUntrusted: Any
    kVolume: Any
    mCurrentTime: Any
    mDeltaTime: Any
    mDirection: Any
    mDirectionX: Any
    mDirectionY: Any
    mDirectionZ: Any
    mEmitterType: Any
    mInheritFactor: Any
    mIsFull: Any
    mMaxDistance: Any
    mMinDistance: Any
    mOutput: Any
    mOwnerCentroid: Any
    mOwnerCentroidX: Any
    mOwnerCentroidY: Any
    mOwnerCentroidZ: Any
    mOwnerPosData: Any
    mOwnerVelData: Any
    mRandState: Any
    mRandStateX: Any
    mRandStateY: Any
    mRandStateZ: Any
    mRate: Any
    mSeed: Any
    mSpeed: Any
    mStartTime: Any
    mSweptGeometry: Any
    mWorldMatrix: Any
    message: Any
    state: Any
    thisown: Any
    def __init__(self) -> None:
        """Class constructor."""
    @staticmethod
    def addAttribute(attr: MObject) -> MStatus:
        """This method adds a new attribute to a user defined node type during the type's initialization."""
    def addExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Adds content info to the specified table from a file path attribute."""
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> MStatus: ...
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject, affectsTopology: bool) -> MStatus:
        """This method specifies that a particular input attribute affects a specific output attribute."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def compute(self, plug: MPlug, dataBlock: MDataBlock) -> MStatus:
        """This method should be overridden in user defined nodes."""
    def configCache(self) -> None:
        """Introduced in 2020.0"""
    def connectionBroken(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are made to attributes of this node."""
    def copyInternalData(self) -> None:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def dependsOn(self, depends: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def draw(self, view: M3dView, path: MDagPath, style: int, DisplayStatus: int) -> None:
        """Overriding this method allows the drawing of custom geometry using standard OpenGL calls."""
    def evalEmission2dTexture(self, texAttr: MObject, uCoords: MDoubleArray, vCoords: MDoubleArray, resultColors: MVectorArray, resultAlphas: MDoubleArray) -> MStatus:
        """If a supported 2d texture (see hasValidEmission2dTexture() method documentation) is connected to the given emitter attri"""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    def getCacheSetup(self) -> None:
        """Introduced in 2020.0"""
    def getCurrentTime(self, block: MDataBlock) -> MTime:
        """Intended to be called from within the emitter's compute() method, this method returns the time at which the emitter is c"""
    def getDeltaTime(self, plugIndex: int, block: MDataBlock) -> MTime:
        """Intended to be called from within the emitter's compute() method, this method returns the width of the time interval rep"""
    def getEmitterType(self, block: MDataBlock) -> Any:
        """Retrieves the type of the emitter, determined by the "emitterType" attribute value."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> None:
        """Returns the external content (files) that this node depends on."""
    def getFilesToArchive(self, shortName: bool = False, unresolvedName: bool = False, markCouldBeImageSequence: bool = False) -> Any:
        """Use this method to return all external files used by this node."""
    def getInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def getInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def getMaxDistance(self, block: MDataBlock) -> float:
        """Intended to be called from within the emitter's compute() method, this method retrieves the "maxDistance" attribute valu"""
    def getMinDistance(self, block: MDataBlock) -> float:
        """Intended to be called from within the emitter's compute() method, this method retrieves the "minDistance" attribute valu"""
    def getOwnerShape(self) -> MObject:
        """If the emitter is a emitting from an object, this method returns the shape node for the object."""
    def getRandomSeed(self, plugIndex: int, block: MDataBlock) -> int:
        """Intended to be called from within the emitter's compute() method, this method returns the random seed for a specified em"""
    def getRandomState(self, plugIndex: int, block: MDataBlock) -> None:
        """Intended to be called from within the emitter's compute() method, this method copies the emitter node attribute represen"""
    def getRate(self, block: MDataBlock) -> float:
        """Intended to be called from within the emitter's compute() method, this method retrieves the "rate" attribute value commo"""
    def getStartTime(self, plugIndex: int, block: MDataBlock) -> MTime:
        """Intended to be called from within the emitter's compute() method, this method returns the start times for each particle """
    def getWorldMatrix(self) -> MMatrix:
        """Returns the matrix that maps from the emitter's local space coordinates to worldspace."""
    def getWorldPosition(self) -> MPoint:
        """Returns the worldspace coordinates of the emitter."""
    def hasInvalidationRangeTransformation(self) -> bool:
        """Introduced in 2020.0"""
    def hasValidEmission2dTexture(self, texAttr: MObject) -> bool:
        """Certain aspects of Maya's particle and fluid emitters can be textured using 2d textures."""
    @staticmethod
    def inheritAttributesFrom(parentClassName: str) -> MStatus:
        """This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node."""
    @overload
    def internalArrayCount(self) -> int: ...
    @overload
    def internalArrayCount(self) -> int:
        """This method is overridden by nodes that have internal array attributes which are not stored in Maya's datablock."""
    def isAbstractClass(self) -> bool:
        """Override this class to return true if this node is an abstract node."""
    def isPassiveOutput(self) -> bool:
        """This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent val"""
    def isTrackingTopology(self) -> bool:
        """Introduced in 2019.0"""
    def legalConnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal connections being made to attributes of this node."""
    def legalDisconnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal disconnections being made to attributes of this node."""
    def name(self) -> str:
        """Returns the name of this particular instance of this class."""
    def passThroughToMany(self) -> bool:
        """This method is overridden by nodes that want to control the traversal behavior of some Maya search algorithms which trav"""
    def passThroughToOne(self) -> MPlug:
        """This method may be overridden by nodes that have a one-to-one relationship between an input attribute and a correspondin"""
    def postConstructor(self) -> None:
        """Post constructor."""
    def postEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode, evalType: Any) -> MStatus:
        """Clean up node's internal state after threaded evaluation."""
    def preEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode) -> MStatus:
        """Prepare a node's internal state for threaded evaluation."""
    def randgen(self) -> float:
        """Intended to be called from within the emitter's compute() method, this method generates a double-precision random number"""
    def resetRandomState(self, plugIndex: int, block: MDataBlock) -> None:
        """Intended to be called from within the emitter's compute() method, this method resets the emitter's random state data mem"""
    def schedulingType(self) -> Any:
        """When overridden this method controls the degree of parallelism supported by the node during threaded evaluation."""
    def setDependentsDirty(self, plug: MPlug, plugArray: MPlugArray) -> MStatus:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug """
    def setExistWithoutInConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without input connections."""
    def setExistWithoutOutConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without output connections."""
    def setExternalContent(self) -> None:
        """Changes the location of external content in batch."""
    def setExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Sets content info in the specified attribute from the table."""
    def setInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def setRandomState(self, plugIndex: int, block: MDataBlock) -> None:
        """Intended to be called from within the emitter's compute() method, this method copies the emitter node class random state"""
    def shouldSave(self, isSaving: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def thisMObject(self) -> MObject:
        """Returns the MObject associated with this user defined node."""
    def transformInvalidationRange(self, source: MPlug, input: MTimeRange) -> MTimeRange:
        """Introduced in 2020.0"""
    def type(self) -> int:
        """This method returns the type of the node."""
    def typeId(self) -> MTypeId:
        """Returns the TYPEID of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""
    def volumePrimitiveBoundingBox(self, box: MBoundingBox) -> bool:
        """For volume emitters, this method returns the object-space bounding box of the volume primitive associated with the emitt"""
    def volumePrimitiveDistanceFromAxis(self, worldPoint: MPoint, emitterWorldMatrix: MMatrix) -> float:
        """For volume emitters, this method determines the distance from a particular point to the major axis of the volumetric pri"""
    def volumePrimitivePointInside(self, worldPoint: MPoint, emitterWorldMatrix: MMatrix) -> bool:
        """For volume emitters, this method determines whether a particular point in space lies within the volume defined by the em"""

class MPxFieldNode:
    caching: Any
    frozen: Any
    isHistoricallyInteresting: Any
    kAssembly: Any
    kBlendShape: Any
    kCameraSetNode: Any
    kClientDeviceNode: Any
    kConstraintNode: Any
    kDefaultScheduling: Any
    kDeformerNode: Any
    kDependNode: Any
    kEmitterNode: Any
    kEvaluatedDirectly: Any
    kEvaluatedIndirectly: Any
    kFieldNode: Any
    kFluidEmitterNode: Any
    kGeometryFilter: Any
    kGloballySerial: Any
    kGloballySerialize: Any
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
    kParallel: Any
    kParticleAttributeMapperNode: Any
    kPostEvaluationTypeLast: Any
    kSchedulingTypeLast: Any
    kSerial: Any
    kSerialize: Any
    kSkinCluster: Any
    kSpringNode: Any
    kSurfaceShape: Any
    kThreadedDeviceNode: Any
    kTransformNode: Any
    kUntrusted: Any
    mApplyPerVertex: Any
    mAttenuation: Any
    mDeltaTime: Any
    mInputData: Any
    mInputForce: Any
    mInputMass: Any
    mInputPPData: Any
    mInputPositions: Any
    mInputVelocities: Any
    mMagnitude: Any
    mMaxDistance: Any
    mOutputForce: Any
    mOwnerCentroid: Any
    mOwnerCentroidX: Any
    mOwnerCentroidY: Any
    mOwnerCentroidZ: Any
    mOwnerPPData: Any
    mOwnerPosData: Any
    mOwnerVelData: Any
    mUseMaxDistance: Any
    mWorldMatrix: Any
    message: Any
    state: Any
    thisown: Any
    def __init__(self) -> None:
        """Class constructor."""
    @staticmethod
    def addAttribute(attr: MObject) -> MStatus:
        """This method adds a new attribute to a user defined node type during the type's initialization."""
    def addExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Adds content info to the specified table from a file path attribute."""
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> MStatus: ...
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject, affectsTopology: bool) -> MStatus:
        """This method specifies that a particular input attribute affects a specific output attribute."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def compute(self, plug: MPlug, dataBlock: MDataBlock) -> MStatus:
        """This method should be overridden in user defined nodes."""
    def configCache(self) -> None:
        """Introduced in 2020.0"""
    def connectionBroken(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are made to attributes of this node."""
    def copyInternalData(self) -> None:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def dependsOn(self, depends: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def draw(self, view: M3dView, path: MDagPath, style: int, DisplayStatus: int) -> None:
        """Overriding this method allows the drawing of custom geometry using standard OpenGL calls."""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    def falloffCurve(self, param: float) -> float:
        """Returns the falloff at the given parameter value."""
    def getCacheSetup(self) -> None:
        """Introduced in 2020.0"""
    def getExternalContent(self, table: MExternalContentInfoTable) -> None:
        """Returns the external content (files) that this node depends on."""
    def getFilesToArchive(self, shortName: bool = False, unresolvedName: bool = False, markCouldBeImageSequence: bool = False) -> Any:
        """Use this method to return all external files used by this node."""
    def getForceAtPoint(self, point: MVectorArray, velocity: MVectorArray, mass: MDoubleArray, force: MVectorArray, deltaTime: float) -> MStatus:
        """This method is not required to be overridden, it is only necessary for compatibility with the MFnField function set."""
    def getInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def getInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def hasInvalidationRangeTransformation(self) -> bool:
        """Introduced in 2020.0"""
    def iconBitmap(self, bitmap: Any) -> MStatus:
        """Define the bitmap for the field's icon."""
    def iconSizeAndOrigin(self, width: Any, height: Any, xbo: Any, ybo: Any) -> MStatus:
        """Define the size and the origin of the field's icon."""
    @staticmethod
    def inheritAttributesFrom(parentClassName: str) -> MStatus:
        """This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node."""
    @overload
    def internalArrayCount(self) -> int: ...
    @overload
    def internalArrayCount(self) -> int:
        """This method is overridden by nodes that have internal array attributes which are not stored in Maya's datablock."""
    def isAbstractClass(self) -> bool:
        """Override this class to return true if this node is an abstract node."""
    def isFalloffCurveConstantOne(self) -> bool:
        """Returns true if the falloffCurve is a constant one (default) or false if not."""
    def isPassiveOutput(self) -> bool:
        """This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent val"""
    def isTrackingTopology(self) -> bool:
        """Introduced in 2019.0"""
    def legalConnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal connections being made to attributes of this node."""
    def legalDisconnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal disconnections being made to attributes of this node."""
    def name(self) -> str:
        """Returns the name of this particular instance of this class."""
    def passThroughToMany(self) -> bool:
        """This method is overridden by nodes that want to control the traversal behavior of some Maya search algorithms which trav"""
    def passThroughToOne(self) -> MPlug:
        """This method may be overridden by nodes that have a one-to-one relationship between an input attribute and a correspondin"""
    def postConstructor(self) -> None:
        """Post constructor."""
    def postEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode, evalType: Any) -> MStatus:
        """Clean up node's internal state after threaded evaluation."""
    def preEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode) -> MStatus:
        """Prepare a node's internal state for threaded evaluation."""
    def schedulingType(self) -> Any:
        """When overridden this method controls the degree of parallelism supported by the node during threaded evaluation."""
    def setDependentsDirty(self, plug: MPlug, plugArray: MPlugArray) -> MStatus:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug """
    def setExistWithoutInConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without input connections."""
    def setExistWithoutOutConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without output connections."""
    def setExternalContent(self) -> None:
        """Changes the location of external content in batch."""
    def setExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Sets content info in the specified attribute from the table."""
    def setInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def shouldSave(self, isSaving: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def thisMObject(self) -> MObject:
        """Returns the MObject associated with this user defined node."""
    def transformInvalidationRange(self, source: MPlug, input: MTimeRange) -> MTimeRange:
        """Introduced in 2020.0"""
    def type(self) -> int:
        """This method returns the type of the node."""
    def typeId(self) -> MTypeId:
        """Returns the TYPEID of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""

class MPxFileResolver:
    kInput: Any
    kNone: Any
    thisown: Any
    def __init__(self) -> None:
        """The class constructor."""
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def findURIResolverByName(resolverName: str) -> MPxFileResolver:
        """Find a registered file resolver by name."""
    @staticmethod
    def findURIResolverByScheme(uriScheme: str) -> MPxFileResolver:
        """Find a registered file resolver that implements a given URI scheme."""
    @staticmethod
    def getURIResolversByName() -> Any:
        """Generate a list containing the names of all registered file resolvers."""
    @staticmethod
    def getURIResolversByScheme() -> Any:
        """Generate a list containing the URI schemes for all registered file resolvers."""
    @staticmethod
    def numURIResolvers() -> int:
        """Determine the number of registered URI file resolvers."""
    def performAfterSaveURI(self, uriValue: MURI, resolvedFullPath: str) -> None:
        """This optional handler is provided so that registered URI file resolvers can do custom processing after file save."""
    def resolveURI(self, uriValue: MURI, mode: int) -> str:
        """This routine is called by Maya to convert a URI value to a file path that can be accessed by Maya."""
    def resolveURIWithContext(self, uriValue: MURI, mode: int, contextNodeFullName: str) -> str:
        """This routine is called by Maya to convert a URI value to a file path that can be accessed by Maya."""
    def resolverName(self) -> str:
        """This routine is called to query the name of this resolver."""
    def uriScheme(self) -> str:
        """This routine is called to query the URI scheme that is handled by this resolver."""

class MPxFileTranslator:
    kCouldBeMyFileType: Any
    kExportAccessMode: Any
    kExportActiveAccessMode: Any
    kImportAccessMode: Any
    kIsMyFileType: Any
    kNotMyFileType: Any
    kOpenAccessMode: Any
    kReferenceAccessMode: Any
    kSaveAccessMode: Any
    kUnknownAccessMode: Any
    thisown: Any
    def __init__(self) -> None:
        """The class constructor."""
    def allowMultipleFileOptimization(self, *args: Any, **kwargs: Any) -> Any: ...
    def canBeOpened(self) -> bool:
        """This routine is called by Maya while it is executing in the MPxFileTranslator constructor."""
    def defaultExtension(self) -> str:
        """This routine is called by Maya whenever it needs to know the default extension of a translator."""
    @staticmethod
    def fileAccessMode() -> int:
        """This routine returns the fileAccess mode maya is currently in."""
    def filter(self) -> str:
        """This virtual method may be overloaded in a derived class to set the filter extension that will be used by the file dialo"""
    def haveNamespaceSupport(self) -> bool:
        """When a file is imported or referenced into an existing scene, there is the possibility that nodes in the incoming file w"""
    def haveReadMethod(self) -> bool:
        """This routine is called by Maya while it is executing in the MPxFileTranslator constructor."""
    def haveReferenceMethod(self) -> bool:
        """This method is called by Maya to see if the translator implements its own custom file referencing."""
    def haveWriteMethod(self) -> bool:
        """This routine is called by Maya while it is executing in the MPxFileTranslator constructor."""
    def identifyFile(self, file: MFileObject, buffer: str, size: Any) -> int:
        """This routine is called by Maya when a file selection dialog accesses a new directory."""
    def reader(self, file: MFileObject, optionsString: str, mode: Any) -> MStatus:
        """This routine is called by Maya when it is necessary to load a file of a type supported by this translator."""
    def writer(self, file: MFileObject, optionsString: str, mode: Any) -> MStatus:
        """This routine is called by Maya when it is necessary to save a file of a type supported by this translator."""

class MPxFluidEmitterNode:
    caching: Any
    frozen: Any
    isHistoricallyInteresting: Any
    kAssembly: Any
    kBlendShape: Any
    kCameraSetNode: Any
    kClientDeviceNode: Any
    kConstraintNode: Any
    kCurve: Any
    kDefaultScheduling: Any
    kDeformerNode: Any
    kDependNode: Any
    kDirectional: Any
    kEmitterNode: Any
    kEvaluatedDirectly: Any
    kEvaluatedIndirectly: Any
    kFieldNode: Any
    kFluidEmitterNode: Any
    kGeometryFilter: Any
    kGloballySerial: Any
    kGloballySerialize: Any
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
    kOmni: Any
    kParallel: Any
    kParticleAttributeMapperNode: Any
    kPostEvaluationTypeLast: Any
    kSchedulingTypeLast: Any
    kSerial: Any
    kSerialize: Any
    kSkinCluster: Any
    kSpringNode: Any
    kSurface: Any
    kSurfaceShape: Any
    kThreadedDeviceNode: Any
    kTransformNode: Any
    kUntrusted: Any
    kVolume: Any
    mCurrentTime: Any
    mDeltaTime: Any
    mDirection: Any
    mDirectionX: Any
    mDirectionY: Any
    mDirectionZ: Any
    mEmissionFunction: Any
    mEmitFluidColor: Any
    mEmitterType: Any
    mFluidColor: Any
    mFluidColorB: Any
    mFluidColorG: Any
    mFluidColorR: Any
    mFluidDensityEmission: Any
    mFluidDropoff: Any
    mFluidFuelEmission: Any
    mFluidHeatEmission: Any
    mFluidJitter: Any
    mInheritFactor: Any
    mIsFull: Any
    mMaxDistance: Any
    mMinDistance: Any
    mOutput: Any
    mOwnerCentroid: Any
    mOwnerCentroidX: Any
    mOwnerCentroidY: Any
    mOwnerCentroidZ: Any
    mOwnerPosData: Any
    mOwnerVelData: Any
    mRandState: Any
    mRandStateX: Any
    mRandStateY: Any
    mRandStateZ: Any
    mRate: Any
    mSeed: Any
    mSpeed: Any
    mStartTime: Any
    mSweptGeometry: Any
    mTurbulence: Any
    mWorldMatrix: Any
    message: Any
    state: Any
    thisown: Any
    def __init__(self) -> None:
        """Class constructor."""
    @staticmethod
    def addAttribute(attr: MObject) -> MStatus:
        """This method adds a new attribute to a user defined node type during the type's initialization."""
    def addExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Adds content info to the specified table from a file path attribute."""
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> MStatus: ...
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject, affectsTopology: bool) -> MStatus:
        """This method specifies that a particular input attribute affects a specific output attribute."""
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
    def compute(self, plug: MPlug, dataBlock: MDataBlock) -> MStatus:
        """This method should be overridden in user defined nodes."""
    def configCache(self) -> None:
        """Introduced in 2020.0"""
    def connectionBroken(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are made to attributes of this node."""
    def copyInternalData(self) -> None:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def dependsOn(self, depends: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def draw(self, view: M3dView, path: MDagPath, style: int, DisplayStatus: int) -> None:
        """Overriding this method allows the drawing of custom geometry using standard OpenGL calls."""
    def evalEmission2dTexture(self, texAttr: MObject, uCoords: MDoubleArray, vCoords: MDoubleArray, resultColors: MVectorArray, resultAlphas: MDoubleArray) -> MStatus:
        """If a supported 2d texture (see hasValidEmission2dTexture() method documentation) is connected to the given emitter attri"""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    def fluidColor(self, block: MDataBlock) -> MColor:
        """Intended to be called from within the emitter's compute() method, this method retrieves the "fluidColor" attribute value"""
    def fluidDensityEmission(self, block: MDataBlock) -> float:
        """Intended to be called from within the emitter's compute() method, this method retrieves the "fluidDensityEmission" attri"""
    def fluidDropoff(self, block: MDataBlock) -> float:
        """Intended to be called from within the emitter's compute() method, this method retrieves the "fluidDropoff" attribute val"""
    def fluidEmitColor(self, block: MDataBlock) -> bool:
        """Intended to be called from within the emitter's compute() method, this method retrieves the "fluidEmitColor" attribute v"""
    def fluidEmitter(self, fluidObj: MObject, worldMatrix: MMatrix, plugIndex: int) -> MStatus:
        """This is the main method that plug-in fluid emitter nodes must override in order to emit into fluids."""
    def fluidFuelEmission(self, block: MDataBlock) -> float:
        """Intended to be called from within the emitter's compute() method, this method retrieves the "fluidFuelEmission" attribut"""
    def fluidHeatEmission(self, block: MDataBlock) -> float:
        """Intended to be called from within the emitter's compute() method, this method retrieves the "fluidHeatEmission" attribut"""
    def fluidJitter(self, block: MDataBlock) -> bool:
        """Intended to be called from within the emitter's compute() method, this method retrieves the "fluidJitter" attribute valu"""
    def getCacheSetup(self) -> None:
        """Introduced in 2020.0"""
    def getCurrentTime(self, block: MDataBlock) -> MTime:
        """Intended to be called from within the emitter's compute() method, this method returns the time at which the emitter is c"""
    def getDeltaTime(self, plugIndex: int, block: MDataBlock) -> MTime:
        """Intended to be called from within the emitter's compute() method, this method returns the width of the time interval rep"""
    def getEmitterType(self, block: MDataBlock) -> Any:
        """Retrieves the type of the emitter, determined by the "emitterType" attribute value."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> None:
        """Returns the external content (files) that this node depends on."""
    def getFilesToArchive(self, shortName: bool = False, unresolvedName: bool = False, markCouldBeImageSequence: bool = False) -> Any:
        """Use this method to return all external files used by this node."""
    def getInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def getInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def getMaxDistance(self, block: MDataBlock) -> float:
        """Intended to be called from within the emitter's compute() method, this method retrieves the "maxDistance" attribute valu"""
    def getMinDistance(self, block: MDataBlock) -> float:
        """Intended to be called from within the emitter's compute() method, this method retrieves the "minDistance" attribute valu"""
    def getOwnerShape(self) -> MObject:
        """If the emitter is a emitting from an object, this method returns the shape node for the object."""
    def getRandomSeed(self, plugIndex: int, block: MDataBlock) -> int:
        """Intended to be called from within the emitter's compute() method, this method returns the random seed for a specified em"""
    def getRandomState(self, plugIndex: int, block: MDataBlock) -> None:
        """Intended to be called from within the emitter's compute() method, this method copies the emitter node attribute represen"""
    def getRate(self, block: MDataBlock) -> float:
        """Intended to be called from within the emitter's compute() method, this method retrieves the "rate" attribute value commo"""
    def getStartTime(self, plugIndex: int, block: MDataBlock) -> MTime:
        """Intended to be called from within the emitter's compute() method, this method returns the start times for each particle """
    def getWorldMatrix(self) -> MMatrix:
        """Returns the matrix that maps from the emitter's local space coordinates to worldspace."""
    def getWorldPosition(self) -> MPoint:
        """Returns the worldspace coordinates of the emitter."""
    def hasInvalidationRangeTransformation(self) -> bool:
        """Introduced in 2020.0"""
    def hasValidEmission2dTexture(self, texAttr: MObject) -> bool:
        """Certain aspects of Maya's particle and fluid emitters can be textured using 2d textures."""
    @staticmethod
    def inheritAttributesFrom(parentClassName: str) -> MStatus:
        """This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node."""
    @overload
    def internalArrayCount(self) -> int: ...
    @overload
    def internalArrayCount(self) -> int:
        """This method is overridden by nodes that have internal array attributes which are not stored in Maya's datablock."""
    def isAbstractClass(self) -> bool:
        """Override this class to return true if this node is an abstract node."""
    def isPassiveOutput(self) -> bool:
        """This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent val"""
    def isTrackingTopology(self) -> bool:
        """Introduced in 2019.0"""
    def legalConnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal connections being made to attributes of this node."""
    def legalDisconnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal disconnections being made to attributes of this node."""
    def name(self) -> str:
        """Returns the name of this particular instance of this class."""
    def passThroughToMany(self) -> bool:
        """This method is overridden by nodes that want to control the traversal behavior of some Maya search algorithms which trav"""
    def passThroughToOne(self) -> MPlug:
        """This method may be overridden by nodes that have a one-to-one relationship between an input attribute and a correspondin"""
    def postConstructor(self) -> None:
        """Post constructor."""
    def postEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode, evalType: Any) -> MStatus:
        """Clean up node's internal state after threaded evaluation."""
    def preEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode) -> MStatus:
        """Prepare a node's internal state for threaded evaluation."""
    def randgen(self) -> float:
        """Intended to be called from within the emitter's compute() method, this method generates a double-precision random number"""
    def resetRandomState(self, plugIndex: int, block: MDataBlock) -> None:
        """Intended to be called from within the emitter's compute() method, this method resets the emitter's random state data mem"""
    def schedulingType(self) -> Any:
        """When overridden this method controls the degree of parallelism supported by the node during threaded evaluation."""
    def setDependentsDirty(self, plug: MPlug, plugArray: MPlugArray) -> MStatus:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug """
    def setExistWithoutInConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without input connections."""
    def setExistWithoutOutConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without output connections."""
    def setExternalContent(self) -> None:
        """Changes the location of external content in batch."""
    def setExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Sets content info in the specified attribute from the table."""
    def setInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def setRandomState(self, plugIndex: int, block: MDataBlock) -> None:
        """Intended to be called from within the emitter's compute() method, this method copies the emitter node class random state"""
    def shouldSave(self, isSaving: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def thisMObject(self) -> MObject:
        """Returns the MObject associated with this user defined node."""
    def transformInvalidationRange(self, source: MPlug, input: MTimeRange) -> MTimeRange:
        """Introduced in 2020.0"""
    def turbulence(self, block: MDataBlock) -> float:
        """Intended to be called from within the emitter's compute() method, this method retrieves the "turbulence" attribute value"""
    def type(self) -> int:
        """This method returns the type of the node."""
    def typeId(self) -> MTypeId:
        """Returns the TYPEID of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""
    def volumePrimitiveBoundingBox(self, box: MBoundingBox) -> bool:
        """For volume emitters, this method returns the object-space bounding box of the volume primitive associated with the emitt"""
    def volumePrimitiveDistanceFromAxis(self, worldPoint: MPoint, emitterWorldMatrix: MMatrix) -> float:
        """For volume emitters, this method determines the distance from a particular point to the major axis of the volumetric pri"""
    def volumePrimitivePointInside(self, worldPoint: MPoint, emitterWorldMatrix: MMatrix) -> bool:
        """For volume emitters, this method determines whether a particular point in space lies within the volume defined by the em"""

class MPxGeometryData:
    kData: Any
    kGeometryData: Any
    kLast: Any
    thisown: Any
    def __init__(self) -> None:
        """Class Constructor."""
    def copy(self, src: MPxData) -> None:
        """This method initializes an instance of an MPxGeometryData derived class from another existing instance."""
    def deleteComponent(self, compList: MObjectArray) -> bool:
        """This method should be overridden if this data is to support component deletion."""
    def deleteComponentsFromGroups(self, compList: MObjectArray, groupIdArray: MIntArray, groupComponentArray: MObjectArray) -> bool:
        """This method should be overridden to modify the groups that flows along with the geometry, as part of the data, based on """
    @overload
    def iterator(self, componentList: MObjectArray, component: MObject, useComponents: bool) -> MPxGeometryIterator: ...
    @overload
    def iterator(self, componentList: MObjectArray, component: MObject, useComponents: bool, world: bool) -> MPxGeometryIterator:
        """Associates a control point based geometry iterator with this data."""
    @overload
    def matrix(self) -> MMatrix: ...
    @overload
    def matrix(self) -> bool:
        """Return the matrix associated to MPxGeometryData ."""
    def name(self) -> str:
        """Determines the type name of the Data object."""
    def readASCII(self, argList: MArgList, endOfTheLastParsedElement: int) -> MStatus:
        """Creates Data in Data Block as specified by input from ASCII file record."""
    def readBinary(self, in_: int, length: int) -> MStatus:
        """Creates Data in Data Block as specified by binary data from the given stream."""
    def setMatrix(self) -> None:
        """Store the matrix associated to MPxGeometryData ."""
    def smartCopy(self, srcGeom: MPxGeometryData) -> bool:
        """This method is used in conjunction with MPxSurfaceShape classes which support maya's deformations."""
    def typeId(self) -> MTypeId:
        """Determines the type id of the Data object."""
    def updateCompleteVertexGroup(self, component: MObject) -> bool:
        """This method is used in conjunction with MPxSurfaceShape classes which support maya's deformations."""
    def writeASCII(self, out: int) -> MStatus:
        """Encodes Data in accordance with the ASCII file format and outputs it to the given stream."""
    def writeBinary(self, out: int) -> MStatus:
        """Encodes Data in accordance with the binary file format and outputs it to the given stream."""

class MPxGeometryFilter:
    caching: Any
    componentTagExpression: Any
    envelope: Any
    frozen: Any
    groupId: Any
    input: Any
    inputGeom: Any
    isHistoricallyInteresting: Any
    kAssembly: Any
    kBlendShape: Any
    kCameraSetNode: Any
    kClientDeviceNode: Any
    kConstraintNode: Any
    kDefaultScheduling: Any
    kDeformerNode: Any
    kDeformsAll: Any
    kDeformsColors: Any
    kDeformsUVs: Any
    kDependNode: Any
    kEmitterNode: Any
    kEvaluatedDirectly: Any
    kEvaluatedIndirectly: Any
    kFieldNode: Any
    kFluidEmitterNode: Any
    kGeometryFilter: Any
    kGloballySerial: Any
    kGloballySerialize: Any
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
    kParallel: Any
    kParticleAttributeMapperNode: Any
    kPostEvaluationTypeLast: Any
    kSchedulingTypeLast: Any
    kSerial: Any
    kSerialize: Any
    kSkinCluster: Any
    kSpringNode: Any
    kSurfaceShape: Any
    kThreadedDeviceNode: Any
    kTransformNode: Any
    kUntrusted: Any
    message: Any
    outputGeom: Any
    state: Any
    thisown: Any
    def __init__(self) -> None:
        """Class constructor."""
    def accessoryAttribute(self) -> MObject:
        """This method returns an MObject for the attribute to which an accessory shape is connected."""
    def accessoryNodeSetup(self, cmd: MDagModifier) -> MStatus:
        """This method is called by the "deformer -type" command when your node is specified."""
    @staticmethod
    def addAttribute(attr: MObject) -> MStatus:
        """This method adds a new attribute to a user defined node type during the type's initialization."""
    def addExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Adds content info to the specified table from a file path attribute."""
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> MStatus: ...
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject, affectsTopology: bool) -> MStatus:
        """This method specifies that a particular input attribute affects a specific output attribute."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def compute(self) -> MStatus:
        """This method should be overridden in user defined nodes."""
    def configCache(self) -> None:
        """Introduced in 2020.0"""
    def connectionBroken(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are made to attributes of this node."""
    def copyInternalData(self) -> None:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def deform(self, block: MDataBlock, iter: MItGeometry, mat: MMatrix, multiIndex: int) -> MStatus:
        """This method performs the deformation algorithm."""
    def dependsOn(self, depends: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    def getCacheSetup(self) -> None:
        """Introduced in 2020.0"""
    def getDeformationDetails(self) -> int:
        """Retrieves the value set by setDeformationDetails() ."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> None:
        """Returns the external content (files) that this node depends on."""
    def getFilesToArchive(self, shortName: bool = False, unresolvedName: bool = False, markCouldBeImageSequence: bool = False) -> Any:
        """Use this method to return all external files used by this node."""
    def getFixedSetupData(self, name: str) -> MObject:
        """Introduced in 2022.0"""
    def getGeometryIterator(self, iter: MItGeometry, block: MDataBlock, dataHandle: MDataHandle, multiIndex: int, readOnly: bool = True) -> int:
        """Introduced in 2022.0"""
    def getInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def getInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def hasInvalidationRangeTransformation(self) -> bool:
        """Introduced in 2020.0"""
    def indexMapper(self, multiIndex: int) -> Any:
        """Introduced in 2024.0"""
    @staticmethod
    def inheritAttributesFrom(parentClassName: str) -> MStatus:
        """This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node."""
    @overload
    def internalArrayCount(self) -> int: ...
    @overload
    def internalArrayCount(self) -> int:
        """This method is overridden by nodes that have internal array attributes which are not stored in Maya's datablock."""
    def isAbstractClass(self) -> bool:
        """Override this class to return true if this node is an abstract node."""
    def isPassiveOutput(self) -> bool:
        """This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent val"""
    def isTrackingTopology(self) -> bool:
        """Introduced in 2019.0"""
    def legalConnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal connections being made to attributes of this node."""
    def legalDisconnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal disconnections being made to attributes of this node."""
    def name(self) -> str:
        """Returns the name of this particular instance of this class."""
    def passThroughToMany(self) -> bool:
        """This method is overridden by nodes that want to control the traversal behavior of some Maya search algorithms which trav"""
    def passThroughToOne(self) -> MPlug:
        """This method may be overridden by nodes that have a one-to-one relationship between an input attribute and a correspondin"""
    def postConstructor(self) -> None:
        """Post constructor."""
    def postEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode, evalType: Any) -> MStatus:
        """Clean up node's internal state after threaded evaluation."""
    def preEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode) -> MStatus:
        """Prepare a node's internal state for threaded evaluation."""
    def schedulingType(self) -> Any:
        """When overridden this method controls the degree of parallelism supported by the node during threaded evaluation."""
    def setDeformationDetails(self, flags: int) -> MStatus:
        """This method allows the plug-in node to inform the system that it intends to deform components other than just positions."""
    def setDependentsDirty(self, plug: MPlug, plugArray: MPlugArray) -> MStatus:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug """
    def setExistWithoutInConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without input connections."""
    def setExistWithoutOutConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without output connections."""
    def setExternalContent(self) -> None:
        """Changes the location of external content in batch."""
    def setExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Sets content info in the specified attribute from the table."""
    def setInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def setModifiedCallback(self, list: MSelectionList, listAdded: bool) -> None:
        """This callback method can be overriden and is called whenever the set this deformer is operating on is modified."""
    def setUseExistingConnectionWhenSetEditing(self, state: bool) -> None:
        """This method allows the plugin node to request special treatment during set editing."""
    def shouldSave(self, isSaving: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def thisMObject(self) -> MObject:
        """Returns the MObject associated with this user defined node."""
    def transformInvalidationRange(self, source: MPlug, input: MTimeRange) -> MTimeRange:
        """Introduced in 2020.0"""
    def type(self) -> int:
        """This method returns the type of the node."""
    def typeId(self) -> MTypeId:
        """Returns the TYPEID of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""

class MPxGeometryIterator:
    thisown: Any
    @overload
    def __init__(self, userGeometry: None, components: MObjectArray) -> None: ...
    @overload
    def __init__(self, userGeometry: None, components: MObject) -> None:
        """Class constructor."""
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def component(self, component: MObject) -> None:
        """Returns a component for the current item in the iteration."""
    def currentPoint(self) -> int:
        """Returns the index that is being iterated on."""
    def geometry(self) -> None:
        """Returns a pointer to the geometry that this iterator is iterating over."""
    def hasNormals(self) -> bool:
        """Indicates whether the underlying geometry has normals."""
    def hasPoints(self) -> bool:
        """Indicates whether the underlying geometry has point data."""
    def index(self) -> int:
        """Returns a unique index for the current item in the iteration."""
    def indexUnsimplified(self) -> int:
        """Returns a unique index for the current item in the iteration Rather than being the iterator index this is the index for """
    def isDone(self) -> bool:
        """Indicates if all the items have been traversed yet."""
    def iteratorCount(self) -> int:
        """Returns an estimate of how many items will be iterated over."""
    def maxPoints(self) -> int:
        """Returns the largest index that will be iterated over."""
    def next(self) -> MStatus:
        """Advances to the next component."""
    def point(self) -> MPoint:
        """Returns the current component's positional data."""
    def reset(self) -> None:
        """Resets the iterator to the start of the components so that another pass over them may be made."""
    def setCurrentPoint(self, arg: Any) -> None:
        """Set the current index of the iteration."""
    def setMaxPoints(self, arg: Any) -> None:
        """Sets the largest index that will be iterated over."""
    def setObject(self) -> None:
        """Optional method to set a shape object to iterate over to allow tweaking of the shape's history (input geometry)."""
    def setPoint(self) -> None:
        """Sets the current component's positional data."""
    def setPointGetNext(self) -> int:
        """Sets the current component's positional data, gets the next point."""

class MPxGlBuffer:
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, view: M3dView) -> None:
        """Construct an MPxGlBuffer for use with the currently active view."""
    def beginBufferNotify(self) -> None:
        """This method is called when the GL buffer is being setup by the viewport renderer."""
    def bindFbo(self) -> MStatus:
        """If a frame buffer object was created using the method openFbo, then this method can be used to bind that Fbo."""
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def closeFbo(self) -> MStatus:
        """Destroy a frame buffer object that was created by createFbo."""
    def endBufferNotify(self) -> None:
        """This method is called when the GL buffer is being shutdown by the viewport renderer."""
    def openFbo(self, width: Any, height: Any) -> MStatus:
        """Create a frame buffer object where the renderer result will be stored."""
    def unbindFbo(self) -> MStatus:
        """If a frame buffer object was created using the method openFbo, then this method can be used to unbind that Fbo."""

class MPxHardwareShader:
    caching: Any
    frozen: Any
    isHistoricallyInteresting: Any
    kAssembly: Any
    kBlendShape: Any
    kCameraSetNode: Any
    kClientDeviceNode: Any
    kConstraintNode: Any
    kDefaultScheduling: Any
    kDeformerNode: Any
    kDependNode: Any
    kEmitterNode: Any
    kEvaluatedDirectly: Any
    kEvaluatedIndirectly: Any
    kFieldNode: Any
    kFluidEmitterNode: Any
    kGeometryFilter: Any
    kGloballySerial: Any
    kGloballySerialize: Any
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
    kParallel: Any
    kParticleAttributeMapperNode: Any
    kPostEvaluationTypeLast: Any
    kSchedulingTypeLast: Any
    kSerial: Any
    kSerialize: Any
    kSkinCluster: Any
    kSpringNode: Any
    kSurfaceShape: Any
    kThreadedDeviceNode: Any
    kTransformNode: Any
    kUntrusted: Any
    message: Any
    outColor: Any
    outColorB: Any
    outColorG: Any
    outColorR: Any
    state: Any
    thisown: Any
    def __init__(self) -> None:
        """Class constructor."""
    @staticmethod
    def addAttribute(attr: MObject) -> MStatus:
        """This method adds a new attribute to a user defined node type during the type's initialization."""
    def addExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Adds content info to the specified table from a file path attribute."""
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> MStatus: ...
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject, affectsTopology: bool) -> MStatus:
        """This method specifies that a particular input attribute affects a specific output attribute."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def compute(self) -> MStatus:
        """This method should be overridden in user defined nodes."""
    def configCache(self) -> None:
        """Introduced in 2020.0"""
    def connectionBroken(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are made to attributes of this node."""
    def copyInternalData(self) -> None:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def dependsOn(self, depends: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    @staticmethod
    def findResource(name: str, shaderPath: str) -> str:
        """This is a static utility to find the full path to a shader resource (typically a texture)."""
    def getCacheSetup(self) -> None:
        """Introduced in 2020.0"""
    def getExternalContent(self, table: MExternalContentInfoTable) -> None:
        """Returns the external content (files) that this node depends on."""
    def getFilesToArchive(self, shortName: bool = False, unresolvedName: bool = False, markCouldBeImageSequence: bool = False) -> Any:
        """Use this method to return all external files used by this node."""
    @staticmethod
    def getHardwareShaderPtr(object: MObject) -> MPxHardwareShader:
        """This is a static convenience method to be able to get an MPxHardwareShader from an MObject provided by a swatch generato"""
    def getInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def getInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def hasInvalidationRangeTransformation(self) -> bool:
        """Introduced in 2020.0"""
    @staticmethod
    def inheritAttributesFrom(parentClassName: str) -> MStatus:
        """This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node."""
    @overload
    def internalArrayCount(self) -> int: ...
    @overload
    def internalArrayCount(self) -> int:
        """This method is overridden by nodes that have internal array attributes which are not stored in Maya's datablock."""
    def isAbstractClass(self) -> bool:
        """Override this class to return true if this node is an abstract node."""
    def isPassiveOutput(self) -> bool:
        """This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent val"""
    def isTrackingTopology(self) -> bool:
        """Introduced in 2019.0"""
    def legalConnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal connections being made to attributes of this node."""
    def legalDisconnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal disconnections being made to attributes of this node."""
    def name(self) -> str:
        """Returns the name of this particular instance of this class."""
    def passThroughToMany(self) -> bool:
        """This method is overridden by nodes that want to control the traversal behavior of some Maya search algorithms which trav"""
    def passThroughToOne(self) -> MPlug:
        """This method may be overridden by nodes that have a one-to-one relationship between an input attribute and a correspondin"""
    def postConstructor(self) -> None:
        """Post constructor."""
    def postEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode, evalType: Any) -> MStatus:
        """Clean up node's internal state after threaded evaluation."""
    def preEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode) -> MStatus:
        """Prepare a node's internal state for threaded evaluation."""
    def profile(self) -> Any:
        """Override this method to specify the renderers your shader supports."""
    def render(self, iterator: MGeometryList) -> MStatus:
        """Override this method to render geometry using your hardware shader."""
    def renderSwatchImage(self, image: MImage) -> MStatus:
        """If the shader specifies to override swatch rendering, then this method must be overridden in order to draw anything into"""
    def schedulingType(self) -> Any:
        """When overridden this method controls the degree of parallelism supported by the node during threaded evaluation."""
    def setDependentsDirty(self, plug: MPlug, plugArray: MPlugArray) -> MStatus:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug """
    def setExistWithoutInConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without input connections."""
    def setExistWithoutOutConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without output connections."""
    def setExternalContent(self) -> None:
        """Changes the location of external content in batch."""
    def setExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Sets content info in the specified attribute from the table."""
    def setInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def setUniformParameters(self, parameters: MUniformParameterList, remapCurrentValues: bool = True, dagModifier: MDagModifier | None = None) -> MStatus:
        """Call this method to set the list of uniform parameters this shader uses."""
    def setVaryingParameters(self, parameters: MVaryingParameterList, remapCurrentValues: bool = True, dagModifier: MDagModifier | None = None) -> MStatus:
        """Call this method to set the list of varying parameters this shader uses."""
    def shouldSave(self, isSaving: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def thisMObject(self) -> MObject:
        """Returns the MObject associated with this user defined node."""
    def transformInvalidationRange(self, source: MPlug, input: MTimeRange) -> MTimeRange:
        """Introduced in 2020.0"""
    def transparencyOptions(self) -> int:
        """This method returns transparency options for usage as hints for Maya's internal draw during a given rendering pass."""
    def type(self) -> int:
        """This method returns the type of the node."""
    def typeId(self) -> MTypeId:
        """Returns the TYPEID of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""

class MPxHwShaderNode:
    caching: Any
    frozen: Any
    isHistoricallyInteresting: Any
    kAssembly: Any
    kBlendShape: Any
    kCameraSetNode: Any
    kClientDeviceNode: Any
    kConstraintNode: Any
    kDefaultScheduling: Any
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
    kGloballySerial: Any
    kGloballySerialize: Any
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
    kParallel: Any
    kParticleAttributeMapperNode: Any
    kPostEvaluationTypeLast: Any
    kSchedulingTypeLast: Any
    kSerial: Any
    kSerialize: Any
    kSkinCluster: Any
    kSpringNode: Any
    kSurfaceShape: Any
    kThreadedDeviceNode: Any
    kTransformNode: Any
    kUntrusted: Any
    kWriteAll: Any
    kWriteColorArrays: Any
    kWriteNone: Any
    kWriteNormalArray: Any
    kWriteTexCoordArrays: Any
    kWriteVertexArray: Any
    message: Any
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
    state: Any
    thisown: Any
    def __init__(self) -> None:
        """Class constructor."""
    @staticmethod
    def addAttribute(attr: MObject) -> MStatus:
        """This method adds a new attribute to a user defined node type during the type's initialization."""
    def addExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Adds content info to the specified table from a file path attribute."""
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> MStatus: ...
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject, affectsTopology: bool) -> MStatus:
        """This method specifies that a particular input attribute affects a specific output attribute."""
    def bind(self, request: MDrawRequest, view: M3dView) -> MStatus:
        """This method is invoked for hardware rendering to Maya's 3D view."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def colorsPerVertex(self) -> int:
        """This method returns the number of color values per vertex that the hw shader node would like to receive from Maya."""
    def compute(self) -> MStatus:
        """This method should be overridden in user defined nodes."""
    def configCache(self) -> None:
        """Introduced in 2020.0"""
    def connectionBroken(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are made to attributes of this node."""
    def copyInternalData(self) -> None:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def currentPath(self) -> MDagPath:
        """This method returns a reference to the current path that the shader is invoked for."""
    def currentShadingEngine(self) -> MObject:
        """This method returns an MObject to the shading engine that is currently being rendered."""
    def dependsOn(self, depends: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def dirtyMask(self) -> int:
        """This method returns a "dirty" mask that indicates which geometry items have changed from the last invocation of the plug"""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    @overload
    def geometry(self, request: MDrawRequest, view: M3dView, prim: int, writable: int, indexCount: int, indexArray: int, vertexCount: int, vertexIDs: int, vertexArray: float, normalCount: int, normalArrays: Any, colorCount: int, colorArrays: Any, texCoordCount: int, texCoordArrays: Any) -> MStatus: ...
    @overload
    def geometry(self, request: MDrawRequest, view: M3dView, prim: int, writable: int, indexCount: int, indexArray: int, vertexCount: int, vertexIDs: int, vertexArray: float, normalCount: int, normalArrays: Any, colorCount: int, colorArrays: Any, texCoordCount: int, texCoordArrays: Any, faceIDs: int, localUVCoord: float) -> MStatus:
        """Deprecated in 2016.0"""
    def getCacheSetup(self) -> None:
        """Introduced in 2020.0"""
    def getExternalContent(self, table: MExternalContentInfoTable) -> None:
        """Returns the external content (files) that this node depends on."""
    def getFilesToArchive(self, shortName: bool = False, unresolvedName: bool = False, markCouldBeImageSequence: bool = False) -> Any:
        """Use this method to return all external files used by this node."""
    @staticmethod
    def getHwShaderNodePtr(object: MObject) -> MPxHwShaderNode:
        """This is a static convenience method to be able to get an MPxHwShaderNode from an MObject provided by a swatch generator """
    def getInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def getInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def glBind(self, shapePath: MDagPath) -> MStatus:
        """This method should only be overridden for hardware rendering."""
    @overload
    def glGeometry(self, shapePath: MDagPath, glPrim: int, writeMask: int, indexCount: int, indexArray: int, vertexCount: int, vertexIDs: int, vertexArray: float, normalCount: int, normalArrays: Any, colorCount: int, colorArrays: Any, texCoordCount: int, texCoordArrays: Any) -> MStatus: ...
    @overload
    def glGeometry(self, shapePath: MDagPath, glPrim: int, writeMask: int, indexCount: int, indexArray: int, vertexCount: int, vertexIDs: int, vertexArray: float, normalCount: int, normalArrays: Any, colorCount: int, colorArrays: Any, texCoordCount: int, texCoordArrays: Any, faceIDs: int, localUVCoord: float) -> MStatus:
        """Deprecated in 2016.0"""
    def glUnbind(self, shapePath: MDagPath) -> MStatus:
        """This method should only be overridden for hardware rendering."""
    def hasInvalidationRangeTransformation(self) -> bool:
        """Introduced in 2020.0"""
    def hasTransparency(self) -> bool:
        """This method returns a boolean value that indicates whether the object will be drawn transparently or not."""
    @staticmethod
    def inheritAttributesFrom(parentClassName: str) -> MStatus:
        """This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node."""
    @overload
    def internalArrayCount(self) -> int: ...
    @overload
    def internalArrayCount(self) -> int:
        """This method is overridden by nodes that have internal array attributes which are not stored in Maya's datablock."""
    def invertTexCoords(self) -> bool:
        """Specifies whether this shader requires inverted texture coordinates."""
    def isAbstractClass(self) -> bool:
        """Override this class to return true if this node is an abstract node."""
    def isPassiveOutput(self) -> bool:
        """This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent val"""
    def isTrackingTopology(self) -> bool:
        """Introduced in 2019.0"""
    def legalConnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal connections being made to attributes of this node."""
    def legalDisconnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal disconnections being made to attributes of this node."""
    def name(self) -> str:
        """Returns the name of this particular instance of this class."""
    def normalsPerVertex(self) -> int:
        """Specifies how many normals per vertex the HW shader would like Maya to provide."""
    def passThroughToMany(self) -> bool:
        """This method is overridden by nodes that want to control the traversal behavior of some Maya search algorithms which trav"""
    def passThroughToOne(self) -> MPlug:
        """This method may be overridden by nodes that have a one-to-one relationship between an input attribute and a correspondin"""
    def postConstructor(self) -> None:
        """Post constructor."""
    def postEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode, evalType: Any) -> MStatus:
        """Clean up node's internal state after threaded evaluation."""
    def preEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode) -> MStatus:
        """Prepare a node's internal state for threaded evaluation."""
    def provideFaceIDs(self) -> bool:
        """This method returns a boolean value that indicates whether a map of the face IDs will be provided to the geometry method"""
    def provideLocalUVCoord(self) -> bool:
        """This method returns a boolean value that indicates whether the local uv coordinates of the subdivided face vertices will"""
    def provideVertexIDs(self) -> bool:
        """This method returns a boolean value that indicates whether a map of the vertex IDs will be provided to the geometry meth"""
    def renderSwatchImage(self, image: MImage) -> MStatus:
        """If the shader specifies to override swatch rendering, then this method must be overridden in order to draw anything into"""
    def schedulingType(self) -> Any:
        """When overridden this method controls the degree of parallelism supported by the node during threaded evaluation."""
    def setDependentsDirty(self, plug: MPlug, plugArray: MPlugArray) -> MStatus:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug """
    def setExistWithoutInConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without input connections."""
    def setExistWithoutOutConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without output connections."""
    def setExternalContent(self) -> None:
        """Changes the location of external content in batch."""
    def setExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Sets content info in the specified attribute from the table."""
    def setInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def shouldSave(self, isSaving: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def supportsBatching(self) -> bool:
        """Specifies whether or not this shader supports batched rendering of shapes."""
    def texCoordsPerVertex(self) -> int:
        """This method returns the number of texture coordinate values per vertex that the hw shader node would like to receive fro"""
    def thisMObject(self) -> MObject:
        """Returns the MObject associated with this user defined node."""
    def transformInvalidationRange(self, source: MPlug, input: MTimeRange) -> MTimeRange:
        """Introduced in 2020.0"""
    def transparencyOptions(self) -> int:
        """This method returns transparency options for usage as hints for Maya's internal draw during a given rendering pass."""
    def type(self) -> int:
        """This method returns the type of the node."""
    def typeId(self) -> MTypeId:
        """Returns the TYPEID of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""
    def unbind(self, request: MDrawRequest, view: M3dView) -> MStatus:
        """This method is invoked for hardware rendering to Maya's 3D view."""

class MPxIkSolverNode:
    caching: Any
    frozen: Any
    isHistoricallyInteresting: Any
    kAssembly: Any
    kBlendShape: Any
    kCameraSetNode: Any
    kClientDeviceNode: Any
    kConstraintNode: Any
    kDefaultScheduling: Any
    kDeformerNode: Any
    kDependNode: Any
    kEmitterNode: Any
    kEvaluatedDirectly: Any
    kEvaluatedIndirectly: Any
    kFieldNode: Any
    kFluidEmitterNode: Any
    kGeometryFilter: Any
    kGloballySerial: Any
    kGloballySerialize: Any
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
    kParallel: Any
    kParticleAttributeMapperNode: Any
    kPostEvaluationTypeLast: Any
    kSchedulingTypeLast: Any
    kSerial: Any
    kSerialize: Any
    kSkinCluster: Any
    kSpringNode: Any
    kSurfaceShape: Any
    kThreadedDeviceNode: Any
    kTransformNode: Any
    kUntrusted: Any
    message: Any
    state: Any
    thisown: Any
    def __init__(self) -> None:
        """Constructor."""
    @staticmethod
    def addAttribute(attr: MObject) -> MStatus:
        """This method adds a new attribute to a user defined node type during the type's initialization."""
    def addExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Adds content info to the specified table from a file path attribute."""
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> MStatus: ...
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject, affectsTopology: bool) -> MStatus:
        """This method specifies that a particular input attribute affects a specific output attribute."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def compute(self) -> MStatus:
        """This method should be overridden in user defined nodes."""
    def configCache(self) -> None:
        """Introduced in 2020.0"""
    def connectionBroken(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are made to attributes of this node."""
    def copyInternalData(self) -> None:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def create(self, *args: Any, **kwargs: Any) -> Any: ...
    def dependsOn(self, depends: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def doSolve(self) -> MStatus:
        """This is where the main solving takes place."""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    def funcValueTolerance(self) -> float:
        """Return the error value for this solver."""
    def getCacheSetup(self) -> None:
        """Introduced in 2020.0"""
    def getExternalContent(self, table: MExternalContentInfoTable) -> None:
        """Returns the external content (files) that this node depends on."""
    def getFilesToArchive(self, shortName: bool = False, unresolvedName: bool = False, markCouldBeImageSequence: bool = False) -> Any:
        """Use this method to return all external files used by this node."""
    def getInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def getInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def groupHandlesByTopology(self) -> bool:
        """Deprecated in 2016.0"""
    def handleGroup(self) -> Any:
        """Returns the handle group for this solver."""
    def hasInvalidationRangeTransformation(self) -> bool:
        """Introduced in 2020.0"""
    def hasJointLimitSupport(self) -> bool:
        """Deprecated in 2016.0"""
    def hasUniqueSolution(self) -> bool:
        """Deprecated in 2016.0"""
    @staticmethod
    def inheritAttributesFrom(parentClassName: str) -> MStatus:
        """This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node."""
    @overload
    def internalArrayCount(self) -> int: ...
    @overload
    def internalArrayCount(self) -> int:
        """This method is overridden by nodes that have internal array attributes which are not stored in Maya's datablock."""
    def isAbstractClass(self) -> bool:
        """Override this class to return true if this node is an abstract node."""
    def isAttributeCreatedBySolver(self, attr: MObject) -> bool:
        """Introduced in 2019.0"""
    def isPassiveOutput(self) -> bool:
        """This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent val"""
    def isPositionOnly(self) -> bool:
        """Deprecated in 2016.0"""
    def isSingleChainOnly(self) -> bool:
        """This method indicates whether this solver is a single chain solver."""
    def isTrackingTopology(self) -> bool:
        """Introduced in 2019.0"""
    def legalConnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal connections being made to attributes of this node."""
    def legalDisconnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal disconnections being made to attributes of this node."""
    def maxIterations(self) -> int:
        """Return the the maximum nuber of itertations for a solution by this solver."""
    def name(self) -> str:
        """Returns the name of this particular instance of this class."""
    def passThroughToMany(self) -> bool:
        """This method is overridden by nodes that want to control the traversal behavior of some Maya search algorithms which trav"""
    def passThroughToOne(self) -> MPlug:
        """This method may be overridden by nodes that have a one-to-one relationship between an input attribute and a correspondin"""
    def positionOnly(self) -> bool:
        """Indicates whether the ik solution is dependent on the ikHandle position only or also uses the orientation."""
    def postConstructor(self) -> None:
        """Post constructor."""
    def postEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode, evalType: Any) -> MStatus:
        """Clean up node's internal state after threaded evaluation."""
    def postSolve(self) -> MStatus:
        """This method is called after doSolve has finished."""
    def preEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode) -> MStatus:
        """Prepare a node's internal state for threaded evaluation."""
    def preSolve(self) -> MStatus:
        """This method is called before doSolve ."""
    def rotatePlane(self) -> bool:
        """This method indicates whether this solver supports the rotate plane."""
    def schedulingType(self) -> Any:
        """When overridden this method controls the degree of parallelism supported by the node during threaded evaluation."""
    def setDependentsDirty(self, plug: MPlug, plugArray: MPlugArray) -> MStatus:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug """
    def setExistWithoutInConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without input connections."""
    def setExistWithoutOutConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without output connections."""
    def setExternalContent(self) -> None:
        """Changes the location of external content in batch."""
    def setExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Sets content info in the specified attribute from the table."""
    def setFuncValueTolerance(self, tolerance: float) -> MStatus:
        """Set the error value for this solver."""
    def setHandleGroup(self) -> None:
        """Set the handle group of this solver."""
    def setInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def setMaxIterations(self, value: int) -> MStatus:
        """Set the maximum iterations for a solution by this solver."""
    def setPositionOnly(self, positionOnly: bool) -> MStatus:
        """Sets whether or not the solver supports handle orientation."""
    def setRotatePlane(self, rotatePlane: bool) -> MStatus:
        """This method sets whether or not this solver supports the rotate plane."""
    def setSingleChainOnly(self, singleChainOnly: bool) -> MStatus:
        """This method sets whether or not this solver is a single chain solver."""
    def setSupportJointLimits(self, supportJointLimits: bool) -> MStatus:
        """This method sets whether or not the solver supports limits on joint angles."""
    def setUniqueSolution(self, uniqueSolution: bool) -> MStatus:
        """This method sets whether or not the solver provides a unique solution."""
    def shouldSave(self, isSaving: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def singleChainOnly(self) -> bool:
        """This method indicates whether this solver is a single chain solver."""
    def snapHandle(self, handle: MObject) -> None:
        """This function positions the handle at the end effector position."""
    def solverTypeName(self) -> str:
        """This method returns the type name of the solver."""
    def supportJointLimits(self) -> bool:
        """This method indicates whether the solver supports limits on joint angles."""
    def thisMObject(self) -> MObject:
        """Returns the MObject associated with this user defined node."""
    def toSolverSpace(self) -> MMatrix:
        """Returns the local space matrix for this solver."""
    def toWorldSpace(self) -> MMatrix:
        """Returns the world space matrix for this solver."""
    def transformInvalidationRange(self, source: MPlug, input: MTimeRange) -> MTimeRange:
        """Introduced in 2020.0"""
    def type(self) -> int:
        """This method returns the type of the node."""
    def typeId(self) -> MTypeId:
        """Returns the TYPEID of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""
    def uniqueSolution(self) -> bool:
        """This method indicates whether the solver provides a unique solution."""

class MPxImageFile:
    thisown: Any
    def __init__(self) -> None:
        """The default class constructor."""
    def close(self) -> MStatus:
        """Close the image file."""
    def glLoad(self, info: MImageFileInfo, imageNumber: int) -> MStatus:
        """Load the previously opened image file as an OpenGL texture."""
    def load(self, image: MImage, imageNumber: int) -> MStatus:
        """Load the previously opened image file into an MImage ."""
    def open(self, pathname: str, info: MImageFileInfo) -> MStatus:
        """Attempt to open the specified file as an image and extract the image characteristics."""

class MPxImagePlane:
    alphaGain: Any
    alreadyPremult: Any
    caching: Any
    center: Any
    centerX: Any
    centerY: Any
    centerZ: Any
    colorGain: Any
    colorGainB: Any
    colorGainG: Any
    colorGainR: Any
    colorOffset: Any
    colorOffsetB: Any
    colorOffsetG: Any
    colorOffsetR: Any
    composite: Any
    coverage: Any
    coverageOrigin: Any
    coverageOriginX: Any
    coverageOriginY: Any
    coverageX: Any
    coverageY: Any
    depth: Any
    depthBias: Any
    depthFile: Any
    depthOversample: Any
    depthScale: Any
    displayMode: Any
    displayOnlyIfCurrent: Any
    fit: Any
    frameExtension: Any
    frameOffset: Any
    frozen: Any
    height: Any
    imageName: Any
    imageType: Any
    isHistoricallyInteresting: Any
    kAssembly: Any
    kBlendShape: Any
    kCameraSetNode: Any
    kClientDeviceNode: Any
    kConstraintNode: Any
    kDefaultScheduling: Any
    kDeformerNode: Any
    kDependNode: Any
    kEmitterNode: Any
    kEvaluatedDirectly: Any
    kEvaluatedIndirectly: Any
    kFieldNode: Any
    kFluidEmitterNode: Any
    kGeometryFilter: Any
    kGloballySerial: Any
    kGloballySerialize: Any
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
    kParallel: Any
    kParticleAttributeMapperNode: Any
    kPostEvaluationTypeLast: Any
    kSchedulingTypeLast: Any
    kSerial: Any
    kSerialize: Any
    kSkinCluster: Any
    kSpringNode: Any
    kSurfaceShape: Any
    kThreadedDeviceNode: Any
    kTransformNode: Any
    kUntrusted: Any
    lockedToCamera: Any
    maxShadingSamples: Any
    message: Any
    offset: Any
    offsetX: Any
    offsetY: Any
    rotate: Any
    separateDepth: Any
    shadingSamples: Any
    shadingSamplesOverride: Any
    size: Any
    sizeX: Any
    sizeY: Any
    sourceTexture: Any
    squeezeCorrection: Any
    state: Any
    thisown: Any
    useDepthMap: Any
    useFrameExtension: Any
    visibleInReflections: Any
    visibleInRefractions: Any
    width: Any
    def __init__(self) -> None:
        """Class constructor."""
    @staticmethod
    def addAttribute(attr: MObject) -> MStatus:
        """This method adds a new attribute to a user defined node type during the type's initialization."""
    def addExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Adds content info to the specified table from a file path attribute."""
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> MStatus: ...
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject, affectsTopology: bool) -> MStatus:
        """This method specifies that a particular input attribute affects a specific output attribute."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def compute(self) -> MStatus:
        """This method should be overridden in user defined nodes."""
    def configCache(self) -> None:
        """Introduced in 2020.0"""
    def connectionBroken(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are made to attributes of this node."""
    def copyInternalData(self) -> None:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def dependsOn(self, depends: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def exactImageFile(self, refFileName: str) -> str:
        """API users can call this method to resolve a file name."""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    def getCacheSetup(self) -> None:
        """Introduced in 2020.0"""
    def getExternalContent(self, table: MExternalContentInfoTable) -> None:
        """Returns the external content (files) that this node depends on."""
    def getFilesToArchive(self, shortName: bool = False, unresolvedName: bool = False, markCouldBeImageSequence: bool = False) -> Any:
        """Use this method to return all external files used by this node."""
    def getInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def getInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def hasInvalidationRangeTransformation(self) -> bool:
        """Introduced in 2020.0"""
    @staticmethod
    def inheritAttributesFrom(parentClassName: str) -> MStatus:
        """This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node."""
    @overload
    def internalArrayCount(self) -> int: ...
    @overload
    def internalArrayCount(self) -> int:
        """This method is overridden by nodes that have internal array attributes which are not stored in Maya's datablock."""
    def isAbstractClass(self) -> bool:
        """Override this class to return true if this node is an abstract node."""
    def isPassiveOutput(self) -> bool:
        """This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent val"""
    def isTrackingTopology(self) -> bool:
        """Introduced in 2019.0"""
    def legalConnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal connections being made to attributes of this node."""
    def legalDisconnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal disconnections being made to attributes of this node."""
    def loadImageMap(self, fileName: str, frame: int, image: MImage) -> MStatus:
        """Override this method to load the file of name fileName into the image MImage ."""
    def name(self) -> str:
        """Returns the name of this particular instance of this class."""
    def passThroughToMany(self) -> bool:
        """This method is overridden by nodes that want to control the traversal behavior of some Maya search algorithms which trav"""
    def passThroughToOne(self) -> MPlug:
        """This method may be overridden by nodes that have a one-to-one relationship between an input attribute and a correspondin"""
    def postConstructor(self) -> None:
        """Post constructor."""
    def postEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode, evalType: Any) -> MStatus:
        """Clean up node's internal state after threaded evaluation."""
    def preEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode) -> MStatus:
        """Prepare a node's internal state for threaded evaluation."""
    def refreshImage(self) -> None:
        """Forces the image plane to be refreshed."""
    def schedulingType(self) -> Any:
        """When overridden this method controls the degree of parallelism supported by the node during threaded evaluation."""
    def setDependentsDirty(self, plug: MPlug, plugArray: MPlugArray) -> MStatus:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug """
    def setExistWithoutInConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without input connections."""
    def setExistWithoutOutConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without output connections."""
    def setExternalContent(self) -> None:
        """Changes the location of external content in batch."""
    def setExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Sets content info in the specified attribute from the table."""
    def setImageDirty(self) -> None:
        """Forces the image plane to be reloaded on the next refresh."""
    def setInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def shouldSave(self, isSaving: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def thisMObject(self) -> MObject:
        """Returns the MObject associated with this user defined node."""
    def transformInvalidationRange(self, source: MPlug, input: MTimeRange) -> MTimeRange:
        """Introduced in 2020.0"""
    def type(self) -> int:
        """Returns the type of node that this is."""
    def typeId(self) -> MTypeId:
        """Returns the TYPEID of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""

class MPxLocatorNode:
    boundingBoxCenterX: Any
    boundingBoxCenterY: Any
    boundingBoxCenterZ: Any
    caching: Any
    center: Any
    frozen: Any
    instObjGroups: Any
    intermediateObject: Any
    inverseMatrix: Any
    isHistoricallyInteresting: Any
    isTemplated: Any
    kAssembly: Any
    kBlendShape: Any
    kCameraSetNode: Any
    kClientDeviceNode: Any
    kConstraintNode: Any
    kDefaultScheduling: Any
    kDeformerNode: Any
    kDependNode: Any
    kEmitterNode: Any
    kEvaluatedDirectly: Any
    kEvaluatedIndirectly: Any
    kFieldNode: Any
    kFluidEmitterNode: Any
    kGeometryFilter: Any
    kGloballySerial: Any
    kGloballySerialize: Any
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
    kParallel: Any
    kParticleAttributeMapperNode: Any
    kPostEvaluationTypeLast: Any
    kSchedulingTypeLast: Any
    kSerial: Any
    kSerialize: Any
    kSkinCluster: Any
    kSpringNode: Any
    kSurfaceShape: Any
    kThreadedDeviceNode: Any
    kTransformNode: Any
    kUntrusted: Any
    localPosition: Any
    localPositionX: Any
    localPositionY: Any
    localPositionZ: Any
    localScale: Any
    localScaleX: Any
    localScaleY: Any
    localScaleZ: Any
    matrix: Any
    message: Any
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
    state: Any
    thisown: Any
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
        """Constructor"""
    @staticmethod
    def addAttribute(attr: MObject) -> MStatus:
        """This method adds a new attribute to a user defined node type during the type's initialization."""
    def addExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Adds content info to the specified table from a file path attribute."""
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> MStatus: ...
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject, affectsTopology: bool) -> MStatus:
        """This method specifies that a particular input attribute affects a specific output attribute."""
    def boundingBox(self) -> MBoundingBox:
        """This method should be overridden to return a bounding box for the locator."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def closestPoint(self, cursorRayPoint: MPoint, cursorRayDir: MVector) -> MPoint:
        """Returns the point on the locator, in the locator's local space, which is closest along the specified ray."""
    def color(self, displayStatus: int) -> int:
        """This method returns the index of the color that is the default draw color for the given display status."""
    def colorRGB(self, displayStatus: int) -> MColor:
        """This method returns the RGB values of the default draw color for the given display status."""
    def compute(self) -> MStatus:
        """This method should be overridden in user defined nodes."""
    def configCache(self) -> None:
        """Introduced in 2020.0"""
    def connectionBroken(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are made to attributes of this node."""
    def copyInternalData(self) -> None:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def dependsOn(self, depends: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def draw(self, view: M3dView, path: MDagPath, style: int, DisplayStatus: int) -> None:
        """Deprecated in 2024.0"""
    def drawLast(self) -> bool:
        """Indicates that this locator should be the last item draw in a given refresh cycle."""
    def excludeAsLocator(self) -> bool:
        """When the modelPanel is set to not draw locators, returing true will also not draw the custom locator."""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    def getCacheSetup(self, evalNode: MEvaluationNode, disablingInfo: MNodeCacheDisablingInfo, cacheSetupInfo: MNodeCacheSetupInfo, monitoredAttributes: MObjectArray) -> None:
        """Introduced in 2020.0"""
    def getExternalContent(self, table: MExternalContentInfoTable) -> None:
        """Returns the external content (files) that this node depends on."""
    def getFilesToArchive(self, shortName: bool = False, unresolvedName: bool = False, markCouldBeImageSequence: bool = False) -> Any:
        """Use this method to return all external files used by this node."""
    def getInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def getInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def getShapeSelectionMask(self) -> MSelectionMask:
        """This routine can be overridden to provide information about the selection mask of the locator."""
    def hasInvalidationRangeTransformation(self) -> bool:
        """Introduced in 2020.0"""
    @staticmethod
    def inheritAttributesFrom(parentClassName: str) -> MStatus:
        """This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node."""
    @overload
    def internalArrayCount(self) -> int: ...
    @overload
    def internalArrayCount(self) -> int:
        """This method is overridden by nodes that have internal array attributes which are not stored in Maya's datablock."""
    def isAbstractClass(self) -> bool:
        """Override this class to return true if this node is an abstract node."""
    def isBounded(self) -> bool:
        """This method should be overridden to return true if the user supplies a bounding box routine."""
    def isPassiveOutput(self) -> bool:
        """This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent val"""
    def isTrackingTopology(self) -> bool:
        """Introduced in 2019.0"""
    def isTransparent(self) -> bool:
        """Indicates that this locator uses transparency during draw() method calls."""
    def legalConnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal connections being made to attributes of this node."""
    def legalDisconnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal disconnections being made to attributes of this node."""
    def name(self) -> str:
        """Returns the name of this particular instance of this class."""
    def passThroughToMany(self) -> bool:
        """This method is overridden by nodes that want to control the traversal behavior of some Maya search algorithms which trav"""
    def passThroughToOne(self) -> MPlug:
        """This method may be overridden by nodes that have a one-to-one relationship between an input attribute and a correspondin"""
    def postConstructor(self) -> None:
        """Post constructor."""
    def postEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode, evalType: Any) -> MStatus:
        """Clean up node's internal state after threaded evaluation."""
    def preEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode) -> MStatus:
        """Prepare a node's internal state for threaded evaluation."""
    def schedulingType(self) -> Any:
        """When overridden this method controls the degree of parallelism supported by the node during threaded evaluation."""
    def setDependentsDirty(self, plug: MPlug, plugArray: MPlugArray) -> MStatus:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug """
    def setExistWithoutInConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without input connections."""
    def setExistWithoutOutConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without output connections."""
    def setExternalContent(self) -> None:
        """Changes the location of external content in batch."""
    def setExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Sets content info in the specified attribute from the table."""
    def setInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def shouldSave(self, isSaving: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def thisMObject(self) -> MObject:
        """Returns the MObject associated with this user defined node."""
    def transformInvalidationRange(self, source: MPlug, input: MTimeRange) -> MTimeRange:
        """Introduced in 2020.0"""
    def type(self) -> int:
        """This method returns the type of the node."""
    def typeId(self) -> MTypeId:
        """Returns the TYPEID of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""
    def useClosestPointForSelection(self) -> bool:
        """Determines whether Maya should call closestPoint() when doing single selection."""

class MPxManipContainer:
    caching: Any
    frozen: Any
    isHistoricallyInteresting: Any
    kAssembly: Any
    kBlendShape: Any
    kCameraSetNode: Any
    kCircleSweepManip: Any
    kClientDeviceNode: Any
    kConstraintNode: Any
    kCurveSegmentManip: Any
    kCustomManip: Any
    kDefaultScheduling: Any
    kDeformerNode: Any
    kDependNode: Any
    kDirectionManip: Any
    kDiscManip: Any
    kDistanceManip: Any
    kEmitterNode: Any
    kEvaluatedDirectly: Any
    kEvaluatedIndirectly: Any
    kFieldNode: Any
    kFluidEmitterNode: Any
    kFreePointTriadManip: Any
    kGeometryFilter: Any
    kGloballySerial: Any
    kGloballySerialize: Any
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
    kParallel: Any
    kParticleAttributeMapperNode: Any
    kPointOnCurveManip: Any
    kPointOnSurfaceManip: Any
    kPostEvaluationTypeLast: Any
    kSchedulingTypeLast: Any
    kSerial: Any
    kSerialize: Any
    kSkinCluster: Any
    kSpringNode: Any
    kStateManip: Any
    kSurfaceShape: Any
    kThreadedDeviceNode: Any
    kToggleManip: Any
    kTransformNode: Any
    kUntrusted: Any
    message: Any
    state: Any
    thisown: Any
    def __init__(self) -> None:
        """Constructor."""
    @staticmethod
    def addAttribute(attr: MObject) -> MStatus:
        """This method adds a new attribute to a user defined node type during the type's initialization."""
    def addCircleSweepManip(self, manipName: str, angleName: str) -> MDagPath:
        """This method creates a CircleSweepManip and adds it to the MPxManipContainer container."""
    def addCurveSegmentManip(self, manipName: str, startParamName: str, endParamName: str) -> MDagPath:
        """This method creates a CurveSegmentManip and adds it to the MPxManipContainer container."""
    def addDirectionManip(self, manipName: str, directionName: str) -> MDagPath:
        """This method creates a DirectionManip and adds it to the MPxManipContainer container."""
    def addDiscManip(self, manipName: str, angleName: str) -> MDagPath:
        """This method creates a DiscManip and adds it to the MPxManipContainer container."""
    def addDistanceManip(self, manipName: str, distanceName: str) -> MDagPath:
        """This method creates a DistanceManip and adds it to the MPxManipContainer container."""
    def addExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Adds content info to the specified table from a file path attribute."""
    def addFreePointTriadManip(self, manipName: str, pointName: str) -> MDagPath:
        """This method creates a FreePointTriadManip and adds it to the MPxManipContainer container."""
    def addMPxManipulatorNode(self, manipTypeName: str, manipName: str, proxyManip: MPxManipulatorNode) -> MStatus:
        """This method creates a custom MPxManipulatorNode and adds it to the MPxManipContainer container."""
    def addManipToPlugConversion(self, plug: MPlug) -> int:
        """This method adds a manipulator to plug converter for the specified plug."""
    def addPlugToInViewEditor(self, plug: MPlug) -> None:
        """Adds a plug to the In-View Editor."""
    def addPlugToManipConversion(self, manipIndex: int) -> None:
        """This method adds a plug to manipulator converter for the specified manipulator value (e.g."""
    def addPointOnCurveManip(self, manipName: str, paramName: str) -> MDagPath:
        """This method creates a PointOnCurveManip and adds it to the MPxManipContainer container."""
    def addPointOnSurfaceManip(self, manipName: str, paramName: str) -> MDagPath:
        """This method creates a PointOnSurfaceManip and adds it to the MPxManipContainer container."""
    def addRotateManip(self, manipName: str, rotationName: str) -> MDagPath:
        """This method creates a rotate manipulator and adds it to the MPxManipContainer container."""
    def addScaleManip(self, manipName: str, scaleName: str) -> MDagPath:
        """This method creates a scale manipulator and adds it to the MPxManipContainer container."""
    def addStateManip(self, manipName: str, stateName: str) -> MDagPath:
        """This method creates a StateManip and adds it to the MPxManipContainer container."""
    @staticmethod
    def addToManipConnectTable() -> MStatus:
        """This method adds the user defined node as an entry in the manipConnectTable so that when this node is selected the user """
    def addToggleManip(self, manipName: str, toggleName: str) -> MDagPath:
        """This method creates a ToggleManip and adds it to the MPxManipContainer container."""
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> MStatus: ...
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject, affectsTopology: bool) -> MStatus:
        """This method specifies that a particular input attribute affects a specific output attribute."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def compute(self) -> MStatus:
        """This method should be overridden in user defined nodes."""
    def configCache(self) -> None:
        """Introduced in 2020.0"""
    def connectToDependNode(self, dependNode: MObject) -> MStatus:
        """This method connects the manipulator to the dependency node."""
    def connectionBroken(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are made to attributes of this node."""
    def copyInternalData(self) -> None:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def createChildren(self) -> MStatus:
        """This method should be overridden in user defined manipulators."""
    def dependsOn(self, depends: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def doDrag(self) -> MStatus:
        """This method gets called when the manipulator receives a mouse drag event."""
    def doPress(self) -> MStatus:
        """This method gets called when the manipulator receives a mouse down event."""
    def doRelease(self) -> MStatus:
        """This method gets called when the manipulator receives a mouse release event."""
    def draw(self, view: M3dView, path: MDagPath, style: int, status: int) -> None:
        """This method can be overloaded to customize the drawing of the child manipulators."""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    def finishAddingManips(self) -> MStatus:
        """This method should be called from the user-defined manipulator plug-in near the end of the connectToDependNode method so"""
    def getCacheSetup(self) -> None:
        """Introduced in 2020.0"""
    @overload
    def getConverterManipValue(self, manipIndex: int, value: int) -> MStatus: ...
    @overload
    def getConverterManipValue(self, manipIndex: int, value: float) -> MStatus: ...
    @overload
    def getConverterManipValue(self, manipIndex: int, x: float, y: float) -> MStatus: ...
    @overload
    def getConverterManipValue(self, manipIndex: int, point: MPoint) -> MStatus: ...
    @overload
    def getConverterManipValue(self, manipIndex: int, vector: MVector) -> MStatus: ...
    @overload
    def getConverterManipValue(self, manipIndex: int, matrix: MMatrix) -> MStatus: ...
    @overload
    def getConverterManipValue(self, manipIndex: int, rotation: MEulerRotation) -> MStatus: ...
    @overload
    def getConverterManipValue(self, manipIndex: int, xform: MTransformationMatrix) -> MStatus:
        """This method retrieves the value of a converterManipValue of type unsigned int at a given index from the converter."""
    @overload
    def getConverterPlugValue(self, plugIndex: int, value: float) -> MStatus: ...
    @overload
    def getConverterPlugValue(self, plugIndex: int, x: float, y: float) -> MStatus: ...
    @overload
    def getConverterPlugValue(self, plugIndex: int, point: MPoint) -> MStatus: ...
    @overload
    def getConverterPlugValue(self, plugIndex: int, vector: MVector) -> MStatus: ...
    @overload
    def getConverterPlugValue(self, plugIndex: int, matrix: MMatrix) -> MStatus: ...
    @overload
    def getConverterPlugValue(self, plugIndex: int, rotation: MEulerRotation) -> MStatus:
        """This method retrieves the value of a converterPlugValue of type double at a given index from the converter."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> None:
        """Returns the external content (files) that this node depends on."""
    def getFilesToArchive(self, shortName: bool = False, unresolvedName: bool = False, markCouldBeImageSequence: bool = False) -> Any:
        """Use this method to return all external files used by this node."""
    def getInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def getInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def hasInvalidationRangeTransformation(self) -> bool:
        """Introduced in 2020.0"""
    @staticmethod
    def inheritAttributesFrom(parentClassName: str) -> MStatus:
        """This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node."""
    @staticmethod
    def initialize() -> MStatus:
        """This method initializes the manipulator, and should be overriden in user-defined manipulators."""
    @overload
    def internalArrayCount(self) -> int: ...
    @overload
    def internalArrayCount(self) -> int:
        """This method is overridden by nodes that have internal array attributes which are not stored in Maya's datablock."""
    def isAbstractClass(self) -> bool:
        """Override this class to return true if this node is an abstract node."""
    def isManipActive(self, manipType: int, manipObject: MObject) -> bool:
        """This method determines if custom manip is active &amp; gets the current manip object."""
    def isPassiveOutput(self) -> bool:
        """This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent val"""
    def isTrackingTopology(self) -> bool:
        """Introduced in 2019.0"""
    def legalConnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal connections being made to attributes of this node."""
    def legalDisconnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal disconnections being made to attributes of this node."""
    def manipToPlugConversion(self, manipIndex: int) -> Any:
        """This virtual method calculates and returns the requested plug value, based upon the container's manipulator values."""
    def name(self) -> str:
        """Returns the name of this particular instance of this class."""
    @staticmethod
    def newManipulator(manipName: str, manipObject: MObject) -> MPxManipContainer:
        """This static function is used to create a user-defined manipulator."""
    def passThroughToMany(self) -> bool:
        """This method is overridden by nodes that want to control the traversal behavior of some Maya search algorithms which trav"""
    def passThroughToOne(self) -> MPlug:
        """This method may be overridden by nodes that have a one-to-one relationship between an input attribute and a correspondin"""
    def plugToManipConversion(self, manipIndex: int) -> Any:
        """This virtual method calculates and returns the requested manipulator value, based upon the values of plugs on the nodes """
    def postConstructor(self) -> None:
        """Post constructor."""
    def postEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode, evalType: Any) -> MStatus:
        """Clean up node's internal state after threaded evaluation."""
    def preEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode) -> MStatus:
        """Prepare a node's internal state for threaded evaluation."""
    @staticmethod
    def removeFromManipConnectTable() -> MStatus:
        """This method removes the user defined node entry from the manipConnectTable."""
    def schedulingType(self) -> Any:
        """When overridden this method controls the degree of parallelism supported by the node during threaded evaluation."""
    def setDependentsDirty(self, plug: MPlug, plugArray: MPlugArray) -> MStatus:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug """
    def setExistWithoutInConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without input connections."""
    def setExistWithoutOutConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without output connections."""
    def setExternalContent(self) -> None:
        """Changes the location of external content in batch."""
    def setExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Sets content info in the specified attribute from the table."""
    def setInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def shouldSave(self, isSaving: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def thisMObject(self) -> MObject:
        """Introduced in 2020.0"""
    def transformInvalidationRange(self, source: MPlug, input: MTimeRange) -> MTimeRange:
        """Introduced in 2020.0"""
    def type(self) -> int:
        """This method returns the type of the node."""
    def typeId(self) -> MTypeId:
        """Returns the TYPEID of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""

class MPxManipulatorNode:
    caching: Any
    connectedNodes: Any
    frozen: Any
    isHistoricallyInteresting: Any
    kAssembly: Any
    kBlendShape: Any
    kCameraSetNode: Any
    kClientDeviceNode: Any
    kConstraintNode: Any
    kDefaultScheduling: Any
    kDeformerNode: Any
    kDependNode: Any
    kEmitterNode: Any
    kEvaluatedDirectly: Any
    kEvaluatedIndirectly: Any
    kFieldNode: Any
    kFluidEmitterNode: Any
    kGeometryFilter: Any
    kGloballySerial: Any
    kGloballySerialize: Any
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
    kParallel: Any
    kParticleAttributeMapperNode: Any
    kPostEvaluationTypeLast: Any
    kSchedulingTypeLast: Any
    kSerial: Any
    kSerialize: Any
    kSkinCluster: Any
    kSpringNode: Any
    kSurfaceShape: Any
    kThreadedDeviceNode: Any
    kTransformNode: Any
    kUntrusted: Any
    message: Any
    state: Any
    thisown: Any
    def __init__(self) -> None:
        """Class constructor."""
    @staticmethod
    def addAttribute(attr: MObject) -> MStatus:
        """This method adds a new attribute to a user defined node type during the type's initialization."""
    def addDependentPlug(self, plug: MPlug) -> MStatus:
        """This method adds the plug to the list of those to be keyframed."""
    def addDoubleValue(self, valueName: str, defaultValue: float, valueIndex: int) -> MStatus:
        """Manipulators which call connectPlugToValue() must first create the value on the node."""
    def addExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Adds content info to the specified table from a file path attribute."""
    def addPointValue(self, valueName: str, defaultValue: MPoint, valueIndex: int) -> MStatus:
        """Manipulators which call connectPlugToValue() must first create the value on the node."""
    def addVectorValue(self, valueName: str, defaultValue: MVector, valueIndex: int) -> MStatus:
        """Manipulators which call connectPlugToValue() must first create the value on the node."""
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> MStatus: ...
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject, affectsTopology: bool) -> MStatus:
        """This method specifies that a particular input attribute affects a specific output attribute."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def colorAndName(self, view: M3dView, glName: Any, glNameIsPickable: bool, colorIndex: Any) -> MStatus:
        """This method is used to set the color of the GL component that is being drawn next."""
    def compute(self) -> MStatus:
        """This method should be overridden in user defined nodes."""
    def configCache(self) -> None:
        """Introduced in 2020.0"""
    def connectPlugToValue(self, plug: MPlug, valueIndex: int, plugIndex: int) -> MStatus:
        """This method is called in the connectToDependNode() virtual if it is implemented for the custom manipulator."""
    def connectToDependNode(self, dependNode: MObject) -> MStatus:
        """This method connects the manipulator to the dependency node."""
    def connectionBroken(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are made to attributes of this node."""
    def copyInternalData(self) -> None:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def dependentPlugsReset(self) -> MStatus:
        """This method resets the list of dependent plugs for this manipulator."""
    def dependsOn(self, depends: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def deregisterForMouseMove(self) -> MStatus:
        """This method deregisters this manipulator from receiving mouse move events."""
    def dimmedColor(self) -> Any:
        """This method returns the color index for a dimmed or unselectable component."""
    def doDrag(self, view: M3dView) -> MStatus:
        """This method gets called when the manipulator receives a mouse drag event."""
    def doMove(self, view: M3dView, refresh: bool) -> MStatus:
        """This method gets called when the manipulator receives a mouse move event, if the manipulator registered for mouse move e"""
    def doPress(self, view: M3dView) -> MStatus:
        """This method gets called when the manipulator receives a mouse down event."""
    def doRelease(self, view: M3dView) -> MStatus:
        """This method gets called when the manipulator receives a mouse release event."""
    def draw(self, view: M3dView, path: MDagPath, style: int, status: int) -> None:
        """This method is overloaded to draw the manipulators."""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    def finishAddingManips(self) -> MStatus:
        """This method should be called from the user-defined manipulator plug-in near the end of the connectToDependNode method so"""
    def getCacheSetup(self) -> None:
        """Introduced in 2020.0"""
    def getDoubleValue(self, valueIndex: int, previousValue: bool, value: float) -> MStatus:
        """This method is used for getting a double value associated with the manipulator."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> None:
        """Returns the external content (files) that this node depends on."""
    def getFilesToArchive(self, shortName: bool = False, unresolvedName: bool = False, markCouldBeImageSequence: bool = False) -> Any:
        """Use this method to return all external files used by this node."""
    def getInstancePtr(self, *args: Any, **kwargs: Any) -> Any: ...
    def getInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def getInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def getPointValue(self, valueIndex: int, previousValue: bool, value: MPoint) -> MStatus:
        """This method is used for getting a MPoint value associated with the manipulator."""
    def getVectorValue(self, valueIndex: int, previousValue: bool, value: MVector) -> MStatus:
        """This method is used for getting a MVector value associated with the manipulator."""
    def glActiveName(self, glName: Any) -> MStatus:
        """This method returns the unsigned int value which specifies the current active handle."""
    def glFirstHandle(self, firstHandle: Any) -> MStatus:
        """This method is used to find the unsigned int value that should be used for the first GL handle."""
    def hasInvalidationRangeTransformation(self) -> bool:
        """Introduced in 2020.0"""
    @staticmethod
    def inheritAttributesFrom(parentClassName: str) -> MStatus:
        """This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node."""
    @overload
    def internalArrayCount(self) -> int: ...
    @overload
    def internalArrayCount(self) -> int:
        """This method is overridden by nodes that have internal array attributes which are not stored in Maya's datablock."""
    def isAbstractClass(self) -> bool:
        """Override this class to return true if this node is an abstract node."""
    def isPassiveOutput(self) -> bool:
        """This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent val"""
    def isTrackingTopology(self) -> bool:
        """Introduced in 2019.0"""
    def labelBackgroundColor(self) -> Any:
        """This method returns the color index of a label background."""
    def labelColor(self) -> Any:
        """This method returns the color index of a label."""
    def legalConnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal connections being made to attributes of this node."""
    def legalDisconnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal disconnections being made to attributes of this node."""
    def lineColor(self) -> Any:
        """This method returns the color index of a line."""
    def mainColor(self) -> Any:
        """This method returns the main color index."""
    def mouseDown(self, x_pos: Any, y_pos: Any) -> MStatus:
        """This method returns the mouse down position within a view."""
    def mousePosition(self, x_pos: Any, y_pos: Any) -> MStatus:
        """This method returns the current mouse position within a view."""
    def mouseRay(self, linePoint: MPoint, lineDirection: MVector) -> MStatus:
        """This method returns the location of the mouse within a view."""
    def mouseRayWorld(self, linePoint: MPoint, lineDirection: MVector) -> MStatus:
        """This method returns the location of the mouse within a view."""
    def mouseUp(self, x_pos: Any, y_pos: Any) -> MStatus:
        """This method returns the mouse up position within a view."""
    def name(self) -> str:
        """Returns the name of this particular instance of this class."""
    @staticmethod
    def newManipulator(manipName: str, manipObject: MObject) -> MPxManipulatorNode:
        """This static function is used to create a user-defined manipulator."""
    def passThroughToMany(self) -> bool:
        """This method is overridden by nodes that want to control the traversal behavior of some Maya search algorithms which trav"""
    def passThroughToOne(self) -> MPlug:
        """This method may be overridden by nodes that have a one-to-one relationship between an input attribute and a correspondin"""
    def postConstructor(self) -> None:
        """Post constructor."""
    def postEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode, evalType: Any) -> MStatus:
        """Clean up node's internal state after threaded evaluation."""
    def preEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode) -> MStatus:
        """Prepare a node's internal state for threaded evaluation."""
    def prevColor(self) -> Any:
        """This method returns the previously color used by the colorAndName() method."""
    def registerForMouseMove(self) -> MStatus:
        """This method registers this manipulator to receive mouse move events."""
    def schedulingType(self) -> Any:
        """When overridden this method controls the degree of parallelism supported by the node during threaded evaluation."""
    def selectedColor(self) -> Any:
        """This method returns the color index of a selected component."""
    def setDependentsDirty(self, plug: MPlug, plugArray: MPlugArray) -> MStatus:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug """
    def setDoubleValue(self, valueIndex: int, value: float) -> MStatus:
        """This method is used for setting a double value associated with the manipulator."""
    def setExistWithoutInConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without input connections."""
    def setExistWithoutOutConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without output connections."""
    def setExternalContent(self) -> None:
        """Changes the location of external content in batch."""
    def setExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Sets content info in the specified attribute from the table."""
    def setHandleColor(self, drawManager: int, handleName: int, colorIndex: Any) -> MStatus:
        """This method is used to set the color of component that is being drawn next."""
    def setInstancePtr(self, *args: Any, **kwargs: Any) -> Any: ...
    def setInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def setPointValue(self, valueIndex: int, value: MPoint) -> MStatus:
        """This method is used for setting an MPoint value associated with the manipulator."""
    def setVectorValue(self, valueIndex: int, value: MVector) -> MStatus:
        """This method is used for setting a MVector value associated with the manipulator."""
    def shouldDrawHandleAsSelected(self, name: int, useSelectedColor: bool) -> MStatus:
        """Deprecated in 2019.0"""
    def shouldSave(self, isSaving: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def thisMObject(self) -> MObject:
        """Returns the MObject associated with this user defined node."""
    def transformInvalidationRange(self, source: MPlug, input: MTimeRange) -> MTimeRange:
        """Introduced in 2020.0"""
    def type(self) -> Any:
        """Returns the type of node that this is."""
    def typeId(self) -> MTypeId:
        """Returns the TYPEID of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""
    def xColor(self) -> Any:
        """This method returns the color index of the x axis."""
    def yColor(self) -> Any:
        """This method returns the color index of the y axis."""
    def zColor(self) -> Any:
        """This method returns the color index of the z axis."""

class MPxMaterialInformation:
    kOverrideDraw: Any
    kSimpleMaterial: Any
    kTexture: Any
    thisown: Any
    @overload
    def __init__(self, materialNode: MObject) -> None: ...
    @overload
    def __init__(self) -> None:
        """Constructor."""
    def computeMaterial(self, data: MaterialInputData) -> bool:
        """Compute the material properties/information for the shader."""
    def connectAsTexture(self, plug: MPlug) -> bool:
        """Called by Maya to when an incoming connection is made to plug on the shader."""
    def materialInfoIsDirty(self, plug: MPlug) -> bool:
        """Called by Maya to when a plug on the shader has been changed."""
    def textureDisconnected(self, plug: MPlug) -> bool:
        """Called whenever an incoming connection to the shader is broken."""
    def useMaterialAsTexture(self) -> bool:
        """Tells Maya whether to this material should be displayed as a texture, ie whether it should be baked."""

class MPxMayaAsciiFilter:
    kCouldBeMyFileType: Any
    kExportAccessMode: Any
    kExportActiveAccessMode: Any
    kImportAccessMode: Any
    kIsMyFileType: Any
    kNotMyFileType: Any
    kOpenAccessMode: Any
    kReferenceAccessMode: Any
    kSaveAccessMode: Any
    kUnknownAccessMode: Any
    thisown: Any
    def __init__(self) -> None:
        """The class constructor."""
    def allowMultipleFileOptimization(self, *args: Any, **kwargs: Any) -> Any: ...
    def canBeOpened(self) -> bool:
        """This routine is called by Maya while it is executing in the MPxFileTranslator constructor."""
    def defaultExtension(self) -> str:
        """This routine is called by Maya whenever it needs to know the default extension of a translator."""
    @staticmethod
    def fileAccessMode() -> int:
        """This routine returns the fileAccess mode maya is currently in."""
    def filter(self) -> str:
        """This virtual method may be overloaded in a derived class to set the filter extension that will be used by the file dialo"""
    def haveNamespaceSupport(self) -> bool:
        """When a file is imported or referenced into an existing scene, there is the possibility that nodes in the incoming file w"""
    def haveReadMethod(self) -> bool:
        """Overrides MPxFileTranslator::haveReadMethod() to indicate that this translator has a read method."""
    def haveReferenceMethod(self) -> bool:
        """This method is called by Maya to see if the translator implements its own custom file referencing."""
    def haveWriteMethod(self) -> bool:
        """Overrides MPxFileTranslator::haveWriteMethod() to indicate that this translator has a write method."""
    def identifyFile(self, file: MFileObject, buffer: str, size: Any) -> int:
        """This routine is called by Maya when a file selection dialog accesses a new directory."""
    def processReadOptions(self, optionsString: str) -> MStatus:
        """Allows the translator to handle any options passed into the reader() method, above."""
    def processWriteOptions(self, optionsString: str) -> MStatus:
        """Allows the translator to handle any options passed into the reader() method, above."""
    def reader(self, file: MFileObject, optionsString: str, mode: Any) -> MStatus:
        """Reader method for the ascii filter translator."""
    def writePostConnectAttrsBlock(self, fileIO: MPxMayaAsciiFilterOutput) -> MStatus:
        """Allows data to be written out to the file after the connect attrs block."""
    def writePostCreateNodesBlock(self, fileIO: MPxMayaAsciiFilterOutput) -> MStatus:
        """Allows data to be written out to the file after the create nodes block."""
    def writePostHeader(self, fileIO: MPxMayaAsciiFilterOutput) -> MStatus:
        """Allows data to be written out to the file after the header block."""
    def writePostRequires(self, fileIO: MPxMayaAsciiFilterOutput) -> MStatus:
        """Allows data to be written out to the file after the requires block."""
    def writePreConnectAttrsBlock(self, fileIO: MPxMayaAsciiFilterOutput) -> MStatus:
        """Allows data to be written out to the file before the connect attrs block."""
    def writePreCreateNodesBlock(self, fileIO: MPxMayaAsciiFilterOutput) -> MStatus:
        """Allows data to be written out to the file before the create nodes block."""
    def writePreTrailer(self, fileIO: MPxMayaAsciiFilterOutput) -> MStatus:
        """Allows data to be written out to the file before the trailer block."""
    def writer(self, file: MFileObject, optionsString: str, mode: Any) -> MStatus:
        """Writer method for the ascii filter translator."""
    def writesConnectAttr(self, srcPlug: MPlug, destPlug: MPlug) -> bool:
        """Determines if a "connectAttr" command should be written for a particular node."""
    def writesCreateNode(self, node: MObject) -> bool:
        """Determines if a "createNode" command should be written for a particular node."""
    def writesDisconnectAttr(self, srcPlug: MPlug, destPlug: MPlug) -> bool:
        """Determines if a "disconnectAttr" command should be written for a particular connection."""
    def writesFileReference(self, referenceFile: MFileObject) -> bool:
        """Determines if a "fileReference" command should be written for a file."""
    def writesMetadata(self) -> bool:
        """Asserts that "dataStructure/addMetadata/applyMetadata" commands should be written in the file."""
    def writesParentNode(self, parent: MDagPath, child: MDagPath) -> bool:
        """Determines if a "parent" command should be written for a particular parent and child."""
    def writesRequirements(self) -> bool:
        """Determines if "requires" commands should be written in the file."""
    def writesSelectNode(self, node: MObject) -> bool:
        """Determines if a "select" command should be written for a particular node."""
    def writesSetAttr(self, srcPlug: MPlug) -> bool:
        """Determines if a "setAttr" command should be written for a particular node."""

class MPxMayaAsciiFilterOutput:
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class MPxMidiInputDevice:
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def closeDevice(self) -> None:
        """Close the midi device."""
    def deviceState(self) -> Any:
        """Return the current state of the input device."""
    def doButtonEvents(self, arg: Any = True) -> None:
        """This method is used to specify whether this device is accepting button events from its child."""
    def doMovementEvents(self, arg: Any = True) -> None:
        """This method is used to specify whether this device is accepting movement input from its child."""
    def getMessage(self, messageType: Any, messageResponse: str) -> str:
        """User should override this method."""
    def nameAxes(self) -> None:
        """Assign names to the axes of the device."""
    def nameButtons(self) -> None:
        """Assign names to the buttons of the device."""
    def openDevice(self) -> MStatus:
        """Open the midi device."""
    def sendMessage(self, messageType: Any, messageParams: Any) -> MStatus:
        """If this midi event belongs to this device then fiil up the MDeviceState ."""

class MPxModelEditorCommand:
    thisown: Any
    def __init__(self) -> None:
        """Class constructor."""
    def appendSyntax(self) -> MStatus:
        """This method should be overridden to append syntax to the panel command."""
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def doEditFlags(self) -> MStatus:
        """This method is called when the command is called in edit mode."""
    def doQueryFlags(self) -> MStatus:
        """This method is called when the command is called in query mode."""
    def editorCommandName(self) -> str:
        """Returns the name of editor command."""
    def editorMenuScriptName(self) -> str:
        """Returns the name of the script that should get executed to construct the menu for the editor."""
    def makeModelView(self) -> MPx3dModelView:
        """This method is called when the modelEditor is being created and it can be overriden to allow the user to handle the allo"""
    def modelView(self) -> MPx3dModelView:
        """Returns a pointer to the MPx3dModelView created by this command."""
    @overload
    def setResult(self, result: bool) -> MStatus: ...
    @overload
    def setResult(self, result: int) -> MStatus: ...
    @overload
    def setResult(self, result: float) -> MStatus: ...
    @overload
    def setResult(self, result: str) -> MStatus: ...
    @overload
    def setResult(self, result: Any) -> MStatus: ...
    @overload
    def setResult(self, result: MDoubleArray) -> MStatus: ...
    @overload
    def setResult(self, result: MIntArray) -> MStatus:
        """This method should be called when the result of the panel command is a boolean."""
    def skipFlagForCreate(self, longFlag: str) -> bool:
        """Returns true if the passed long flag name should be skipped during the creation portion of the command."""

class MPxMotionPathNode:
    allCoordinates: Any
    bank: Any
    bankScale: Any
    bankThreshold: Any
    caching: Any
    flowNode: Any
    follow: Any
    fractionMode: Any
    frontAxis: Any
    frontTwist: Any
    frozen: Any
    inverseFront: Any
    inverseUp: Any
    isHistoricallyInteresting: Any
    kAssembly: Any
    kBlendShape: Any
    kCameraSetNode: Any
    kClientDeviceNode: Any
    kConstraintNode: Any
    kDefaultScheduling: Any
    kDeformerNode: Any
    kDependNode: Any
    kEmitterNode: Any
    kEvaluatedDirectly: Any
    kEvaluatedIndirectly: Any
    kFieldNode: Any
    kFluidEmitterNode: Any
    kGeometryFilter: Any
    kGloballySerial: Any
    kGloballySerialize: Any
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
    kParallel: Any
    kParticleAttributeMapperNode: Any
    kPostEvaluationTypeLast: Any
    kSchedulingTypeLast: Any
    kSerial: Any
    kSerialize: Any
    kSkinCluster: Any
    kSpringNode: Any
    kSurfaceShape: Any
    kThreadedDeviceNode: Any
    kTransformNode: Any
    kUntrusted: Any
    kUpNormal: Any
    kUpObject: Any
    kUpObjectRotation: Any
    kUpScene: Any
    kUpVector: Any
    message: Any
    normal: Any
    orientMatrix: Any
    orientationMarkerTime: Any
    pathGeometry: Any
    positionMarkerTime: Any
    rotate: Any
    rotateOrder: Any
    rotateX: Any
    rotateY: Any
    rotateZ: Any
    sideTwist: Any
    state: Any
    thisown: Any
    uValue: Any
    upAxis: Any
    upTwist: Any
    updateOrientationMarkers: Any
    worldUpMatrix: Any
    worldUpType: Any
    worldUpVector: Any
    worldUpVectorX: Any
    worldUpVectorY: Any
    worldUpVectorZ: Any
    xCoordinate: Any
    yCoordinate: Any
    zCoordinate: Any
    def __init__(self) -> None:
        """Class constructor."""
    @staticmethod
    def addAttribute(attr: MObject) -> MStatus:
        """This method adds a new attribute to a user defined node type during the type's initialization."""
    def addExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Adds content info to the specified table from a file path attribute."""
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> MStatus: ...
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject, affectsTopology: bool) -> MStatus:
        """This method specifies that a particular input attribute affects a specific output attribute."""
    def banking(self, data: MDataBlock, f: float, worldUp: MVector, bankScale: float, bankLimit: float) -> MQuaternion:
        """Calculate the banking on the motion path at the fractional distance `frac' along the path."""
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def compute(self) -> MStatus:
        """This method should be overridden in user defined nodes."""
    def configCache(self) -> None:
        """Introduced in 2020.0"""
    def connectionBroken(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are made to attributes of this node."""
    def copyInternalData(self) -> None:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def dependsOn(self, depends: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def evaluatePath(self, data: MDataBlock, u: float, uRange: float, wraparound: bool, sideOffset: float, upOffset: float, follow: bool, inverseFront: bool, inverseUp: bool, frontAxis: int, upAxis: int, frontTwist: float, upTwist: float, sideTwist: float, bank: bool, bankScale: float, bankLimit: float, resultPosition: MPoint, resultOrientation: MMatrix) -> MStatus:
        """Callable from your custom plug-ins compute() method to evaluate the path at the specified location."""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    def fractionalToParametric(self, f: float) -> float:
        """Converts a fractional location on the path curve to the corresponding parametric location."""
    def getCacheSetup(self) -> None:
        """Introduced in 2020.0"""
    def getExternalContent(self, table: MExternalContentInfoTable) -> None:
        """Returns the external content (files) that this node depends on."""
    def getFilesToArchive(self, shortName: bool = False, unresolvedName: bool = False, markCouldBeImageSequence: bool = False) -> Any:
        """Use this method to return all external files used by this node."""
    def getInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def getInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def getVectors(self, data: MDataBlock, f: float, front: MVector, side: MVector, up: MVector, worldUp: MVector | None = None) -> MStatus:
        """Calculate the orientation on the motion path at the fractional distance `frac' along the path."""
    def hasInvalidationRangeTransformation(self) -> bool:
        """Introduced in 2020.0"""
    @staticmethod
    def inheritAttributesFrom(parentClassName: str) -> MStatus:
        """This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node."""
    @overload
    def internalArrayCount(self) -> int: ...
    @overload
    def internalArrayCount(self) -> int:
        """This method is overridden by nodes that have internal array attributes which are not stored in Maya's datablock."""
    def isAbstractClass(self) -> bool:
        """Override this class to return true if this node is an abstract node."""
    def isPassiveOutput(self) -> bool:
        """This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent val"""
    def isTrackingTopology(self) -> bool:
        """Introduced in 2019.0"""
    def legalConnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal connections being made to attributes of this node."""
    def legalDisconnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal disconnections being made to attributes of this node."""
    def matrix(self, front: MVector, side: MVector, up: MVector, frontAxisIdx: int = 1, upAxisIdx: int = 2) -> MMatrix:
        """Create a matrix given vector space specified by the three orthogonal input vectors."""
    def name(self) -> str:
        """Returns the name of this particular instance of this class."""
    def parametricToFractional(self, u: float) -> float:
        """Converts a parametric location on the path curve to the corresponding fraction of the total path curve length."""
    def passThroughToMany(self) -> bool:
        """This method is overridden by nodes that want to control the traversal behavior of some Maya search algorithms which trav"""
    def passThroughToOne(self) -> MPlug:
        """This method may be overridden by nodes that have a one-to-one relationship between an input attribute and a correspondin"""
    def position(self, data: MDataBlock, f: float) -> MPoint:
        """This method returns the position on the path associated with the motionPath node at a specified fractional distance alon"""
    def postConstructor(self) -> None:
        """Post constructor."""
    def postEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode, evalType: Any) -> MStatus:
        """Clean up node's internal state after threaded evaluation."""
    def preEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode) -> MStatus:
        """Prepare a node's internal state for threaded evaluation."""
    def schedulingType(self) -> Any:
        """When overridden this method controls the degree of parallelism supported by the node during threaded evaluation."""
    def setDependentsDirty(self, plug: MPlug, plugArray: MPlugArray) -> MStatus:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug """
    def setExistWithoutInConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without input connections."""
    def setExistWithoutOutConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without output connections."""
    def setExternalContent(self) -> None:
        """Changes the location of external content in batch."""
    def setExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Sets content info in the specified attribute from the table."""
    def setInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def shouldSave(self, isSaving: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def thisMObject(self) -> MObject:
        """Returns the MObject associated with this user defined node."""
    def transformInvalidationRange(self, source: MPlug, input: MTimeRange) -> MTimeRange:
        """Introduced in 2020.0"""
    def type(self) -> int:
        """Returns the type of node that this is."""
    def typeId(self) -> MTypeId:
        """Returns the TYPEID of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""
    def wraparoundFractionalValue(self, f: float) -> float:
        """Given the fractional distance `frac' along the path, this method checks if the value goes beyond the 0 to 1 range and if"""

class MPxMultiPolyTweakUVCommand:
    kDouble: Any
    kLong: Any
    kNoArg: Any
    kString: Any
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def appendToResult(self, *args: Any, **kwargs: Any) -> Any: ...
    def className(self, *args: Any, **kwargs: Any) -> Any: ...
    def clearResult(self, *args: Any, **kwargs: Any) -> Any: ...
    def commandString(self, *args: Any, **kwargs: Any) -> Any: ...
    def currentDoubleResult(self, *args: Any, **kwargs: Any) -> Any: ...
    def currentIntResult(self, *args: Any, **kwargs: Any) -> Any: ...
    def currentResultType(self, *args: Any, **kwargs: Any) -> Any: ...
    def currentStringResult(self, *args: Any, **kwargs: Any) -> Any: ...
    def displayError(self, *args: Any, **kwargs: Any) -> Any: ...
    def displayInfo(self, *args: Any, **kwargs: Any) -> Any: ...
    def displayWarning(self, *args: Any, **kwargs: Any) -> Any: ...
    def doIt(self, *args: Any, **kwargs: Any) -> Any: ...
    def getCurrentResult(self, *args: Any, **kwargs: Any) -> Any: ...
    def getTweakedUVs(self, *args: Any, **kwargs: Any) -> Any: ...
    def hasSyntax(self, *args: Any, **kwargs: Any) -> Any: ...
    def isCurrentResultArray(self, *args: Any, **kwargs: Any) -> Any: ...
    def isHistoryOn(self, *args: Any, **kwargs: Any) -> Any: ...
    def isUndoable(self, *args: Any, **kwargs: Any) -> Any: ...
    def newSyntax(self, *args: Any, **kwargs: Any) -> Any: ...
    def parseSyntax(self, *args: Any, **kwargs: Any) -> Any: ...
    def preProcessUVs(self, *args: Any, **kwargs: Any) -> Any: ...
    def redoIt(self, *args: Any, **kwargs: Any) -> Any: ...
    def setCommandString(self, *args: Any, **kwargs: Any) -> Any: ...
    def setHistoryOn(self, *args: Any, **kwargs: Any) -> Any: ...
    def setResult(self, *args: Any, **kwargs: Any) -> Any: ...
    def setUndoable(self, *args: Any, **kwargs: Any) -> Any: ...
    def syntax(self, *args: Any, **kwargs: Any) -> Any: ...
    def undoIt(self, *args: Any, **kwargs: Any) -> Any: ...

class MPxNode:
    caching: Any
    frozen: Any
    isHistoricallyInteresting: Any
    kAssembly: Any
    kBlendShape: Any
    kCameraSetNode: Any
    kClientDeviceNode: Any
    kConstraintNode: Any
    kDefaultScheduling: Any
    kDeformerNode: Any
    kDependNode: Any
    kEmitterNode: Any
    kEvaluatedDirectly: Any
    kEvaluatedIndirectly: Any
    kFieldNode: Any
    kFluidEmitterNode: Any
    kGeometryFilter: Any
    kGloballySerial: Any
    kGloballySerialize: Any
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
    kParallel: Any
    kParticleAttributeMapperNode: Any
    kPostEvaluationTypeLast: Any
    kSchedulingTypeLast: Any
    kSerial: Any
    kSerialize: Any
    kSkinCluster: Any
    kSpringNode: Any
    kSurfaceShape: Any
    kThreadedDeviceNode: Any
    kTransformNode: Any
    kUntrusted: Any
    message: Any
    state: Any
    thisown: Any
    def __init__(self) -> None:
        """Constructor."""
    @staticmethod
    def addAttribute(attr: MObject) -> MStatus:
        """This method adds a new attribute to a user defined node type during the type's initialization."""
    def addExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Adds content info to the specified table from a file path attribute."""
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> MStatus: ...
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject, affectsTopology: bool) -> MStatus:
        """This method specifies that a particular input attribute affects a specific output attribute."""
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def compute(self) -> MStatus:
        """This method should be overridden in user defined nodes."""
    def configCache(self) -> None:
        """Introduced in 2020.0"""
    def connectionBroken(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are made to attributes of this node."""
    def copyInternalData(self) -> None:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def dependsOn(self, depends: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    def getCacheSetup(self) -> None:
        """Introduced in 2020.0"""
    def getExternalContent(self, table: MExternalContentInfoTable) -> None:
        """Returns the external content (files) that this node depends on."""
    def getFilesToArchive(self, shortName: bool = False, unresolvedName: bool = False, markCouldBeImageSequence: bool = False) -> Any:
        """Use this method to return all external files used by this node."""
    def getInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def getInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def hasInvalidationRangeTransformation(self) -> bool:
        """Introduced in 2020.0"""
    @staticmethod
    def inheritAttributesFrom(parentClassName: str) -> MStatus:
        """This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node."""
    @overload
    def internalArrayCount(self) -> int: ...
    @overload
    def internalArrayCount(self) -> int:
        """This method is overridden by nodes that have internal array attributes which are not stored in Maya's datablock."""
    def isAbstractClass(self) -> bool:
        """Override this class to return true if this node is an abstract node."""
    def isPassiveOutput(self) -> bool:
        """This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent val"""
    def isTrackingTopology(self) -> bool:
        """Introduced in 2019.0"""
    def legalConnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal connections being made to attributes of this node."""
    def legalDisconnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal disconnections being made to attributes of this node."""
    def name(self) -> str:
        """Returns the name of this particular instance of this class."""
    def passThroughToMany(self) -> bool:
        """This method is overridden by nodes that want to control the traversal behavior of some Maya search algorithms which trav"""
    def passThroughToOne(self) -> MPlug:
        """This method may be overridden by nodes that have a one-to-one relationship between an input attribute and a correspondin"""
    def postConstructor(self) -> None:
        """Post constructor."""
    def postEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode, evalType: Any) -> MStatus:
        """Clean up node's internal state after threaded evaluation."""
    def preEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode) -> MStatus:
        """Prepare a node's internal state for threaded evaluation."""
    def schedulingType(self) -> Any:
        """When overridden this method controls the degree of parallelism supported by the node during threaded evaluation."""
    def setDependentsDirty(self, plug: MPlug, plugArray: MPlugArray) -> MStatus:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug """
    def setExistWithoutInConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without input connections."""
    def setExistWithoutOutConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without output connections."""
    def setExternalContent(self) -> None:
        """Changes the location of external content in batch."""
    def setExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Sets content info in the specified attribute from the table."""
    def setInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def shouldSave(self, isSaving: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def thisMObject(self) -> MObject:
        """Returns the MObject associated with this user defined node."""
    def transformInvalidationRange(self, source: MPlug, input: MTimeRange) -> MTimeRange:
        """Introduced in 2020.0"""
    def type(self) -> Any:
        """Returns the type of node that this is."""
    def typeId(self) -> MTypeId:
        """Returns the TYPEID of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""

class MPxObjectSet:
    DNSetMembers: Any
    annotation: Any
    caching: Any
    dagSetMembers: Any
    edgesOnlySet: Any
    editPointsOnlySet: Any
    facetsOnlySet: Any
    frozen: Any
    groupNodes: Any
    isHistoricallyInteresting: Any
    isLayer: Any
    kAssembly: Any
    kBlendShape: Any
    kCameraSetNode: Any
    kClientDeviceNode: Any
    kConstraintNode: Any
    kDefaultScheduling: Any
    kDeformerNode: Any
    kDependNode: Any
    kEmitterNode: Any
    kEvaluatedDirectly: Any
    kEvaluatedIndirectly: Any
    kFieldNode: Any
    kFluidEmitterNode: Any
    kGeometryFilter: Any
    kGloballySerial: Any
    kGloballySerialize: Any
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
    kParallel: Any
    kParticleAttributeMapperNode: Any
    kPostEvaluationTypeLast: Any
    kSchedulingTypeLast: Any
    kSerial: Any
    kSerialize: Any
    kSkinCluster: Any
    kSpringNode: Any
    kSurfaceShape: Any
    kThreadedDeviceNode: Any
    kTransformNode: Any
    kUntrusted: Any
    memberWireframeColor: Any
    message: Any
    partition: Any
    renderableOnlySet: Any
    state: Any
    thisown: Any
    usedByNodes: Any
    verticesOnlySet: Any
    def __init__(self) -> None:
        """Class constructor."""
    @staticmethod
    def addAttribute(attr: MObject) -> MStatus:
        """This method adds a new attribute to a user defined node type during the type's initialization."""
    def addExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Adds content info to the specified table from a file path attribute."""
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> MStatus: ...
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject, affectsTopology: bool) -> MStatus:
        """This method specifies that a particular input attribute affects a specific output attribute."""
    def canBeDeleted(self, isSrcNode: bool) -> bool:
        """A method that is called whenever a neighboring node is deleted, to check if this node should be deleted alongside or as """
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def compute(self) -> MStatus:
        """This method should be overridden in user defined nodes."""
    def configCache(self) -> None:
        """Introduced in 2020.0"""
    def connectionBroken(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are made to attributes of this node."""
    def copyInternalData(self) -> None:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def dependsOn(self, depends: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    def getCacheSetup(self) -> None:
        """Introduced in 2020.0"""
    def getExternalContent(self, table: MExternalContentInfoTable) -> None:
        """Returns the external content (files) that this node depends on."""
    def getFilesToArchive(self, shortName: bool = False, unresolvedName: bool = False, markCouldBeImageSequence: bool = False) -> Any:
        """Use this method to return all external files used by this node."""
    def getInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def getInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def hasInvalidationRangeTransformation(self) -> bool:
        """Introduced in 2020.0"""
    @staticmethod
    def inheritAttributesFrom(parentClassName: str) -> MStatus:
        """This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node."""
    @overload
    def internalArrayCount(self) -> int: ...
    @overload
    def internalArrayCount(self) -> int:
        """This method is overridden by nodes that have internal array attributes which are not stored in Maya's datablock."""
    def isAbstractClass(self) -> bool:
        """Override this class to return true if this node is an abstract node."""
    def isPassiveOutput(self) -> bool:
        """This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent val"""
    def isTrackingTopology(self) -> bool:
        """Introduced in 2019.0"""
    def legalConnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal connections being made to attributes of this node."""
    def legalDisconnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal disconnections being made to attributes of this node."""
    def name(self) -> str:
        """Returns the name of this particular instance of this class."""
    def passThroughToMany(self) -> bool:
        """This method is overridden by nodes that want to control the traversal behavior of some Maya search algorithms which trav"""
    def passThroughToOne(self) -> MPlug:
        """This method may be overridden by nodes that have a one-to-one relationship between an input attribute and a correspondin"""
    def postConstructor(self) -> None:
        """Post constructor."""
    def postEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode, evalType: Any) -> MStatus:
        """Clean up node's internal state after threaded evaluation."""
    def preEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode) -> MStatus:
        """Prepare a node's internal state for threaded evaluation."""
    def schedulingType(self) -> Any:
        """When overridden this method controls the degree of parallelism supported by the node during threaded evaluation."""
    def setDependentsDirty(self, plug: MPlug, plugArray: MPlugArray) -> MStatus:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug """
    def setExistWithoutInConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without input connections."""
    def setExistWithoutOutConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without output connections."""
    def setExternalContent(self) -> None:
        """Changes the location of external content in batch."""
    def setExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Sets content info in the specified attribute from the table."""
    def setInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def shouldSave(self, isSaving: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def thisMObject(self) -> MObject:
        """Returns the MObject associated with this user defined node."""
    def transformInvalidationRange(self, source: MPlug, input: MTimeRange) -> MTimeRange:
        """Introduced in 2020.0"""
    def type(self) -> int:
        """Returns the type of node that this is."""
    def typeId(self) -> MTypeId:
        """Returns the TYPEID of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""

class MPxParticleAttributeMapperNode:
    caching: Any
    computeNode: Any
    computeNodeColor: Any
    computeNodeColorB: Any
    computeNodeColorG: Any
    computeNodeColorR: Any
    frozen: Any
    isHistoricallyInteresting: Any
    kAssembly: Any
    kBlendShape: Any
    kCameraSetNode: Any
    kClientDeviceNode: Any
    kConstraintNode: Any
    kDefaultScheduling: Any
    kDeformerNode: Any
    kDependNode: Any
    kEmitterNode: Any
    kEvaluatedDirectly: Any
    kEvaluatedIndirectly: Any
    kFieldNode: Any
    kFluidEmitterNode: Any
    kGeometryFilter: Any
    kGloballySerial: Any
    kGloballySerialize: Any
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
    kParallel: Any
    kParticleAttributeMapperNode: Any
    kPostEvaluationTypeLast: Any
    kSchedulingTypeLast: Any
    kSerial: Any
    kSerialize: Any
    kSkinCluster: Any
    kSpringNode: Any
    kSurfaceShape: Any
    kThreadedDeviceNode: Any
    kTransformNode: Any
    kUntrusted: Any
    message: Any
    outColorPP: Any
    outMaxValue: Any
    outMinValue: Any
    outValuePP: Any
    state: Any
    thisown: Any
    time: Any
    uCoordPP: Any
    vCoordPP: Any
    def __init__(self) -> None:
        """Class constructor."""
    @staticmethod
    def addAttribute(attr: MObject) -> MStatus:
        """This method adds a new attribute to a user defined node type during the type's initialization."""
    def addExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Adds content info to the specified table from a file path attribute."""
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> MStatus: ...
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject, affectsTopology: bool) -> MStatus:
        """This method specifies that a particular input attribute affects a specific output attribute."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def compute(self, plug: MPlug, dataBlock: MDataBlock) -> MStatus:
        """This method should be overridden in user defined nodes."""
    def configCache(self) -> None:
        """Introduced in 2020.0"""
    def connectionBroken(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are made to attributes of this node."""
    def copyInternalData(self) -> None:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def dependsOn(self, depends: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    def getCacheSetup(self) -> None:
        """Introduced in 2020.0"""
    def getExternalContent(self, table: MExternalContentInfoTable) -> None:
        """Returns the external content (files) that this node depends on."""
    def getFilesToArchive(self, shortName: bool = False, unresolvedName: bool = False, markCouldBeImageSequence: bool = False) -> Any:
        """Use this method to return all external files used by this node."""
    def getInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def getInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def hasInvalidationRangeTransformation(self) -> bool:
        """Introduced in 2020.0"""
    @staticmethod
    def inheritAttributesFrom(parentClassName: str) -> MStatus:
        """This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node."""
    @overload
    def internalArrayCount(self) -> int: ...
    @overload
    def internalArrayCount(self) -> int:
        """This method is overridden by nodes that have internal array attributes which are not stored in Maya's datablock."""
    def isAbstractClass(self) -> bool:
        """Override this class to return true if this node is an abstract node."""
    def isPassiveOutput(self) -> bool:
        """This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent val"""
    def isTrackingTopology(self) -> bool:
        """Introduced in 2019.0"""
    def legalConnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal connections being made to attributes of this node."""
    def legalDisconnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal disconnections being made to attributes of this node."""
    def name(self) -> str:
        """Returns the name of this particular instance of this class."""
    def passThroughToMany(self) -> bool:
        """This method is overridden by nodes that want to control the traversal behavior of some Maya search algorithms which trav"""
    def passThroughToOne(self) -> MPlug:
        """This method may be overridden by nodes that have a one-to-one relationship between an input attribute and a correspondin"""
    def postConstructor(self) -> None:
        """Post constructor."""
    def postEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode, evalType: Any) -> MStatus:
        """Clean up node's internal state after threaded evaluation."""
    def preEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode) -> MStatus:
        """Prepare a node's internal state for threaded evaluation."""
    def schedulingType(self) -> Any:
        """When overridden this method controls the degree of parallelism supported by the node during threaded evaluation."""
    def setDependentsDirty(self, plug: MPlug, plugArray: MPlugArray) -> MStatus:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug """
    def setExistWithoutInConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without input connections."""
    def setExistWithoutOutConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without output connections."""
    def setExternalContent(self) -> None:
        """Changes the location of external content in batch."""
    def setExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Sets content info in the specified attribute from the table."""
    def setInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def shouldSave(self, isSaving: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def thisMObject(self) -> MObject:
        """Returns the MObject associated with this user defined node."""
    def transformInvalidationRange(self, source: MPlug, input: MTimeRange) -> MTimeRange:
        """Introduced in 2020.0"""
    def type(self) -> int:
        """Returns the type of node that this is."""
    def typeId(self) -> MTypeId:
        """Returns the TYPEID of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""

class MPxPolyTrg:
    caching: Any
    frozen: Any
    isHistoricallyInteresting: Any
    kAssembly: Any
    kBlendShape: Any
    kCameraSetNode: Any
    kClientDeviceNode: Any
    kConstraintNode: Any
    kDefaultScheduling: Any
    kDeformerNode: Any
    kDependNode: Any
    kEmitterNode: Any
    kEvaluatedDirectly: Any
    kEvaluatedIndirectly: Any
    kFieldNode: Any
    kFluidEmitterNode: Any
    kGeometryFilter: Any
    kGloballySerial: Any
    kGloballySerialize: Any
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
    kParallel: Any
    kParticleAttributeMapperNode: Any
    kPostEvaluationTypeLast: Any
    kSchedulingTypeLast: Any
    kSerial: Any
    kSerialize: Any
    kSkinCluster: Any
    kSpringNode: Any
    kSurfaceShape: Any
    kThreadedDeviceNode: Any
    kTransformNode: Any
    kUntrusted: Any
    message: Any
    state: Any
    thisown: Any
    def __init__(self) -> None:
        """Constructor."""
    @staticmethod
    def addAttribute(attr: MObject) -> MStatus:
        """This method adds a new attribute to a user defined node type during the type's initialization."""
    def addExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Adds content info to the specified table from a file path attribute."""
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> MStatus: ...
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject, affectsTopology: bool) -> MStatus:
        """This method specifies that a particular input attribute affects a specific output attribute."""
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def compute(self, plug: MPlug, dataBlock: MDataBlock) -> MStatus:
        """This method should be overridden in user defined nodes."""
    def configCache(self) -> None:
        """Introduced in 2020.0"""
    def connectionBroken(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are made to attributes of this node."""
    def copyInternalData(self) -> None:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def dependsOn(self, depends: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    def getCacheSetup(self) -> None:
        """Introduced in 2020.0"""
    def getExternalContent(self, table: MExternalContentInfoTable) -> None:
        """Returns the external content (files) that this node depends on."""
    def getFilesToArchive(self, shortName: bool = False, unresolvedName: bool = False, markCouldBeImageSequence: bool = False) -> Any:
        """Use this method to return all external files used by this node."""
    def getInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def getInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def hasInvalidationRangeTransformation(self) -> bool:
        """Introduced in 2020.0"""
    @staticmethod
    def inheritAttributesFrom(parentClassName: str) -> MStatus:
        """This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node."""
    @overload
    def internalArrayCount(self) -> int: ...
    @overload
    def internalArrayCount(self) -> int:
        """This method is overridden by nodes that have internal array attributes which are not stored in Maya's datablock."""
    def isAbstractClass(self) -> bool:
        """Each new node has to implement that fuction."""
    def isPassiveOutput(self) -> bool:
        """This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent val"""
    def isTrackingTopology(self) -> bool:
        """Introduced in 2019.0"""
    def legalConnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal connections being made to attributes of this node."""
    def legalDisconnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal disconnections being made to attributes of this node."""
    def name(self) -> str:
        """Returns the name of this particular instance of this class."""
    def passThroughToMany(self) -> bool:
        """This method is overridden by nodes that want to control the traversal behavior of some Maya search algorithms which trav"""
    def passThroughToOne(self) -> MPlug:
        """This method may be overridden by nodes that have a one-to-one relationship between an input attribute and a correspondin"""
    def postConstructor(self) -> None:
        """Post constructor."""
    def postEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode, evalType: Any) -> MStatus:
        """Clean up node's internal state after threaded evaluation."""
    def preEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode) -> MStatus:
        """Prepare a node's internal state for threaded evaluation."""
    def registerTrgFunction(self, name: str, f: Any) -> MStatus:
        """Register a triangulation function with maya."""
    def schedulingType(self) -> Any:
        """When overridden this method controls the degree of parallelism supported by the node during threaded evaluation."""
    def setDependentsDirty(self, plug: MPlug, plugArray: MPlugArray) -> MStatus:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug """
    def setExistWithoutInConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without input connections."""
    def setExistWithoutOutConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without output connections."""
    def setExternalContent(self) -> None:
        """Changes the location of external content in batch."""
    def setExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Sets content info in the specified attribute from the table."""
    def setInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def shouldSave(self, isSaving: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def thisMObject(self) -> MObject:
        """Returns the MObject associated with this user defined node."""
    def transformInvalidationRange(self, source: MPlug, input: MTimeRange) -> MTimeRange:
        """Introduced in 2020.0"""
    def type(self) -> Any:
        """Returns the type of node that this is."""
    def typeId(self) -> MTypeId:
        """Returns the TYPEID of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""
    def unregisterTrgFunction(self, name: str) -> MStatus:
        """Constructor."""

class MPxPolyTweakUVCommand:
    kDouble: Any
    kLong: Any
    kNoArg: Any
    kString: Any
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def appendToResult(self, *args: Any, **kwargs: Any) -> Any: ...
    def className(self, *args: Any, **kwargs: Any) -> Any: ...
    def clearResult(self, *args: Any, **kwargs: Any) -> Any: ...
    def commandString(self, *args: Any, **kwargs: Any) -> Any: ...
    def currentDoubleResult(self, *args: Any, **kwargs: Any) -> Any: ...
    def currentIntResult(self, *args: Any, **kwargs: Any) -> Any: ...
    def currentResultType(self, *args: Any, **kwargs: Any) -> Any: ...
    def currentStringResult(self, *args: Any, **kwargs: Any) -> Any: ...
    def displayError(self, *args: Any, **kwargs: Any) -> Any: ...
    def displayInfo(self, *args: Any, **kwargs: Any) -> Any: ...
    def displayWarning(self, *args: Any, **kwargs: Any) -> Any: ...
    def doIt(self, *args: Any, **kwargs: Any) -> Any: ...
    def getCurrentResult(self, *args: Any, **kwargs: Any) -> Any: ...
    def getTweakedUVs(self, *args: Any, **kwargs: Any) -> Any: ...
    def hasSyntax(self, *args: Any, **kwargs: Any) -> Any: ...
    def isCurrentResultArray(self, *args: Any, **kwargs: Any) -> Any: ...
    def isHistoryOn(self, *args: Any, **kwargs: Any) -> Any: ...
    def isUndoable(self, *args: Any, **kwargs: Any) -> Any: ...
    def newSyntax(self, *args: Any, **kwargs: Any) -> Any: ...
    def parseSyntax(self, *args: Any, **kwargs: Any) -> Any: ...
    def redoIt(self, *args: Any, **kwargs: Any) -> Any: ...
    def setCommandString(self, *args: Any, **kwargs: Any) -> Any: ...
    def setHistoryOn(self, *args: Any, **kwargs: Any) -> Any: ...
    def setResult(self, *args: Any, **kwargs: Any) -> Any: ...
    def setUndoable(self, *args: Any, **kwargs: Any) -> Any: ...
    def syntax(self, *args: Any, **kwargs: Any) -> Any: ...
    def undoIt(self, *args: Any, **kwargs: Any) -> Any: ...

class MPxPolyTweakUVInteractiveCommand:
    kDouble: Any
    kLong: Any
    kNoArg: Any
    kString: Any
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def appendToResult(self, *args: Any, **kwargs: Any) -> Any: ...
    def cancel(self, *args: Any, **kwargs: Any) -> Any: ...
    def className(self, *args: Any, **kwargs: Any) -> Any: ...
    def clearResult(self, *args: Any, **kwargs: Any) -> Any: ...
    def commandString(self, *args: Any, **kwargs: Any) -> Any: ...
    def currentDoubleResult(self, *args: Any, **kwargs: Any) -> Any: ...
    def currentIntResult(self, *args: Any, **kwargs: Any) -> Any: ...
    def currentResultType(self, *args: Any, **kwargs: Any) -> Any: ...
    def currentStringResult(self, *args: Any, **kwargs: Any) -> Any: ...
    def displayError(self, *args: Any, **kwargs: Any) -> Any: ...
    def displayInfo(self, *args: Any, **kwargs: Any) -> Any: ...
    def displayWarning(self, *args: Any, **kwargs: Any) -> Any: ...
    def doIt(self, *args: Any, **kwargs: Any) -> Any: ...
    def finalize(self, *args: Any, **kwargs: Any) -> Any: ...
    def getCurrentResult(self, *args: Any, **kwargs: Any) -> Any: ...
    def hasSyntax(self, *args: Any, **kwargs: Any) -> Any: ...
    def isCurrentResultArray(self, *args: Any, **kwargs: Any) -> Any: ...
    def isHistoryOn(self, *args: Any, **kwargs: Any) -> Any: ...
    def isUndoable(self, *args: Any, **kwargs: Any) -> Any: ...
    def redoIt(self, *args: Any, **kwargs: Any) -> Any: ...
    def setCommandString(self, *args: Any, **kwargs: Any) -> Any: ...
    def setHistoryOn(self, *args: Any, **kwargs: Any) -> Any: ...
    def setResult(self, *args: Any, **kwargs: Any) -> Any: ...
    def setUVs(self, *args: Any, **kwargs: Any) -> Any: ...
    def setUndoable(self, *args: Any, **kwargs: Any) -> Any: ...
    def syntax(self, *args: Any, **kwargs: Any) -> Any: ...
    def undoIt(self, *args: Any, **kwargs: Any) -> Any: ...

class MPxRenderPassImpl:
    kBit: Any
    kColorSemantic: Any
    kDepthSemantic: Any
    kDirectionVectorSemantic: Any
    kFloat16: Any
    kFloat32: Any
    kFloat64: Any
    kInt16: Any
    kInt32: Any
    kInt64: Any
    kInt8: Any
    kInvalidSemantic: Any
    kLabelSemantic: Any
    kMaskSemantic: Any
    kOther: Any
    kOtherSemantic: Any
    kUInt16: Any
    kUInt32: Any
    kUInt64: Any
    kUInt8: Any
    kVectorSemantic: Any
    thisown: Any
    def __init__(self) -> None:
        """Default constructor."""
    def frameBufferSemantic(self) -> Any:
        """Called by Maya to get the frame buffer semantic."""
    def getDefaultType(self) -> Any:
        """Called by Maya to determine the default type for this pass."""
    def getNumChannels(self) -> int:
        """Called by Maya to get the number of channels supported by this pass."""
    def isCompatible(self, renderer: str) -> bool:
        """Called by Maya check whether this pass implementation is compatible with the given renderer."""
    def perLightPassContributionSupported(self) -> bool:
        """Called by Maya to determine if this pass implementation supports per-light contributions defined by pass contribution ma"""
    def typesSupported(self) -> Any:
        """Called by Maya to determine which types are supported by this pass."""

class MPxRepresentation:
    thisown: Any
    def __init__(self, assembly: MPxAssembly, name: str) -> None:
        """Class constructor, to be called by concrete derived classes."""
    def activate(self) -> bool:
        """Activate this representation."""
    def canApplyEdits(self) -> bool:
        """Determines whether this representation can apply tracked edits to its data."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> None:
        """Get external content for this representation."""
    def getName(self) -> str:
        """Returns the name of the representation."""
    def getType(self) -> str:
        """Return the representation type string."""
    def inactivate(self) -> bool:
        """Inactivate this representation."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> None:
        """Set external content for this representation."""

class MPxSelectionContext:
    kImage1: Any
    kImage2: Any
    kImage3: Any
    thisown: Any
    def __init__(self) -> None:
        """Class contstructor."""
    def abortAction(self) -> None:
        """This method is called when the abort key is pressed."""
    def addManipulator(self, manipulator: MObject) -> MStatus:
        """This method adds a manipulator to the context, and also adds the manipulator to the DAG."""
    def argTypeNumericalInput(self, index: int) -> int:
        """This method is used by the feedback line to determine what units to display."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def completeAction(self) -> None:
        """This method is called when the complete key is pressed."""
    def deleteAction(self) -> None:
        """This method is called when the delete or backspace key is pressed."""
    def deleteManipulators(self) -> MStatus:
        """This method deletes all the manipulators that belong to the context."""
    @overload
    def doDrag(self, event: MEvent, drawMgr: int, context: int) -> MStatus: ...
    @overload
    def doDrag(self, event: MEvent) -> MStatus:
        """Not available in Python."""
    def doEnterRegion(self, event: MEvent) -> MStatus:
        """This method is called when the mouse pointer enters a screen panel region."""
    def doExitRegion(self, event: MEvent) -> MStatus:
        """Introduced in 2024.0"""
    @overload
    def doHold(self, event: MEvent, drawMgr: int, context: int) -> MStatus: ...
    @overload
    def doHold(self, event: MEvent) -> MStatus:
        """Not available in Python."""
    @overload
    def doPress(self, event: MEvent, drawMgr: int, context: int) -> MStatus: ...
    @overload
    def doPress(self, event: MEvent) -> MStatus:
        """Not available in Python."""
    @overload
    def doPtrMoved(self, event: MEvent, drawMgr: int, context: int) -> MStatus: ...
    @overload
    def doPtrMoved(self, event: MEvent) -> MStatus:
        """Not available in Python."""
    @overload
    def doRelease(self, event: MEvent, drawMgr: int, context: int) -> MStatus: ...
    @overload
    def doRelease(self, event: MEvent) -> MStatus:
        """Not available in Python."""
    def feedbackNumericalInput(self) -> bool:
        """This method is called to update the numerical feedback."""
    def helpStateHasChanged(self) -> MStatus:
        """This method is called whenever the help state may need to be updated."""
    @overload
    def image(self, index: Any) -> str: ...
    @overload
    def image(self, index: Any) -> str:
        """This method is used to retrieve an XPM icon image that has previously been set for this tool context."""
    def inAlternateContext(self) -> bool:
        """Introduced in 2024.0"""
    def newToolCommand(self) -> MPxToolCommand:
        """CALL _newToolCommand() IN SCRIPT."""
    def processNumericalInput(self, values: MDoubleArray, flags: MIntArray, isAbsolute: bool) -> bool:
        """This method processes the input from the numerical input field."""
    def setAllowDoubleClickAction(self) -> MStatus:
        """This method enables the support of double click smart selection for this context."""
    def setAllowPaintSelect(self) -> MStatus:
        """Introduced in 2023.0"""
    def setAllowPreSelectHilight(self) -> MStatus:
        """This method enables the support of pre-selection highlight for this context."""
    def setAllowSoftSelect(self) -> MStatus:
        """This method enables the support of soft selection for this context."""
    def setAllowSymmetry(self) -> MStatus:
        """This method enables the support of symmetrical selection for this context."""
    @overload
    def setImage(self, image: str, index: Any) -> MStatus: ...
    @overload
    def setImage(self, image: str, index: Any) -> MStatus:
        """This method is used to set an XPM icon image that is to be used to represent this tool context in various places includi"""
    def stringClassName(self) -> str:
        """This method is called to determine the name that uniquely identifies the context."""
    def toolOffCleanup(self) -> None:
        """This method is called when the context is deactivated, i.e when another context is activated."""
    def toolOnSetup(self, event: MEvent) -> None:
        """This method is called when the context is activated, i.e when the toolButton for the context is pressed."""

class MPxSkinCluster:
    bindPreMatrix: Any
    caching: Any
    componentTagExpression: Any
    envelope: Any
    frozen: Any
    groupId: Any
    input: Any
    inputGeom: Any
    isHistoricallyInteresting: Any
    kAssembly: Any
    kBlendShape: Any
    kCameraSetNode: Any
    kClientDeviceNode: Any
    kConstraintNode: Any
    kDefaultScheduling: Any
    kDeformerNode: Any
    kDeformsAll: Any
    kDeformsColors: Any
    kDeformsUVs: Any
    kDependNode: Any
    kEmitterNode: Any
    kEvaluatedDirectly: Any
    kEvaluatedIndirectly: Any
    kFieldNode: Any
    kFluidEmitterNode: Any
    kGeometryFilter: Any
    kGloballySerial: Any
    kGloballySerialize: Any
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
    kParallel: Any
    kParticleAttributeMapperNode: Any
    kPostEvaluationTypeLast: Any
    kSchedulingTypeLast: Any
    kSerial: Any
    kSerialize: Any
    kSkinCluster: Any
    kSpringNode: Any
    kSurfaceShape: Any
    kThreadedDeviceNode: Any
    kTransformNode: Any
    kUntrusted: Any
    matrix: Any
    message: Any
    outputGeom: Any
    state: Any
    thisown: Any
    weightList: Any
    weights: Any
    def __init__(self) -> None:
        """Class constructor."""
    def accessoryAttribute(self) -> MObject:
        """This method returns an MObject for the attribute to which an accessory shape is connected."""
    def accessoryNodeSetup(self, cmd: MDagModifier) -> MStatus:
        """This method is called by the "deformer -type" command when your node is specified."""
    @staticmethod
    def addAttribute(attr: MObject) -> MStatus:
        """This method adds a new attribute to a user defined node type during the type's initialization."""
    def addExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Adds content info to the specified table from a file path attribute."""
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> MStatus: ...
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject, affectsTopology: bool) -> MStatus:
        """This method specifies that a particular input attribute affects a specific output attribute."""
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
    def compute(self) -> MStatus:
        """This method should be overridden in user defined nodes."""
    def configCache(self) -> None:
        """Introduced in 2020.0"""
    def connectionBroken(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are made to attributes of this node."""
    def copyInternalData(self) -> None:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def deform(self, block: MDataBlock, iter: MItGeometry, mat: MMatrix, multiIndex: int) -> MStatus:
        """This method performs the deformation algorithm."""
    def dependsOn(self, depends: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    def getCacheSetup(self) -> None:
        """Introduced in 2020.0"""
    def getDeformationDetails(self) -> int:
        """Retrieves the value set by setDeformationDetails() ."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> None:
        """Returns the external content (files) that this node depends on."""
    def getFilesToArchive(self, shortName: bool = False, unresolvedName: bool = False, markCouldBeImageSequence: bool = False) -> Any:
        """Use this method to return all external files used by this node."""
    def getFixedSetupData(self, name: str) -> MObject:
        """Introduced in 2022.0"""
    def getGeometryIterator(self, iter: MItGeometry, block: MDataBlock, dataHandle: MDataHandle, multiIndex: int, readOnly: bool = True) -> int:
        """Introduced in 2022.0"""
    def getInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def getInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def hasInvalidationRangeTransformation(self) -> bool:
        """Introduced in 2020.0"""
    def indexMapper(self, multiIndex: int) -> Any:
        """Introduced in 2024.0"""
    @staticmethod
    def inheritAttributesFrom(parentClassName: str) -> MStatus:
        """This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node."""
    @overload
    def internalArrayCount(self) -> int: ...
    @overload
    def internalArrayCount(self) -> int:
        """This method is overridden by nodes that have internal array attributes which are not stored in Maya's datablock."""
    def isAbstractClass(self) -> bool:
        """Override this class to return true if this node is an abstract node."""
    def isPassiveOutput(self) -> bool:
        """This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent val"""
    def isTrackingTopology(self) -> bool:
        """Introduced in 2019.0"""
    def legalConnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal connections being made to attributes of this node."""
    def legalDisconnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal disconnections being made to attributes of this node."""
    def name(self) -> str:
        """Returns the name of this particular instance of this class."""
    def passThroughToMany(self) -> bool:
        """This method is overridden by nodes that want to control the traversal behavior of some Maya search algorithms which trav"""
    def passThroughToOne(self) -> MPlug:
        """This method may be overridden by nodes that have a one-to-one relationship between an input attribute and a correspondin"""
    def postConstructor(self) -> None:
        """Post constructor."""
    def postEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode, evalType: Any) -> MStatus:
        """Clean up node's internal state after threaded evaluation."""
    def preEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode) -> MStatus:
        """Prepare a node's internal state for threaded evaluation."""
    def schedulingType(self) -> Any:
        """When overridden this method controls the degree of parallelism supported by the node during threaded evaluation."""
    def setDeformationDetails(self, flags: int) -> MStatus:
        """This method allows the plug-in node to inform the system that it intends to deform components other than just positions."""
    def setDependentsDirty(self, plug: MPlug, plugArray: MPlugArray) -> MStatus:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug """
    def setExistWithoutInConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without input connections."""
    def setExistWithoutOutConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without output connections."""
    def setExternalContent(self) -> None:
        """Changes the location of external content in batch."""
    def setExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Sets content info in the specified attribute from the table."""
    def setInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def setModifiedCallback(self, list: MSelectionList, listAdded: bool) -> None:
        """This callback method can be overriden and is called whenever the set this deformer is operating on is modified."""
    def setUseExistingConnectionWhenSetEditing(self, state: bool) -> None:
        """This method allows the plugin node to request special treatment during set editing."""
    def shouldSave(self, isSaving: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def thisMObject(self) -> MObject:
        """Returns the MObject associated with this user defined node."""
    def transformInvalidationRange(self, source: MPlug, input: MTimeRange) -> MTimeRange:
        """Introduced in 2020.0"""
    def type(self) -> int:
        """This method returns the type of the node."""
    def typeId(self) -> MTypeId:
        """Returns the TYPEID of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""
    def weightValue(self, mblock: MDataBlock, multiIndex: int, wtIndex: int) -> float:
        """This method returns the weightValue stored in the datablock for the given geometry's lattice point/CV/vertex."""

class MPxSpringNode:
    caching: Any
    frozen: Any
    isHistoricallyInteresting: Any
    kAssembly: Any
    kBlendShape: Any
    kCameraSetNode: Any
    kClientDeviceNode: Any
    kConstraintNode: Any
    kDefaultScheduling: Any
    kDeformerNode: Any
    kDependNode: Any
    kEmitterNode: Any
    kEvaluatedDirectly: Any
    kEvaluatedIndirectly: Any
    kFieldNode: Any
    kFluidEmitterNode: Any
    kGeometryFilter: Any
    kGloballySerial: Any
    kGloballySerialize: Any
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
    kParallel: Any
    kParticleAttributeMapperNode: Any
    kPostEvaluationTypeLast: Any
    kSchedulingTypeLast: Any
    kSerial: Any
    kSerialize: Any
    kSkinCluster: Any
    kSpringNode: Any
    kSurfaceShape: Any
    kThreadedDeviceNode: Any
    kTransformNode: Any
    kUntrusted: Any
    mDeltaTime: Any
    mEnd1Weight: Any
    mEnd2Weight: Any
    message: Any
    state: Any
    thisown: Any
    def __init__(self) -> None:
        """Class constructor."""
    @staticmethod
    def addAttribute(attr: MObject) -> MStatus:
        """This method adds a new attribute to a user defined node type during the type's initialization."""
    def addExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Adds content info to the specified table from a file path attribute."""
    def applySpringLaw(self, stiffness: float, damping: float, restLength: float, endMass1: float, endMass2: float, endP1: MVector, endP2: MVector, endV1: MVector, endV2: MVector, forceV1: MVector, forceV2: MVector) -> MStatus:
        """This method should be overridden in user defined nodes."""
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> MStatus: ...
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject, affectsTopology: bool) -> MStatus:
        """This method specifies that a particular input attribute affects a specific output attribute."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def compute(self) -> MStatus:
        """This method should be overridden in user defined nodes."""
    def configCache(self) -> None:
        """Introduced in 2020.0"""
    def connectionBroken(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are made to attributes of this node."""
    def copyInternalData(self) -> None:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def dependsOn(self, depends: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    def getCacheSetup(self) -> None:
        """Introduced in 2020.0"""
    def getExternalContent(self, table: MExternalContentInfoTable) -> None:
        """Returns the external content (files) that this node depends on."""
    def getFilesToArchive(self, shortName: bool = False, unresolvedName: bool = False, markCouldBeImageSequence: bool = False) -> Any:
        """Use this method to return all external files used by this node."""
    def getInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def getInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def hasInvalidationRangeTransformation(self) -> bool:
        """Introduced in 2020.0"""
    @staticmethod
    def inheritAttributesFrom(parentClassName: str) -> MStatus:
        """This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node."""
    @overload
    def internalArrayCount(self) -> int: ...
    @overload
    def internalArrayCount(self) -> int:
        """This method is overridden by nodes that have internal array attributes which are not stored in Maya's datablock."""
    def isAbstractClass(self) -> bool:
        """Override this class to return true if this node is an abstract node."""
    def isPassiveOutput(self) -> bool:
        """This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent val"""
    def isTrackingTopology(self) -> bool:
        """Introduced in 2019.0"""
    def legalConnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal connections being made to attributes of this node."""
    def legalDisconnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal disconnections being made to attributes of this node."""
    def name(self) -> str:
        """Returns the name of this particular instance of this class."""
    def passThroughToMany(self) -> bool:
        """This method is overridden by nodes that want to control the traversal behavior of some Maya search algorithms which trav"""
    def passThroughToOne(self) -> MPlug:
        """This method may be overridden by nodes that have a one-to-one relationship between an input attribute and a correspondin"""
    def postConstructor(self) -> None:
        """Post constructor."""
    def postEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode, evalType: Any) -> MStatus:
        """Clean up node's internal state after threaded evaluation."""
    def preEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode) -> MStatus:
        """Prepare a node's internal state for threaded evaluation."""
    def schedulingType(self) -> Any:
        """When overridden this method controls the degree of parallelism supported by the node during threaded evaluation."""
    def setDependentsDirty(self, plug: MPlug, plugArray: MPlugArray) -> MStatus:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug """
    def setExistWithoutInConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without input connections."""
    def setExistWithoutOutConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without output connections."""
    def setExternalContent(self) -> None:
        """Changes the location of external content in batch."""
    def setExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Sets content info in the specified attribute from the table."""
    def setInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def shouldSave(self, isSaving: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def thisMObject(self) -> MObject:
        """Returns the MObject associated with this user defined node."""
    def transformInvalidationRange(self, source: MPlug, input: MTimeRange) -> MTimeRange:
        """Introduced in 2020.0"""
    def type(self) -> int:
        """This method returns the type of the node."""
    def typeId(self) -> MTypeId:
        """Returns the TYPEID of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""

class MPxSurfaceShape:
    boundingBoxCenterX: Any
    boundingBoxCenterY: Any
    boundingBoxCenterZ: Any
    caching: Any
    center: Any
    frozen: Any
    instObjGroups: Any
    intermediateObject: Any
    inverseMatrix: Any
    isHistoricallyInteresting: Any
    isTemplated: Any
    kAssembly: Any
    kBlendShape: Any
    kBoundingBoxChanged: Any
    kCameraSetNode: Any
    kClientDeviceNode: Any
    kConstraintNode: Any
    kDefaultScheduling: Any
    kDeformerNode: Any
    kDependNode: Any
    kEmitterNode: Any
    kEvaluatedDirectly: Any
    kEvaluatedIndirectly: Any
    kFieldNode: Any
    kFluidEmitterNode: Any
    kGeometryFilter: Any
    kGloballySerial: Any
    kGloballySerialize: Any
    kHardwareShader: Any
    kHwShaderNode: Any
    kIkSolverNode: Any
    kImagePlaneNode: Any
    kLast: Any
    kLeaveDirty: Any
    kLocatorNode: Any
    kManipContainer: Any
    kManipulatorNode: Any
    kMatchInvalidAttribute: Any
    kMatchInvalidAttributeDim: Any
    kMatchInvalidAttributeIndex: Any
    kMatchInvalidAttributeRange: Any
    kMatchInvalidName: Any
    kMatchNone: Any
    kMatchOk: Any
    kMatchTooMany: Any
    kMotionPathNode: Any
    kNoPointCaching: Any
    kNormal: Any
    kObjectChanged: Any
    kObjectSet: Any
    kParallel: Any
    kParticleAttributeMapperNode: Any
    kPostEvaluationTypeLast: Any
    kRestorePoints: Any
    kSavePoints: Any
    kSchedulingTypeLast: Any
    kSerial: Any
    kSerialize: Any
    kSkinCluster: Any
    kSpringNode: Any
    kSurfaceShape: Any
    kThreadedDeviceNode: Any
    kTransformNode: Any
    kTransformOriginalPoints: Any
    kUTangent: Any
    kUVNTriad: Any
    kUntrusted: Any
    kUpdatePoints: Any
    kVTangent: Any
    mControlPoints: Any
    mControlValueX: Any
    mControlValueY: Any
    mControlValueZ: Any
    mHasHistoryOnCreate: Any
    matrix: Any
    message: Any
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
    state: Any
    thisown: Any
    useObjectColor: Any
    visibility: Any
    worldInverseMatrix: Any
    worldMatrix: Any
    def __init__(self) -> None:
        """Class constructor."""
    @overload
    def acceptsGeometryIterator(self, writeable: bool = True) -> bool: ...
    @overload
    def acceptsGeometryIterator(self, writeable: bool = True, forReadOnly: bool = False) -> bool:
        """If the shape can supply a component iterator then then this method should be overridden to return true."""
    def activeComponents(self) -> MObjectArray:
        """Returns a list of active (selected) components for the shape."""
    @staticmethod
    def addAttribute(attr: MObject) -> MStatus:
        """This method adds a new attribute to a user defined node type during the type's initialization."""
    def addExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Adds content info to the specified table from a file path attribute."""
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> MStatus: ...
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject, affectsTopology: bool) -> MStatus:
        """This method specifies that a particular input attribute affects a specific output attribute."""
    def boundingBox(self) -> MBoundingBox:
        """This method should be overridden to return a bounding box for the shape."""
    def cachedShapeAttr(self) -> MObject:
        """Returns the attribute containing the shape's cached geometry, if it has one."""
    def canMakeLive(self) -> bool:
        """This method is used by Maya to determine whether a surface can be made live."""
    def childChanged(self, MChildChanged: Any) -> None:
        """This method can be used to trigger the shape to recalculate its bounding box."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @overload
    def closestPoint(self, raySource: MPoint, rayDirection: MVector, theClosestPoint: MPoint, theClosestNormal: MVector, findClosestOnMiss: bool, tolerance: float) -> bool: ...
    @overload
    def closestPoint(self, toThisPoint: MPoint, theClosestPoint: MPoint, tolerance: float) -> None:
        """This method is used by Maya for snapping queries when your surface is live."""
    def componentToPlugs(self, component: MObject, selectionList: MSelectionList) -> None:
        """Converts the given component into a selection list of plugs."""
    def compute(self) -> MStatus:
        """This method should be overridden in user defined nodes."""
    def configCache(self) -> None:
        """Introduced in 2020.0"""
    def connectionBroken(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are made to attributes of this node."""
    def convertToTweakNodePlug(self, plug: MPlug) -> bool:
        """Check if a tweak node is connected to this node."""
    def copyInternalData(self) -> None:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def createFullRenderGroup(self) -> MObject:
        """This method is used to create a component containing every renderable element in the object."""
    def createFullVertexGroup(self) -> MObject:
        """This method is used to create a component containing every vertex/CV in the object."""
    def deleteComponents(self, componentList: MObjectArray, undoInfo: MDoubleArray) -> bool:
        """This method should be overridden if the shape is to support deletion of components."""
    def dependsOn(self, depends: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def evalNodeAffectsDrawDb(self, evaluationNode: MEvaluationNode) -> bool:
        """This method should be overridden to return true if the evaluationNode contains any dirty plugs that will affect the draw"""
    def excludeAsPluginShape(self) -> bool:
        """A Maya viewport can be set to not display "Plugin Shapes", which means shapes derived from MPxSurfaceShape ."""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    def geometryData(self) -> MObject:
        """Returns the geometry data of the shape."""
    def geometryIteratorSetup(self, forReadOnly: bool = False) -> MPxGeometryIterator:
        """This method should be overridden by the user to return a geometry iterator compatible with the user's geometry."""
    def getCacheSetup(self) -> None:
        """Introduced in 2020.0"""
    def getComponentSelectionMask(self) -> MSelectionMask:
        """This routine must be overridden if the shape is to support interactive component selection in Viewport 2.0 and should pr"""
    def getExternalContent(self, table: MExternalContentInfoTable) -> None:
        """Returns the external content (files) that this node depends on."""
    def getFilesToArchive(self, shortName: bool = False, unresolvedName: bool = False, markCouldBeImageSequence: bool = False) -> Any:
        """Use this method to return all external files used by this node."""
    def getInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def getInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def getShapeSelectionMask(self) -> MSelectionMask:
        """This routine must be overridden if the shape is to support interactive object selection in Viewport 2.0 and should provi"""
    def getWorldMatrix(self, arg: int) -> MMatrix:
        """Returns MMatrix which takes a point from local object space to world space."""
    def hasActiveComponents(self) -> bool:
        """This method is used to determine whether or not the shape has active (selected) components."""
    def hasInvalidationRangeTransformation(self) -> bool:
        """Introduced in 2020.0"""
    @staticmethod
    def inheritAttributesFrom(parentClassName: str) -> MStatus:
        """This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node."""
    @overload
    def internalArrayCount(self) -> int: ...
    @overload
    def internalArrayCount(self) -> int:
        """This method is overridden by nodes that have internal array attributes which are not stored in Maya's datablock."""
    def isAbstractClass(self) -> bool:
        """Override this class to return true if this node is an abstract node."""
    def isBounded(self) -> bool:
        """This method should be overridden to return true if the user supplies a bounding box routine."""
    def isPassiveOutput(self) -> bool:
        """This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent val"""
    def isRenderable(self) -> bool:
        """Returns true if the shape is a renderable shape."""
    def isTrackingTopology(self) -> bool:
        """Introduced in 2019.0"""
    def legalConnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal connections being made to attributes of this node."""
    def legalDisconnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal disconnections being made to attributes of this node."""
    def localShapeInAttr(self) -> MObject:
        """Returns the attribute containing the shape's input geometry in local space."""
    def localShapeOutAttr(self) -> MObject:
        """Returns the attribute containing the shape's output geometry in local space."""
    def match(self, mask: MSelectionMask, componentList: MObjectArray) -> bool:
        """This method is used to check for matches between a selection type (or mask) and a given component."""
    def matchComponent(self, item: MSelectionList, spec: MAttributeSpecArray, list: MSelectionList) -> Any:
        """This method is used to convert the string representation of a component into a component object and to validate that the"""
    def name(self) -> str:
        """Returns the name of this particular instance of this class."""
    def newControlPointComponent(self) -> MObject:
        """The default action of this method is to return an MFnSingleIndexedComponent (of type MFn::kMeshVertComponent ) in order """
    def passThroughToMany(self) -> bool:
        """This method is overridden by nodes that want to control the traversal behavior of some Maya search algorithms which trav"""
    def passThroughToOne(self) -> MPlug:
        """This method may be overridden by nodes that have a one-to-one relationship between an input attribute and a correspondin"""
    def pointAtParm(self, atThisParm: MPoint, evaluatedPoint: MPoint) -> bool:
        """This method is used by Maya in functions (such as select) that require point at parameter values."""
    def postConstructor(self) -> None:
        """Post constructor."""
    def postEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode, evalType: Any) -> MStatus:
        """Clean up node's internal state after threaded evaluation."""
    def preEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode) -> MStatus:
        """Prepare a node's internal state for threaded evaluation."""
    def renderGroupComponentType(self) -> int:
        """This method is used to return the type of renderable components for this shape."""
    def schedulingType(self) -> Any:
        """When overridden this method controls the degree of parallelism supported by the node during threaded evaluation."""
    def setDependentsDirty(self, plug: MPlug, plugArray: MPlugArray) -> MStatus:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug """
    def setExistWithoutInConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without input connections."""
    def setExistWithoutOutConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without output connections."""
    def setExternalContent(self) -> None:
        """Changes the location of external content in batch."""
    def setExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Sets content info in the specified attribute from the table."""
    def setInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def setRenderable(self, arg: Any) -> None:
        """Specifies whether the shape is a renderable shape."""
    def shouldSave(self, isSaving: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def thisMObject(self) -> MObject:
        """Returns the MObject associated with this user defined node."""
    def transformInvalidationRange(self, source: MPlug, input: MTimeRange) -> MTimeRange:
        """Introduced in 2020.0"""
    @overload
    def transformUsing(self, mat: MMatrix, componentList: MObjectArray) -> None: ...
    @overload
    def transformUsing(self, mat: MMatrix, componentList: MObjectArray, cachingMode: Any, pointCache: MPointArray) -> None:
        """Transform the given components using the specified transformation matrix."""
    def tweakUsing(self, mat: MMatrix, componentList: MObjectArray, cachingMode: Any, pointCache: MPointArray, handle: MArrayDataHandle) -> None:
        """Transform the given components using the specified transformation matrix."""
    def type(self) -> int:
        """Returns the type of node that this is."""
    def typeId(self) -> MTypeId:
        """Returns the TYPEID of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""
    def undeleteComponents(self, componentList: MObjectArray, undoInfo: MDoubleArray) -> bool:
        """This method should be overridden if the shape is to support undeletion of components."""
    def vertexOffsetDirection(self, component: MObject, direction: MVectorArray, mode: Any, normalize: bool) -> bool:
        """This method should be overridden if the shape supports components that can be moved in the direction of the normal or UV"""
    def weightedTransformUsing(self, xform: MTransformationMatrix, space: MMatrix, componentList: MObjectArray, cachingMode: Any, pointCache: MPointArray, freezePlane: MPlane) -> None:
        """Transform the given components with interpolation using the specified transformation matrix."""
    def weightedTweakUsing(self, xform: MTransformationMatrix, space: MMatrix, componentList: MObjectArray, cachingMode: Any, pointCache: MPointArray, freezePlane: MPlane, handle: MArrayDataHandle) -> None:
        """Transform the given components with interpolation using the specified transformation matrix."""
    def worldShapeOutAttr(self) -> MObject:
        """Returns the attribute containing the shape's output geometry in world space."""

class MPxSurfaceShapeUI:
    kSelectMeshEdges: Any
    kSelectMeshFaces: Any
    kSelectMeshUVs: Any
    kSelectMeshVerts: Any
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def canDrawUV(self, *args: Any, **kwargs: Any) -> Any: ...
    def className(self, *args: Any, **kwargs: Any) -> Any: ...
    def draw(self, *args: Any, **kwargs: Any) -> Any: ...
    def drawUV(self, *args: Any, **kwargs: Any) -> Any: ...
    def getDrawData(self, *args: Any, **kwargs: Any) -> Any: ...
    def getDrawRequests(self, *args: Any, **kwargs: Any) -> Any: ...
    def material(self, *args: Any, **kwargs: Any) -> Any: ...
    def materials(self, *args: Any, **kwargs: Any) -> Any: ...
    def select(self, *args: Any, **kwargs: Any) -> Any: ...
    def selectUV(self, *args: Any, **kwargs: Any) -> Any: ...
    def snap(self, *args: Any, **kwargs: Any) -> Any: ...
    def surfaceShape(self, *args: Any, **kwargs: Any) -> Any: ...
    def surfaceShapeUI(self, *args: Any, **kwargs: Any) -> Any: ...

class MPxTexContext:
    kImage1: Any
    kImage2: Any
    kImage3: Any
    thisown: Any
    def __init__(self) -> None:
        """Class contstructor."""
    def abortAction(self) -> None:
        """This method is called when the abort key is pressed."""
    def addManipulator(self, manipulator: MObject) -> MStatus:
        """This method adds a manipulator to the context."""
    def argTypeNumericalInput(self, index: int) -> int:
        """This method is used by the feedback line to determine what units to display."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def completeAction(self) -> None:
        """This method is called when the complete key is pressed."""
    def deleteAction(self) -> None:
        """This method is called when the delete or backspace key is pressed."""
    def deleteManipulators(self) -> MStatus:
        """This method deletes all the manipulators that belong to the context."""
    @overload
    def doDrag(self, event: MEvent, drawMgr: int, context: int) -> MStatus: ...
    @overload
    def doDrag(self, event: MEvent) -> MStatus:
        """Not available in Python."""
    def doEnterRegion(self, event: MEvent) -> MStatus:
        """This method is called when the mouse pointer enters a screen panel region."""
    def doExitRegion(self, event: MEvent) -> MStatus:
        """Introduced in 2024.0"""
    @overload
    def doHold(self, event: MEvent, drawMgr: int, context: int) -> MStatus: ...
    @overload
    def doHold(self, event: MEvent) -> MStatus:
        """Not available in Python."""
    @overload
    def doPress(self, event: MEvent, drawMgr: int, context: int) -> MStatus: ...
    @overload
    def doPress(self, event: MEvent) -> MStatus:
        """Not available in Python."""
    @overload
    def doPtrMoved(self, event: MEvent, drawMgr: int, context: int) -> MStatus: ...
    @overload
    def doPtrMoved(self, event: MEvent) -> MStatus:
        """Not available in Python."""
    @overload
    def doRelease(self, event: MEvent, drawMgr: int, context: int) -> MStatus: ...
    @overload
    def doRelease(self, event: MEvent) -> MStatus:
        """Not available in Python."""
    def feedbackNumericalInput(self) -> bool:
        """This method is called to update the numerical feedback."""
    @staticmethod
    def getMarqueeSelection(xMin: float, yMin: float, xMax: float, yMax: float, mask: MSelectionMask, bPickSingle: bool, bIgnoreSelectionMode: bool, selectionList: MSelectionList) -> bool:
        """This method is called when the user performs a selection within the uv editor."""
    def helpStateHasChanged(self, event: MEvent) -> MStatus:
        """This method is called whenever the help state may need to be updated."""
    def image(self, index: Any) -> str:
        """This method is used to retrieve an XPM icon image that has previously been set for this tool context."""
    def inAlternateContext(self) -> bool:
        """Introduced in 2024.0"""
    def newToolCommand(self) -> MPxToolCommand:
        """Create a new instance of the tool command associated with this context."""
    def portSize(self, width: float, height: float) -> None:
        """This method is used to get the window dimension of the current uv viewport."""
    def portToView(self, xPort: Any, yPort: Any, xView: float, yView: float) -> None:
        """This method is used to convert port (window) coordinates to view coordinates."""
    def processNumericalInput(self, values: MDoubleArray, flags: MIntArray, isAbsolute: bool) -> bool:
        """This method processes the input from the numerical input field."""
    def setImage(self, image: str, index: Any) -> MStatus:
        """This method is used to set an XPM icon image that is to be used to represent this tool context in various places includi"""
    def stringClassName(self) -> str:
        """This method is called to determine the name that uniquely identifies the context."""
    def toolOffCleanup(self) -> None:
        """This method is called when the context is deactivated, i.e when another context is activated."""
    def toolOnSetup(self, event: MEvent) -> None:
        """This method is called when the context is activated, i.e when the toolButton for the context is pressed."""
    def viewRect(self, left: float, right: float, bottom: float, top: float) -> None:
        """This method is used to get the current uv viewport dimensions."""
    def viewToPort(self, xView: float, yView: float, xPort: Any, yPort: Any) -> None:
        """This method is used to convert view coordinates to port (window) coordinates."""

class MPxToolCommand:
    kDouble: Any
    kLong: Any
    kNoArg: Any
    kString: Any
    thisown: Any
    def __init__(self) -> None:
        """Class constructor."""
    @overload
    @staticmethod
    def appendToResult(val: int) -> None: ...
    @overload
    @staticmethod
    def appendToResult(val: float) -> None: ...
    @overload
    @staticmethod
    def appendToResult(val: bool) -> None: ...
    @overload
    @staticmethod
    def appendToResult(val: str) -> None: ...
    @overload
    @staticmethod
    def appendToResult(val: str) -> None: ...
    @overload
    @staticmethod
    def appendToResult(val: Any) -> None:
        """This method will add the given value to the end of the result array of integers."""
    def cancel(self) -> MStatus:
        """This method cancels the command."""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def clearResult() -> None:
        """Initializes the place where results from Maya commands get stored."""
    def commandString(self) -> str:
        """This method returns the command string that is associated with this command."""
    @staticmethod
    def currentDoubleResult() -> float:
        """This method gets the current node's result as a double, if possible."""
    @staticmethod
    def currentIntResult() -> int:
        """This method gets the current node's result as a int, if possible."""
    @staticmethod
    def currentResultType() -> Any:
        """This method will return the type of the current result for the command."""
    @staticmethod
    def currentStringResult() -> str:
        """This method gets the current node's result as a MString , if possible."""
    @staticmethod
    def displayError(theError: str, showLineNumber: bool = False) -> None:
        """This method is used to display an error in the script editor."""
    @staticmethod
    def displayInfo(theInfo: str) -> None:
        """This method is used to display information in the script editor."""
    @staticmethod
    def displayWarning(theWarning: str, showLineNumber: bool = False) -> None:
        """This method is used to display a warning in the script editor."""
    def doIt(self, args: MArgList) -> MStatus:
        """This method should perform a command by setting up internal class data and then calling the redoIt method."""
    def finalize(self) -> MStatus:
        """This method is used to create a string representing the command and its arguments."""
    @overload
    @staticmethod
    def getCurrentResult(val: int) -> MStatus: ...
    @overload
    @staticmethod
    def getCurrentResult(val: float) -> MStatus: ...
    @overload
    @staticmethod
    def getCurrentResult(val: str) -> MStatus: ...
    @overload
    @staticmethod
    def getCurrentResult(val: MIntArray) -> MStatus: ...
    @overload
    @staticmethod
    def getCurrentResult(val: MDoubleArray) -> MStatus: ...
    @overload
    @staticmethod
    def getCurrentResult(val: Any) -> MStatus:
        """Not available in Python."""
    def hasSyntax(self) -> bool:
        """This method specifies whether or not the command has a syntax object."""
    @staticmethod
    def isCurrentResultArray() -> bool:
        """This method will return whether the return result for the command is an array or not."""
    def isHistoryOn(self) -> bool:
        """Returns whether history is on."""
    def isUndoable(self) -> bool:
        """This method is used to specify whether or not the command is undoable."""
    def redoIt(self) -> MStatus:
        """This method should do the actual work of the command based on the internal class data only."""
    def setCommandString(self) -> MStatus:
        """Sets the command string that is associated with this command object."""
    def setHistoryOn(self, state: bool) -> MStatus:
        """This method specifies if history for this command is on."""
    @overload
    @staticmethod
    def setResult(val: int) -> None: ...
    @overload
    @staticmethod
    def setResult(val: int) -> None: ...
    @overload
    @staticmethod
    def setResult(val: float) -> None: ...
    @overload
    @staticmethod
    def setResult(val: bool) -> None: ...
    @overload
    @staticmethod
    def setResult(val: str) -> None: ...
    @overload
    @staticmethod
    def setResult(val: str) -> None: ...
    @overload
    @staticmethod
    def setResult(val: MIntArray) -> None: ...
    @overload
    @staticmethod
    def setResult(val: MDoubleArray) -> None: ...
    @overload
    @staticmethod
    def setResult(val: Any) -> None:
        """This method puts the given value into the return value area for a command."""
    def setUndoable(self, state: bool) -> MStatus:
        """Deprecated in 2019.0"""
    def syntax(self) -> Any:
        """This method is intended to be used in an MArgDataBase or MArgParser contructor when the plugin command's syntax is being"""
    def undoIt(self) -> MStatus:
        """This method should undo the work done by the redoIt method based on the internal class data only."""

class MPxTransform:
    baseTransformationMatrix: Any
    boundingBoxCenterX: Any
    boundingBoxCenterY: Any
    boundingBoxCenterZ: Any
    caching: Any
    center: Any
    displayHandle: Any
    displayLocalAxis: Any
    displayRotatePivot: Any
    displayScalePivot: Any
    drawOverride: Any
    dynamics: Any
    frozen: Any
    geometry: Any
    ghosting: Any
    identification: Any
    inheritsTransform: Any
    instObjGroups: Any
    intermediateObject: Any
    inverseMatrix: Any
    isHistoricallyInteresting: Any
    isTemplated: Any
    kAssembly: Any
    kBlendShape: Any
    kCameraSetNode: Any
    kClientDeviceNode: Any
    kConstraintNode: Any
    kDefaultScheduling: Any
    kDeformerNode: Any
    kDependNode: Any
    kEmitterNode: Any
    kEvaluatedDirectly: Any
    kEvaluatedIndirectly: Any
    kFieldNode: Any
    kFluidEmitterNode: Any
    kGeometryFilter: Any
    kGloballySerial: Any
    kGloballySerialize: Any
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
    kParallel: Any
    kParticleAttributeMapperNode: Any
    kPostEvaluationTypeLast: Any
    kSchedulingTypeLast: Any
    kSerial: Any
    kSerialize: Any
    kSkinCluster: Any
    kSpringNode: Any
    kSurfaceShape: Any
    kThreadedDeviceNode: Any
    kTransformNode: Any
    kUntrusted: Any
    layerOverrideColor: Any
    layerRenderable: Any
    lodVisibility: Any
    matrix: Any
    maxRotLimit: Any
    maxRotLimitEnable: Any
    maxRotXLimit: Any
    maxRotXLimitEnable: Any
    maxRotYLimit: Any
    maxRotYLimitEnable: Any
    maxRotZLimit: Any
    maxRotZLimitEnable: Any
    maxScaleLimit: Any
    maxScaleLimitEnable: Any
    maxScaleXLimit: Any
    maxScaleXLimitEnable: Any
    maxScaleYLimit: Any
    maxScaleYLimitEnable: Any
    maxScaleZLimit: Any
    maxScaleZLimitEnable: Any
    maxTransLimit: Any
    maxTransLimitEnable: Any
    maxTransXLimit: Any
    maxTransXLimitEnable: Any
    maxTransYLimit: Any
    maxTransYLimitEnable: Any
    maxTransZLimit: Any
    maxTransZLimitEnable: Any
    message: Any
    minRotLimit: Any
    minRotLimitEnable: Any
    minRotXLimit: Any
    minRotXLimitEnable: Any
    minRotYLimit: Any
    minRotYLimitEnable: Any
    minRotZLimit: Any
    minRotZLimitEnable: Any
    minScaleLimit: Any
    minScaleLimitEnable: Any
    minScaleXLimit: Any
    minScaleXLimitEnable: Any
    minScaleYLimit: Any
    minScaleYLimitEnable: Any
    minScaleZLimit: Any
    minScaleZLimitEnable: Any
    minTransLimit: Any
    minTransLimitEnable: Any
    minTransXLimit: Any
    minTransXLimitEnable: Any
    minTransYLimit: Any
    minTransYLimitEnable: Any
    minTransZLimit: Any
    minTransZLimitEnable: Any
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
    offsetParentMatrix: Any
    overrideColor: Any
    overrideDisplayType: Any
    overrideEnabled: Any
    overrideLevelOfDetail: Any
    overridePlayback: Any
    overrideShading: Any
    overrideTexturing: Any
    overrideVisibility: Any
    parentInverseMatrix: Any
    parentMatrix: Any
    renderInfo: Any
    renderLayerColor: Any
    renderLayerId: Any
    renderLayerInfo: Any
    renderLayerRenderable: Any
    rotate: Any
    rotateAxis: Any
    rotateAxisX: Any
    rotateAxisY: Any
    rotateAxisZ: Any
    rotateOrder: Any
    rotatePivot: Any
    rotatePivotTranslate: Any
    rotatePivotTranslateX: Any
    rotatePivotTranslateY: Any
    rotatePivotTranslateZ: Any
    rotatePivotX: Any
    rotatePivotY: Any
    rotatePivotZ: Any
    rotateQuaternion: Any
    rotateQuaternionW: Any
    rotateQuaternionX: Any
    rotateQuaternionY: Any
    rotateQuaternionZ: Any
    rotateX: Any
    rotateY: Any
    rotateZ: Any
    rotationInterpolation: Any
    scale: Any
    scalePivot: Any
    scalePivotTranslate: Any
    scalePivotTranslateX: Any
    scalePivotTranslateY: Any
    scalePivotTranslateZ: Any
    scalePivotX: Any
    scalePivotY: Any
    scalePivotZ: Any
    scaleX: Any
    scaleY: Any
    scaleZ: Any
    selectHandle: Any
    selectHandleX: Any
    selectHandleY: Any
    selectHandleZ: Any
    shear: Any
    shearXY: Any
    shearXZ: Any
    shearYZ: Any
    showManipDefault: Any
    specifiedManipLocation: Any
    state: Any
    thisown: Any
    transMinusRotatePivot: Any
    transMinusRotatePivotX: Any
    transMinusRotatePivotY: Any
    transMinusRotatePivotZ: Any
    translate: Any
    translateX: Any
    translateY: Any
    translateZ: Any
    useObjectColor: Any
    visibility: Any
    worldInverseMatrix: Any
    worldMatrix: Any
    xformMatrix: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self) -> None:
        """Class constructor."""
    @staticmethod
    def addAttribute(attr: MObject) -> MStatus:
        """This method adds a new attribute to a user defined node type during the type's initialization."""
    def addExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Adds content info to the specified table from a file path attribute."""
    def applyRotateOrientationLocks(self, toTest: MEulerRotation, savedRO: MEulerRotation) -> MEulerRotation:
        """This method allows the custom transform to apply its own locking mechanism to rotation orientation."""
    def applyRotatePivotLocks(self, toTest: MPoint, savedRP: MPoint) -> MVector:
        """This method allows the custom transform to apply its own locking mechanism to rotation pivots."""
    def applyRotatePivotLocksTranslate(self, toTest: MVector, savedRPT: MVector) -> MVector:
        """This method allows the custom transform to apply its own locking mechanism to the rotatePivotTranslate attribute."""
    def applyRotationLimits(self, unclampedR: MEulerRotation) -> MEulerRotation:
        """This method returns a copy of the passed rotation value with its members limited by any enabled rotation limits on this """
    def applyRotationLocks(self, toTest: MEulerRotation, savedR: MEulerRotation) -> MEulerRotation:
        """This method allows the custom transform to apply its own locking mechanism to rotation."""
    def applyScaleLimits(self, unclampedS: MVector) -> MVector:
        """This method returns a copy of the passed scale value with its members limited by any enabled scale limits on this node."""
    def applyScaleLocks(self, toTest: MVector, savedS: MVector) -> MVector:
        """This method allows the custom transform to apply its own locking mechanism to scale."""
    def applyScaleLocksPivot(self, toTest: MPoint, savedSP: MPoint) -> MVector:
        """This method allows the custom transform to apply its own locking mechanism to scale pivot."""
    def applyScaleLocksPivotTranslate(self, toTest: MVector, savedSPT: MVector) -> MVector:
        """This method allows the custom transform to apply its own locking mechanism to the scalePivotTranslate attribute."""
    def applyShearLocks(self, toTest: MVector, savedSh: MVector) -> MVector:
        """This method allows the custom transform to apply its own locking mechanism to shear."""
    def applyTranslationLimits(self, unclampedT: MVector) -> MVector:
        """This method returns a copy of the passed translation value with its members limited by any enabled translation limits on"""
    def applyTranslationLocks(self, toTest: MVector, savedT: MVector) -> MVector:
        """This method allows the custom transform to apply its own locking mechanism to translation."""
    def assign(self, other: MPxTransform) -> None: ...
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> MStatus: ...
    @overload
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject, affectsTopology: bool) -> MStatus:
        """This method specifies that a particular input attribute affects a specific output attribute."""
    def boundingBox(self) -> MBoundingBox:
        """This method should be overridden to return a bounding box for the transform."""
    def checkAndSetRotateOrientation(self, Space: int | None = None, balance: bool = True) -> MStatus:
        """This method verifies that the passed value can be set on the rotateAxis plugs."""
    def checkAndSetRotatePivot(self, Space: int | None = None, balance: bool = True) -> MStatus:
        """This method verifies that the passed value can be set on the rotatePivot plugs."""
    def checkAndSetRotatePivotTranslation(self, Space: int | None = None) -> MStatus:
        """This method verifies that the passed value can be set on the rotatePivotTranslate plugs."""
    def checkAndSetRotation(self, Space: int | None = None) -> MStatus:
        """This method verifies that the passed value can be set on the rotate plugs."""
    def checkAndSetScale(self, Space: int | None = None) -> MStatus:
        """This method verifies that the passed value can be set on the scale plugs."""
    def checkAndSetScalePivot(self, Space: int | None = None, arg: Any = True) -> MStatus:
        """This method verifies that the passed value can be set on the scalePivot plugs."""
    def checkAndSetScalePivotTranslation(self, Space: int | None = None) -> MStatus:
        """This method verifies that the passed value can be set on the scalePivotTranslate plugs."""
    def checkAndSetShear(self, Space: int | None = None) -> MStatus:
        """This method verifies that the passed value can be set on the shear plugs."""
    def checkAndSetTranslation(self, Space: int | None = None) -> MStatus:
        """This method is used to modify and set the new translate values being passed in from the compute method or from the valid"""
    @overload
    @staticmethod
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def clearLimits(self) -> MStatus:
        """This method turns off all of the limits and sets them to their default values."""
    def compute(self, plug: MPlug, data: MDataBlock) -> MStatus:
        """The transform's compute method."""
    def computeLocalTransformation(self) -> MStatus:
        """This method computes the transformation matrix for a passed data block and places the output into a passed transformatio"""
    def configCache(self) -> None:
        """Introduced in 2020.0"""
    def connectionBroken(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, asSrc: bool) -> MStatus:
        """This method gets called when connections are made to attributes of this node."""
    def copyInternalData(self) -> None:
        """This function copies the internal data of the transform node."""
    def createTransformationMatrix(self) -> MPxTransformationMatrix:
        """This method returns a new transformation matrix."""
    def dependsOn(self, depends: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def enableLimit(self, LimitType: int, flag: bool) -> MStatus:
        """Enable or disable the limit value for the specified limit type."""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    def getCacheSetup(self) -> None:
        """Introduced in 2020.0"""
    @overload
    def getEulerRotation(self, Space: int | None = None) -> MEulerRotation: ...
    @overload
    def getEulerRotation(self, Space: int) -> MEulerRotation:
        """Returns the rotation component of the transform as a euler rotation."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> None:
        """Returns the external content (files) that this node depends on."""
    def getFilesToArchive(self, shortName: bool = False, unresolvedName: bool = False, markCouldBeImageSequence: bool = False) -> Any:
        """Use this method to return all external files used by this node."""
    def getInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def getInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    @overload
    def getMatrix(self) -> MMatrix: ...
    @overload
    def getMatrix(self) -> MMatrix:
        """This method returns a 4x4 matrix that is produced by applying all of the components of the transform."""
    @overload
    def getMatrixInverse(self) -> MMatrix: ...
    @overload
    def getMatrixInverse(self) -> MMatrix:
        """This method returns the inverse of the 4x4 matrix that describes this transformation in the current evaluation context."""
    def getPreRotation(self) -> MQuaternion:
        """This methods returns preRotation, which is an optional rotation that can be applied after the rotation channel and befor"""
    @overload
    def getRotateOrientation(self, apiSpace: int | None = None) -> MQuaternion: ...
    @overload
    def getRotateOrientation(self, apiSpace: int, apiContext: MDGContext) -> MQuaternion:
        """Returns the rotate orientation for the transformation matrix as a quaternion."""
    @overload
    def getRotatePivot(self, Space: int | None = None) -> MPoint: ...
    @overload
    def getRotatePivot(self, Space: int) -> MPoint:
        """This method returns the position of the pivot used by the rotate component of the transform."""
    @overload
    def getRotatePivotTranslation(self, Space: int | None = None) -> MVector: ...
    @overload
    def getRotatePivotTranslation(self, Space: int) -> MVector:
        """This method returns the rotate pivot translation in internal units (centimeters)."""
    @overload
    def getRotation(self, Space: int | None = None) -> MQuaternion: ...
    @overload
    def getRotation(self, Space: int) -> MQuaternion:
        """This method returns the rotation of the transform as a quaternion."""
    @overload
    def getRotationOrder(self) -> int: ...
    @overload
    def getRotationOrder(self) -> int:
        """Returns the rotation order used by the rotation component of the transformation matrix."""
    @overload
    def getScale(self, Space: int | None = None) -> MVector: ...
    @overload
    def getScale(self, Space: int) -> MVector:
        """Returns the scale component of the transform."""
    @overload
    def getScalePivot(self, Space: int | None = None) -> MPoint: ...
    @overload
    def getScalePivot(self, Space: int) -> MPoint:
        """This method returns the position of the pivot used by the scale component of the transform."""
    @overload
    def getScalePivotTranslation(self, Space: int | None = None) -> MVector: ...
    @overload
    def getScalePivotTranslation(self, Space: int) -> MVector:
        """This method returns the scale pivot translation in internal units (centimeters)."""
    @overload
    def getShear(self, Space: int | None = None) -> MVector: ...
    @overload
    def getShear(self, Space: int) -> MVector:
        """Get the shear value for this transform."""
    @overload
    def getTranslation(self, Space: int | None = None) -> MVector: ...
    @overload
    def getTranslation(self, Space: int) -> MVector:
        """This method returns the translation component of the transform as a MVector in internal units (centimeters)."""
    def hasInvalidationRangeTransformation(self) -> bool:
        """Introduced in 2020.0"""
    @staticmethod
    def inheritAttributesFrom(parentClassName: str) -> MStatus:
        """This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node."""
    @overload
    def internalArrayCount(self) -> int: ...
    @overload
    def internalArrayCount(self) -> int:
        """This method is overridden by nodes that have internal array attributes which are not stored in Maya's datablock."""
    def isAbstractClass(self) -> bool:
        """Override this class to return true if this node is an abstract node."""
    def isBounded(self) -> bool:
        """This method should be overridden to return true if the user supplies a bounding box routine."""
    def isLimited(self, LimitType: int) -> bool:
        """Determine if the specified limit attribute is enabled or disabled."""
    @staticmethod
    def isNonAffineMatricesEnabled() -> bool:
        """This method returns true is non-affine matrix calculations are being used for transforms."""
    def isPassiveOutput(self) -> bool:
        """This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent val"""
    def isTrackingTopology(self) -> bool:
        """Introduced in 2019.0"""
    def legalConnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal connections being made to attributes of this node."""
    def legalDisconnection(self, asSrc: bool, isLegal: bool) -> MStatus:
        """This method allows you to check for legal disconnections being made to attributes of this node."""
    def limitValue(self, LimitType: int) -> float:
        """Returns the current value of the specified limit in internal units as a double."""
    @staticmethod
    def mustCallValidateAndSet() -> None:
        """This method must be called in the initialize() method for all attributes that affect the matrix of the transform."""
    def name(self) -> str:
        """Returns the name of this particular instance of this class."""
    def passThroughToMany(self) -> bool:
        """This method is overridden by nodes that want to control the traversal behavior of some Maya search algorithms which trav"""
    def passThroughToOne(self) -> MPlug:
        """This method may be overridden by nodes that have a one-to-one relationship between an input attribute and a correspondin"""
    def postConstructor(self) -> None:
        """Post constructor."""
    def postEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode, evalType: Any) -> MStatus:
        """Clean up node's internal state after threaded evaluation."""
    def preEvaluation(self, context: MDGContext, evaluationNode: MEvaluationNode) -> MStatus:
        """Prepare a node's internal state for threaded evaluation."""
    @overload
    def resetTransformation(self) -> None: ...
    @overload
    def resetTransformation(self) -> None:
        """This method will reset the transformation matrix to one that is constructed with the passed MMatrix ."""
    @overload
    def rotateBy(self, Space: int | None = None) -> MStatus: ...
    @overload
    def rotateBy(self, Space: int | None = None) -> MStatus: ...
    @overload
    def rotateBy(self, Space: int) -> MStatus: ...
    @overload
    def rotateBy(self, Space: int) -> MStatus:
        """Adds to the rotation component of the transform by rotating relative to the existing transformation using a quaternion."""
    @overload
    def rotateTo(self, Space: int | None = None) -> MStatus: ...
    @overload
    def rotateTo(self, Space: int | None = None) -> MStatus: ...
    @overload
    def rotateTo(self, Space: int) -> MStatus: ...
    @overload
    def rotateTo(self, Space: int) -> MStatus:
        """Sets the rotation component of the transform using a quaternion."""
    @overload
    def scaleBy(self, Space: int | None = None) -> MStatus: ...
    @overload
    def scaleBy(self, Space: int) -> MStatus:
        """This method will apply a relative scale to an existing scale."""
    @overload
    def scaleTo(self, Space: int | None = None) -> MStatus: ...
    @overload
    def scaleTo(self, Space: int) -> MStatus:
        """This method will set the scale of the transform to the passed value."""
    def schedulingType(self) -> Any:
        """When overridden this method controls the degree of parallelism supported by the node during threaded evaluation."""
    def setDependentsDirty(self, plug: MPlug, plugArray: MPlugArray) -> MStatus:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug """
    def setExistWithoutInConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without input connections."""
    def setExistWithoutOutConnections(self, flag: bool) -> MStatus:
        """This method specifies whether or not the node can exist without output connections."""
    def setExternalContent(self) -> None:
        """Changes the location of external content in batch."""
    def setExternalContentForFileAttr(self, attr: MObject) -> bool:
        """Sets content info in the specified attribute from the table."""
    def setInternalValue(self) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self) -> bool:
        """Deprecated in 2018.0"""
    def setLimit(self, LimitType: int, value: float) -> MStatus:
        """Change the limit value for the specified limit type, and automatically enable the limit to be true."""
    @staticmethod
    def setNonAffineMatricesEnabled(arg: Any) -> MStatus:
        """Normal Maya transforms consist of translate, rotate, scale, and shear."""
    @overload
    def setRotateOrientation(self, q: MQuaternion, apiSpace: int | None = None, balance: bool = True) -> MStatus: ...
    @overload
    def setRotateOrientation(self, q: MQuaternion, Space: int, balance: bool) -> MStatus:
        """This method sets the rotate orientation for this transform."""
    @overload
    def setRotatePivot(self, Space: int | None = None, balance: bool = True) -> MStatus: ...
    @overload
    def setRotatePivot(self, Space: int, balance: bool) -> MStatus:
        """This method sets the position of the rotate pivot."""
    @overload
    def setRotatePivotTranslation(self, Space: int | None = None) -> MStatus: ...
    @overload
    def setRotatePivotTranslation(self, Space: int) -> MStatus:
        """This method sets the rotate pivot translation in internal units (centimeters)."""
    @overload
    def setRotationOrder(self, ro: int, reorder: bool = True) -> MStatus: ...
    @overload
    def setRotationOrder(self, RotationOrder: int, reorder: bool) -> MStatus:
        """Sets the rotation order used by the rotation component of the transformation matrix."""
    @overload
    def setScalePivot(self, Space: int | None = None, balance: bool = True) -> MStatus: ...
    @overload
    def setScalePivot(self, Space: int, balance: bool) -> MStatus:
        """This method sets the position of the scale pivot."""
    @overload
    def setScalePivotTranslation(self, Space: int | None = None) -> MStatus: ...
    @overload
    def setScalePivotTranslation(self, Space: int) -> MStatus:
        """This method sets the scale pivot translation in internal units (centimeters)."""
    @overload
    def shearBy(self, Space: int | None = None) -> MStatus: ...
    @overload
    def shearBy(self, Space: int) -> MStatus:
        """This method will apply a relative shear to the existing shear."""
    @overload
    def shearTo(self, Space: int | None = None) -> MStatus: ...
    @overload
    def shearTo(self, Space: int) -> MStatus:
        """The method sets the shear component of the transform."""
    def shouldSave(self, isSaving: bool) -> MStatus:
        """This method may be overridden by the user defined node."""
    def thisMObject(self) -> MObject:
        """Returns the MObject associated with this user defined node."""
    def transformInvalidationRange(self, source: MPlug, input: MTimeRange) -> MTimeRange:
        """Introduced in 2020.0"""
    def transformationMatrix(self) -> MPxTransformationMatrix:
        """This method returns a reference to the cached transformation matrix for current context."""
    def transformationMatrixPtr(self) -> MPxTransformationMatrix:
        """This function returns a pointer to the cached transformation matrix for current context."""
    @overload
    def translateBy(self, Space: int | None = None) -> MStatus: ...
    @overload
    def translateBy(self, Space: int) -> MStatus:
        """Add to the translation component by translating relative to the existing transform."""
    @overload
    def translateTo(self, Space: int | None = None) -> MStatus: ...
    @overload
    def translateTo(self, Space: int) -> MStatus:
        """Set the translation component of the transform in centimeters."""
    def treatAsTransform(self) -> bool:
        """Maya's base transform node type is treated differently from node types which are derived from it."""
    def type(self) -> int:
        """This method returns the type of the node."""
    def typeId(self) -> MTypeId:
        """Returns the TYPEID of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""
    @overload
    def updateMatrixAttrs(self) -> MStatus: ...
    @overload
    def updateMatrixAttrs(self, attr: MObject) -> MStatus: ...
    @overload
    def updateMatrixAttrs(self) -> MStatus: ...
    @overload
    def updateMatrixAttrs(self, attr: MObject) -> MStatus:
        """This method is used only for the MPxTransform and MPxTransform derived classes."""
    @overload
    def validateAndSetValue(self) -> MStatus: ...
    @overload
    def validateAndSetValue(self) -> MStatus:
        """When a plug's value is set, and the plug is on a default transform attribute, or has been flagged by the mustCallValidat"""

class MPxTransformationMatrix:
    baseTransformationMatrixId: Any
    identity: Any
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self) -> None:
        """Class Constructor."""
    def asInterpolationMatrix(self, toM: MTransformationMatrix, percent: float, rot: bool, direction: int = 0) -> MMatrix:
        """Returns a matrix that represents the specified percentage of this transformation matrix."""
    @overload
    def asMatrix(self) -> MMatrix: ...
    @overload
    def asMatrix(self, percent: float) -> MMatrix:
        """Returns the four by four matrix that describes this transformation."""
    def asMatrixInverse(self) -> MMatrix:
        """Returns the inverse of the four by four matrix that describes this transformation."""
    def asRotateMatrix(self) -> MMatrix:
        """Returns the rotate section of the transformation matrix."""
    def asRotateMatrixInverse(self) -> MMatrix:
        """Returns the inverse of the rotate matrix."""
    def asScaleMatrix(self) -> MMatrix:
        """Returns scale matrix."""
    def asScaleMatrixInverse(self) -> MMatrix:
        """Returns inverse of the scale matrix."""
    def asTransformationMatrix(self) -> MTransformationMatrix:
        """Returns the custom transformation matrix as a standard MTransformationMatrix ."""
    def assign(self, other: MPxTransformationMatrix) -> None: ...
    @staticmethod
    def convertEulerRotationOrder(RotationOrder: int) -> int:
        """Convert from MEulerRotation::RotationOrder to MTransformationMatrix::RotationOrder ."""
    @staticmethod
    def convertTransformationRotationOrder(RotationOrder: int) -> int:
        """Convert from MTransformationMatrix::RotationOrder to MEulerRotation::RotationOrder ."""
    def copyValues(self) -> None:
        """This method should be overridden for any transform that uses more then the default transform values."""
    @staticmethod
    def creator() -> MPxTransformationMatrix:
        """A method to use when registering a custom transform that uses a default MPxTransformationMatrix ."""
    def decomposeMatrix(self) -> MStatus:
        """This method converts a passed MMatrix into individual transformation matrix components."""
    def eulerRotateOrientation(self, Space: int | None = None) -> MEulerRotation:
        """Returns the rotate orientation for the transformation matrix as an euler rotation."""
    def eulerRotation(self, space: int | None = None) -> MEulerRotation:
        """Returns the rotation component of the transformation matrix as a euler rotation."""
    @overload
    def isEquivalent(self, tolerance: float) -> bool: ...
    @overload
    def isEquivalent(self, tolerance: float) -> bool: ...
    @overload
    def isEquivalent(self, tolerance: float) -> bool:
        """Determine if the MPxTransformationMatrix is equivalent within a specified tolerance."""
    def preRotation(self) -> MQuaternion:
        """This methods returns preRotation, which is an optional rotation that can be applied after the rotation channel and befor"""
    def reverse(self) -> MPxTransformationMatrix:
        """Returns the negated translate, rotate, and scale without taking the pivots into account."""
    @overload
    def rotateBy(self, q: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def rotateBy(self, e: MEulerRotation, Space: int | None = None) -> MStatus:
        """Rotates relative to the current rotation value of the transformation matrix."""
    def rotateOrientation(self, Space: int | None = None) -> MQuaternion:
        """Returns the rotate orientation for the transformation matrix as a quaternion."""
    def rotatePivot(self, Space: int | None = None) -> MPoint:
        """Returns the pivot used by the rotation."""
    def rotatePivotTranslation(self, Space: int | None = None) -> MVector:
        """Returns the rotate pivot translation, which is used to compensate for changes of the rotate pivot."""
    @overload
    def rotateTo(self, q: MQuaternion, Space: int | None = None) -> MStatus: ...
    @overload
    def rotateTo(self, e: MEulerRotation, Space: int | None = None) -> MStatus:
        """Sets the rotation component of the transformation matrix using a quaternion."""
    def rotation(self, Space: int | None = None) -> MQuaternion:
        """Returns the rotation component of the transformation matrix as a quaternion."""
    def rotationOrder(self) -> int:
        """Returns the rotation order used by the rotation component of the transformation matrix."""
    def scale(self, Space: int | None = None) -> MVector:
        """Returns the scale component of the transformation matrix."""
    def scaleBy(self, Space: int | None = None) -> MStatus:
        """Apply a relative scale to the existing scale."""
    def scalePivot(self, Space: int | None = None) -> MPoint:
        """Returns the pivot used by the scale."""
    def scalePivotTranslation(self, Space: int | None = None) -> MVector:
        """Returns the scale pivot translation, which is used to compensate for changes of the scale pivot."""
    def scaleTo(self, Space: int | None = None) -> MStatus:
        """Set the scale component of the transformation matrix."""
    @overload
    def setRotateOrientation(self, q: MQuaternion, Space: int | None = None, balance: bool = True) -> MStatus: ...
    @overload
    def setRotateOrientation(self, euler: MEulerRotation, Space: int | None = None, balance: bool = True) -> MStatus:
        """Sets the rotate orientation for the transformation matrix to the passed quaternion."""
    def setRotatePivot(self, Space: int | None = None, balance: bool = True) -> MStatus:
        """Set the pivot used by the rotation."""
    def setRotatePivotTranslation(self, vector: MVector, Space: int | None = None) -> MStatus:
        """Set the rotate pivot translation."""
    def setRotationOrder(self, RotationOrder: int, preserve: bool = True) -> MStatus:
        """Sets the rotation order used by the rotation component of the transformation matrix."""
    def setScalePivot(self, Space: int | None = None, balance: bool = True) -> MStatus:
        """Set the pivot used by the scale."""
    def setScalePivotTranslation(self, vector: MVector, Space: int | None = None) -> MStatus:
        """Set the scale pivot translation."""
    def shear(self, Space: int | None = None) -> MVector:
        """Returns the shear component of the transformation matrix."""
    def shearBy(self, shear: MVector, Space: int | None = None) -> MStatus:
        """Apply a new shear to the existing shear component of the transformation matrix."""
    def shearTo(self, shear: MVector, Space: int | None = None) -> MStatus:
        """Sets the shear component of the transformation matrix."""
    def transformBy(self) -> MPxTransformationMatrix:
        """Transforms the transformation matrix by the passed MTransformationMatrix ."""
    def translateBy(self, vector: MVector, Space: int | None = None) -> MStatus:
        """Add to the translate component by translating relative to the existing transformation."""
    def translateTo(self, vector: MVector, Space: int | None = None) -> MStatus:
        """Sets the translate component of the transformation matrix in centimeters."""
    def translation(self, Space: int | None = None) -> MVector:
        """Returns the translation component of the transformation matrix as a MVector in centimeters (the internal Maya linear uni"""
    def typeId(self) -> MTypeId:
        """Returns the MTypeId of this transformation matrix."""
    def unSquishIt(self) -> MStatus:
        """Remove any shearing and any non-proportional scaling from this transform."""
    def unSquishMatrix(self) -> MMatrix:
        """Remove any shearing and any non-proportional scaling."""

class MPxUIControl:
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def className(self, *args: Any, **kwargs: Any) -> Any: ...

class MPxUITableControl:
    kAllLabels: Any
    kColumnLabel: Any
    kNoLabel: Any
    kRowLabel: Any
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def addToSelection(self, *args: Any, **kwargs: Any) -> Any: ...
    def allowEdit(self, *args: Any, **kwargs: Any) -> Any: ...
    def allowSelection(self, *args: Any, **kwargs: Any) -> Any: ...
    def cellString(self, *args: Any, **kwargs: Any) -> Any: ...
    def className(self, *args: Any, **kwargs: Any) -> Any: ...
    def clearSelection(self, *args: Any, **kwargs: Any) -> Any: ...
    def collapseOrExpandRow(self, *args: Any, **kwargs: Any) -> Any: ...
    def getCellColor(self, *args: Any, **kwargs: Any) -> Any: ...
    def isSelected(self, *args: Any, **kwargs: Any) -> Any: ...
    def labelString(self, *args: Any, **kwargs: Any) -> Any: ...
    def numberOfColumns(self, *args: Any, **kwargs: Any) -> Any: ...
    def numberOfRows(self, *args: Any, **kwargs: Any) -> Any: ...
    def redrawCells(self, *args: Any, **kwargs: Any) -> Any: ...
    def redrawLabels(self, *args: Any, **kwargs: Any) -> Any: ...
    def removeFromSelection(self, *args: Any, **kwargs: Any) -> Any: ...
    def setNumberOfColumns(self, *args: Any, **kwargs: Any) -> Any: ...
    def setNumberOfRows(self, *args: Any, **kwargs: Any) -> Any: ...
    def setSelection(self, *args: Any, **kwargs: Any) -> Any: ...
    def suspendUpdates(self, *args: Any, **kwargs: Any) -> Any: ...

class MaterialInputData:
    ambient: Any
    diffuse: Any
    emission: Any
    hasTransparency: Any
    shininess: Any
    specular: Any
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

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

def asHashable(*args: Any, **kwargs: Any) -> Any: ...
def asMPxPtr(*args: Any, **kwargs: Any) -> Any: ...
def getLockCaptureCount(*args: Any, **kwargs: Any) -> Any: ...