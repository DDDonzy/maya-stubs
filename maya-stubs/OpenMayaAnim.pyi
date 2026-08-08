# Stub for maya.OpenMayaAnim - OM1, signatures from Maya 2024 C++ API reference
from typing import Any, overload

from maya.OpenMaya import MAngle
from maya.OpenMaya import MCallbackIdArray
from maya.OpenMaya import MColor
from maya.OpenMaya import MDGModifier
from maya.OpenMaya import MDagPath
from maya.OpenMaya import MDagPathArray
from maya.OpenMaya import MDoubleArray
from maya.OpenMaya import MEulerRotation
from maya.OpenMayaMPx import MExternalContentInfoTable
from maya.OpenMayaMPx import MExternalContentLocationTable
from maya.OpenMaya import MFloatArray
from maya.OpenMaya import MIntArray
from maya.OpenMaya import MMatrix
from maya.OpenMaya import MObject
from maya.OpenMaya import MObjectArray
from maya.OpenMaya import MPlug
from maya.OpenMaya import MPlugArray
from maya.OpenMaya import MPoint
from maya.OpenMaya import MQuaternion
from maya.OpenMaya import MSelectionList
from maya.OpenMaya import MTime
from maya.OpenMaya import MTimeArray
from maya.OpenMaya import MTransformationMatrix
from maya.OpenMaya import MTypeId
from maya.OpenMaya import MUuid
from maya.OpenMaya import MVector

class MStatus:
    ...

class MAnimControl:
    kPlaybackLoop: Any
    kPlaybackOnce: Any
    kPlaybackOscillate: Any
    kPlaybackViewActive: Any
    kPlaybackViewAll: Any
    thisown: Any
    def __init__(self) -> None:
        """Class constructor."""
    @staticmethod
    def animationEndTime() -> MTime:
        """Return an MTime specifying the last frame of the animation, as specified by the Maya user in the Range Slider UI."""
    @staticmethod
    def animationStartTime() -> MTime:
        """Return an MTime specifying the first frame of the animation, as specified by the Maya user in the Range Slider UI."""
    @staticmethod
    def autoKeyMode() -> bool:
        """Return the autoKeyMode."""
    @staticmethod
    def currentTime() -> MTime:
        """Return an MTime instance containing the current animation frame."""
    @staticmethod
    def globalInTangentType() -> int:
        """Return the current global in tangent type."""
    @staticmethod
    def globalOutTangentType() -> int:
        """Return the current global out tangent type."""
    @staticmethod
    def isPlaying() -> bool:
        """Return a value indicating whether Maya is currently playing the animation."""
    @staticmethod
    def isScrubbing() -> bool:
        """Return a value indicating whether interactive scrubbing is occuring while Maya is not currently playing an animation."""
    @staticmethod
    def isValid() -> bool:
        """Introduced in 2020.0"""
    @staticmethod
    def maxTime() -> MTime:
        """Return an MTime specifying the last frame of the current playback time range."""
    @staticmethod
    def minTime() -> MTime:
        """Return an MTime specifying the first frame of the current playback time range."""
    @staticmethod
    def playBackward() -> MStatus:
        """Start playing the current animation backwards."""
    @staticmethod
    def playForward() -> MStatus:
        """Start playing the current animation forwards."""
    @staticmethod
    def playbackBy() -> float:
        """Return a double specifying the increment between times viewed during the playing of the animation."""
    @staticmethod
    def playbackMode() -> int:
        """Return the playback mode currently in effect."""
    @staticmethod
    def playbackSpeed() -> float:
        """Return the speed with with to play the animation."""
    @staticmethod
    def setAnimationEndTime(newEndTime: MTime) -> MStatus:
        """Set the value of the last frame in the animation."""
    @staticmethod
    def setAnimationStartEndTime(newStartTime: MTime, newEndTime: MTime) -> MStatus:
        """Set the values of the first and last frames in the animation."""
    @staticmethod
    def setAnimationStartTime(newStartTime: MTime) -> MStatus:
        """Set the value of the first frame in the animation."""
    @staticmethod
    def setAutoKeyMode(mode: bool) -> MStatus:
        """Set the autoKeyMode."""
    @staticmethod
    def setCurrentTime(newTime: MTime) -> MStatus:
        """Set the current animation frame."""
    @staticmethod
    def setGlobalInTangentType(tangentType: int) -> MStatus:
        """Set the current global in tangent type."""
    @staticmethod
    def setGlobalOutTangentType(tangentType: int) -> MStatus:
        """Set the current global out tangent type."""
    @staticmethod
    def setMaxTime(newMaxTime: MTime) -> MStatus:
        """Set the value of the last frame of the current playback time range."""
    @staticmethod
    def setMinMaxTime(min: MTime, max: MTime) -> MStatus:
        """Set the values of the first and last frames of the playback time range."""
    @staticmethod
    def setMinTime(newMinTime: MTime) -> MStatus:
        """Set the first frame of the current playback time range."""
    @staticmethod
    def setPlaybackBy(newTime: float) -> MStatus:
        """Specify the increment between times viewed during the playing of the animation."""
    @staticmethod
    def setPlaybackMode(newMode: Any) -> MStatus:
        """Set the current playback mode."""
    @staticmethod
    def setPlaybackSpeed(newSpeed: float) -> MStatus:
        """Set the desired speed factor at which the animation will play back."""
    @staticmethod
    def setViewMode(newMode: Any) -> MStatus:
        """Set the current viewing mode."""
    @staticmethod
    def setWeightedTangents(weightState: bool) -> MStatus:
        """Sets whether or not the tangents on the Anim Curve are weighted."""
    @staticmethod
    def stop() -> MStatus:
        """Stop playing the current animation."""
    @staticmethod
    def viewMode() -> int:
        """Return the viewing mode currently in effect."""
    @staticmethod
    def weightedTangents() -> bool:
        """Determine whether or not the tangents on the Anim Curve are weighted."""

class MAnimCurveChange:
    thisown: Any
    def __init__(self) -> None:
        """Class Constructor."""
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def isInteractive(self) -> bool:
        """Return the performance hint flag value."""
    def redoIt(self) -> MStatus:
        """Redoes all of the Anim Curve edits that this cache previously undid."""
    def setInteractive(self, value: bool) -> None:
        """The interactive flag is a performance hint."""
    def undoIt(self) -> MStatus:
        """Undoes all of the Anim Curve edits that have been given to this cache."""

class MAnimCurveClipboard:
    thisown: Any
    def __init__(self) -> None:
        """Default Constructor."""
    def clear(self) -> MStatus:
        """This method empties the clipboard."""
    def clipboardItems(self) -> MAnimCurveClipboardItemArray:
        """Returns the contents of the clipboard."""
    def endTime(self) -> MTime:
        """Returns the end time of the clipboard."""
    def endUnitlessInput(self) -> float:
        """Returns the end unitless input of the clipboard."""
    def isEmpty(self) -> bool:
        """Determines if the clipboard is empty."""
    @overload
    def set(self, cb: MAnimCurveClipboard) -> MStatus: ...
    @overload
    def set(self, clipboardItemArray: MAnimCurveClipboardItemArray) -> MStatus: ...
    @overload
    def set(self, clipboardItemArray: MAnimCurveClipboardItemArray, startTime: MTime, endTime: MTime, startUnitlessInput: float, endUnitlessInput: float, strictValidation: bool = True) -> MStatus:
        """Replaces the contents of the clipboard."""
    def startTime(self) -> MTime:
        """Returns the start time of the clipboard."""
    def startUnitlessInput(self) -> float:
        """Returns the start unitless input of the clipboard."""
    @staticmethod
    def theAPIClipboard() -> MAnimCurveClipboard:
        """Returns the static API clipboard."""

class MAnimCurveClipboardItem:
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, r: MAnimCurveClipboardItem) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self) -> None:
        """Default Constructor."""
    def animCurve(self) -> MObject:
        """Returns the animCurve held by this clipboard item as an MObject ."""
    def animCurveType(self) -> int:
        """Returns the animCurve type."""
    def assign(self, other: MAnimCurveClipboardItem) -> None: ...
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def fullAttributeName(self) -> str:
        """Returns the attribute's full name."""
    def getAddressingInfo(self, rowCount: int, childCount: int, attributeCount: int) -> MStatus:
        """Returns the addressing information for this clipboard item,."""
    def leafAttributeName(self) -> str:
        """Returns the attribute's leaf name."""
    def nodeName(self) -> str:
        """Returns the node name."""
    def setAddressingInfo(self, rowCount: int, childCount: int, attributeCount: int) -> MStatus:
        """Sets the clipboard item's addressing info."""
    def setAnimCurve(self, curve: MObject) -> MStatus:
        """Sets the clipboard item's animCurve."""
    def setNameInfo(self, nodeName: str, fullName: str, leafName: str) -> MStatus:
        """Sets the clipboard item's name info."""

class MAnimCurveClipboardItemArray:
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: MAnimCurveClipboardItemArray) -> None: ...
    @overload
    def __init__(self, initialSize: int, initialValue: MAnimCurveClipboardItem) -> None: ...
    @overload
    def __init__(self, count: int) -> None: ...
    @overload
    def __init__(self) -> None:
        """Default Constructor."""
    def append(self, element: MAnimCurveClipboardItem) -> MStatus:
        """Adds a new element to the end of the array."""
    def assign(self, other: MAnimCurveClipboardItemArray) -> None: ...
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def clear(self) -> MStatus:
        """Clear the contents of the array."""
    def copy(self, source: MAnimCurveClipboardItemArray) -> MStatus:
        """Copy the contents of the source array to this array."""
    def insert(self, element: MAnimCurveClipboardItem, index: int) -> MStatus:
        """Inserts a new value into the array at the given index."""
    def isValid(self, failedIndex: int) -> bool:
        """Ensures that the MAnimCurveClipboard items in the array make sense."""
    def length(self) -> int:
        """Returns the number of elements in the instance."""
    def remove(self, index: int) -> MStatus:
        """Remove the array element at the given index."""
    def set(self, element: MAnimCurveClipboardItem, index: int) -> MStatus:
        """Sets the value of the indicated element to the indicated MAnimCurveClipboardItem value."""
    def setLength(self, length: int) -> MStatus:
        """Set the length of the array."""
    def setSizeIncrement(self, newIncrement: int) -> None:
        """Set the size by which the array will be expanded whenever expansion is necessary."""
    def sizeIncrement(self) -> int:
        """Return the size by which the array will be expanded whenever expansion is necessary."""

class MAnimMessage:
    kDefaultAction: Any
    kDoAction: Any
    kDoNotDoAction: Any
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @staticmethod
    def addAnimCurveEditedCallback(func: int, clientData: None = None) -> Any:
        """AnimCurve edited callback."""
    @staticmethod
    def addAnimKeyframeEditCheckCallback(func: int, clientData: None = None) -> Any:
        """AnimCurve keyframe edit check callback."""
    @overload
    @staticmethod
    def addAnimKeyframeEditedCallback(func: int, clientData: None = None) -> Any: ...
    @overload
    @staticmethod
    def addAnimKeyframeEditedCallback(animNode: MObject, func: int, clientData: None = None) -> Any:
        """AnimCurve keyframe edited callback."""
    @staticmethod
    def addDisableImplicitControlCallback(func: int, clientData: None = None) -> Any:
        """Disable Implicit Control callback."""
    @staticmethod
    def addNodeAnimKeyframeEditedCallback(animNode: MObject, func: int, clientData: None = None) -> Any:
        """AnimCurve keyframe edited callback."""
    @staticmethod
    def addPostBakeResultsCallback(func: int, clientData: None = None) -> Any:
        """Post Bake Simulation callback."""
    @staticmethod
    def addPreBakeResultsCallback(func: int, clientData: None = None) -> Any:
        """Pre Bake Simulation callback."""
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
    def flushAnimKeyframeEditedCallbacks() -> None:
        """AnimCurve keyframe edited callback flush."""
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

class MAnimUtil:
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def findAnimatablePlugs(selectionList: MSelectionList, animatablePlugs: MPlugArray) -> bool:
        """Find the list of attributes (MPlugs) on any member of an MSelectionList that is animatable."""
    @overload
    @staticmethod
    def findAnimatedPlugs(node: MObject, animatedPlugs: MPlugArray, checkParent: bool = False) -> bool: ...
    @overload
    @staticmethod
    def findAnimatedPlugs(path: MDagPath, animatedPlugs: MPlugArray, checkParent: bool = False) -> bool: ...
    @overload
    @staticmethod
    def findAnimatedPlugs(selectionList: MSelectionList, animatedPlugs: MPlugArray, checkParent: bool = False) -> bool:
        """Find the list of attributes (MPlugs) on an MObject that is animated."""
    @staticmethod
    def findAnimation(plug: MPlug, animation: MObjectArray) -> bool:
        """Find the animCurve(s) that are animating a given attribute ( MPlug )."""
    def findAnimationLayers(self, *args: Any, **kwargs: Any) -> Any: ...
    @staticmethod
    def findConstraint(plug: MPlug, constraint: MObject, targets: MObjectArray) -> bool:
        """Find any constraint that is directly driving the specified attribute."""
    @staticmethod
    def findSetDrivenKeyAnimation(plug: MPlug, animation: MObjectArray, drivers: MPlugArray) -> bool:
        """Find any driven keyframe animCurves, the blendWeighted node and the driver attribute(s) that are animating a given attri"""
    @overload
    @staticmethod
    def isAnimated(node: MObject, checkParent: bool = False) -> bool: ...
    @overload
    @staticmethod
    def isAnimated(path: MDagPath, checkParent: bool = False) -> bool: ...
    @overload
    @staticmethod
    def isAnimated(plug: MPlug, checkParent: bool = False) -> bool: ...
    @overload
    @staticmethod
    def isAnimated(selectionList: MSelectionList, checkParent: bool = False) -> bool:
        """Determine whether or not an MObject is animated."""

