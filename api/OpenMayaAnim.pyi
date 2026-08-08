# Stub for maya.api.OpenMayaAnim - generated from Maya 2024 Python API reference

from typing import Any

from maya.api.OpenMaya import MAngle
from maya.api.OpenMaya import MDagPath
from maya.api.OpenMaya import MDagPathArray
from maya.api.OpenMaya import MDoubleArray
from maya.api.OpenMaya import MExternalContentInfoTable
from maya.api.OpenMaya import MExternalContentLocationTable
from maya.api.OpenMaya import MFloatArray
from maya.api.OpenMaya import MIntArray
from maya.api.OpenMaya import MMatrix
from maya.api.OpenMaya import MObject
from maya.api.OpenMaya import MObjectArray
from maya.api.OpenMaya import MPlug
from maya.api.OpenMaya import MPlugArray
from maya.api.OpenMaya import MPoint
from maya.api.OpenMaya import MPxNode
from maya.api.OpenMaya import MQuaternion
from maya.api.OpenMaya import MSelectionList
from maya.api.OpenMaya import MTime
from maya.api.OpenMaya import MTransformationMatrix
from maya.api.OpenMaya import MUuid
from maya.api.OpenMaya import MVector

class MAnimControl:
    kPlaybackLoop: Any
    kPlaybackOnce: Any
    kPlaybackOscillate: Any
    kPlaybackViewActive: Any
    kPlaybackViewAll: Any
    def __init__(self) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
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
        """Return a value indicating whether Maya is currently playing the animation"""
    @staticmethod
    def isScrubbing() -> bool:
        """Return a value indicating whether interactive scrubbing is occuring while Maya is not currently playing an animation."""
    @staticmethod
    def maxTime() -> MTime:
        """Return an MTime specifying the last frame of the current playback time range."""
    @staticmethod
    def minTime() -> MTime:
        """Return an MTime specifying the first frame of the current playback time range."""
    @staticmethod
    def playBackward() -> None:
        """Start playing the current animation backwards."""
    @staticmethod
    def playForward() -> None:
        """Start playing the current animation forwards."""
    @staticmethod
    def playbackBy() -> float:
        """Return a float specifying the increment between times viewed during the playing of the animation."""
    @staticmethod
    def playbackMode() -> int:
        """Return the playback mode currently in effect:"""
    @staticmethod
    def playbackSpeed() -> float:
        """Return the speed with with to play the animation."""
    @staticmethod
    def setAnimationEndTime(MTime: MTime) -> None:
        """Set the value of the last frame in the animation."""
    @staticmethod
    def setAnimationStartEndTime(MTime: MTime, MTime_: MTime) -> None:
        """Set the values of the first and last frames in the animation."""
    @staticmethod
    def setAnimationStartTime(MTime: MTime) -> None:
        """Set the value of the first frame in the animation."""
    @staticmethod
    def setAutoKeyMode(bool: bool) -> None:
        """Set the autoKeyMode."""
    @staticmethod
    def setCurrentTime(newTime: MTime) -> None:
        """setMinTime(MTime) -> None"""
    @staticmethod
    def setGlobalInTangentType(int: int) -> None:
        """Set the current global in tangent type"""
    @staticmethod
    def setGlobalOutTangentType(int: int) -> None:
        """Set the current global out tangent type."""
    @staticmethod
    def setMaxTime(MTime: MTime) -> None:
        """Set the value of the last frame of the current playback time range."""
    @staticmethod
    def setMinMaxTime(MTime: MTime, MTime_: MTime) -> None:
        """Set the values of the first and last frames of the playback time range."""
    @staticmethod
    def setMinTime(MTime: MTime) -> None:
        """Set the value of the first frame of the current playback time range."""
    @staticmethod
    def setPlaybackBy(float: float) -> None:
        """Specify the increment between times viewed during the playing of the animation."""
    @staticmethod
    def setPlaybackMode(int: Any) -> None:
        """Set the current playback mode."""
    @staticmethod
    def setPlaybackSpeed(float: float) -> None:
        """Set the desired speed factor at which the animation will play back."""
    @staticmethod
    def setViewMode(int: Any) -> None:
        """Set the current viewing mode."""
    @staticmethod
    def setWeightedTangents(bool: bool) -> None:
        """Sets whether or not the tangents on the Anim Curve are weighted."""
    @staticmethod
    def stop() -> None:
        """Stop playing the current animation."""
    @staticmethod
    def viewMode() -> int:
        """Return the viewing mode currently in effect:"""
    @staticmethod
    def weightedTangents() -> bool:
        """Determine whether or not the tangents on the Anim Curve are weighted."""

class MAnimCurveChange:
    def __init__(self) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def redoIt(self) -> None:
        """Redo all of the Anim Curve changes in this cache."""
    def undoIt(self) -> None:
        """Undo all of the Anim Curve changes in this cache."""

class MAnimCurveClipboard:
    endTime: Any
    endUnitlessInput: Any
    isEmpty: Any
    startTime: Any
    startUnitlessInput: Any
    theAPIClipboard: Any
    def __init__(self) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def clear(self) -> MAnimCurveClipboard:
        """Clears the clipboard."""
    def clipboardItems(self) -> MAnimCurveClipboardItemArray:
        """Returns the clipboard items."""
    def set(self, clipboard: MAnimCurveClipboard | MAnimCurveClipboardItemArray) -> MAnimCurveClipboard:
        """set( items ) -> self"""