class MFnAnimCurve:
    kAnimCurveTA: Any
    kAnimCurveTL: Any
    kAnimCurveTT: Any
    kAnimCurveTU: Any
    kAnimCurveUA: Any
    kAnimCurveUL: Any
    kAnimCurveUT: Any
    kAnimCurveUU: Any
    kAnimCurveUnknown: Any
    kConstant: Any
    kCycle: Any
    kCycleRelative: Any
    kExtensionAttr: Any
    kInvalidAttr: Any
    kLinear: Any
    kLocalDynamicAttr: Any
    kNormalAttr: Any
    kOscillate: Any
    kTangentAuto: Any
    kTangentAutoCustom: Any
    kTangentAutoEase: Any
    kTangentAutoMix: Any
    kTangentClamped: Any
    kTangentCustomEnd: Any
    kTangentCustomStart: Any
    kTangentFast: Any
    kTangentFixed: Any
    kTangentFlat: Any
    kTangentGlobal: Any
    kTangentLinear: Any
    kTangentPlateau: Any
    kTangentShared1: Any
    kTangentShared2: Any
    kTangentShared3: Any
    kTangentShared4: Any
    kTangentShared5: Any
    kTangentShared6: Any
    kTangentShared7: Any
    kTangentShared8: Any
    kTangentSlow: Any
    kTangentSmooth: Any
    kTangentStep: Any
    kTangentStepNext: Any
    kTangentTypeCount: Any
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
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None: ...
    @overload
    def __init__(self, plug: MPlug) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None:
        """Default constructor."""
    def absoluteName(self) -> str:
        """Returns the absolute name of this node."""
    @overload
    def addAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def addAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Add a new dynamic attibute to this node."""
    def addExternalContentForFileAttr(self, table: MExternalContentInfoTable, attr: MObject) -> MStatus:
        """Adds content info to the specified table from a file path attribute."""
    @overload
    def addKey(self, time: MTime, value: float, tangentInType: Any, tangentOutType: Any, change: MAnimCurveChange | None = None) -> int: ...
    @overload
    def addKey(self, timeInput: MTime, timeValue: MTime, tangentInType: Any, tangentOutType: Any, change: MAnimCurveChange | None = None) -> int: ...
    @overload
    def addKey(self, unitlessInput: float, value: float, tangentInType: Any, tangentOutType: Any, change: MAnimCurveChange | None = None) -> int: ...
    @overload
    def addKey(self, unitlessInput: float, time: MTime, tangentInType: Any, tangentOutType: Any, change: MAnimCurveChange | None = None) -> int:
        """Adds a new key with the given value and tangent types at the specified time for curves of type kAnimCurveTA, kAnimCurveT"""
    @overload
    def addKeyframe(self, time: MTime, value: float, change: MAnimCurveChange | None = None) -> MStatus: ...
    @overload
    def addKeyframe(self, time: MTime, value: float, tangentInType: Any, tangentOutType: Any, change: MAnimCurveChange | None = None) -> MStatus:
        """Adds a new key with the given value at the specified time."""
    def addKeys(self, timeArray: MTimeArray, valueArray: MDoubleArray, tangentInType: Any, tangentOutType: Any, keepExistingKeys: bool = False, change: MAnimCurveChange | None = None) -> MStatus:
        """Add a set of new keys with the given corresponding values and tangent types at the specified times."""
    def addKeysWithTangents(self, timeArray: MTimeArray, valueArray: MDoubleArray, tangentInType: Any, tangentOutType: Any, tangentInTypeArray: MIntArray | None = None, tangentOutTypeArray: MIntArray | None = None, tangentInXArray: MDoubleArray | None = None, tangentInYArray: MDoubleArray | None = None, tangentOutXArray: MDoubleArray | None = None, tangentOutYArray: MDoubleArray | None = None, tangentsLockedArray: MIntArray | None = None, weightsLockedArray: MIntArray | None = None, convertUnits: bool = True, keepExistingKeys: bool = False, change: MAnimCurveChange | None = None) -> MStatus:
        """Add a set of new keys with the given corresponding values and tangent types at the specified times."""
    def affectsAnimation(self) -> bool:
        """Introduced in 2019.0"""
    @staticmethod
    def allocateFlag(pluginName: str) -> int:
        """Allocates a node flag for sole use by the caller."""
    def animCurveType(self) -> Any:
        """Returns the animCurve type."""
    @overload
    def attribute(self, index: int) -> MObject: ...
    @overload
    def attribute(self, attrName: str) -> MObject:
        """Finds the attribute of this node at the given index."""
    def attributeClass(self, attr: MObject) -> Any:
        """Returns the class (normal, dynamic, extension) of the specified attribute."""
    def attributeCount(self) -> int:
        """Returns the number of attributes that this node has."""
    def canBeWritten(self) -> bool:
        """Returns the do not write state of the node."""
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
    @overload
    def create(self, node: MObject, attribute: MObject, modifier: MDGModifier | None = None) -> MObject: ...
    @overload
    def create(self, node: MObject, attribute: MObject, arg: Any, modifier: MDGModifier | None = None) -> MObject: ...
    @overload
    def create(self, plug: MPlug, modifier: MDGModifier | None = None) -> MObject: ...
    @overload
    def create(self, plug: MPlug, arg: Any, modifier: MDGModifier | None = None) -> MObject: ...
    @overload
    def create(self, arg: Any, modifier: MDGModifier | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str) -> MObject: ...
    @overload
    def create(self, type: str) -> MObject: ...
    @overload
    def create(self, type: str, name: str) -> MObject:
        """Creates a new Anim Curve Node, attaches the Function Set to the new Node (detaching from the current Node) and connects """
    @staticmethod
    def deallocateAllFlags(pluginName: str) -> MStatus:
        """Deallocates all of the node flags which are currently allocated to the specified plugin."""
    @staticmethod
    def deallocateFlag(pluginName: str, flag: int) -> MStatus:
        """Deallocates a node flag which was previously allocated by a call to allocateFlag ."""
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
    @staticmethod
    def enableDGTiming(enable: bool) -> None:
        """Globally enables or disables the DG node timing mechanism."""
    @overload
    def evaluate(self, atTime: MTime) -> float: ...
    @overload
    def evaluate(self, atTime: MTime, value: float) -> MStatus: ...
    @overload
    def evaluate(self, atTime: MTime, timeValue: MTime) -> MStatus: ...
    @overload
    def evaluate(self, atUnitlessInput: float, value: float) -> MStatus: ...
    @overload
    def evaluate(self, atUnitlessInput: float, timeValue: MTime) -> MStatus:
        """Determines the interpolated output value of Anim Curves of type kAnimCurveTA, kAnimCurveTL and kAnimCurveTU at the speci"""
    @overload
    def find(self, time: MTime, index: int) -> bool: ...
    @overload
    def find(self, unitlessInput: float, index: int) -> bool:
        """Determines the index of the key which is set at the specified time."""
    def findAlias(self, alias: str, attrObj: MObject) -> bool:
        """Retrieves the attribute with the given alias."""
    @overload
    def findClosest(self, time: MTime) -> int: ...
    @overload
    def findClosest(self, unitlessInput: float) -> int:
        """Determines the index of the key which is set at the time closest to the specified time."""
    @overload
    def findPlug(self, attr: MObject, wantNetworkedPlug: bool) -> MPlug: ...
    @overload
    def findPlug(self, attrName: str, wantNetworkedPlug: bool) -> MPlug: ...
    @overload
    def findPlug(self, attr: MObject) -> MPlug: ...
    @overload
    def findPlug(self, attrName: str) -> MPlug:
        """Attempt to find a plug for the given attribute."""
    def getAffectedAttributes(self, attr: MObject, affectedAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that are affected by the attribute passed in."""
    def getAffectedByAttributes(self, attr: MObject, affectedByAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that affect the attribute passed in, attr ."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute al"""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns a list of all attribute aliases for this node."""
    def getConnections(self, array: MPlugArray) -> MStatus:
        """Get all of the current connections to this node as an array of plugs."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> MStatus:
        """Returns the external content (files) that this node depends on."""
    @overload
    def getTangent(self, index: int, x: Any, y: Any, inTangent: bool) -> MStatus: ...
    @overload
    def getTangent(self, index: int, angle: MAngle, weight: float, inTangent: bool) -> MStatus:
        """Determines the x,y value representing the vector of the in- or out-tangent (depending on the value of the inTangent para"""
    def hasAttribute(self, name: str) -> bool:
        """Returns true if the node already has an attribute with the given name."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    def hasUniqueName(self) -> bool:
        """Indicates whether or not this node's name is unique within the scene."""
    def icon(self) -> str:
        """Returns the custom icon filename associated with the node."""
    def inTangentType(self, index: int) -> Any:
        """Determines the type of the tangent to the curve entering the current key."""
    def insertKey(self, time: MTime, breakdown: bool = False, change: MAnimCurveChange | None = None) -> int:
        """Introduced in 2019.0"""
    def isBreakdown(self, index: int) -> bool:
        """Determines whether or not a key is a breakdown."""
    def isDefaultNode(self) -> bool:
        """Returns true if the node is a default node."""
    def isFlagSet(self, flag: int) -> bool:
        """Retrieves the current state of the specified flag for a node."""
    def isFromReferencedFile(self) -> bool:
        """Indicates whether or not this node came from a referenced file."""
    def isLocked(self) -> bool:
        """Indicates whether or not this node is locked."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Indicates whether or not the specified attribute was added to this node within the current scene."""
    def isShared(self) -> bool:
        """Indicates whether or not this node is shared."""
    def isStatic(self) -> bool:
        """Determines whether or not the animCurve is static."""
    def isTimeInput(self) -> bool:
        """Determines the input type of the animCurve."""
    def isTrackingEdits(self) -> bool:
        """Returns whether or not edits on the given node are being tracked by the generalized edit system."""
    def isUnitlessInput(self) -> bool:
        """Determines the input type of the animCurve."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def isWeighted(self) -> bool:
        """Determines whether or not the curve has weighted tangents."""
    def name(self) -> str:
        """Returns the name of this node."""
    def numKeyframes(self) -> int:
        """Deprecated in 2016.0"""
    def numKeys(self) -> int:
        """Determines the number of keys on the Anim Curve Node."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def outTangentType(self, index: int) -> Any:
        """Determines the type of the tangent to the curve leaving the current key."""
    def parentNamespace(self) -> str:
        """Returns the name of the namespace in which this node resides."""
    def pluginName(self) -> str:
        """Returns the name of the plug-in this MFnDependendencyNode was defined in."""
    def plugsAlias(self, plug: MPlug) -> str:
        """Returns the alias for the plug's attribute or the empty string if that attribute has no alias."""
    def postInfinityType(self) -> Any:
        """Determines the behaviour of the curve for the range occurring after the last key."""
    def preInfinityType(self) -> Any:
        """Determines the behaviour of the curve for the range occurring before the first key."""
    def quaternionW(self, index: int) -> float:
        """Introduced in 2024.0"""
    def remove(self, index: int, change: MAnimCurveChange | None = None) -> MStatus:
        """Removes the key at the specified index."""
    @overload
    def removeAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def removeAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Remove a dynamic attribute from a node."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Some nodes, such as the various animCurve nodes, require that their attributes be set in a specific order for proper ope"""
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setAngle(self, index: int, angle: MAngle, inTangent: bool, change: MAnimCurveChange | None = None) -> MStatus:
        """Set the in- or out-angle of the tangent for the key at the given index."""
    def setDoNotWrite(self, flag: bool) -> MStatus:
        """Use this method to mark the "do not write" state of this node."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> MStatus:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> MStatus:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> MStatus:
        """Sets the state of the specified flag for the node."""
    def setIcon(self, filename: str) -> MStatus:
        """Associates a custom icon with the node for display in the Maya UI."""
    def setInTangentType(self, index: int, arg: Any, change: MAnimCurveChange | None = None) -> MStatus:
        """Sets the type of the tangent to the curve entering the key at the specified index."""
    def setIsBreakdown(self, index: int, isBreakdown: bool, change: MAnimCurveChange | None = None) -> MStatus:
        """Sets the breakdown state of a key at a given index."""
    def setIsWeighted(self, isWeighted: bool, change: MAnimCurveChange | None = None) -> MStatus:
        """Sets whether or not the curve has weighted tangents."""
    def setLocked(self, locked: bool) -> MStatus:
        """Locks or unlocks this node."""
    @overload
    def setName(self, name: str, createNamespace: bool = False) -> str: ...
    @overload
    def setName(self, name: str) -> str:
        """Sets the name of this node."""
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches the Function Set to the specified Maya Object."""
    def setOutTangentType(self, index: int, arg: Any, change: MAnimCurveChange | None = None) -> MStatus:
        """Sets the type of the tangent to the curve leaving the key at the specified index."""
    def setPostInfinityType(self, arg: Any, change: MAnimCurveChange | None = None) -> MStatus:
        """Set the behaviour of the curve for the range occurring after the last key."""
    def setPreInfinityType(self, arg: Any, change: MAnimCurveChange | None = None) -> MStatus:
        """Set the behaviour of the curve for the range occurring before the first key."""
    def setQuaternionW(self, index: int, quaternionW: float, change: MAnimCurveChange | None = None) -> MStatus:
        """Introduced in 2024.0"""
    @overload
    def setTangent(self, index: int, x: Any, y: Any, inTangent: bool, change: MAnimCurveChange | None = None, convertUnits: bool = True) -> MStatus: ...
    @overload
    def setTangent(self, index: int, angle: MAngle, weight: float, inTangent: bool, change: MAnimCurveChange | None = None, convertUnits: bool = True) -> MStatus:
        """Sets the tangent for the key at the specified index."""
    def setTangentTypes(self, indexArray: MIntArray, tangentInType: Any, tangentOutType: Any, change: MAnimCurveChange | None = None) -> MStatus:
        """Sets the tangent types for multiple keys."""
    def setTangentsLocked(self, index: int, locked: bool, change: MAnimCurveChange | None = None) -> MStatus:
        """Lock or unlock the tangents at the given key."""
    def setTime(self, index: int, time: MTime, change: MAnimCurveChange | None = None) -> MStatus:
        """Sets the time of the key at the specified index."""
    def setUnitlessInput(self, index: int, unitlessInput: float, change: MAnimCurveChange | None = None) -> MStatus:
        """Sets the value of the unitless input of the key at the specified index."""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def setValue(self, index: int, value: float, change: MAnimCurveChange | None = None) -> MStatus:
        """Sets the value of the key at the specified index."""
    def setWeight(self, index: int, weight: float, inTangent: bool, change: MAnimCurveChange | None = None) -> MStatus:
        """Set the in- or out-weight of the tangent for the key at the given index."""
    def setWeightsLocked(self, index: int, locked: bool, change: MAnimCurveChange | None = None) -> MStatus:
        """Lock or unlock the weights at the given key."""
    def tangentsLocked(self, index: int) -> bool:
        """Determines whether the tangents are locked at the given key."""
    def time(self, index: int) -> MTime:
        """Determines the time of the key at the specified index."""
    def timedAnimCurveTypeForPlug(self, plug: MPlug) -> Any:
        """Returns the timed animCurve type appropriate for the specified plug."""
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
    def unitlessAnimCurveTypeForPlug(self, plug: MPlug) -> Any:
        """Returns the unitless animCurve type appropriate for the specified plug."""
    def unitlessInput(self, index: int) -> float:
        """Determines the unitless input value of the key at the specified index."""
    def userNode(self) -> Any:
        """If the function set's node is a plug-in node, then this method will extract the MPxNode pointer from it."""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""
    def value(self, index: int) -> float:
        """Determines the value of the key at the specified index."""
    def weightsLocked(self, index: int) -> bool:
        """Determines whether the weights are locked at the given key."""

class MFnBlendShapeDeformer:
    kExtensionAttr: Any
    kFrontOfChain: Any
    kInvalidAttr: Any
    kLocalDynamicAttr: Any
    kLocalOrigin: Any
    kNormal: Any
    kNormalAttr: Any
    kObject: Any
    kOther: Any
    kPost: Any
    kTangent: Any
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
    kWorldOrigin: Any
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None:
        """Default constructor."""
    def absoluteName(self) -> str:
        """Returns the absolute name of this node."""
    @overload
    def addAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def addAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Add a new dynamic attibute to this node."""
    def addBaseObject(self, object: MObject) -> MStatus:
        """Adds a new base object to the deformer."""
    def addExternalContentForFileAttr(self, table: MExternalContentInfoTable, attr: MObject) -> MStatus:
        """Adds content info to the specified table from a file path attribute."""
    @overload
    def addTarget(self, baseObject: MObject, weightIndex: int, newTarget: MObject, fullWeight: float, arg: Any) -> MStatus: ...
    @overload
    def addTarget(self, baseObject: MObject, weightIndex: int, fullWeight: float, arg: Any) -> MStatus:
        """Adds a new target object for the given base object."""
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
    def canBeWritten(self) -> bool:
        """Returns the do not write state of the node."""
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
    @overload
    def create(self, baseObject: MObject, originSpace: Any) -> MObject: ...
    @overload
    def create(self, baseObjects: MObjectArray, originSpace: Any, HistoryLocation: Any) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str) -> MObject: ...
    @overload
    def create(self, type: str) -> MObject: ...
    @overload
    def create(self, type: str, name: str) -> MObject:
        """Creates a new blend shape deformer in the dependency graph with the specified shape as the baseObject."""
    @staticmethod
    def deallocateAllFlags(pluginName: str) -> MStatus:
        """Deallocates all of the node flags which are currently allocated to the specified plugin."""
    @staticmethod
    def deallocateFlag(pluginName: str, flag: int) -> MStatus:
        """Deallocates a node flag which was previously allocated by a call to allocateFlag ."""
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
    @staticmethod
    def enableDGTiming(enable: bool) -> None:
        """Globally enables or disables the DG node timing mechanism."""
    def envelope(self) -> float:
        """Gets the envelope value of the deformer."""
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
    def getAffectedAttributes(self, attr: MObject, affectedAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that are affected by the attribute passed in."""
    def getAffectedByAttributes(self, attr: MObject, affectedByAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that affect the attribute passed in, attr ."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute al"""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns a list of all attribute aliases for this node."""
    def getBaseObjects(self, objects: MObjectArray) -> MStatus:
        """Get a list of all of the base objects for this deformer."""
    def getConnections(self, array: MPlugArray) -> MStatus:
        """Get all of the current connections to this node as an array of plugs."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> MStatus:
        """Returns the external content (files) that this node depends on."""
    def getTargets(self, baseObject: MObject, weightIndex: int, targetObjects: MObjectArray) -> MStatus:
        """Get a list of all of the target objects for the given base object that affect it based on the given weight index."""
    def hasAttribute(self, name: str) -> bool:
        """Returns true if the node already has an attribute with the given name."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    def hasUniqueName(self) -> bool:
        """Indicates whether or not this node's name is unique within the scene."""
    def historyLocation(self) -> Any:
        """Gets the history location (deformation order)."""
    def icon(self) -> str:
        """Returns the custom icon filename associated with the node."""
    def isDefaultNode(self) -> bool:
        """Returns true if the node is a default node."""
    def isFlagSet(self, flag: int) -> bool:
        """Retrieves the current state of the specified flag for a node."""
    def isFromReferencedFile(self) -> bool:
        """Indicates whether or not this node came from a referenced file."""
    def isLocked(self) -> bool:
        """Indicates whether or not this node is locked."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Indicates whether or not the specified attribute was added to this node within the current scene."""
    def isShared(self) -> bool:
        """Indicates whether or not this node is shared."""
    def isTrackingEdits(self) -> bool:
        """Returns whether or not edits on the given node are being tracked by the generalized edit system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def name(self) -> str:
        """Returns the name of this node."""
    def numWeights(self) -> int:
        """Return the number of weight values that this blend shape deformer has."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def origin(self) -> Any:
        """Gets the origin space."""
    def parentNamespace(self) -> str:
        """Returns the name of the namespace in which this node resides."""
    def pluginName(self) -> str:
        """Returns the name of the plug-in this MFnDependendencyNode was defined in."""
    def plugsAlias(self, plug: MPlug) -> str:
        """Returns the alias for the plug's attribute or the empty string if that attribute has no alias."""
    @overload
    def removeAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def removeAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Remove a dynamic attribute from a node."""
    def removeTarget(self, baseObject: MObject, weightIndex: int, target: MObject, fullWeight: float) -> MStatus:
        """Remove a target object for the given base object."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Some nodes, such as the various animCurve nodes, require that their attributes be set in a specific order for proper ope"""
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setDoNotWrite(self, flag: bool) -> MStatus:
        """Use this method to mark the "do not write" state of this node."""
    def setEnvelope(self, envelope: float) -> MStatus:
        """Sets the envelope value of the deformer."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> MStatus:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> MStatus:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> MStatus:
        """Sets the state of the specified flag for the node."""
    def setIcon(self, filename: str) -> MStatus:
        """Associates a custom icon with the node for display in the Maya UI."""
    def setLocked(self, locked: bool) -> MStatus:
        """Locks or unlocks this node."""
    @overload
    def setName(self, name: str, createNamespace: bool = False) -> str: ...
    @overload
    def setName(self, name: str) -> str:
        """Sets the name of this node."""
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches the Function Set to the specified Maya Object."""
    def setOrigin(self, space: Any) -> MStatus:
        """Sets the origin space."""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def setWeight(self, index: int, weight: float) -> MStatus:
        """Set the weight value at the given index."""
    def targetItemIndexList(self, weightIndex: int, baseObject: MObject, targetItemIndices: MIntArray) -> MStatus:
        """A base object may have more than one target using the same element of the blendShape's 'weights' array."""
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
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""
    def weight(self, index: int) -> float:
        """Get the weight value at the given index."""
    def weightIndexList(self, indexList: MIntArray) -> MStatus:
        """Return the array index numbers corresponding to the targets."""

class MFnCharacter:
    kEdgesOnly: Any
    kEditPointsOnly: Any
    kExtensionAttr: Any
    kFacetsOnly: Any
    kInvalidAttr: Any
    kLocalDynamicAttr: Any
    kNone: Any
    kNormalAttr: Any
    kRenderableOnly: Any
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
    kVerticesOnly: Any
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None:
        """Default constructor."""
    def absoluteName(self) -> str:
        """Returns the absolute name of this node."""
    @overload
    def addAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def addAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Add a new dynamic attibute to this node."""
    def addCurveToClip(self, curve: MObject, sourceClip: MObject, characterPlug: MPlug, dgMod: MDGModifier) -> MStatus:
        """Adds an animation curve to a clip."""
    def addExternalContentForFileAttr(self, table: MExternalContentInfoTable, attr: MObject) -> MStatus:
        """Adds content info to the specified table from a file path attribute."""
    @overload
    def addMember(self, obj: MObject) -> MStatus: ...
    @overload
    def addMember(self, obj: MDagPath, component: MObject | None = None) -> MStatus: ...
    @overload
    def addMember(self, plug: MPlug) -> MStatus:
        """Add a new object (dependency node) to the set."""
    def addMembers(self, list: MSelectionList) -> MStatus:
        """Add a list of new objects to the set."""
    def affectsAnimation(self) -> bool:
        """Introduced in 2019.0"""
    @staticmethod
    def allocateFlag(pluginName: str) -> int:
        """Allocates a node flag for sole use by the caller."""
    def annotation(self) -> str:
        """Returns the annotation string for this set."""
    def attachInstanceToCharacter(self, instanceClip: MObject, dgMod: MDGModifier) -> MStatus:
        """Attaches an instance of a clip to the character."""
    def attachSourceToCharacter(self, sourceClip: MObject, dgMod: MDGModifier) -> MStatus:
        """Attaches a given source clip node (created using MFnClip::createSourceClip ) to the character's clipLibrary."""
    @overload
    def attribute(self, index: int) -> MObject: ...
    @overload
    def attribute(self, attrName: str) -> MObject:
        """Finds the attribute of this node at the given index."""
    def attributeClass(self, attr: MObject) -> Any:
        """Returns the class (normal, dynamic, extension) of the specified attribute."""
    def attributeCount(self) -> int:
        """Returns the number of attributes that this node has."""
    def blendExists(self, instancedClip1: MObject, instancedClip2: MObject, blendResult: MObject) -> bool:
        """Return true if a blend exists between the two instanced clips on the character."""
    def canBeWritten(self) -> bool:
        """Returns the do not write state of the node."""
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
    def clear(self) -> MStatus:
        """Removes all elements from this set."""
    @overload
    def create(self, members: MSelectionList, arg: Any) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str) -> MObject: ...
    @overload
    def create(self, type: str) -> MObject: ...
    @overload
    def create(self, type: str, name: str) -> MObject:
        """Creates a new set dependency node and puts it in the dependency graph."""
    def createBlend(self, instancedClip1: MObject, instancedClip2: MObject, blendAnimCurve: MObject, dgMod: MDGModifier) -> MObject:
        """Creates a blend between two instanced clips on the character."""
    @staticmethod
    def deallocateAllFlags(pluginName: str) -> MStatus:
        """Deallocates all of the node flags which are currently allocated to the specified plugin."""
    @staticmethod
    def deallocateFlag(pluginName: str, flag: int) -> MStatus:
        """Deallocates a node flag which was previously allocated by a call to allocateFlag ."""
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
    @staticmethod
    def enableDGTiming(enable: bool) -> None:
        """Globally enables or disables the DG node timing mechanism."""
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
    def getAffectedAttributes(self, attr: MObject, affectedAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that are affected by the attribute passed in."""
    def getAffectedByAttributes(self, attr: MObject, affectedByAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that affect the attribute passed in, attr ."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute al"""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns a list of all attribute aliases for this node."""
    def getBlend(self, index: int) -> MObject:
        """Return the animBlendInOut node corresponding to the specified index."""
    def getBlendClips(self, index: int, clip1: MObject, clip2: MObject) -> MStatus:
        """Returns the clip nodes that are blended by the blend node corresponding to the specified index."""
    def getBlendCount(self) -> int:
        """Return the number of blends that have been added to clips on this character."""
    def getCharacterThatOwnsPlug(self, plug: MPlug, result: MObject) -> bool:
        """Given a plug, test the plug to see if it is owned by a character."""
    def getClipScheduler(self) -> MObject:
        """Get the clipScheduler node that manages the playback of clips on this character."""
    def getConnections(self, array: MPlugArray) -> MStatus:
        """Get all of the current connections to this node as an array of plugs."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> MStatus:
        """Returns the external content (files) that this node depends on."""
    @overload
    def getIntersection(self, withSet: MObject, result: MSelectionList) -> MStatus: ...
    @overload
    def getIntersection(self, setList: MObjectArray, result: MSelectionList) -> MStatus:
        """This method calculates the intersection of two sets."""
    def getMemberPaths(self, members: MDagPathArray, shading: bool = False) -> MStatus:
        """Introduced in 2023.0"""
    def getMemberPlugs(self, result: MPlugArray) -> MStatus:
        """Get the members of the character set that are attributes."""
    def getMembers(self, members: MSelectionList, flatten: bool) -> MStatus:
        """Get the members of this set as a selection list."""
    def getScheduledClip(self, index: int) -> MObject:
        """Return the scheduled animClip node corresponding to the specified index."""
    def getScheduledClipCount(self) -> int:
        """Return the number of clips that have been scheduled on this character."""
    def getSourceClip(self, index: int) -> MObject:
        """Return the animClip node corresponding to the specified index."""
    def getSourceClipCount(self) -> int:
        """Return the number of source clips managed by the clipLibrary node of this character."""
    def getSubCharacters(self, result: MSelectionList) -> MStatus:
        """Get a list of the subcharacters that are members of the character set."""
    @overload
    def getUnion(self, withSet: MObject, result: MSelectionList) -> MStatus: ...
    @overload
    def getUnion(self, setList: MObjectArray, result: MSelectionList) -> MStatus:
        """This method calculates the union of two sets."""
    def hasAttribute(self, name: str) -> bool:
        """Returns true if the node already has an attribute with the given name."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    def hasRestrictions(self) -> bool:
        """Returns true if this function set has restrictions on the type of objects that it may contain."""
    def hasUniqueName(self) -> bool:
        """Indicates whether or not this node's name is unique within the scene."""
    def icon(self) -> str:
        """Returns the custom icon filename associated with the node."""
    def intersectsWith(self, otherSet: MObject) -> bool:
        """Returns true if this set intersects with the given set."""
    def isDefaultNode(self) -> bool:
        """Returns true if the node is a default node."""
    def isFlagSet(self, flag: int) -> bool:
        """Retrieves the current state of the specified flag for a node."""
    def isFromReferencedFile(self) -> bool:
        """Indicates whether or not this node came from a referenced file."""
    def isLocked(self) -> bool:
        """Indicates whether or not this node is locked."""
    @overload
    def isMember(self, object: MObject) -> bool: ...
    @overload
    def isMember(self, object: MDagPath, component: MObject | None = None) -> bool: ...
    @overload
    def isMember(self, plug: MPlug) -> bool:
        """Returns true if the given object (dependency node) is a member of this set."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Indicates whether or not the specified attribute was added to this node within the current scene."""
    def isShared(self) -> bool:
        """Indicates whether or not this node is shared."""
    def isTrackingEdits(self) -> bool:
        """Returns whether or not edits on the given node are being tracked by the generalized edit system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def name(self) -> str:
        """Returns the name of this node."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def parentNamespace(self) -> str:
        """Returns the name of the namespace in which this node resides."""
    def pluginName(self) -> str:
        """Returns the name of the plug-in this MFnDependendencyNode was defined in."""
    def plugsAlias(self, plug: MPlug) -> str:
        """Returns the alias for the plug's attribute or the empty string if that attribute has no alias."""
    @overload
    def removeAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def removeAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Remove a dynamic attribute from a node."""
    def removeBlend(self, instancedClip1: MObject, instancedClip2: MObject, dgMod: MDGModifier) -> bool:
        """Remove the blend between the two instanced clips on the character."""
    @overload
    def removeMember(self, obj: MObject) -> MStatus: ...
    @overload
    def removeMember(self, obj: MDagPath, component: MObject) -> MStatus: ...
    @overload
    def removeMember(self, plug: MPlug) -> MStatus:
        """Remove an object (dependency node) from the set."""
    def removeMembers(self, list: MSelectionList) -> MStatus:
        """Remove items of the selection list from the set."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Some nodes, such as the various animCurve nodes, require that their attributes be set in a specific order for proper ope"""
    def restriction(self) -> Any:
        """Returns the type of membership restriction that this set has."""
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setAnnotation(self, annotation: str) -> MStatus:
        """Sets the annotation string for this set."""
    def setDoNotWrite(self, flag: bool) -> MStatus:
        """Use this method to mark the "do not write" state of this node."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> MStatus:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> MStatus:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> MStatus:
        """Sets the state of the specified flag for the node."""
    def setIcon(self, filename: str) -> MStatus:
        """Associates a custom icon with the node for display in the Maya UI."""
    def setLocked(self, locked: bool) -> MStatus:
        """Locks or unlocks this node."""
    @overload
    def setName(self, name: str, createNamespace: bool = False) -> str: ...
    @overload
    def setName(self, name: str) -> str:
        """Sets the name of this node."""
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches the Function Set to the specified Maya Object."""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
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
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnClip:
    kExtensionAttr: Any
    kInvalidAttr: Any
    kLocalDynamicAttr: Any
    kNormalAttr: Any
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
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None:
        """Default constructor."""
    def absoluteName(self) -> str:
        """Returns the absolute name of this node."""
    @overload
    def addAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def addAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Add a new dynamic attibute to this node."""
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
    def canBeWritten(self) -> bool:
        """Returns the do not write state of the node."""
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
    @overload
    def create(self, typeId: MTypeId) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str) -> MObject: ...
    @overload
    def create(self, type: str) -> MObject: ...
    @overload
    def create(self, type: str, name: str) -> MObject:
        """Creates a new dependency node with the given type tag."""
    def createInstancedClip(self, sourceClip: MObject, start: MTime, dgMod: MDGModifier, absolute: bool = True, postCycle: float = 0.0, weight: float = 1.0, scale: float = 1.0, preCycle: float = 0.0) -> MObject:
        """Creates an instance of a clip that will be viewable in the Trax editor."""
    def createSourceClip(self, sourceStart: MTime, sourceDuration: MTime, dgMod: MDGModifier) -> MObject:
        """Creates a source clip node and associates it with this function set."""
    @staticmethod
    def deallocateAllFlags(pluginName: str) -> MStatus:
        """Deallocates all of the node flags which are currently allocated to the specified plugin."""
    @staticmethod
    def deallocateFlag(pluginName: str, flag: int) -> MStatus:
        """Deallocates a node flag which was previously allocated by a call to allocateFlag ."""
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
    @staticmethod
    def enableDGTiming(enable: bool) -> None:
        """Globally enables or disables the DG node timing mechanism."""
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
    def getAbsolute(self) -> bool:
        """Deprecated in 2016.0"""
    def getAbsoluteChannelSettings(self, absoluteChannels: MIntArray) -> MStatus:
        """Return an array indicating which channels of the clip are absolute and which are relative."""
    def getAffectedAttributes(self, attr: MObject, affectedAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that are affected by the attribute passed in."""
    def getAffectedByAttributes(self, attr: MObject, affectedByAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that affect the attribute passed in, attr ."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute al"""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns a list of all attribute aliases for this node."""
    def getConnections(self, array: MPlugArray) -> MStatus:
        """Get all of the current connections to this node as an array of plugs."""
    def getCycle(self) -> float:
        """Deprecated in 2016.0"""
    def getEnabled(self) -> bool:
        """Return the value of this clip's enable attribute."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> MStatus:
        """Returns the external content (files) that this node depends on."""
    def getMemberAnimCurves(self, curves: MObjectArray, associatedAttrs: MPlugArray) -> MStatus:
        """Return two arrays: the first contains the animCurves associated with this clip."""
    def getPostCycle(self) -> float:
        """Return the value of this clip's post cycle attribute."""
    def getPreCycle(self) -> float:
        """Return the value of this clip's pre cycle attribute."""
    def getScale(self) -> float:
        """Return the value of this clip's scale attribute."""
    def getSourceDuration(self) -> MTime:
        """Return the value of the start frame of this clip's source duration."""
    def getSourceStart(self) -> MTime:
        """Return the value of the start frame of this clip's source clip."""
    def getStartFrame(self) -> MTime:
        """Return the value of this clip's start frame."""
    def getTrack(self) -> int:
        """Return the track number for the clip."""
    def getWeight(self) -> float:
        """Return the value of this clip's weight attribute."""
    def hasAttribute(self, name: str) -> bool:
        """Returns true if the node already has an attribute with the given name."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    def hasUniqueName(self) -> bool:
        """Indicates whether or not this node's name is unique within the scene."""
    def icon(self) -> str:
        """Returns the custom icon filename associated with the node."""
    def isDefaultNode(self) -> bool:
        """Returns true if the node is a default node."""
    def isFlagSet(self, flag: int) -> bool:
        """Retrieves the current state of the specified flag for a node."""
    def isFromReferencedFile(self) -> bool:
        """Indicates whether or not this node came from a referenced file."""
    def isInstancedClip(self) -> bool:
        """Return true or false as to whether the clip node represents the source clip or an instanced clip."""
    def isLocked(self) -> bool:
        """Indicates whether or not this node is locked."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Indicates whether or not the specified attribute was added to this node within the current scene."""
    def isPose(self) -> bool:
        """Return true or false as to whether the clip node represents a pose."""
    def isShared(self) -> bool:
        """Indicates whether or not this node is shared."""
    def isTrackingEdits(self) -> bool:
        """Returns whether or not edits on the given node are being tracked by the generalized edit system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def name(self) -> str:
        """Returns the name of this node."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def parentNamespace(self) -> str:
        """Returns the name of the namespace in which this node resides."""
    def pluginName(self) -> str:
        """Returns the name of the plug-in this MFnDependendencyNode was defined in."""
    def plugsAlias(self, plug: MPlug) -> str:
        """Returns the alias for the plug's attribute or the empty string if that attribute has no alias."""
    @overload
    def removeAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def removeAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Remove a dynamic attribute from a node."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Some nodes, such as the various animCurve nodes, require that their attributes be set in a specific order for proper ope"""
    def setAbsolute(self, abs: bool, mod: MDGModifier | None = None) -> MStatus:
        """Deprecated in 2016.0"""
    def setAbsoluteChannelSettings(self, absoluteChannels: MIntArray, mod: MDGModifier | None = None) -> MStatus:
        """Set which channels of the clip are absolute and which are relative."""
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setCycle(self, cycle: float, mod: MDGModifier | None = None) -> MStatus:
        """Deprecated in 2016.0"""
    def setDoNotWrite(self, flag: bool) -> MStatus:
        """Use this method to mark the "do not write" state of this node."""
    def setEnabled(self, val: bool, mod: MDGModifier | None = None) -> MStatus:
        """Specify whether or not the clip is enabled."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> MStatus:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> MStatus:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> MStatus:
        """Sets the state of the specified flag for the node."""
    def setIcon(self, filename: str) -> MStatus:
        """Associates a custom icon with the node for display in the Maya UI."""
    def setLocked(self, locked: bool) -> MStatus:
        """Locks or unlocks this node."""
    @overload
    def setName(self, name: str, createNamespace: bool = False) -> str: ...
    @overload
    def setName(self, name: str) -> str:
        """Sets the name of this node."""
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches the Function Set to the specified Maya Object."""
    def setPoseClip(self, state: bool, mod: MDGModifier | None = None) -> MStatus:
        """Specify whether or not this clip node should be tagged as a pose rather than a clip."""
    def setPostCycle(self, cycle: float, mod: MDGModifier | None = None) -> MStatus:
        """Specify the post cycle value for the clip."""
    def setPreCycle(self, cycle: float, mod: MDGModifier | None = None) -> MStatus:
        """Specify the pre cycle value for the clip."""
    def setScale(self, scale: float, mod: MDGModifier | None = None) -> MStatus:
        """Specify a scale value for the clip."""
    def setSourceData(self, start: MTime, duration: MTime, mod: MDGModifier | None = None) -> MStatus:
        """Specify the start frame and duration for the source clip associated with this clip."""
    def setStartFrame(self, start: MTime, mod: MDGModifier | None = None) -> MStatus:
        """Specify the start frame for the instanced clip."""
    def setTrack(self, index: int, mod: MDGModifier | None = None) -> MStatus:
        """Specify the one-based track number for the clip."""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def setWeight(self, wt: float, mod: MDGModifier | None = None) -> MStatus:
        """Specify a weight value for the clip."""
    def sourceClip(self) -> MObject:
        """Return the source clip associated with the MFnClip 's clip."""
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
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnGeometryFilter:
    kExtensionAttr: Any
    kInvalidAttr: Any
    kLocalDynamicAttr: Any
    kNormalAttr: Any
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
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None:
        """Default constructor."""
    def absoluteName(self) -> str:
        """Returns the absolute name of this node."""
    @overload
    def addAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def addAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Add a new dynamic attibute to this node."""
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
    def canBeWritten(self) -> bool:
        """Returns the do not write state of the node."""
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
    @overload
    def create(self, typeId: MTypeId) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str) -> MObject: ...
    @overload
    def create(self, type: str) -> MObject: ...
    @overload
    def create(self, type: str, name: str) -> MObject:
        """Creates a new dependency node with the given type tag."""
    @staticmethod
    def deallocateAllFlags(pluginName: str) -> MStatus:
        """Deallocates all of the node flags which are currently allocated to the specified plugin."""
    @staticmethod
    def deallocateFlag(pluginName: str, flag: int) -> MStatus:
        """Deallocates a node flag which was previously allocated by a call to allocateFlag ."""
    def deformerSet(self) -> MObject:
        """Returns the set containing the objects that are deformed."""
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
    @staticmethod
    def enableDGTiming(enable: bool) -> None:
        """Globally enables or disables the DG node timing mechanism."""
    def envelope(self) -> float:
        """Returns the envelope value."""
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
    def getAffectedAttributes(self, attr: MObject, affectedAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that are affected by the attribute passed in."""
    def getAffectedByAttributes(self, attr: MObject, affectedByAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that affect the attribute passed in, attr ."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute al"""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns a list of all attribute aliases for this node."""
    def getComponentAtIndex(self, index: int) -> MObject:
        """Introduced in 2022.0"""
    def getConnections(self, array: MPlugArray) -> MStatus:
        """Get all of the current connections to this node as an array of plugs."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> MStatus:
        """Returns the external content (files) that this node depends on."""
    def getIndexMapper(self, index: int) -> MStatus:
        """Introduced in 2024.1"""
    def getInputGeometry(self, objects: MObjectArray) -> MStatus:
        """This method returns the input geometry for the deformer by traversing the graph to find upstream shape nodes."""
    def getOutputGeometry(self, objects: MObjectArray) -> MStatus:
        """The output geometry is packed into the provided list of MObjects."""
    def getPathAtIndex(self, index: int, path: MDagPath) -> MStatus:
        """The DAG path of the output geometry at the specified plug index is put in the dagPath argument."""
    def groupIdAtIndex(self, index: int) -> int:
        """Returns the groupId at the specified plug index."""
    def hasAttribute(self, name: str) -> bool:
        """Returns true if the node already has an attribute with the given name."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    def hasUniqueName(self) -> bool:
        """Indicates whether or not this node's name is unique within the scene."""
    def icon(self) -> str:
        """Returns the custom icon filename associated with the node."""
    def indexForGroupId(self, groupId: int) -> int:
        """Returns the plug index corresponding to the groupId."""
    def indexForOutputConnection(self, connectionIndex: int) -> int:
        """Returns the plug index corresponding to the connection index."""
    def indexForOutputShape(self, shape: MObject) -> int:
        """Returns the plug index for the specified output shape."""
    def inputShapeAtIndex(self, index: int) -> MObject:
        """Returns the input shape corresponding to the plug index."""
    def isDefaultNode(self) -> bool:
        """Returns true if the node is a default node."""
    def isFlagSet(self, flag: int) -> bool:
        """Retrieves the current state of the specified flag for a node."""
    def isFromReferencedFile(self) -> bool:
        """Indicates whether or not this node came from a referenced file."""
    def isLocked(self) -> bool:
        """Indicates whether or not this node is locked."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Indicates whether or not the specified attribute was added to this node within the current scene."""
    def isShared(self) -> bool:
        """Indicates whether or not this node is shared."""
    def isTrackingEdits(self) -> bool:
        """Returns whether or not edits on the given node are being tracked by the generalized edit system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def name(self) -> str:
        """Returns the name of this node."""
    def numOutputConnections(self) -> int:
        """Returns the number of output geometries connected to this node."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def outputShapeAtIndex(self, index: int) -> MObject:
        """Returns the output shape corresponding to the plug index."""
    def parentNamespace(self) -> str:
        """Returns the name of the namespace in which this node resides."""
    def pluginName(self) -> str:
        """Returns the name of the plug-in this MFnDependendencyNode was defined in."""
    def plugsAlias(self, plug: MPlug) -> str:
        """Returns the alias for the plug's attribute or the empty string if that attribute has no alias."""
    @overload
    def removeAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def removeAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Remove a dynamic attribute from a node."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Some nodes, such as the various animCurve nodes, require that their attributes be set in a specific order for proper ope"""
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setDoNotWrite(self, flag: bool) -> MStatus:
        """Use this method to mark the "do not write" state of this node."""
    def setEnvelope(self, envelope: float) -> MStatus:
        """Sets the envelope value."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> MStatus:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> MStatus:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> MStatus:
        """Sets the state of the specified flag for the node."""
    def setIcon(self, filename: str) -> MStatus:
        """Associates a custom icon with the node for display in the Maya UI."""
    def setLocked(self, locked: bool) -> MStatus:
        """Locks or unlocks this node."""
    @overload
    def setName(self, name: str, createNamespace: bool = False) -> str: ...
    @overload
    def setName(self, name: str) -> str:
        """Sets the name of this node."""
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches the Function Set to the specified Maya Object."""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
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
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnHikEffector:
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
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def classification(nodeTypeName: str) -> str:
        """Retrieves the classification string for a node type."""
    def clearRestPosition(self) -> MStatus:
        """Clear the saved rest position of this transform."""
    @overload
    def create(self, parent: MObject | None = None) -> MObject: ...
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
        """Creates a new fbik effector."""
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
    def getAuxiliaryEffectors(self, effs: MObjectArray) -> MStatus:
        """Returns an array of the auxiliary effectors associated with this effector."""
    def getConnectedSetsAndMembers(self, instanceNumber: int, sets: MObjectArray, comps: MObjectArray, renderableSetsOnly: bool) -> MStatus:
        """Returns all the sets connected to the specified instance of this DAG object."""
    def getConnections(self, array: MPlugArray) -> MStatus:
        """Get all of the current connections to this node as an array of plugs."""
    def getEffColor(self) -> MColor:
        """Retrieve the cached humanIK color of this effector."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> MStatus:
        """Returns the external content (files) that this node depends on."""
    def getPath(self, path: MDagPath) -> MStatus:
        """Returns a DAG Path to the DAG Node attached to the Function Set."""
    def getPivotOffset(self) -> MVector:
        """Retrieve the pivot offset of this effector."""
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
    def isParentOf(self, node: MObject) -> bool:
        """Determines whether or not the DAG Node attached to the Function Set is a parent of the given node."""
    def isShared(self) -> bool:
        """Indicates whether or not this node is shared."""
    def isTrackingEdits(self) -> bool:
        """Returns whether or not edits on the given node are being tracked by the generalized edit system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def limitValue(self, type: int) -> float:
        """Determine the current value of the specified limit."""
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
    def setEffColor(self, color: MColor) -> MStatus:
        """Set the humanIK color for this effector."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> MStatus:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> MStatus:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> MStatus:
        """Sets the state of the specified flag for the node."""
    def setIcon(self, filename: str) -> MStatus:
        """Associates a custom icon with the node for display in the Maya UI."""
    def setInstanceable(self, how: bool) -> MStatus:
        """Sets whether or not the DAG node is instanceable."""
    def setIntermediateObject(self, isIntermediate: bool) -> MStatus:
        """Sets whether this object is an intermediate in a geometry calculation."""
    def setLimit(self, type: int, value: float) -> MStatus:
        """Change the limit value for the specified limit type, and automatically enable the limit to be true."""
    def setLocked(self, locked: bool) -> MStatus:
        """Locks or unlocks this node."""
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
    def setPivotOffset(self, vector: MVector) -> MStatus:
        """Set the pivot offset for this effector."""
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

class MFnIkEffector:
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
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def classification(nodeTypeName: str) -> str:
        """Retrieves the classification string for a node type."""
    def clearRestPosition(self) -> MStatus:
        """Clear the saved rest position of this transform."""
    @overload
    def create(self, parent: MObject | None = None) -> MObject: ...
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
        """Creates a new end effector."""
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
    def isParentOf(self, node: MObject) -> bool:
        """Determines whether or not the DAG Node attached to the Function Set is a parent of the given node."""
    def isShared(self) -> bool:
        """Indicates whether or not this node is shared."""
    def isTrackingEdits(self) -> bool:
        """Returns whether or not edits on the given node are being tracked by the generalized edit system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def limitValue(self, type: int) -> float:
        """Determine the current value of the specified limit."""
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
    def setExternalContent(self, table: MExternalContentLocationTable) -> MStatus:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> MStatus:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> MStatus:
        """Sets the state of the specified flag for the node."""
    def setIcon(self, filename: str) -> MStatus:
        """Associates a custom icon with the node for display in the Maya UI."""
    def setInstanceable(self, how: bool) -> MStatus:
        """Sets whether or not the DAG node is instanceable."""
    def setIntermediateObject(self, isIntermediate: bool) -> MStatus:
        """Sets whether this object is an intermediate in a geometry calculation."""
    def setLimit(self, type: int, value: float) -> MStatus:
        """Change the limit value for the specified limit type, and automatically enable the limit to be true."""
    def setLocked(self, locked: bool) -> MStatus:
        """Locks or unlocks this node."""
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

class MFnIkHandle:
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
    kStickyOff: Any
    kStickyOn: Any
    kSuperSticky: Any
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
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def classification(nodeTypeName: str) -> str:
        """Retrieves the classification string for a node type."""
    def clearRestPosition(self) -> MStatus:
        """Clear the saved rest position of this transform."""
    @overload
    def create(self, startJoint: MDagPath, effector: MDagPath) -> MObject: ...
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
        """Creates a new ik handle."""
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
    def getEffector(self, effectorPath: MDagPath) -> MStatus:
        """Get a dag path to the end-effector of the handle's joint chain."""
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
    def getStartJoint(self, jointPath: MDagPath) -> MStatus:
        """This method will get a dag path to the starting joint of the handle's joint chain."""
    def getTranslation(self, space: int) -> MVector:
        """Retrieve the translation component of this transformation in centimeters."""
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
    def isParentOf(self, node: MObject) -> bool:
        """Determines whether or not the DAG Node attached to the Function Set is a parent of the given node."""
    def isShared(self) -> bool:
        """Indicates whether or not this node is shared."""
    def isTrackingEdits(self) -> bool:
        """Returns whether or not edits on the given node are being tracked by the generalized edit system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def limitValue(self, type: int) -> float:
        """Determine the current value of the specified limit."""
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
    def poWeight(self) -> float:
        """Gets the position/orientation weight of a handle."""
    def priority(self) -> int:
        """Get the priority of this handle in case a solution is affected by more than one handle."""
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
    def setEffector(self, effectorPath: MDagPath) -> MStatus:
        """Set the dag path to the end-effector of the handle's joint chain."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> MStatus:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> MStatus:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> MStatus:
        """Sets the state of the specified flag for the node."""
    def setIcon(self, filename: str) -> MStatus:
        """Associates a custom icon with the node for display in the Maya UI."""
    def setInstanceable(self, how: bool) -> MStatus:
        """Sets whether or not the DAG node is instanceable."""
    def setIntermediateObject(self, isIntermediate: bool) -> MStatus:
        """Sets whether this object is an intermediate in a geometry calculation."""
    def setLimit(self, type: int, value: float) -> MStatus:
        """Change the limit value for the specified limit type, and automatically enable the limit to be true."""
    def setLocked(self, locked: bool) -> MStatus:
        """Locks or unlocks this node."""
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
    def setPOWeight(self, weight: float) -> MStatus:
        """Sets the position/orientation weight of a handle."""
    def setPriority(self, priority: int) -> MStatus:
        """Set the priority of this handle in case a solution is affected by more than one handle."""
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
    @overload
    def setSolver(self, solver: MObject) -> MStatus: ...
    @overload
    def setSolver(self, solverName: str) -> MStatus:
        """Set the solver for this handle."""
    def setStartJoint(self, jointPath: MDagPath) -> MStatus:
        """This method will set the dag path for the starting joint of the handle's joint chain."""
    def setStartJointAndEffector(self, jointPath: MDagPath, effectorPath: MDagPath) -> MStatus:
        """This method will set the dag path for the starting joint and the end-effector of the handle's joint chain."""
    def setStickiness(self, arg: Any) -> MStatus:
        """Set the stickiness of this handle."""
    def setTranslation(self, vec: MVector, space: int) -> MStatus:
        """Change the translation component of this transformation."""
    def setUseObjectColor(self, useObjectColor: bool) -> MStatus:
        """Deprecated in 2016.0"""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def setWeight(self, weight: float) -> MStatus:
        """Specifies the handles weight in error calculations."""
    def shearBy(self) -> MStatus:
        """Relatively shear this transformation."""
    def solver(self) -> MObject:
        """Returns the solver attached to this handle."""
    def stickiness(self) -> Any:
        """Get the stickiness of this handle."""
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
    def weight(self) -> float:
        """Get the handles weight in error calculations."""

class MFnIkJoint:
    kExtensionAttr: Any
    kInvalidAttr: Any
    kLocalDynamicAttr: Any
    kNextPos: Any
    kNone: Any
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
    kXAxis: Any
    kYAxis: Any
    kZAxis: Any
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
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def classification(nodeTypeName: str) -> str:
        """Retrieves the classification string for a node type."""
    def clearRestPosition(self) -> MStatus:
        """Clear the saved rest position of this transform."""
    @overload
    def create(self, parent: MObject | None = None) -> MObject: ...
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
        """Create a new joint in a skeleton."""
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
    def getDegreesOfFreedom(self, freeInX: bool, freeInY: bool, freeInZ: bool) -> MStatus:
        """Get degrees of freedom of this joint."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> MStatus:
        """Returns the external content (files) that this node depends on."""
    @overload
    def getOrientation(self, quaternion: MQuaternion) -> MStatus: ...
    @overload
    def getOrientation(self, rotation: MEulerRotation) -> MStatus: ...
    @overload
    def getOrientation(self, order: int) -> MStatus:
        """Get the joint orientation."""
    def getPath(self, path: MDagPath) -> MStatus:
        """Returns a DAG Path to the DAG Node attached to the Function Set."""
    def getPreferedAngle(self) -> MStatus:
        """Obsolete - use correctly spelled getPreferredAngle."""
    def getPreferredAngle(self) -> MStatus:
        """Get the preferred orientation for this joint (in XYZ order)"""
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
    @overload
    def getScaleOrientation(self, quaternion: MQuaternion) -> MStatus: ...
    @overload
    def getScaleOrientation(self, order: int) -> MStatus:
        """Get the orientation of the coordinate axes for rotation."""
    def getSegmentScale(self) -> MStatus:
        """Get the local space scale values for the joint segment (bone)."""
    def getShear(self) -> MStatus:
        """Retrieve the shearing component of this transformation."""
    def getStiffness(self) -> MStatus:
        """Get the stiffness (from 0 to 100.0) for the joint."""
    def getTranslation(self, space: int) -> MVector:
        """Retrieve the translation component of this transformation in centimeters."""
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
    def hikJointName(self) -> str:
        """Get the name that the HumanIK solver uses to identify this joint."""
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
    def isParentOf(self, node: MObject) -> bool:
        """Determines whether or not the DAG Node attached to the Function Set is a parent of the given node."""
    def isShared(self) -> bool:
        """Indicates whether or not this node is shared."""
    def isTrackingEdits(self) -> bool:
        """Returns whether or not edits on the given node are being tracked by the generalized edit system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def limitValue(self, type: int) -> float:
        """Determine the current value of the specified limit."""
    def maxRotateDampXRange(self) -> float:
        """Get the maximum of the damping range in X."""
    def maxRotateDampXStrength(self) -> float:
        """Get the minimum of the damping strength in X."""
    def maxRotateDampYRange(self) -> float:
        """Get the maximum of the damping range in Y."""
    def maxRotateDampYStrength(self) -> float:
        """Get the minimum of the damping strength in X."""
    def maxRotateDampZRange(self) -> float:
        """Get the maximum of the damping range in Z."""
    def maxRotateDampZStrength(self) -> float:
        """Get the minimum of the damping strength in X."""
    def minRotateDampXRange(self) -> float:
        """Get the minimum of the damping range in X."""
    def minRotateDampXStrength(self) -> float:
        """Get the minimum of the damping strength in X."""
    def minRotateDampYRange(self) -> float:
        """Get the minimum of the damping range in Y."""
    def minRotateDampYStrength(self) -> float:
        """Get the minimum of the damping strength in X."""
    def minRotateDampZRange(self) -> float:
        """Get the minimum of the damping range in Z."""
    def minRotateDampZStrength(self) -> float:
        """Get the minimum of the damping strength in X."""
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
    def setDegreesOfFreedom(self, freeInX: bool, freeInY: bool, freeInZ: bool) -> MStatus:
        """Set the degrees of freedom of this joint by specifying which axes are allowed to rotate."""
    def setDoNotWrite(self, flag: bool) -> MStatus:
        """Use this method to mark the "do not write" state of this node."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> MStatus:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> MStatus:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> MStatus:
        """Sets the state of the specified flag for the node."""
    def setIcon(self, filename: str) -> MStatus:
        """Associates a custom icon with the node for display in the Maya UI."""
    def setInstanceable(self, how: bool) -> MStatus:
        """Sets whether or not the DAG node is instanceable."""
    def setIntermediateObject(self, isIntermediate: bool) -> MStatus:
        """Sets whether this object is an intermediate in a geometry calculation."""
    def setLimit(self, type: int, value: float) -> MStatus:
        """Change the limit value for the specified limit type, and automatically enable the limit to be true."""
    def setLocked(self, locked: bool) -> MStatus:
        """Locks or unlocks this node."""
    def setMaxRotateDampXRange(self, angle: float) -> MStatus:
        """Set the maximum of the damping range in X."""
    def setMaxRotateDampXStrength(self, angle: float) -> MStatus:
        """Set the maximum of the damping strength in X."""
    def setMaxRotateDampYRange(self, angle: float) -> MStatus:
        """Set the maximum of the damping range in Y."""
    def setMaxRotateDampYStrength(self, angle: float) -> MStatus:
        """Set the maximum of the damping strength in Y."""
    def setMaxRotateDampZRange(self, angle: float) -> MStatus:
        """Set the maximum of the damping range in Z."""
    def setMaxRotateDampZStrength(self, angle: float) -> MStatus:
        """Set the maximum of the damping strength in Z."""
    def setMinRotateDampXRange(self, angle: float) -> MStatus:
        """Set the minimum of the damping range in X."""
    def setMinRotateDampXStrength(self, angle: float) -> MStatus:
        """Set the maximum of the damping strength in Z."""
    def setMinRotateDampYRange(self, angle: float) -> MStatus:
        """Set the minimum of the damping range in Y."""
    def setMinRotateDampYStrength(self, angle: float) -> MStatus:
        """Set the maximum of the damping strength in Y."""
    def setMinRotateDampZRange(self, angle: float) -> MStatus:
        """Set the minimum of the damping range in Z."""
    def setMinRotateDampZStrength(self, angle: float) -> MStatus:
        """Set the minimum of the damping strength in Z."""
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
    @overload
    def setOrientation(self, quaternion: MQuaternion) -> MStatus: ...
    @overload
    def setOrientation(self, rotation: MEulerRotation) -> MStatus: ...
    @overload
    def setOrientation(self, order: int) -> MStatus:
        """Set the jointOrient value."""
    def setPreferedAngle(self) -> MStatus:
        """Obsolete - use correctly spelled setPreferredAngle."""
    def setPreferredAngle(self) -> MStatus:
        """Set the preferred orientation for this joint (in XYZ order)"""
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
    @overload
    def setScaleOrientation(self, quaternion: MQuaternion) -> MStatus: ...
    @overload
    def setScaleOrientation(self, order: int) -> MStatus:
        """Set the orientation of the coordinate axes for rotation."""
    def setScalePivot(self, point: MPoint, space: int, balance: bool) -> MStatus:
        """Set the pivot around which the scale is applied in centimeters."""
    def setScalePivotTranslation(self, vec: MVector, space: int) -> MStatus:
        """Set the scale pivot translation in centimeters."""
    def setSegmentScale(self) -> MStatus:
        """Set the local space scale values for the joint segment (bone)."""
    def setShear(self) -> MStatus:
        """Set the shearing component of this transformation."""
    def setStiffness(self) -> MStatus:
        """Set the stiffness (from 0 to 100.0) for the joint."""
    def setTranslation(self, vec: MVector, space: int) -> MStatus:
        """Change the translation component of this transformation."""
    def setUseObjectColor(self, useObjectColor: bool) -> MStatus:
        """Deprecated in 2016.0"""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
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

class MFnIkSolver:
    kExtensionAttr: Any
    kInvalidAttr: Any
    kLocalDynamicAttr: Any
    kNormalAttr: Any
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
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None:
        """Default constructor."""
    def absoluteName(self) -> str:
        """Returns the absolute name of this node."""
    @overload
    def addAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def addAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Add a new dynamic attibute to this node."""
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
    def canBeWritten(self) -> bool:
        """Returns the do not write state of the node."""
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
    @overload
    def create(self, typeId: MTypeId) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str) -> MObject: ...
    @overload
    def create(self, type: str) -> MObject: ...
    @overload
    def create(self, type: str, name: str) -> MObject:
        """Creates a new dependency node with the given type tag."""
    @staticmethod
    def deallocateAllFlags(pluginName: str) -> MStatus:
        """Deallocates all of the node flags which are currently allocated to the specified plugin."""
    @staticmethod
    def deallocateFlag(pluginName: str, flag: int) -> MStatus:
        """Deallocates a node flag which was previously allocated by a call to allocateFlag ."""
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
    @staticmethod
    def enableDGTiming(enable: bool) -> None:
        """Globally enables or disables the DG node timing mechanism."""
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
    def getAffectedAttributes(self, attr: MObject, affectedAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that are affected by the attribute passed in."""
    def getAffectedByAttributes(self, attr: MObject, affectedByAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that affect the attribute passed in, attr ."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute al"""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns a list of all attribute aliases for this node."""
    def getConnections(self, array: MPlugArray) -> MStatus:
        """Get all of the current connections to this node as an array of plugs."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> MStatus:
        """Returns the external content (files) that this node depends on."""
    def hasAttribute(self, name: str) -> bool:
        """Returns true if the node already has an attribute with the given name."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    def hasUniqueName(self) -> bool:
        """Indicates whether or not this node's name is unique within the scene."""
    def icon(self) -> str:
        """Returns the custom icon filename associated with the node."""
    def isDefaultNode(self) -> bool:
        """Returns true if the node is a default node."""
    def isFlagSet(self, flag: int) -> bool:
        """Retrieves the current state of the specified flag for a node."""
    def isFromReferencedFile(self) -> bool:
        """Indicates whether or not this node came from a referenced file."""
    def isLocked(self) -> bool:
        """Indicates whether or not this node is locked."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Indicates whether or not the specified attribute was added to this node within the current scene."""
    def isShared(self) -> bool:
        """Indicates whether or not this node is shared."""
    def isTrackingEdits(self) -> bool:
        """Returns whether or not edits on the given node are being tracked by the generalized edit system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def maxIterations(self) -> int:
        """Returns the maximum number of iterations used when solving."""
    def name(self) -> str:
        """Returns the name of this node."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def parentNamespace(self) -> str:
        """Returns the name of the namespace in which this node resides."""
    def pluginName(self) -> str:
        """Returns the name of the plug-in this MFnDependendencyNode was defined in."""
    def plugsAlias(self, plug: MPlug) -> str:
        """Returns the alias for the plug's attribute or the empty string if that attribute has no alias."""
    @overload
    def removeAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def removeAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Remove a dynamic attribute from a node."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Some nodes, such as the various animCurve nodes, require that their attributes be set in a specific order for proper ope"""
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setDoNotWrite(self, flag: bool) -> MStatus:
        """Use this method to mark the "do not write" state of this node."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> MStatus:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> MStatus:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> MStatus:
        """Sets the state of the specified flag for the node."""
    def setIcon(self, filename: str) -> MStatus:
        """Associates a custom icon with the node for display in the Maya UI."""
    def setLocked(self, locked: bool) -> MStatus:
        """Locks or unlocks this node."""
    def setMaxIterations(self, maxIters: int) -> MStatus:
        """Sets the maximum number of iterations used when solving."""
    @overload
    def setName(self, name: str, createNamespace: bool = False) -> str: ...
    @overload
    def setName(self, name: str) -> str:
        """Sets the name of this node."""
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches the Function Set to the specified Maya Object."""
    def setTolerance(self, tolerance: float) -> MStatus:
        """Sets the tolerance used when solving."""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def tolerance(self) -> float:
        """Returns the tolerance used when solving."""
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
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnKeyframeDelta:
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
    def keyIndex(self) -> int:
        """The index of this key on the animation curve."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def paramCurve(self) -> MObject:
        """Return the Animation Curve MObject that this key belongs to."""
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches the Function Set to the specified Maya Object."""
    def type(self) -> int:
        """Function set type."""
    @staticmethod
    def typeString(Type: int) -> str:
        """Introduced in 2020.0"""

class MFnKeyframeDeltaAddRemove:
    kAdded: Any
    kRemoved: Any
    kReplaced: Any
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
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def deltaType(self) -> Any:
        """Indicates the type of change that this class instance represents."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def keyIndex(self) -> int:
        """The index of this key on the animation curve."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def paramCurve(self) -> MObject:
        """Return the Animation Curve MObject that this key belongs to."""
    def replacedValue(self) -> float:
        """The value of the key that was replaced."""
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches the Function Set to the specified Maya Object."""
    def time(self) -> MTime:
        """The time value of the key that was added or removed."""
    def type(self) -> int:
        """Function set type."""
    @staticmethod
    def typeString(Type: int) -> str:
        """Introduced in 2020.0"""
    def value(self) -> float:
        """The value of the key that was added or removed."""

class MFnKeyframeDeltaBlockAddRemove:
    kAdded: Any
    kRemoved: Any
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
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def deltaType(self) -> Any:
        """Indicates the type of change, i.e."""
    def endTime(self) -> MTime:
        """Returns an MTime value indicating the endTime of the add/remove."""
    def getTimes(self, times: MTimeArray) -> None:
        """Returns the times of all keys involved in the group add or remove."""
    def getValues(self, values: MDoubleArray) -> None:
        """Returns the values of all keys involved in the group add or remove."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def keyIndex(self) -> int:
        """The index of this key on the animation curve."""
    def numKeys(self) -> int:
        """Total number of keys involved in this add or remove operation."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def paramCurve(self) -> MObject:
        """Return the Animation Curve MObject that this key belongs to."""
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches the Function Set to the specified Maya Object."""
    def startTime(self) -> MTime:
        """An MTime value indicating the start time of the add/remove."""
    def type(self) -> int:
        """Function set type."""
    @staticmethod
    def typeString(Type: int) -> str:
        """Introduced in 2020.0"""

class MFnKeyframeDeltaBreakdown:
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
    def isBreakdown(self) -> bool:
        """Returns the current breakdown state of the key."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def keyIndex(self) -> int:
        """The index of this key on the animation curve."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def paramCurve(self) -> MObject:
        """Return the Animation Curve MObject that this key belongs to."""
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches the Function Set to the specified Maya Object."""
    def type(self) -> int:
        """Function set type."""
    @staticmethod
    def typeString(Type: int) -> str:
        """Introduced in 2020.0"""
    def wasBreakdown(self) -> bool:
        """Returns the previous breakdown state of the key."""

class MFnKeyframeDeltaInfType:
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
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def currentInfinityType(self) -> int:
        """The current infinity type."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    def isPreInfinity(self) -> bool:
        """This class can describe changes to both the pre-infinity and post-infinity this method allows the API user to figure out"""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def keyIndex(self) -> int:
        """The index of this key on the animation curve."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def paramCurve(self) -> MObject:
        """Return the Animation Curve MObject that this key belongs to."""
    def previousInfinityType(self) -> int:
        """The previous infinity type."""
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches the Function Set to the specified Maya Object."""
    def type(self) -> int:
        """Function set type."""
    @staticmethod
    def typeString(Type: int) -> str:
        """Introduced in 2020.0"""

class MFnKeyframeDeltaMove:
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
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def currentTime(self) -> MTime:
        """The current/current time value."""
    def currentValue(self) -> float:
        """The current value of the key."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def keyIndex(self) -> int:
        """The current index value of this key."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def paramCurve(self) -> MObject:
        """Return the Animation Curve MObject that this key belongs to."""
    def previousIndex(self) -> int:
        """The previous index value of this key."""
    def previousTime(self) -> MTime:
        """The previous time value of this key."""
    def previousValue(self) -> float:
        """The previous value of the key prior to the change."""
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches the Function Set to the specified Maya Object."""
    def type(self) -> int:
        """Function set type."""
    @staticmethod
    def typeString(Type: int) -> str:
        """Introduced in 2020.0"""

class MFnKeyframeDeltaScale:
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
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def currentEndTime(self) -> MTime:
        """The current end time."""
    def currentStartTime(self) -> MTime:
        """The current scale time (after scaling has been performed)."""
    def endTime(self) -> MTime:
        """The end time of the scaling block."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def keyIndex(self) -> int:
        """The index of this key on the animation curve."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def paramCurve(self) -> MObject:
        """Return the Animation Curve MObject that this key belongs to."""
    def pivotTime(self) -> MTime:
        """The pivot point of the scale (in time)."""
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches the Function Set to the specified Maya Object."""
    def startTime(self) -> MTime:
        """The start time of the scaling block."""
    def type(self) -> int:
        """Function set type."""
    @staticmethod
    def typeString(Type: int) -> str:
        """Introduced in 2020.0"""

class MFnKeyframeDeltaTangent:
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
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def currentTangentType(self) -> int:
        """Returns the current tangent type that the key represents."""
    def getCurrentPosition(self, x: int, y: int) -> MStatus:
        """Get the values of the current time/value position of the tangent for this key."""
    def getPreviousPosition(self, x: int, y: int) -> MStatus:
        """Get the values of the previous time/value position of the tangent for this key."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    def isInTangent(self) -> bool:
        """Key's have two tangents, in-bound and out-bound."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def keyIndex(self) -> int:
        """The index of this key on the animation curve."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def paramCurve(self) -> MObject:
        """Return the Animation Curve MObject that this key belongs to."""
    def previousTangentType(self) -> int:
        """Returns the previous tangent type."""
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches the Function Set to the specified Maya Object."""
    def type(self) -> int:
        """Function set type."""
    @staticmethod
    def typeString(Type: int) -> str:
        """Introduced in 2020.0"""

class MFnKeyframeDeltaWeighted:
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
    def keyIndex(self) -> int:
        """The index of this key on the animation curve."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def paramCurve(self) -> MObject:
        """Return the Animation Curve MObject that this key belongs to."""
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches the Function Set to the specified Maya Object."""
    def type(self) -> int:
        """Function set type."""
    @staticmethod
    def typeString(Type: int) -> str:
        """Introduced in 2020.0"""
    def wasWeighted(self) -> bool:
        """Returns true if the key had weighted tangent, but it is not currently."""

class MFnLattice:
    kExtensionAttr: Any
    kInvalidAttr: Any
    kLocalDynamicAttr: Any
    kNextPos: Any
    kNormalAttr: Any
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
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def classification(nodeTypeName: str) -> str:
        """Retrieves the classification string for a node type."""
    @overload
    def create(self, xDiv: int, yDiv: int, zDiv: int, parentOrOwner: MObject | None = None) -> MObject: ...
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
        """Create a new lattice."""
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
    def duplicate(self, instance: bool = False, instanceLeaf: bool = False) -> MObject:
        """This method duplicates the DAG hierarchy rooted at the current node."""
    @staticmethod
    def enableDGTiming(enable: bool) -> None:
        """Globally enables or disables the DG node timing mechanism."""
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
    def getDivisions(self, s: int, t: int, u: int) -> MStatus:
        """Get the number of divisions in the lattice."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> MStatus:
        """Returns the external content (files) that this node depends on."""
    def getPath(self, path: MDagPath) -> MStatus:
        """Returns a DAG Path to the DAG Node attached to the Function Set."""
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
    def isLocked(self) -> bool:
        """Indicates whether or not this node is locked."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Indicates whether or not the specified attribute was added to this node within the current scene."""
    def isParentOf(self, node: MObject) -> bool:
        """Determines whether or not the DAG Node attached to the Function Set is a parent of the given node."""
    def isShared(self) -> bool:
        """Indicates whether or not this node is shared."""
    def isTrackingEdits(self) -> bool:
        """Returns whether or not edits on the given node are being tracked by the generalized edit system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
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
    def point(self, s: int, t: int, u: int) -> MPoint:
        """Returns the point in the lattice that is at the given indices."""
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
    def reset(self, sSize: float = 1.0, tSize: float = 1.0, uSize: float = 1.0) -> MStatus:
        """Reset the lattice points to a uniform parallelipiped shape with the specified dimensions: sSize x tSize x uSize."""
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setDivisions(self, s: int, t: int, u: int) -> MStatus:
        """Set the number of divisions in the lattice."""
    def setDoNotWrite(self, flag: bool) -> MStatus:
        """Use this method to mark the "do not write" state of this node."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> MStatus:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> MStatus:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> MStatus:
        """Sets the state of the specified flag for the node."""
    def setIcon(self, filename: str) -> MStatus:
        """Associates a custom icon with the node for display in the Maya UI."""
    def setInstanceable(self, how: bool) -> MStatus:
        """Sets whether or not the DAG node is instanceable."""
    def setIntermediateObject(self, isIntermediate: bool) -> MStatus:
        """Sets whether this object is an intermediate in a geometry calculation."""
    def setLocked(self, locked: bool) -> MStatus:
        """Locks or unlocks this node."""
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
    def setUseObjectColor(self, useObjectColor: bool) -> MStatus:
        """Deprecated in 2016.0"""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
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

class MFnLatticeDeformer:
    kExtensionAttr: Any
    kInvalidAttr: Any
    kLocalDynamicAttr: Any
    kNormalAttr: Any
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
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None:
        """Default constructor."""
    def absoluteName(self) -> str:
        """Returns the absolute name of this node."""
    @overload
    def addAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def addAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Add a new dynamic attibute to this node."""
    def addExternalContentForFileAttr(self, table: MExternalContentInfoTable, attr: MObject) -> MStatus:
        """Adds content info to the specified table from a file path attribute."""
    def addGeometry(self, object: MObject) -> MStatus:
        """Adds a piece of geometry to the deformation."""
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
    def baseLattice(self) -> MObject:
        """This returns the base version of the lattice that describes the region of space deformed by the lattice."""
    def canBeWritten(self) -> bool:
        """Returns the do not write state of the node."""
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
    @overload
    def create(self, xDiv: int, yDiv: int, zDiv: int) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str) -> MObject: ...
    @overload
    def create(self, type: str) -> MObject: ...
    @overload
    def create(self, type: str, name: str) -> MObject:
        """Creates a new lattice deformer with the given number of divisions."""
    @staticmethod
    def deallocateAllFlags(pluginName: str) -> MStatus:
        """Deallocates all of the node flags which are currently allocated to the specified plugin."""
    @staticmethod
    def deallocateFlag(pluginName: str, flag: int) -> MStatus:
        """Deallocates a node flag which was previously allocated by a call to allocateFlag ."""
    def deformLattice(self) -> MObject:
        """This returns the deformed version of the lattice."""
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
    @staticmethod
    def enableDGTiming(enable: bool) -> None:
        """Globally enables or disables the DG node timing mechanism."""
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
    def getAffectedAttributes(self, attr: MObject, affectedAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that are affected by the attribute passed in."""
    def getAffectedByAttributes(self, attr: MObject, affectedByAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that affect the attribute passed in, attr ."""
    def getAffectedGeometry(self, objects: MObjectArray) -> MStatus:
        """The geometry affected by this deformer is packed into the provided list of MObjects."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute al"""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns a list of all attribute aliases for this node."""
    def getConnections(self, array: MPlugArray) -> MStatus:
        """Get all of the current connections to this node as an array of plugs."""
    def getDivisions(self, x: int, y: int, z: int) -> MStatus:
        """Retrieve the number of divisions in each of the X, Y, and Z directions."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> MStatus:
        """Returns the external content (files) that this node depends on."""
    def hasAttribute(self, name: str) -> bool:
        """Returns true if the node already has an attribute with the given name."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    def hasUniqueName(self) -> bool:
        """Indicates whether or not this node's name is unique within the scene."""
    def icon(self) -> str:
        """Returns the custom icon filename associated with the node."""
    def isDefaultNode(self) -> bool:
        """Returns true if the node is a default node."""
    def isFlagSet(self, flag: int) -> bool:
        """Retrieves the current state of the specified flag for a node."""
    def isFromReferencedFile(self) -> bool:
        """Indicates whether or not this node came from a referenced file."""
    def isLocked(self) -> bool:
        """Indicates whether or not this node is locked."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Indicates whether or not the specified attribute was added to this node within the current scene."""
    def isShared(self) -> bool:
        """Indicates whether or not this node is shared."""
    def isTrackingEdits(self) -> bool:
        """Returns whether or not edits on the given node are being tracked by the generalized edit system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def name(self) -> str:
        """Returns the name of this node."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def parentNamespace(self) -> str:
        """Returns the name of the namespace in which this node resides."""
    def pluginName(self) -> str:
        """Returns the name of the plug-in this MFnDependendencyNode was defined in."""
    def plugsAlias(self, plug: MPlug) -> str:
        """Returns the alias for the plug's attribute or the empty string if that attribute has no alias."""
    @overload
    def removeAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def removeAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Remove a dynamic attribute from a node."""
    def removeGeometry(self, object: MObject) -> MStatus:
        """Removes a piece of geometry from the deformation."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Some nodes, such as the various animCurve nodes, require that their attributes be set in a specific order for proper ope"""
    def resetLattice(self, centerLattice: bool = False) -> MStatus:
        """This method resets the deformed lattice to match the base lattice."""
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setDivisions(self, x: int, y: int, z: int) -> MStatus:
        """Set the number of divisions in each of the X, Y, and Z directions."""
    def setDoNotWrite(self, flag: bool) -> MStatus:
        """Use this method to mark the "do not write" state of this node."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> MStatus:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> MStatus:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> MStatus:
        """Sets the state of the specified flag for the node."""
    def setIcon(self, filename: str) -> MStatus:
        """Associates a custom icon with the node for display in the Maya UI."""
    def setLocked(self, locked: bool) -> MStatus:
        """Locks or unlocks this node."""
    @overload
    def setName(self, name: str, createNamespace: bool = False) -> str: ...
    @overload
    def setName(self, name: str) -> str:
        """Sets the name of this node."""
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches the Function Set to the specified Maya Object."""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
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
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnMotionPath:
    kExtensionAttr: Any
    kInvalidAttr: Any
    kLocalDynamicAttr: Any
    kNormalAttr: Any
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
    kXaxis: Any
    kYaxis: Any
    kZaxis: Any
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None:
        """Default constructor."""
    def absoluteName(self) -> str:
        """Returns the absolute name of this node."""
    def addAnimatedObject(self, objectToAnimate: MDagPath, modifier: MDGModifier | None = None) -> MStatus:
        """Add an object to be animated along this motion path."""
    @overload
    def addAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def addAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Add a new dynamic attibute to this node."""
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
    def bank(self, *args: Any, **kwargs: Any) -> Any: ...
    def bankScale(self) -> float:
        """Return the bank scale for this motion path."""
    def bankThreshold(self) -> float:
        """Return the bank threshold for this motion path."""
    def canBeWritten(self) -> bool:
        """Returns the do not write state of the node."""
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
    @overload
    def create(self, pathObject: MDagPath, objectToAnimate: MDagPath, timeStart: MTime, timeEnd: MTime, modifier: MDGModifier | None = None) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str) -> MObject: ...
    @overload
    def create(self, type: str) -> MObject: ...
    @overload
    def create(self, type: str, name: str) -> MObject:
        """Create a new motion path dependency node."""
    @staticmethod
    def deallocateAllFlags(pluginName: str) -> MStatus:
        """Deallocates all of the node flags which are currently allocated to the specified plugin."""
    @staticmethod
    def deallocateFlag(pluginName: str, flag: int) -> MStatus:
        """Deallocates a node flag which was previously allocated by a call to allocateFlag ."""
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
    @staticmethod
    def enableDGTiming(enable: bool) -> None:
        """Globally enables or disables the DG node timing mechanism."""
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
    def follow(self) -> bool:
        """Determines whether follow is set for this motion path node."""
    def followAxis(self) -> Any:
        """Return the follow axis for this motion path."""
    def getAffectedAttributes(self, attr: MObject, affectedAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that are affected by the attribute passed in."""
    def getAffectedByAttributes(self, attr: MObject, affectedByAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that affect the attribute passed in, attr ."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute al"""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns a list of all attribute aliases for this node."""
    def getAnimatedObjects(self, array: MDagPathArray) -> MStatus:
        """Returns an array of dag paths to the animated objects for this motion path."""
    def getConnections(self, array: MPlugArray) -> MStatus:
        """Get all of the current connections to this node as an array of plugs."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> MStatus:
        """Returns the external content (files) that this node depends on."""
    def getOrientationMarker(self, arg: int) -> MObject:
        """Gets the orientation marker where markerNum is the order in which the marker was created."""
    def getPositionMarker(self, arg: int) -> MObject:
        """Gets the position marker where markerNum is the order in which the marker was created."""
    def hasAttribute(self, name: str) -> bool:
        """Returns true if the node already has an attribute with the given name."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    def hasUniqueName(self) -> bool:
        """Indicates whether or not this node's name is unique within the scene."""
    def icon(self) -> str:
        """Returns the custom icon filename associated with the node."""
    def inverseNormal(self) -> bool:
        """Determines whether the up-axis of the animated object for this motion path is aligned to the opposite direction of the n"""
    def isDefaultNode(self) -> bool:
        """Returns true if the node is a default node."""
    def isFlagSet(self, flag: int) -> bool:
        """Retrieves the current state of the specified flag for a node."""
    def isFromReferencedFile(self) -> bool:
        """Indicates whether or not this node came from a referenced file."""
    def isLocked(self) -> bool:
        """Indicates whether or not this node is locked."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Indicates whether or not the specified attribute was added to this node within the current scene."""
    def isShared(self) -> bool:
        """Indicates whether or not this node is shared."""
    def isTrackingEdits(self) -> bool:
        """Returns whether or not edits on the given node are being tracked by the generalized edit system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def name(self) -> str:
        """Returns the name of this node."""
    def numOrientationMarkers(self) -> int:
        """Returns the number of orientation markers on this motion path."""
    def numPositionMarkers(self) -> int:
        """Returns the number of position markers on this motion path."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def parentNamespace(self) -> str:
        """Returns the name of the namespace in which this node resides."""
    def pathObject(self) -> MDagPath:
        """Return a dag path to the motion path object."""
    def pluginName(self) -> str:
        """Returns the name of the plug-in this MFnDependendencyNode was defined in."""
    def plugsAlias(self, plug: MPlug) -> str:
        """Returns the alias for the plug's attribute or the empty string if that attribute has no alias."""
    @overload
    def removeAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def removeAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Remove a dynamic attribute from a node."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Some nodes, such as the various animCurve nodes, require that their attributes be set in a specific order for proper ope"""
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setBank(self, bank: bool) -> MStatus:
        """Determines whether bank has been enabled for this motion path."""
    def setBankScale(self, bankScale: float) -> MStatus:
        """Set the bank scale for this motion path."""
    def setBankThreshold(self, bankThreshold: float) -> MStatus:
        """Set the bank threshold for this motion path."""
    def setDoNotWrite(self, flag: bool) -> MStatus:
        """Use this method to mark the "do not write" state of this node."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> MStatus:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> MStatus:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> MStatus:
        """Sets the state of the specified flag for the node."""
    def setFollow(self, on: bool, modifier: MDGModifier | None = None) -> MStatus:
        """Setting follow on will cause the animated object(s) local axis to be aligned with the tangent of the motion path."""
    def setFollowAxis(self, arg: Any) -> MStatus:
        """Sets the axis of the animated object that will follow the motion path."""
    def setIcon(self, filename: str) -> MStatus:
        """Associates a custom icon with the node for display in the Maya UI."""
    def setInverseNormal(self, invert: bool) -> MStatus:
        """If true , enable alignment of the up axis of the moving object(s) to the opposite direction of the normal vector of the """
    def setLocked(self, locked: bool) -> MStatus:
        """Locks or unlocks this node."""
    @overload
    def setName(self, name: str, createNamespace: bool = False) -> str: ...
    @overload
    def setName(self, name: str) -> str:
        """Sets the name of this node."""
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches the Function Set to the specified Maya Object."""
    def setPathObject(self, pathObject: MDagPath, modifier: MDGModifier | None = None) -> MStatus:
        """Set the curve or surface for this motion path."""
    def setUEnd(self, end: float) -> MStatus:
        """Sets the end value of the u parameterization for the animation."""
    def setUStart(self, start: float) -> MStatus:
        """Sets the starting value of the u parameterization for the animation."""
    def setUTimeEnd(self, end: MTime) -> MStatus:
        """Sets the end time of the animation for the u parameter."""
    def setUTimeStart(self, start: MTime) -> MStatus:
        """Sets the starting time of the animation for the u parameter."""
    def setUpAxis(self, arg: Any) -> MStatus:
        """Set the up-axis for this motion path."""
    def setUseNormal(self, use: bool) -> MStatus:
        """If true , enables alignment of the up axis of the animated object to the normal vector of the path geometry."""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def type(self) -> int:
        """Function set type."""
    def typeId(self) -> MTypeId:
        """Returns the type id of this node."""
    def typeName(self) -> str:
        """Returns the type name of this node."""
    @staticmethod
    def typeString(Type: int) -> str:
        """Introduced in 2020.0"""
    def uEnd(self) -> float:
        """Returns the end value of the u parameterization for the animation."""
    def uStart(self) -> float:
        """Returns the starting value of the u parameterization for the animation."""
    def uTimeEnd(self) -> MTime:
        """Returns the end time of the animation for the u parameter."""
    def uTimeStart(self) -> MTime:
        """Returns the start time of the animation for the u parameter."""
    def uniqueName(self) -> str:
        """Introduced in 2023.0"""
    def upAxis(self) -> Any:
        """Return the up-axis for this motion path."""
    def useNormal(self) -> bool:
        """Determines whether the up-axis of the animated object for this motion path is aligned with the normal vector of the path"""
    def userNode(self) -> Any:
        """If the function set's node is a plug-in node, then this method will extract the MPxNode pointer from it."""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnSkinCluster:
    kExtensionAttr: Any
    kInvalidAttr: Any
    kLocalDynamicAttr: Any
    kNormalAttr: Any
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
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None:
        """Default constructor."""
    def absoluteName(self) -> str:
        """Returns the absolute name of this node."""
    @overload
    def addAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def addAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Add a new dynamic attibute to this node."""
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
    def canBeWritten(self) -> bool:
        """Returns the do not write state of the node."""
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
    @overload
    def create(self, typeId: MTypeId) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str) -> MObject: ...
    @overload
    def create(self, type: str) -> MObject: ...
    @overload
    def create(self, type: str, name: str) -> MObject:
        """Creates a new dependency node with the given type tag."""
    @staticmethod
    def deallocateAllFlags(pluginName: str) -> MStatus:
        """Deallocates all of the node flags which are currently allocated to the specified plugin."""
    @staticmethod
    def deallocateFlag(pluginName: str, flag: int) -> MStatus:
        """Deallocates a node flag which was previously allocated by a call to allocateFlag ."""
    def deformerSet(self) -> MObject:
        """Returns the set containing the objects that are deformed."""
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
    @staticmethod
    def enableDGTiming(enable: bool) -> None:
        """Globally enables or disables the DG node timing mechanism."""
    def envelope(self) -> float:
        """Returns the envelope value."""
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
    def getAffectedAttributes(self, attr: MObject, affectedAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that are affected by the attribute passed in."""
    def getAffectedByAttributes(self, attr: MObject, affectedByAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that affect the attribute passed in, attr ."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute al"""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns a list of all attribute aliases for this node."""
    def getBlendWeights(self, path: MDagPath, components: MObject, weights: MDoubleArray) -> MStatus:
        """This method returns weights from skinCluster's blend weight array."""
    def getComponentAtIndex(self, index: int) -> MObject:
        """Introduced in 2022.0"""
    def getConnections(self, array: MPlugArray) -> MStatus:
        """Get all of the current connections to this node as an array of plugs."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> MStatus:
        """Returns the external content (files) that this node depends on."""
    def getIndexMapper(self, index: int) -> MStatus:
        """Introduced in 2024.1"""
    def getInputGeometry(self, objects: MObjectArray) -> MStatus:
        """This method returns the input geometry for the deformer by traversing the graph to find upstream shape nodes."""
    def getOutputGeometry(self, objects: MObjectArray) -> MStatus:
        """The output geometry is packed into the provided list of MObjects."""
    def getPathAtIndex(self, index: int, path: MDagPath) -> MStatus:
        """The DAG path of the output geometry at the specified plug index is put in the dagPath argument."""
    @overload
    def getPointsAffectedByInfluence(self, path: MDagPath, result: MSelectionList, weights: MDoubleArray) -> MStatus: ...
    @overload
    def getPointsAffectedByInfluence(self, path: MDagPath, result: MSelectionList, weights: MFloatArray) -> MStatus:
        """During deformation, the skinCluster algorithm is applied for a given influence object on all points in the deformer's se"""
    @overload
    def getWeights(self, path: MDagPath, components: MObject, influenceIndex: int, weights: MDoubleArray) -> MStatus: ...
    @overload
    def getWeights(self, path: MDagPath, components: MObject, weights: MDoubleArray, influenceCount: int) -> MStatus: ...
    @overload
    def getWeights(self, path: MDagPath, components: MObject, influenceIndices: MIntArray, weights: MDoubleArray) -> MStatus: ...
    @overload
    def getWeights(self, path: MDagPath, components: MObject, influenceIndex: int, weights: MFloatArray) -> MStatus: ...
    @overload
    def getWeights(self, path: MDagPath, components: MObject, weights: MFloatArray, influenceCount: int) -> MStatus:
        """Gets the skinCluster weights for the influence object for the specified components of the object whose dagPath is specif"""
    def groupIdAtIndex(self, index: int) -> int:
        """Returns the groupId at the specified plug index."""
    def hasAttribute(self, name: str) -> bool:
        """Returns true if the node already has an attribute with the given name."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    def hasUniqueName(self) -> bool:
        """Indicates whether or not this node's name is unique within the scene."""
    def icon(self) -> str:
        """Returns the custom icon filename associated with the node."""
    def indexForGroupId(self, groupId: int) -> int:
        """Returns the plug index corresponding to the groupId."""
    def indexForInfluenceObject(self, path: MDagPath) -> int:
        """Returns the logical index of the matrix array attribute where the specified influence object is attached."""
    def indexForOutputConnection(self, connectionIndex: int) -> int:
        """Returns the plug index corresponding to the connection index."""
    def indexForOutputShape(self, shape: MObject) -> int:
        """Returns the plug index for the specified output shape."""
    def influenceObjects(self, paths: MDagPathArray) -> int:
        """Returns an array of paths to the influence objects for the skinCluster."""
    def inputShapeAtIndex(self, index: int) -> MObject:
        """Returns the input shape corresponding to the plug index."""
    def isDefaultNode(self) -> bool:
        """Returns true if the node is a default node."""
    def isFlagSet(self, flag: int) -> bool:
        """Retrieves the current state of the specified flag for a node."""
    def isFromReferencedFile(self) -> bool:
        """Indicates whether or not this node came from a referenced file."""
    def isLocked(self) -> bool:
        """Indicates whether or not this node is locked."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Indicates whether or not the specified attribute was added to this node within the current scene."""
    def isShared(self) -> bool:
        """Indicates whether or not this node is shared."""
    def isTrackingEdits(self) -> bool:
        """Returns whether or not edits on the given node are being tracked by the generalized edit system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def name(self) -> str:
        """Returns the name of this node."""
    def numOutputConnections(self) -> int:
        """Returns the number of output geometries connected to this node."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def outputShapeAtIndex(self, index: int) -> MObject:
        """Returns the output shape corresponding to the plug index."""
    def parentNamespace(self) -> str:
        """Returns the name of the namespace in which this node resides."""
    def pluginName(self) -> str:
        """Returns the name of the plug-in this MFnDependendencyNode was defined in."""
    def plugsAlias(self, plug: MPlug) -> str:
        """Returns the alias for the plug's attribute or the empty string if that attribute has no alias."""
    @overload
    def removeAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def removeAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Remove a dynamic attribute from a node."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Some nodes, such as the various animCurve nodes, require that their attributes be set in a specific order for proper ope"""
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setBlendWeights(self, path: MDagPath, components: MObject, weights: MDoubleArray) -> MStatus:
        """This method sets weights in skinCluster's blend weight array."""
    def setDoNotWrite(self, flag: bool) -> MStatus:
        """Use this method to mark the "do not write" state of this node."""
    def setEnvelope(self, envelope: float) -> MStatus:
        """Sets the envelope value."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> MStatus:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> MStatus:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> MStatus:
        """Sets the state of the specified flag for the node."""
    def setIcon(self, filename: str) -> MStatus:
        """Associates a custom icon with the node for display in the Maya UI."""
    def setLocked(self, locked: bool) -> MStatus:
        """Locks or unlocks this node."""
    @overload
    def setName(self, name: str, createNamespace: bool = False) -> str: ...
    @overload
    def setName(self, name: str) -> str:
        """Sets the name of this node."""
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches the Function Set to the specified Maya Object."""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    @overload
    def setWeights(self, path: MDagPath, components: MObject, jointIndex: int, value: float, normalize: bool = True, oldValues: MDoubleArray | None = None) -> MStatus: ...
    @overload
    def setWeights(self, path: MDagPath, components: MObject, influenceIndices: MIntArray, values: MDoubleArray, normalize: bool = True, oldValues: MDoubleArray | None = None) -> MStatus: ...
    @overload
    def setWeights(self, path: MDagPath, components: MObject, jointIndex: int, value: float, normalize: bool = True, oldValues: MFloatArray | None = None) -> MStatus: ...
    @overload
    def setWeights(self, path: MDagPath, components: MObject, influenceIndices: MIntArray, values: MFloatArray, normalize: bool = True, oldValues: MFloatArray | None = None) -> MStatus:
        """Sets the skinCluster weight for the influence object on the specified components of the object whose dagPath is specifie"""
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
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnWeightGeometryFilter:
    kExtensionAttr: Any
    kInvalidAttr: Any
    kLocalDynamicAttr: Any
    kNormalAttr: Any
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
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None:
        """Default constructor."""
    def absoluteName(self) -> str:
        """Returns the absolute name of this node."""
    @overload
    def addAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def addAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Add a new dynamic attibute to this node."""
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
    def canBeWritten(self) -> bool:
        """Returns the do not write state of the node."""
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
    @overload
    def create(self, typeId: MTypeId) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str) -> MObject: ...
    @overload
    def create(self, type: str) -> MObject: ...
    @overload
    def create(self, type: str, name: str) -> MObject:
        """Creates a new dependency node with the given type tag."""
    @staticmethod
    def deallocateAllFlags(pluginName: str) -> MStatus:
        """Deallocates all of the node flags which are currently allocated to the specified plugin."""
    @staticmethod
    def deallocateFlag(pluginName: str, flag: int) -> MStatus:
        """Deallocates a node flag which was previously allocated by a call to allocateFlag ."""
    def deformerSet(self) -> MObject:
        """Returns the set containing the objects that are deformed."""
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
    @staticmethod
    def enableDGTiming(enable: bool) -> None:
        """Globally enables or disables the DG node timing mechanism."""
    def envelope(self) -> float:
        """Returns the envelope value."""
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
    def getAffectedAttributes(self, attr: MObject, affectedAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that are affected by the attribute passed in."""
    def getAffectedByAttributes(self, attr: MObject, affectedByAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that affect the attribute passed in, attr ."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute al"""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns a list of all attribute aliases for this node."""
    def getComponentAtIndex(self, index: int) -> MObject:
        """Introduced in 2022.0"""
    def getConnections(self, array: MPlugArray) -> MStatus:
        """Get all of the current connections to this node as an array of plugs."""
    def getEnvelopeWeights(self, index: int, weights: MFloatArray) -> MStatus:
        """Introduced in 2024.1"""
    def getExternalContent(self, table: MExternalContentInfoTable) -> MStatus:
        """Returns the external content (files) that this node depends on."""
    def getIndexMapper(self, index: int) -> MStatus:
        """Introduced in 2024.1"""
    def getInputGeometry(self, objects: MObjectArray) -> MStatus:
        """This method returns the input geometry for the deformer by traversing the graph to find upstream shape nodes."""
    def getOutputGeometry(self, objects: MObjectArray) -> MStatus:
        """The output geometry is packed into the provided list of MObjects."""
    def getPathAtIndex(self, index: int, path: MDagPath) -> MStatus:
        """The DAG path of the output geometry at the specified plug index is put in the dagPath argument."""
    @overload
    def getWeightPlugStrings(self, list: MSelectionList, plugStringArray: Any) -> MStatus: ...
    @overload
    def getWeightPlugStrings(self, list: MSelectionList, plugStrings: str) -> MStatus:
        """Set the plugStringArray argument to contain the names of the plugs on this node that correspond to the components in the"""
    @overload
    def getWeights(self, index: int, components: MObject, weights: MFloatArray) -> MStatus: ...
    @overload
    def getWeights(self, path: MDagPath, components: MObject, weights: MFloatArray) -> MStatus:
        """Gets the weights of the components that correspond to the geometry at the specified plug index."""
    def groupIdAtIndex(self, index: int) -> int:
        """Returns the groupId at the specified plug index."""
    def hasAttribute(self, name: str) -> bool:
        """Returns true if the node already has an attribute with the given name."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    def hasUniqueName(self) -> bool:
        """Indicates whether or not this node's name is unique within the scene."""
    def icon(self) -> str:
        """Returns the custom icon filename associated with the node."""
    def indexForGroupId(self, groupId: int) -> int:
        """Returns the plug index corresponding to the groupId."""
    def indexForOutputConnection(self, connectionIndex: int) -> int:
        """Returns the plug index corresponding to the connection index."""
    def indexForOutputShape(self, shape: MObject) -> int:
        """Returns the plug index for the specified output shape."""
    def inputShapeAtIndex(self, index: int) -> MObject:
        """Returns the input shape corresponding to the plug index."""
    def isDefaultNode(self) -> bool:
        """Returns true if the node is a default node."""
    def isFlagSet(self, flag: int) -> bool:
        """Retrieves the current state of the specified flag for a node."""
    def isFromReferencedFile(self) -> bool:
        """Indicates whether or not this node came from a referenced file."""
    def isLocked(self) -> bool:
        """Indicates whether or not this node is locked."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Indicates whether or not the specified attribute was added to this node within the current scene."""
    def isShared(self) -> bool:
        """Indicates whether or not this node is shared."""
    def isTrackingEdits(self) -> bool:
        """Returns whether or not edits on the given node are being tracked by the generalized edit system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def name(self) -> str:
        """Returns the name of this node."""
    def numOutputConnections(self) -> int:
        """Returns the number of output geometries connected to this node."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def outputShapeAtIndex(self, index: int) -> MObject:
        """Returns the output shape corresponding to the plug index."""
    def parentNamespace(self) -> str:
        """Returns the name of the namespace in which this node resides."""
    def pluginName(self) -> str:
        """Returns the name of the plug-in this MFnDependendencyNode was defined in."""
    def plugsAlias(self, plug: MPlug) -> str:
        """Returns the alias for the plug's attribute or the empty string if that attribute has no alias."""
    @overload
    def removeAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def removeAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Remove a dynamic attribute from a node."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Some nodes, such as the various animCurve nodes, require that their attributes be set in a specific order for proper ope"""
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setDoNotWrite(self, flag: bool) -> MStatus:
        """Use this method to mark the "do not write" state of this node."""
    def setEnvelope(self, envelope: float) -> MStatus:
        """Sets the envelope value."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> MStatus:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> MStatus:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> MStatus:
        """Sets the state of the specified flag for the node."""
    def setIcon(self, filename: str) -> MStatus:
        """Associates a custom icon with the node for display in the Maya UI."""
    def setLocked(self, locked: bool) -> MStatus:
        """Locks or unlocks this node."""
    @overload
    def setName(self, name: str, createNamespace: bool = False) -> str: ...
    @overload
    def setName(self, name: str) -> str:
        """Sets the name of this node."""
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches the Function Set to the specified Maya Object."""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    @overload
    def setWeight(self, path: MDagPath, index: int, components: MObject, weight: float, oldValues: MFloatArray | None = None) -> MStatus: ...
    @overload
    def setWeight(self, path: MDagPath, components: MObject, weight: float, oldValues: MFloatArray | None = None) -> MStatus: ...
    @overload
    def setWeight(self, path: MDagPath, index: int, components: MObject, values: MFloatArray) -> MStatus: ...
    @overload
    def setWeight(self, path: MDagPath, components: MObject, values: MFloatArray) -> MStatus:
        """Sets the weights of the specified components of the object whose DAG path is specified."""
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
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""
    def weightPlugStrings(self, list: MSelectionList) -> str:
        """Sets the plugStrings argument to be a string (separated by spaces) containing the names of the plugs on this node that c"""

class MFnWireDeformer:
    kExtensionAttr: Any
    kInvalidAttr: Any
    kLocalDynamicAttr: Any
    kNormalAttr: Any
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
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None: ...
    @overload
    def __init__(self, object: MObject) -> None:
        """Default constructor."""
    def absoluteName(self) -> str:
        """Returns the absolute name of this node."""
    @overload
    def addAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def addAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Add a new dynamic attibute to this node."""
    def addExternalContentForFileAttr(self, table: MExternalContentInfoTable, attr: MObject) -> MStatus:
        """Adds content info to the specified table from a file path attribute."""
    def addGeometry(self, object: MObject) -> MStatus:
        """Adds a piece of geometry to the deformation."""
    def addWire(self, object: MObject) -> MStatus:
        """Adds a new wire curve to the deformation."""
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
    def canBeWritten(self) -> bool:
        """Returns the do not write state of the node."""
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
    @overload
    def create(self) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId) -> MObject: ...
    @overload
    def create(self, typeId: MTypeId, name: str) -> MObject: ...
    @overload
    def create(self, type: str) -> MObject: ...
    @overload
    def create(self, type: str, name: str) -> MObject:
        """Creates a new wire deformer."""
    def crossingEffect(self) -> float:
        """Returns the crossing effect for this wire deformer."""
    @staticmethod
    def deallocateAllFlags(pluginName: str) -> MStatus:
        """Deallocates all of the node flags which are currently allocated to the specified plugin."""
    @staticmethod
    def deallocateFlag(pluginName: str, flag: int) -> MStatus:
        """Deallocates a node flag which was previously allocated by a call to allocateFlag ."""
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
    @staticmethod
    def enableDGTiming(enable: bool) -> None:
        """Globally enables or disables the DG node timing mechanism."""
    def envelope(self) -> float:
        """Returns the envelope for this deformer."""
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
    def getAffectedAttributes(self, attr: MObject, affectedAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that are affected by the attribute passed in."""
    def getAffectedByAttributes(self, attr: MObject, affectedByAttributes: MObjectArray) -> MStatus:
        """Returns an array of attributes that affect the attribute passed in, attr ."""
    def getAffectedGeometry(self, objects: MObjectArray) -> MStatus:
        """The geometry affected by this deformer is packed into the provided list of MObjects."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute al"""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns a list of all attribute aliases for this node."""
    def getConnections(self, array: MPlugArray) -> MStatus:
        """Get all of the current connections to this node as an array of plugs."""
    def getDropoffLocator(self, wireIndex: int, locatorIndex: int, param: float, percentage: float) -> MStatus:
        """Gets the parameters of a drop off locator."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> MStatus:
        """Returns the external content (files) that this node depends on."""
    def hasAttribute(self, name: str) -> bool:
        """Returns true if the node already has an attribute with the given name."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    def hasUniqueName(self) -> bool:
        """Indicates whether or not this node's name is unique within the scene."""
    def holdingShape(self, wireIndex: int) -> MObject:
        """Returns the holding shape for the given wire."""
    def icon(self) -> str:
        """Returns the custom icon filename associated with the node."""
    def isDefaultNode(self) -> bool:
        """Returns true if the node is a default node."""
    def isFlagSet(self, flag: int) -> bool:
        """Retrieves the current state of the specified flag for a node."""
    def isFromReferencedFile(self) -> bool:
        """Indicates whether or not this node came from a referenced file."""
    def isLocked(self) -> bool:
        """Indicates whether or not this node is locked."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Indicates whether or not the specified attribute was added to this node within the current scene."""
    def isShared(self) -> bool:
        """Indicates whether or not this node is shared."""
    def isTrackingEdits(self) -> bool:
        """Returns whether or not edits on the given node are being tracked by the generalized edit system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def localIntensity(self) -> float:
        """Returns the local intensity for this wire deformer."""
    def name(self) -> str:
        """Returns the name of this node."""
    def numDropoffLocators(self, wireIndex: int) -> int:
        """Returns the number of drop off locators."""
    def numWires(self) -> int:
        """returns the number of wire curves connected to this deformer."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    def parentNamespace(self) -> str:
        """Returns the name of the namespace in which this node resides."""
    def pluginName(self) -> str:
        """Returns the name of the plug-in this MFnDependendencyNode was defined in."""
    def plugsAlias(self, plug: MPlug) -> str:
        """Returns the alias for the plug's attribute or the empty string if that attribute has no alias."""
    @overload
    def removeAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def removeAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Remove a dynamic attribute from a node."""
    def removeGeometry(self, object: MObject) -> MStatus:
        """Removes a piece of geometry from the deformation."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Some nodes, such as the various animCurve nodes, require that their attributes be set in a specific order for proper ope"""
    def rotation(self) -> float:
        """Returns the rotation value for this deformer."""
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setCrossingEffect(self, crossingEffect: float) -> MStatus:
        """Sets the crossing effect for this wire deformer."""
    def setDoNotWrite(self, flag: bool) -> MStatus:
        """Use this method to mark the "do not write" state of this node."""
    def setDropoffLocator(self, wireIndex: int, locatorIndex: int, param: float, percentage: float) -> MStatus:
        """Sets the parameters of a drop off locator."""
    def setEnvelope(self, envelope: float) -> MStatus:
        """Sets the envelope for this deformer."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> MStatus:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> MStatus:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> MStatus:
        """Sets the state of the specified flag for the node."""
    def setHoldingShape(self, wireIndex: int, holdingCurve: MObject) -> MStatus:
        """Sets the holding shape for the given wire."""
    def setIcon(self, filename: str) -> MStatus:
        """Associates a custom icon with the node for display in the Maya UI."""
    def setLocalIntensity(self, localIntensity: float) -> MStatus:
        """Sets the local intensity for this wire deformer."""
    def setLocked(self, locked: bool) -> MStatus:
        """Locks or unlocks this node."""
    @overload
    def setName(self, name: str, createNamespace: bool = False) -> str: ...
    @overload
    def setName(self, name: str) -> str:
        """Sets the name of this node."""
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches the Function Set to the specified Maya Object."""
    def setRotation(self, rotation: float) -> MStatus:
        """Sets the rotation value for this deformer."""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def setWireDropOffDistance(self, wireIndex: int, dropOff: float) -> MStatus:
        """Sets the drop off distance of the wire at the given index."""
    def setWireScale(self, wireIndex: int, scale: float) -> MStatus:
        """Sets the radial scale value of the wire at the given index."""
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
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""
    def wire(self, wireIndex: int) -> MObject:
        """Return the wire at the given index."""
    def wireDropOffDistance(self, wireIndex: int) -> float:
        """Return the drop off distance of the wire at the given index."""
    def wireScale(self, wireIndex: int) -> float:
        """Return the radial scale of the wire at the given index."""

class MIkHandleGroup:
    thisown: Any
    def __init__(self) -> None:
        """Default constructor."""
    def checkEffectorAtGoal(self) -> bool:
        """Determines whether the end-effector at the handle(goal) location."""
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def dofCount(self) -> int:
        """Return the total number of degrees of freedom of this handle group."""
    def handle(self, ith: int) -> MObject:
        """Return the ith handle in the handle list for this group."""
    def handleCount(self) -> int:
        """Return the number of handles in the handle list for this group."""
    def priority(self) -> int:
        """Return the priority value of this handle group."""
    def setPriority(self, arg: Any) -> MStatus:
        """Set the priority of this handle group."""
    def setSolverID(self, arg: Any) -> MStatus:
        """Set the solver id for this handle group."""
    def solve(self) -> MStatus:
        """Do all ik solving steps for this group."""
    def solverID(self) -> int:
        """Return the solver id used by this handle group."""
    def solverPriority(self) -> int:
        """return the priority of the solver used by this handle group."""

class MIkSystem:
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def findSolver(name: str) -> MObject:
        """Returns the ik solver with the given name."""
    @staticmethod
    def getSolvers(names: Any) -> MStatus:
        """Get a list of the names for the solvers that are available in the system."""
    @staticmethod
    def isGlobalSnap() -> bool:
        """Determines whether global snapping is on."""
    @staticmethod
    def isGlobalSolve() -> bool:
        """Determines whether global solving is on."""
    @staticmethod
    def setGlobalSnap(isSnap: bool) -> MStatus:
        """Turns global snapping on or off."""
    @staticmethod
    def setGlobalSolve(isSnap: bool) -> MStatus:
        """Turns global solving on or off."""

class MItKeyframe:
    kTangentAuto: Any
    kTangentAutoCustom: Any
    kTangentAutoEase: Any
    kTangentAutoMix: Any
    kTangentClamped: Any
    kTangentFast: Any
    kTangentFixed: Any
    kTangentFlat: Any
    kTangentGlobal: Any
    kTangentLinear: Any
    kTangentPlateau: Any
    kTangentSlow: Any
    kTangentSmooth: Any
    kTangentStep: Any
    kTangentStepNext: Any
    thisown: Any
    def __init__(self, animCurveNode: MObject) -> None:
        """Class Constructor."""
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def getTangentIn(self, x: Any, y: Any) -> MStatus:
        """Determines the x,y value of the tangent to the curve entering the current keyframe."""
    def getTangentOut(self, x: Any, y: Any) -> MStatus:
        """Determines the x,y value of the tangent to the curve leaving the current keyframe."""
    def inTangentType(self) -> Any:
        """Determines the type of the tangent to the curve entering the current keyframe."""
    def isDone(self) -> bool:
        """Indicates that the iterator has moved beyond the last keyframe on the Anim Curve Node to which the iterator is attached."""
    def next(self) -> MStatus:
        """Moves to the next keyframe on the Anim Curve Node to which the iterator is attached."""
    def outTangentType(self) -> Any:
        """Determines the type of the tangent to the curve leaving the current keyframe."""
    @overload
    def reset(self, animCurveNode: MObject) -> MStatus: ...
    @overload
    def reset(self) -> MStatus:
        """Detaches the iterator from the current Anim Curve Node and attaches it to the given Node."""
    def setInTangentType(self, arg: Any) -> MStatus:
        """Sets the type of the tangent to the curve entering the current keyframe."""
    def setOutTangentType(self, arg: Any) -> MStatus:
        """Sets the type of the tangent to the curve entering the current keyframe."""
    def setTangentsLocked(self, locked: bool) -> MStatus:
        """Lock or unlock the tangents at this keyframe."""
    def setTime(self, time: MTime) -> MStatus:
        """Sets the time of the current keyframe."""
    def setValue(self, value: float) -> MStatus:
        """Sets the value of the current keyframe."""
    def tangentsLocked(self) -> bool:
        """Determines whether the tangents are locked at this keyframe."""
    def time(self) -> MTime:
        """Determines the time of the current keyframe."""
    def value(self) -> float:
        """Determines the value of the current keyframe."""

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