class MAnimCurveClipboardItem:
    animCurve: Any
    fullAttributeName: Any
    leafAttributeName: Any
    nodeName: Any
    def __init__(self, r: MAnimCurveClipboardItem | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def animCurveType(self) -> Any:
        """Returns the type of the item's anim curve."""
    def getAddressingInfo(self, arg: Any, arg_: Any, arg__: Any) -> Any:
        """Returns the addressing information for this clipboard item"""
    def setAddressingInfo(self, rowCount: int, childCount: int, attributeCount: int) -> MAnimCurveClipboardItem:
        """Sets the addressing information for this clipboard item."""
    def setAnimCurve(self, object: MObject) -> MAnimCurveClipboardItem:
        """Sets the anim curve MObject."""
    def setNameInfo(self, nodeName: Any, fullName: Any, leafName: Any) -> MAnimCurveClipboardItem:
        """Sets the name information for this clipboard item."""

class MAnimCurveClipboardItemArray:
    sizeIncrement: Any
    def __init__(self, other: MAnimCurveClipboardItemArray | int | None = None, initialValue: MAnimCurveClipboardItem | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def append(self, element: MAnimCurveClipboardItem) -> None:
        """Add a value to the end of the array."""
    def clear(self) -> None:
        """Remove all elements from the array."""
    def copy(self, source: MAnimCurveClipboardItemArray) -> None:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self, element: MAnimCurveClipboardItem, index: int) -> None:
        """Insert a new value into the array at the given index."""
    def remove(self, index: int) -> None:
        """Remove an element from the array."""
    def setLength(self, length: int) -> None:
        """Grow or shrink the array to contain a specific number of elements."""

class MAnimMessage:
    kDefaultAction: Any
    kDoAction: Any
    kDoNotDoAction: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def addAnimCurveEditedCallback(function: int, clientData: None = None) -> int:
        """This method registers a callback that is called whenever an"""
    @staticmethod
    def addAnimKeyframeEditCheckCallback(function: int, clientData: None = None) -> int:
        """This method registers a callback that is used by the setKeyframe command"""
    @staticmethod
    def addAnimKeyframeEditedCallback(function: int | MObject, clientData: None | int = None) -> int:
        """This method registers a callback that is called whenever an"""
    @staticmethod
    def addDisableImplicitControlCallback(function: int, clientData: None = None) -> int:
        """This method registers a callback that is called from bakeResults"""
    @staticmethod
    def addNodeAnimKeyframeEditedCallback(animNode: MObject, function: int, clientData: None = None) -> int:
        """This method registers a callback that is called whenever an a"""
    @staticmethod
    def addPostBakeResultsCallback(function: int, clientData: None = None) -> int:
        """This method registers a callback that is called from bakeResults"""
    @staticmethod
    def addPreBakeResultsCallback(function: int, clientData: None = None) -> int:
        """This method registers a callback that is called from bakeResults"""
    @staticmethod
    def currentCallbackId() -> int:
        """Returns the callback ID of the currently executing callback. If called"""
    @staticmethod
    def flushAnimKeyframeEditedCallbacks() -> None:
        """Animation keyframe edited callbacks are queued to only be issued on an"""
    @staticmethod
    def nodeCallbacks(node: Any) -> int:
        """Returns a list of callback IDs registered to a given node."""
    @staticmethod
    def removeCallback(id: Any) -> None:
        """Removes the specified callback from Maya."""
    @staticmethod
    def removeCallbacks(ids: Any) -> None:
        """Removes all of the specified callbacks from Maya."""

class MAnimUtil:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def findAnimatablePlugs(MSelectionList: MSelectionList) -> MPlugArray:
        """Find the list of attributes (MPlugs) on any member of an MSelectionList"""
    @staticmethod
    def findAnimatedPlugs(MObject: MObject | MDagPath | MSelectionList, bool: MPlugArray) -> MPlugArray:
        """findAnimatedPlugs(MDagPath, bool) -> MPlugArray"""
    @staticmethod
    def findAnimation(MPlug: MPlug) -> MObjectArray:
        """Find the animCurve(s) that are animating a given attribute (MPlug)."""
    @staticmethod
    def findConstraint(arg: MPlug, MObjectArray: MObject) -> Any:
        """Find any constraint that is directly driving the specified attribute."""
    @staticmethod
    def findSetDrivenKeyAnimation(arg: MPlug, MPlugArray: MObjectArray) -> Any:
        """Find any driven keyframe animCurves, the blendWeighted node and the"""
    @staticmethod
    def isAnimated(MObject: MObject | MDagPath | MPlug | MSelectionList, bool: bool) -> bool:
        """isAnimated(MDagPath, bool) -> bool"""

class MFnAnimCurve:
    animCurveType: Any
    isDefaultNode: Any
    isFromReferencedFile: Any
    isLocked: Any
    isShared: Any
    isStatic: Any
    isTimeInput: Any
    isUnitlessInput: Any
    isWeighted: Any
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
    namespace: Any
    numKeys: Any
    pluginName: Any
    postInfinityType: Any
    preInfinityType: Any
    typeId: Any
    typeName: Any
    def __init__(self, object: MObject | MPlug | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def absoluteName(self) -> Any:
        """Returns the absolute name of this node.  The absolute name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself.  Regardless of relative name mode, absoluteName() will always return a full namespace path prefixed with a leading colon (the root namespace).  If the underlying node is a DAG node, then absoluteName() does not guarantee uniqueness, that is, two dependency nodes could have the same absoluteName().  In cases like this the uniqueName() method will guarantee that the name uniquely identifies the node."""
    def addAttribute(self, attr: MObject, type: Any) -> None:
        """Adds a new dynamic attribute to the node."""
    def addExternalContentForFileAttr(self, attr: MObject) -> MExternalContentInfoTable:
        """Adds content info to the specified table from a file path attribute."""
    def addKey(self, at: MTime | float, value: float | MTime, tangentInType: Any, tangentOutType: Any, change: MAnimCurveChange | None = None) -> int:
        """Adds a new key with the given value at the specified time."""
    def addKeys(self, times: Any, values: Any, tangentInType: bool, tangentOutType: Any, keepExistingKeys: bool = False, change: Any = None) -> MFnAnimCurve:
        """Add a set of new keys with the given corresponding values and tangent typesat the specified times.  This method only works for animCurves of typekAnimCurveTA, kAnimCurveTL and kAnimCurveTU."""
    def addKeysWithTangents(self, times: Any, values: Any, tangentInType: bool, tangentOutType: bool, tangentInTypeArray: Any = None, tangentOutTypeArray: Any = None, tangentInXArray: Any = None, tangentInYArray: Any = None, tangentOutXArray: Any = None, tangentOutYArray: Any = None, tangentsLockedArray: Any = None, weightsLockedArray: Any = None, convertUnits: bool = True, keepExistingKeys: bool = False, change: Any = None) -> MFnAnimCurve:
        """Add a set of new keys with the given corresponding values, tangent types and tangents at the specified times.  This method only works for animCurves of typekAnimCurveTA, kAnimCurveTL and kAnimCurveTU."""
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
    def canBeWritten(self) -> bool:
        """Returns true if the node will be written to file."""
    @staticmethod
    def classification(nodeTypeName: Any) -> Any:
        """Returns the classification string for the named node type."""
    def create(self, node: Any, attribute: Any, animCurveType: Any) -> MObject:
        """create(plug, animCurveType=kAnimCurveUnknown [, modifier] ) -> MObject"""
    @staticmethod
    def deallocateAllFlags(pluginName: Any) -> None:
        """Deallocates all node flags which are currently allocated to the named plugin."""
    @staticmethod
    def deallocateFlag(pluginName: Any, flag: int) -> None:
        """Deallocates the specified node flag, which was previously allocated by the named plugin using allocateFlag()."""
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
    def evaluate(self, at: MTime | float) -> Any:
        """Evalutes the curve."""
    def find(self, at: MTime | float) -> int:
        """Determines the index of the key which is set at the specifiedMTime (time-input curves) or double (unitless-input curves)."""
    def findAlias(self, alias: Any, attrObj: MObject) -> bool:
        """Returns the attribute which has the given alias."""
    def findClosest(self, at: MTime | float) -> int:
        """Determines the index of the key which is set at theMTime (time-input curves) or double (unitless-input curves)closest to the specified time."""
    def findPlug(self, attr: Any, wantNetworkedPlug: bool) -> MPlug:
        """Returns a plug for the given attribute."""
    def getAffectedAttributes(self, attr: MObject) -> MObjectArray:
        """Returns all of the attributes which are affected by the specified attribute."""
    def getAffectingAttributes(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all of the attributes which affect the specified attribute."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute aliases."""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns all of the node's attribute aliases."""
    def getConnections(self) -> MPlugArray:
        """Returns all the plugs which are connected to attributes of this node."""
    def getExternalContent(self) -> MExternalContentInfoTable:
        """Gets the external content (files) that this node depends on."""
    def getTangentAngleWeight(self, index: Any, arg: Any, double: Any) -> Any:
        """Determines the angle and weight of the in- or out-tangent to the curvefor the key at the specified index"""
    def getTangentXY(self, index: Any, arg: Any, y: Any) -> Any:
        """Determines the x,y value representing the vector of the in- orout-tangent (depending on the value of the isInTangent parameter) tothe curve for the key at the specified index.  The values returnedwill be in Maya's internal units (seconds for time, centimeters forlinear, radians for angles)."""
    def hasAttribute(self, name: Any) -> bool:
        """Returns True if the node has an attribute with the given name."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def hasUniqueName(self) -> bool:
        """Returns True if the node's name is unique."""
    def inTangentType(self, index: int) -> Any:
        """Determines the type of the tangent to the curve entering the current key."""
    def input(self, index: Any) -> Any:
        """Determines the input (MTime for T* curves or double for U* curves) of the key at the specified index."""
    def insertKey(self, time: MTime, breakdown: bool | None = None, change: MAnimCurveChange | None = None) -> int:
        """addKey(time, breakdown=False, change=None) -> unsigned int"""
    def isBreakdown(self, index: int) -> bool:
        """Determines whether or not a key is a breakdown."""
    def isFlagSet(self, flag: int) -> bool:
        """Returns the state of the specified node flag."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files."""
    def isTrackingEdits(self) -> bool:
        """Returns True if the node is referenced or in an assembly that is tracking edits."""
    def name(self) -> Any:
        """Returns the node's name."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def outTangentType(self, index: int) -> Any:
        """Determines the type of the tangent to the curve leaving the current key."""
    def plugsAlias(self, plug: MPlug) -> Any:
        """Returns the alias for a plug's attribute."""
    def quaternionW(self, index: int) -> float:
        """Returns the quaternionW of the key at the specified index.  This methodshould only be used on Anim Curves of type kAnimCurveTA."""
    def remove(self, index: int, change: Any = None) -> MFnAnimCurve:
        """Removes the key at the specified index."""
    def removeAttribute(self, attr: MObject, type: Any) -> None:
        """Removes a dynamic attribute from the node."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Returns one of the node's attribute, based on the order in which they are written to file."""
    def setAffectsAnimation(self) -> None:
        """Specifies that modifications to a node could potentially affect the animation."""
    def setAlias(self, alias: Any, name: Any, plug: MPlug, add: bool | None = None) -> bool:
        """Adds or removes an attribute alias."""
    def setAngle(self, index: int, setAngle: MAngle, isInTangent: bool, change: Any = None) -> MFnAnimCurve:
        """Sets the in- or out-angle of the tangent for the key at the given index."""
    def setDoNotWrite(self, flag: bool) -> None:
        """Used to prevent the node from being written to file."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> None:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> None:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> None:
        """Sets the state of the specified node flag."""
    def setInTangentType(self, index: int, tangentType: Any, change: Any = None) -> MFnAnimCurve:
        """Sets the type of the tangent to the curve entering the key at thespecified index."""
    def setInput(self, index: Any, at: Any, change: Any = None) -> MFnAnimCurve:
        """Sets the input (MTime for T* curves or double for U* curves) of the key at the specified index.  This will fail ifsetting the input would require re-ordering of the keys."""
    def setIsBreakdown(self, index: int, isBreakdown: bool, change: Any = None) -> MFnAnimCurve:
        """Sets the breakdown state of a key at a given index."""
    def setIsWeighted(self, isWeighted: bool, change: Any = None) -> MFnAnimCurve:
        """Sets whether or not the curve has weighted tangents."""
    def setName(self, name: Any, createNamespace: bool | None = None) -> Any:
        """Sets the node's name."""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def setOutTangentType(self, index: int, tangentType: Any, change: Any = None) -> MFnAnimCurve:
        """Sets the type of the tangent to the curve leaving the key at thespecified index."""
    def setPostInfinityType(self, infinityType: Any, change: Any = None) -> MFnAnimCurve:
        """Sets the behaviour of the curve for the range occurring after the last key."""
    def setPreInfinityType(self, infinityType: Any, change: Any = None) -> MFnAnimCurve:
        """Sets the behaviour of the curve for the range occurring before the first key."""
    def setQuaternionW(self, index: int, quaternionW: float, change: Any = None) -> MFnAnimCurve:
        """Sets the quaternionW of the key at the specified index.  This methodshould only be used on Anim Curves of type kAnimCurve*A."""
    def setTangent(self, index: int, xOrAngle: Any, yOrWeight: Any, isInTangent: bool, change: bool | None = None, convertUnits: bool = True) -> MFnAnimCurve:
        """Sets the tangent for the key at the specified index."""
    def setTangentTypes(self, indexArray: MIntArray, tangentInType: Any, tangentOutType: Any, change: Any = None) -> MFnAnimCurve:
        """Sets the tangent types for multiple keys."""
    def setTangentsLocked(self, index: int, locked: bool, change: Any = None) -> MFnAnimCurve:
        """Lock or unlock the tangents at the given key."""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def setValue(self, index: int, value: float, change: Any = None) -> MFnAnimCurve:
        """Sets the value of the key at the specified index.  This methodshould only be used on Anim Curves of type kAnimCurve*A, kAnimCurve*Lor kAnimCurve*U."""
    def setWeight(self, index: int, weight: float, isInTangent: bool, change: Any = None) -> MFnAnimCurve:
        """Sets the in- or out-weight of the tangent for the key at the given index."""
    def setWeightsLocked(self, index: int, locked: bool, change: Any = None) -> MFnAnimCurve:
        """Lock or unlock the weights at the given key."""
    def tangentsLocked(self, index: int) -> bool:
        """Determines whether the tangents are locked at the given key."""
    def timedAnimCurveTypeForPlug(self, plug: MPlug) -> Any:
        """Returns the timed animCurve type appropriate for the specified plug."""
    def type(self) -> int:
        """Returns the type of the function set."""
    def uniqueName(self) -> Any:
        """For a DAG node, the unique name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself. For a non-DAG node, the uniqueName is just its name."""
    def unitlessAnimCurveTypeForPlug(self, plug: MPlug) -> Any:
        """Returns the unitless animCurve type appropriate for the specified plug."""
    def userNode(self) -> MPxNode:
        """Returns the MPxNode object for a plugin node."""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""
    def value(self, index: int) -> float:
        """Determines the value of the key at the specified index.  This methodshould only be used on Anim Curves of type kAnimCurve*A, kAnimCurve*Lor kAnimCurve*U."""
    def weightsLocked(self, index: int) -> bool:
        """Determines whether the weights are locked at the given key."""

class MFnGeometryFilter:
    deformerSet: Any
    envelope: Any
    isDefaultNode: Any
    isFromReferencedFile: Any
    isLocked: Any
    isShared: Any
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
    namespace: Any
    pluginName: Any
    typeId: Any
    typeName: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def absoluteName(self) -> Any:
        """Returns the absolute name of this node.  The absolute name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself.  Regardless of relative name mode, absoluteName() will always return a full namespace path prefixed with a leading colon (the root namespace).  If the underlying node is a DAG node, then absoluteName() does not guarantee uniqueness, that is, two dependency nodes could have the same absoluteName().  In cases like this the uniqueName() method will guarantee that the name uniquely identifies the node."""
    def addAttribute(self, attr: MObject, type: Any) -> None:
        """Adds a new dynamic attribute to the node."""
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
    def canBeWritten(self) -> bool:
        """Returns true if the node will be written to file."""
    @staticmethod
    def classification(nodeTypeName: Any) -> Any:
        """Returns the classification string for the named node type."""
    def create(self, typeId: Any, name: Any) -> MObject:
        """Creates a new node of the given type."""
    @staticmethod
    def deallocateAllFlags(pluginName: Any) -> None:
        """Deallocates all node flags which are currently allocated to the named plugin."""
    @staticmethod
    def deallocateFlag(pluginName: Any, flag: int) -> None:
        """Deallocates the specified node flag, which was previously allocated by the named plugin using allocateFlag()."""
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
    def findAlias(self, alias: Any, attrObj: MObject) -> bool:
        """Returns the attribute which has the given alias."""
    def findPlug(self, attr: Any, wantNetworkedPlug: bool) -> MPlug:
        """Returns a plug for the given attribute."""
    def getAffectedAttributes(self, attr: MObject) -> MObjectArray:
        """Returns all of the attributes which are affected by the specified attribute."""
    def getAffectingAttributes(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all of the attributes which affect the specified attribute."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute aliases."""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns all of the node's attribute aliases."""
    def getComponentAtIndex(self, index: int) -> MObject:
        """Returns the component which contains the members of the deformer"""
    def getConnections(self) -> MPlugArray:
        """Returns all the plugs which are connected to attributes of this node."""
    def getExternalContent(self) -> MExternalContentInfoTable:
        """Gets the external content (files) that this node depends on."""
    def getInputGeometry(self) -> MObjectArray:
        """Returns the DAG nodes which provide input geometry to the deformer."""
    def getOutputGeometry(self) -> MObjectArray:
        """Returns the DAG nodes which receive output geometry from the deformer."""
    def getPathAtIndex(self, plugIndex: int) -> MDagPath:
        """Returns the DAG path of the specified output geometry."""
    def groupIdAtIndex(self, plugIndex: int) -> int:
        """Returns the groupId associated with the specified geometry."""
    def hasAttribute(self, name: Any) -> bool:
        """Returns True if the node has an attribute with the given name."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def hasUniqueName(self) -> bool:
        """Returns True if the node's name is unique."""
    def indexForGroupId(self, groupId: int) -> int:
        """Returns the plug index of the geometry associated with the specified groupId."""
    def indexForOutputConnection(self, connIndex: int) -> int:
        """Returns the plug index corresponding to a connection index. The"""
    def indexForOutputShape(self, shape: MObject) -> int:
        """Returns the plug index for the specified output shape."""
    def inputShapeAtIndex(self, plugIndex: int) -> MObject:
        """Returns the input shape corresponding to the plug index."""
    def isFlagSet(self, flag: int) -> bool:
        """Returns the state of the specified node flag."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files."""
    def isTrackingEdits(self) -> bool:
        """Returns True if the node is referenced or in an assembly that is tracking edits."""
    def name(self) -> Any:
        """Returns the node's name."""
    def numOutputConnections(self) -> int:
        """Returns the number of output geometries connected to this node. This"""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def outputShapeAtIndex(self, index: int) -> MObject:
        """Returns the DAG path to which this function set is attached, or the first path to the node if the function set is attached to an MObject."""
    def plugsAlias(self, plug: MPlug) -> Any:
        """Returns the alias for a plug's attribute."""
    def removeAttribute(self, attr: MObject, type: Any) -> None:
        """Removes a dynamic attribute from the node."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Returns one of the node's attribute, based on the order in which they are written to file."""
    def setAffectsAnimation(self) -> None:
        """Specifies that modifications to a node could potentially affect the animation."""
    def setAlias(self, alias: Any, name: Any, plug: MPlug, add: bool | None = None) -> bool:
        """Adds or removes an attribute alias."""
    def setDoNotWrite(self, flag: bool) -> None:
        """Used to prevent the node from being written to file."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> None:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> None:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> None:
        """Sets the state of the specified node flag."""
    def setName(self, name: Any, createNamespace: bool | None = None) -> Any:
        """Sets the node's name."""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def type(self) -> int:
        """Returns the type of the function set."""
    def uniqueName(self) -> Any:
        """For a DAG node, the unique name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself. For a non-DAG node, the uniqueName is just its name."""
    def userNode(self) -> MPxNode:
        """Returns the MPxNode object for a plugin node."""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnIkJoint:
    boundingBox: Any
    inModel: Any
    inUnderWorld: Any
    isDefaultNode: Any
    isFromReferencedFile: Any
    isInstanceable: Any
    isIntermediateObject: Any
    isLocked: Any
    isShared: Any
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
    def addChild(self, node: int, index: bool, keepExistingParents: bool = False) -> MFnIkJoint:
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
    def create(self, parent: Any = None) -> Any:
        """Create a new joint in a skeleton.  In maya, skeletons are defined"""
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
    def degreesOfFreedom(self, *args: Any, **kwargs: Any) -> Any:
        """Gets degrees of freedom for this joint, that is, which axes are free"""
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
    def hikJointName(self) -> Any:
        """Get the name that HIK uses to identify this joint"""
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
    def maxRotateDampXRange(self) -> float:
        """Get the maximum of the damping range in X. This corresponds to the"""
    def maxRotateDampXStrength(self) -> float:
        """Get the maximum of the damping strength in X. This corresponds to the"""
    def maxRotateDampYRange(self) -> float:
        """Get the maximum of the damping range in Y. This corresponds to the"""
    def maxRotateDampYStrength(self) -> float:
        """Get the maximum of the damping strength in Y. This corresponds to the"""
    def maxRotateDampZRange(self) -> float:
        """Get the maximum of the damping range in Z. This corresponds to the"""
    def maxRotateDampZStrength(self) -> float:
        """Get the maximum of the damping strength in Z. This corresponds to the"""
    def minRotateDampXRange(self) -> float:
        """Get the minimum of the damping range in X. This corresponds to the"""
    def minRotateDampXStrength(self) -> float:
        """Get the minimum of the damping strength in X. This corresponds to the"""
    def minRotateDampYRange(self) -> float:
        """Get the minimum of the damping range in Y. This corresponds to the"""
    def minRotateDampYStrength(self) -> float:
        """Get the minimum of the damping strength in Y. This corresponds to the"""
    def minRotateDampZRange(self) -> float:
        """Get the minimum of the damping range in Z. This corresponds to the"""
    def minRotateDampZStrength(self) -> float:
        """Get the minimum of the damping strength in Z. This corresponds to the"""
    def name(self) -> Any:
        """Returns the node's name."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def orientation(self, *args: Any, **kwargs: Any) -> Any:
        """Gets the joint orientation as either an Euler rotation or a """
    def orientationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Get the joint orientation"""
    def parent(self, index: int) -> MObject:
        """Returns the specified parent of this node."""
    def parentCount(self) -> int:
        """Returns the number of parents this node has."""
    def partialPathName(self) -> Any:
        """Returns the minimum path string necessary to uniquely identify the attached object."""
    def plugsAlias(self, plug: MPlug) -> Any:
        """Returns the alias for a plug's attribute."""
    def preferredAngle(self, *args: Any, **kwargs: Any) -> Any:
        """Get the preferred orientation angle for the joint."""
    def removeAttribute(self, attr: MObject, type: Any) -> None:
        """Removes a dynamic attribute from the node."""
    def removeChild(self, node: Any) -> MFnIkJoint:
        """Removes the child, specified by MObject, reparenting it under the world."""
    def removeChildAt(self, index: int) -> MFnIkJoint:
        """Removes the child, specified by index, reparenting it under the world."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Returns one of the node's attribute, based on the order in which they are written to file."""
    def resetFromRestPosition(self) -> None:
        """Resets the transform from its rest position matrix."""
    def resetTransformation(self, m: MMatrix) -> None:
        """Resets the transform's attribute values to represent the given transformation matrix in world space."""
    def restPosition(self) -> MTransformationMatrix:
        """Returns the transform's rest position matrix."""
    def rotateBy(self, quaternion: Any, Space: int | None = None) -> None:
        """Adds an MEulerRotation or MQuaternion to the transform's rotation."""
    def rotateByComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Adds to the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""
    def rotateOrientation(self, space: int) -> MQuaternion:
        """Returns the MQuaternion which orients the local rotation space."""
    def rotatePivot(self, space: int) -> MPoint:
        """Returns the transform's rotate pivot."""
    def rotatePivotTranslation(self, space: int) -> MVector:
        """Returns the transform's rotate pivot translation."""
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
    def scaleOrientation(self, *args: Any, **kwargs: Any) -> Any:
        """Gets the orientation of the coordinate axes, as either a quaternion"""
    def scalePivot(self, space: int) -> MPoint:
        """Returns the transform's scale pivot."""
    def scalePivotTranslation(self, space: int) -> MVector:
        """Returns the transform's scale pivot translation."""
    def segmentScale(self, *args: Any, **kwargs: Any) -> Any:
        """Get the local space scale values for the joint segment (bone). This is"""
    def setAffectsAnimation(self) -> None:
        """Specifies that modifications to a node could potentially affect the animation."""
    def setAlias(self, alias: Any, name: Any, plug: MPlug, add: bool | None = None) -> bool:
        """Adds or removes an attribute alias."""
    def setDegreesOfFreedom(self, freeInX: bool, freeInY: bool, freeInZ: bool) -> None:
        """Set the degrees of freedom for this joint by specifying which axes"""
    def setDoNotWrite(self, flag: bool) -> None:
        """Used to prevent the node from being written to file."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> None:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> None:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> None:
        """Sets the state of the specified node flag."""
    def setLimit(self, type: int, value: float) -> None:
        """Sets the value of the specified limit."""
    def setMaxRotateDampXRange(self, angle: float) -> None:
        """Set the maximum of the damping range in X. This corresponds to the"""
    def setMaxRotateDampXStrength(self, angle: float) -> None:
        """Set the maximum of the damping strength in X. This corresponds to the"""
    def setMaxRotateDampYRange(self, angle: float) -> None:
        """Set the maximum of the damping range in Y. This corresponds to the"""
    def setMaxRotateDampYStrength(self, angle: float) -> None:
        """Set the maximum of the damping strength in Y. This corresponds to the"""
    def setMaxRotateDampZRange(self, angle: float) -> None:
        """Set the maximum of the damping range in Z. This corresponds to the"""
    def setMaxRotateDampZStrength(self, angle: float) -> None:
        """Set the maximum of the damping strength in Z. This corresponds to the"""
    def setMinRotateDampXRange(self, angle: float) -> None:
        """Set the minimum of the damping range in X. This corresponds to the"""
    def setMinRotateDampXStrength(self, angle: float) -> None:
        """Set the minimum of the damping strength in X. This corresponds to the"""
    def setMinRotateDampYRange(self, angle: float) -> None:
        """Set the minimum of the damping range in Y. This corresponds to the"""
    def setMinRotateDampYStrength(self, angle: float) -> None:
        """Set the minimum of the damping strength in Y. This corresponds to the"""
    def setMinRotateDampZRange(self, angle: float) -> None:
        """Set the minimum of the damping range in Z. This corresponds to the"""
    def setMinRotateDampZStrength(self, angle: float) -> None:
        """Set the minimum of the damping strength in Z. This corresponds to the"""
    def setName(self, name: Any, createNamespace: bool | None = None) -> Any:
        """Sets the node's name."""
    def setObject(self, arg: MDagPath | MObject) -> MFnIkJoint:
        """Attaches the function set to the specified node or DAG path."""
    def setOrientation(self, quaternion: Any) -> None:
        """Sets the joint orientation, which can be specified as either an Euler"""
    def setPreferredAngle(self) -> None:
        """Set the preferred orientation angle for the joint."""
    def setRestPosition(self, matrix: MTransformationMatrix) -> None:
        """Sets the transform's rest position matrix."""
    def setRotateOrientation(self, quat: MQuaternion, space: int, balance: bool) -> None:
        """Sets the MQuaternion which orients the local rotation space."""
    def setRotatePivot(self, point: MPoint, space: int, balance: bool) -> None:
        """Sets the transform's rotate pivot."""
    def setRotatePivotTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's rotate pivot translation."""
    def setRotation(self, quaternion: Any, Space: int | None = None) -> None:
        """Sets the transform's rotation using an MEulerRotation or MQuaternion."""
    def setRotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""
    def setRotationOrder(self, order: int, reorder: bool) -> None:
        """Sets the transform's rotation order."""
    def setScale(self) -> None:
        """Sets the transform's scale components."""
    def setScaleOrientation(self, quaternion: MQuaternion | int) -> None:
        """Sets the orientation of the coordinate axes, which can be specified as either an Euler"""
    def setScalePivot(self, point: MPoint, space: int, balance: bool) -> None:
        """Sets the transform's scale pivot."""
    def setScalePivotTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's scale pivot translation."""
    def setSegmentScale(self) -> None:
        """Set the segment scale for the joint."""
    def setShear(self) -> None:
        """Sets the transform's shear."""
    def setStiffness(self) -> None:
        """Set the stiffness for the joint. This is equivalent to calling"""
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
    def stiffness(self, *args: Any, **kwargs: Any) -> Any:
        """Get the stiffness for the joint."""
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

class MFnSkinCluster:
    deformerSet: Any
    envelope: Any
    isDefaultNode: Any
    isFromReferencedFile: Any
    isLocked: Any
    isShared: Any
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
    namespace: Any
    pluginName: Any
    typeId: Any
    typeName: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def absoluteName(self) -> Any:
        """Returns the absolute name of this node.  The absolute name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself.  Regardless of relative name mode, absoluteName() will always return a full namespace path prefixed with a leading colon (the root namespace).  If the underlying node is a DAG node, then absoluteName() does not guarantee uniqueness, that is, two dependency nodes could have the same absoluteName().  In cases like this the uniqueName() method will guarantee that the name uniquely identifies the node."""
    def addAttribute(self, attr: MObject, type: Any) -> None:
        """Adds a new dynamic attribute to the node."""
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
    def canBeWritten(self) -> bool:
        """Returns true if the node will be written to file."""
    @staticmethod
    def classification(nodeTypeName: Any) -> Any:
        """Returns the classification string for the named node type."""
    def create(self, typeId: Any, name: Any) -> MObject:
        """Creates a new node of the given type."""
    @staticmethod
    def deallocateAllFlags(pluginName: Any) -> None:
        """Deallocates all node flags which are currently allocated to the named plugin."""
    @staticmethod
    def deallocateFlag(pluginName: Any, flag: int) -> None:
        """Deallocates the specified node flag, which was previously allocated by the named plugin using allocateFlag()."""
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
    def findAlias(self, alias: Any, attrObj: MObject) -> bool:
        """Returns the attribute which has the given alias."""
    def findPlug(self, attr: Any, wantNetworkedPlug: bool) -> MPlug:
        """Returns a plug for the given attribute."""
    def getAffectedAttributes(self, attr: MObject) -> MObjectArray:
        """Returns all of the attributes which are affected by the specified attribute."""
    def getAffectingAttributes(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all of the attributes which affect the specified attribute."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute aliases."""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns all of the node's attribute aliases."""
    def getBlendWeights(self, shape: MDagPath, components: MObject) -> MDoubleArray:
        """Returns blend weights for the specified components of the deformed"""
    def getComponentAtIndex(self, index: int) -> MObject:
        """Returns the component which contains the members of the deformer"""
    def getConnections(self) -> MPlugArray:
        """Returns all the plugs which are connected to attributes of this node."""
    def getExternalContent(self) -> MExternalContentInfoTable:
        """Gets the external content (files) that this node depends on."""
    def getInputGeometry(self) -> MObjectArray:
        """Returns the DAG nodes which provide input geometry to the deformer."""
    def getOutputGeometry(self) -> MObjectArray:
        """Returns the DAG nodes which receive output geometry from the deformer."""
    def getPathAtIndex(self, plugIndex: int) -> MDagPath:
        """Returns the DAG path of the specified output geometry."""
    def getPointsAffectedByInfluence(self, arg: MDagPath, MDoubleArray: Any) -> Any:
        """During deformation, the skinCluster algorithm is applied for a given"""
    def getWeights(self, shape: MDagPath, arg: MObject, int: int) -> Any:
        """getWeights(shape, components, influence) -> MDoubleArray"""
    def groupIdAtIndex(self, plugIndex: int) -> int:
        """Returns the groupId associated with the specified geometry."""
    def hasAttribute(self, name: Any) -> bool:
        """Returns True if the node has an attribute with the given name."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def hasUniqueName(self) -> bool:
        """Returns True if the node's name is unique."""
    def indexForGroupId(self, groupId: int) -> int:
        """Returns the plug index of the geometry associated with the specified groupId."""
    def indexForInfluenceObject(self, influenceObj: MDagPath) -> int:
        """Returns the logical index of the matrix array attribute where the"""
    def indexForOutputConnection(self, connIndex: int) -> int:
        """Returns the plug index corresponding to a connection index. The"""
    def indexForOutputShape(self, shape: MObject) -> int:
        """Returns the plug index for the specified output shape."""
    def influenceObjects(self, paths: MDagPathArray) -> MDagPathArray:
        """Returns an array of paths to the influence objects for the skinCluster."""
    def inputShapeAtIndex(self, plugIndex: int) -> MObject:
        """Returns the input shape corresponding to the plug index."""
    def isFlagSet(self, flag: int) -> bool:
        """Returns the state of the specified node flag."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files."""
    def isTrackingEdits(self) -> bool:
        """Returns True if the node is referenced or in an assembly that is tracking edits."""
    def name(self) -> Any:
        """Returns the node's name."""
    def numOutputConnections(self) -> int:
        """Returns the number of output geometries connected to this node. This"""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def outputShapeAtIndex(self, index: int) -> MObject:
        """Returns the DAG path to which this function set is attached, or the first path to the node if the function set is attached to an MObject."""
    def plugsAlias(self, plug: MPlug) -> Any:
        """Returns the alias for a plug's attribute."""
    def removeAttribute(self, attr: MObject, type: Any) -> None:
        """Removes a dynamic attribute from the node."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Returns one of the node's attribute, based on the order in which they are written to file."""
    def setAffectsAnimation(self) -> None:
        """Specifies that modifications to a node could potentially affect the animation."""
    def setAlias(self, alias: Any, name: Any, plug: MPlug, add: bool | None = None) -> bool:
        """Adds or removes an attribute alias."""
    def setBlendWeights(self, shape: MDagPath, components: MObject, weights: MDoubleArray) -> MFnSkinCluster:
        """Sets blend weights for the specified components of the shape being"""
    def setDoNotWrite(self, flag: bool) -> None:
        """Used to prevent the node from being written to file."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> None:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> None:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> None:
        """Sets the state of the specified node flag."""
    def setName(self, name: Any, createNamespace: bool | None = None) -> Any:
        """Sets the node's name."""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def setWeights(self, shape: MDagPath, components: MObject, influence: int | bool, weight: float, normalize: bool = True, returnOldWeights: bool = False) -> Any:
        """setWeights(shape, components, influences, weights, normalize=True, returnOldWeights=False) -> None or MDoubleArray"""
    def type(self) -> int:
        """Returns the type of the function set."""
    def uniqueName(self) -> Any:
        """For a DAG node, the unique name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself. For a non-DAG node, the uniqueName is just its name."""
    def userNode(self) -> MPxNode:
        """Returns the MPxNode object for a plugin node."""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnWeightGeometryFilter:
    deformerSet: Any
    envelope: Any
    isDefaultNode: Any
    isFromReferencedFile: Any
    isLocked: Any
    isShared: Any
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
    namespace: Any
    pluginName: Any
    typeId: Any
    typeName: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def absoluteName(self) -> Any:
        """Returns the absolute name of this node.  The absolute name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself.  Regardless of relative name mode, absoluteName() will always return a full namespace path prefixed with a leading colon (the root namespace).  If the underlying node is a DAG node, then absoluteName() does not guarantee uniqueness, that is, two dependency nodes could have the same absoluteName().  In cases like this the uniqueName() method will guarantee that the name uniquely identifies the node."""
    def addAttribute(self, attr: MObject, type: Any) -> None:
        """Adds a new dynamic attribute to the node."""
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
    def canBeWritten(self) -> bool:
        """Returns true if the node will be written to file."""
    @staticmethod
    def classification(nodeTypeName: Any) -> Any:
        """Returns the classification string for the named node type."""
    def create(self, typeId: Any, name: Any) -> MObject:
        """Creates a new node of the given type."""
    @staticmethod
    def deallocateAllFlags(pluginName: Any) -> None:
        """Deallocates all node flags which are currently allocated to the named plugin."""
    @staticmethod
    def deallocateFlag(pluginName: Any, flag: int) -> None:
        """Deallocates the specified node flag, which was previously allocated by the named plugin using allocateFlag()."""
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
    def findAlias(self, alias: Any, attrObj: MObject) -> bool:
        """Returns the attribute which has the given alias."""
    def findPlug(self, attr: Any, wantNetworkedPlug: bool) -> MPlug:
        """Returns a plug for the given attribute."""
    def getAffectedAttributes(self, attr: MObject) -> MObjectArray:
        """Returns all of the attributes which are affected by the specified attribute."""
    def getAffectingAttributes(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all of the attributes which affect the specified attribute."""
    def getAliasAttr(self, force: bool) -> MObject:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute aliases."""
    def getAliasList(self, strArray: Any) -> bool:
        """Returns all of the node's attribute aliases."""
    def getComponentAtIndex(self, index: int) -> MObject:
        """Returns the component which contains the members of the deformer"""
    def getConnections(self) -> MPlugArray:
        """Returns all the plugs which are connected to attributes of this node."""
    def getEnvelopeWeights(self, index: int) -> MFloatArray:
        """Returns the weights the deformer uses for the geometry at the specified plug index."""
    def getExternalContent(self) -> MExternalContentInfoTable:
        """Gets the external content (files) that this node depends on."""
    def getInputGeometry(self) -> MObjectArray:
        """Returns the DAG nodes which provide input geometry to the deformer."""
    def getOutputGeometry(self) -> MObjectArray:
        """Returns the DAG nodes which receive output geometry from the deformer."""
    def getPathAtIndex(self, plugIndex: int) -> MDagPath:
        """Returns the DAG path of the specified output geometry."""
    def getWeightPlugStrings(self, list: MSelectionList) -> Any:
        """weightPlugStrings(list) -> MStringArray"""
    def getWeights(self, index: int | MDagPath, components: MObject) -> MFloatArray:
        """getWeights(path, components) -> MFloatArray"""
    def groupIdAtIndex(self, plugIndex: int) -> int:
        """Returns the groupId associated with the specified geometry."""
    def hasAttribute(self, name: Any) -> bool:
        """Returns True if the node has an attribute with the given name."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def hasUniqueName(self) -> bool:
        """Returns True if the node's name is unique."""
    def indexForGroupId(self, groupId: int) -> int:
        """Returns the plug index of the geometry associated with the specified groupId."""
    def indexForOutputConnection(self, connIndex: int) -> int:
        """Returns the plug index corresponding to a connection index. The"""
    def indexForOutputShape(self, shape: MObject) -> int:
        """Returns the plug index for the specified output shape."""
    def inputShapeAtIndex(self, plugIndex: int) -> MObject:
        """Returns the input shape corresponding to the plug index."""
    def isFlagSet(self, flag: int) -> bool:
        """Returns the state of the specified node flag."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files."""
    def isTrackingEdits(self) -> bool:
        """Returns True if the node is referenced or in an assembly that is tracking edits."""
    def name(self) -> Any:
        """Returns the node's name."""
    def numOutputConnections(self) -> int:
        """Returns the number of output geometries connected to this node. This"""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def outputShapeAtIndex(self, index: int) -> MObject:
        """Returns the DAG path to which this function set is attached, or the first path to the node if the function set is attached to an MObject."""
    def plugsAlias(self, plug: MPlug) -> Any:
        """Returns the alias for a plug's attribute."""
    def removeAttribute(self, attr: MObject, type: Any) -> None:
        """Removes a dynamic attribute from the node."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Returns one of the node's attribute, based on the order in which they are written to file."""
    def setAffectsAnimation(self) -> None:
        """Specifies that modifications to a node could potentially affect the animation."""
    def setAlias(self, alias: Any, name: Any, plug: MPlug, add: bool | None = None) -> bool:
        """Adds or removes an attribute alias."""
    def setDoNotWrite(self, flag: bool) -> None:
        """Used to prevent the node from being written to file."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> None:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> None:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> None:
        """Sets the state of the specified node flag."""
    def setName(self, name: Any, createNamespace: bool | None = None) -> Any:
        """Sets the node's name."""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def setWeight(self, path: MDagPath, index: int | MObject, components: MObject | float, weight: float, oldValues: Any = None) -> Any:
        """setWeight(path, index, components, values)"""
    def type(self) -> int:
        """Returns the type of the function set."""
    def uniqueName(self) -> Any:
        """For a DAG node, the unique name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself. For a non-DAG node, the uniqueName is just its name."""
    def userNode(self) -> MPxNode:
        """Returns the MPxNode object for a plugin node."""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""
    def weightPlugStrings(self, list: MSelectionList) -> str:
        """Returns a string (separated by spaces) containing the names of the plugs on this node that correspond to the components in the selection list."""