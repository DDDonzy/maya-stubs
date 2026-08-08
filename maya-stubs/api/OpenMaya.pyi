# Stub for maya.api.OpenMaya - generated from Maya 2024 Python API reference

from typing import Any

def getStringResource(*args: Any, **kwargs: Any) -> Any: ...
def registerStringResource(*args: Any, **kwargs: Any) -> Any: ...
def registerStringResources(*args: Any, **kwargs: Any) -> Any: ...

class MAngle:
    kAngMinutes: Any
    kAngSeconds: Any
    kDegrees: Any
    kInvalid: Any
    kLast: Any
    kRadians: Any
    unit: Any
    value: Any
    def __init__(self, src: MAngle | float | None = None, u: Any = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def asAngMinutes(self) -> float:
        """Returns the angular value, converted to minutes of arc."""
    def asAngSeconds(self) -> float:
        """Returns the angular value, converted to seconds of arc."""
    def asDegrees(self) -> float:
        """Returns the angular value, converted to degrees."""
    def asRadians(self) -> float:
        """Returns the angular value, converted to radians."""
    def asUnits(self, otherUnit: Any) -> float:
        """Returns the angular value, converted to the specified units."""
    @staticmethod
    def internalToUI(internalValue: float) -> float:
        """Converts a value from Maya's internal units to the units used in the UI."""
    @staticmethod
    def internalUnit() -> Any:
        """Returns the angular unit used internally by Maya."""
    @staticmethod
    def setUIUnit(newUnit: Any) -> None:
        """Sets the angular unit used in Maya's UI."""
    @staticmethod
    def uiToInternal(uiValue: float) -> float:
        """Converts a value from the units used in the UI to Maya's internal units."""
    @staticmethod
    def uiUnit() -> Any:
        """Returns the units used to display angles in Maya's UI."""

class MArgDatabase:
    isEdit: Any
    isQuery: Any
    numberOfFlagsUsed: Any
    def __init__(self, syntax: MSyntax | None = None, argList: MArgList | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def commandArgumentBool(self, argIndex: int) -> bool:
        """Returns the specified command argument as a bool."""
    def commandArgumentDouble(self, index: int) -> float:
        """Alias for commandArgumentFloat()."""
    def commandArgumentFloat(self, argIndex: Any) -> float:
        """Returns the specified command argument as a float."""
    def commandArgumentInt(self, argIndex: int) -> int:
        """Returns the specified command argument as an int."""
    def commandArgumentMAngle(self, argIndex: int) -> MAngle:
        """Returns the specified command argument as an MAngle."""
    def commandArgumentMDistance(self, argIndex: int) -> MDistance:
        """Returns the specified command argument as an MDistance."""
    def commandArgumentMSelectionList(self, argIndex: Any) -> MSelectionList:
        """Returns the specified command argument as an MSelectionList."""
    def commandArgumentMTime(self, argIndex: int) -> MTime:
        """Returns the specified command argument as an MTime."""
    def commandArgumentString(self, argIndex: int) -> Any:
        """Returns the specified command argument as a string."""
    def flagArgumentBool(self, flagName: Any, argIndex: int) -> bool:
        """Returns the specified argument of the specified single-use flag as"""
    def flagArgumentDouble(self, flagName: Any, argIndex: int) -> float:
        """Alias for flagArgumentFloat()."""
    def flagArgumentFloat(self, flagName: Any, argIndex: Any) -> float:
        """Returns the specified argument of the specified single-use flag as"""
    def flagArgumentInt(self, flagName: Any, argIndex: int) -> int:
        """Returns the specified argument of the specified single-use flag as"""
    def flagArgumentMAngle(self, flagName: Any, argIndex: int) -> MAngle:
        """Returns the specified argument of the specified single-use flag as"""
    def flagArgumentMDistance(self, flagName: Any, argIndex: int) -> MDistance:
        """Returns the specified argument of the specified single-use flag as"""
    def flagArgumentMSelectionList(self, flagName: Any, argIndex: Any) -> MSelectionList:
        """Returns the specified argument of the specified single-use flag as"""
    def flagArgumentMTime(self, flagName: Any, argIndex: int) -> MTime:
        """Returns the specified argument of the specified single-use flag as"""
    def flagArgumentString(self, flagName: Any, argIndex: int) -> Any:
        """Returns the specified argument of the specified single-use flag as"""
    def getFlagArgumentList(self, flagName: Any, occurrence: int) -> MArgList:
        """Returns the arguments for the specified occurrence of the given"""
    def getFlagArgumentPosition(self, flagName: Any, occurrence: int) -> int:
        """Returns the position in the argument list of the specified occurrence"""
    def getObjectList(self) -> MSelectionList:
        """If the command's MSyntax has set the object format to kSelectionList"""
    def getObjectStrings(self) -> tuple[Any]:
        """If the command's MSyntax has set the object format to kStringObjects"""
    def isFlagSet(self, flagName: Any) -> bool:
        """Returns True if the given flag appears on the command line."""
    def numberOfFlagUses(self, flagName: Any) -> int:
        """Returns the number of times that the flag appears on the command"""

class MArgList:
    kInvalidArgIndex: Any
    def __init__(self, other: MArgList | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addArg(self, arg: Any) -> Any:
        """MTime, MPoint or	MVector."""
    def asAngle(self, index: int) -> MAngle:
        """Return an argument as an MAngle."""
    def asBool(self, index: int) -> bool:
        """Return an argument as a boolean."""
    def asDistance(self, index: int) -> MDistance:
        """Return an argument as an MDistance."""
    def asDouble(self, index: int) -> float:
        """Alias for asFloat()."""
    def asDoubleArray(self, index: int) -> MDoubleArray:
        """Return a sequence of arguments as an MDoubleArray."""
    def asFloat(self, index: Any) -> float:
        """Return an argument as a float."""
    def asInt(self, index: int) -> int:
        """Return an argument as an integer."""
    def asIntArray(self, index: int) -> MIntArray:
        """Return a sequence of arguments as an MIntArray."""
    def asMatrix(self, index: int) -> MMatrix:
        """Return a sequence of arguments as an MMatrix."""
    def asPoint(self, index: int) -> MPoint:
        """Return a sequence of arguments as an MPoint."""
    def asString(self, index: int) -> Any:
        """Return an argument as a string."""
    def asStringArray(self, index: int) -> list[str]:
        """Return a sequence of arguments as a list of strings."""
    def asTime(self, index: int) -> MTime:
        """Return an argument as an MTime."""
    def asVector(self, index: int) -> MVector:
        """Return a sequence of arguments as an MVector."""
    def flagIndex(self, shortFlag: Any, longFlag: Any = None) -> int:
        """Return index of first occurrence of specified flag."""
    def lastArgUsed(self) -> int:
        """Return index of last argument used by the most recent as*() method."""

class MArgParser:
    isEdit: Any
    isQuery: Any
    numberOfFlagsUsed: Any
    def __init__(self, syntax: MSyntax | None = None, argList: MArgList | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def commandArgumentBool(self, argIndex: int) -> bool:
        """Returns the specified command argument as a bool."""
    def commandArgumentDouble(self, index: int) -> float:
        """Alias for commandArgumentFloat()."""
    def commandArgumentFloat(self, argIndex: Any) -> float:
        """Returns the specified command argument as a float."""
    def commandArgumentInt(self, argIndex: int) -> int:
        """Returns the specified command argument as an int."""
    def commandArgumentMAngle(self, argIndex: int) -> MAngle:
        """Returns the specified command argument as an MAngle."""
    def commandArgumentMDistance(self, argIndex: int) -> MDistance:
        """Returns the specified command argument as an MDistance."""
    def commandArgumentMTime(self, argIndex: int) -> MTime:
        """Returns the specified command argument as an MTime."""
    def commandArgumentString(self, argIndex: int) -> Any:
        """Returns the specified command argument as a string."""
    def flagArgumentBool(self, flagName: Any, argIndex: int) -> bool:
        """Returns the specified argument of the specified single-use flag as"""
    def flagArgumentDouble(self, flagName: Any, argIndex: int) -> float:
        """Alias for flagArgumentFloat()."""
    def flagArgumentFloat(self, flagName: Any, argIndex: Any) -> float:
        """Returns the specified argument of the specified single-use flag as"""
    def flagArgumentInt(self, flagName: Any, argIndex: int) -> int:
        """Returns the specified argument of the specified single-use flag as"""
    def flagArgumentMAngle(self, flagName: Any, argIndex: int) -> MAngle:
        """Returns the specified argument of the specified single-use flag as"""
    def flagArgumentMDistance(self, flagName: Any, argIndex: int) -> MDistance:
        """Returns the specified argument of the specified single-use flag as"""
    def flagArgumentMTime(self, flagName: Any, argIndex: int) -> MTime:
        """Returns the specified argument of the specified single-use flag as"""
    def flagArgumentString(self, flagName: Any, argIndex: int) -> Any:
        """Returns the specified argument of the specified single-use flag as"""
    def getFlagArgumentList(self, flagName: Any, occurrence: int) -> MArgList:
        """Returns the arguments for the specified occurrence of the given"""
    def getFlagArgumentPosition(self, flagName: Any, occurrence: int) -> int:
        """Returns the position in the argument list of the specified occurrence"""
    def getObjectStrings(self) -> tuple[Any]:
        """If the command's MSyntax has set the object format to kStringObjects"""
    def isFlagSet(self, flagName: Any) -> bool:
        """Returns True if the given flag appears on the command line."""
    def numberOfFlagUses(self, flagName: Any) -> int:
        """Returns the number of times that the flag appears on the command"""

class MArrayDataBuilder:
    def __init__(self, attribute: MObject | MArrayDataBuilder | None = None, numElements: int | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addElement(self, index: int) -> MDataHandle:
        """Adds a new element to the array at the given index."""
    def addElementArray(self, index: int) -> MArrayDataHandle:
        """Adds a new element to the array at the given index.  The added element is also an array."""
    def addLast(self) -> MDataHandle:
        """Adds a new element to the end of the array.  The index of the element will be the current highest index + 1."""
    def addLastArray(self) -> MArrayDataHandle:
        """Adds a new element to the end of the array.  The added element is also an array.  The index of the element will the current highest index + 1."""
    def copy(self, source: Any) -> MArrayDataBuilder:
        """Copy data from source builder."""
    def growArray(self, amount: int) -> MArrayDataBuilder:
        """Grows the array storage by the given amount."""
    def removeElement(self, index: int) -> MArrayDataBuilder:
        """Removes the specified element from the array"""
    def setGrowSize(self, size: int) -> MArrayDataBuilder:
        """Sets the grow size of the array.  As elements are added to the array, the builder will allocate memory in chunks.  This method tells the builder how many elements to allocate each time it grows the array."""

class MArrayDataHandle:
    def __init__(self, in_: MDataHandle | MArrayDataHandle | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def builder(self) -> MArrayDataBuilder:
        """Returns a builder for this handle's array so that it can be expanded."""
    def copy(self, source: Any) -> MArrayDataHandle:
        """Copy data from source array."""
    def elementLogicalIndex(self) -> int:
        """Returns the index that we are currently at in the array.  It is possible for the index to be invalid, in which case the return status will report an error.  These may be sparse arrays so the element index returned will be a logical index."""
    def inputArrayValue(self) -> MArrayDataHandle:
        """Gets a handle into this data block for the current array element.  This method should be used when the array elements are also arrays.  The data represented by the handle will be valid.  If the data is from an dirty connection, then the connection will be evaluated."""
    def inputValue(self) -> MDataHandle:
        """Gets a handle into this data block for the current array element.  The data represented by the handle will be valid.  If the data is from an dirty connection, then the connection will be evaluated."""
    def isDone(self) -> bool:
        """Specifies whether or not there are more elements to iterate over."""
    def jumpToLogicalElement(self, index: Any) -> MArrayDataHandle:
        """Jump to a specific logical element in the array."""
    def jumpToPhysicalElement(self, position: Any) -> MArrayDataHandle:
        """Jump to a specific physical element in the array."""
    def next(self) -> bool:
        """Advance to the next element in the array."""
    def outputArrayValue(self) -> MArrayDataHandle:
        """Gets a handle into this data block for the current array element.  This method should be used when the array elements are also arrays. The array's elements are not evaluated and may no longer be valid. Therefore, this handle should only be used for writing over the data."""
    def outputValue(self) -> MDataHandle:
        """Gets a handle into this data block for the current array element. The element is not evaluated so its data may not be valid. Therefore, this handle should only be used for writing over the data."""
    def set(self, builder: Any) -> MArrayDataHandle:
        """Sets the data for this array from the data in the builder object"""
    def setAllClean(self) -> MArrayDataHandle:
        """Marks every element of the array attribute represented by the handle as clean.  This method should be used if a compute function is asked to compute a single element of a multi, but instead calculates all the elements.  Calling <i>setAllClean</i> in this situation will prevent further calls to the node's compute method for the other elements of the multi."""
    def setClean(self) -> MArrayDataHandle:
        """Marks the data that is represented by this handle as being clean.  This should be done after recalculating the data from the inputs."""

class MAttributeIndex:
    kFloat: Any
    kInteger: Any
    def __init__(self, other: MAttributeIndex | int | float | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def copy(self, source: Any) -> MAttributeIndex:
        """Copy data from source index."""
    def getLower(self) -> Any:
        """Returns the lower bound of the index."""
    def getUpper(self) -> Any:
        """Returns the upper bound of the index."""
    def getValue(self) -> Any:
        """Returns the current value of the index."""
    def hasLowerBound(self) -> bool:
        """Returns True if a lower bound is specified."""
    def hasRange(self) -> bool:
        """Returns True if a range was specified."""
    def hasUpperBound(self) -> bool:
        """Returns True if an upper bound is specified."""
    def hasValidRange(self) -> bool:
        """Returns True if upper bound is greater than lower bound."""
    def isBounded(self) -> bool:
        """Returns True if the index is bounded."""
    def setLower(self, value: int | float) -> MAttributeIndex:
        """Sets the lower bound of the index."""
    def setType(self, type: Any) -> MAttributeIndex:
        """Sets the type of attribute index."""
    def setUpper(self, value: int | float) -> MAttributeIndex:
        """Sets the upper bound of the index."""
    def setValue(self, value: int | float) -> MAttributeIndex:
        """Sets the value of the index."""
    def type(self) -> int:
        """Returns the type of attribute index."""

class MAttributePattern:
    def __init__(self, name: Any = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addRootAttr(self, attr: MObject) -> None:
        """Add the given root attribute to this pattern."""
    @staticmethod
    def attrPattern(n: int) -> MAttributePattern:
        """Return the specified pattern indexed from the global list."""
    @staticmethod
    def attrPatternCount() -> int:
        """Return the global number of patterns created."""
    @staticmethod
    def findPattern(name: Any) -> MAttributePattern:
        """Return a pattern with the given name, None if not found."""
    def name(self) -> Any:
        """Return the name of the attribute pattern."""
    def removeRootAttr(self, idx: int | MObject) -> None:
        """Return the nth or passed-in root attribute from this pattern."""
    def rootAttr(self, idx: int) -> MObject:
        """Return the nth root attribute in this pattern."""
    def rootAttrCount(self) -> int:
        """Return the number of root attributes in this pattern."""

class MAttributeSpec:
    dimensions: Any
    name: Any
    def __init__(self, name: Any = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def copy(self, source: Any) -> MAttributeSpec:
        """Copy data from source specification."""

class MAttributeSpecArray:
    sizeIncrement: Any
    def __init__(self, other: MAttributeSpecArray | int | None = None, initialValue: MAttributeSpec | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def append(self, element: MAttributeSpec) -> None:
        """Add a value to the end of the array."""
    def clear(self) -> None:
        """Remove all elements from the array."""
    def copy(self, source: MAttributeSpecArray) -> None:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self, element: MAttributeSpec, index: int) -> None:
        """Insert a new value into the array at the given index."""
    def remove(self, index: int) -> None:
        """Remove an element from the array."""
    def setLength(self, length: int) -> None:
        """Grow or shrink the array to contain a specific number of elements."""

class MBoundingBox:
    center: Any
    depth: Any
    height: Any
    max: Any
    min: Any
    width: Any
    def __init__(self, src: MBoundingBox | MPoint | None = None, corner2: MPoint | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def clear(self) -> None:
        """Empties the bounding box, setting its corners to (0, 0, 0)."""
    def contains(self, point: MPoint) -> bool:
        """Returns True if a point lies within the bounding box."""
    def expand(self, point: MPoint | MBoundingBox) -> None:
        """Expands the bounding box to include a point or other bounding box."""
    def intersects(self, box: MBoundingBox, tol: float | None = None) -> bool:
        """Returns True if any part of a given bounding box lies within this one."""
    def transformUsing(self, matrix: MMatrix) -> None:
        """Multiplies the bounding box's corners by a matrix."""

class MCacheSchema:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def add(self, attribute: Any) -> MCacheSchema:
        """Force the attribute to be cached"""
    def reset(self) -> Any:
        """Reset this schema to the minimal."""

class MCallbackIdArray:
    sizeIncrement: Any
    def __init__(self, other: MCallbackIdArray | int | None = None, initialValue: Any = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def append(self, element: Any) -> None:
        """Add a value to the end of the array."""
    def clear(self) -> None:
        """Remove all elements from the array."""
    def copy(self, source: MCallbackIdArray) -> None:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self, element: Any, index: int) -> None:
        """Insert a new value into the array at the given index."""
    def remove(self, index: int) -> None:
        """Remove an element from the array."""
    def setLength(self, length: int) -> None:
        """Grow or shrink the array to contain a specific number of elements."""

class MCameraMessage:
    kDefaultAction: Any
    kDoAction: Any
    kDoNotDoAction: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def addBeginManipulationCallback(node: MObject, function: int, clientData: None = None) -> int:
        """Registers callbacks for camera manipulation beginning messages."""
    @staticmethod
    def addEndManipulationCallback(node: MObject, function: int, clientData: None = None) -> int:
        """Registers callbacks for camera manipulation ending messages."""
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

class MColor:
    a: float
    b: float
    g: float
    kByte: Any
    kCMY: Any
    kCMYK: Any
    kFloat: Any
    kHSV: Any
    kOpaqueBlack: Any
    kRGB: Any
    kShort: Any
    r: float
    def __init__(self, src: Any = None, gg: Any = None, bb: Any = None, aa: Any = None, alpha: Any = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getColor(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the color's components, in the specified color model."""
    def setColor(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the color's components and color model."""

class MColorArray:
    sizeIncrement: Any
    def __init__(self, other: MColorArray | int | None = None, initialValue: MColor | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def append(self, element: MColor | float, g: float, b: float, a: float | None = None) -> None:
        """Add a value to the end of the array."""
    def clear(self) -> None:
        """Remove all elements from the array."""
    def copy(self, source: MColorArray) -> None:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self, element: MColor, index: int) -> None:
        """Insert a new value into the array at the given index."""
    def remove(self, index: int) -> None:
        """Remove an element from the array."""
    def setLength(self, length: int) -> None:
        """Grow or shrink the array to contain a specific number of elements."""

class MCommandMessage:
    kDefaultAction: Any
    kDisplay: Any
    kDoAction: Any
    kDoNotDoAction: Any
    kError: Any
    kHistory: Any
    kInfo: Any
    kMELCommand: Any
    kMELProc: Any
    kResult: Any
    kStackTrace: Any
    kWarning: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def addCommandCallback(function: int, clientData: None = None) -> int:
        """This method registers a callback for command messages that are"""
    @staticmethod
    def addCommandOutputCallback(function: int, clientData: None = None) -> int:
        """This method registers a callback for whenever commands generate"""
    @staticmethod
    def addCommandOutputFilterCallback(function: int, clientData: None = None) -> int:
        """This method registers a callback for whenever commands generate"""
    @staticmethod
    def addProcCallback(function: int, clientData: None = None) -> int:
        """This method registers a callback that is executed every time a MEL"""
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

class MConditionMessage:
    kDefaultAction: Any
    kDoAction: Any
    kDoNotDoAction: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def addConditionCallback(conditionName: Any, function: int, clientData: None = None) -> int:
        """This method registers a callback for condition changed messages."""
    @staticmethod
    def currentCallbackId() -> int:
        """Returns the callback ID of the currently executing callback. If called"""
    @staticmethod
    def getConditionNames(arg: Any, string: Any, arg_: Any) -> Any:
        """This method returns the list of available condition names."""
    @staticmethod
    def getConditionState(name: Any) -> bool:
        """This method returns the current state of a condition."""
    @staticmethod
    def nodeCallbacks(node: Any) -> int:
        """Returns a list of callback IDs registered to a given node."""
    @staticmethod
    def removeCallback(id: Any) -> None:
        """Removes the specified callback from Maya."""
    @staticmethod
    def removeCallbacks(ids: Any) -> None:
        """Removes all of the specified callbacks from Maya."""

class MContainerMessage:
    kDefaultAction: Any
    kDoAction: Any
    kDoNotDoAction: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def addBoundAttrCallback(function: int, clientData: None = None) -> int:
        """This method registers a callback that is called whenever an attribute"""
    @staticmethod
    def addPublishAttrCallback(function: int, clientData: None = None) -> int:
        """This method registers a callback that is called whenever an attribute"""
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

class MDAGDrawOverrideInfo:
    displayType: Any
    enableShading: Any
    enableTexturing: Any
    enableVisible: Any
    kDisplayTypeNormal: Any
    kDisplayTypeReference: Any
    kDisplayTypeTemplate: Any
    kLODBoundingBox: Any
    kLODFull: Any
    lod: Any
    overrideEnabled: Any
    playbackVisible: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MDGContext:
    kNormal: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def copy(self, source: Any) -> MDGContext:
        """Copy data from source context."""
    @staticmethod
    def current(*args: Any, **kwargs: Any) -> Any:
        """Returns the current context being used for evaluation."""
    def getTime(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the time at which this context is set to evaluate."""
    def isCurrent(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the context is currently being used for evaluation. Returns False if some other context is being used for evaluation."""
    def isNormal(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the context is set to evaluate normally. Returns False if the context is set to evaluate at a specific time."""
    def makeCurrent(self, *args: Any, **kwargs: Any) -> Any:
        """Makes this context the new current one being used for evaluation. Returns the previous evaluation context."""

class MDGMessage:
    kDefaultAction: Any
    kDoAction: Any
    kDoNotDoAction: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def addConnectionCallback(function: Any, clientData: Any = None) -> int:
        """This method registers a callback that is called whenever a connection"""
    @staticmethod
    def addDelayedTimeChangeCallback(function: Any, clientData: Any = None) -> int:
        """This method registers a callback that is called whenever the time"""
    @staticmethod
    def addDelayedTimeChangeRunupCallback(function: Any, clientData: Any = None) -> int:
        """This method registers a callback that is called whenever the time"""
    @staticmethod
    def addForceUpdateCallback(function: Any, clientData: Any = None) -> int:
        """This method registers a callback that is called after the time"""
    @staticmethod
    def addNodeAddedCallback(function: Any, nodeType: Any, clientData: Any = None) -> int:
        """This method registers a callback that is called whenever a new node"""
    @staticmethod
    def addNodeChangeUuidCheckCallback(function: Any, clientData: Any = None) -> int:
        """This method registers a callback that is called whenever a node"""
    @staticmethod
    def addNodeRemovedCallback(function: Any, nodeType: Any, clientData: Any = None) -> int:
        """This method registers a callback that is called whenever a new node"""
    @staticmethod
    def addPreConnectionCallback(function: Any, clientData: Any = None) -> int:
        """This method registers a callback that is called whenever any connection"""
    @staticmethod
    def addTimeChangeCallback(function: Any, clientData: Any = None) -> int:
        """This method registers a callback that is called whenever the time"""
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

class MDGModifier:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addAttribute(self, arg: Any, arg_: Any) -> MDGModifier:
        """Adds an operation to the modifier to add a new dynamic attribute to the"""
    def addExtensionAttribute(self, arg: Any, arg_: Any) -> MDGModifier:
        """Adds an operation to the modifier to add a new extension attribute to"""
    def commandToExecute(self, command: Any) -> MDGModifier:
        """Adds an operation to the modifier to execute a MEL command. The command"""
    def connect(self, arg: Any, arg_: Any) -> MDGModifier:
        """connect(MObject sourceNode, MObject sourceAttr,"""
    def createNode(self, typeName: Any) -> MObject:
        """createNode(MTypeId typeId) -> MObject"""
    def deleteNode(self, arg: Any, arg_: Any) -> MDGModifier:
        """Adds an operation to the modifier which deletes the specified node from"""
    def disconnect(self, arg: Any, arg_: Any) -> MDGModifier:
        """disconnect(MObject sourceNode, MObject sourceAttr,"""
    def doIt(self) -> MDGModifier:
        """Executes the modifier's operations. If doIt() is called multiple times"""
    def linkExtensionAttributeToPlugin(self, arg: Any, arg_: Any) -> MDGModifier:
        """The plugin can call this method to indicate that the extension attribute"""
    def newPlugValue(self, arg: Any, arg_: Any) -> MDGModifier:
        """Adds an operation to the modifier to set the value of a plug, where"""
    def newPlugValueBool(self, arg: Any, arg_: Any) -> MDGModifier:
        """Adds an operation to the modifier to set a value onto a bool plug."""
    def newPlugValueChar(self, arg: Any, arg_: Any) -> MDGModifier:
        """Adds an operation to the modifier to set a value onto a char (single"""
    def newPlugValueDouble(self, arg: Any, arg_: Any) -> MDGModifier:
        """Adds an operation to the modifier to set a value onto a double-precision"""
    def newPlugValueFloat(self, arg: Any, arg_: Any) -> MDGModifier:
        """Adds an operation to the modifier to set a value onto a single-precision"""
    def newPlugValueInt(self, arg: Any, arg_: Any) -> MDGModifier:
        """Adds an operation to the modifier to set a value onto an int plug."""
    def newPlugValueMAngle(self, arg: Any, arg_: Any) -> MDGModifier:
        """Adds an operation to the modifier to set a value onto an angle plug."""
    def newPlugValueMDistance(self, arg: Any, arg_: Any) -> MDGModifier:
        """Adds an operation to the modifier to set a value onto a distance plug."""
    def newPlugValueMTime(self, arg: Any, arg_: Any) -> MDGModifier:
        """Adds an operation to the modifier to set a value onto a time plug."""
    def newPlugValueShort(self, arg: Any, arg_: Any) -> MDGModifier:
        """Adds an operation to the modifier to set a value onto a short"""
    def newPlugValueString(self, arg: Any, arg_: Any) -> MDGModifier:
        """Adds an operation to the modifier to set a value onto a string plug."""
    def pythonCommandToExecute(self, arg: Any) -> MDGModifier:
        """Adds an operation to the modifier to execute a Python command, which"""
    def removeAttribute(self, arg: Any, arg_: Any) -> MDGModifier:
        """Adds an operation to the modifier to remove a dynamic attribute from the"""
    def removeExtensionAttribute(self, arg: Any, arg_: Any) -> MDGModifier:
        """Adds an operation to the modifier to remove an extension attribute from"""
    def removeExtensionAttributeIfUnset(self, *args: Any, **kwargs: Any) -> Any:
        """removeExtensionAttributeIfUnset(MNodeClass nodeClass,"""
    def removeMultiInstance(self, arg: Any, arg_: Any) -> MDGModifier:
        """Adds an operation to the modifier to remove an element of a multi (array) plug."""
    def renameAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """renameAttribute(MObject node, MObject attribute, """
    def renameNode(self, arg: Any, arg_: Any) -> MDGModifier:
        """Adds an operation to the modifer to rename a node."""
    def setNodeLockState(self, arg: Any, arg_: Any) -> MDGModifier:
        """Adds an operation to the modifier to set the lockState of a node."""
    def undoIt(self) -> MDGModifier:
        """Undoes all of the operations that have been given to this modifier. It"""
    def unlinkExtensionAttributeFromPlugin(self, *args: Any, **kwargs: Any) -> Any:
        """unlinkExtensionAttributeFromPlugin(MObject plugin,"""

class MDagMessage:
    kAll: Any
    kChildAdded: Any
    kChildRemoved: Any
    kChildReordered: Any
    kDefaultAction: Any
    kDoAction: Any
    kDoNotDoAction: Any
    kInstanceAdded: Any
    kInstanceRemoved: Any
    kInvalidMsg: Any
    kLast: Any
    kParentAdded: Any
    kParentRemoved: Any
    kRotateOrder: Any
    kRotateOrient: Any
    kRotateOrientX: Any
    kRotateOrientY: Any
    kRotateOrientZ: Any
    kRotatePivot: Any
    kRotatePivotTrans: Any
    kRotatePivotX: Any
    kRotatePivotY: Any
    kRotatePivotZ: Any
    kRotateTransX: Any
    kRotateTransY: Any
    kRotateTransZ: Any
    kRotateX: Any
    kRotateY: Any
    kRotateZ: Any
    kRotation: Any
    kScale: Any
    kScalePivot: Any
    kScalePivotTrans: Any
    kScalePivotX: Any
    kScalePivotY: Any
    kScalePivotZ: Any
    kScaleTransX: Any
    kScaleTransY: Any
    kScaleTransZ: Any
    kScaleX: Any
    kScaleY: Any
    kScaleZ: Any
    kShear: Any
    kShearXY: Any
    kShearXZ: Any
    kShearYZ: Any
    kTranslateX: Any
    kTranslateY: Any
    kTranslateZ: Any
    kTranslation: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def addAllDagChangesCallback(function: int | MDagPath, clientData: None | int = None) -> int:
        """This method registers a callback that is called whenever any"""
    @staticmethod
    def addAllDagChangesDagPathCallback(node: MDagPath, function: int, clientData: None = None) -> int:
        """This method registers a callback that is called whenever a DAG"""
    @staticmethod
    def addChildAddedCallback(function: int | MDagPath, clientData: None | int = None) -> int:
        """This method registers a callback that is called whenever a child is"""
    @staticmethod
    def addChildAddedDagPathCallback(node: MDagPath, function: int, clientData: None = None) -> int:
        """This method registers a callback that is called whenever a child is"""
    @staticmethod
    def addChildRemovedCallback(function: int | MDagPath, clientData: None | int = None) -> int:
        """This method registers a callback that is called whenever a child is"""
    @staticmethod
    def addChildRemovedDagPathCallback(node: MDagPath, function: int, clientData: None = None) -> int:
        """This method registers a callback that is called whenever a child is"""
    @staticmethod
    def addChildReorderedCallback(function: int | MDagPath, clientData: None | int = None) -> int:
        """This method registers a callback that is called whenever a child is"""
    @staticmethod
    def addChildReorderedDagPathCallback(node: MDagPath, function: int, clientData: None = None) -> int:
        """This method registers a callback that is called whenever a child of"""
    @staticmethod
    def addDagCallback(msgType: Any, function: Any, clientData: None | int = None) -> int:
        """This method registers a callback that is called for specified"""
    @staticmethod
    def addDagDagPathCallback(node: MDagPath, msgType: Any, function: int, clientData: None = None) -> int:
        """This method registers a callback that is called for specified a DAG"""
    @staticmethod
    def addInstanceAddedCallback(function: int | MDagPath, clientData: None | int = None) -> int:
        """This method registers a callback that is called whenever any node in the DAG"""
    @staticmethod
    def addInstanceAddedDagPathCallback(node: MDagPath, function: int, clientData: None = None) -> int:
        """This method registers a callback that is called whenever the specified node"""
    @staticmethod
    def addInstanceRemovedCallback(function: int | MDagPath, clientData: None | int = None) -> int:
        """This method registers a callback that is called whenever an instance of any DAG"""
    @staticmethod
    def addInstanceRemovedDagPathCallback(node: MDagPath, function: int, clientData: None = None) -> int:
        """This method registers a callback that is called whenever an instance of the specified"""
    @staticmethod
    def addMatrixModifiedCallback(node: MDagPath, function: int, clientData: None = None) -> int:
        """This method registers a callback that is called when the local matrix"""
    @staticmethod
    def addParentAddedCallback(function: int | MDagPath, clientData: None | int = None) -> int:
        """This method registers a callback that is called whenever a parent is"""
    @staticmethod
    def addParentAddedDagPathCallback(node: MDagPath, function: int, clientData: None = None) -> int:
        """This method registers a callback that is called whenever a parent is"""
    @staticmethod
    def addParentRemovedCallback(function: int | MDagPath, clientData: None | int = None) -> int:
        """This method registers a callback that is called whenever a parent is"""
    @staticmethod
    def addParentRemovedDagPathCallback(node: MDagPath, function: int, clientData: None = None) -> int:
        """This method registers a callback that is called whenever a parent is"""
    @staticmethod
    def addWorldMatrixModifiedCallback(node: MDagPath, function: int, clientData: None = None) -> int:
        """This method registers a callback that is called when a parent matrix of the"""
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

class MDagModifier:
    def __init__(self) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addAttribute(self, arg: MObject, arg_: MObject) -> MDagModifier:
        """Adds an operation to the modifier to add a new dynamic attribute to the"""
    def addExtensionAttribute(self, arg: MNodeClass, arg_: MObject) -> MDagModifier:
        """Adds an operation to the modifier to add a new extension attribute to"""
    def commandToExecute(self, command: Any) -> MDagModifier:
        """Adds an operation to the modifier to execute a MEL command. The command"""
    def connect(self, arg: MObject | MPlug, arg_: MObject | MPlug) -> MDagModifier:
        """connect(MObject sourceNode, MObject sourceAttr,"""
    def createNode(self, typeName: Any, parent: MObject | None = None) -> Any:
        """createNode(typeId,   parent=MObject.kNullObj) -> new DAG node MObject"""
    def deleteNode(self, arg: MObject, arg_: bool) -> MDagModifier:
        """Adds an operation to the modifier which deletes the specified node from"""
    def disconnect(self, arg: MObject | MPlug, arg_: MObject | MPlug) -> MDagModifier:
        """disconnect(MObject sourceNode, MObject sourceAttr,"""
    def doIt(self) -> MDagModifier:
        """Executes the modifier's operations. If doIt() is called multiple times"""
    def linkExtensionAttributeToPlugin(self, arg: MObject, arg_: MObject) -> MDagModifier:
        """The plugin can call this method to indicate that the extension attribute"""
    def newPlugValue(self, arg: MPlug, arg_: Any) -> MDagModifier:
        """Adds an operation to the modifier to set the value of a plug, where"""
    def newPlugValueBool(self, arg: MPlug, arg_: bool) -> MDagModifier:
        """Adds an operation to the modifier to set a value onto a bool plug."""
    def newPlugValueChar(self, arg: MPlug, arg_: Any) -> MDagModifier:
        """Adds an operation to the modifier to set a value onto a char (single"""
    def newPlugValueDouble(self, arg: MPlug, arg_: float) -> MDagModifier:
        """Adds an operation to the modifier to set a value onto a double-precision"""
    def newPlugValueFloat(self, arg: MPlug, arg_: float) -> MDagModifier:
        """Adds an operation to the modifier to set a value onto a single-precision"""
    def newPlugValueInt(self, arg: MPlug, arg_: int) -> MDagModifier:
        """Adds an operation to the modifier to set a value onto an int plug."""
    def newPlugValueMAngle(self, arg: MPlug, arg_: MAngle) -> MDagModifier:
        """Adds an operation to the modifier to set a value onto an angle plug."""
    def newPlugValueMDistance(self, arg: MPlug, arg_: MDistance) -> MDagModifier:
        """Adds an operation to the modifier to set a value onto a distance plug."""
    def newPlugValueMTime(self, arg: MPlug, arg_: MTime) -> MDagModifier:
        """Adds an operation to the modifier to set a value onto a time plug."""
    def newPlugValueShort(self, arg: MPlug, arg_: Any) -> MDagModifier:
        """Adds an operation to the modifier to set a value onto a short"""
    def newPlugValueString(self, arg: MPlug, arg_: Any) -> MDagModifier:
        """Adds an operation to the modifier to set a value onto a string plug."""
    def pythonCommandToExecute(self, arg: Any) -> MDagModifier:
        """Adds an operation to the modifier to execute a Python command, which"""
    def removeAttribute(self, arg: MObject, arg_: MObject) -> MDagModifier:
        """Adds an operation to the modifier to remove a dynamic attribute from the"""
    def removeExtensionAttribute(self, arg: MNodeClass, arg_: MObject) -> MDagModifier:
        """Adds an operation to the modifier to remove an extension attribute from"""
    def removeExtensionAttributeIfUnset(self, nodeClass: MNodeClass, attribute: MObject) -> None:
        """removeExtensionAttributeIfUnset(MNodeClass nodeClass,"""
    def removeMultiInstance(self, arg: MPlug, arg_: bool) -> MDagModifier:
        """Adds an operation to the modifier to remove an element of a multi (array) plug."""
    def renameAttribute(self, node: MObject, attribute: MObject, shortName: Any, longName: Any) -> None:
        """renameAttribute(MObject node, MObject attribute, """
    def renameNode(self, arg: MObject, arg_: Any) -> MDagModifier:
        """Adds an operation to the modifer to rename a node."""
    def reparentNode(self, arg: MObject, newParent: MObject | None = None) -> MDagModifier:
        """Adds an operation to the modifier to reparent a DAG node under a"""
    def setNodeLockState(self, arg: MObject, arg_: bool) -> MDagModifier:
        """Adds an operation to the modifier to set the lockState of a node."""
    def undoIt(self) -> MDagModifier:
        """Undoes all of the operations that have been given to this modifier. It"""
    def unlinkExtensionAttributeFromPlugin(self, mPlugin: MObject, mAttribute: MObject) -> None:
        """unlinkExtensionAttributeFromPlugin(MObject plugin,"""

class MDagPath:
    def __init__(self, src: MDagPath | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def apiType(self) -> int:
        """Returns the type of the object at the end of the path."""
    def child(self, index: int) -> MDagPath:
        """Returns the specified child of the object at the end of the path."""
    def childCount(self) -> int:
        """Returns the number of objects parented directly beneath the object at the end of the path."""
    def exclusiveMatrix(self) -> MMatrix:
        """Returns the matrix for all transforms in the path, excluding the end object."""
    def exclusiveMatrixInverse(self) -> MMatrix:
        """Returns the inverse of exclusiveMatrix()."""
    def extendToShape(self) -> MDagPath:
        """Extends the path to the specified shape node parented directly beneath the transform at the current end of the path."""
    def fullPathName(self) -> Any:
        """Returns a string representation of the path from the DAG root to the path's last node."""
    @staticmethod
    def getAPathTo(node: MObject) -> MDagPath:
        """Returns the first path found to the given node."""
    @staticmethod
    def getAllPathsTo(node: MObject) -> MDagPathArray:
        """Returns all paths to the given node."""
    def getDisplayStatus(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the display status for this path."""
    def getDrawOverrideInfo(self) -> MDAGDrawOverrideInfo:
        """Returns the draw override information for this path."""
    def getPath(self, i: int | None = None) -> MDagPath:
        """Returns the specified sub-path of this path."""
    def hasFn(self, type: int) -> bool:
        """Returns True if the object at the end of the path supports the given function set."""
    def inclusiveMatrix(self) -> MMatrix:
        """Returns the matrix for all transforms in the path, including the end object, if it is a transform."""
    def inclusiveMatrixInverse(self) -> MMatrix:
        """Returns the inverse of inclusiveMatrix()."""
    def instanceNumber(self) -> int:
        """Returns the instance number of this path to the object at the end."""
    def isInstanced(self) -> bool:
        """Returns True if the object at the end of the path can be reached by more than one path."""
    def isTemplated(self) -> bool:
        """Returns true if the DAG Node at the end of the path is templated."""
    def isValid(self) -> bool:
        """Returns True if this is a valid path."""
    def isVisible(self) -> bool:
        """Returns true if the DAG Node at the end of the path is visible."""
    def length(self) -> int:
        """Returns the number of nodes on the path, not including the DAG's root node."""
    @staticmethod
    def matchTransform(source: MDagPath, target: MDagPath, relative: MDagPath, preserveOffsetParentMatrix: bool | None = None, preservePivot: bool | None = None, preservePivotOffset: bool | None = None) -> MTransformationMatrix:
        """Do some new stuff."""
    def node(self) -> MObject:
        """Returns the DAG node at the end of the path."""
    def numberOfShapesDirectlyBelow(self) -> int:
        """Returns the number of shape nodes parented directly beneath the transform at the end of the path."""
    def partialPathName(self) -> Any:
        """Returns the minimum string representation which will uniquely identify the path."""
    def pathCount(self) -> int:
        """Returns the number of sub-paths which make up this path."""
    def pop(self, num: int | None = None) -> None:
        """Removes objects from the end of the path."""
    def push(self, child: MObject) -> None:
        """Extends the path to the specified child object, which must be parented directly beneath the object currently at the end of the path."""
    def set(self, src: MDagPath) -> None:
        """Replaces the current path held by this object with another."""
    def transform(self) -> MDagPath:
        """Returns the last transform node on the path."""

class MDagPathArray:
    sizeIncrement: Any
    def __init__(self, other: MDagPathArray | int | None = None, initialValue: MDagPath | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def append(self, element: MDagPath) -> None:
        """Add a value to the end of the array."""
    def clear(self) -> None:
        """Remove all elements from the array."""
    def copy(self, source: MDagPathArray) -> None:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self, element: MDagPath, index: int) -> None:
        """Insert a new value into the array at the given index."""
    def remove(self, index: int) -> None:
        """Remove an element from the array."""
    def setLength(self, length: int) -> None:
        """Grow or shrink the array to contain a specific number of elements."""

class MDataBlock:
    def __init__(self, in_: MDataBlock) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def context(self) -> MDGContext:
        """Returns a copy of the dependecy graph context for which this data block was created. The context is used to specify how a dependency node is going to be evaluated."""
    def inputArrayValue(self, attr: MObject) -> MArrayDataHandle:
        """inputArrayValue(attribute) -> MArrayDataHandle"""
    def inputValue(self, attr: MObject) -> MDataHandle:
        """inputValue(attribute) -> MDataHandle"""
    def isClean(self, plug: MPlug | MObject) -> bool:
        """isClean(attribute) -> bool"""
    def outputArrayValue(self, attr: MObject) -> MArrayDataHandle:
        """outputArrayValue(attribute) -> MArrayDataHandle"""
    def outputValue(self, attr: MObject) -> MDataHandle:
        """outputValue(attribute) -> MDataHandle"""
    def setClean(self, plug: MPlug | MObject) -> MDataBlock:
        """setClean(attribute) -> self"""
    def setContext(self, ctx: MDGContext) -> MDataBlock:
        """Set the dependency graph context for this data block. The context is used to specify how a dependency node is going to be evaluated, thus replacing the context for the given datablock. This does not modify the dirty state of the datablock so that they apply to the new context."""

class MDataHandle:
    def __init__(self) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def acceptedTypeIds(self) -> Any:
        """This method returns an array of MTypeIds."""
    def asAddr(self) -> int:
        """Returns the data represented by this handle in the data block."""
    def asAngle(self) -> MAngle:
        """Returns the data represented by this handle in the data block."""
    def asBool(self) -> bool:
        """Returns the data represented by this handle in the data block."""
    def asChar(self) -> int:
        """Returns the data represented by this handle in the data block."""
    def asDistance(self) -> MDistance:
        """Returns the data represented by this handle in the data block."""
    def asDouble(self) -> float:
        """Returns the data represented by this handle in the data block."""
    def asDouble2(self) -> Any:
        """Returns the data represented by this handle in the data block."""
    def asDouble3(self) -> Any:
        """Returns the data represented by this handle in the data block."""
    def asDouble4(self) -> Any:
        """Returns the data represented by this handle in the data block."""
    def asFloat(self) -> float:
        """Returns the data represented by this handle in the data block."""
    def asFloat2(self) -> Any:
        """Returns the data represented by this handle in the data block."""
    def asFloat3(self) -> Any:
        """Returns the data represented by this handle in the data block."""
    def asFloatMatrix(self) -> MFloatMatrix:
        """Returns the data represented by this handle in the data block."""
    def asFloatVector(self) -> MFloatVector:
        """Returns the data represented by this handle in the data block."""
    def asGenericBool(self) -> bool:
        """Returns the generic data represented by this handle in the data block."""
    def asGenericChar(self) -> int:
        """Returns the generic data represented by this handle in the data block."""
    def asGenericDouble(self) -> float:
        """Returns the generic data represented by this handle in the data block."""
    def asGenericFloat(self) -> float:
        """Returns the generic data represented by this handle in the data block."""
    def asGenericInt(self) -> int:
        """Returns the generic data represented by this handle in the data block."""
    def asGenericShort(self) -> int:
        """Returns the generic data represented by this handle in the data block."""
    def asInt(self) -> int:
        """Returns the data represented by this handle in the data block."""
    def asInt2(self) -> Any:
        """Returns the data represented by this handle in the data block."""
    def asInt3(self) -> Any:
        """Returns the data represented by this handle in the data block."""
    def asMatrix(self) -> MMatrix:
        """Returns the data represented by this handle in the data block.This method is only valid for attributes created using the MFnMatrixAttribute function set."""
    def asMesh(self) -> MObject:
        """Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the mesh function set and iterators.  Even though this method does not return a reference to an MObject, modifications to the MObject instance will update the contents of the handle in the data block.  The method MDataHandle.setClean() should be called after the data block has been modified."""
    def asMeshTransformed(self) -> MObject:
        """Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the mesh function set (MFnMesh) or any of the mesh iterators."""
    def asNurbsCurve(self) -> MObject:
        """Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the nurbs curve function set and iterator.  Even though this method does not return a reference to an MObject, modifications to the MObject instance will update the contents of the handle in the data block.  The method MDataHandle.setClean() should be called after the data block has been modified."""
    def asNurbsCurveTransformed(self) -> MObject:
        """Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the nurbs curve function set (MFnNurbsCurve) or the nurbs curve CV iterator (MItCurveCV)."""
    def asNurbsSurface(self) -> MObject:
        """Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the nurbs surface function set and iterator.  Even though this method does not return a reference to an MObject, modifications to the MObject instance will update the contents of the handle in the data block.  The method MDataHandle.setClean() should be called after the data block has been modified."""
    def asNurbsSurfaceTransformed(self) -> MObject:
        """Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the nurbs surface function set (MFnNurbsSurface) or the nurbs surface CV iterator (MItSurfaceCV)."""
    def asPluginData(self) -> MPxData:
        """Returns the data represented by this handle in the data block.  The object is returned as plugin data.  This should be used to access data types defined by plugins."""
    def asShort(self) -> int:
        """Returns the data represented by this handle in the data block."""
    def asShort2(self) -> Any:
        """Returns the data represented by this handle in the data block."""
    def asShort3(self) -> Any:
        """Returns the data represented by this handle in the data block."""
    def asString(self) -> Any:
        """Returns the data represented by this handle in the data block."""
    def asSubdSurface(self) -> MObject:
        """Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the subdivision surface function set and iterator.  Even though this method does not return a reference to an MObject, modifications to the MObject instance will update the contents of the handle in the data block.  The method MDataHandle.setClean() should be called after the data block has been modified."""
    def asSubdSurfaceTransformed(self) -> MObject:
        """Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the subdivision surface function set (MFnSubdSurface) or the subdivision surface iterators (MItSubdVertex, MItSubdFace, MItSubdEdge)."""
    def asTime(self) -> MTime:
        """Returns the data represented by this handle in the data block."""
    def asUChar(self) -> int:
        """Returns the data represented by this handle in the data block."""
    def asVector(self) -> MVector:
        """Returns the data represented by this handle in the data block."""
    def child(self, MPlug: MPlug | MObject) -> MDataHandle:
        """child(MObject) -> MDataHandle"""
    def copy(self, src: MDataHandle) -> MDataHandle:
        """Copies the attribute from the src attribute to the attribute referenced by this handle.  This is the only method which can completely copy a compound attribute from one handle to another.  The construct outputHandle.set (inputHandle.data()) will not work for compound or multi attributes."""
    def copyWritable(self, src: MDataHandle) -> MDataHandle:
        """Copies the attribute from the <i>src</i> attribute to the attribute referenced by this handle.  When the copy is made it ensures that the data in this handle is writable. That is, if the src handle has a writable copy of the data then it will be duplicated, otherwise this handle will claim the writer status for the data."""
    def data(self) -> MObject:
        """Returns the data object from this handle.  The object returned should be used with the appropriate data function set.  This method is not valid for simple numeric types."""
    def datablock(self) -> MDataBlock:
        """Returns a reference to the datablock assigned to this data handle."""
    def geometryTransformMatrix(self) -> MMatrix:
        """This method returns a reference to the local-to-world transformation matrix that can accompany a geometry data object.  Only use this method on handles to geometry data (curves, surfaces, and meshes)."""
    def isGeneric(self, isNumeric: bool, isNull: bool) -> Any:
        """Returns True if this handle is for generic data.  There are 2 forms of generic data.  The first is for simple data and is used if the isNumeric parameter returns True.  In this case, the asGeneric*() and setGeneric*() methods of this class are used to query and set values."""
    def isNumeric(self) -> bool:
        """Returns True if this handle is for simple numeric data. That means that the numeric data is directly accessible through the non-generic as*() and set*() methods of this handle. For example, depending on handle initialization, the asBool() may be called but the asGenericBool() should not be called."""
    def numericType(self) -> int:
        """Returns the type of data represented by this handle.  This method is only valid for data handles of simple numeric types."""
    def set2Double(self, float: Any, float_: Any) -> MDataHandle:
        """Set the data that this handle represents in the data block."""
    def set2Float(self, float: Any, float_: Any) -> MDataHandle:
        """Set the data that this handle represents in the data block."""
    def set2Int(self, int: Any, int_: Any) -> MDataHandle:
        """Set the data that this handle represents in the data block."""
    def set2Short(self, int: Any, int_: Any) -> MDataHandle:
        """Set the data that this handle represents in the data block."""
    def set3Double(self, float: Any, float_: Any, float__: Any) -> MDataHandle:
        """Set the data that this handle represents in the data block."""
    def set3Float(self, float: Any, float_: Any, float__: Any) -> MDataHandle:
        """Set the data that this handle represents in the data block."""
    def set3Int(self, int: Any, int_: Any, int__: Any) -> MDataHandle:
        """Set the data that this handle represents in the data block."""
    def set3Short(self, int: Any, int_: Any, int__: Any) -> MDataHandle:
        """Set the data that this handle represents in the data block."""
    def set4Double(self, float: Any, float_: Any, float__: Any, float___: Any) -> MDataHandle:
        """Set the data that this handle represents in the data block."""
    def setBool(self, value: bool) -> None:
        """Set the data that this handle represents in the data block."""
    def setChar(self, int: Any) -> MDataHandle:
        """Set the data that this handle represents in the data block."""
    def setClean(self) -> MDataHandle:
        """Marks the data that is represented by this handle as being clean.  This should be done after recalculating the data from the inputs."""
    def setDouble(self, value: float) -> None:
        """Set the data that this handle represents in the data block."""
    def setFloat(self, value: float) -> None:
        """Set the data that this handle represents in the data block."""
    def setGenericBool(self, bool: bool, force: bool) -> MDataHandle:
        """Set the data that this handle represents in the data block."""
    def setGenericChar(self, int: Any, force: bool) -> MDataHandle:
        """Set the data that this handle represents in the data block."""
    def setGenericDouble(self, float: float, force: bool) -> MDataHandle:
        """Set the data that this handle represents in the data block."""
    def setGenericFloat(self, float: float, force: bool) -> MDataHandle:
        """Set the data that this handle represents in the data block."""
    def setGenericInt(self, int: int, force: bool) -> MDataHandle:
        """Set the data that this handle represents in the data block."""
    def setGenericShort(self, int: Any, force: bool) -> MDataHandle:
        """Set the data that this handle represents in the data block."""
    def setInt(self, value: int) -> None:
        """Set the data that this handle represents in the data block."""
    def setMAngle(self, MAngle: Any) -> MDataHandle:
        """Set the data that this handle represents in the data block."""
    def setMDistance(self, MDistance: Any) -> MDataHandle:
        """Set the data that this handle represents in the data block."""
    def setMFloatMatrix(self, MFloatMatrix: Any) -> MDataHandle:
        """Set the data that this handle represents in the data block."""
    def setMFloatVector(self, MFloatVector: Any) -> MDataHandle:
        """Set the data that this handle represents in the data block."""
    def setMMatrix(self, MMatrix: Any) -> MDataHandle:
        """Set the data that this handle represents in the data block."""
    def setMObject(self, value: MObject) -> None:
        """Set the data that this handle represents in the data block.  This method assumes that the MObject is a dependency graph data object.  These objects can be created using the appropriate MFn..Data function set."""
    def setMPxData(self, MPxData: Any) -> MDataHandle:
        """Set the data that this handle represents in the data block.  This method takes a pointer to a user defined data object.  The data block will become the new owner of the data object that you pass in.  Do not delete it."""
    def setMTime(self, MTime: Any) -> MDataHandle:
        """Set the data that this handle represents in the data block."""
    def setMVector(self, MVector: Any) -> MDataHandle:
        """Set the data that this handle represents in the data block."""
    def setShort(self, int: Any) -> MDataHandle:
        """Set the data that this handle represents in the data block."""
    def setString(self, value: Any) -> None:
        """Set the data that this handle represents in the data block."""
    def type(self) -> int:
        """Returns the type of data represented by this handle."""
    def typeId(self) -> MTypeId:
        """Returns the type of data represented by this handle as a type id.  A type id is a four character code that is used to identify the data type."""

class MDistance:
    kCentimeters: Any
    kFeet: Any
    kInches: Any
    kInvalid: Any
    kKilometers: Any
    kLast: Any
    kMeters: Any
    kMiles: Any
    kMillimeters: Any
    kYards: Any
    unit: Any
    value: Any
    def __init__(self, value: float | MDistance | None = None, unitSystem: Any = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def asCentimeters(self) -> float:
        """Return the distance value, converted to centimeters."""
    def asFeet(self) -> float:
        """Return the distance value, converted to feet."""
    def asInches(self) -> float:
        """Return the distance value, converted to inches."""
    def asKilometers(self) -> float:
        """Return the distance value, converted to kilometers."""
    def asMeters(self) -> float:
        """Return the distance value, converted to meters."""
    def asMiles(self) -> float:
        """Return the distance value, converted to miles."""
    def asMillimeters(self) -> float:
        """Return the distance value, converted to millimeters."""
    def asUnits(self, newUnit: Any) -> float:
        """Return the distance value, converted to the specified units."""
    def asYards(self) -> float:
        """Return the distance value, converted to yards."""
    @staticmethod
    def internalToUI(internalValue: float) -> float:
        """Convert a value from Maya's internal units to the units used in the UI."""
    @staticmethod
    def internalUnit() -> Any:
        """Return the distance unit used internally by Maya."""
    @staticmethod
    def setUIUnit(newUnit: Any) -> None:
        """Change the units used to display distances in Maya's UI."""
    @staticmethod
    def uiToInternal(uiValue: float) -> float:
        """Convert a value from the units used in the UI to Maya's internal units."""
    @staticmethod
    def uiUnit() -> Any:
        """Return the units used to display distances in Maya's UI."""

class MDoubleArray:
    sizeIncrement: Any
    def __init__(self, other: MDoubleArray | int | None = None, initialValue: float | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def append(self, element: float) -> None:
        """Add a value to the end of the array."""
    def clear(self) -> None:
        """Remove all elements from the array."""
    def copy(self, source: MDoubleArray) -> None:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self, element: float, index: int) -> None:
        """Insert a new value into the array at the given index."""
    def remove(self, index: int) -> None:
        """Remove an element from the array."""
    def setLength(self, length: int) -> None:
        """Grow or shrink the array to contain a specific number of elements."""

class MEulerRotation:
    kIdentity: Any
    kTolerance: Any
    kXYZ: Any
    kXZY: Any
    kYXZ: Any
    kYZX: Any
    kZXY: Any
    kZYX: Any
    order: Any
    x: Any
    y: Any
    z: Any
    def __init__(self, src: MEulerRotation | MVector | float | None = None, ord: Any = None, zz: float | None = None, ord_: Any = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def alternateSolution(self, src: MEulerRotation | None = None) -> MEulerRotation:
        """Returns an equivalent rotation which is not simply a multiple."""
    def asMatrix(self) -> MMatrix:
        """Returns the rotation as an equivalent matrix."""
    def asQuaternion(self) -> MQuaternion:
        """Returns the rotation as an equivalent quaternion."""
    def asVector(self) -> MVector:
        """Returns the X, Y and Z rotations as a vector."""
    def bound(self, src: MEulerRotation | None = None) -> MEulerRotation:
        """Returns a new MEulerRotation having this rotation, but with each rotation component bound within +/- PI."""
    def boundIt(self, src: MEulerRotation | None = None) -> MEulerRotation:
        """In-place bounding of each rotation component to lie wthin +/- PI."""
    def closestCut(self, dst: MEulerRotation, dst_: MEulerRotation) -> MEulerRotation:
        """Returns the rotation which is full spin multiples of this one and comes closest to target."""
    def closestSolution(self, dst: MEulerRotation, dst_: MEulerRotation) -> MEulerRotation:
        """Returns the equivalent rotation which comes closest to a target."""
    @staticmethod
    def computeAlternateSolution(*args: Any, **kwargs: Any) -> Any:
        """Returns an equivalent rotation which is not simply a multiple."""
    @staticmethod
    def computeBound(*args: Any, **kwargs: Any) -> Any:
        """Returns an equivalent rotation with each rotation component bound within +/- PI."""
    @staticmethod
    def computeClosestCut(*args: Any, **kwargs: Any) -> Any:
        """Returns the rotation which is full spin multiples of the src and comes closest to target."""
    @staticmethod
    def computeClosestSolution(*args: Any, **kwargs: Any) -> Any:
        """Returns the equivalent rotation which comes closest to a target."""
    @staticmethod
    def decompose(matrix: MMatrix, ord: Any) -> MEulerRotation:
        """Extracts a rotation from a matrix."""
    def incrementalRotateBy(self, axis: MVector, angle: float) -> MEulerRotation:
        """Increase this rotation by a given angle around the specified axis. The update is done in series of small increments to avoid flipping."""
    def inverse(self) -> MEulerRotation:
        """Returns a new MEulerRotation containing the inverse rotation of this one and reversed rotation order."""
    def invertIt(self) -> MEulerRotation:
        """In-place inversion of the rotation. Rotation order is also reversed."""
    def isEquivalent(self, other: MEulerRotation, tolerance: float | None = None) -> bool:
        """Returns true if this rotation has the same order as another and their X, Y and Z components are within a tolerance of each other."""
    def isZero(self, tolerance: float | None = None) -> bool:
        """Returns true if the X, Y and Z components are each within a tolerance of 0.0."""
    def reorder(self, ord: Any) -> MEulerRotation:
        """Returns a new MEulerRotation having this rotation, reordered to use the given rotation order."""
    def reorderIt(self, ord: Any) -> MEulerRotation:
        """In-place reordering to use the given rotation order."""
    def setToAlternateSolution(self, src: MEulerRotation | None = None) -> MEulerRotation:
        """Replace this rotation with an alternate solution."""
    def setToClosestCut(self, src: MEulerRotation, dst: MEulerRotation) -> MEulerRotation:
        """Replace this rotation with the closest cut to a target."""
    def setToClosestSolution(self, src: MEulerRotation, dst: MEulerRotation) -> MEulerRotation:
        """Replace this rotation with the closest solution to a target."""
    def setValue(self, v: MVector | float, zz: float, ord: Any = None, ord_: Any = None) -> MEulerRotation:
        """Set the rotation."""

class MEvaluationNode:
    def __init__(self, evalNode: MEvaluationNode) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def datablock(self) -> MDataBlock:
        """Returns the datablock for this node."""
    def dependencyNode(self) -> MObject:
        """Returns the dependency node this evaluation node represents."""
    def dirtyPlug(self, attribute: MObject) -> MPlug:
        """Returns the top-most plug for the specified attribute if the attribute has dirty plugs. This call should be made from MPxNode::preEvaluation() and MPxNode::postEvaluation() to access a networked plug which is going to be dirty and computed."""
    def dirtyPlugExists(self, attribute: MObject) -> bool:
        """Returns true if the specified attribute has a dirty plug. This call should be made from MPxNode::preEvaluation() and MPxNode::postEvaluation() to verify which plugs are going to be dirty and computed."""
    def iterator(self) -> MEvaluationNodeIterator:
        """Returns an iterator at the beginning of the dirty plug list."""

class MEvaluationNodeIterator:
    def __init__(self, node: MEvaluationNode | MEvaluationNodeIterator | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def isDone(self) -> bool:
        """Checks to see if the iterator has reached the end of the iteration."""
    def next(self) -> None:
        """Advances the iterator to the next position in the dirty plug list."""
    def plug(self) -> MPlug:
        """Returns the dirty plug at the current iterator position. Returns an empty plug if the iterator is illegal."""
    def reset(self) -> None:
        """Resets the iterator to the first position in the dirty plug list."""

class MEventMessage:
    kDefaultAction: Any
    kDoAction: Any
    kDoNotDoAction: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def addEventCallback(eventName: Any, function: int, clientData: None = None) -> int:
        """This method registers a callback for event occurred messages."""
    @staticmethod
    def currentCallbackId() -> int:
        """Returns the callback ID of the currently executing callback. If called"""
    @staticmethod
    def getEventNames(arg: Any, string: Any, arg_: Any) -> Any:
        """This method returns the list of available event names."""
    @staticmethod
    def nodeCallbacks(node: Any) -> int:
        """Returns a list of callback IDs registered to a given node."""
    @staticmethod
    def removeCallback(id: Any) -> None:
        """Removes the specified callback from Maya."""
    @staticmethod
    def removeCallbacks(ids: Any) -> None:
        """Removes all of the specified callbacks from Maya."""

class MExternalContentInfoTable:
    def __init__(self, data: None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addResolvedEntry(self, key: Any, unresolvedLocation: Any, resolvedLocation: Any, contextNodeFullName: Any, roles: Any) -> MExternalContentInfoTable:
        """Add an entry in the table."""
    def addUnresolvedEntry(self, key: Any, unresolvedLocation: Any, contextNodeFullName: Any, roles: Any = None) -> MExternalContentInfoTable:
        """Add an entry in the table. The resolved location will be inferred from the application's built-in file resolving for the specified file type. This will automatically add entries into the roles vector that correspond to the search rules for this file type."""
    def getEntry(self, index: int) -> Any:
        """Retrieves external content entry based on its position in the table."""
    def getInfo(self, key: Any) -> Any:
        """Retrieves external content information based on its key."""

class MExternalContentLocationTable:
    def __init__(self, data: Any = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addEntry(self, key: Any, location: Any) -> MExternalContentLocationTable:
        """Adds an external content location and its key to the table."""
    def getEntry(self, index: int) -> Any:
        """Retrieves external content entry based on its position in the table."""
    def getLocation(self, key: Any) -> Any:
        """Retrieves an entry's location based on the associated key."""

class MFileObject:
    kBaseName: Any
    kDirMap: Any
    kExact: Any
    kInputFile: Any
    kInputReference: Any
    kNone: Any
    kReferenceMappings: Any
    kRelative: Any
    kStrict: Any
    resolveMethod: Any
    def __init__(self, other: MFileObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def copy(self, source: Any) -> MFileObject:
        """Copy data from source file object."""
    def exists(self, index: int | None = None) -> bool:
        """Checks to see if the file exists and is readable."""
    def expandedFullName(self) -> Any:
        """Returns the pathname of a file constructed from the unresolved file object values. The file name will consist of the the expanded raw path and raw name elements."""
    def expandedPath(self) -> Any:
        """Returns the raw path element of the unresolved file object with all environment variables expanded. In the case that the path expands to multiple paths, the first expanded path will be returned."""
    def fullName(self, index: Any) -> Any:
        """Returns the pathname of a file constructed from the indicated portion of the path element and filename element."""
    @staticmethod
    def getResolvedFullName(rawFullName: Any) -> Any:
        """Returns the full path to the resolved file, or an empty string if the resolution was unsuccessful."""
    @staticmethod
    def getResolvedFullNameAndExistsStatus(rawFullName: Any, method: Any, bool: Any) -> Any:
        """Returns the full path to the resolved file, or an empty string if the resolution was unsuccessful, and a boolean that indicate if the resolved path exists or not."""
    @staticmethod
    def isAbsolutePath(fileName: Any) -> bool:
        """Checks a file path string and determines if it represents an absolute file path. An absolute path can uniquely identify a directory or file."""
    def isSet(self) -> bool:
        """Checks to see if both file and path elements of the file object have been set."""
    def overrideResolvedFullName(self, fullFileName: Any, reresolveType: bool = False) -> MFileObject:
        """Normally when a raw file name is set, Maya will perform a series of operations on it in an attempt to resolve it to a valid file name. This final resolved file name can be accessed through the resolvedName(), resolvedPath(), and resolvedFullFileName() methods and can be quite different from the originally specified raw file name."""
    def path(self, index: Any) -> Any:
        """Returns the indicated portion of the path element of the file object.  All variables in the path element are expanded, and the portion indicated by the argument is extracted and returned."""
    def pathCount(self) -> int:
        """Returns the number of paths in the path element of the file object."""
    def rawFullName(self) -> Any:
        """Returns the unresolved full file name (path plus filename) of the MFileObject with all environment variables unexpanded."""
    def rawName(self) -> Any:
        """Returns the unresolved filename element of the MFileObject."""
    def rawPath(self) -> Any:
        """Returns the path element of the MFileObject with all environment variables unexpanded."""
    def rawURI(self) -> MURI:
        """Returns the unresolved URI of the MFileObject, if any."""
    def resolvedFullName(self) -> Any:
        """Returns the first pathname of a file constructed from the path and filename elements.  All variables in the path element are expanded, and the first path (the part before the first ':' in the path) is prepended to the filename element. After expanding all environment	variables Maya may then perform additional modifications, such	as prepending directories to a relative path name, in order to resolve the path to a valid location on disk."""
    def resolvedName(self) -> Any:
        """Returns the resolved filename element of the file object."""
    def resolvedPath(self) -> Any:
        """Returns the resolved path element of the file object. In order to build the resolved path, Maya first expands all environment variables and then may perform additional modifications, such as prepending directories to a relative path name, in order to resolve the path to a valid location on disk."""
    def setRawFullName(self, fullFileName: Any) -> MFileObject:
        """This method combines the functions of the setRawName and setRawPath methods in that it sets both the path and filename from the given name."""
    def setRawName(self, fileName: Any) -> MFileObject:
        """Set the unresolved filename element of the MFileObject instance.  This name should not contain any '/' characters, it should indicate simply the name of a file.  The directories in which this name will be searched for are specified by setRawPath."""
    def setRawPath(self, pathName: Any) -> MFileObject:
        """Set the unresolved path element of the MFileObject instance.  This should contain a list of directories, each separated by a single ':' character.  The pathnames can contain Unix environment variables in the form $VARNAME.  These will be expanded when paths to actual filenames are constructed."""
    def setRawURI(self, uri: Any) -> MFileObject:
        """Set the unresolved URI of the MFileObject instance."""

class MFloatArray:
    sizeIncrement: Any
    def __init__(self, other: MFloatArray | int | None = None, initialValue: float | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def append(self, element: float) -> None:
        """Add a value to the end of the array."""
    def clear(self) -> None:
        """Remove all elements from the array."""
    def copy(self, source: MFloatArray) -> None:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self, element: float, index: int) -> None:
        """Insert a new value into the array at the given index."""
    def remove(self, index: int) -> None:
        """Remove an element from the array."""
    def setLength(self, length: int) -> None:
        """Grow or shrink the array to contain a specific number of elements."""

class MFloatMatrix:
    kTolerance: Any
    def __init__(self, src: MFloatMatrix | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def adjoint(self) -> MFloatMatrix:
        """Returns a new matrix containing this matrix's adjoint."""
    def det3x3(self) -> float:
        """Returns the determinant of the 3x3 matrix formed by the first 3 elements of the first 3 rows of this matrix."""
    def det4x4(self) -> float:
        """Returns this matrix's determinant."""
    def getElement(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the matrix element for the specified row and column."""
    def homogenize(self) -> MFloatMatrix:
        """Returns a new matrix containing the homogenized version of this matrix."""
    def inverse(self) -> MFloatMatrix:
        """Returns a new matrix containing this matrix's inverse."""
    def isEquivalent(self, other: MFloatMatrix, tolerance: float | None = None) -> bool:
        """Test for equivalence of two matrices, within a tolerance."""
    def setElement(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the matrix element for the specified row and column."""
    def setToIdentity(self) -> MFloatMatrix:
        """Sets this matrix to the identity."""
    def setToProduct(self, left: MFloatMatrix, right: MFloatMatrix) -> MFloatMatrix:
        """Sets this matrix to the product of the two matrices passed in."""
    def transpose(self) -> MFloatMatrix:
        """Returns a new matrix containing this matrix's transpose."""

class MFloatPoint:
    kOrigin: Any
    kTolerance: Any
    w: Any
    x: Any
    y: Any
    z: Any
    def __init__(self, srcpt: MFloatPoint | MPoint | MFloatVector | MVector | float | None = None, yy: float | None = None, zz: float | None = None, ww: float | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def cartesianize(self) -> MFloatPoint:
        """Convert point to cartesian form."""
    def distanceTo(self, other: MFloatPoint) -> float:
        """Return distance between this point and another."""
    def homogenize(self) -> MFloatPoint:
        """Convert point to homogenous form."""
    def isEquivalent(self, other: MFloatPoint, tolerance: float | None = None) -> bool:
        """Test for equivalence of two points, within a tolerance."""
    def rationalize(self) -> MFloatPoint:
        """Convert point to rational form."""

class MFloatPointArray:
    sizeIncrement: Any
    def __init__(self, other: MFloatPointArray | int | None = None, initialValue: MFloatPoint | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def append(self, element: MFloatPoint | float, y: float, z: float | None = None, w: float | None = None) -> None:
        """Add a value to the end of the array."""
    def clear(self) -> None:
        """Remove all elements from the array."""
    def copy(self, source: MFloatPointArray) -> None:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self, element: MFloatPoint, index: int) -> None:
        """Insert a new value into the array at the given index."""
    def remove(self, index: int) -> None:
        """Remove an element from the array."""
    def setLength(self, length: int) -> None:
        """Grow or shrink the array to contain a specific number of elements."""

class MFloatVector:
    kOneVector: Any
    kTolerance: Any
    kXaxisVector: Any
    kXnegAxisVector: Any
    kYaxisVector: Any
    kYnegAxisVector: Any
    kZaxisVector: Any
    kZeroVector: Any
    kZnegAxisVector: Any
    x: Any
    y: Any
    z: Any
    def __init__(self, xx: float | None = None, yy: float | None = None, zz: float | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def angle(self, other: MFloatVector) -> float:
        """Returns the angle, in radians, between this vector and another."""
    def isEquivalent(self, other: MFloatVector, tolerance: float | None = None) -> bool:
        """Returns True if this vector and another are within a given tolerance of being equal."""
    def isParallel(self, other: MFloatVector, tolerance: float | None = None) -> bool:
        """Returns True if this vector and another are within the given tolerance of being parallel."""
    def length(self) -> float:
        """Returns the magnitude of this vector."""
    def normal(self) -> MFloatVector:
        """Returns a new vector containing the normalized version of this one."""
    def normalize(self) -> None:
        """Normalizes this vector in-place and returns a new reference to it."""
    def transformAsNormal(self, matrix: MFloatMatrix) -> MFloatVector:
        """Returns a new vector which is calculated by postmultiplying this vector by the transpose of the given matrix and then normalizing the result."""

class MFloatVectorArray:
    sizeIncrement: Any
    def __init__(self, other: MFloatVectorArray | int | None = None, initialValue: MFloatVector | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def append(self, element: MFloatVector) -> None:
        """Add a value to the end of the array."""
    def clear(self) -> None:
        """Remove all elements from the array."""
    def copy(self, source: MFloatVectorArray) -> None:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self, element: MFloatVector, index: int) -> None:
        """Insert a new value into the array at the given index."""
    def remove(self, index: int) -> None:
        """Remove an element from the array."""
    def setLength(self, length: int) -> None:
        """Grow or shrink the array to contain a specific number of elements."""

class MFn:
    kACos: Any
    kAISEnvFacade: Any
    kASin: Any
    kATan: Any
    kATan2: Any
    kAbsolute: Any
    kAddDoubleLinear: Any
    kAdskMaterial: Any
    kAffect: Any
    kAimConstraint: Any
    kAimMatrix: Any
    kAir: Any
    kAlignCurve: Any
    kAlignManip: Any
    kAlignSurface: Any
    kAmbientLight: Any
    kAnd: Any
    kAngle: Any
    kAngleBetween: Any
    kAngleToDoubleNode: Any
    kAnimBlend: Any
    kAnimBlendInOut: Any
    kAnimCurve: Any
    kAnimCurveTimeToAngular: Any
    kAnimCurveTimeToDistance: Any
    kAnimCurveTimeToTime: Any
    kAnimCurveTimeToUnitless: Any
    kAnimCurveUnitlessToAngular: Any
    kAnimCurveUnitlessToDistance: Any
    kAnimCurveUnitlessToTime: Any
    kAnimCurveUnitlessToUnitless: Any
    kAnimLayer: Any
    kAnisotropy: Any
    kAnnotation: Any
    kAnyGeometryVarGroup: Any
    kArcLength: Any
    kAreaLight: Any
    kArrayMapper: Any
    kArrowManip: Any
    kArubaTesselate: Any
    kAssembly: Any
    kAsset: Any
    kAttachCurve: Any
    kAttachSurface: Any
    kAttribute: Any
    kAttribute2Double: Any
    kAttribute2Float: Any
    kAttribute2Int: Any
    kAttribute2Short: Any
    kAttribute3Double: Any
    kAttribute3Float: Any
    kAttribute3Int: Any
    kAttribute3Short: Any
    kAttribute4Double: Any
    kAudio: Any
    kAverage: Any
    kAverageCurveManip: Any
    kAvgCurves: Any
    kAvgNurbsSurfacePoints: Any
    kAvgSurfacePoints: Any
    kAxesActionManip: Any
    kAxisFromMatrix: Any
    kBackground: Any
    kBallProjectionManip: Any
    kBarnDoorManip: Any
    kBase: Any
    kBaseLattice: Any
    kBendLattice: Any
    kBevel: Any
    kBevelManip: Any
    kBevelPlus: Any
    kBezierCurve: Any
    kBezierCurveData: Any
    kBezierCurveToNurbs: Any
    kBinaryData: Any
    kBirailSrf: Any
    kBlend: Any
    kBlendColorSet: Any
    kBlendColors: Any
    kBlendDevice: Any
    kBlendFalloff: Any
    kBlendManip: Any
    kBlendMatrix: Any
    kBlendNodeAdditiveRotation: Any
    kBlendNodeAdditiveScale: Any
    kBlendNodeBase: Any
    kBlendNodeBoolean: Any
    kBlendNodeDouble: Any
    kBlendNodeDoubleAngle: Any
    kBlendNodeDoubleLinear: Any
    kBlendNodeEnum: Any
    kBlendNodeFloat: Any
    kBlendNodeFloatAngle: Any
    kBlendNodeFloatLinear: Any
    kBlendNodeInt16: Any
    kBlendNodeInt32: Any
    kBlendNodeTime: Any
    kBlendShape: Any
    kBlendTwoAttr: Any
    kBlendWeighted: Any
    kBlindData: Any
    kBlindDataTemplate: Any
    kBlinn: Any
    kBlinnMaterial: Any
    kBoundary: Any
    kBox: Any
    kBoxData: Any
    kBrownian: Any
    kBrush: Any
    kBulge: Any
    kBulgeLattice: Any
    kBump: Any
    kBump3d: Any
    kButtonManip: Any
    kCacheBase: Any
    kCacheBlend: Any
    kCacheFile: Any
    kCacheTrack: Any
    kCacheableNode: Any
    kCaddyManipBase: Any
    kCamera: Any
    kCameraManip: Any
    kCameraPlaneManip: Any
    kCameraSet: Any
    kCameraView: Any
    kCeil: Any
    kCenterManip: Any
    kChainToSpline: Any
    kCharacter: Any
    kCharacterMap: Any
    kCharacterMappingData: Any
    kCharacterOffset: Any
    kChecker: Any
    kChoice: Any
    kChooser: Any
    kCircle: Any
    kCircleManip: Any
    kCirclePointManip: Any
    kCircleSweepManip: Any
    kClampColor: Any
    kClampRange: Any
    kClientDevice: Any
    kClip: Any
    kClipGhostShape: Any
    kClipLibrary: Any
    kClipScheduler: Any
    kClipToGhostData: Any
    kCloseCurve: Any
    kCloseSurface: Any
    kClosestPointOnMesh: Any
    kClosestPointOnSurface: Any
    kCloth: Any
    kCloud: Any
    kCluster: Any
    kClusterFilter: Any
    kClusterFlexor: Any
    kCoiManip: Any
    kCollision: Any
    kColorBackground: Any
    kColorMgtGlobals: Any
    kColorProfile: Any
    kColumnFromMatrix: Any
    kCombinationShape: Any
    kCommCornerManip: Any
    kCommCornerOperManip: Any
    kCommEdgeOperManip: Any
    kCommEdgePtManip: Any
    kCommEdgeSegmentManip: Any
    kComponent: Any
    kComponentFalloff: Any
    kComponentListData: Any
    kComponentManip: Any
    kComponentMatch: Any
    kComposeMatrix: Any
    kCompoundAttribute: Any
    kConcentricProjectionManip: Any
    kCondition: Any
    kCone: Any
    kConstraint: Any
    kContainer: Any
    kContainerBase: Any
    kContourProjectionManip: Any
    kContrast: Any
    kControl: Any
    kControllerTag: Any
    kCopyColorSet: Any
    kCopyUVSet: Any
    kCos: Any
    kCpManip: Any
    kCrater: Any
    kCreaseSet: Any
    kCreate: Any
    kCreateBPManip: Any
    kCreateBezierManip: Any
    kCreateCVManip: Any
    kCreateColorSet: Any
    kCreateEPManip: Any
    kCreateSectionManip: Any
    kCreateUVSet: Any
    kCrossProduct: Any
    kCrossSectionEditManip: Any
    kCrossSectionManager: Any
    kCubicProjectionManip: Any
    kCurve: Any
    kCurveCVComponent: Any
    kCurveCurveIntersect: Any
    kCurveEPComponent: Any
    kCurveEdManip: Any
    kCurveFromMeshCoM: Any
    kCurveFromMeshEdge: Any
    kCurveFromSubdivEdge: Any
    kCurveFromSubdivFace: Any
    kCurveFromSurface: Any
    kCurveFromSurfaceBnd: Any
    kCurveFromSurfaceCoS: Any
    kCurveFromSurfaceIso: Any
    kCurveInfo: Any
    kCurveKnotComponent: Any
    kCurveNormalizerAngle: Any
    kCurveNormalizerLinear: Any
    kCurveParamComponent: Any
    kCurveSegmentManip: Any
    kCurveVarGroup: Any
    kCustomEvaluatorClusterNode: Any
    kCylinder: Any
    kCylindricalProjectionManip: Any
    kDOF: Any
    kDPbirailSrf: Any
    kDagContainer: Any
    kDagNode: Any
    kDagPose: Any
    kDagSelectionItem: Any
    kData: Any
    kData2Double: Any
    kData2Float: Any
    kData2Int: Any
    kData2Short: Any
    kData3Double: Any
    kData3Float: Any
    kData3Int: Any
    kData3Short: Any
    kData4Double: Any
    kDblTrsManip: Any
    kDecayRegionCapComponent: Any
    kDecayRegionComponent: Any
    kDecomposeMatrix: Any
    kDefaultLightList: Any
    kDeformBend: Any
    kDeformBendManip: Any
    kDeformFlare: Any
    kDeformFlareManip: Any
    kDeformFunc: Any
    kDeformSine: Any
    kDeformSineManip: Any
    kDeformSquash: Any
    kDeformSquashManip: Any
    kDeformTwist: Any
    kDeformTwistManip: Any
    kDeformWave: Any
    kDeformWaveManip: Any
    kDeleteColorSet: Any
    kDeleteComponent: Any
    kDeleteUVSet: Any
    kDeltaMush: Any
    kDependencyNode: Any
    kDetachCurve: Any
    kDetachSurface: Any
    kDeterminant: Any
    kDiffuseMaterial: Any
    kDimension: Any
    kDimensionManip: Any
    kDirectedDisc: Any
    kDirectionManip: Any
    kDirectionalLight: Any
    kDiscManip: Any
    kDiskCache: Any
    kDispatchCompute: Any
    kDisplacementShader: Any
    kDisplayLayer: Any
    kDisplayLayerManager: Any
    kDistance: Any
    kDistanceBetween: Any
    kDistanceManip: Any
    kDivide: Any
    kDofManip: Any
    kDotProduct: Any
    kDoubleAngleAttribute: Any
    kDoubleArrayData: Any
    kDoubleIndexedComponent: Any
    kDoubleLinearAttribute: Any
    kDoubleShadingSwitch: Any
    kDoubleToAngleNode: Any
    kDrag: Any
    kDropOffFunction: Any
    kDropoffLocator: Any
    kDropoffManip: Any
    kDummy: Any
    kDummyConnectable: Any
    kDynAirManip: Any
    kDynArrayAttrsData: Any
    kDynAttenuationManip: Any
    kDynBase: Any
    kDynBaseFieldManip: Any
    kDynEmitterManip: Any
    kDynFieldsManip: Any
    kDynGlobals: Any
    kDynNewtonManip: Any
    kDynParticleSetComponent: Any
    kDynSpreadManip: Any
    kDynSweptGeometryData: Any
    kDynTurbulenceManip: Any
    kDynamicConstraint: Any
    kDynamicsController: Any
    kEdgeComponent: Any
    kEditCurve: Any
    kEditCurveManip: Any
    kEditMetadata: Any
    kEditsManager: Any
    kEmitter: Any
    kEnableManip: Any
    kEnumAttribute: Any
    kEnvBall: Any
    kEnvChrome: Any
    kEnvCube: Any
    kEnvFacade: Any
    kEnvFogMaterial: Any
    kEnvFogShape: Any
    kEnvSky: Any
    kEnvSphere: Any
    kEqual: Any
    kExplodeNurbsShell: Any
    kExpression: Any
    kExtendCurve: Any
    kExtendCurveDistanceManip: Any
    kExtendSurface: Any
    kExtendSurfaceDistanceManip: Any
    kExtract: Any
    kExtrude: Any
    kExtrudeManip: Any
    kFFD: Any
    kFFblendSrf: Any
    kFFfilletSrf: Any
    kFacade: Any
    kFalloffEval: Any
    kFfdDualBase: Any
    kField: Any
    kFileBackground: Any
    kFileTexture: Any
    kFilletCurve: Any
    kFilter: Any
    kFilterClosestSample: Any
    kFilterEuler: Any
    kFilterSimplify: Any
    kFitBspline: Any
    kFixedLineManip: Any
    kFlexor: Any
    kFloatAngleAttribute: Any
    kFloatArrayData: Any
    kFloatLinearAttribute: Any
    kFloatMatrixAttribute: Any
    kFloatVectorArrayData: Any
    kFloor: Any
    kFlow: Any
    kFluid: Any
    kFluidData: Any
    kFluidEmitter: Any
    kFluidGeom: Any
    kFluidTexture2D: Any
    kFluidTexture3D: Any
    kFollicle: Any
    kForceUpdateManip: Any
    kFosterParent: Any
    kFourByFourMatrix: Any
    kFractal: Any
    kFreePointManip: Any
    kFreePointTriadManip: Any
    kGammaCorrect: Any
    kGenericAttribute: Any
    kGeoConnectable: Any
    kGeoConnector: Any
    kGeomBind: Any
    kGeometric: Any
    kGeometryConstraint: Any
    kGeometryData: Any
    kGeometryFilt: Any
    kGeometryOnLineManip: Any
    kGeometryVarGroup: Any
    kGlobalCacheControls: Any
    kGlobalStitch: Any
    kGranite: Any
    kGravity: Any
    kGreasePencilSequence: Any
    kGreasePlane: Any
    kGreasePlaneRenderShape: Any
    kGreaterThan: Any
    kGrid: Any
    kGroundPlane: Any
    kGroupId: Any
    kGroupParts: Any
    kGuide: Any
    kGuideLine: Any
    kHairConstraint: Any
    kHairSystem: Any
    kHairTubeShader: Any
    kHandleRotateManip: Any
    kHardenPointCurve: Any
    kHardwareReflectionMap: Any
    kHardwareRenderGlobals: Any
    kHardwareRenderingGlobals: Any
    kHeightField: Any
    kHikEffector: Any
    kHikFKJoint: Any
    kHikFloorContactMarker: Any
    kHikGroundPlane: Any
    kHikHandle: Any
    kHikIKEffector: Any
    kHikSolver: Any
    kHistorySwitch: Any
    kHsvToRgb: Any
    kHwShaderNode: Any
    kHyperGraphInfo: Any
    kHyperLayout: Any
    kHyperLayoutDG: Any
    kHyperView: Any
    kIkEffector: Any
    kIkHandle: Any
    kIkRPManip: Any
    kIkSolver: Any
    kIkSplineManip: Any
    kIkSystem: Any
    kIllustratorCurve: Any
    kImageAdd: Any
    kImageBlur: Any
    kImageColorCorrect: Any
    kImageData: Any
    kImageDepth: Any
    kImageDiff: Any
    kImageDisplay: Any
    kImageFilter: Any
    kImageLoad: Any
    kImageMotionBlur: Any
    kImageMultiply: Any
    kImageNetDest: Any
    kImageNetSrc: Any
    kImageOver: Any
    kImagePlane: Any
    kImageRender: Any
    kImageSave: Any
    kImageSource: Any
    kImageUnder: Any
    kImageView: Any
    kImplicitCone: Any
    kImplicitSphere: Any
    kInsertKnotCrv: Any
    kInsertKnotSrf: Any
    kInstancer: Any
    kInt64ArrayData: Any
    kIntArrayData: Any
    kIntersectSurface: Any
    kInvalid: Any
    kInverseLinearInterpolation: Any
    kIsoparmComponent: Any
    kIsoparmManip: Any
    kItemList: Any
    kJiggleDeformer: Any
    kJoint: Any
    kJointCluster: Any
    kJointClusterManip: Any
    kJointTranslateManip: Any
    kKeyframeDelta: Any
    kKeyframeDeltaAddRemove: Any
    kKeyframeDeltaBlockAddRemove: Any
    kKeyframeDeltaBreakdown: Any
    kKeyframeDeltaInfType: Any
    kKeyframeDeltaMove: Any
    kKeyframeDeltaScale: Any
    kKeyframeDeltaTangent: Any
    kKeyframeDeltaWeighted: Any
    kKeyframeRegionManip: Any
    kKeyingGroup: Any
    kLambert: Any
    kLambertMaterial: Any
    kLattice: Any
    kLatticeComponent: Any
    kLatticeData: Any
    kLatticeGeom: Any
    kLayeredShader: Any
    kLayeredTexture: Any
    kLeastSquares: Any
    kLeather: Any
    kLength: Any
    kLessThan: Any
    kLight: Any
    kLightDataAttribute: Any
    kLightFogMaterial: Any
    kLightInfo: Any
    kLightLink: Any
    kLightList: Any
    kLightManip: Any
    kLightProjectionGeometry: Any
    kLightSource: Any
    kLightSourceMaterial: Any
    kLimitManip: Any
    kLineArrowManip: Any
    kLineManip: Any
    kLineModifier: Any
    kLinearInterpolation: Any
    kLinearLight: Any
    kLocator: Any
    kLodGroup: Any
    kLodThresholds: Any
    kLog: Any
    kLookAt: Any
    kLuminance: Any
    kMCsolver: Any
    kMPbirailSrf: Any
    kMakeGroup: Any
    kMandelbrot: Any
    kMandelbrot3D: Any
    kManip2DContainer: Any
    kManipContainer: Any
    kManipulator: Any
    kManipulator2D: Any
    kManipulator3D: Any
    kMarble: Any
    kMarker: Any
    kMarkerManip: Any
    kMaterial: Any
    kMaterialFacade: Any
    kMaterialInfo: Any
    kMaterialTemplate: Any
    kMatrixAdd: Any
    kMatrixArrayData: Any
    kMatrixAttribute: Any
    kMatrixData: Any
    kMatrixFloatData: Any
    kMatrixHold: Any
    kMatrixMult: Any
    kMatrixPass: Any
    kMatrixWtAdd: Any
    kMax: Any
    kMembrane: Any
    kMentalRayTexture: Any
    kMergeVertsToolManip: Any
    kMesh: Any
    kMeshComponent: Any
    kMeshData: Any
    kMeshEdgeComponent: Any
    kMeshFaceVertComponent: Any
    kMeshFrEdgeComponent: Any
    kMeshGeom: Any
    kMeshMapComponent: Any
    kMeshPolygonComponent: Any
    kMeshVarGroup: Any
    kMeshVertComponent: Any
    kMeshVtxFaceComponent: Any
    kMessageAttribute: Any
    kMidModifier: Any
    kMidModifierWithMatrix: Any
    kMin: Any
    kModel: Any
    kModifyEdgeBaseManip: Any
    kModifyEdgeCrvManip: Any
    kModifyEdgeManip: Any
    kModulo: Any
    kMorph: Any
    kMotionPath: Any
    kMotionPathManip: Any
    kMountain: Any
    kMoveUVShellManip2D: Any
    kMoveVertexManip: Any
    kMultDoubleLinear: Any
    kMultiSubVertexComponent: Any
    kMultilisterLight: Any
    kMultiply: Any
    kMultiplyDivide: Any
    kMultiplyPointByMatrix: Any
    kMultiplyVectorByMatrix: Any
    kMute: Any
    kNBase: Any
    kNCloth: Any
    kNComponent: Any
    kNId: Any
    kNIdData: Any
    kNLE: Any
    kNObject: Any
    kNObjectData: Any
    kNParticle: Any
    kNRigid: Any
    kNamedObject: Any
    kNearestPointOnCurve: Any
    kNegate: Any
    kNewton: Any
    kNodeGraphEditorBookmarkInfo: Any
    kNodeGraphEditorBookmarks: Any
    kNodeGraphEditorInfo: Any
    kNoise: Any
    kNonAmbientLight: Any
    kNonDagSelectionItem: Any
    kNonExtendedLight: Any
    kNonLinear: Any
    kNormalConstraint: Any
    kNormalize: Any
    kNot: Any
    kNucleus: Any
    kNumericAttribute: Any
    kNumericData: Any
    kNurbsBoolean: Any
    kNurbsCircular2PtArc: Any
    kNurbsCircular3PtArc: Any
    kNurbsCube: Any
    kNurbsCurve: Any
    kNurbsCurveData: Any
    kNurbsCurveGeom: Any
    kNurbsCurveToBezier: Any
    kNurbsPlane: Any
    kNurbsSquare: Any
    kNurbsSurface: Any
    kNurbsSurfaceData: Any
    kNurbsSurfaceGeom: Any
    kNurbsTesselate: Any
    kNurbsToSubdiv: Any
    kObjectAttrFilter: Any
    kObjectBinFilter: Any
    kObjectFilter: Any
    kObjectMultiFilter: Any
    kObjectNameFilter: Any
    kObjectRenderFilter: Any
    kObjectScriptFilter: Any
    kObjectTypeFilter: Any
    kOcean: Any
    kOceanDeformer: Any
    kOceanShader: Any
    kOffsetCos: Any
    kOffsetCosManip: Any
    kOffsetCurve: Any
    kOffsetCurveManip: Any
    kOffsetSurface: Any
    kOffsetSurfaceManip: Any
    kOldGeometryConstraint: Any
    kOpaqueAttribute: Any
    kOpticalFX: Any
    kOr: Any
    kOrientConstraint: Any
    kOrientationComponent: Any
    kOrientationLocator: Any
    kOrientationMarker: Any
    kOrthoGrid: Any
    kPASolver: Any
    kPIConstant: Any
    kPairBlend: Any
    kParamDimension: Any
    kParentConstraint: Any
    kParentMatrix: Any
    kParticle: Any
    kParticleAgeMapper: Any
    kParticleCloud: Any
    kParticleColorMapper: Any
    kParticleIncandecenceMapper: Any
    kParticleSamplerInfo: Any
    kParticleTransparencyMapper: Any
    kPartition: Any
    kPassContributionMap: Any
    kPfxGeometry: Any
    kPfxHair: Any
    kPfxToon: Any
    kPhong: Any
    kPhongExplorer: Any
    kPhongMaterial: Any
    kPickMatrix: Any
    kPivotComponent: Any
    kPivotManip2D: Any
    kPlace2dTexture: Any
    kPlace3dTexture: Any
    kPlanarProjectionManip: Any
    kPlanarTrimSrf: Any
    kPlane: Any
    kPlugin: Any
    kPluginBlendShape: Any
    kPluginCameraSet: Any
    kPluginClientDevice: Any
    kPluginConstraintNode: Any
    kPluginData: Any
    kPluginDeformerNode: Any
    kPluginDependNode: Any
    kPluginEmitterNode: Any
    kPluginFieldNode: Any
    kPluginGeometryData: Any
    kPluginGeometryFilter: Any
    kPluginHardwareShader: Any
    kPluginHwShaderNode: Any
    kPluginIkSolver: Any
    kPluginImagePlaneNode: Any
    kPluginLocatorNode: Any
    kPluginManipContainer: Any
    kPluginManipulatorNode: Any
    kPluginMotionPathNode: Any
    kPluginObjectSet: Any
    kPluginParticleAttributeMapperNode: Any
    kPluginShape: Any
    kPluginSkinCluster: Any
    kPluginSpringNode: Any
    kPluginThreadedDevice: Any
    kPluginTransformNode: Any
    kPlusMinusAverage: Any
    kPointArrayData: Any
    kPointConstraint: Any
    kPointLight: Any
    kPointManip: Any
    kPointMatrixMult: Any
    kPointOnCurveInfo: Any
    kPointOnCurveManip: Any
    kPointOnLineManip: Any
    kPointOnPolyConstraint: Any
    kPointOnSurfaceInfo: Any
    kPointOnSurfaceManip: Any
    kPoleVectorConstraint: Any
    kPolyAppend: Any
    kPolyAppendVertex: Any
    kPolyArrow: Any
    kPolyAutoProj: Any
    kPolyAutoProjManip: Any
    kPolyAverageVertex: Any
    kPolyAxis: Any
    kPolyBevel: Any
    kPolyBevel2: Any
    kPolyBevel3: Any
    kPolyBlindData: Any
    kPolyBoolOp: Any
    kPolyBridgeEdge: Any
    kPolyCBoolOp: Any
    kPolyCaddyManip: Any
    kPolyChipOff: Any
    kPolyCircularize: Any
    kPolyClean: Any
    kPolyCloseBorder: Any
    kPolyCollapseEdge: Any
    kPolyCollapseF: Any
    kPolyColorDel: Any
    kPolyColorMod: Any
    kPolyColorPerVertex: Any
    kPolyComponentData: Any
    kPolyCone: Any
    kPolyConnectComponents: Any
    kPolyContourProj: Any
    kPolyCreaseEdge: Any
    kPolyCreateFacet: Any
    kPolyCreateToolManip: Any
    kPolyCreator: Any
    kPolyCube: Any
    kPolyCut: Any
    kPolyCutManip: Any
    kPolyCutManipContainer: Any
    kPolyCylProj: Any
    kPolyCylinder: Any
    kPolyDelEdge: Any
    kPolyDelFacet: Any
    kPolyDelVertex: Any
    kPolyDuplicateEdge: Any
    kPolyEdgeToCurve: Any
    kPolyEditEdgeFlow: Any
    kPolyExtrudeEdge: Any
    kPolyExtrudeFacet: Any
    kPolyExtrudeManip: Any
    kPolyExtrudeManipContainer: Any
    kPolyExtrudeVertex: Any
    kPolyFlipEdge: Any
    kPolyFlipUV: Any
    kPolyHelix: Any
    kPolyHoleFace: Any
    kPolyLayoutUV: Any
    kPolyMapCut: Any
    kPolyMapDel: Any
    kPolyMapSew: Any
    kPolyMapSewMove: Any
    kPolyMappingManip: Any
    kPolyMergeEdge: Any
    kPolyMergeFacet: Any
    kPolyMergeUV: Any
    kPolyMergeVert: Any
    kPolyMesh: Any
    kPolyMirror: Any
    kPolyMirrorManipContainer: Any
    kPolyModifierManip: Any
    kPolyModifierManipContainer: Any
    kPolyMoveEdge: Any
    kPolyMoveFacet: Any
    kPolyMoveFacetUV: Any
    kPolyMoveUV: Any
    kPolyMoveUVManip: Any
    kPolyMoveVertex: Any
    kPolyMoveVertexManip: Any
    kPolyMoveVertexUV: Any
    kPolyNormal: Any
    kPolyNormalPerVertex: Any
    kPolyNormalizeUV: Any
    kPolyPassThru: Any
    kPolyPinUV: Any
    kPolyPipe: Any
    kPolyPlanProj: Any
    kPolyPlatonicSolid: Any
    kPolyPoke: Any
    kPolyPokeManip: Any
    kPolyPrimitive: Any
    kPolyPrimitiveMisc: Any
    kPolyPrism: Any
    kPolyProj: Any
    kPolyProjectCurve: Any
    kPolyProjectionManip: Any
    kPolyPyramid: Any
    kPolyQuad: Any
    kPolyReFormManip: Any
    kPolyReFormManipContainer: Any
    kPolyReduce: Any
    kPolyRemesh: Any
    kPolySelectEditFeedbackManip: Any
    kPolySeparate: Any
    kPolySewEdge: Any
    kPolySmooth: Any
    kPolySmoothFacet: Any
    kPolySmoothProxy: Any
    kPolySoftEdge: Any
    kPolySphProj: Any
    kPolySphere: Any
    kPolySpinEdge: Any
    kPolySplit: Any
    kPolySplitEdge: Any
    kPolySplitRing: Any
    kPolySplitToolManip: Any
    kPolySplitVert: Any
    kPolyStraightenUVBorder: Any
    kPolySubdEdge: Any
    kPolySubdFacet: Any
    kPolyToSubdiv: Any
    kPolyToolFeedbackManip: Any
    kPolyToolFeedbackShape: Any
    kPolyTorus: Any
    kPolyTransfer: Any
    kPolyTriangulate: Any
    kPolyTweak: Any
    kPolyTweakUV: Any
    kPolyUVRectangle: Any
    kPolyUnite: Any
    kPolyUnsmooth: Any
    kPolyVertexNormalManip: Any
    kPolyWedgeFace: Any
    kPoseInterpolatorManager: Any
    kPositionMarker: Any
    kPostProcessList: Any
    kPower: Any
    kPrecompExport: Any
    kPrimitive: Any
    kPrimitiveFalloff: Any
    kProjectCurve: Any
    kProjectTangent: Any
    kProjectTangentManip: Any
    kProjection: Any
    kProjectionManip: Any
    kProjectionMultiManip: Any
    kProjectionUVManip: Any
    kPropModManip: Any
    kPropMoveTriadManip: Any
    kProximityFalloff: Any
    kProximityPin: Any
    kProximityWrap: Any
    kProxy: Any
    kProxyManager: Any
    kPsdFileTexture: Any
    kQuadPtOnLineManip: Any
    kQuadShadingSwitch: Any
    kRBFsurface: Any
    kRPsolver: Any
    kRadial: Any
    kRadius: Any
    kRamp: Any
    kRampBackground: Any
    kRampShader: Any
    kRbfSrfManip: Any
    kReForm: Any
    kRebuildCurve: Any
    kRebuildSurface: Any
    kRecord: Any
    kReference: Any
    kReflect: Any
    kRemapColor: Any
    kRemapHsv: Any
    kRemapValue: Any
    kRenderBox: Any
    kRenderCone: Any
    kRenderGlobals: Any
    kRenderGlobalsList: Any
    kRenderLayer: Any
    kRenderLayerManager: Any
    kRenderPass: Any
    kRenderPassSet: Any
    kRenderQuality: Any
    kRenderRect: Any
    kRenderSetup: Any
    kRenderSphere: Any
    kRenderTarget: Any
    kRenderUtilityList: Any
    kRenderedImageSource: Any
    kRenderingList: Any
    kReorderUVSet: Any
    kResolution: Any
    kResultCurve: Any
    kResultCurveTimeToAngular: Any
    kResultCurveTimeToDistance: Any
    kResultCurveTimeToTime: Any
    kResultCurveTimeToUnitless: Any
    kReverse: Any
    kReverseCrvManip: Any
    kReverseCurve: Any
    kReverseCurveManip: Any
    kReverseSurface: Any
    kReverseSurfaceManip: Any
    kRevolve: Any
    kRevolveManip: Any
    kRevolvedPrimitive: Any
    kRevolvedPrimitiveManip: Any
    kRgbToHsv: Any
    kRigid: Any
    kRigidConstraint: Any
    kRigidDeform: Any
    kRigidSolver: Any
    kRock: Any
    kRotateBoxManip: Any
    kRotateLimitsManip: Any
    kRotateManip: Any
    kRotateUVManip2D: Any
    kRotateVector: Any
    kRotationFromMatrix: Any
    kRound: Any
    kRoundConstantRadius: Any
    kRoundConstantRadiusManip: Any
    kRoundRadiusCrvManip: Any
    kRoundRadiusManip: Any
    kRowFromMatrix: Any
    kSCsolver: Any
    kSPbirailSrf: Any
    kSamplerInfo: Any
    kScaleConstraint: Any
    kScaleFromMatrix: Any
    kScaleLimitsManip: Any
    kScaleManip: Any
    kScalePointManip: Any
    kScaleUVManip2D: Any
    kScalingBoxManip: Any
    kScreenAlignedCircleManip: Any
    kScript: Any
    kScriptManip: Any
    kSculpt: Any
    kSectionManip: Any
    kSelectionItem: Any
    kSelectionList: Any
    kSelectionListData: Any
    kSelectionListOperator: Any
    kSequenceManager: Any
    kSequencer: Any
    kSet: Any
    kSetGroupComponent: Any
    kSetRange: Any
    kSfRevolveManip: Any
    kShaderGlow: Any
    kShaderList: Any
    kShadingEngine: Any
    kShadingMap: Any
    kShape: Any
    kShapeEditorManager: Any
    kShapeFragment: Any
    kShot: Any
    kShrinkWrapFilter: Any
    kSimpleVolumeShader: Any
    kSin: Any
    kSingleIndexedComponent: Any
    kSingleShadingSwitch: Any
    kSketchPlane: Any
    kSkin: Any
    kSkinBinding: Any
    kSkinClusterFilter: Any
    kSkinShader: Any
    kSl60: Any
    kSmear: Any
    kSmoothCurve: Any
    kSmoothStep: Any
    kSmoothTangentSrf: Any
    kSnapUVManip2D: Any
    kSnapshot: Any
    kSnapshotPath: Any
    kSnapshotShape: Any
    kSnow: Any
    kSoftMod: Any
    kSoftModFilter: Any
    kSoftModManip: Any
    kSolidFractal: Any
    kSolidify: Any
    kSphere: Any
    kSphereData: Any
    kSphericalProjectionManip: Any
    kSplineSolver: Any
    kSpotCylinderManip: Any
    kSpotLight: Any
    kSpotManip: Any
    kSpring: Any
    kSprite: Any
    kSquareSrf: Any
    kSquareSrfManip: Any
    kStandardSurface: Any
    kStateManip: Any
    kStencil: Any
    kStereoCameraMaster: Any
    kStitchAsNurbsShell: Any
    kStitchSrf: Any
    kStitchSrfManip: Any
    kStoryBoard: Any
    kStringArrayData: Any
    kStringData: Any
    kStringShadingSwitch: Any
    kStroke: Any
    kStrokeGlobals: Any
    kStucco: Any
    kStudioClearCoat: Any
    kStyleCurve: Any
    kSubCurve: Any
    kSubSurface: Any
    kSubVertexComponent: Any
    kSubdAddTopology: Any
    kSubdAutoProj: Any
    kSubdBlindData: Any
    kSubdBoolean: Any
    kSubdCleanTopology: Any
    kSubdCloseBorder: Any
    kSubdDelFace: Any
    kSubdExtrudeFace: Any
    kSubdHierBlind: Any
    kSubdLayoutUV: Any
    kSubdMapCut: Any
    kSubdMapSewMove: Any
    kSubdMappingManip: Any
    kSubdMergeVert: Any
    kSubdModifier: Any
    kSubdModifyEdge: Any
    kSubdMoveEdge: Any
    kSubdMoveFace: Any
    kSubdMoveVertex: Any
    kSubdPlanProj: Any
    kSubdProjectionManip: Any
    kSubdSplitFace: Any
    kSubdSubdivideFace: Any
    kSubdTweak: Any
    kSubdTweakUV: Any
    kSubdiv: Any
    kSubdivCVComponent: Any
    kSubdivCollapse: Any
    kSubdivCompId: Any
    kSubdivData: Any
    kSubdivEdgeComponent: Any
    kSubdivFaceComponent: Any
    kSubdivGeom: Any
    kSubdivMapComponent: Any
    kSubdivReverseFaces: Any
    kSubdivSurfaceVarGroup: Any
    kSubdivToNurbs: Any
    kSubdivToPoly: Any
    kSubsetFalloff: Any
    kSubtract: Any
    kSum: Any
    kSummaryObject: Any
    kSuper: Any
    kSurface: Any
    kSurfaceCVComponent: Any
    kSurfaceEPComponent: Any
    kSurfaceEdManip: Any
    kSurfaceFaceComponent: Any
    kSurfaceInfo: Any
    kSurfaceKnotComponent: Any
    kSurfaceLuminance: Any
    kSurfaceRangeComponent: Any
    kSurfaceShader: Any
    kSurfaceVarGroup: Any
    kSymmetryConstraint: Any
    kSymmetryLocator: Any
    kSymmetryMapCurve: Any
    kSymmetryMapVector: Any
    kTan: Any
    kTangentConstraint: Any
    kTension: Any
    kTexLattice: Any
    kTexLatticeDeformManip: Any
    kTexSmoothManip: Any
    kTexSmudgeUVManip: Any
    kTextButtonManip: Any
    kTextCurves: Any
    kTextManip: Any
    kTexture2d: Any
    kTexture3d: Any
    kTextureBakeSet: Any
    kTextureDeformer: Any
    kTextureDeformerHandle: Any
    kTextureEnv: Any
    kTextureList: Any
    kTextureManip3D: Any
    kThreadedDevice: Any
    kThreePointArcManip: Any
    kTime: Any
    kTimeAttribute: Any
    kTimeEditor: Any
    kTimeEditorAnimSource: Any
    kTimeEditorClip: Any
    kTimeEditorClipBase: Any
    kTimeEditorClipEvaluator: Any
    kTimeEditorInterpolator: Any
    kTimeEditorTracks: Any
    kTimeFunction: Any
    kTimeToUnitConversion: Any
    kTimeWarp: Any
    kToggleManip: Any
    kToggleOnLineManip: Any
    kToolContext: Any
    kToonLineAttributes: Any
    kTorus: Any
    kTowPointManip: Any
    kTowPointOnCurveManip: Any
    kTowPointOnSurfaceManip: Any
    kTrackInfoManager: Any
    kTransferAttributes: Any
    kTransferFalloff: Any
    kTransform: Any
    kTransformBoxManip: Any
    kTransformGeometry: Any
    kTranslateBoxManip: Any
    kTranslateLimitsManip: Any
    kTranslateManip: Any
    kTranslateManip2D: Any
    kTranslateUVManip: Any
    kTranslateUVManip2D: Any
    kTranslationFromMatrix: Any
    kTriadManip: Any
    kTrim: Any
    kTrimLocator: Any
    kTrimManip: Any
    kTrimWithBoundaries: Any
    kTriplanarProjectionManip: Any
    kTripleIndexedComponent: Any
    kTripleShadingSwitch: Any
    kTrsInsertManip: Any
    kTrsManip: Any
    kTrsTransManip: Any
    kTrsXformManip: Any
    kTruncate: Any
    kTurbulence: Any
    kTweak: Any
    kTwoPointArcManip: Any
    kTxSl: Any
    kTypedAttribute: Any
    kUInt64ArrayData: Any
    kUVManip2D: Any
    kUVPin: Any
    kUfeProxyTransform: Any
    kUint64SingleIndexedComponent: Any
    kUintArrayData: Any
    kUnderWorld: Any
    kUniform: Any
    kUniformFalloff: Any
    kUnitAttribute: Any
    kUnitConversion: Any
    kUnitToTimeConversion: Any
    kUnknown: Any
    kUnknownDag: Any
    kUnknownTransform: Any
    kUntrim: Any
    kUnused1: Any
    kUnused2: Any
    kUnused3: Any
    kUnused4: Any
    kUnused5: Any
    kUnused6: Any
    kUseBackground: Any
    kUvChooser: Any
    kVectorArrayData: Any
    kVectorProduct: Any
    kVertexBakeSet: Any
    kVertexWeightSet: Any
    kViewColorManager: Any
    kViewManip: Any
    kVolumeAxis: Any
    kVolumeBindManip: Any
    kVolumeFog: Any
    kVolumeLight: Any
    kVolumeNoise: Any
    kVolumeShader: Any
    kVortex: Any
    kWater: Any
    kWeightFunctionData: Any
    kWeightGeometryFilt: Any
    kWire: Any
    kWood: Any
    kWorld: Any
    kWrapFilter: Any
    kWriteToColorBuffer: Any
    kWriteToDepthBuffer: Any
    kWriteToFrameBuffer: Any
    kWriteToLabelBuffer: Any
    kWriteToVectorBuffer: Any
    kXformManip: Any
    kXsectionSubdivEdit: Any
    def __init__(self) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MFnAssembly:
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
    def activate(self, arg: Any) -> MFnAssembly:
        """Activate a representation. The representation to activate is specified as a string name. If no representation is specified then the previously-active representation (if any) will be inactivated and no representation will be active. This method will fail if canActivate() returns False."""
    def activateNonRecursive(self, arg: Any) -> MFnAssembly:
        """Activate a representation, but prevent any nested assemblies created and initialized during this activation from activating any of their representations."""
    def addAttribute(self, attr: MObject, type: Any) -> None:
        """Adds a new dynamic attribute to the node."""
    def addChild(self, node: int, index: bool, keepExistingParents: bool = False) -> MFnAssembly:
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
    def canActivate(self) -> bool:
        """Determines whether this assembly can activate a representation, for the node attached to this function set. For example, this method will return False for a nested assembly, during a call to activateNonRecursive() on the parent assembly. If canActivate() returns False, activate() and activateNonRecursive() will fail."""
    def canBeWritten(self) -> bool:
        """Returns true if the node will be written to file."""
    def canRepApplyEdits(self, representation: Any) -> bool:
        """Determines whether the given representation can apply edits to its data, for the node attached to this function set. If an empty string is passed in as the representation name, this method will return False, since an invalid (or 'None') representation does not have any data and thus, cannot have edits applied to it."""
    def child(self, index: int) -> MObject:
        """Returns the specified child of this node."""
    def childCount(self) -> int:
        """Returns the number of nodes which are children of this one."""
    @staticmethod
    def classification(nodeTypeName: Any) -> Any:
        """Returns the classification string for the named node type."""
    def create(self, type: Any, name: Any = None, parent: MObject | None = None) -> MObject:
        """Creates a new DAG node of the specified type, with the given name."""
    def createRepresentation(self, input: Any, arg: Any) -> str:
        """createRepresentation(input, type, representation[, undoRedo]) -> MString"""
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
    def deleteAllRepresentations(self) -> MFnAssembly:
        """Delete all representations managed by the node attached to this function set."""
    def deleteRepresentation(self, representation: Any) -> MFnAssembly:
        """Delete a representation managed by the node attached to this function set."""
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
    def findAlias(self, alias: Any, attrObj: MObject) -> bool:
        """Returns the attribute which has the given alias."""
    def findPlug(self, attr: Any, wantNetworkedPlug: bool) -> MPlug:
        """Returns a plug for the given attribute."""
    def fullPathName(self) -> Any:
        """Returns the full path of the attached object, from the root of the DAG on down."""
    def getAbsoluteRepNamespace(self) -> str:
        """Get the fully-qualified (absolute) namespace for representations of this assembly node. This is the namespace where nodes created by the activation of a representation will be added. This namespace is shared by all representations."""
    def getActive(self) -> str:
        """Get the active representation in the list of representations. If the list of representations is empty, the return string will be empty."""
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
    def getInitialRep(self, arg: bool, bool: Any) -> Any:
        """Get the initial representation to use when the assembly is first loaded."""
    def getParentAssembly(self) -> MObject:
        """Return the immediate parent assembly of this assembly if there is one, otherwise returns None. An assembly with no parent is a top level assembly."""
    def getPath(self) -> MDagPath:
        """Returns the DAG path to which this function set is attached, or the first path to the node if the function set is attached to an MObject."""
    def getRepLabel(self, representation: Any) -> str:
        """Get the label of the specified representation. The label of a representation is a string that is meant to be shown in the UI and identify the representation meaningfully to a user. The representation label should support localization requirements. If the specified representation is not found in this assembly, an empty string is returned."""
    def getRepNamespace(self) -> str:
        """Get the representations namespace of this assembly node. This is the namespace where nodes created by the activation of a representation will be added. This namespace is shared by all representations. The name can be updated by Maya if a name clash occurs when the namespace is added to its parent namespace (see MPxAssembly::updateRepNamespace() for details)."""
    def getRepType(self, representation: Any) -> str:
        """Get the type of the specified representation. The type string does not have to be user-readable, and does not have to be localized; the type label should be used for UI purposes. If the specified representation is not found in this assembly, an empty string is returned."""
    def getRepresentations(self) -> Any:
        """Returns an array of the representations managed by the node attached to this function set."""
    def getSubAssemblies(self) -> MObjectArray:
        """Returns a list containing direct children of this assembly that are themselves assemblies, for the currently active representation. The returned list will be empty if there are no assembly children of the currently active representation."""
    @staticmethod
    def getTopLevelAssemblies() -> MObjectArray:
        """Returns a list containing top-level assemblies. These are assembliesthat are not nested inside another assembly."""
    def handlesAddEdits(self) -> bool:
        """Determines whether the assembly supplies edits to its data, for the node attached to this function set."""
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
    def importFile(self, arg: Any) -> MFnAssembly:
        """Import the scene elements from the given file into this assembly. See MFileIO::importFile() for more information.  All elements imported from the file become members of the assembly. DAG nodes in the imported file that are parented to world are parented to the assembly. DAG nodes in the imported file whose parent is not world keep their existing parenting relationship."""
    def instanceCount(self, indirect: bool) -> int:
        """Returns the number of instances for this node."""
    def isActive(self, representation: Any) -> bool:
        """Determines whether the given representation is the active representation for the node attached to this function set."""
    def isChildOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a parent of this one."""
    def isFlagSet(self, flag: int) -> bool:
        """Returns the state of the specified node flag."""
    def isInstanced(self, indirect: bool = True) -> bool:
        """Returns True if this node is instanced."""
    def isInstancedAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute is an instanced attribute of this node."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files."""
    def isParentOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a child of this one."""
    def isTopLevel(self) -> bool:
        """Returns whether this assembly node is a top-level assembly. An assembly node is a top-level assembly if no container in its (possibly empty) chain of nesting parent containers is an assembly. Of course, this includes the trivial case of its immediate parent container being null."""
    def isTrackingEdits(self) -> bool:
        """Returns True if the node is referenced or in an assembly that is tracking edits."""
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
    def postLoad(self) -> MFnAssembly:
        """Initialize assemblies after their creation."""
    def removeAttribute(self, attr: MObject, type: Any) -> None:
        """Removes a dynamic attribute from the node."""
    def removeChild(self, node: Any) -> MFnAssembly:
        """Removes the child, specified by MObject, reparenting it under the world."""
    def removeChildAt(self, index: int) -> MFnAssembly:
        """Removes the child, specified by index, reparenting it under the world."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Returns one of the node's attribute, based on the order in which they are written to file."""
    def repTypes(self) -> Any:
        """Return the list of representation types that can be created for this assembly node."""
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
    def setObject(self, arg: MDagPath | MObject) -> MFnAssembly:
        """Attaches the function set to the specified node or DAG path."""
    def setRepLabel(self, representation: Any, label: Any) -> MFnAssembly:
        """Change the representation label."""
    def setRepName(self, representation: Any, newName: Any) -> str:
        """Rename a representation. The newName argument is used as a starting point for the new representation name. This string value can be modified by the derived implementation to meet representation name uniqueness, or other constraints. This method returns the final representation name."""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def supportsEdits(self) -> bool:
        """Returns True if this assembly supports tracking of edits on its nodes."""
    def supportsMemberChanges(self) -> bool:
        """If the assembly does not use Maya's edit tracking system (see supportsEdits()), does it support changes to its member nodes, outside of activation? If so, this means that any mutatingoperation on Maya nodes (parenting, connecting, disconnecting, renaming, deleting, setting attributes, adding attributes, removing attributes, locking) can be performed on member nodes of the assembly."""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
    def type(self) -> int:
        """Returns the type of the function set."""
    def uniqueName(self) -> Any:
        """For a DAG node, the unique name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself. For a non-DAG node, the uniqueName is just its name."""
    def userNode(self) -> MPxNode:
        """Returns the MPxNode object for a plugin node."""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnAttribute:
    affectsAppearance: Any
    affectsWorldSpace: Any
    array: Any
    cached: Any
    channelBox: Any
    connectable: Any
    disconnectBehavior: Any
    dynamic: Any
    extension: Any
    hidden: Any
    indeterminant: Any
    indexMatters: Any
    internal: Any
    isProxyAttribute: Any
    kDelete: Any
    kNothing: Any
    kReset: Any
    keyable: Any
    name: Any
    parent: Any
    readable: Any
    renderSource: Any
    shortName: Any
    storable: Any
    usedAsColor: Any
    usedAsFilename: Any
    usesArrayDataBuilder: Any
    worldSpace: Any
    writable: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def accepts(self, type: int | MTypeId) -> bool:
        """Returns True if this attribute can accept a connection of the given type."""
    def acceptsAttribute(self, attr: MFnAttribute) -> bool:
        """Returns True if this attribute can accept a connection with the given attribute."""
    def addToCategory(self, category: Any) -> None:
        """Adds the attribute to a category"""
    def getAddAttrCmd(self, useLongName: bool | None = None) -> Any:
        """Returns a string containing a MEL 'addAttr' command capable of recreating the attribute."""
    def hasCategory(self, category: Any) -> bool:
        """Checks to see if the attribute has a given category"""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def setNiceNameOverride(self, localizedName: Any) -> None:
        """Sets a nice UI name for this attribute rather than using the default derived from it's long name."""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def type(self) -> int:
        """Returns the type of the function set."""

class MFnBase:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def type(self) -> int:
        """Returns the type of the function set."""

class MFnCamera:
    boundingBox: Any
    cameraScale: Any
    centerOfInterest: Any
    fStop: Any
    farClippingPlane: Any
    farFocusDistance: Any
    filmFit: Any
    filmFitOffset: Any
    filmRollOrder: Any
    filmRollValue: Any
    filmTranslateH: Any
    filmTranslateV: Any
    focalLength: Any
    focusDistance: Any
    horizontalFilmAperture: Any
    horizontalFilmOffset: Any
    horizontalPan: Any
    horizontalRollPivot: Any
    horizontalShake: Any
    inModel: Any
    inUnderWorld: Any
    isClippingPlanes: Any
    isDefaultNode: Any
    isDepthOfField: Any
    isDisplayFilmGate: Any
    isDisplayGateMask: Any
    isFromReferencedFile: Any
    isInstanceable: Any
    isIntermediateObject: Any
    isLocked: Any
    isMotionBlur: Any
    isShared: Any
    isVerticalLock: Any
    kExtensionAttr: Any
    kFillFilmFit: Any
    kHorizontalFilmFit: Any
    kInvalid: Any
    kInvalidAttr: Any
    kLocalDynamicAttr: Any
    kNextPos: Any
    kNormalAttr: Any
    kOverscanFilmFit: Any
    kRotateTranslate: Any
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
    kTranslateRotate: Any
    kVerticalFilmFit: Any
    lensSqueezeRatio: Any
    namespace: Any
    nearClippingPlane: Any
    nearFocusDistance: Any
    objectColor: Any
    objectColorRGB: Any
    objectColorType: Any
    orthoWidth: Any
    overscan: Any
    panZoomEnabled: Any
    pluginName: Any
    postScale: Any
    preScale: Any
    renderPanZoom: Any
    shakeEnabled: Any
    shakeOverscan: Any
    shakeOverscanEnabled: Any
    shutterAngle: Any
    stereoHIT: Any
    stereoHITEnabled: Any
    tumblePivot: Any
    typeId: Any
    typeName: Any
    useObjectColor: Any
    usePivotAsLocalSpace: Any
    verticalFilmAperture: Any
    verticalFilmOffset: Any
    verticalPan: Any
    verticalRollPivot: Any
    verticalShake: Any
    zoom: Any
    def __init__(self, object: MObject | MDagPath | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def absoluteName(self) -> Any:
        """Returns the absolute name of this node.  The absolute name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself.  Regardless of relative name mode, absoluteName() will always return a full namespace path prefixed with a leading colon (the root namespace).  If the underlying node is a DAG node, then absoluteName() does not guarantee uniqueness, that is, two dependency nodes could have the same absoluteName().  In cases like this the uniqueName() method will guarantee that the name uniquely identifies the node."""
    def addAttribute(self, attr: MObject, type: Any) -> None:
        """Adds a new dynamic attribute to the node."""
    def addChild(self, node: int, index: bool, keepExistingParents: bool = False) -> MFnCamera:
        """Makes a node a child of this one."""
    def addExternalContentForFileAttr(self, attr: MObject) -> MExternalContentInfoTable:
        """Adds content info to the specified table from a file path attribute."""
    def affectsAnimation(self) -> bool:
        """Returns true if the changes to the node may affect animation."""
    @staticmethod
    def allocateFlag(pluginName: Any) -> int:
        """Allocates a flag on all nodes for use by the named plugin and returns the flag's index."""
    def aspectRatio(self) -> float:
        """Returns the aspect ratio for the camera."""
    def attribute(self, index: Any) -> MObject:
        """Returns an attribute of the node, given either its index or name."""
    def attributeClass(self, attr: MObject) -> Any:
        """Returns the class of the specified attribute."""
    def attributeCount(self) -> int:
        """Returns the number of attributes on the node."""
    def canBeWritten(self) -> bool:
        """Returns true if the node will be written to file."""
    def centerOfInterestPoint(self, space: int) -> MPoint:
        """Returns the center of interest point for the camera."""
    def child(self, index: int) -> MObject:
        """Returns the specified child of this node."""
    def childCount(self) -> int:
        """Returns the number of nodes which are children of this one."""
    @staticmethod
    def classification(nodeTypeName: Any) -> Any:
        """Returns the classification string for the named node type."""
    def computeDepthOfField(self, nearLimit: float | None = None) -> MFnCamera:
        """Compute the depth of field"""
    def copyViewFrom(self, otherCamera: MDagPath) -> MFnCamera:
        """Copy the camera settings related to the perspective from the given camera view."""
    def create(self, parent: Any = None) -> MObject:
        """Creates a perspective camera. A parent can be specified for the new camera, otherwise a transform is created."""
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
    def eyePoint(self, space: int) -> MPoint:
        """Returns the eye point for the camera."""
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
    def getAspectRatioLimits(self, arg: Any, float: Any) -> Any:
        """Returns the minimum and maximum aspect ratio limits for the camera."""
    def getConnectedSetsAndMembers(self, instance: int, arg: bool, MObjectArray: Any) -> Any:
        """Returns a tuple containing an array of sets and an array of the"""
    def getConnections(self) -> MPlugArray:
        """Returns all the plugs which are connected to attributes of this node."""
    def getExternalContent(self) -> MExternalContentInfoTable:
        """Gets the external content (files) that this node depends on."""
    def getFilmApertureLimits(self, arg: Any, float: Any) -> Any:
        """Returns the maximum and minimum film aperture limits for the camera."""
    def getFilmFrustum(self, distance: float, applyPanZoom: MPointArray | bool, float: bool, float_: Any, float__: Any) -> Any:
        """Returns the film frustum for the camera (horizontal size, vertical size, horizontal offset and vertical offset). The frustum defines the projective transformation."""
    def getFilmFrustumCorners(self, distance: Any, applyPanZoom: bool = False) -> MPointArray:
        """Returns the film frustum for the camera. The frustum defines the projective transformation."""
    def getFocalLengthLimits(self, arg: Any, float: Any) -> Any:
        """Returns the maximum and minimum focal length limits for the camera."""
    def getPath(self) -> MDagPath:
        """Returns the DAG path to which this function set is attached, or the first path to the node if the function set is attached to an MObject."""
    def getPortFieldOfView(self, int: int, arg: int, float: Any) -> Any:
        """Returns the horizontal and vertical field of view in radians from the given viewport width and height."""
    def getRenderingFrustum(self, arg: float, float: Any, float_: Any, float__: Any) -> Any:
        """Returns the rendering frustum (left, right, bottom and top) for the camera."""
    def getViewParameters(self, windowAspect: float, applyPanZoom: bool, float: Any, float_: Any, float__: Any, applyOverscan: bool = False, applySqueeze: bool = False) -> Any:
        """Returns the intermediate viewing frustum (apertureX, apertureY, offsetX and offsetY) parameters for the camera. The aperture and offset are used by getViewingFrustum() and getRenderingFrustum() to compute the extent (left, right, top, bottom) of the frustum in the following manner:"""
    def getViewingFrustum(self, windowAspect: float, applyPanZoom: bool, float: Any, float_: Any, float__: Any, applyOverscan: bool = False, applySqueeze: bool = False) -> Any:
        """Returns the viewing frustum (left, right, bottom and top) for the camera."""
    def hasAttribute(self, name: Any) -> bool:
        """Returns True if the node has an attribute with the given name."""
    def hasChild(self, node: MObject) -> bool:
        """Returns True if the specified node is a child of this one."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def hasParent(self, node: MObject) -> bool:
        """Returns True if the specified node is a parent of this one."""
    def hasSamePerspective(self, otherCamera: MDagPath) -> bool:
        """Returns True if the camera has same perspective settings as the given camera."""
    def hasUniqueName(self) -> bool:
        """Returns True if the node's name is unique."""
    def horizontalFieldOfView(self) -> float:
        """Returns the horizontal field of view for the camera."""
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
    def isNewAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files."""
    def isOrtho(self) -> bool:
        """Returns True if the camera is in orthographic mode."""
    def isParentOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a child of this one."""
    def isTrackingEdits(self) -> bool:
        """Returns True if the node is referenced or in an assembly that is tracking edits."""
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
    def postProjectionMatrix(self, context: MDGContext | None = None) -> MFloatMatrix:
        """Returns the post projection matrix used to compute film roll on the film back plane."""
    def projectionMatrix(self, context: MDGContext | None = None) -> MFloatMatrix:
        """Returns the orthographic or perspective projection matrix for the camera."""
    def removeAttribute(self, attr: MObject, type: Any) -> None:
        """Removes a dynamic attribute from the node."""
    def removeChild(self, node: Any) -> MFnCamera:
        """Removes the child, specified by MObject, reparenting it under the world."""
    def removeChildAt(self, index: int) -> MFnCamera:
        """Removes the child, specified by index, reparenting it under the world."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Returns one of the node's attribute, based on the order in which they are written to file."""
    def rightDirection(self, space: int) -> MVector:
        """Returns the right direction vector for the camera."""
    def set(self, wsEyeLocation: MPoint, wsViewDirection: MVector, wsUpDirection: MVector, horizFieldOfView: float, aspectRatio: float) -> MFnCamera:
        """Convenience routine to set the camera viewing parameters. The specified values should be in world space where applicable."""
    def setAffectsAnimation(self) -> None:
        """Specifies that modifications to a node could potentially affect the animation."""
    def setAlias(self, alias: Any, name: Any, plug: MPlug, add: bool | None = None) -> bool:
        """Adds or removes an attribute alias."""
    def setAspectRatio(self, aspectRatio: float) -> MFnCamera:
        """Set the aspect ratio of the View.  The aspect ratio is expressed as width/height.  This also modifies the entity's scale transformation to reflect the new aspect ratio."""
    def setCenterOfInterestPoint(self, centerOfInterest: MPoint, space: int) -> MFnCamera:
        """Positions the center-of-interest of the camera keeping the eye-point fixed in space. This method changed the orientation and translation of the camera's transform attributes as well as the center-of-interest distance."""
    def setDoNotWrite(self, flag: bool) -> None:
        """Used to prevent the node from being written to file."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> None:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> None:
        """Sets content info in the specified attribute from the table."""
    def setEyePoint(self, eyeLocation: MPoint, space: int) -> MFnCamera:
        """Positions the eye-point of the camera keeping the center of interest fixed in space. This method changed the orientation and translation of the camera's transform attributes as well as the center-of-interest distance."""
    def setFlag(self, flag: int, state: bool) -> None:
        """Sets the state of the specified node flag."""
    def setHorizontalFieldOfView(self, fov: float) -> MFnCamera:
        """Sets the horizontal field of view for the camera."""
    def setIsOrtho(self, orthoState: bool, useDist: float | None = None) -> MFnCamera:
        """Switch the camera in and out of orthographic mode.  When the switch happens, the camera has to calculate a new fov or ortho width, each of which is based on the other and a set distance.  The caller can specify the distance; otherwise the center of interest is used."""
    def setName(self, name: Any, createNamespace: bool | None = None) -> Any:
        """Sets the node's name."""
    def setNearFarClippingPlanes(self, near: float, far: float) -> MFnCamera:
        """Set the distances to the Near and Far Clipping Planes."""
    def setObject(self, arg: MDagPath | MObject) -> MFnCamera:
        """Attaches the function set to the specified node or DAG path."""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def setVerticalFieldOfView(self, fov: float) -> MFnCamera:
        """Sets the vertical field of view for the camera."""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
    def type(self) -> int:
        """Returns the type of the function set."""
    def uniqueName(self) -> Any:
        """For a DAG node, the unique name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself. For a non-DAG node, the uniqueName is just its name."""
    def upDirection(self, space: int) -> MVector:
        """Returns the up direction vector for the camera."""
    def userNode(self) -> MPxNode:
        """Returns the MPxNode object for a plugin node."""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""
    def verticalFieldOfView(self) -> float:
        """Returns the vertical field of view for the camera."""
    def viewDirection(self, space: int) -> MVector:
        """Returns the view direction for the camera"""

class MFnComponent:
    componentType: Any
    elementCount: Any
    hasWeights: Any
    isComplete: Any
    isEmpty: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def isEqual(self, arg: Any) -> bool:
        """Returns True if other refers to the same component as the"""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def type(self) -> int:
        """Returns the type of the function set."""
    def weight(self, index: int) -> MWeight:
        """Returns the weight associated with the specified element,"""

class MFnComponentListData:
    kAny: Any
    kComponentList: Any
    kDoubleArray: Any
    kDynArrayAttrs: Any
    kDynSweptGeometry: Any
    kFalloffFunction: Any
    kFloatArray: Any
    kIntArray: Any
    kInvalid: Any
    kLast: Any
    kLattice: Any
    kMatrix: Any
    kMatrixArray: Any
    kMesh: Any
    kNId: Any
    kNObject: Any
    kNumeric: Any
    kNurbsCurve: Any
    kNurbsSurface: Any
    kPlugin: Any
    kPluginGeometry: Any
    kPointArray: Any
    kSphere: Any
    kString: Any
    kStringArray: Any
    kSubdSurface: Any
    kVectorArray: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def add(self, MObject: Any) -> MFnComponentListData:
        """Adds the specified component to the end of the list."""
    def clear(self) -> MFnComponentListData:
        """Removes all of the components from the list."""
    def create(self) -> MObject:
        """Creates a new, empty component list, attaches it to the"""
    def get(self, index: Any) -> MObject:
        """Returns a copy of the component at the specified index."""
    def has(self, MObject: MObject) -> bool:
        """Returns True if the list contains the specified"""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def length(self) -> int:
        """Returns the number of components in the list."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def remove(self, MObject: int) -> MFnComponentListData:
        """remove(index) -> self"""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def type(self) -> int:
        """Returns the type of the function set."""

class MFnCompoundAttribute:
    affectsAppearance: Any
    affectsWorldSpace: Any
    array: Any
    cached: Any
    channelBox: Any
    connectable: Any
    disconnectBehavior: Any
    dynamic: Any
    extension: Any
    hidden: Any
    indeterminant: Any
    indexMatters: Any
    internal: Any
    isProxyAttribute: Any
    kDelete: Any
    kNothing: Any
    kReset: Any
    keyable: Any
    name: Any
    parent: Any
    readable: Any
    renderSource: Any
    shortName: Any
    storable: Any
    usedAsColor: Any
    usedAsFilename: Any
    usesArrayDataBuilder: Any
    worldSpace: Any
    writable: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def accepts(self, type: int | MTypeId) -> bool:
        """Returns True if this attribute can accept a connection of the given type."""
    def acceptsAttribute(self, attr: MFnAttribute) -> bool:
        """Returns True if this attribute can accept a connection with the given attribute."""
    def addChild(self, child: MObject) -> None:
        """Add a child attribute."""
    def addToCategory(self, category: Any) -> None:
        """Adds the attribute to a category"""
    def child(self, index: int) -> MObject:
        """Returns one of the attribute's children, specified by index."""
    def create(self, full: Any, brief: Any) -> MObject:
        """Creates a new compound attribute, attaches it to the function set and returns it as an MObject."""
    def getAddAttrCmd(self, useLongName: bool | None = None) -> Any:
        """Returns a string containing a MEL 'addAttr' command capable of recreating the attribute."""
    def getAddAttrCmds(self, useLongNames: bool | None = None) -> Any:
        """Returns a list of MEL 'addAttr' commands capable of recreating the attribute and all of its children."""
    def hasCategory(self, category: Any) -> bool:
        """Checks to see if the attribute has a given category"""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def numChildren(self) -> int:
        """Returns number of child attributes currently parented under the compound attribute."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def removeChild(self, child: MObject) -> None:
        """Remove a child attribute."""
    def setNiceNameOverride(self, localizedName: Any) -> None:
        """Sets a nice UI name for this attribute rather than using the default derived from it's long name."""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def type(self) -> int:
        """Returns the type of the function set."""

class MFnContainerNode:
    isDefaultNode: Any
    isFromReferencedFile: Any
    isLocked: Any
    isShared: Any
    kChildAnchor: Any
    kExtensionAttr: Any
    kGeneric: Any
    kInvalidAttr: Any
    kLocalDynamicAttr: Any
    kNormalAttr: Any
    kParentAnchor: Any
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
    def clear(self) -> Any:
        """Delete all members of the container."""
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
    def getConnections(self) -> MPlugArray:
        """Returns all the plugs which are connected to attributes of this node."""
    @staticmethod
    def getCurrentAsMObject() -> MObject:
        """Retrieve the current container node."""
    def getExternalContent(self) -> MExternalContentInfoTable:
        """Gets the external content (files) that this node depends on."""
    def getMembers(self) -> MObjectArray:
        """Return an array of the nodes included in this container."""
    def getParentContainer(self) -> MObject:
        """Return the parent container, if there is one. Otherwise return an empty MObject."""
    def getPublishedNames(self, unboundOnly: bool) -> Any:
        """Return a list of published names on the container. Depending on the arguments, either all published names or only unbound published names will be returned."""
    def getPublishedNodes(self, publishNodeType: Any, arg: Any) -> Any:
        """Return a list of the published nodes of a given type. For any names that have assigned nodes, return the node at the corresponding array index. For any names that do not have assigned nodes, a NULL MObject will be at the corresponding array index."""
    def getPublishedPlugs(self, arg: Any, arg_: Any) -> Any:
        """Return a tuple of plugs that have been published on this container and the names of those plugs."""
    def getRootTransform(self) -> MObject:
        """Return the root transform, if there is one. Otherwise return an empty MObject."""
    def getSubcontainers(self) -> MObjectArray:
        """Return an array of the container nodes included in this container."""
    def hasAttribute(self, name: Any) -> bool:
        """Returns True if the node has an attribute with the given name."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def hasUniqueName(self) -> bool:
        """Returns True if the node's name is unique."""
    def isCurrent(self) -> bool:
        """Return whether the container node managed by this function set is the current container."""
    def isFlagSet(self, flag: int) -> bool:
        """Returns the state of the specified node flag."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files."""
    def isTrackingEdits(self) -> bool:
        """Returns True if the node is referenced or in an assembly that is tracking edits."""
    def makeCurrent(self, isCurrent: bool) -> MFnContainerNode:
        """Set or clear whether the container managed by this function set is denoted as the"""
    def name(self) -> Any:
        """Returns the node's name."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
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

class MFnDagNode:
    boundingBox: Any
    inModel: Any
    inUnderWorld: Any
    isDefaultNode: Any
    isFromReferencedFile: Any
    isInstanceable: Any
    isIntermediateObject: bool
    isLocked: Any
    isShared: Any
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
    def addChild(self, node: int, index: bool, keepExistingParents: bool = False) -> MFnDagNode:
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
    def canBeWritten(self) -> bool:
        """Returns true if the node will be written to file."""
    def child(self, count: int, type: int | None = None) -> MObject:
        """Returns the specified child of this node."""
    def childCount(self) -> int:
        """Returns the number of nodes which are children of this one."""
    @staticmethod
    def classification(nodeTypeName: Any) -> Any:
        """Returns the classification string for the named node type."""
    def create(self, type: Any, name: Any = None, parent: MObject | None = None) -> MObject:
        """Creates a new DAG node of the specified type, with the given name."""
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
    def isNewAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files."""
    def isParentOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a child of this one."""
    def isTrackingEdits(self) -> bool:
        """Returns True if the node is referenced or in an assembly that is tracking edits."""
    def name(self) -> Any:
        """Returns the node's name."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def parent(self, count: int) -> MObject:
        """Returns the specified parent of this node."""
    def parentCount(self) -> int:
        """Returns the number of parents this node has."""
    def partialPathName(self) -> Any:
        """Returns the minimum path string necessary to uniquely identify the attached object."""
    def plugsAlias(self, plug: MPlug) -> Any:
        """Returns the alias for a plug's attribute."""
    def removeAttribute(self, attr: MObject, type: Any) -> None:
        """Removes a dynamic attribute from the node."""
    def removeChild(self, node: Any) -> MFnDagNode:
        """Removes the child, specified by MObject, reparenting it under the world."""
    def removeChildAt(self, index: int) -> MFnDagNode:
        """Removes the child, specified by index, reparenting it under the world."""
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
    def setObject(self, arg: MDagPath | MObject) -> MFnDagNode:
        """Attaches the function set to the specified node or DAG path."""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
    def type(self) -> int:
        """Returns the type of the function set."""
    def uniqueName(self) -> Any:
        """For a DAG node, the unique name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself. For a non-DAG node, the uniqueName is just its name."""
    def userNode(self) -> MPxNode:
        """Returns the MPxNode object for a plugin node."""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnData:
    kAny: Any
    kComponentList: Any
    kDoubleArray: Any
    kDynArrayAttrs: Any
    kDynSweptGeometry: Any
    kFalloffFunction: Any
    kFloatArray: Any
    kIntArray: Any
    kInvalid: Any
    kLast: Any
    kLattice: Any
    kMatrix: Any
    kMatrixArray: Any
    kMesh: Any
    kNId: Any
    kNObject: Any
    kNumeric: Any
    kNurbsCurve: Any
    kNurbsSurface: Any
    kPlugin: Any
    kPluginGeometry: Any
    kPointArray: Any
    kSphere: Any
    kString: Any
    kStringArray: Any
    kSubdSurface: Any
    kVectorArray: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def type(self) -> int:
        """Returns the type of the function set."""

class MFnDependencyNode:
    isDefaultNode: Any
    isFromReferencedFile: bool
    isLocked: bool
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
    def attribute(self, attrName: Any) -> MObject:
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
    def create(self, type: Any, name: Any = None) -> MObject:
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
    def getConnections(self) -> MPlugArray:
        """Returns all the plugs which are connected to attributes of this node."""
    def getExternalContent(self) -> MExternalContentInfoTable:
        """Gets the external content (files) that this node depends on."""
    def hasAttribute(self, name: Any) -> bool:
        """Returns True if the node has an attribute with the given name."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def hasUniqueName(self) -> bool:
        """Returns True if the node's name is unique."""
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
    def setObject(self, object: MObject) -> None:
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

class MFnDisplayLayer:
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
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def absoluteName(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the absolute name of this node.  The absolute name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself.  Regardless of relative name mode, absoluteName() will always return a full namespace path prefixed with a leading colon (the root namespace).  If the underlying node is a DAG node, then absoluteName() does not guarantee uniqueness, that is, two dependency nodes could have the same absoluteName().  In cases like this the uniqueName() method will guarantee that the name uniquely identifies the node."""
    def add(self, item: Any) -> Any:
        """Adds the item to the display layer, where item can be a Ufe path string"""
    def addAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """Adds a new dynamic attribute to the node."""
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
    def canBeWritten(self, *args: Any, **kwargs: Any) -> Any:
        """Returns true if the node will be written to file."""
    @staticmethod
    def classification(*args: Any, **kwargs: Any) -> Any:
        """Returns the classification string for the named node type."""
    def contains(self, item: Any) -> bool:
        """Returns true if the item is in the display layer, where item can be a Ufe"""
    def containsAncestorInclusive(self, item: Any) -> Any:
        """Returns true if the item or one of its ancestors is in the display layer,"""
    def create(self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new node of the given type."""
    @staticmethod
    def deallocateAllFlags(*args: Any, **kwargs: Any) -> Any:
        """Deallocates all node flags which are currently allocated to the named plugin."""
    @staticmethod
    def deallocateFlag(*args: Any, **kwargs: Any) -> Any:
        """Deallocates the specified node flag, which was previously allocated by the named plugin using allocateFlag()."""
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
    def findAlias(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the attribute which has the given alias."""
    def findPlug(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a plug for the given attribute."""
    def getAffectedAttributes(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all of the attributes which are affected by the specified attribute."""
    def getAffectingAttributes(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all of the attributes which affect the specified attribute."""
    def getAliasAttr(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute aliases."""
    def getAliasList(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all of the node's attribute aliases."""
    def getConnections(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all the plugs which are connected to attributes of this node."""
    def getExternalContent(self, *args: Any, **kwargs: Any) -> Any:
        """Gets the external content (files) that this node depends on."""
    def getMembers(self, members: Any) -> Any:
        """Get the members of the display layer"""
    def hasAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the node has an attribute with the given name."""
    def hasObj(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the function set is compatible with the specified Maya object."""
    def hasUniqueName(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the node's name is unique."""
    def isFlagSet(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the state of the specified node flag."""
    def isNewAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files."""
    def isTrackingEdits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the node is referenced or in an assembly that is tracking edits."""
    def name(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the node's name."""
    def object(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def plugsAlias(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the alias for a plug's attribute."""
    def remove(self, item: Any) -> Any:
        """Removes the item to the display layer, where item can be a Ufe path string"""
    def removeAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """Removes a dynamic attribute from the node."""
    def reorderedAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """Returns one of the node's attribute, based on the order in which they are written to file."""
    def setAffectsAnimation(self, *args: Any, **kwargs: Any) -> Any:
        """Specifies that modifications to a node could potentially affect the animation."""
    def setAlias(self, *args: Any, **kwargs: Any) -> Any:
        """Adds or removes an attribute alias."""
    def setDoNotWrite(self, *args: Any, **kwargs: Any) -> Any:
        """Used to prevent the node from being written to file."""
    def setExternalContent(self, *args: Any, **kwargs: Any) -> Any:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, *args: Any, **kwargs: Any) -> Any:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the state of the specified node flag."""
    def setName(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the node's name."""
    def setObject(self, *args: Any, **kwargs: Any) -> Any:
        """Attaches the function set to the specified Maya object."""
    def setUuid(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the node's UUID."""
    def type(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the type of the function set."""
    def uniqueName(self, *args: Any, **kwargs: Any) -> Any:
        """For a DAG node, the unique name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself. For a non-DAG node, the uniqueName is just its name."""
    def userNode(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the MPxNode object for a plugin node."""
    def uuid(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the node's UUID."""

class MFnDisplayLayerManager:
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
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def absoluteName(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the absolute name of this node.  The absolute name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself.  Regardless of relative name mode, absoluteName() will always return a full namespace path prefixed with a leading colon (the root namespace).  If the underlying node is a DAG node, then absoluteName() does not guarantee uniqueness, that is, two dependency nodes could have the same absoluteName().  In cases like this the uniqueName() method will guarantee that the name uniquely identifies the node."""
    def addAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """Adds a new dynamic attribute to the node."""
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
    def canBeWritten(self, *args: Any, **kwargs: Any) -> Any:
        """Returns true if the node will be written to file."""
    @staticmethod
    def classification(*args: Any, **kwargs: Any) -> Any:
        """Returns the classification string for the named node type."""
    def create(self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new node of the given type."""
    @staticmethod
    def currentDisplayLayerManager() -> MObject:
        """Get the current display layer manager"""
    @staticmethod
    def deallocateAllFlags(*args: Any, **kwargs: Any) -> Any:
        """Deallocates all node flags which are currently allocated to the named plugin."""
    @staticmethod
    def deallocateFlag(*args: Any, **kwargs: Any) -> Any:
        """Deallocates the specified node flag, which was previously allocated by the named plugin using allocateFlag()."""
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
    def findAlias(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the attribute which has the given alias."""
    def findPlug(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a plug for the given attribute."""
    def getAffectedAttributes(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all of the attributes which are affected by the specified attribute."""
    def getAffectingAttributes(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all of the attributes which affect the specified attribute."""
    def getAliasAttr(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute aliases."""
    def getAliasList(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all of the node's attribute aliases."""
    def getAllDisplayLayers(self) -> Any:
        """Get all the display layers managed by the display layer manager"""
    def getAncestorLayersInclusive(self, item: Any) -> Any:
        """Finds the layers the item and it's ancestors are in, where item can be a Ufe"""
    def getConnections(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all the plugs which are connected to attributes of this node."""
    def getExternalContent(self, *args: Any, **kwargs: Any) -> Any:
        """Gets the external content (files) that this node depends on."""
    def getLayer(self, item: Any) -> Any:
        """Finds the layer the item is in, where item can be a Ufe"""
    def hasAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the node has an attribute with the given name."""
    def hasObj(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the function set is compatible with the specified Maya object."""
    def hasUniqueName(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the node's name is unique."""
    def isFlagSet(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the state of the specified node flag."""
    def isNewAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files."""
    def isTrackingEdits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the node is referenced or in an assembly that is tracking edits."""
    def name(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the node's name."""
    def object(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def plugsAlias(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the alias for a plug's attribute."""
    def removeAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """Removes a dynamic attribute from the node."""
    def reorderedAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """Returns one of the node's attribute, based on the order in which they are written to file."""
    def setAffectsAnimation(self, *args: Any, **kwargs: Any) -> Any:
        """Specifies that modifications to a node could potentially affect the animation."""
    def setAlias(self, *args: Any, **kwargs: Any) -> Any:
        """Adds or removes an attribute alias."""
    def setDoNotWrite(self, *args: Any, **kwargs: Any) -> Any:
        """Used to prevent the node from being written to file."""
    def setExternalContent(self, *args: Any, **kwargs: Any) -> Any:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, *args: Any, **kwargs: Any) -> Any:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the state of the specified node flag."""
    def setName(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the node's name."""
    def setObject(self, *args: Any, **kwargs: Any) -> Any:
        """Attaches the function set to the specified Maya object."""
    def setUuid(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the node's UUID."""
    def type(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the type of the function set."""
    def uniqueName(self, *args: Any, **kwargs: Any) -> Any:
        """For a DAG node, the unique name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself. For a non-DAG node, the uniqueName is just its name."""
    def userNode(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the MPxNode object for a plugin node."""
    def uuid(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the node's UUID."""

class MFnDoubleArrayData:
    kAny: Any
    kComponentList: Any
    kDoubleArray: Any
    kDynArrayAttrs: Any
    kDynSweptGeometry: Any
    kFalloffFunction: Any
    kFloatArray: Any
    kIntArray: Any
    kInvalid: Any
    kLast: Any
    kLattice: Any
    kMatrix: Any
    kMatrixArray: Any
    kMesh: Any
    kNId: Any
    kNObject: Any
    kNumeric: Any
    kNurbsCurve: Any
    kNurbsSurface: Any
    kPlugin: Any
    kPluginGeometry: Any
    kPointArray: Any
    kSphere: Any
    kString: Any
    kStringArray: Any
    kSubdSurface: Any
    kVectorArray: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def array(self) -> MDoubleArray:
        """Returns the encapsulated array as an MDoubleArray."""
    def copyTo(self) -> None:
        """Replaces the elements of an array with those in the encapsulated array."""
    def create(self, in_: MDoubleArray | None = None) -> MObject:
        """Creates a new double array data object."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def set(self, element: float | MDoubleArray, index: int) -> None:
        """Sets values in the encapsulated array."""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def type(self) -> int:
        """Returns the type of the function set."""

class MFnDoubleIndexedComponent:
    componentType: Any
    elementCount: Any
    hasWeights: Any
    isComplete: Any
    isEmpty: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addElement(self, uIndex: int, vIndex: int) -> MFnDoubleIndexedComponent:
        """addElement([uIndex, vIndex]) -> self"""
    def addElements(self, arg: MIntArray) -> MFnDoubleIndexedComponent:
        """Adds the specified elements to the component. Each item in the"""
    def create(self, arg: int) -> MObject:
        """Creates a new, empty component, attaches it to the function set and"""
    def getCompleteData(self, arg: Any, numV: Any) -> Any:
        """Returns a tuple containing the number of U and V indices in the complete"""
    def getElement(self, arg: int, vIndex: Any) -> Any:
        """Returns the index'th element of the component as a tuple containing the"""
    def getElements(self, arg: Any, vIndex: Any) -> Any:
        """Returns all of the component's elements as a list of tuples with each"""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def isEqual(self, arg: Any) -> bool:
        """Returns True if other refers to the same component as the"""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def setCompleteData(self, numU: int, numV: int) -> MFnDoubleIndexedComponent:
        """Marks the component as complete (i.e. contains all possible elements)."""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def type(self) -> int:
        """Returns the type of the function set."""
    def weight(self, index: int) -> MWeight:
        """Returns the weight associated with the specified element,"""

class MFnEnumAttribute:
    affectsAppearance: Any
    affectsWorldSpace: Any
    array: Any
    cached: Any
    channelBox: Any
    connectable: Any
    default: Any
    disconnectBehavior: Any
    dynamic: Any
    extension: Any
    hidden: Any
    indeterminant: Any
    indexMatters: Any
    internal: Any
    isProxyAttribute: Any
    kDelete: Any
    kNothing: Any
    kReset: Any
    keyable: Any
    name: Any
    parent: Any
    readable: Any
    renderSource: Any
    shortName: Any
    storable: Any
    usedAsColor: Any
    usedAsFilename: Any
    usesArrayDataBuilder: Any
    worldSpace: Any
    writable: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def accepts(self, type: int | MTypeId) -> bool:
        """Returns True if this attribute can accept a connection of the given type."""
    def acceptsAttribute(self, attr: MFnAttribute) -> bool:
        """Returns True if this attribute can accept a connection with the given attribute."""
    def addField(self, fieldString: Any, index: Any) -> None:
        """Add an item to the enumeration with a specified UI name and corresponding attribute value."""
    def addToCategory(self, category: Any) -> None:
        """Adds the attribute to a category"""
    def create(self, fullName: Any, briefName: Any, defaultValue: Any = None) -> MObject:
        """Creates a new enumeration attribute, attaches it to the function set and returns it as an MObject."""
    def fieldName(self, index: Any) -> Any:
        """Returns the name of the enumeration item which has a given value."""
    def fieldValue(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the value of the enumeration item which has a given name."""
    def getAddAttrCmd(self, useLongName: bool | None = None) -> Any:
        """Returns a string containing a MEL 'addAttr' command capable of recreating the attribute."""
    def getMax(self) -> Any:
        """Returns the maximum value of all the enumeration items."""
    def getMin(self) -> Any:
        """Returns the minimum value of all the enumeration items."""
    def hasCategory(self, category: Any) -> bool:
        """Checks to see if the attribute has a given category"""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def setDefaultByName(self, *args: Any, **kwargs: Any) -> Any:
        """Set the default value using the name of an enumeration item. Equivalent to: attr.default = attr.fieldValue(name)"""
    def setNiceNameOverride(self, localizedName: Any) -> None:
        """Sets a nice UI name for this attribute rather than using the default derived from it's long name."""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def type(self) -> int:
        """Returns the type of the function set."""

class MFnGenericAttribute:
    affectsAppearance: Any
    affectsWorldSpace: Any
    array: Any
    cached: Any
    channelBox: Any
    connectable: Any
    disconnectBehavior: Any
    dynamic: Any
    extension: Any
    hidden: Any
    indeterminant: Any
    indexMatters: Any
    internal: Any
    isProxyAttribute: Any
    kDelete: Any
    kNothing: Any
    kReset: Any
    keyable: Any
    name: Any
    parent: Any
    readable: Any
    renderSource: Any
    shortName: Any
    storable: Any
    usedAsColor: Any
    usedAsFilename: Any
    usesArrayDataBuilder: Any
    worldSpace: Any
    writable: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def accepts(self, type: int | MTypeId) -> bool:
        """Returns True if this attribute can accept a connection of the given type."""
    def acceptsAttribute(self, attr: MFnAttribute) -> bool:
        """Returns True if this attribute can accept a connection with the given attribute."""
    def addDataType(self, *args: Any, **kwargs: Any) -> Any:
        """Adds the specified Maya data type to the list of those accepted by the attribute."""
    def addNumericType(self, *args: Any, **kwargs: Any) -> Any:
        """Adds the specified numeric type to the list of those accepted by the attribute."""
    def addToCategory(self, category: Any) -> None:
        """Adds the attribute to a category"""
    def addTypeId(self, *args: Any, **kwargs: Any) -> Any:
        """Adds the specified data typeId to the list of those accepted by the attribute."""
    def create(self, full: Any, brief: Any) -> MObject:
        """Creates a new generic attribute, attaches it to the function set and returns it as an MObject."""
    def getAddAttrCmd(self, useLongName: bool | None = None) -> Any:
        """Returns a string containing a MEL 'addAttr' command capable of recreating the attribute."""
    def hasCategory(self, category: Any) -> bool:
        """Checks to see if the attribute has a given category"""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def removeDataType(self, *args: Any, **kwargs: Any) -> Any:
        """Removes the specified Maya data type from the list of those accepted by the attribute."""
    def removeNumericType(self, *args: Any, **kwargs: Any) -> Any:
        """Removes the specified numeric type from the list of those accepted by the attribute."""
    def removeTypeId(self, *args: Any, **kwargs: Any) -> Any:
        """Removes the specified data typeId from the list of those accepted by the attribute."""
    def setNiceNameOverride(self, localizedName: Any) -> None:
        """Sets a nice UI name for this attribute rather than using the default derived from it's long name."""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def type(self) -> int:
        """Returns the type of the function set."""

class MFnGeometryData:
    isIdentity: Any
    isNotIdentity: Any
    kAny: Any
    kAuto: Any
    kCompleteGroup: Any
    kComponentList: Any
    kDoubleArray: Any
    kDynArrayAttrs: Any
    kDynSweptGeometry: Any
    kEdges: Any
    kEmptyGroup: Any
    kFaces: Any
    kFalloffFunction: Any
    kFloatArray: Any
    kIntArray: Any
    kInvalid: Any
    kInvalidGroup: Any
    kLast: Any
    kLattice: Any
    kMatrix: Any
    kMatrixArray: Any
    kMesh: Any
    kNId: Any
    kNObject: Any
    kNull: Any
    kNumeric: Any
    kNurbsCurve: Any
    kNurbsSurface: Any
    kPartialGroup: Any
    kPlugin: Any
    kPluginGeometry: Any
    kPointArray: Any
    kSphere: Any
    kString: Any
    kStringArray: Any
    kSubdSurface: Any
    kUnsupported: Any
    kVectorArray: Any
    kVerts: Any
    matrix: Any
    objectGroupCount: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addComponentTag(self, key: Any) -> MFnGeometryData:
        """Adds a componentTag with the given key to the object."""
    def addObjectGroup(self, id: int) -> MFnGeometryData:
        """Adds an object group with the given id to the object."""
    def addObjectGroupComponent(self, id: int, arg: Any) -> MFnGeometryData:
        """Adds the members of the given component to the object group"""
    def changeObjectGroupId(self, sourceId: int, destId: int) -> MFnGeometryData:
        """Changes the id of the object group with the given id to the new id."""
    def componentTagContents(self, key: Any) -> MObject:
        """Returns a component which contains the members of the componentTag"""
    def componentTagExpressionSubsetState(self, expr: Any, ctg: Any) -> Any:
        """Returns the state of the contents of the resolved componentTag expression."""
    def componentTagType(self, key: Any) -> Any:
        """Returns the type of the component that the componentTag with the"""
    def componentTags(self) -> MObject:
        """Returns the componentTag keys contained in the object."""
    def copyObjectGroups(self, arg: Any) -> MFnGeometryData:
        """Copies the object groups from the given geometry data object."""
    def hasComponentTag(self, key: Any) -> bool:
        """Returns True if a componentTag with the given key exists."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def hasObjectGroup(self, id: int) -> MFnGeometryData:
        """Returns True if an object group with the given id is"""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def objectGroup(self, index: int) -> int:
        """Returns the id of the index'th object group contained by the object."""
    def objectGroupComponent(self, id: int) -> MObject:
        """Returns a component which contains the members of the object group"""
    def objectGroupSubsetState(self, id: int) -> Any:
        """Returns the state of the group contents of the object group with the"""
    def objectGroupType(self, id: int) -> Any:
        """Returns the type of the component that the object group with the"""
    def removeComponentTag(self, key: Any) -> MFnGeometryData:
        """Removes a componentTag with the given key from the object."""
    def removeObjectGroup(self, id: int) -> MFnGeometryData:
        """Removes an object group with the given id from the object."""
    def removeObjectGroupComponent(self, id: int, arg: Any) -> MFnGeometryData:
        """Removes the members of the given component from the object group"""
    def renameComponentTag(self, key: Any, newKey: Any) -> MFnGeometryData:
        """Renames a componentag with the given key the object."""
    def resolveComponentTagExpression(self, key: Any, ctg: Any) -> MObject:
        """Returns a component which is the result of the resolved componentTag expression"""
    def setComponentTagContents(self, key: Any, arg: Any) -> MFnGeometryData:
        """Sets the members of the componentTag with the given key"""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def setObjectGroupComponent(self, id: int, arg: Any) -> MFnGeometryData:
        """Sets the members of the object group with the given id"""
    def type(self) -> int:
        """Returns the type of the function set."""

class MFnIntArrayData:
    kAny: Any
    kComponentList: Any
    kDoubleArray: Any
    kDynArrayAttrs: Any
    kDynSweptGeometry: Any
    kFalloffFunction: Any
    kFloatArray: Any
    kIntArray: Any
    kInvalid: Any
    kLast: Any
    kLattice: Any
    kMatrix: Any
    kMatrixArray: Any
    kMesh: Any
    kNId: Any
    kNObject: Any
    kNumeric: Any
    kNurbsCurve: Any
    kNurbsSurface: Any
    kPlugin: Any
    kPluginGeometry: Any
    kPointArray: Any
    kSphere: Any
    kString: Any
    kStringArray: Any
    kSubdSurface: Any
    kVectorArray: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def array(self) -> MIntArray:
        """Returns the encapsulated array as an MIntArray."""
    def copyTo(self) -> None:
        """Replaces the elements of an array with those in the encapsulated array."""
    def create(self, in_: MIntArray | None = None) -> MObject:
        """Creates a new int array data object."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def set(self, element: int | MIntArray, index: int) -> None:
        """Sets values in the encapsulated array."""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def type(self) -> int:
        """Returns the type of the function set."""

class MFnLightDataAttribute:
    affectsAppearance: Any
    affectsWorldSpace: Any
    array: Any
    cached: Any
    channelBox: Any
    connectable: Any
    default: Any
    disconnectBehavior: Any
    dynamic: Any
    extension: Any
    hidden: Any
    indeterminant: Any
    indexMatters: Any
    internal: Any
    isProxyAttribute: Any
    kDelete: Any
    kNothing: Any
    kReset: Any
    keyable: Any
    name: Any
    parent: Any
    readable: Any
    renderSource: Any
    shortName: Any
    storable: Any
    usedAsColor: Any
    usedAsFilename: Any
    usesArrayDataBuilder: Any
    worldSpace: Any
    writable: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def accepts(self, type: int | MTypeId) -> bool:
        """Returns True if this attribute can accept a connection of the given type."""
    def acceptsAttribute(self, attr: MFnAttribute) -> bool:
        """Returns True if this attribute can accept a connection with the given attribute."""
    def addToCategory(self, category: Any) -> None:
        """Adds the attribute to a category"""
    def child(self, index: int) -> MObject:
        """Returns one of the attribute's children, specified by index."""
    def create(self, fullName: Any, briefName: Any, direction: MObject, intensity: MObject, ambient: MObject, diffuse: MObject, specular: MObject, shadowFraciton: MObject, preShadowIntensity: MObject, blindData: MObject) -> MObject:
        """Creates a new light data attribute, attaches it to the function set and returns it as an MObject."""
    def getAddAttrCmd(self, useLongName: bool | None = None) -> Any:
        """Returns a string containing a MEL 'addAttr' command capable of recreating the attribute."""
    def hasCategory(self, category: Any) -> bool:
        """Checks to see if the attribute has a given category"""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def setNiceNameOverride(self, localizedName: Any) -> None:
        """Sets a nice UI name for this attribute rather than using the default derived from it's long name."""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def type(self) -> int:
        """Returns the type of the function set."""

class MFnMatrixArrayData:
    kAny: Any
    kComponentList: Any
    kDoubleArray: Any
    kDynArrayAttrs: Any
    kDynSweptGeometry: Any
    kFalloffFunction: Any
    kFloatArray: Any
    kIntArray: Any
    kInvalid: Any
    kLast: Any
    kLattice: Any
    kMatrix: Any
    kMatrixArray: Any
    kMesh: Any
    kNId: Any
    kNObject: Any
    kNumeric: Any
    kNurbsCurve: Any
    kNurbsSurface: Any
    kPlugin: Any
    kPluginGeometry: Any
    kPointArray: Any
    kSphere: Any
    kString: Any
    kStringArray: Any
    kSubdSurface: Any
    kVectorArray: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def array(self) -> MMatrixArray:
        """Returns the encapsulated array as an MMatrixArray."""
    def copyTo(self) -> None:
        """Replaces the elements of an array with those in the encapsulated array."""
    def create(self, in_: MMatrixArray | None = None) -> MObject:
        """Creates a new MMatrix array data object."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def set(self, index: int | MMatrixArray) -> MMatrix | None:
        """Sets values in the encapsulated array."""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def type(self) -> int:
        """Returns the type of the function set."""

class MFnMatrixAttribute:
    affectsAppearance: Any
    affectsWorldSpace: Any
    array: Any
    cached: Any
    channelBox: Any
    connectable: Any
    default: Any
    disconnectBehavior: Any
    dynamic: Any
    extension: Any
    hidden: Any
    indeterminant: Any
    indexMatters: Any
    internal: Any
    isProxyAttribute: Any
    kDelete: Any
    kDouble: Any
    kFloat: Any
    kNothing: Any
    kReset: Any
    keyable: Any
    name: Any
    parent: Any
    readable: Any
    renderSource: Any
    shortName: Any
    storable: Any
    usedAsColor: Any
    usedAsFilename: Any
    usesArrayDataBuilder: Any
    worldSpace: Any
    writable: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def accepts(self, type: int | MTypeId) -> bool:
        """Returns True if this attribute can accept a connection of the given type."""
    def acceptsAttribute(self, attr: MFnAttribute) -> bool:
        """Returns True if this attribute can accept a connection with the given attribute."""
    def addToCategory(self, category: Any) -> None:
        """Adds the attribute to a category"""
    def create(self, fullName: Any, briefName: Any, matrixType: Any = None) -> MObject:
        """Creates a new matrix attribute, attaches it to the function set and returns it as an MObject."""
    def getAddAttrCmd(self, useLongName: bool | None = None) -> Any:
        """Returns a string containing a MEL 'addAttr' command capable of recreating the attribute."""
    def hasCategory(self, category: Any) -> bool:
        """Checks to see if the attribute has a given category"""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def setNiceNameOverride(self, localizedName: Any) -> None:
        """Sets a nice UI name for this attribute rather than using the default derived from it's long name."""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def type(self) -> int:
        """Returns the type of the function set."""

class MFnMatrixData:
    kAny: Any
    kComponentList: Any
    kDoubleArray: Any
    kDynArrayAttrs: Any
    kDynSweptGeometry: Any
    kFalloffFunction: Any
    kFloatArray: Any
    kIntArray: Any
    kInvalid: Any
    kLast: Any
    kLattice: Any
    kMatrix: Any
    kMatrixArray: Any
    kMesh: Any
    kNId: Any
    kNObject: Any
    kNumeric: Any
    kNurbsCurve: Any
    kNurbsSurface: Any
    kPlugin: Any
    kPluginGeometry: Any
    kPointArray: Any
    kSphere: Any
    kString: Any
    kStringArray: Any
    kSubdSurface: Any
    kVectorArray: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def create(self) -> MObject:
        """Creates a new matrix data object."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def isTransformation(self) -> bool:
        """Returns True if the attached object is an MTransformationMatrix, False if it is an MMatrix."""
    def matrix(self) -> MMatrix:
        """Returns the encapsulated matrix as an MMatrix."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def set(self, transformation: MTransformationMatrix | MMatrix) -> None:
        """Sets the value of the encapsulated matrix."""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def transformation(self) -> MTransformationMatrix:
        """Returns the encapsulated matrix as an MTransformationMatrix."""
    def type(self) -> int:
        """Returns the type of the function set."""

class MFnMesh:
    boundingBox: Any
    checkSamePointTwice: Any
    displayColors: Any
    inModel: Any
    inUnderWorld: Any
    isDefaultNode: Any
    isFromReferencedFile: Any
    isInstanceable: Any
    isIntermediateObject: Any
    isLocked: Any
    isShared: Any
    kAlpha: Any
    kDifference: Any
    kEdgeClassification: Any
    kExtensionAttr: Any
    kGeomBorder: Any
    kInstanceUnspecified: Any
    kInternalPoint: Any
    kIntersectTolerance: Any
    kIntersection: Any
    kInvalid: Any
    kInvalidAttr: Any
    kLocalDynamicAttr: Any
    kNextPos: Any
    kNormalAttr: Any
    kNormalClassification: Any
    kOnEdge: Any
    kPointTolerance: Any
    kRGB: Any
    kRGBA: Any
    kSharedUV: Any
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
    kUVBorder: Any
    kUnion: Any
    kUnsharedUV: Any
    namespace: Any
    numColorSets: Any
    numEdges: Any
    numFaceVertices: Any
    numNormals: Any
    numPolygons: Any
    numUVSets: Any
    numVertices: Any
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
    def addChild(self, node: int, index: bool, keepExistingParents: bool = False) -> MFnMesh:
        """Makes a node a child of this one."""
    def addExternalContentForFileAttr(self, attr: MObject) -> MExternalContentInfoTable:
        """Adds content info to the specified table from a file path attribute."""
    def addHoles(self, faceIndex: int, vertices: MPointArray, loopCounts: MIntArray, pointTolerance: float, mergeVertices: bool = True) -> MFnMesh:
        """Adds holes to a mesh polygon."""
    def addPolygon(self, vertices: MPointArray, pointTolerance: float | bool | int, mergeVertices: bool = True, loopCounts: MObject | float | bool | None = None) -> Any:
        """Adds a new polygon to the mesh, returning the index of the new"""
    def affectsAnimation(self) -> bool:
        """Returns true if the changes to the node may affect animation."""
    def allIntersections(self, raySource: MFloatPoint, rayDirection: MFloatVector, faceIds: MIntArray, triIds: MIntArray, idsSorted: bool, space: int, maxParam: float, testBothDirections: bool, accelerator: MMeshIsectAccelParams, sortHits: bool, hitPoints: MFloatPointArray, hitRayParams: MFloatArray, hitFaces: MIntArray, hitTriangles: MIntArray, hitBary1: MFloatArray, hitBary2: MFloatArray, tolerance: float | None = None) -> bool:
        """allIntersections(raySource, rayDirection, space, maxParam,"""
    @staticmethod
    def allocateFlag(pluginName: Any) -> int:
        """Allocates a flag on all nodes for use by the named plugin and returns the flag's index."""
    def anyIntersection(self, raySource: MFloatPoint, rayDirection: MFloatVector, faceIds: MIntArray, triIds: MIntArray, idsSorted: bool, space: int, maxParam: float, testBothDirections: bool, accelerator: MMeshIsectAccelParams, hitPoint: MFloatPoint, hitRayParam: float, hitFace: int, hitTriangle: int, hitBary1: float, hitBary2: float, tolerance: float | None = None) -> bool:
        """anyIntersection(raySource, rayDirection, space, maxParam,"""
    def assignColor(self, faceId: int, vertexIndex: int, colorId: int, colorSet: Any = '') -> MFnMesh:
        """Assigns a color from a colorSet to a specified vertex of a face."""
    def assignColors(self, colorIds: MIntArray, colorSet: Any) -> MFnMesh:
        """Assigns colors to all of the mesh's face-vertices. The colorIds"""
    def assignUV(self, faceId: int, vertexIndex: int, uvId: int, uvSet: Any = '') -> MFnMesh:
        """Assigns a UV coordinate from a uvSet to a specified vertex of a face."""
    def assignUVs(self, uvCounts: MIntArray, uvIds: MIntArray, uvSet: Any = '') -> MFnMesh:
        """Assigns UV coordinates to the mesh's face-vertices."""
    def attribute(self, index: Any) -> MObject:
        """Returns an attribute of the node, given either its index or name."""
    def attributeClass(self, attr: MObject) -> Any:
        """Returns the class of the specified attribute."""
    def attributeCount(self) -> int:
        """Returns the number of attributes on the node."""
    @staticmethod
    def autoUniformGridParams() -> MMeshIsectAccelParams:
        """Creates an object which specifies a uniform voxel grid structure"""
    def booleanOp(self, op: Any) -> tuple[Any]:
        """(Deprecated: Please use booleanOps instead) booleanOp(Boolean Operation constant, MFnMesh, MFnMesh) -> self"""
    def booleanOps(self, arg: Any, MObjectArray: MObjectArray, bool: bool) -> MFnMesh:
        """Replaces this mesh's geometry with the result of a boolean operation"""
    def cachedIntersectionAcceleratorInfo(self) -> Any:
        """Retrieves a string that describes the intersection acceleration"""
    def canBeWritten(self) -> bool:
        """Returns true if the node will be written to file."""
    def child(self, index: int) -> MObject:
        """Returns the specified child of this node."""
    def childCount(self) -> int:
        """Returns the number of nodes which are children of this one."""
    @staticmethod
    def classification(nodeTypeName: Any) -> Any:
        """Returns the classification string for the named node type."""
    def cleanupEdgeSmoothing(self) -> MFnMesh:
        """Updates the mesh after setEdgeSmoothing has been done. This should"""
    def clearBlindData(self, compType: int) -> MFnMesh:
        """clearBlindData(compType, blindDataId, compId=None, attr='') -> self"""
    def clearColors(self, colorSet: Any = '') -> MFnMesh:
        """Clears out all colors from a colorSet, and leaves behind an empty"""
    @staticmethod
    def clearGlobalIntersectionAcceleratorInfo() -> Any:
        """Clears the 'total count', 'total build time', and 'peak memory'"""
    def clearUVs(self, uvSet: Any = '') -> MFnMesh:
        """Clears out all uvs from a uvSet, and leaves behind an empty"""
    def closestIntersection(self, raySource: MFloatPoint, rayDirection: MFloatVector, faceIds: MIntArray, triIds: MIntArray, idsSorted: bool, space: int, maxParam: float, testBothDirections: bool, accelerator: MMeshIsectAccelParams, hitPoint: MFloatPoint, hitRayParam: float, hitFace: int, hitTriangle: int, hitBary1: float, hitBary2: float, tolerance: float | None = None) -> bool:
        """closestIntersection(raySource, rayDirection, space, maxParam,"""
    def collapseEdges(self, arg: Any) -> MFnMesh:
        """Collapses edges into vertices. The two vertices that create each"""
    def collapseFaces(self, arg: Any) -> MFnMesh:
        """Collapses faces into vertices. Adjacent faces will be collapsed"""
    def copy(self, MObject: MObject, parent: MObject) -> MObject:
        """Creates a new mesh with the same geometry as the source. Raises"""
    def copyInPlace(self, MObject: MObject) -> MFnMesh:
        """Replaces the current mesh's geometry with that from the source."""
    def copyUVSet(self, fromName: Any, toName: Any, modifier: Any = None) -> Any:
        """Copies the contents of one UV set into another."""
    def create(self, vertices: Any, polygonCounts: Any, polygonConnects: MFloatPointArray | MPointArray | MIntArray | MObject, parent: MObject | bool | MFloatArray, edges: MObject | MFloatArray, edgeConnectsCount: MObject, edgeFaceConnects: Any, edgeFaceDesc: Any, parent_: Any, edges_: Any, polygonCounts_: Any, polygonConnects_: Any, parent__: Any, uValues: MIntArray | None = None, vValues: MIntArray | MObject | MFloatArray | None = None, storeDoubles: bool = False, uValues_: Any = None, vValues_: Any = None) -> MObject:
        """Creates a new polygonal mesh and sets this function set to operate"""
    def createBlindDataType(self, blindDataId: int, arg: Any) -> MFnMesh:
        """Create a new blind data type with the specified attributes."""
    def createColorSet(self, name: MUintArray | bool, clamped: Any, rep: MUintArray, modifier: Any = None, instances: Any = None) -> Any:
        """Creates a new, empty color set for this mesh."""
    def createInPlace(self, vertices: int | MPointArray | MFloatPointArray, polygonCounts: int | MIntArray, arg: MFloatPointArray | MIntArray, edges: MIntArray, polygonCounts_: MIntArray, polygonConnects: Any) -> MFnMesh:
        """Replaces the existing polygonal mesh with a new one. This method is"""
    def createUVSet(self, name: MUintArray, modifier: Any = None, instances: Any = None) -> Any:
        """Creates a new, empty UV set for this mesh."""
    def currentColorSetName(self, instance: int) -> Any:
        """Get the name of the 'current' color set. The current color set is"""
    def currentUVSetName(self, instance: int) -> Any:
        """Get the name of the 'current' uv set. The current uv set is"""
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
    def deleteColorSet(self, colorSet: Any, modifier: Any = None, currentSelection: Any = None) -> MFnMesh:
        """Deletes a color set from the mesh."""
    def deleteEdge(self, edgeId: int, modifier: Any = None) -> MFnMesh:
        """Deletes the specified edge."""
    def deleteFace(self, faceId: int, modifier: Any = None) -> MFnMesh:
        """Deletes the specified face."""
    def deleteUVSet(self, uvSet: Any, modifier: Any = None, currentSelection: Any = None) -> MFnMesh:
        """Deletes a uv set from the mesh."""
    def deleteVertex(self, vertexId: int, modifier: Any = None) -> MFnMesh:
        """Deletes the specified vertex."""
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
    def duplicateFaces(self, faces: Any, translation: Any = None) -> MFnMesh:
        """Duplicates a set of faces and detaches them from the rest of the"""
    def edgeBorderInfo(self, edgeId: int, setId: int = 0) -> Any:
        """Returns if the specified edge is on geom/UV shell border or has shared/unshared UVs."""
    def extractFaces(self, faces: Any, translation: Any = None) -> MFnMesh:
        """Detaches a set of faces from the rest of the mesh. The resulting"""
    def extrudeEdges(self, edges: int, extrusionCount: int = 1, translation: float | None = None, extrudeTogether: bool = True, thickness: float = 0.0, offset: float = 0.0) -> MFnMesh:
        """Extrude the given edges along a vector. The resulting mesh will have"""
    def extrudeFaces(self, faces: int, extrusionCount: int = 1, translation: float | None = None, extrudeTogether: bool = True, thickness: float = 0.0, offset: float = 0.0) -> MFnMesh:
        """Extrude the given faces along a vector. The resulting mesh will have"""
    def findAlias(self, alias: Any, attrObj: MObject) -> bool:
        """Returns the attribute which has the given alias."""
    def findPlug(self, attr: Any, wantNetworkedPlug: bool) -> MPlug:
        """Returns a plug for the given attribute."""
    def freeCachedIntersectionAccelerator(self) -> MFnMesh:
        """If the mesh has a cached intersection accelerator structure, then"""
    def fullPathName(self) -> Any:
        """Returns the full path of the attached object, from the root of the DAG on down."""
    def generateSmoothMesh(self, parent: MObject, options: MMeshSmoothOptions | None = None) -> MObject:
        """Creates a new polygonal mesh which is a smoothed version of the one"""
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
    def getAssignedUVs(self, uvSet: Any, uvIds: Any) -> Any:
        """Returns a tuple containing all of the UV assignments for the specified"""
    def getAssociatedColorSetInstances(self, colorSet: Any) -> MIntArray:
        """Returns the instance numbers associated with the specified Color set."""
    def getAssociatedUVSetInstances(self, uvSet: Any) -> MIntArray:
        """Returns the instance numbers associated with the specified UV set."""
    def getAssociatedUVSetTextures(self, uvSet: Any) -> MObjectArray:
        """Returns the texture nodes which are using the specified UV set. If"""
    def getBinaryBlindData(self, compId: int, compType: int, blindDataId: Any, attr: Any) -> Any:
        """getBinaryBlindData(compType, blindDataId, attr)"""
    def getBinormals(self, space: int | None = None, uvSet: Any = '') -> MFloatVectorArray:
        """Returns the binormal vectors for all face-vertices."""
    def getBlindDataAttrNames(self, arg: int, arg_: Any) -> Any:
        """Returns a tuple listing the attributes of the given blind data type."""
    def getBlindDataTypes(self, arg: int) -> MIntArray:
        """Returns all the blind data ID's associated with the given component"""
    def getBoolBlindData(self, compId: int, compType: int, blindDataId: Any, attr: Any) -> bool:
        """getBoolBlindData(compType, blindDataId, attr) -> (MIntArray, MIntArray)"""
    def getClosestNormal(self, MPoint: MPoint, space: int, int: Any) -> Any:
        """Returns a tuple containing the normal at the closest point on the"""
    def getClosestPoint(self, MPoint: MPoint, space: int, int: Any) -> Any:
        """Returns a tuple containing the closest point on the mesh to the"""
    def getClosestPointAndNormal(self, MPoint: MPoint, space: int | None = None) -> Any:
        """-> (MPoint, MVector, int)"""
    def getClosestUVs(self, u: Any, v: Any, uvSet: Any = '') -> MIntArray:
        """Returns the IDs of the UVs which are nearest in uv space to the"""
    def getColor(self, colorId: int, colorSet: Any = '') -> MColor:
        """Returns a color from a colorSet. Raises IndexError if the colorId is"""
    def getColorIndex(self, faceId: int, localVertexId: int, colorSet: Any = '') -> int:
        """Returns the index into the specified colorSet of the color used by a"""
    def getColorRepresentation(self, colorSet: Any) -> Any:
        """Returns the Color Representation used by the specified color set."""
    def getColorSetFamilyNames(self, arg: Any, arg_: Any) -> Any:
        """Returns the names of all of the color set families on this object. A"""
    def getColorSetNames(self, arg: Any, arg_: Any) -> Any:
        """Returns the names of all the color sets on this object."""
    def getColorSetsInFamily(self, arg: Any, arg_: Any) -> Any:
        """Returns the names of all of the color sets that belong to the"""
    def getColors(self, colorSet: Any = '') -> MColorArray:
        """Returns all of the colors in a colorSet. If no colorSet is specified"""
    def getConnectedSetsAndMembers(self, instance: int, arg: bool, MObjectArray: Any) -> Any:
        """Returns a tuple containing an array of sets and an array of the"""
    def getConnectedShaders(self, arg: int, MIntArray: Any) -> Any:
        """Returns a tuple containing an array of shaders (sets) and an array"""
    def getConnections(self) -> MPlugArray:
        """Returns all the plugs which are connected to attributes of this node."""
    def getCreaseEdges(self, arg: Any, MDoubleArray: Any) -> Any:
        """Returns a tuple containing two arrays. The first contains the mesh-"""
    def getCreaseVertices(self, arg: Any, MDoubleArray: Any) -> Any:
        """Returns a tuple containing two arrays. The first contains the mesh-"""
    def getDoubleBlindData(self, compId: int, compType: int, blindDataId: Any, attr: Any) -> float:
        """getDoubleBlindData(compType, blindDataId, attr) -> (MIntArray, MDoubleArray)"""
    def getEdgeVertices(self, arg: int, int: Any) -> Any:
        """Returns a tuple containing the mesh-relative/global IDs of the"""
    def getExternalContent(self) -> MExternalContentInfoTable:
        """Gets the external content (files) that this node depends on."""
    def getFaceAndVertexIndices(self, faceVertexIndex: Any, localVertex: Any, int: Any) -> Any:
        """Returns a tuple containg the faceId and vertexIndex represented by"""
    def getFaceNormalIds(self, faceId: int) -> MIntArray:
        """Returns the IDs of the normals for all the vertices of a given face."""
    def getFaceUVSetNames(self, arg: int, arg_: Any) -> Any:
        """Returns the names of all of the uv sets mapped to the specified face."""
    def getFaceVertexBinormal(self, faceId: int, vertexId: int, space: int | None = None, uvSet: Any = '') -> MVector:
        """Returns the binormal vector at a given face vertex."""
    def getFaceVertexBinormals(self, faceId: int, space: int | None = None, uvSet: Any = '') -> MFloatVectorArray:
        """Returns all the per-vertex-per-face binormals for a given face."""
    def getFaceVertexColors(self, colorSet: Any = '', defaultUnsetColor: MColor | None = None) -> MColorArray:
        """Returns colors for all the mesh's face-vertices."""
    def getFaceVertexIndex(self, faceId: Any, vertexIndex: Any, localVertex: bool = True) -> int:
        """Returns the index for a specific face-vertex into an array of face-"""
    def getFaceVertexNormal(self, faceId: int, vertexId: int, space: int | None = None) -> MVector:
        """Returns the per-vertex-per-face normal for a given face and vertex."""
    def getFaceVertexNormals(self, faceId: int, space: int | None = None) -> MFloatVectorArray:
        """Returns the normals for a given face."""
    def getFaceVertexTangent(self, faceId: int, vertexId: int, space: int | None = None, uvSet: Any = '') -> MVector:
        """Return the normalized tangent vector at a given face vertex."""
    def getFaceVertexTangents(self, faceId: int, space: int | None = None, uvSet: Any = '') -> MFloatVectorArray:
        """Returns all the per-vertex-per-face tangents for a given face."""
    def getFloatBlindData(self, compId: int, compType: int, blindDataId: Any, attr: Any) -> float:
        """getFloatBlindData(compType, blindDataId, attr) -> (MIntArray, MFloatArray)"""
    def getFloatPoints(self, space: Any = None) -> MFloatPointArray:
        """Returns an MFloatPointArray containing the mesh's vertices."""
    def getHoles(self, arg: MIntArray, arg_: MIntArray, arg__: Any) -> Any:
        """Returns a tuple describing the holes in the mesh. Each element of the"""
    def getIntBlindData(self, compId: int, compType: int, blindDataId: Any, attr: Any) -> int:
        """getIntBlindData(compType, blindDataId, attr) -> (MIntArray, MIntArray)"""
    def getInvisibleFaces(self) -> MUintArray:
        """Returns the invisible faces of the mesh. Invisible faces are like"""
    def getMeshShellsIds(self, arg: int, MIntArray: Any) -> Any:
        """Returns a tuple containing describing how the specified component type items"""
    def getNormalIds(self, arg: Any, MIntArray: Any) -> Any:
        """Returns the normal IDs for all of the mesh's polygons as a tuple of"""
    def getNormals(self, space: int | None = None) -> MFloatVectorArray:
        """Returns a copy of the mesh's normals. The normals are the per-polygon"""
    def getPath(self) -> MDagPath:
        """Returns the DAG path to which this function set is attached, or the first path to the node if the function set is attached to an MObject."""
    def getPoint(self, vertexId: int, space: int | None = None) -> MPoint:
        """Returns the position of specified vertex."""
    def getPointAtUV(self, faceId: int, u: int, v: Any, space: float | None = None, uvSet: Any = '', tolerance: float = 0.0) -> MPoint:
        """Returns the position of the point at the give UV value in the"""
    def getPoints(self, space: int | None = None) -> MPointArray:
        """Returns a copy of the mesh's vertex positions as an MPointArray."""
    def getPointsAtUV(self, u: Any, v: int, tolerance: Any, MPointArray: Any, space: Any = None, uvSet: Any = '') -> Any:
        """Returns the polygon ids and positions of points at the given UV position on the mesh."""
    def getPolygonNormal(self, polygonId: int, space: int | None = None) -> MVector:
        """Returns the per-polygon normal for the given polygon."""
    def getPolygonTriangleVertices(self, polygonId: int, arg: int, int: Any, int_: Any) -> Any:
        """Returns the mesh-relative/global IDs of the 3 vertices of the"""
    def getPolygonUV(self, polygonId: int, vertexId: int, uvSet: Any, float: Any) -> Any:
        """Returns a tuple containing the U and V values at a specified vertex"""
    def getPolygonUVid(self, polygonId: int, vertexId: int, uvSet: Any = '') -> int:
        """Returns the ID of the UV at a specified vertex of a specified polygon."""
    def getPolygonVertices(self, polygonIndex: int) -> MIntArray:
        """Returns the mesh-relative/global vertex IDs the specified polygon."""
    def getSmoothMeshDisplayOptions(self) -> MMeshSmoothOptions:
        """Returns the options currently in use when smoothing the mesh for display."""
    def getStringBlindData(self, compId: int, compType: int, blindDataId: Any, attr: Any) -> Any:
        """getStringBlindData(compType, blindDataId, attr)"""
    def getTangentId(self, faceId: int, vertexId: int) -> int:
        """Returns the ID of the tangent for a given face and vertex."""
    def getTangents(self, space: int | None = None, uvSet: Any = '') -> MFloatVectorArray:
        """Return the tangent vectors for all face vertices. The tangent is"""
    def getTriangleOffsets(self, arg: Any, MIntArray: Any) -> Any:
        """Returns the number of triangles for every polygon face and the"""
    def getTriangles(self, arg: Any, MIntArray: Any) -> Any:
        """Returns a tuple describing the mesh's triangulation. The first"""
    def getUV(self, uvId: int, uvSet: Any, float: Any) -> Any:
        """Returns a tuple containing the u and v values of the specified UV."""
    def getUVAtPoint(self, point: int, uvSet: Any, float: Any, int: Any, space: Any = None) -> Any:
        """Returns a tuple containing the u and v coordinates of the point on"""
    def getUVBorderEdges(self, setId: int) -> MIntArray:
        """Retrieves the edge indices for edges lying on a UV border."""
    def getUVSetFamilyNames(self, arg: Any, arg_: Any) -> Any:
        """Returns the names of all of the uv set families on this object. A"""
    def getUVSetNames(self, arg: Any, arg_: Any) -> Any:
        """Returns the names of all the uv sets on this object."""
    def getUVSetsInFamily(self, arg: Any, arg_: Any) -> Any:
        """Returns the names of all of the uv sets that belong to the"""
    def getUVs(self, uvSet: Any, MFloatArray: Any) -> Any:
        """Returns a tuple containing an array of U values and an array of V"""
    def getUvShellsIds(self, uvSet: Any, MIntArray: Any) -> Any:
        """Returns a tuple containing describing how the specified UV set's UVs"""
    def getVertexColors(self, colorSet: Any = '', defaultUnsetColor: MColor | None = None) -> MColorArray:
        """Gets colors for all vertices of the given colorSet. If no face has"""
    def getVertexNormal(self, vertexId: int, angleWeighted: int | bool, space: int | None = None) -> MVector:
        """Returns the normal at the given vertex. The returned normal is a"""
    def getVertexNormals(self, angleWeighted: bool, space: int | None = None) -> MFloatVectorArray:
        """Returns all the vertex normals. The returned normals are per-vertex"""
    def getVertices(self, arg: Any, MIntArray: Any) -> Any:
        """Returns the mesh-relative/global vertex IDs for all of the mesh's"""
    @staticmethod
    def globalIntersectionAcceleratorsInfo() -> Any:
        """Returns a string that describes the system-wide resource usage for"""
    def hasAlphaChannels(self, colorSet: Any) -> bool:
        """Returns True if the color set has an alpha channel."""
    def hasAttribute(self, name: Any) -> bool:
        """Returns True if the node has an attribute with the given name."""
    def hasBlindData(self, compType: int, compId: int | None = None, blindDataId: int | None = None) -> bool:
        """Returns true if any component of the given type on this mesh has"""
    def hasChild(self, node: MObject) -> bool:
        """Returns True if the specified node is a child of this one."""
    def hasColorChannels(self, colorSet: Any) -> bool:
        """Returns True if the color set has RGB channels."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def hasParent(self, node: MObject) -> bool:
        """Returns True if the specified node is a parent of this one."""
    def hasUniqueName(self) -> bool:
        """Returns True if the node's name is unique."""
    def instanceCount(self, indirect: bool) -> int:
        """Returns the number of instances for this node."""
    def intersectFaceAtUV(self, u: Any, v: Any, uvSet: Any = '') -> int:
        """Returns the IDs of the UVs on this surface which are nearest"""
    def isBlindDataTypeUsed(self, blindDataId: int) -> bool:
        """Returns True if the blind data type is already in use anywhere in the scene."""
    def isChildOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a parent of this one."""
    def isColorClamped(self, colorSet: Any) -> bool:
        """Returns True if the color sets RGBA components are clamped to the"""
    def isColorSetPerInstance(self, colorSet: Any) -> bool:
        """Returns True if the color set is per-instance, and False if it is"""
    def isEdgeSmooth(self, edgeId: int) -> bool:
        """Returns True if the edge is smooth, False if it is hard."""
    def isFlagSet(self, flag: int) -> bool:
        """Returns the state of the specified node flag."""
    def isInstanced(self, indirect: bool = True) -> bool:
        """Returns True if this node is instanced."""
    def isInstancedAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute is an instanced attribute of this node."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files."""
    def isNormalLocked(self, normalId: int) -> bool:
        """Returns True if the normal is locked, False otherwise."""
    def isParentOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a child of this one."""
    def isPolygonConvex(self, faceId: int) -> bool:
        """Returns True if the polygon is convex, False if it is concave."""
    def isPolygonUVReversed(self, faceId: int) -> bool:
        """Returns True if the texture coordinates (uv's) for specified polygon are"""
    def isRightHandedTangent(self, tangentId: int, uvSet: Any = '') -> bool:
        """Returns True if the normal, tangent, and binormal form a right handed"""
    def isTrackingEdits(self) -> bool:
        """Returns True if the node is referenced or in an assembly that is tracking edits."""
    def isUVSetPerInstance(self, uvSet: Any) -> bool:
        """Returns True if the UV set is per-instance, and False if it is shared"""
    def lockFaceVertexNormals(self, arg: Any, arg_: Any) -> MFnMesh:
        """Locks the normals for the given face/vertex pairs."""
    def lockVertexNormals(self, arg: Any) -> MFnMesh:
        """Locks the shared normals for the specified vertices."""
    def name(self) -> Any:
        """Returns the node's name."""
    def numColors(self, colorSet: Any = '') -> int:
        """Returns the number of colors in the given color set. If no color set"""
    def numUVs(self, uvSet: Any = '') -> int:
        """Returns the number of UVs (texture coordinates) in the given UV set."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def onBoundary(self, faceId: int) -> bool:
        """Returns true if the face is on the border of the mesh, meaning that"""
    def parent(self, index: int) -> MObject:
        """Returns the specified parent of this node."""
    def parentCount(self) -> int:
        """Returns the number of parents this node has."""
    def partialPathName(self) -> Any:
        """Returns the minimum path string necessary to uniquely identify the attached object."""
    def plugsAlias(self, plug: MPlug) -> Any:
        """Returns the alias for a plug's attribute."""
    def polygonVertexCount(self, faceId: int) -> int:
        """Returns the number of vertices in the given polygon. Raises"""
    def removeAttribute(self, attr: MObject, type: Any) -> None:
        """Removes a dynamic attribute from the node."""
    def removeChild(self, node: Any) -> MFnMesh:
        """Removes the child, specified by MObject, reparenting it under the world."""
    def removeChildAt(self, index: int) -> MFnMesh:
        """Removes the child, specified by index, reparenting it under the world."""
    def removeFaceColors(self, arg: Any) -> MFnMesh:
        """Removes colors from all vertices of the specified faces."""
    def removeFaceVertexColors(self, arg: Any, arg_: Any) -> MFnMesh:
        """Removes colors from the specified face/vertex pairs."""
    def removeVertexColors(self, arg: Any) -> MFnMesh:
        """Removes colors from the specified vertices in all of the faces which"""
    def renameUVSet(self, origName: Any, newName: Any, modifier: Any = None) -> MFnMesh:
        """Renames a UV set. The set must exist and the new name cannot be the"""
    def reorderedAttribute(self, index: int) -> MObject:
        """Returns one of the node's attribute, based on the order in which they are written to file."""
    def setAffectsAnimation(self) -> None:
        """Specifies that modifications to a node could potentially affect the animation."""
    def setAlias(self, alias: Any, name: Any, plug: MPlug, add: bool | None = None) -> bool:
        """Adds or removes an attribute alias."""
    def setBinaryBlindData(self, compId: int, compType: int, blindDataId: Any, attr: Any, data: Any) -> MFnMesh:
        """setBinaryBlindData(seq of compId, compType, blindDataId, attr, data) -> self"""
    def setBoolBlindData(self, compId: int, compType: int, blindDataId: Any, attr: Any, data: bool) -> MFnMesh:
        """setBoolBlindData(seq of compId, compType, blindDataId, attr, data) -> self"""
    def setColor(self, colorId: int, MColor: MColor, rep: Any, colorSet: Any = '') -> MFnMesh:
        """Sets a color in the specified colorSet. If no colorSet is given the"""
    def setColors(self, arg: MColorArray, rep: Any, colorSet: Any = '') -> MFnMesh:
        """Sets all the colors of the specified colorSet. If no colorSet is"""
    def setCreaseEdges(self, edgeIds: MUintArray, arg: MDoubleArray) -> MFnMesh:
        """Sets the specified edges of the mesh as crease edges."""
    def setCreaseVertices(self, edgeIds: MUintArray, arg: MDoubleArray) -> MFnMesh:
        """Sets the specified edges of the mesh as crease edges."""
    def setCurrentColorSetName(self, colorSet: Any, modifier: Any = None, currentSelection: Any = None) -> MFnMesh:
        """Sets the 'current' color set for this object. The current color set"""
    def setCurrentUVSetName(self, uvSet: Any, modifier: Any = None, currentSelection: Any = None) -> MFnMesh:
        """Sets the 'current' uv set for this object. The current uv set is the"""
    def setDoNotWrite(self, flag: bool) -> None:
        """Used to prevent the node from being written to file."""
    def setDoubleBlindData(self, compId: int, compType: int, blindDataId: Any, attr: Any, data: float) -> MFnMesh:
        """setDoubleBlindData(seq of compId, compType, blindDataId, attr, data) -> self"""
    def setEdgeSmoothing(self, edgeId: int, smooth: bool = True) -> MFnMesh:
        """Sets the specified edge to be hard or smooth. You must use the"""
    def setEdgeSmoothings(self, edgeIds: MIntArray, smooths: MIntArray) -> MFnMesh:
        """Sets the specified edges to be hard or smooth. You must use the"""
    def setExternalContent(self, table: MExternalContentLocationTable) -> None:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> None:
        """Sets content info in the specified attribute from the table."""
    def setFaceColor(self, color: int, faceId: Any, rep: Any) -> MFnMesh:
        """Sets the face-vertex color for all vertices on this face."""
    def setFaceColors(self, colors: Any, faceIds: Any, rep: Any) -> MFnMesh:
        """Sets the colors of the specified faces. For each face in the faceIds"""
    def setFaceVertexColor(self, color: int, faceId: int, vertexId: Any, rep: Any, modifier: Any = None) -> MFnMesh:
        """Sets a face-specific normal at a vertex."""
    def setFaceVertexColors(self, colors: Any, faceIds: Any, vertexIds: Any, rep: Any, modifier: Any = None) -> MFnMesh:
        """Sets the colors of the specified face/vertex pairs."""
    def setFaceVertexNormal(self, normal: int, faceId: int, vertexId: int, space: Any = None, modifier: Any = None) -> MFnMesh:
        """Sets a face-specific normal at a vertex."""
    def setFaceVertexNormals(self, space: int | None = None) -> tuple[Any]:
        """setFaceVertexNormal(normals, faceIds, vertexIds, space=MSpace.kObject) -> self"""
    def setFlag(self, flag: int, state: bool) -> None:
        """Sets the state of the specified node flag."""
    def setFloatBlindData(self, compId: int, compType: int, blindDataId: Any, attr: Any, data: float) -> MFnMesh:
        """setFloatBlindData(seq of compId, compType, blindDataId, attr, data) -> self"""
    def setIntBlindData(self, compId: int, compType: int, blindDataId: Any, attr: Any, data: int) -> MFnMesh:
        """setIntBlindData(seq of compId, compType, blindDataId, attr, data) -> self"""
    def setInvisibleFaces(self, faceIds: MUintArray, makeVisible: bool = False) -> MFnMesh:
        """Sets the specified faces of the mesh to be visible or invisible. See"""
    def setIsColorClamped(self, colorSet: Any, clamped: bool) -> MFnMesh:
        """Sets whether the color set's RGBA components should be clamped to the"""
    def setName(self, name: Any, createNamespace: bool | None = None) -> Any:
        """Sets the node's name."""
    def setNormals(self, normals: int, space: Any = None) -> MFnMesh:
        """Sets the mesh's normals (user normals)."""
    def setObject(self, arg: MDagPath | MObject) -> MFnMesh:
        """Attaches the function set to the specified node or DAG path."""
    def setPoint(self, vertexId: int, MPoint: MPoint, space: int | None = None) -> MFnMesh:
        """Sets the position of specified vertex."""
    def setPoints(self, points: MPointArray, space: int | None = None) -> None:
        """Sets the positions of the mesh's vertices. The positions may be"""
    def setSmoothMeshDisplayOptions(self, MMeshSmoothOptions: MMeshSmoothOptions) -> MFnMesh:
        """Sets the options to use when smoothing the mesh for display."""
    def setSomeColors(self, colorIds: MIntArray, colors: MColorArray, rep: Any, colorSet: Any = '') -> MFnMesh:
        """Sets specific colors in a colorSet."""
    def setSomeUVs(self, uvIds: MIntArray, uValues: MFloatArray, vValues: MFloatArray, uvSet: Any = '') -> MFnMesh:
        """Sets the specified texture coordinates (uv's) for this mesh. The uv"""
    def setStringBlindData(self, compId: int, compType: int, blindDataId: Any, attr: Any, data: Any) -> MFnMesh:
        """setStringBlindData(seq of compId, compType, blindDataId, attr, data) -> self"""
    def setUV(self, uvId: int, u: float, v: float, uvSet: Any = '') -> MFnMesh:
        """Sets the specified texture coordinate."""
    def setUVs(self, uValues: MFloatArray, vValues: MFloatArray, uvSet: Any = '') -> MFnMesh:
        """Sets all of the texture coordinates (uv's) for this mesh. The uv"""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def setVertexColor(self, color: int, vertexId: Any, rep: Any, modifier: Any = None) -> MFnMesh:
        """Sets the color for a vertex in all the faces which share it."""
    def setVertexColors(self, colors: Any, vertexIds: Any, rep: Any, modifier: Any = None) -> MFnMesh:
        """Sets the colors of the specified vertices. For each vertex in the"""
    def setVertexNormal(self, normal: int, vertexId: int, space: Any = None, modifier: Any = None) -> MFnMesh:
        """Sets the shared normal at a vertex."""
    def setVertexNormals(self, space: int | None = None) -> tuple[Any]:
        """setVertexNormal(normals, vertexIds, space=MSpace.kObject) -> self"""
    def sortIntersectionFaceTriIds(self, faceIds: Any, triIds: Any = None) -> MFnMesh:
        """Convenience routine for sorting faceIds or face/triangle ids before"""
    def split(self, arg: Any) -> MFnMesh:
        """Each tuple in the placements sequence consists of a Split Placement"""
    def subdivideEdges(self, edges: int, numDivisions: Any) -> MFnMesh:
        """Subdivides edges at regular intervals. For example, if numDivisions"""
    def subdivideFaces(self, faces: int, numDivisions: Any) -> MFnMesh:
        """Subdivides each specified face into a grid of smaller faces."""
    def syncObject(self) -> MFnMesh:
        """If a non-api operation happens that many have changed the"""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
    def type(self) -> int:
        """Returns the type of the function set."""
    @staticmethod
    def uniformGridParams(xDiv: int, yDiv: int, zDiv: int) -> MMeshIsectAccelParams:
        """Creates an object which specifies a uniform voxel grid structure"""
    def uniqueName(self) -> Any:
        """For a DAG node, the unique name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself. For a non-DAG node, the uniqueName is just its name."""
    def unlockFaceVertexNormals(self, arg: Any, arg_: Any) -> MFnMesh:
        """Unlocks the normals for the given face/vertex pairs."""
    def unlockVertexNormals(self, arg: Any) -> MFnMesh:
        """Unlocks the shared normals for the specified vertices."""
    def updateSurface(self) -> None:
        """Signal that this polygonal mesh has changed and needs to be redrawn."""
    def userNode(self) -> MPxNode:
        """Returns the MPxNode object for a plugin node."""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnMeshData:
    isIdentity: Any
    isNotIdentity: Any
    kAny: Any
    kAuto: Any
    kCompleteGroup: Any
    kComponentList: Any
    kDoubleArray: Any
    kDynArrayAttrs: Any
    kDynSweptGeometry: Any
    kEdges: Any
    kEmptyGroup: Any
    kFaces: Any
    kFalloffFunction: Any
    kFloatArray: Any
    kIntArray: Any
    kInvalid: Any
    kInvalidGroup: Any
    kLast: Any
    kLattice: Any
    kMatrix: Any
    kMatrixArray: Any
    kMesh: Any
    kNId: Any
    kNObject: Any
    kNull: Any
    kNumeric: Any
    kNurbsCurve: Any
    kNurbsSurface: Any
    kPartialGroup: Any
    kPlugin: Any
    kPluginGeometry: Any
    kPointArray: Any
    kSphere: Any
    kString: Any
    kStringArray: Any
    kSubdSurface: Any
    kUnsupported: Any
    kVectorArray: Any
    kVerts: Any
    matrix: Any
    objectGroupCount: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addComponentTag(self, key: Any) -> MFnMeshData:
        """Adds a componentTag with the given key to the object."""
    def addObjectGroup(self, id: int) -> MFnMeshData:
        """Adds an object group with the given id to the object."""
    def addObjectGroupComponent(self, id: int, arg: Any) -> MFnMeshData:
        """Adds the members of the given component to the object group"""
    def changeObjectGroupId(self, sourceId: int, destId: int) -> MFnMeshData:
        """Changes the id of the object group with the given id to the new id."""
    def componentTagContents(self, key: Any) -> MObject:
        """Returns a component which contains the members of the componentTag"""
    def componentTagExpressionSubsetState(self, expr: Any, ctg: Any) -> Any:
        """Returns the state of the contents of the resolved componentTag expression."""
    def componentTagType(self, key: Any) -> Any:
        """Returns the type of the component that the componentTag with the"""
    def componentTags(self) -> MObject:
        """Returns the componentTag keys contained in the object."""
    def copyObjectGroups(self, arg: Any) -> MFnMeshData:
        """Copies the object groups from the given geometry data object."""
    def create(self) -> MObject:
        """Creates a new mesh data object, attaches it to this function set"""
    def hasComponentTag(self, key: Any) -> bool:
        """Returns True if a componentTag with the given key exists."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def hasObjectGroup(self, id: int) -> MFnMeshData:
        """Returns True if an object group with the given id is"""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def objectGroup(self, index: int) -> int:
        """Returns the id of the index'th object group contained by the object."""
    def objectGroupComponent(self, id: int) -> MObject:
        """Returns a component which contains the members of the object group"""
    def objectGroupSubsetState(self, id: int) -> Any:
        """Returns the state of the group contents of the object group with the"""
    def objectGroupType(self, id: int) -> Any:
        """Returns the type of the component that the object group with the"""
    def removeComponentTag(self, key: Any) -> MFnMeshData:
        """Removes a componentTag with the given key from the object."""
    def removeObjectGroup(self, id: int) -> MFnMeshData:
        """Removes an object group with the given id from the object."""
    def removeObjectGroupComponent(self, id: int, arg: Any) -> MFnMeshData:
        """Removes the members of the given component from the object group"""
    def renameComponentTag(self, key: Any, newKey: Any) -> MFnMeshData:
        """Renames a componentag with the given key the object."""
    def resolveComponentTagExpression(self, key: Any, ctg: Any) -> MObject:
        """Returns a component which is the result of the resolved componentTag expression"""
    def setComponentTagContents(self, key: Any, arg: Any) -> MFnMeshData:
        """Sets the members of the componentTag with the given key"""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def setObjectGroupComponent(self, id: int, arg: Any) -> MFnMeshData:
        """Sets the members of the object group with the given id"""
    def type(self) -> int:
        """Returns the type of the function set."""

class MFnMessageAttribute:
    affectsAppearance: Any
    affectsWorldSpace: Any
    array: Any
    cached: Any
    channelBox: Any
    connectable: Any
    disconnectBehavior: Any
    dynamic: Any
    extension: Any
    hidden: Any
    indeterminant: Any
    indexMatters: Any
    internal: Any
    isProxyAttribute: Any
    kDelete: Any
    kNothing: Any
    kReset: Any
    keyable: Any
    name: Any
    parent: Any
    readable: Any
    renderSource: Any
    shortName: Any
    storable: Any
    usedAsColor: Any
    usedAsFilename: Any
    usesArrayDataBuilder: Any
    worldSpace: Any
    writable: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def accepts(self, type: int | MTypeId) -> bool:
        """Returns True if this attribute can accept a connection of the given type."""
    def acceptsAttribute(self, attr: MFnAttribute) -> bool:
        """Returns True if this attribute can accept a connection with the given attribute."""
    def addToCategory(self, category: Any) -> None:
        """Adds the attribute to a category"""
    def create(self, fullName: Any, briefName: Any) -> MObject:
        """Creates a new message attribute, attaches it to the function set and returns it as an MObject."""
    def getAddAttrCmd(self, useLongName: bool | None = None) -> Any:
        """Returns a string containing a MEL 'addAttr' command capable of recreating the attribute."""
    def hasCategory(self, category: Any) -> bool:
        """Checks to see if the attribute has a given category"""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def setNiceNameOverride(self, localizedName: Any) -> None:
        """Sets a nice UI name for this attribute rather than using the default derived from it's long name."""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def type(self) -> int:
        """Returns the type of the function set."""

class MFnNumericAttribute:
    affectsAppearance: Any
    affectsWorldSpace: Any
    array: Any
    cached: Any
    channelBox: Any
    connectable: Any
    default: Any
    disconnectBehavior: Any
    dynamic: Any
    extension: Any
    hidden: Any
    indeterminant: Any
    indexMatters: Any
    internal: Any
    isProxyAttribute: Any
    kDelete: Any
    kNothing: Any
    kReset: Any
    keyable: Any
    name: Any
    parent: Any
    readable: Any
    renderSource: Any
    shortName: Any
    storable: Any
    usedAsColor: Any
    usedAsFilename: Any
    usesArrayDataBuilder: Any
    worldSpace: Any
    writable: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def accepts(self, type: int | MTypeId) -> bool:
        """Returns True if this attribute can accept a connection of the given type."""
    def acceptsAttribute(self, attr: MFnAttribute) -> bool:
        """Returns True if this attribute can accept a connection with the given attribute."""
    def addToCategory(self, category: Any) -> None:
        """Adds the attribute to a category"""
    def child(self, index: int) -> MObject:
        """Returns the specified child attribute of the parent attribute currently attached to the function set."""
    def create(self, fullName: Any, briefName: Any, unitType: int | MObject, child4: MObject, defaultValue: float | MObject | None = None, child3: MObject | None = None) -> MObject:
        """Creates a new simple or compound numeric attribute, attaches it to the function set and returns it in an MObject."""
    def createAddr(self, fullName: Any, briefName: Any, defaultValue: None = None) -> MObject:
        """Creates a new address attribute, attaches it to the function set and returns it in an MObject."""
    def createColor(self, fullName: Any, briefName: Any) -> MObject:
        """Creates a new color attribute, attaches it to the function set and returns it in an MObject."""
    def createPoint(self, fullName: Any, briefName: Any) -> MObject:
        """Creates a new 3D point attribute, attaches it to the function set and returns it in an MObject."""
    def getAddAttrCmd(self, useLongName: bool | None = None) -> Any:
        """Returns a string containing a MEL 'addAttr' command capable of recreating the attribute."""
    def getMax(self) -> float | tuple[Any]:
        """Returns the attribute's hard maximum value(s)."""
    def getMin(self) -> float | tuple[Any]:
        """Returns the attribute's hard minimum value(s)."""
    def getSoftMax(self) -> float:
        """Returns the attribute's soft maximum value."""
    def getSoftMin(self) -> float:
        """Returns the attribute's soft minimum value."""
    def hasCategory(self, category: Any) -> bool:
        """Checks to see if the attribute has a given category"""
    def hasMax(self) -> bool:
        """Returns True if a hard maximum value has been specified for the attribute."""
    def hasMin(self) -> bool:
        """Returns True if a hard minimum value has been specified for the attribute."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def hasSoftMax(self) -> bool:
        """Returns True if a soft maximum value has been specified for the attribute."""
    def hasSoftMin(self) -> bool:
        """Returns True if a soft minimum value has been specified for the attribute."""
    def numericType(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the numeric type of the attribute currently attached to the function set."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def setMax(self, max1: float, max2: float, max3: float, max4: float) -> None:
        """Sets the attribute's hard maximum value(s)."""
    def setMin(self, min1: float, min2: float, min3: float, min4: float) -> None:
        """Sets the attribute's hard minimum value(s)."""
    def setNiceNameOverride(self, localizedName: Any) -> None:
        """Sets a nice UI name for this attribute rather than using the default derived from it's long name."""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def setSoftMax(self, max1: float) -> None:
        """Sets the attribute's soft maximum value."""
    def setSoftMin(self, min1: float) -> None:
        """Sets the attribute's soft minimum value."""
    def type(self) -> int:
        """Returns the type of the function set."""

class MFnNumericData:
    k2Double: Any
    k2Float: Any
    k2Int: Any
    k2Long: Any
    k2Short: Any
    k3Double: Any
    k3Float: Any
    k3Int: Any
    k3Long: Any
    k3Short: Any
    k4Double: Any
    kAddr: Any
    kAny: Any
    kBoolean: Any
    kByte: Any
    kChar: Any
    kComponentList: Any
    kDouble: Any
    kDoubleArray: Any
    kDynArrayAttrs: Any
    kDynSweptGeometry: Any
    kFalloffFunction: Any
    kFloat: Any
    kFloatArray: Any
    kInt: Any
    kInt64: Any
    kIntArray: Any
    kInvalid: Any
    kLast: Any
    kLattice: Any
    kLong: Any
    kMatrix: Any
    kMatrixArray: Any
    kMesh: Any
    kNId: Any
    kNObject: Any
    kNumeric: Any
    kNurbsCurve: Any
    kNurbsSurface: Any
    kPlugin: Any
    kPluginGeometry: Any
    kPointArray: Any
    kShort: Any
    kSphere: Any
    kString: Any
    kStringArray: Any
    kSubdSurface: Any
    kVectorArray: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def create(self, dataType: Any) -> MObject:
        """Creates a new numeric data object."""
    def getData(self) -> Any:
        """Returns a list containing the attached data object's data."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def numericType(self) -> Any:
        """Returns the type of data in the attached data object."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def setData(self, val1: Any, val2: Any, val3: Any, val4: float) -> None:
        """Sets the value of the data in the attached data object."""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def type(self) -> int:
        """Returns the type of the function set."""

class MFnNurbsCurve:
    boundingBox: Any
    degree: Any
    form: Any
    hasHistoryOnCreate: Any
    inModel: Any
    inUnderWorld: Any
    isDefaultNode: Any
    isFromReferencedFile: Any
    isInstanceable: Any
    isIntermediateObject: Any
    isLocked: Any
    isPlanar: Any
    isShared: Any
    kClosed: Any
    kExtensionAttr: Any
    kFindParamTolerance: Any
    kInvalid: Any
    kInvalidAttr: Any
    kLast: Any
    kLocalDynamicAttr: Any
    kNextPos: Any
    kNormalAttr: Any
    kOpen: Any
    kPeriodic: Any
    kPointTolerance: Any
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
    knotDomain: Any
    namespace: Any
    numCVs: Any
    numKnots: Any
    numSpans: Any
    objectColor: Any
    objectColorRGB: Any
    objectColorType: Any
    planeNormal: Any
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
    def addChild(self, node: int, index: bool, keepExistingParents: bool = False) -> MFnNurbsCurve:
        """Makes a node a child of this one."""
    def addExternalContentForFileAttr(self, attr: MObject) -> MExternalContentInfoTable:
        """Adds content info to the specified table from a file path attribute."""
    def affectsAnimation(self) -> bool:
        """Returns true if the changes to the node may affect animation."""
    @staticmethod
    def allocateFlag(pluginName: Any) -> int:
        """Allocates a flag on all nodes for use by the named plugin and returns the flag's index."""
    def area(self, tolerance: float) -> float:
        """Returns the area bounded by the curve. The curve must be closed and"""
    def attribute(self, index: Any) -> MObject:
        """Returns an attribute of the node, given either its index or name."""
    def attributeClass(self, attr: MObject) -> Any:
        """Returns the class of the specified attribute."""
    def attributeCount(self) -> int:
        """Returns the number of attributes on the node."""
    def canBeWritten(self) -> bool:
        """Returns true if the node will be written to file."""
    def child(self, index: int) -> MObject:
        """Returns the specified child of this node."""
    def childCount(self) -> int:
        """Returns the number of nodes which are children of this one."""
    @staticmethod
    def classification(nodeTypeName: Any) -> Any:
        """Returns the classification string for the named node type."""
    def closestPoint(self, toThisPoint: MPoint, param: float | bool | None = None, tolerance: float | None = None, space: int | float | None = None, space_: int | None = None) -> MPoint:
        """closestPoint(testPoint, guess=None, tolerance=kPointTolerance,"""
    def copy(self, source: MObject, parent: MObject | None = None) -> MObject:
        """Returns a new NURBS curve which is a copy of 'source' and resets"""
    def create(self, cvs: Any, knots: Any, degree: int | MObject, form: Any, is2D: bool, rational: bool, parent: MObject) -> Any:
        """-> self"""
    def createWithEditPoints(self, editPoints: MPointArray, degree: int, agForm: Any, create2D: bool, createRational: bool, uniformParam: bool, parentOrOwner: MObject | None = None) -> MObject:
        """createWithEditPoints(eps, degree, form, is2D, rational, uniform,"""
    def cvPosition(self, index: Any, space: Any) -> MPoint:
        """Returns the position of a single control vertex."""
    def cvPositions(self, space: Any) -> MPointArray:
        """Returns the positions of all of the curve's control vertices."""
    def cvs(self, arg: int) -> MObject:
        """Returns a CV or a range of CVs as a component. MItCurveCV can be"""
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
    def distanceToPoint(self, point: MPoint, space: int) -> float:
        """Returns the distance from the given point to the point on the curve"""
    def duplicate(self, instance: bool = False, instanceLeaf: bool = False) -> MObject:
        """Duplicates the DAG hierarchy rooted at the current node."""
    def findAlias(self, alias: Any, attrObj: MObject) -> bool:
        """Returns the attribute which has the given alias."""
    def findLengthFromParam(self, param: float) -> float:
        """Returns the length along the curve corresponding to a given"""
    def findParamFromLength(self, length: float, tolerance: float) -> float:
        """Returns the parameter value corresponding to a given length along"""
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
    def getDerivativesAtParam(self, param: Any, space: Any, arg: Any) -> Any:
        """Evaluates the curve at the given parameter value, returning a tuple"""
    def getExternalContent(self) -> MExternalContentInfoTable:
        """Gets the external content (files) that this node depends on."""
    def getParamAtPoint(self, point: MPoint, tolerance: int | float, space: int) -> float:
        """Returns the parameter value corresponding to the given point on the"""
    def getPath(self) -> MDagPath:
        """Returns the DAG path to which this function set is attached, or the first path to the node if the function set is attached to an MObject."""
    def getPointAtParam(self, param: float, space: int) -> MPoint:
        """Returns the point on the curve at the given parameter value."""
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
    def isNewAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files."""
    def isParamOnCurve(self, param: float) -> bool:
        """Returns True if the given parameter value lies on the curve (i.e. is"""
    def isParentOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a child of this one."""
    def isPointOnCurve(self, point: MPoint, tolerance: float, space: int) -> bool:
        """Returns True if the given point lies on the curve, False otherwise."""
    def isTrackingEdits(self) -> bool:
        """Returns True if the node is referenced or in an assembly that is tracking edits."""
    def knot(self, index: int) -> float:
        """Returns the parameter value of a single knot."""
    def knots(self) -> MDoubleArray:
        """Returns the parameter values for all of the curve's knots."""
    def length(self, tolerance: float) -> float:
        """Returns the arc length of this curve or 0.0 if it cannot be computed."""
    def makeMultipleEndKnots(self) -> MFnNurbsCurve:
        """Sets the curve's end knots to have full multiplicity. This ensures"""
    def name(self) -> Any:
        """Returns the node's name."""
    def normal(self, param: float, space: int) -> MVector:
        """Returns the normal at the given parameter value on the curve. For"""
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
    def removeChild(self, node: Any) -> MFnNurbsCurve:
        """Removes the child, specified by MObject, reparenting it under the world."""
    def removeChildAt(self, index: int) -> MFnNurbsCurve:
        """Removes the child, specified by index, reparenting it under the world."""
    def removeKnot(self, param: float, removeAll: bool = False) -> MFnNurbsCurve:
        """Removes one or more knots at the given parameter value."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Returns one of the node's attribute, based on the order in which they are written to file."""
    def reverse(self, constructionHistory: bool | None = None) -> MFnNurbsCurve:
        """Reverses the direction of the curve."""
    def setAffectsAnimation(self) -> None:
        """Specifies that modifications to a node could potentially affect the animation."""
    def setAlias(self, alias: Any, name: Any, plug: MPlug, add: bool | None = None) -> bool:
        """Adds or removes an attribute alias."""
    def setCVPosition(self, index: Any, point: Any, space: Any) -> MFnNurbsCurve:
        """Sets the position of a single control vertex of the curve."""
    def setCVPositions(self, points: Any, space: Any) -> MFnNurbsCurve:
        """Sets the positions of all of the curve's control vertices."""
    def setDoNotWrite(self, flag: bool) -> None:
        """Used to prevent the node from being written to file."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> None:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> None:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> None:
        """Sets the state of the specified node flag."""
    def setKnot(self, index: int, param: float) -> MFnNurbsCurve:
        """Sets the parameter value of a single knot."""
    def setKnots(self, params: MDoubleArray, startIndex: int, endIndex: int) -> MFnNurbsCurve:
        """Sets the parameter values of a contiguous group of knots."""
    def setName(self, name: Any, createNamespace: bool | None = None) -> Any:
        """Sets the node's name."""
    def setObject(self, arg: MDagPath | MObject) -> MFnNurbsCurve:
        """Attaches the function set to the specified node or DAG path."""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def tangent(self, param: float, space: int) -> MVector:
        """Returns the normalized tangent vector at the given parameter value"""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
    def type(self) -> int:
        """Returns the type of the function set."""
    def uniqueName(self) -> Any:
        """For a DAG node, the unique name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself. For a non-DAG node, the uniqueName is just its name."""
    def updateCurve(self) -> None:
        """Tells the shape node which represents the curve in the scene, if"""
    def userNode(self) -> MPxNode:
        """Returns the MPxNode object for a plugin node."""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnNurbsCurveData:
    isIdentity: Any
    isNotIdentity: Any
    kAny: Any
    kAuto: Any
    kCompleteGroup: Any
    kComponentList: Any
    kDoubleArray: Any
    kDynArrayAttrs: Any
    kDynSweptGeometry: Any
    kEdges: Any
    kEmptyGroup: Any
    kFaces: Any
    kFalloffFunction: Any
    kFloatArray: Any
    kIntArray: Any
    kInvalid: Any
    kInvalidGroup: Any
    kLast: Any
    kLattice: Any
    kMatrix: Any
    kMatrixArray: Any
    kMesh: Any
    kNId: Any
    kNObject: Any
    kNull: Any
    kNumeric: Any
    kNurbsCurve: Any
    kNurbsSurface: Any
    kPartialGroup: Any
    kPlugin: Any
    kPluginGeometry: Any
    kPointArray: Any
    kSphere: Any
    kString: Any
    kStringArray: Any
    kSubdSurface: Any
    kUnsupported: Any
    kVectorArray: Any
    kVerts: Any
    matrix: Any
    objectGroupCount: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addComponentTag(self, key: Any) -> MFnNurbsCurveData:
        """Adds a componentTag with the given key to the object."""
    def addObjectGroup(self, id: int) -> MFnNurbsCurveData:
        """Adds an object group with the given id to the object."""
    def addObjectGroupComponent(self, id: int, arg: Any) -> MFnNurbsCurveData:
        """Adds the members of the given component to the object group"""
    def changeObjectGroupId(self, sourceId: int, destId: int) -> MFnNurbsCurveData:
        """Changes the id of the object group with the given id to the new id."""
    def componentTagContents(self, key: Any) -> MObject:
        """Returns a component which contains the members of the componentTag"""
    def componentTagExpressionSubsetState(self, expr: Any, ctg: Any) -> Any:
        """Returns the state of the contents of the resolved componentTag expression."""
    def componentTagType(self, key: Any) -> Any:
        """Returns the type of the component that the componentTag with the"""
    def componentTags(self) -> MObject:
        """Returns the componentTag keys contained in the object."""
    def copyObjectGroups(self, arg: Any) -> MFnNurbsCurveData:
        """Copies the object groups from the given geometry data object."""
    def create(self) -> MObject:
        """Creates a new nurbs curve data object, attaches it to this function set"""
    def hasComponentTag(self, key: Any) -> bool:
        """Returns True if a componentTag with the given key exists."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def hasObjectGroup(self, id: int) -> MFnNurbsCurveData:
        """Returns True if an object group with the given id is"""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def objectGroup(self, index: int) -> int:
        """Returns the id of the index'th object group contained by the object."""
    def objectGroupComponent(self, id: int) -> MObject:
        """Returns a component which contains the members of the object group"""
    def objectGroupSubsetState(self, id: int) -> Any:
        """Returns the state of the group contents of the object group with the"""
    def objectGroupType(self, id: int) -> Any:
        """Returns the type of the component that the object group with the"""
    def removeComponentTag(self, key: Any) -> MFnNurbsCurveData:
        """Removes a componentTag with the given key from the object."""
    def removeObjectGroup(self, id: int) -> MFnNurbsCurveData:
        """Removes an object group with the given id from the object."""
    def removeObjectGroupComponent(self, id: int, arg: Any) -> MFnNurbsCurveData:
        """Removes the members of the given component from the object group"""
    def renameComponentTag(self, key: Any, newKey: Any) -> MFnNurbsCurveData:
        """Renames a componentag with the given key the object."""
    def resolveComponentTagExpression(self, key: Any, ctg: Any) -> MObject:
        """Returns a component which is the result of the resolved componentTag expression"""
    def setComponentTagContents(self, key: Any, arg: Any) -> MFnNurbsCurveData:
        """Sets the members of the componentTag with the given key"""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def setObjectGroupComponent(self, id: int, arg: Any) -> MFnNurbsCurveData:
        """Sets the members of the object group with the given id"""
    def type(self) -> int:
        """Returns the type of the function set."""

class MFnNurbsSurface:
    boundingBox: Any
    dataObject: Any
    degreeInU: Any
    degreeInV: Any
    formInU: Any
    formInV: Any
    hasHistoryOnCreate: Any
    inModel: Any
    inUnderWorld: Any
    isBezier: Any
    isDefaultNode: Any
    isFoldedOnBispan: Any
    isFromReferencedFile: Any
    isInstanceable: Any
    isIntermediateObject: Any
    isLocked: Any
    isShared: Any
    isTrimmedSurface: Any
    isUniform: Any
    kClosed: Any
    kClosedSegment: Any
    kExtensionAttr: Any
    kInner: Any
    kInvalid: Any
    kInvalidAttr: Any
    kInvalidBoundary: Any
    kLast: Any
    kLocalDynamicAttr: Any
    kNextPos: Any
    kNormalAttr: Any
    kOpen: Any
    kOuter: Any
    kPeriodic: Any
    kPointTolerance: Any
    kSegment: Any
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
    knotDomainInU: Any
    knotDomainInV: Any
    namespace: Any
    numCVsInU: Any
    numCVsInV: Any
    numKnotsInU: Any
    numKnotsInV: Any
    numNonZeroSpansInU: Any
    numNonZeroSpansInV: Any
    numPatches: Any
    numPatchesInU: Any
    numPatchesInV: Any
    numRegions: Any
    numSpansInU: Any
    numSpansInV: Any
    numUVs: Any
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
    def addChild(self, node: int, index: bool, keepExistingParents: bool = False) -> MFnNurbsSurface:
        """Makes a node a child of this one."""
    def addExternalContentForFileAttr(self, attr: MObject) -> MExternalContentInfoTable:
        """Adds content info to the specified table from a file path attribute."""
    def affectsAnimation(self) -> bool:
        """Returns true if the changes to the node may affect animation."""
    @staticmethod
    def allocateFlag(pluginName: Any) -> int:
        """Allocates a flag on all nodes for use by the named plugin and returns the flag's index."""
    def area(self, space: float | int, tolerance: float) -> float:
        """Returns the surface's area, or 0.0 if the area cannot be determined."""
    def assignUV(self, patchId: int, cornerIndex: int, uvId: int) -> MFnNurbsSurface:
        """Maps a texture coordinate (uv) to a the specified corner of a patch."""
    def assignUVs(self, uvCounts: MIntArray, uvIds: MIntArray) -> MFnNurbsSurface:
        """Maps all texture coordinates for the surface. setUV() and setUVs()"""
    def attribute(self, index: Any) -> MObject:
        """Returns an attribute of the node, given either its index or name."""
    def attributeClass(self, attr: MObject) -> Any:
        """Returns the class of the specified attribute."""
    def attributeCount(self) -> int:
        """Returns the number of attributes on the node."""
    def boundaryType(self, region: int, boundary: int) -> int:
        """Returns the type of the specified boundary. The surface must be a"""
    def canBeWritten(self) -> bool:
        """Returns true if the node will be written to file."""
    def child(self, index: int) -> MObject:
        """Returns the specified child of this node."""
    def childCount(self) -> int:
        """Returns the number of nodes which are children of this one."""
    @staticmethod
    def classification(nodeTypeName: Any) -> Any:
        """Returns the classification string for the named node type."""
    def clearUVs(self) -> MFnNurbsSurface:
        """Clears out all texture coordinates for the nurbsSurface, and leaves"""
    def closestPoint(self, toThisPoint: MPoint, paramU: float | bool | None = None, paramV: float | None = None, ignoreTrimBoundaries: bool | float | None = None, tolerance: float | bool | None = None, space: int | float | None = None, space_: int | None = None) -> MPoint:
        """closestPoint(testPoint, uStart=None, vStart=None,"""
    def copy(self, source: MObject, parent: MObject) -> MObject:
        """Returns a new NURBS surface, which is a copy of the source surface,"""
    def create(self, controlVertices: Any, degreeInU: int, degreeInV: int, formU: Any, formV: Any, createRational: bool, uKnotSequences: Any = None, vKnotSequences: MDoubleArray | MObject | None = None, parentOrOwner: MObject | None = None) -> MObject:
        """create(cvs, uKnots, vKnots, uDegree, vDegree, uForm, vForm,"""
    def cv(self, uIndex: int, vIndex: int) -> MObject:
        """Returns a component for the specified control vertex."""
    def cvPosition(self, uIndex: Any, vIndex: Any, space: Any) -> MPoint:
        """Returns the position of the specified control vertex."""
    def cvPositions(self, space: Any) -> MPointArray:
        """Returns the positions of all the surface's control vertices."""
    def cvsInU(self, startUIndex: int, endUIndex: int, vIndex: int) -> MObject:
        """Returns a component for a set of control vertices in the U direction."""
    def cvsInV(self, startVIndex: int, endVIndex: int, uIndex: int) -> MObject:
        """Returns a component for a set of control vertices in the V direction."""
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
    def distanceToPoint(self, point: MPoint, space: int) -> float:
        """Returns the distance from the given point to the closest point on"""
    def duplicate(self, instance: bool = False, instanceLeaf: bool = False) -> MObject:
        """Duplicates the DAG hierarchy rooted at the current node."""
    def edge(self, region: int, boundary: int, edge: int, paramEdge: bool = False) -> MObjectArray:
        """Return the specified edge of a trim boundary."""
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
    def getAssignedUVs(self, arg: Any, MIntArray: Any) -> Any:
        """Returns the indices of all UVs which have been mapped to the surface."""
    def getConnectedSetsAndMembers(self, instance: int, arg: bool, MObjectArray: Any) -> Any:
        """Returns a tuple containing an array of sets and an array of the"""
    def getConnectedShaders(self, arg: int, MIntArray: Any) -> Any:
        """Returns a tuple containing an array of all the shaders (sets)"""
    def getConnections(self) -> MPlugArray:
        """Returns all the plugs which are connected to attributes of this node."""
    def getDerivativesAtParam(self, uParam: Any, vParam: Any, space: Any, secondOrder: bool = False) -> Any:
        """-> (MPoint, MVector, MVector)"""
    def getExternalContent(self) -> MExternalContentInfoTable:
        """Gets the external content (files) that this node depends on."""
    def getParamAtPoint(self, atThisPoint: MPoint, ignoreTrimBoundaries: bool | int | None = None, space: int | None = None, tolerance: float | None = None) -> tuple[Any]:
        """getParamAtPoint(point, ignoreTrimBoundaries, tolerance=kPointTolerance,"""
    def getPatchUV(self, patchId: int, arg: int, float: Any) -> Any:
        """Returns a tuple containing the texture texture coordinate for a"""
    def getPatchUVid(self, patchId: int, cornerIndex: int) -> int:
        """Returns the id of the texture coordinate for a single corner of a patch."""
    def getPatchUVs(self, arg: int, MFloatArray: Any) -> Any:
        """Returns a tuple containing the values of the texture coordinates on"""
    def getPath(self) -> MDagPath:
        """Returns the DAG path to which this function set is attached, or the first path to the node if the function set is attached to an MObject."""
    def getPointAtParam(self, uParam: float, vParam: float, space: int) -> MPoint: ...
    def getUV(self, arg: int, float: Any) -> Any:
        """Returns a tuple containing the U and V values for the a texture coordinate"""
    def getUVs(self, arg: Any, MFloatArray: Any) -> Any:
        """Returns all of the surface's texture coordinates as a tuple containing"""
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
    def intersect(self, rayStartingPoint: MPoint, alongThisDirection: MVector, u: float | MDoubleArray, v: float | MDoubleArray, intersectionData: MPoint | MPointArray, tolerance: float | None = None, space: int | None = None, calculateDistance: bool | None = None, distance: float | MDoubleArray | None = None, calculateExactHit: bool | None = None, wasExactHit: bool | None = None) -> bool:
        """intersect(rayStart, rayDir, tolerance=kPointTolerance, space=kObject,"""
    def isChildOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a parent of this one."""
    def isFlagSet(self, flag: int) -> bool:
        """Returns the state of the specified node flag."""
    def isFlipNorm(self, region: int) -> bool:
        """Checks whether the normal for the specified region is flipped"""
    def isInstanced(self, indirect: bool = True) -> bool:
        """Returns True if this node is instanced."""
    def isInstancedAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute is an instanced attribute of this node."""
    def isKnotU(self, param: float) -> bool:
        """Checks if the specified parameter value is a knot value in the U"""
    def isKnotV(self, param: float) -> bool:
        """Checks if the specified parameter value is a knot value in the V"""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files."""
    def isParamOnSurface(self, uParam: float, vParam: float) -> bool:
        """Checks if the specified parameter point is on this surface."""
    def isParentOf(self, node: MObject) -> bool:
        """Returns True if the specified node is a child of this one."""
    def isPointInTrimmedRegion(self, uParam: float, vParam: float) -> bool:
        """Checks if the given point is in a trimmed away region of a trimmed"""
    def isPointOnSurface(self, point: MPoint, tolerance: float, space: int) -> bool:
        """Checks if the given point is on this surface."""
    def isTrackingEdits(self) -> bool:
        """Returns True if the node is referenced or in an assembly that is tracking edits."""
    def knotInU(self, index: int) -> float:
        """Returns the knot value at the specified U index. U knots are indexed"""
    def knotInV(self, index: int) -> float:
        """Returns the knot value at the specified V index. V knots are indexed"""
    def knotsInU(self) -> MDoubleArray:
        """Returns all of the surface's knots in the U direction."""
    def knotsInV(self) -> MDoubleArray:
        """Returns all of the surface's knots in the V direction."""
    def name(self) -> Any:
        """Returns the node's name."""
    def normal(self, uParam: float, vParam: float, space: int) -> MVector:
        """Returns the normal at the given parameter value on the surface."""
    def numBoundaries(self, region: int) -> int:
        """Returns the number of boundaries for the specified region. The"""
    def numEdges(self, region: int, boundary: int) -> int:
        """Returns the number of edges for the specified trim boundary."""
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
    def projectCurve(self, arg: MDagPath, keepHistory: bool = False) -> MFnNurbsSurface:
        """Projects the given curve onto the surface, creating a curve on surface."""
    def removeAttribute(self, attr: MObject, type: Any) -> None:
        """Removes a dynamic attribute from the node."""
    def removeChild(self, node: Any) -> MFnNurbsSurface:
        """Removes the child, specified by MObject, reparenting it under the world."""
    def removeChildAt(self, index: int) -> MFnNurbsSurface:
        """Removes the child, specified by index, reparenting it under the world."""
    def removeKnotInU(self, param: float, removeAll: bool = False) -> MFnNurbsSurface:
        """Removes one or more U knots at the specified parameter value from"""
    def removeKnotInV(self, param: float, removeAll: bool = False) -> MFnNurbsSurface:
        """Removes one or more V knots at the specified parameter value from"""
    def removeOneKnotInU(self, param: float) -> MFnNurbsSurface:
        """Removes one U knot at the specified parameter value. If there are"""
    def removeOneKnotInV(self, param: float) -> MFnNurbsSurface:
        """Removes one V knot at the specified parameter value. If there are"""
    def reorderedAttribute(self, index: int) -> MObject:
        """Returns one of the node's attribute, based on the order in which they are written to file."""
    def setAffectsAnimation(self) -> None:
        """Specifies that modifications to a node could potentially affect the animation."""
    def setAlias(self, alias: Any, name: Any, plug: MPlug, add: bool | None = None) -> bool:
        """Adds or removes an attribute alias."""
    def setCVPosition(self, uIndex: Any, vIndex: Any, point: Any, space: Any) -> MFnNurbsSurface: ...
    def setCVPositions(self, points: Any, space: Any) -> MFnNurbsSurface:
        """Set the positions of all of the surface's CVs."""
    def setDoNotWrite(self, flag: bool) -> None:
        """Used to prevent the node from being written to file."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> None:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> None:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> None:
        """Sets the state of the specified node flag."""
    def setKnotInU(self, index: int, param: float) -> MFnNurbsSurface:
        """Sets the value of an existing U knot. U knots are indexed from 0 to"""
    def setKnotInV(self, index: int, param: float) -> MFnNurbsSurface:
        """Sets the value of an existing V knot. V knots are indexed from 0 to"""
    def setKnotsInU(self, params: MDoubleArray, startIndex: int, endIndex: int) -> MFnNurbsSurface:
        """Sets the values of a range of U knots."""
    def setKnotsInV(self, params: MDoubleArray, startIndex: int, endIndex: int) -> MFnNurbsSurface:
        """Sets the values of a range of V knots."""
    def setName(self, name: Any, createNamespace: bool | None = None) -> Any:
        """Sets the node's name."""
    def setObject(self, arg: MDagPath | MObject) -> MFnNurbsSurface:
        """Attaches the function set to the specified node or DAG path."""
    def setUV(self, uvId: int, u: float, v: float) -> MFnNurbsSurface:
        """Sets a single texture coordinate. If 'uvId' is greater than or equal"""
    def setUVs(self, uList: MFloatArray, vList: MFloatArray) -> MFnNurbsSurface:
        """Sets all of the texture coordinates (uvs) for this surface. The """
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def tangents(self, uParam: Any, vParam: Any, space: Any, MVector: Any) -> Any:
        """Returns the tangents in the U and V directions at a given parameter"""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
    def trim(self, regionsToKeepU: MDoubleArray, regionsToKeepV: MDoubleArray, keepHistory: bool = False) -> MFnNurbsSurface:
        """Trims the surface to its curves on surface. Regions which are kept"""
    def type(self) -> int:
        """Returns the type of the function set."""
    def uniqueName(self) -> Any:
        """For a DAG node, the unique name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself. For a non-DAG node, the uniqueName is just its name."""
    def updateSurface(self) -> MFnNurbsSurface:
        """Signals that this surface has changed and needs to be recalculated."""
    def userNode(self) -> MPxNode:
        """Returns the MPxNode object for a plugin node."""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnNurbsSurfaceData:
    isIdentity: Any
    isNotIdentity: Any
    kAny: Any
    kAuto: Any
    kCompleteGroup: Any
    kComponentList: Any
    kDoubleArray: Any
    kDynArrayAttrs: Any
    kDynSweptGeometry: Any
    kEdges: Any
    kEmptyGroup: Any
    kFaces: Any
    kFalloffFunction: Any
    kFloatArray: Any
    kIntArray: Any
    kInvalid: Any
    kInvalidGroup: Any
    kLast: Any
    kLattice: Any
    kMatrix: Any
    kMatrixArray: Any
    kMesh: Any
    kNId: Any
    kNObject: Any
    kNull: Any
    kNumeric: Any
    kNurbsCurve: Any
    kNurbsSurface: Any
    kPartialGroup: Any
    kPlugin: Any
    kPluginGeometry: Any
    kPointArray: Any
    kSphere: Any
    kString: Any
    kStringArray: Any
    kSubdSurface: Any
    kUnsupported: Any
    kVectorArray: Any
    kVerts: Any
    matrix: Any
    objectGroupCount: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addComponentTag(self, key: Any) -> MFnNurbsSurfaceData:
        """Adds a componentTag with the given key to the object."""
    def addObjectGroup(self, id: int) -> MFnNurbsSurfaceData:
        """Adds an object group with the given id to the object."""
    def addObjectGroupComponent(self, id: int, arg: Any) -> MFnNurbsSurfaceData:
        """Adds the members of the given component to the object group"""
    def changeObjectGroupId(self, sourceId: int, destId: int) -> MFnNurbsSurfaceData:
        """Changes the id of the object group with the given id to the new id."""
    def componentTagContents(self, key: Any) -> MObject:
        """Returns a component which contains the members of the componentTag"""
    def componentTagExpressionSubsetState(self, expr: Any, ctg: Any) -> Any:
        """Returns the state of the contents of the resolved componentTag expression."""
    def componentTagType(self, key: Any) -> Any:
        """Returns the type of the component that the componentTag with the"""
    def componentTags(self) -> MObject:
        """Returns the componentTag keys contained in the object."""
    def copyObjectGroups(self, arg: Any) -> MFnNurbsSurfaceData:
        """Copies the object groups from the given geometry data object."""
    def create(self) -> MObject:
        """Creates a new nurbs surface data object, attaches it to this function set"""
    def hasComponentTag(self, key: Any) -> bool:
        """Returns True if a componentTag with the given key exists."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def hasObjectGroup(self, id: int) -> MFnNurbsSurfaceData:
        """Returns True if an object group with the given id is"""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def objectGroup(self, index: int) -> int:
        """Returns the id of the index'th object group contained by the object."""
    def objectGroupComponent(self, id: int) -> MObject:
        """Returns a component which contains the members of the object group"""
    def objectGroupSubsetState(self, id: int) -> Any:
        """Returns the state of the group contents of the object group with the"""
    def objectGroupType(self, id: int) -> Any:
        """Returns the type of the component that the object group with the"""
    def removeComponentTag(self, key: Any) -> MFnNurbsSurfaceData:
        """Removes a componentTag with the given key from the object."""
    def removeObjectGroup(self, id: int) -> MFnNurbsSurfaceData:
        """Removes an object group with the given id from the object."""
    def removeObjectGroupComponent(self, id: int, arg: Any) -> MFnNurbsSurfaceData:
        """Removes the members of the given component from the object group"""
    def renameComponentTag(self, key: Any, newKey: Any) -> MFnNurbsSurfaceData:
        """Renames a componentag with the given key the object."""
    def resolveComponentTagExpression(self, key: Any, ctg: Any) -> MObject:
        """Returns a component which is the result of the resolved componentTag expression"""
    def setComponentTagContents(self, key: Any, arg: Any) -> MFnNurbsSurfaceData:
        """Sets the members of the componentTag with the given key"""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def setObjectGroupComponent(self, id: int, arg: Any) -> MFnNurbsSurfaceData:
        """Sets the members of the object group with the given id"""
    def type(self) -> int:
        """Returns the type of the function set."""

class MFnPlugin:
    version: Any
    def __init__(self, object: MObject | None = None, vendor: Any = None, version: Any = None, requiredApiVersion: Any = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def apiVersion(self) -> Any:
        """Return the API version required by the plug-in."""
    def deregisterAttributePatternFactory(self, typeName: Any) -> None:
        """Deregister a user defined attribute pattern factory type from Maya."""
    def deregisterCommand(self, commandName: Any) -> None:
        """Deregister a user defined command from Maya."""
    def deregisterContextCommand(self, commandName: Any, toolCmdName: Any) -> None:
        """Deregister a user defined context command from Maya."""
    def deregisterData(self, typeId: MTypeId) -> None:
        """Deregister a user defined data type from Maya."""
    def deregisterDragAndDropBehavior(self, behaviorName: Any) -> None:
        """Deregister a user defined drag and drop behavior from Maya."""
    def deregisterNode(self, typeId: MTypeId) -> None:
        """Deregister a user defined dependency node from Maya."""
    @staticmethod
    def findPlugin(pluginName: Any) -> MObject:
        """Returns an MObject corresponding to the named plugin."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def loadPath(self) -> Any:
        """Return the full path name of the file from which the plug-in was loaded."""
    def name(self) -> Any:
        """Return the plug-in's name."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def registerAttributePatternFactory(self, typeName: Any, fnPtr: Any) -> None:
        """Register a new attribute pattern factory type with Maya."""
    def registerCommand(self, commandName: Any, creatorFunction: Any, createSyntaxFunction: Any = None) -> None:
        """Register a new command with Maya."""
    def registerContextCommand(self, commandName: Any, creatorFunction: Any, toolCmdName: Any, toolCmdCreator: Any, toolCmdSyntax: Any = None) -> None:
        """Register a new context command with Maya.  Once registered, the context"""
    def registerData(self, typeName: Any, typeId: MTypeId, creatorFunction: Any, type: int | None = None) -> None:
        """Register a new data type with Maya."""
    def registerDragAndDropBehavior(self, behaviorName: Any, creatorFunction: Any) -> None:
        """Register a new drag and drop behavior with Maya."""
    def registerNode(self, typeName: Any, typeId: MTypeId, creatorFunction: Any, initFunction: Any, type: int | None = None, classification: Any = None) -> None:
        """Register a new dependency node with Maya."""
    def registerShape(self, typeName: Any, typeId: MTypeId, creatorFunction: Any, initFunction: Any, uiCreatorFunction: Any = None, classification: Any = None) -> None:
        """Register a new user defined shape node with Maya."""
    def setName(self, newName: Any, allowRename: bool | None = None) -> None:
        """Set the plug-in's name."""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def type(self) -> int:
        """Returns the type of the function set."""
    def vendor(self) -> Any:
        """Return the plug-in's vendor string."""

class MFnPluginData:
    kAny: Any
    kComponentList: Any
    kDoubleArray: Any
    kDynArrayAttrs: Any
    kDynSweptGeometry: Any
    kFalloffFunction: Any
    kFloatArray: Any
    kIntArray: Any
    kInvalid: Any
    kLast: Any
    kLattice: Any
    kMatrix: Any
    kMatrixArray: Any
    kMesh: Any
    kNId: Any
    kNObject: Any
    kNumeric: Any
    kNurbsCurve: Any
    kNurbsSurface: Any
    kPlugin: Any
    kPluginGeometry: Any
    kPointArray: Any
    kSphere: Any
    kString: Any
    kStringArray: Any
    kSubdSurface: Any
    kVectorArray: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def create(self, id: MTypeId) -> MObject:
        """Create an instance of the specified user defined data type and attach it to this functionset."""
    def data(self) -> MPxData:
        """Return the user defined data held in this instance"""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def type(self) -> int:
        """Returns the type of the function set."""
    def typeId(self) -> MTypeId:
        """Return the unique MTypeId of the user defined data that is held by this instance"""

class MFnPointArrayData:
    kAny: Any
    kComponentList: Any
    kDoubleArray: Any
    kDynArrayAttrs: Any
    kDynSweptGeometry: Any
    kFalloffFunction: Any
    kFloatArray: Any
    kIntArray: Any
    kInvalid: Any
    kLast: Any
    kLattice: Any
    kMatrix: Any
    kMatrixArray: Any
    kMesh: Any
    kNId: Any
    kNObject: Any
    kNumeric: Any
    kNurbsCurve: Any
    kNurbsSurface: Any
    kPlugin: Any
    kPluginGeometry: Any
    kPointArray: Any
    kSphere: Any
    kString: Any
    kStringArray: Any
    kSubdSurface: Any
    kVectorArray: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def array(self) -> MPointArray:
        """Returns the encapsulated array as an MPointArray."""
    def copyTo(self) -> None:
        """Replaces the elements of an array with those in the encapsulated array."""
    def create(self, in_: MPointArray | None = None) -> MObject:
        """Creates a new MPoint array data object."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def set(self, index: int | MPointArray) -> MPoint | None:
        """Sets values in the encapsulated array."""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def type(self) -> int:
        """Returns the type of the function set."""

class MFnReference:
    isDefaultNode: Any
    isFromReferencedFile: Any
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
    def associatedNamespace(self, arg: bool) -> str:
        """Returns the namespace associated with this reference."""
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
    def containsNode(self, MObject: MObject) -> bool:
        """Returns true if the specified node is from this reference or one of its child references. The containsNodeExactly method can be used to test membership without including the child references."""
    def containsNodeExactly(self, MObject: MObject) -> bool:
        """Returns true if the specified node is from this reference. Membership in child references is not checked. The containsNode method may be used to test membership in a reference and its child references."""
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
    def fileName(self, arg: bool, arg_: bool, arg__: bool) -> str:
        """Returns the name of file associated with this reference."""
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
    def getConnections(self) -> MPlugArray:
        """Returns all the plugs which are connected to attributes of this node."""
    def getExternalContent(self) -> MExternalContentInfoTable:
        """Gets the external content (files) that this node depends on."""
    def hasAttribute(self, name: Any) -> bool:
        """Returns True if the node has an attribute with the given name."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def hasUniqueName(self) -> bool:
        """Returns True if the node's name is unique."""
    @staticmethod
    def ignoreReferenceEdits() -> bool:
        """Indicates whether reference edits will be tracked and logged or not."""
    def isExportEditsFile(self) -> bool:
        """Returns true if the reference is an export edits file. An export edits file is a file of type '.editMA' or '.editMB' which was created using Maya's offline file functionality."""
    def isFlagSet(self, flag: int) -> bool:
        """Returns the state of the specified node flag."""
    def isLoaded(self) -> bool:
        """Returns true if the reference is loaded."""
    def isLocked(self) -> bool:
        """Returns true if the reference is locked or if the referenced file was saved as locked."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files."""
    def isTrackingEdits(self) -> bool:
        """Returns True if the node is referenced or in an assembly that is tracking edits."""
    def isValidReference(self) -> bool:
        """Returns true if the reference is an valid file reference."""
    def name(self) -> Any:
        """Returns the node's name."""
    def nodes(self) -> MObjectArray:
        """Returns an array of the nodes associated with this reference."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def parentAssembly(self) -> MObject:
        """Returns the parent assembly node that contains this reference. See MFnAssembly documentation for more details."""
    def parentFileName(self, arg: bool, arg_: bool, arg__: bool) -> str:
        """Returns the name of parent file associated with this reference."""
    def parentReference(self) -> MObject:
        """Returns the reference node associated with the parent reference."""
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
    @staticmethod
    def setIgnoreReferenceEdits(bool: bool) -> None:
        """Specify whether reference edits should be tracked and logged or not."""
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

class MFnSet:
    isDefaultNode: Any
    isFromReferencedFile: Any
    isLocked: Any
    isShared: Any
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
    def addMember(self, object: MObject | MDagPath | MPlug) -> MFnSet:
        """Add a new object to the set."""
    def addMembers(self, MSelectionList: MSelectionList) -> MFnSet:
        """Add a list of new objects to the set."""
    def affectsAnimation(self) -> bool:
        """Returns true if the changes to the node may affect animation."""
    @staticmethod
    def allocateFlag(pluginName: Any) -> int:
        """Allocates a flag on all nodes for use by the named plugin and returns the flag's index."""
    def annotation(self) -> Any:
        """Returns the annotation string for this set.  This allows a description of the set to be stored with it."""
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
    def clear(self) -> MFnSet:
        """Removes all elements from this set."""
    def create(self, members: Any, restriction: Any) -> MObject:
        """Creates a new set dependency node and puts it in the dependency graph."""
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
    def getConnections(self) -> MPlugArray:
        """Returns all the plugs which are connected to attributes of this node."""
    def getExternalContent(self) -> MExternalContentInfoTable:
        """Gets the external content (files) that this node depends on."""
    def getIntersection(self, otherSet: MObject | MObjectArray) -> MSelectionList:
        """This method calculates the intersection of two sets.  The result will be the intersection of this set and the set passed into the method."""
    def getMemberPaths(self, shading: bool) -> MDagPathArray:
        """Get the members of this set as an array of dagPaths."""
    def getMembers(self, flatten: bool) -> MSelectionList:
        """Get the members of this set as a selection list.  This information is providedas a selection list so that all of the path information is retained forDAG nodes."""
    def getUnion(self, otherSet: MObject | MObjectArray) -> MSelectionList:
        """This method calculates the union of two sets.  The result will be the union of this set and the set passed into the method."""
    def hasAttribute(self, name: Any) -> bool:
        """Returns True if the node has an attribute with the given name."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def hasRestrictions(self) -> bool:
        """Returns true if this function set has restrictions on the type of objects that it may contain."""
    def hasUniqueName(self) -> bool:
        """Returns True if the node's name is unique."""
    def intersectsWith(self, otherSet: MObject) -> MFnSet:
        """Returns true if this set intersects with the given set.  An intersection occurs if there are any common members between the two sets."""
    def isFlagSet(self, flag: int) -> bool:
        """Returns the state of the specified node flag."""
    def isMember(self, object: MObject | MDagPath | MPlug) -> bool:
        """Returns true if the given object is a member of this set."""
    def isNewAttribute(self, attr: MObject) -> bool:
        """Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files."""
    def isTrackingEdits(self) -> bool:
        """Returns True if the node is referenced or in an assembly that is tracking edits."""
    def name(self) -> Any:
        """Returns the node's name."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def plugsAlias(self, plug: MPlug) -> Any:
        """Returns the alias for a plug's attribute."""
    def removeAttribute(self, attr: MObject, type: Any) -> None:
        """Removes a dynamic attribute from the node."""
    def removeMember(self, object: MObject | MDagPath | MPlug) -> MFnSet:
        """Remove an object from the set."""
    def removeMembers(self, MSelectionList: MSelectionList) -> MFnSet:
        """Remove items of the selection list from the set."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Returns one of the node's attribute, based on the order in which they are written to file."""
    def restriction(self) -> Any:
        """Returns the type of membership restriction that this set has."""
    def setAffectsAnimation(self) -> None:
        """Specifies that modifications to a node could potentially affect the animation."""
    def setAlias(self, alias: Any, name: Any, plug: MPlug, add: bool | None = None) -> bool:
        """Adds or removes an attribute alias."""
    def setAnnotation(self, annotation: Any) -> MFnSet:
        """Sets the annotation string for this set.  This allows a description of the set to be stored with it."""
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

class MFnSingleIndexedComponent:
    componentType: Any
    elementCount: Any
    elementMax: Any
    hasWeights: Any
    isComplete: Any
    isEmpty: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addElement(self, arg: int) -> MFnSingleIndexedComponent:
        """Adds the specified element to the component."""
    def addElements(self, arg: Any) -> MFnSingleIndexedComponent:
        """addElements(MIntArray) -> self"""
    def create(self, arg: int) -> MObject:
        """Creates a new, empty component, attaches it to the function set and"""
    def element(self, index: int) -> int:
        """Returns the index'th element of the component."""
    def getCompleteData(self) -> int:
        """Returns the number of elements in the complete component, or 0 if the component is not complete."""
    def getElements(self) -> MIntArray:
        """Returns all of the component's elements."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def isEqual(self, arg: Any) -> bool:
        """Returns True if other refers to the same component as the"""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def setCompleteData(self, numElements: int) -> MFnSingleIndexedComponent:
        """Marks the component as complete (i.e. contains all possible elements)."""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def type(self) -> int:
        """Returns the type of the function set."""
    def weight(self, index: int) -> MWeight:
        """Returns the weight associated with the specified element,"""

class MFnStringArrayData:
    kAny: Any
    kComponentList: Any
    kDoubleArray: Any
    kDynArrayAttrs: Any
    kDynSweptGeometry: Any
    kFalloffFunction: Any
    kFloatArray: Any
    kIntArray: Any
    kInvalid: Any
    kLast: Any
    kLattice: Any
    kMatrix: Any
    kMatrixArray: Any
    kMesh: Any
    kNId: Any
    kNObject: Any
    kNumeric: Any
    kNurbsCurve: Any
    kNurbsSurface: Any
    kPlugin: Any
    kPluginGeometry: Any
    kPointArray: Any
    kSphere: Any
    kString: Any
    kStringArray: Any
    kSubdSurface: Any
    kVectorArray: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def array(self) -> Any:
        """Returns the encapsulated array as a list of unicode objects."""
    def create(self, in_: Any = None) -> MObject:
        """Creates a new string array data object."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def set(self, element: Any, index: int) -> None:
        """Sets values in the encapsulated array."""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def type(self) -> int:
        """Returns the type of the function set."""

class MFnStringData:
    kAny: Any
    kComponentList: Any
    kDoubleArray: Any
    kDynArrayAttrs: Any
    kDynSweptGeometry: Any
    kFalloffFunction: Any
    kFloatArray: Any
    kIntArray: Any
    kInvalid: Any
    kLast: Any
    kLattice: Any
    kMatrix: Any
    kMatrixArray: Any
    kMesh: Any
    kNId: Any
    kNObject: Any
    kNumeric: Any
    kNurbsCurve: Any
    kNurbsSurface: Any
    kPlugin: Any
    kPluginGeometry: Any
    kPointArray: Any
    kSphere: Any
    kString: Any
    kStringArray: Any
    kSubdSurface: Any
    kVectorArray: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def create(self, arg: Any = None) -> MObject:
        """Creates a new string data object."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def set(self, newString: Any) -> None:
        """Sets the value of the encapsulated string."""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def string(self) -> Any:
        """Returns the encapsulated string as a unicode object."""
    def type(self) -> int:
        """Returns the type of the function set."""

class MFnTransform:
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
    def addChild(self, node: int, index: bool, keepExistingParents: bool = False) -> MFnTransform:
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
    def create(self, parent: Any = None, parent_: Any = None, parent__: MObject | None = None) -> MObject:
        """Creates a new transform node and attaches it to the function set."""
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
    def removeChild(self, node: Any) -> MFnTransform:
        """Removes the child, specified by MObject, reparenting it under the world."""
    def removeChildAt(self, index: int) -> MFnTransform:
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
    def rotation(self, space: int | None = None) -> MEulerRotation:
        """Returns the transform's rotation as an MEulerRotation or MQuaternion."""
    def rotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotation as the individual components of an MEulerRotation or MQuaternion."""
    def rotationOrder(self) -> int:
        """Returns the order of rotations when the transform's rotation is expressed as an MEulerRotation."""
    def scale(self, space: int | None = None) -> list[float]:
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
    def setExternalContent(self, table: MExternalContentLocationTable) -> None:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> None:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> None:
        """Sets the state of the specified node flag."""
    def setLimit(self, type: int, value: float) -> None:
        """Sets the value of the specified limit."""
    def setName(self, name: Any, createNamespace: bool | None = None) -> Any:
        """Sets the node's name."""
    def setObject(self, arg: MDagPath | MObject) -> MFnTransform:
        """Attaches the function set to the specified node or DAG path."""
    def setRestPosition(self, matrix: MTransformationMatrix) -> None:
        """Sets the transform's rest position matrix."""
    def setRotateOrientation(self, quat: MQuaternion, space: int, balance: bool) -> None:
        """Sets the MQuaternion which orients the local rotation space."""
    def setRotatePivot(self, point: MPoint, space: int, balance: bool) -> None:
        """Sets the transform's rotate pivot."""
    def setRotatePivotTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's rotate pivot translation."""
    def setRotation(self, rot: MEulerRotation, space: int | None = None) -> None:
        """Sets the transform's rotation using an MEulerRotation or MQuaternion."""
    def setRotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""
    def setRotationOrder(self, order: int, reorder: bool) -> None:
        """Sets the transform's rotation order."""
    def setScale(self, vec: MVector, space: int | None = None) -> None:
        """Sets the transform's scale components."""
    def setScalePivot(self, point: MPoint, space: int, balance: bool) -> None:
        """Sets the transform's scale pivot."""
    def setScalePivotTranslation(self, vec: MVector, space: int) -> None:
        """Sets the transform's scale pivot translation."""
    def setShear(self) -> None:
        """Sets the transform's shear."""
    def setTransformation(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's attribute values to represent the given transformation matrix."""
    def setTranslation(self, vec: MVector, space: int | None = None) -> None:
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
    def translation(self, space: int | None = None) -> MVector:
        """Returns the transform's translation as an MVector."""
    def type(self) -> int:
        """Returns the type of the function set."""
    def uniqueName(self) -> Any:
        """For a DAG node, the unique name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself. For a non-DAG node, the uniqueName is just its name."""
    def userNode(self) -> MPxNode:
        """Returns the MPxNode object for a plugin node."""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnTripleIndexedComponent:
    componentType: Any
    elementCount: Any
    hasWeights: Any
    isComplete: Any
    isEmpty: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addElement(self, sIndex: int, tIndex: int, uIndex: int) -> MFnTripleIndexedComponent:
        """addElement([sIndex, tIndex, uIndex]) -> self"""
    def addElements(self, arg: MIntArray) -> MFnTripleIndexedComponent:
        """Adds the specified elements to the component. Each item in the"""
    def create(self, arg: int) -> MObject:
        """Creates a new, empty component, attaches it to the function set and"""
    def getCompleteData(self, arg: Any, numT: Any, numU: Any) -> Any:
        """Returns a tuple containing the number of S, T and U indices in"""
    def getElement(self, arg: int, tIndex: Any, uIndex: Any) -> Any:
        """Returns the index'th element of the component as a tuple containing the"""
    def getElements(self, arg: Any, tIndex: Any, uIndex: Any) -> Any:
        """Returns all of the component's elements as a list of tuples with each"""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def isEqual(self, arg: Any) -> bool:
        """Returns True if other refers to the same component as the"""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def setCompleteData(self, numS: int, numT: int, numU: int) -> MFnTripleIndexedComponent:
        """Marks the component as complete (i.e. contains all possible elements)."""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def type(self) -> int:
        """Returns the type of the function set."""
    def weight(self, index: int) -> MWeight:
        """Returns the weight associated with the specified element,"""

class MFnTypedAttribute:
    affectsAppearance: Any
    affectsWorldSpace: Any
    array: Any
    cached: Any
    channelBox: Any
    connectable: Any
    default: Any
    disconnectBehavior: Any
    dynamic: Any
    extension: Any
    hidden: Any
    indeterminant: Any
    indexMatters: Any
    internal: Any
    isProxyAttribute: Any
    kDelete: Any
    kNothing: Any
    kReset: Any
    keyable: Any
    name: Any
    parent: Any
    readable: Any
    renderSource: Any
    shortName: Any
    storable: Any
    usedAsColor: Any
    usedAsFilename: Any
    usesArrayDataBuilder: Any
    worldSpace: Any
    writable: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def accepts(self, type: int | MTypeId) -> bool:
        """Returns True if this attribute can accept a connection of the given type."""
    def acceptsAttribute(self, attr: MFnAttribute) -> bool:
        """Returns True if this attribute can accept a connection with the given attribute."""
    def addToCategory(self, category: Any) -> None:
        """Adds the attribute to a category"""
    def attrType(self) -> int:
        """Returns the type of data handled by the attribute."""
    def create(self, fullName: Any, briefName: Any, id: MTypeId | int, defaultData: MObject | None = None) -> MObject:
        """Creates a new type attribute, attaches it to the function set and returns it as an MObject."""
    def getAddAttrCmd(self, useLongName: bool | None = None) -> Any:
        """Returns a string containing a MEL 'addAttr' command capable of recreating the attribute."""
    def hasCategory(self, category: Any) -> bool:
        """Checks to see if the attribute has a given category"""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def setNiceNameOverride(self, localizedName: Any) -> None:
        """Sets a nice UI name for this attribute rather than using the default derived from it's long name."""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def type(self) -> int:
        """Returns the type of the function set."""

class MFnUInt64ArrayData:
    kAny: Any
    kComponentList: Any
    kDoubleArray: Any
    kDynArrayAttrs: Any
    kDynSweptGeometry: Any
    kFalloffFunction: Any
    kFloatArray: Any
    kIntArray: Any
    kInvalid: Any
    kLast: Any
    kLattice: Any
    kMatrix: Any
    kMatrixArray: Any
    kMesh: Any
    kNId: Any
    kNObject: Any
    kNumeric: Any
    kNurbsCurve: Any
    kNurbsSurface: Any
    kPlugin: Any
    kPluginGeometry: Any
    kPointArray: Any
    kSphere: Any
    kString: Any
    kStringArray: Any
    kSubdSurface: Any
    kVectorArray: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def array(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the encapsulated array as an MUint64Array."""
    def copyTo(self, *args: Any, **kwargs: Any) -> Any:
        """Replaces the elements of an array with those in the encapsulated array."""
    def create(self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new MUint64 array data object."""
    def hasObj(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the function set is compatible with the specified Maya object."""
    def object(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def set(self, *args: Any, **kwargs: Any) -> Any:
        """Sets values in the encapsulated array."""
    def setObject(self, *args: Any, **kwargs: Any) -> Any:
        """Attaches the function set to the specified Maya object."""
    def type(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the type of the function set."""

class MFnUnitAttribute:
    affectsAppearance: Any
    affectsWorldSpace: Any
    array: Any
    cached: Any
    channelBox: Any
    connectable: Any
    default: Any
    disconnectBehavior: Any
    dynamic: Any
    extension: Any
    hidden: Any
    indeterminant: Any
    indexMatters: Any
    internal: Any
    isProxyAttribute: Any
    kAngle: Any
    kDelete: Any
    kDistance: Any
    kInvalid: Any
    kLast: Any
    kNothing: Any
    kReset: Any
    kTime: Any
    keyable: Any
    name: Any
    parent: Any
    readable: Any
    renderSource: Any
    shortName: Any
    storable: Any
    usedAsColor: Any
    usedAsFilename: Any
    usesArrayDataBuilder: Any
    worldSpace: Any
    writable: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def accepts(self, type: int | MTypeId) -> bool:
        """Returns True if this attribute can accept a connection of the given type."""
    def acceptsAttribute(self, attr: MFnAttribute) -> bool:
        """Returns True if this attribute can accept a connection with the given attribute."""
    def addToCategory(self, category: Any) -> None:
        """Adds the attribute to a category"""
    def create(self, fullName: Any, briefName: Any, unitType: int | MTime | MAngle | MDistance, defaultValue: float | None = None) -> MObject:
        """Creates a new unit attribute, attaches it to the function set and returns it as an MObject."""
    def getAddAttrCmd(self, useLongName: bool | None = None) -> Any:
        """Returns a string containing a MEL 'addAttr' command capable of recreating the attribute."""
    def getMax(self) -> float | MTime | MAngle | MDistance:
        """Returns the attribute's hard maximum value. Returned MAngle and MDistance are always in radians and centimeters, respectively"""
    def getMin(self) -> float | MTime | MAngle | MDistance:
        """Returns the attribute's hard minimum value. Returned MAngle and MDistance are always in radians and centimeters, respectively"""
    def getSoftMax(self) -> float | MTime | MAngle | MDistance:
        """Returns the attribute's soft maximum value. Returned MAngle and MDistance are always in radians and centimeters, respectively"""
    def getSoftMin(self) -> float | MTime | MAngle | MDistance:
        """Returns the attribute's soft minimum value. Returned MAngle and MDistance are always in radians and centimeters, respectively"""
    def hasCategory(self, category: Any) -> bool:
        """Checks to see if the attribute has a given category"""
    def hasMax(self) -> bool:
        """Returns True if the attribute has a hard maximum value."""
    def hasMin(self) -> bool:
        """Returns True if the attribute has a hard minimum value."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def hasSoftMax(self) -> bool:
        """Returns True if the attribute has a soft maximum value."""
    def hasSoftMin(self) -> bool:
        """Returns True if the attribute has a soft minimum value."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def setMax(self, maxValue: float | MTime | MAngle | MDistance) -> None:
        """Sets the attribute's hard maximum value."""
    def setMin(self, minValue: float | MTime | MAngle | MDistance) -> None:
        """Sets the attribute's hard minimum value."""
    def setNiceNameOverride(self, localizedName: Any) -> None:
        """Sets a nice UI name for this attribute rather than using the default derived from it's long name."""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def setSoftMax(self, maxValue: float | MTime | MAngle | MDistance) -> None:
        """Sets the attribute's soft maximum value."""
    def setSoftMin(self, minValue: float | MTime | MAngle | MDistance) -> None:
        """Sets the attribute's soft minimum value."""
    def type(self) -> int:
        """Returns the type of the function set."""
    def unitType(self) -> int:
        """Returns the type of data handled by the attribute."""

class MFnVectorArrayData:
    kAny: Any
    kComponentList: Any
    kDoubleArray: Any
    kDynArrayAttrs: Any
    kDynSweptGeometry: Any
    kFalloffFunction: Any
    kFloatArray: Any
    kIntArray: Any
    kInvalid: Any
    kLast: Any
    kLattice: Any
    kMatrix: Any
    kMatrixArray: Any
    kMesh: Any
    kNId: Any
    kNObject: Any
    kNumeric: Any
    kNurbsCurve: Any
    kNurbsSurface: Any
    kPlugin: Any
    kPluginGeometry: Any
    kPointArray: Any
    kSphere: Any
    kString: Any
    kStringArray: Any
    kSubdSurface: Any
    kVectorArray: Any
    def __init__(self, object: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def array(self) -> MVectorArray:
        """Returns the encapsulated array as an MVectorArray."""
    def copyTo(self) -> None:
        """Replaces the elements of an array with those in the encapsulated array."""
    def create(self, in_: MVectorArray | None = None) -> MObject:
        """Creates a new MVector array data object."""
    def hasObj(self, Type: int | None = None) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def set(self, index: int | MVectorArray) -> MVector | None:
        """Sets values in the encapsulated array."""
    def setObject(self, object: MObject | None = None) -> MObject | None:
        """Attaches the function set to the specified Maya object."""
    def type(self) -> int:
        """Returns the type of the function set."""

class MGlobal:
    kAddToHeadOfList: Any
    kAddToList: Any
    kBaseUIMode: Any
    kBatch: Any
    kInteractive: Any
    kLibraryApp: Any
    kRemoveFromList: Any
    kReplaceList: Any
    kSelectComponentMode: Any
    kSelectLeafMode: Any
    kSelectObjectMode: Any
    kSelectRootMode: Any
    kSelectTemplateMode: Any
    kSurfaceSelectMethod: Any
    kWireframeSelectMethod: Any
    kXORWithList: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def addToModel(MObject: Any, MObject_: Any) -> None:
        """This method is used to add new dag objects to the model.  If no parent node"""
    @staticmethod
    def addToModelAt(MObject: MVector, MVector: Any, arg: Any, arg_: int, rotateOrder: Any = None) -> None:
        """Adds the specified dag object to the DAG and transform the object"""
    @staticmethod
    def animSelectionMask() -> MSelectionMask:
        """Returns the animation selection mask."""
    @staticmethod
    def apiVersion() -> int:
        """Returns a number describing the version of the Maya API at runtime."""
    @staticmethod
    def className() -> Any:
        """Returns the name of this class."""
    @staticmethod
    def clearSelectionList() -> None:
        """Removes all items from the active selection list."""
    @staticmethod
    def closeErrorLog() -> None:
        """This method closes the API error log file.  If error logging is currently"""
    @staticmethod
    def componentSelectionMask() -> MSelectionMask:
        """Returns the component selection mask."""
    @staticmethod
    def currentToolContext() -> MObject:
        """Returns the current tool context as an MObject."""
    @staticmethod
    def defaultErrorLogPathName() -> Any:
        """Determines the default path name of the error log file."""
    @staticmethod
    def deleteNode(node: MObject) -> None:
        """Delete the given dag node or dependency graph node."""
    @staticmethod
    def disableStow() -> bool:
        """This method is used to query if the disabling of Stowing (hiding) """
    @staticmethod
    def displayError(s: Any) -> None:
        """Display an error in the script editor."""
    @staticmethod
    def displayInfo(s: Any) -> None:
        """Display an informational message in the script editor."""
    @staticmethod
    def displayWarning(s: Any) -> None:
        """Display a warning in the script editor."""
    @staticmethod
    def doErrorLogEntry(string: Any) -> bool:
        """Logs an entry in the currently open log file.  It is not necessary for error"""
    @staticmethod
    def errorLogPathName() -> Any:
        """Determines the path name of the current error log file."""
    @staticmethod
    def errorLoggingIsOn() -> bool:
        """This method determines whether or not API errors are being logged."""
    @staticmethod
    def executeCommandOnIdle(string: Any, arg: bool) -> None:
        """Sets a MEL command to execute on the next idle event. Since the command"""
    @staticmethod
    def executeCommandStringResult(string: Any, arg: bool, arg_: bool) -> Any:
        """Executes a MEL command that returns a string or an array of strings """
    @staticmethod
    def getAbsolutePathToResources() -> Any:
        """Return the absolute path of Maya's "Resources" fold on the system,"""
    @staticmethod
    def getActiveSelectionList(orderedSelectionIfAvailable: bool = False) -> MSelectionList:
        """Return an MSelectionList containing the nodes, components and"""
    @staticmethod
    def getAssociatedSets(MSelectionList: MSelectionList) -> list:
        """This utility method finds all the sets that the items in"""
    @staticmethod
    def getFunctionSetList(arg: MObject, string: Any, arg_: Any) -> Any:
        """Returns a tuple of strings that represent the type of each function"""
    @staticmethod
    def getHiliteList() -> MSelectionList:
        """Returns a copy of the hilite list.  The hilite list contains all DAG objects"""
    @staticmethod
    def getLiveList() -> MSelectionList:
        """Returns a copy of the live list. When a user performs a"""
    @staticmethod
    def getPreselectionHiliteList() -> MSelectionList:
        """Gets the objects for which Maya is displaying a preselection"""
    @staticmethod
    def getRichSelection(defaultToActiveSelection: bool = True) -> MRichSelection:
        """Returns the current rich selection (usually the active selection with"""
    @staticmethod
    def getSelectionListByName(name: Any) -> MSelectionList:
        """Returns an MSelectionList with all of the objects that match the"""
    @staticmethod
    def initOptionVar(arg: Any, int: Any, arg_: Any) -> bool:
        """initOptionVar(string name, double, string category) -> bool"""
    @staticmethod
    def isRedoing() -> bool:
        """true if Maya is currently in the middle of a redo."""
    @staticmethod
    def isSelected(MObject: MObject) -> bool:
        """Determines whether the given object is on the active selection list."""
    @staticmethod
    def isUndoing() -> bool:
        """true if Maya is currently in the middle of an undo."""
    @staticmethod
    def isYAxisUp() -> bool:
        """This method returns true if, currently, the Y-axis is UP."""
    @staticmethod
    def isZAxisUp() -> bool:
        """This method returns true if, currently, the Z-axis is UP."""
    @staticmethod
    def mayaFeatureSet() -> int:
        """Returns an enumerated type specifying if Maya API has unlimited set of features."""
    @staticmethod
    def mayaName() -> Any:
        """Returns a string containing name of running application."""
    @staticmethod
    def mayaState() -> int:
        """Returns an enumerated type specifying the way in which Maya was invoked."""
    @staticmethod
    def mayaVersion() -> Any:
        """Returns a string describing this version of Maya."""
    @staticmethod
    def miscSelectionMask() -> MSelectionMask:
        """Returns the miscellaneous selection mask."""
    @staticmethod
    def objectSelectionMask() -> MSelectionMask:
        """Returns the object selection mask."""
    @staticmethod
    def optionVarDoubleValue(string: Any) -> float:
        """This method is used to get the option variable value of type double"""
    @staticmethod
    def optionVarExists(string: Any) -> bool:
        """This method is used to check if the option variable exists"""
    @staticmethod
    def optionVarIntValue(string: Any) -> int:
        """This method is used to get the option variable value of int type"""
    @staticmethod
    def optionVarStringValue(string: Any) -> str:
        """This method is used to get the option variable value of type string"""
    @staticmethod
    def removeFromModel(MObject: Any) -> None:
        """Removes the specified dag node from the scene."""
    @staticmethod
    def removeOptionVar(string: Any) -> None:
        """This method is used to remove the option variable"""
    @staticmethod
    def resetToDefaultErrorLogPathName() -> None:
        """Closes the current log file if it is open, and then resets the log path to"""
    @staticmethod
    def selectByName(string: Any, listAdjustment: Any) -> None:
        """Puts objects that match the give name on the active selection list."""
    @staticmethod
    def selectCommand(MSelectionList: MSelectionList, listAdjustment: Any) -> None:
        """Set the active selection list, by calling the built in Maya select"""
    @staticmethod
    def selectFromScreen(short: Any, short_: Any, listAdjustment: Any, selectMethod: Any) -> None:
        """selectFromScreen(short, short, short, short, listAdjustment=kAddToList, selectMethod=kWireframeSelectMethod) -> None"""
    @staticmethod
    def selectionMethod() -> int:
        """Determines the selection method that should be used in the currently active"""
    @staticmethod
    def selectionMode() -> int:
        """Get current selection mode:"""
    @staticmethod
    def setActiveSelectionList(selectionList: MSelectionList, listAdjustment: int | None = None) -> None:
        """Set the active selection list."""
    @staticmethod
    def setAnimSelectionMask(arg: MSelectionMask) -> MGlobal:
        """Set the animation selection mask to the supplied value."""
    @staticmethod
    def setComponentSelectionMask(arg: MSelectionMask) -> MGlobal:
        """Set the component selection mask to the supplied value."""
    @staticmethod
    def setDisableStow(bool: bool) -> None:
        """This method is used to make the visiblity of all Maya windows unchangable."""
    @staticmethod
    def setDisplayCVs(MSelectionList: Any, bool: Any) -> None:
        """Controls drawing of control points in the specified selection list."""
    @staticmethod
    def setErrorLogPathName(string: Any) -> None:
        """Determines the default path name of the error log file."""
    @staticmethod
    def setHiliteList(MSelectionList: Any) -> None:
        """Sets the current hilite list. The current selection list is unchanged."""
    @staticmethod
    def setMiscSelectionMask(arg: MSelectionMask) -> MGlobal:
        """Set the miscellaneous selection mask to the supplied value."""
    @staticmethod
    def setObjectSelectionMask(arg: MSelectionMask) -> MGlobal:
        """Set the object selection mask to the supplied value."""
    @staticmethod
    def setOptionVarValue(string: Any, int: Any) -> bool:
        """setOptionVarValue(string name, double) -> bool"""
    @staticmethod
    def setPreselectionHiliteList(MSelectionList: MSelectionList) -> None:
        """Sets the objects for which Maya will display a preselection"""
    @staticmethod
    def setRichSelection(MRichSelection: MRichSelection) -> None:
        """Set the current rich selection."""
    @staticmethod
    def setSelectionMode(int: Any) -> None:
        """Set the current selection mode."""
    @staticmethod
    def setTrackSelectionOrderEnabled(enable: bool) -> None:
        """Set whether Maya should maintain an active selection list which"""
    @staticmethod
    def setYAxisUp(rotateView: bool | None = None) -> None:
        """This method sets the flag to identify which axis is Up, and"""
    @staticmethod
    def setZAxisUp(rotateView: bool | None = None) -> None:
        """This method sets the flag to identify which axis is Up, and"""
    @staticmethod
    def sourceFile(string: Any) -> None:
        """Causes the MEL command engine to open the named file and execute"""
    @staticmethod
    def startErrorLogging(logPathName: Any = None) -> None:
        """startErrorLogging(string)"""
    @staticmethod
    def stopErrorLogging() -> None:
        """This method disables output to the API error log but does not close the log file."""
    @staticmethod
    def trackSelectionOrderEnabled() -> bool:
        """Returns whether the selection order is currerntly being tracked."""
    @staticmethod
    def unselect(MObject: MDagPath | MObject) -> None:
        """unselect(MDagPath, MObject) -> None"""
    @staticmethod
    def unselectByName(string: Any) -> None:
        """Removes objects matching the pattern from the active selection list."""
    @staticmethod
    def upAxis() -> MVector:
        """This method returns the model's current up axis."""
    @staticmethod
    def viewFrame(double: MTime | float) -> None:
        """viewFrame(MTime) -> None"""

class MImage:
    kByte: Any
    kFloat: Any
    kHeightFieldBumpFormat: Any
    kNoFormat: Any
    kNormalMapBumpFormat: Any
    kUnknown: Any
    kUnknownFormat: Any
    def __init__(self) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def create(self, width: int, height: int, type: Any, channels: int = 4) -> MImage:
        """Create a new MImage object. Allocates memory for an RGBA array of pixels"""
    def depth(self) -> int:
        """Get the color depth (in bytes) of the currently opened image."""
    def depthMap(self) -> int:
        """Returns a long containing a C++ 'float' pointer which points to the depth data."""
    def filter(self, sourceFormat: Any, targetFormat: Any, scale: float = 1.0, offset: float = 1.0) -> MImage:
        """Modify the content of the image by applying a filter."""
    @staticmethod
    def filterExists(sourceFormat: Any, targetFormat: Any) -> bool:
        """Return whether or not a given source format can be directly converted to a given target format."""
    def floatPixels(self) -> int:
        """Returns a long containing a C++ 'float' pointer which points to the pixel data."""
    def getDepthMapRange(self) -> Any:
        """Compute the minimum and maximum depth values (range) for any stored depth buffer."""
    def getDepthMapSize(self) -> Any:
        """Returns the size of the depth map buffer."""
    def getSize(self) -> Any:
        """Get the width and height of the currently opened image."""
    def haveDepth(self) -> bool:
        """Returns True if this instance of MImage contains a depth map."""
    def isRGBA(self) -> bool:
        """Query flag which indicates whether the pixel information is in RGBA sequence or BGRA sequence."""
    def pixelType(self) -> int:
        """Get the current pixel format of the image:  kUnknown    Format not known or invalid."""
    def pixels(self) -> int:
        """Returns a long containing a C++ 'unsigned char' pointer which points to the pixel data."""
    def readDepthMap(self, pathname: Any) -> MImage:
        """Reads the depth map from the specified file and place the result into the depth map array of this MImage instance."""
    def readFromFile(self, pathname: Any, type: Any) -> MImage:
        """Attempt to identify and open the specified image file."""
    def readFromTextureNode(self, fileTextureObject: MObject, type: Any) -> MImage:
        """Attempt to read the content of the given file texture node."""
    def release(self) -> MImage:
        """Release the current image. If there is no current image, the call is ignored."""
    def resize(self, width: int, height: int, preserveAspectRatio: bool = True) -> MImage:
        """Resize the currently opened image to the specified dimension, or to the closest"""
    def setDepthMap(self, depth: int | MFloatArray, width: int, heigth: int) -> MImage:
        """Specifies the depth map resolution and data."""
    def setFloatPixels(self, pixels: int, width: int, height: int, channels: int = 4) -> MImage:
        """Copy the uncompressed pixels array passed in into the MImage."""
    def setPixels(self, pixels: int, width: int, height: Any) -> MImage:
        """Copy the uncompressed pixels array passed in into the MImage."""
    def setRGBA(self, bool: bool) -> MImage:
        """Sets a flag to indicate that pixel information is in RGBA sequence or BGRA sequence."""
    def verticalFlip(self) -> bool:
        """Flips the image vertically."""
    def writeToFile(self, pathname: Any, outputFormat: Any) -> MImage:
        """Save the content of this image in a file. By default, the file is saved in IFF format."""
    def writeToFileWithDepth(self, pathname: Any, outputFormat: Any, writeDepth: bool = False) -> MImage:
        """Save the content of this image in a file. By default, the file is saved in IFF format."""

class MInt64Array:
    sizeIncrement: Any
    def __init__(self, other: MInt64Array | int | None = None, initialValue: Any = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def append(self, element: Any) -> None:
        """Add a value to the end of the array."""
    def clear(self) -> None:
        """Remove all elements from the array."""
    def copy(self, source: MInt64Array) -> None:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self, element: Any, index: int) -> None:
        """Insert a new value into the array at the given index."""
    def remove(self, index: int) -> None:
        """Remove an element from the array."""
    def setLength(self, length: int) -> None:
        """Grow or shrink the array to contain a specific number of elements."""

class MIntArray:
    sizeIncrement: Any
    def __init__(self, other: MIntArray | int | None = None, initialValue: int | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def append(self, element: int) -> None:
        """Add a value to the end of the array."""
    def clear(self) -> None:
        """Remove all elements from the array."""
    def copy(self, source: MIntArray) -> None:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self, element: int, index: int) -> None:
        """Insert a new value into the array at the given index."""
    def remove(self, index: int) -> None:
        """Remove an element from the array."""
    def setLength(self, length: int) -> None:
        """Grow or shrink the array to contain a specific number of elements."""

class MItCurveCV:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def currentItem(self) -> MObject:
        """Returns the current CV in the iteration as an MObject."""
    def hasHistoryOnCreate(self) -> bool:
        """This method determines if the shape was created with history."""
    def index(self) -> int:
        """Returns the index of the current edge in the iteration."""
    def isDone(self) -> bool:
        """Indicates if all of the edges have been traversed yet."""
    def next(self) -> MItCurveCV:
        """Advances to the next edge in the iteration."""
    def position(self) -> MPoint:
        """Returns the position of the current CV."""
    def reset(self) -> MItCurveCV:
        """reset(curve) -> self"""
    def setPosition(self, point: Any, space: Any) -> MItCurveCV:
        """Sets the position of the current CV, in the given transformation"""
    def translateBy(self, vector: Any, space: Any) -> MItCurveCV:
        """Translate the current CV by the amount specified"""
    def updateCurve(self) -> MItCurveCV:
        """This method is used to signal the curve that it has been changed and needs to redraw itself."""

class MItDag:
    kBreadthFirst: Any
    kDepthFirst: Any
    kInvalidType: Any
    traverseUnderWorld: Any
    def __init__(self, filterType: int | None = None, root: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def currentItem(self) -> MObject:
        """Retrieves DAG node to which the iterator points."""
    def depth(self) -> Any:
        """Returns the height or depth of the current node in the DAG relative to the"""
    def fullPathName(self) -> str:
        """Return a string representing the full path from the root of the dag to this object."""
    def getAllPaths(self) -> MDagPathArray:
        """Determines all DAG Paths to current item in the iteration."""
    def getPath(self) -> MDagPath:
        """Determines a DAG Path to the current item in the iteration."""
    def instanceCount(self, total: bool) -> int:
        """Determines the number of times the current item (DAG node) in the iteration"""
    def isDone(self) -> bool:
        """Indicates end of iteration path."""
    def isInstanced(self, indirect: bool = True) -> bool:
        """Determines whether the current item (DAG node) in the iteration is directly"""
    def iter(self) -> MItDag:
        """Initializes the iterator object for pythonic iteration."""
    def iternext(self) -> MItDag:
        """Used in pythonic iteration to move the iterator"""
    def next(self) -> None:
        """Moves to the next node matching the filter in the graph."""
    def partialPathName(self) -> str:
        """Return a string representing the partial path from the root of the"""
    def prune(self) -> MItDag:
        """Prunes iteration tree at current node."""
    def reset(self, object: MObject | MDagPath | None = None, TraversalType: Any = None, Type: Any = None) -> None:
        """reset(rootObject, traversalType = MItDag.kDepthFirst, filterType = MFn.kInvalid) -> self"""
    def root(self) -> MObject:
        """Returns the root (start node) of the current traversal."""
    def traversalType(self) -> Any:
        """Returns the direction of the traversal."""

class MItDependencyGraph:
    currentDirection: Any
    currentFilter: Any
    currentLevel: Any
    currentRelationship: Any
    currentTraversal: Any
    kBreadthFirst: Any
    kConnectedTo: Any
    kDependsOn: Any
    kDepthFirst: Any
    kDownstream: Any
    kEvaluationGraph: Any
    kNodeLevel: Any
    kPlugLevel: Any
    kUpstream: Any
    nodeDepth: Any
    pruningOnFilter: Any
    traversingOverWorldSpaceDependents: Any
    def __init__(self, rootNode: MObject | MPlug, arg: Any, filter: int | MPlug | None = None, arg_: Any = None, arg__: Any = None, arg___: Any = None, arg____: Any = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def currentNode(self) -> MObject:
        """Retrieves the current node of the iteration.  Results in a null object on"""
    def currentNodeHasUnknownType(self) -> bool:
        """Indicates whether or not the current node has an unrecognised"""
    def currentPlug(self) -> MPlug:
        """Retrieves the current plug of the iteration.  Results in a null"""
    def getNodePath(self) -> MObjectArray:
        """Retrieves the direct path from the current node to the root"""
    def getNodesVisited(self) -> MObjectArray:
        """Retrieves all nodes visited during the iteration."""
    def getPlugPath(self) -> MPlugArray:
        """Retrieves the direct path from the current plug to the root"""
    def getPlugsVisited(self) -> MPlugArray:
        """Retrieves all plugs visited during the iteration."""
    def isDone(self) -> bool:
        """Indicates whether or not all nodes or plugs have been iterated over"""
    def iter(self) -> MItDependencyGraph:
        """Initializes the iterator object for pythonic iteration."""
    def iternext(self) -> MItDependencyGraph:
        """Used in pythonic iteration to move the iterator"""
    def next(self) -> MItDependencyGraph:
        """Iterates to the next node or plug in accordance with the"""
    def previousPlug(self) -> MPlug:
        """Retrieves the previous plug of the iteration.  Results in a"""
    def prune(self) -> MItDependencyGraph:
        """Prunes the search path at the current plug.  Iterator will not"""
    def reset(self) -> MItDependencyGraph:
        """Clears iterator data and resets the iterator to the root node"""
    def resetFilter(self) -> MItDependencyGraph:
        """Resets the node or plug filter to default, MFn.kInvalid"""
    def resetTo(self, rootObject: Any, filter: Any = None, direction: Any = None, traversal: Any = None, level: Any = None, relationship: Any = None) -> MItDependencyGraph:
        """resetTo(rootPlug, filter = MFn.kInvalid, direction = MItDependencyGraph.kDownstream, traversal = MItDependencyGraph.kDepthFirst, level = MItDependencyGraph.kNodeLevel, relationship = MItDependencyGraph.kDependsOn) -> self"""
    def rootNode(self) -> MObject:
        """Retrieves the root node of the iteration."""
    def rootPlug(self) -> MPlug:
        """Retrieves the root plug of the iteration."""

class MItDependencyNodes:
    def __init__(self, filter: int | MIteratorType | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def isDone(self) -> bool:
        """Indicates end of the iteration."""
    def iter(self) -> MItDependencyNodes:
        """Initializes the iterator object for pythonic iteration."""
    def iternext(self) -> MItDependencyNodes:
        """Used in pythonic iteration to move the iterator"""
    def next(self) -> MItDependencyNodes:
        """Moves to the next node matching the filter.  If the filter"""
    def reset(self, filter: int | None = None) -> MItDependencyNodes:
        """reset(filterType = MFn.kInvalid) -> self"""
    def thisNode(self) -> MObject:
        """Retrieves the dependency node to which the iterator points."""

class MItGeometry:
    def __init__(self, dagPath: MDagPath | MObject | MDataHandle | None = None, component: Any = None, readOnly: bool | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def allPositions(self, space: int | None = None) -> Any:
        """Return the position of all the points/CVs/vertices.  This"""
    def component(self) -> MObject:
        """DEPRECATED in 2019, use currentItem instead."""
    def count(self) -> int:
        """Return the number of items in this iteration. This number will"""
    def currentItem(self) -> MObject:
        """This method returns the current component in the iteration."""
    def exactCount(self) -> int:
        """Return the exact number of items in this iteration. This method is"""
    def index(self) -> int:
        """This method returns the index of the current point/CV/vertex"""
    def isDone(self) -> bool:
        """Indicates end of the iteration."""
    def iter(self) -> MItGeometry:
        """Initializes the iterator object for pythonic iteration."""
    def iternext(self) -> MItGeometry:
        """Used in pythonic iteration to move the iterator"""
    def next(self) -> MItGeometry:
        """Advance to the next component in the iteration."""
    def normal(self, space: int | None = None) -> MVector:
        """Return the normal of the current point/CV/vertex component."""
    def position(self, space: int | None = None) -> MPoint:
        """Return the position of the current point/CV/vertex component."""
    def reset(self) -> MItGeometry:
        """Resets the iterator."""
    def setAllPositions(self, points: MPointArray, space: int | None = None) -> Any:
        """Set the position of all the points/CVs/vertices at once. This"""
    def setPosition(self, point: MPoint, space: int | None = None) -> Any:
        """Set the position of the current point/CV/vertex."""
    def weight(self) -> MWeight:
        """Return the weight of the current point/CV/vertex component."""

class MItMeshEdge:
    isSmooth: Any
    def __init__(self, object: MObject, space: int | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def center(self, space: int) -> MPoint:
        """Returns the center point of the edge, in the given transformation space."""
    def connectedToEdge(self, index: int) -> bool:
        """Determines whether the given edge is connected to the current edge."""
    def connectedToFace(self, index: int) -> bool:
        """Determines whether the given face contains the current edge."""
    def count(self) -> int:
        """Return the number of edges in the iteration"""
    def currentItem(self) -> MObject:
        """Returns the current edge in the iteration as a component."""
    def geomChanged(self) -> MItMeshEdge:
        """Resets the geom pointer in the MItMeshEdge. If you're using MFnMesh to"""
    def getConnectedEdges(self, edgeList: MIntArray) -> MIntArray:
        """Returns the indices of edges connected to the current edge."""
    def getConnectedFaces(self, faceList: MIntArray) -> MIntArray:
        """Returns the indices of the faces connected to the current edge."""
    def index(self, index: int | None = None) -> int:
        """Returns the index of the current edge in the iteration."""
    def isDone(self) -> bool:
        """Indicates if all of the edges have been traversed yet."""
    def iter(self) -> MItMeshEdge:
        """Initializes the iterator object for pythonic iteration."""
    def iternext(self) -> MItMeshEdge:
        """Used in pythonic iteration to move the iterator"""
    def length(self, space: Any) -> float:
        """Returns the length of the edge, in the given transformation space."""
    def next(self) -> None:
        """Advances to the next edge in the iteration."""
    def numConnectedEdges(self) -> int:
        """Returns the number of edges connected to the current edge."""
    def numConnectedFaces(self) -> int:
        """Returns the number of faces connected to the current edge."""
    def onBoundary(self) -> bool:
        """Determines if the current edge is a border edge."""
    def point(self, whichVertex: int, space: int) -> MPoint:
        """Returns the position of one of the current edge's vertices, int the"""
    def reset(self, polyObject: MDagPath | None = None) -> MItMeshEdge:
        """reset(mesh) -> self"""
    def setIndex(self, index: int) -> int:
        """Sets the index of the current edge to be accessed. The current edge"""
    def setPoint(self, point: MPoint, whichVertex: int, space: int) -> MItMeshEdge:
        """Sets the position of one of the current edge's vertices, in the given"""
    def updateSurface(self) -> MItMeshEdge:
        """Tells Maya that mesh has been changed and needs to redraw itself."""
    def vertexId(self, whichVertex: Any) -> int:
        """Returns the global index (as opposed to face-relative index) of one of"""

class MItMeshFaceVertex:
    def __init__(self, polyObject: MObject | MDagPath, component: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def currentItem(self) -> MObject:
        """Returns the current faceVertex as a double-indexed component."""
    def faceId(self) -> int:
        """Returns the current face index."""
    def faceVertexId(self) -> int:
        """Returns the relative index of the vertex within the current face. This"""
    def geomChanged(self) -> MItMeshFaceVertex:
        """Resets the geom pointer in the MItMeshFaceVertex. If you're using"""
    def getBinormal(self, space: int | None = None, uvSet: Any = '') -> MVector:
        """Returns the face vertex binormal associated with the UV set."""
    def getColor(self, colorSetName: Any = '') -> MColor:
        """Returns a color of the current face vertex."""
    def getColorIndex(self, colorSetName: Any = '') -> int:
        """Return a color index of the current face vertex."""
    def getNormal(self, space: int | None = None) -> MVector:
        """Returns the face vertex normal."""
    def getTangent(self, space: int | None = None, uvSet: Any = '') -> MVector:
        """Returns the face vertex tangent associated with the given UV set. The"""
    def getUV(self, uvSet: Any, float: Any) -> Any:
        """Returns the texture coordinate for the current face vertex."""
    def getUVIndex(self, uvSet: Any = '') -> int:
        """Returns the index of the texture coordinate for the current face"""
    def hasColor(self) -> bool:
        """Returns whether the current face vertex has a color-per-vertex set."""
    def hasUVs(self, uvSet: Any = '') -> bool:
        """Returns whether the current face vertex has UVs mapped in the given"""
    def isDone(self) -> bool:
        """Indicates if all of the face vertices have been traversed."""
    def iter(self) -> MItMeshFaceVertex:
        """Initializes the iterator object for pythonic iteration."""
    def iternext(self) -> MItMeshFaceVertex:
        """Used in pythonic iteration to move the iterator"""
    def next(self) -> MItMeshFaceVertex:
        """Advances to the next face vertex in the iteration."""
    def normalId(self) -> int:
        """Returns the normal index for the specified vertex. This index refers"""
    def position(self, space: int | None = None) -> MPoint:
        """Returns the position of the current face vertex."""
    def reset(self, polyObject: MObject | MDagPath | None = None) -> MItMeshFaceVertex:
        """reset(mesh) -> self"""
    def setIndex(self, faceId: int, arg: int, oldFaceVertexId: Any) -> Any:
        """Sets the index of the current face vertex to be accessed. The current"""
    def tangentId(self) -> int:
        """Returns the tangent index for the current face vertex. This index"""
    def updateSurface(self) -> MItMeshFaceVertex:
        """Tells Maya that mesh has been changed and needs to redraw itself."""
    def vertexId(self) -> int:
        """Returns the global (as opposed to face-relative) index of the"""

class MItMeshPolygon:
    def __init__(self, object: MObject, space: int | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def center(self, space: int | None = None) -> MPoint:
        """Return the position of the center of the current polygon"""
    def count(self) -> int:
        """Return the number of polygons in the iteration"""
    def currentItem(self) -> MObject:
        """Get the current polygon in the iteration as a component."""
    def geomChanged(self) -> MItMeshPolygon:
        """Reset the geom pointer in the MItMeshPolygon. This is now being handled automatically inside the iterator, and users should no longer need to call this method directly to sync up the iterator to changes made by MFnMesh"""
    def getArea(self, space: int) -> float:
        """This method gets the area of the face"""
    def getColor(self, colorSetName: Any = None) -> MColor:
        """getColor(vertexIndex) -> MColor"""
    def getColorIndex(self, vertexIndex: int, colorSetName: Any = None) -> int:
        """This method returns the colorIndex for a vertex of the current face."""
    def getColorIndices(self, colorSetName: Any = None) -> MIntArray:
        """This method returns the colorIndices for each vertex on the face."""
    def getColors(self, colorSetName: Any = None) -> MColorArray:
        """This method gets the color of the each vertex in the current face."""
    def getConnectedEdges(self) -> MIntArray:
        """This method gets the indices of the edges connected to the vertices of the current face, but DOES not include the edges contained in the current face"""
    def getConnectedFaces(self) -> MIntArray:
        """This method gets the indices of the faces connected to the current face."""
    def getConnectedVertices(self) -> MIntArray:
        """This method gets the object-relative indices of the vertices surrounding the vertices of the current face, but does not include the vertices of the current face"""
    def getEdges(self) -> MIntArray:
        """This method gets the indices of the edges contained in the current face."""
    def getNormal(self, space: int | None = None) -> MVector:
        """getNormal(vertexIndex, [space=]kObject) -> MVector"""
    def getNormals(self, space: int) -> MVectorArray:
        """Returns the normals for all vertices in the current face"""
    def getPointAtUV(self, uvPoint: int, space: Any, uvSet: float | None = None, tolerance: int = 0) -> MPoint:
        """Return the position of the point at the given UV value in the current polygon."""
    def getPoints(self, space: int | None = None) -> MPointArray:
        """Retrieves the positions of the vertices on the current face/polygon that the iterator is pointing to. Vertex positions will be inserted into the given array and will be indexed using face-relative vertex IDs (ie. ordered from 0 to (vertexCount of the face) - 1), which should not be confused with the vertexIDs of each vertex in relation to the entire mesh object. """
    def getTriangle(self, localTriIndex: int, space: int) -> Any:
        """Get the vertices and vertex positions of the given triangle in the current face's triangulation."""
    def getTriangles(self, space: int) -> Any:
        """Get the vertices and vertex positions of all the triangles in the current face's triangulation"""
    def getUV(self, vertexId: int, uvSet: Any = None) -> Any:
        """Return the texture coordinate for the given vertex."""
    def getUVArea(self, uvSet: Any = None) -> float:
        """This method gets the UV area of the face"""
    def getUVAtPoint(self, pt: int, space: Any, uvSet: Any = None) -> Any:
        """Find the point closest to the given point in the current polygon, and return the UV value at that point."""
    def getUVIndex(self, vertex: int, uvSet: Any = None) -> int:
        """Returns the index of the texture coordinate for the given vertex."""
    def getUVIndexAndValue(self, vertex: Any, uvSet: Any = None) -> Any:
        """Return the index and value of the texture coordinate for the given vertex. This index refers to an element of the texture coordinate array for the polygonal object returned by MFnMesh.getUVs."""
    def getUVSetNames(self) -> list[str]:
        """This method is used to find the UV set names mapped to the current face"""
    def getUVs(self, uvSet: Any = None) -> Any:
        """Return the all the texture coordinates for the vertices of this face (in local vertex order)."""
    def getVertices(self) -> MIntArray:
        """This method gets the indices of the vertices of the current face"""
    def hasColor(self, localVertexIndex: int | None = None) -> bool:
        """hasColor(localVertexIndex) -> bool"""
    def hasUVs(self, uvSet: Any = None) -> bool:
        """Tests whether this face has UV's mapped or not (either all the vertices for a face should have UV's, or none of them do, so the UV count for a face is either 0, or equal to the number of vertices)."""
    def hasValidTriangulation(self) -> bool:
        """This method checks if the face has a valid triangulation. If it doesn't, then the face was bad geometry: it may gave degenerate points or cross over itself."""
    def index(self) -> int:
        """Returns the index of the current polygon"""
    def isConnectedToEdge(self, index: int) -> bool:
        """This method determines whether the given face is adjacent to the current face"""
    def isConnectedToFace(self, index: int) -> bool:
        """This method determines whether the given face is adjacent to the current face"""
    def isConnectedToVertex(self, index: int) -> bool:
        """This method determines whether the given vertex shares an edge with a vertex in the current face"""
    def isConvex(self) -> bool:
        """This method checks if the face is convex."""
    def isDone(self) -> bool:
        """Indicates if all of the polygons have been traversed yet."""
    def isHoled(self) -> bool:
        """This method checks if the face has any holes."""
    def isLamina(self) -> bool:
        """This method checks if the face is a lamina (the face is folded over onto itself)."""
    def isPlanar(self) -> bool:
        """This method checks if the face is planar"""
    def isStarlike(self) -> bool:
        """This method checks if the face is starlike. That is, a line from the centre to any vertex lies entirely within the face."""
    def isUVReversed(self, faceId: Any) -> bool:
        """Returns True if the texture coordinates (uv's) for the face are"""
    def iter(self) -> MItMeshPolygon:
        """Initializes the iterator object for pythonic iteration."""
    def iternext(self) -> MItMeshPolygon:
        """Used in pythonic iteration to move the iterator"""
    def next(self) -> None:
        """Advance to the next polygon in the iteration."""
    def normalIndex(self, vertex: int) -> int:
        """Returns the normal index for the specified vertex."""
    def numColors(self, colorSetName: Any = None) -> int:
        """This method checks for the number of colors on vertices in this face"""
    def numConnectedEdges(self) -> int:
        """This method checks for the number of connected edges on the vertices of this face"""
    def numConnectedFaces(self) -> int:
        """This method checks for the number of connected faces"""
    def numTriangles(self) -> int:
        """This Method checks for the number of triangles in this face in the current triangulation"""
    def onBoundary(self) -> bool:
        """This method determines whether the current face is on a boundary"""
    def point(self, index: int, space: int) -> MPoint:
        """Return the position of the vertex at index in the current polygon."""
    def polygonVertexCount(self) -> int:
        """Return the number of vertices for the current polygon"""
    def reset(self, polyObject: MObject | MDagPath | None = None) -> MItMeshPolygon:
        """reset(polyObject) -> self"""
    def setIndex(self, index: int) -> int:
        """This method sets the index of the current face to be accessed."""
    def setPoint(self, point: MPoint, index: int, space: int) -> MItMeshPolygon:
        """Set the vertex at the given index in the current polygon."""
    def setPoints(self, pointArray: int, space: Any) -> MItMeshPolygon:
        """Sets new locations for vertices of the current polygon that the iterator is pointing to."""
    def setUV(self, vertexId: int, uvPoint: Any, uvSet: Any = None) -> MItMeshPolygon:
        """Modify the UV value for the given vertex in the current face."""
    def setUVs(self, uArray: Any, vArray: Any, uvSet: Any = None) -> MItMeshPolygon:
        """Modify the UV value for all vertices in the current face."""
    def tangentIndex(self, localVertexIndex: int) -> int:
        """Returns the tangent (or binormal) index for the specified vertex."""
    def updateSurface(self) -> MItMeshPolygon:
        """Signal that this polygonal surface has changed and needs to redraw itself."""
    def vertexIndex(self, index: int) -> int:
        """Returns the object-relative index of the specified vertex of the current polygon."""
    def zeroArea(self) -> bool:
        """This method checks if its a zero area face"""
    def zeroUVArea(self, uvSet: Any = None) -> bool:
        """This method checks if the UV area of the face is zero"""

class MItMeshVertex:
    def __init__(self, object: MObject, space: int | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def connectedToEdge(self, index: int) -> bool:
        """This method determines whether the given edge contains the current vertex"""
    def connectedToFace(self, index: int) -> bool:
        """This method determines whether the given face contains the current vertex"""
    def count(self) -> int:
        """Return the number of vertices in the iteration"""
    def currentItem(self) -> MObject:
        """Get the current vertex in the iteration as a component."""
    def geomChanged(self) -> MItMeshVertex:
        """Reset the geom pointer in the MItMeshVertex. If you're using MFnMesh to"""
    def getColor(self, colorSetName: Any = None) -> MColor:
        """getColor(faceIndex, colorSetName=None) -> MColor"""
    def getColorIndices(self, colorSetName: Any = None) -> MIntArray:
        """This method returns the colorIndices into the color array see MFnMesh::getColors()"""
    def getColors(self, colorSetName: Any = None) -> MColorArray:
        """This method gets the colors of the current vertex for each face it"""
    def getConnectedEdges(self) -> MIntArray:
        """This method gets the indices of the edges contained in the current vertex."""
    def getConnectedFaces(self) -> MIntArray:
        """This method gets the indices of the faces connected to the current vertex."""
    def getConnectedVertices(self) -> MIntArray:
        """This method gets the indices of the vertices surrounding the current vertex."""
    def getNormal(self, space: int) -> MVector:
        """getNormal(faceIndex, space=kObject) -> MVector"""
    def getNormalIndices(self) -> MIntArray:
        """This method returns the normal indices of the face/vertex associated"""
    def getNormals(self, space: int) -> MVectorArray:
        """Return the normals of the current vertex for all faces"""
    def getOppositeVertex(self, edgeId: int) -> int:
        """This method gets the other vertex of the given edge"""
    def getUV(self, uvSet: Any, arg: Any, uvSet_: Any = None) -> Any:
        """Get the shared UV value at this vertex."""
    def getUVIndices(self, uvSet: Any = None) -> MIntArray:
        """This method returns the uv indices into the normal array see MFnMesh::getUVs()"""
    def getUVs(self, uvSet: Any = None) -> Any:
        """Get the UV values for all mapped faces at the current vertex."""
    def hasColor(self, faceIndex: int | None = None) -> bool:
        """hasColor(index) -> bool"""
    def index(self) -> int:
        """Returns the index of the current vertex in the vertex list for this"""
    def isDone(self) -> bool:
        """Indicates if all of the vertices have been traversed yet."""
    def iter(self) -> MItMeshVertex:
        """Initializes the iterator object for pythonic iteration."""
    def iternext(self) -> MItMeshVertex:
        """Used in pythonic iteration to move the iterator"""
    def next(self) -> None:
        """Advance to the next edge in the iteration."""
    def numConnectedEdges(self) -> int:
        """This Method checks for the number of connected Edges on this vertex"""
    def numConnectedFaces(self) -> int:
        """This Method checks for the number of Connected Faces"""
    def numUVs(self, uvSet: Any = None) -> int:
        """This method returns the number of unique UVs mapped on this vertex"""
    def onBoundary(self) -> bool:
        """This method determines whether the current vertex is on a Boundary"""
    def position(self, space: int | None = None) -> MPoint:
        """Return the position of the current vertex in the specified space."""
    def reset(self, polyObject: MDagPath | None = None) -> MItMeshVertex:
        """reset(polyObject) -> self"""
    def setIndex(self, index: int) -> int:
        """This method sets the index of the current vertex to be accessed."""
    def setPosition(self, point: MPoint, space: int) -> MItMeshVertex:
        """Set the position of the current vertex in the given space."""
    def setUV(self, uvPoint: Any, uvSet: Any, uvPoint_: Any, uvSet_: Any = None) -> MItMeshVertex:
        """Set the shared UV value at this vertex"""
    def setUVs(self, uArray: Any, vArray: Any, faceIds: Any, uvSet: Any = None) -> MItMeshVertex:
        """Set the UV value for the specified faces at the current vertex."""
    def translateBy(self, vector: MVector, space: int) -> MItMeshVertex:
        """Translate the current vertex by the amount specified"""
    def updateSurface(self) -> MItMeshVertex:
        """Signal that this polygonal surface has changed and needs to redraw itself."""

class MItSelectionList:
    kAnimSelectionItem: Any
    kDNselectionItem: Any
    kDagSelectionItem: Any
    kPlugSelectionItem: Any
    kUnknownItem: Any
    def __init__(self, list: MSelectionList, filterType: int | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getComponent(self) -> tuple[Any]:
        """This method retrieves the dag path and the component of the current selection item."""
    def getDagPath(self) -> MDagPath:
        """This method retrieves the dag path of the current selection item."""
    def getDependNode(self) -> MObject:
        """This method retrieves the dependency node of the current selection itemRaises kFailure if there is no dependency node associated with the current item"""
    def getPlug(self) -> MPlug:
        """This method retrieves the plug of the current selection item."""
    def getStrings(self) -> list[str]:
        """Get the string representation of the current item in the selection list."""
    def hasComponents(self) -> bool:
        """Returns whether or not the current selection item has components."""
    def isDone(self) -> bool:
        """Specifies whether or not there is anything more to iterator over."""
    def itemType(self) -> int:
        """Returns the current selection item type."""
    def iter(self) -> MItSelectionList:
        """Initializes the iterator object for pythonic iteration."""
    def iternext(self) -> MItSelectionList:
        """Used in pythonic iteration to move the iterator"""
    def next(self) -> MItSelectionList:
        """Advance to the next item. If components are selected then advance to next component."""
    def reset(self) -> MItSelectionList:
        """Reset the iterator."""
    def setFilter(self, filter: int) -> MItSelectionList:
        """Apply a filter to the iteration."""

class MItSurfaceCV:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def currentItem(self) -> MObject:
        """Get the current CV in the iteration as a component."""
    def hasHistoryOnCreate(self) -> bool:
        """This method determines if the shape was created with history."""
    def index(self) -> int:
        """Get the index of the current CV as it appears in CV array for this surface."""
    def isDone(self) -> bool:
        """Returns True if the iteration is finished, i.e. there are no more CVs to iterate on."""
    def isRowDone(self) -> bool:
        """Returns True if the current row has no more CVs to iterate over."""
    def iter(self) -> MItSurfaceCV:
        """Initializes the iterator object for pythonic iteration."""
    def iternext(self) -> MItSurfaceCV:
        """Used in pythonic iteration to move the iterator"""
    def next(self) -> MItSurfaceCV:
        """Advance to the next CV in the iteration."""
    def nextRow(self) -> MItSurfaceCV:
        """Advance to the next row in the iteration."""
    def position(self, space: Any) -> MPoint:
        """Returns the position of the current CV in the iteration in the specified space."""
    def reset(self) -> MItSurfaceCV:
        """reset(surface, useURows=True) -> self"""
    def setPosition(self, point: Any, space: Any) -> MItSurfaceCV:
        """Set the position of the current CV in the iteration to the specified point."""
    def translateBy(self, vector: Any, space: Any) -> MItSurfaceCV:
        """Move the current CV in the iteration by the sepcified vector."""
    def updateSurface(self) -> MItSurfaceCV:
        """This method is used to signal the surface that it has been changed and needs to redraw itself."""
    def uvIndices(self, arg: Any, indexV: Any) -> Any:
        """Get the u and v index of the current CV."""

class MIteratorType:
    filterList: Any
    filterListEnabled: Any
    filterType: Any
    kMDagPathObject: Any
    kMObject: Any
    kMPlugObject: Any
    objectType: Any
    def __init__(self) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MLockMessage:
    kAddAttr: Any
    kChildReorder: Any
    kCreateChildInstance: Any
    kCreateNodeInstance: Any
    kCreateParentInstance: Any
    kDefaultAction: Any
    kDelete: Any
    kDoAction: Any
    kDoNotDoAction: Any
    kGroup: Any
    kInvalid: Any
    kInvalidDAG: Any
    kInvalidPlug: Any
    kLast: Any
    kLastDAG: Any
    kLastPlug: Any
    kLockAttr: Any
    kLockNode: Any
    kPlugAttrValChange: Any
    kPlugConnect: Any
    kPlugDisconnect: Any
    kPlugLockAttr: Any
    kPlugRemoveAttr: Any
    kPlugRenameAttr: Any
    kPlugUnlockAttr: Any
    kRemoveAttr: Any
    kRename: Any
    kRenameAttr: Any
    kReparent: Any
    kUnGroup: Any
    kUnlockAttr: Any
    kUnlockNode: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
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
    @staticmethod
    def setNodeLockDAGQueryCallback(dagPath: MDagPath, function: int, clientData: None = None) -> int:
        """This methods registers a callback that is invoked in any situation"""
    @staticmethod
    def setNodeLockQueryCallback(node: MObject, function: int, clientData: None = None) -> int:
        """This methods registers a callback that is invoked in any locking"""
    @staticmethod
    def setPlugLockQueryCallback(plug: MPlug | MObject, function: int, clientData: None = None) -> int:
        """This method registers a callback that is invoked in any locking"""

class MMatrix:
    kIdentity: Any
    kTolerance: Any
    def __init__(self, src: MMatrix | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def adjoint(self) -> MMatrix:
        """Returns a new matrix containing this matrix's adjoint."""
    def det3x3(self) -> float:
        """Returns the determinant of the 3x3 matrix formed by the first 3 elements of the first 3 rows of this matrix."""
    def det4x4(self) -> float:
        """Returns this matrix's determinant."""
    def getElement(self, row: int, column: int) -> float:
        """Returns the matrix element for the specified row and column."""
    def homogenize(self) -> MMatrix:
        """Returns a new matrix containing the homogenized version of this matrix."""
    def inverse(self) -> MMatrix:
        """Returns a new matrix containing this matrix's inverse."""
    def isEquivalent(self, other: MMatrix, tolerance: float = 1e-8) -> bool:
        """Test for equivalence of two matrices, within a tolerance."""
    def isSingular(self) -> bool:
        """Returns True if this matrix is singular."""
    def setElement(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the matrix element for the specified row and column."""
    def setToIdentity(self) -> MMatrix:
        """Sets this matrix to the identity."""
    def setToProduct(self, left: MMatrix, right: MMatrix) -> MMatrix:
        """Sets this matrix to the product of the two matrices passed in."""
    def transpose(self) -> MMatrix:
        """Returns a new matrix containing this matrix's transpose."""

class MMatrixArray:
    sizeIncrement: Any
    def __init__(self, other: MMatrixArray | int | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def append(self, element: MMatrix) -> None:
        """Add a value to the end of the array."""
    def clear(self) -> None:
        """Remove all elements from the array."""
    def copy(self, source: MMatrixArray) -> None:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self, element: MMatrix, index: int) -> None:
        """Insert a new value into the array at the given index."""
    def remove(self, index: int) -> None:
        """Remove an element from the array."""
    def setLength(self, length: int) -> None:
        """Grow or shrink the array to contain a specific number of elements."""

class MMeshIntersector:
    isCreated: Any
    def __init__(self, arg: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def create(self, mesh: MMatrix, matrix: MIntArray) -> MMeshIntersector:
        """Creates the internal data required by the intersector. It is a"""
    def getClosestPoint(self, referencePoint: MPoint, maxDistance: float) -> MPointOnMesh:
        """Finds the closest point within 'maxDistance' of the reference point"""

class MMeshIsectAccelParams:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MMeshSmoothOptions:
    boundaryRule: Any
    divisions: Any
    kCatmullClark: Any
    kCreaseAll: Any
    kCreaseEdge: Any
    kInvalid: Any
    kInvalidSubdivision: Any
    kLast: Any
    kLastSubdivision: Any
    kLegacy: Any
    kOpenSubdivCatmullClarkAdaptive: Any
    kOpenSubdivCatmullClarkUniform: Any
    keepBorderEdge: Any
    keepHardEdge: Any
    propEdgeHardness: Any
    smoothUVs: Any
    smoothness: Any
    subdivisionType: Any
    def __init__(self, arg: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MMessage:
    kDefaultAction: Any
    kDoAction: Any
    kDoNotDoAction: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
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

class MModelMessage:
    kActiveListModified: Any
    kDefaultAction: Any
    kDoAction: Any
    kDoNotDoAction: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def addAfterDuplicateCallback(function: int, clientData: None = None) -> int:
        """This method registers a callback that is called after a duplicate"""
    @staticmethod
    def addBeforeDuplicateCallback(function: int, clientData: None = None) -> int:
        """This method registers a callback that is called whenever a duplicate"""
    @staticmethod
    def addCallback(message: Any, function: int, clientData: None = None) -> int:
        """Adds a new callback for the specified model message."""
    @staticmethod
    def addNodeAddedToModelCallback(dagNode: MObject, function: int, clientData: None = None) -> int:
        """This method registers a callback that is called when a dag node is about"""
    @staticmethod
    def addNodeRemovedFromModelCallback(dagNode: MObject, function: int, clientData: None = None) -> int:
        """This method registers a callback that is called when the"""
    @staticmethod
    def addPostDuplicateNodeListCallback(function: int, clientData: None = None) -> int:
        """This method registers a callback that is called after a duplicate"""
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

class MNamespace:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def addNamespace(arg: Any, arg_: Any) -> Any:
        """Create the namespace 'name'. If the `parent' namespace is given"""
    @staticmethod
    def currentNamespace() -> str:
        """Get the name of the current namespace. This name is returned """
    @staticmethod
    def getNamespaceFromName(arg: Any) -> str:
        """Get namespace from a full name. """
    @staticmethod
    def getNamespaceObjects(arg: Any, arg_: bool) -> MObjectArray:
        """Return an array of MObjects representing the object contained within """
    @staticmethod
    def getNamespaces(arg: Any, arg_: bool) -> Any:
        """Return a list of all namespaces in the current namespace."""
    @staticmethod
    def makeNamepathAbsolute(arg: Any) -> str:
        """Make a namepath which is relative to the root into an absolute """
    @staticmethod
    def moveNamespace(arg: Any, arg_: Any, arg__: bool) -> Any:
        """Move the contents of the namespace 'src' into the namespace 'dst'. """
    @staticmethod
    def namespaceExists(arg: Any) -> bool:
        """Check if a given namespace exists."""
    @staticmethod
    def parentNamespace() -> str:
        """Get the name of the current namespace's parent. This name is returned """
    @staticmethod
    def relativeNames() -> bool:
        """Query Maya's current 'relative name lookup' state. Relative name """
    @staticmethod
    def removeNamespace(arg: Any, arg_: bool) -> Any:
        """Remove the specified namespace. """
    @staticmethod
    def renameNamespace(arg: Any, arg_: Any, arg__: Any) -> Any:
        """Rename the specified namespace to a new name with optional parent name. """
    @staticmethod
    def rootNamespace() -> str:
        """Get the name of the root namespace. This name is an absolute"""
    @staticmethod
    def setCurrentNamespace(arg: Any) -> str:
        """Set the specified namespace to be the current namespace. The 'name' """
    @staticmethod
    def setRelativeNames(arg: bool) -> Any:
        """Set relative name lookup mode. """
    @staticmethod
    def stripNamespaceFromName(arg: Any) -> str:
        """Strips the namespace from a full name. """
    @staticmethod
    def validateName(arg: Any) -> str:
        """Convert the specified name to a validated name which """

class MNodeCacheDisablingInfo:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getCacheDisabled(self) -> bool:
        """Return True if the cache should be disabled because of this node."""
    def reset(self) -> Any:
        """Resets the disabling info to an enabled state."""
    def setCacheDisabled(self, bool: bool) -> Any:
        """Set if the cache should be disabled because of this node."""
    def setMitigation(self, mitigation: Any) -> Any:
        """Sets the mitigation to fix the reason for disabling Cached Playback."""
    def setReason(self, reason: Any) -> Any:
        """Sets the reason for disabling Cached Playback."""

class MNodeCacheSetupInfo:
    kLastPreference: Any
    kLastRequirement: Any
    kSimulationSupport: Any
    kWantToCacheByDefault: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getPreference(self, PreferenceFlag: Any) -> bool:
        """Get a preference flag for this node."""
    def getRequirement(self, RequirementFlag: Any) -> bool:
        """Get a requirement flag for this node."""
    def setPreference(self, PreferenceFlag: Any, bool: Any) -> Any:
        """Set a preference flag for this node."""
    def setRequirement(self, RequirementFlag: Any, bool: Any) -> Any:
        """Set a requirement flag for this node."""

class MNodeClass:
    attributeCount: Any
    classification: Any
    pluginName: Any
    typeId: Any
    typeName: Any
    def __init__(self, nodeClassName: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addExtensionAttribute(self, attr: MObject) -> None:
        """Adds an extension attribute to the node class. An extension attribute is a class-level attribute which has been added dynamically to a node class. Because it is added at the class level, all nodes of that class will have the given attribute, and will only store the attribute's value if it differs from the default. Returns the type of the object at the end of the path."""
    def attribute(self, index: Any) -> MObject:
        """If passed an int: Returns the node class's i'th attribute. Raises IndexError if index is out of bounds.  If passed a string, Returns the node class's attribute having the given name. Returns MObject.kNullObj if the class does not have an attribute with that name."""
    def getAttributes(self) -> MObjectArray:
        """Returns an MObjectArray array containing all of the node class's attributes."""
    def hasAttribute(self, attrName: Any) -> bool:
        """Returns True if the node class has an attribute of the given name, False otherwise."""
    def removeExtensionAttribute(self, attr: MObject) -> None:
        """Removes an extension attribute from the node class. Raises ValueError if attr is not an extension attribute of this node class."""
    def removeExtensionAttributeIfUnset(self, attr: MObject) -> None:
        """Removes an extension attribute from the node class, but only if there are no nodes in the graph with non-default values for this attribute. Returns True if the attribute was removed, False otherwise. Raises ValueError if attr is not an extension attribute of this node class."""

class MNodeMessage:
    kAttributeAdded: Any
    kAttributeArrayAdded: Any
    kAttributeArrayRemoved: Any
    kAttributeEval: Any
    kAttributeKeyable: Any
    kAttributeLocked: Any
    kAttributeRemoved: Any
    kAttributeRenamed: Any
    kAttributeSet: Any
    kAttributeUnkeyable: Any
    kAttributeUnlocked: Any
    kConnectionBroken: Any
    kConnectionMade: Any
    kDefaultAction: Any
    kDoAction: Any
    kDoNotDoAction: Any
    kIncomingDirection: Any
    kKeyChangeInvalid: Any
    kKeyChangeLast: Any
    kLast: Any
    kMakeKeyable: Any
    kMakeUnkeyable: Any
    kOtherPlugSet: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def addAttributeAddedOrRemovedCallback(node: MObject, function: int, clientData: None = None) -> int:
        """Registers callbacks for attribute add/removed messages."""
    @staticmethod
    def addAttributeChangedCallback(node: MObject, function: int, clientData: None = None) -> int:
        """This method registers a callback for attribute changed messages."""
    @staticmethod
    def addKeyableChangeOverride(plug: MPlug, function: int, clientData: None = None) -> int:
        """This method registers a callback that is invoked by any class that"""
    @staticmethod
    def addNameChangedCallback(node: MObject, function: int, clientData: None = None) -> int:
        """Registers a callback for name changed messages."""
    @staticmethod
    def addNodeAboutToDeleteCallback(node: MObject, function: int, clientData: None = None) -> int:
        """Registers a callback which will get called when a node is about to"""
    @staticmethod
    def addNodeDestroyedCallback(node: MObject, function: int, clientData: None = None) -> int:
        """Registers a callback which will get called when a node's destructor is"""
    @staticmethod
    def addNodeDirtyCallback(node: MObject, function: int, clientData: None = None) -> int:
        """Registers a callback for node dirty messages."""
    @staticmethod
    def addNodeDirtyPlugCallback(node: MObject, function: int, clientData: None = None) -> int:
        """Registers a callback for node dirty messages.  This callback provides"""
    @staticmethod
    def addNodePreRemovalCallback(node: MObject, function: int, clientData: None = None) -> int:
        """Registers a callback which will get called before a node is deleted."""
    @staticmethod
    def addUuidChangedCallback(node: MObject, function: int, clientData: None = None) -> int:
        """Registers a callback for UUID changed messages."""
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

class MObject:
    apiTypeStr: Any
    kNullObj: Any
    def __init__(self, other: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def apiType(self) -> int:
        """Returns the function set type for the object."""
    def hasFn(self, type: int) -> bool:
        """Tests whether object is compatible with the specified function set."""
    def isNull(self) -> bool:
        """Tests whether there is an internal Maya object."""

class MObjectArray:
    sizeIncrement: Any
    def __init__(self, other: MObjectArray | int | None = None, initialValue: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def append(self, element: MObject) -> None:
        """Add a value to the end of the array."""
    def clear(self) -> None:
        """Remove all elements from the array."""
    def copy(self, source: MObjectArray) -> None:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self, element: MObject, index: int) -> None:
        """Insert a new value into the array at the given index."""
    def remove(self, index: int) -> None:
        """Remove an element from the array."""
    def setLength(self, length: int) -> None:
        """Grow or shrink the array to contain a specific number of elements."""

class MObjectHandle:
    def __init__(self, object: MObject | MObjectHandle | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def assign(self, source: Any) -> MObjectHandle:
        """Assigns this MObjectHandle to an instance of another MObjectHandle, or to a MObject instance."""
    def hashCode(self) -> int:
        """Returns a hash code for the internal Maya object referenced by the MObject within this MObjectHandle. If the MObject is null or no longer alive then 0 will be returned, otherwise the hash code is guaranteed to be non-zero"""
    def isAlive(self) -> bool:
        """Returns the live state of the associated MObject. An object can still be 'alive' but not 'valid' (eg. a deleted object that resides in the undo queue)."""
    def isValid(self) -> bool:
        """Returns the validity of the associated MObject."""
    def object(self) -> MObject:
        """Returns the MObject associated with this handle. The returned MObject will be MObject.kNullObj if the object is invalid."""

class MObjectSetMessage:
    kDefaultAction: Any
    kDoAction: Any
    kDoNotDoAction: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def addSetMembersModifiedCallback(node: MObject, function: int, clientData: None = None) -> int:
        """Registers callbacks for set modified messages."""
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

class MPlane:
    def __init__(self) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def distance(self) -> float:
        """Returns the distance of the plane along the normal."""
    def distanceToPoint(self, point: Any, signed: bool = False) -> float:
        """Returns the distance from the plane to the specified point."""
    def normal(self) -> MVector:
        """Returns the normal of the plane."""
    def setPlane(self, a: float | MVector, b: float, c: float, d: float) -> MPlane:
        """setPlane(n, d) -> self"""

class MPlug:
    info: Any
    isArray: Any
    isCaching: Any
    isChannelBox: Any
    isChild: Any
    isCompound: Any
    isConnected: Any
    isDestination: Any
    isDynamic: Any
    isElement: Any
    isFromReferencedFile: Any
    isIgnoredWhenRendering: Any
    isKeyable: Any
    isLocked: Any
    isNetworked: Any
    isNull: Any
    isProcedural: Any
    isProxy: Any
    isSource: Any
    kAll: Any
    kChanged: Any
    kChildrenNotFreeToChange: Any
    kFreeToChange: Any
    kLastAttrSelector: Any
    kNonDefault: Any
    kNotFreeToChange: Any
    def __init__(self, in_: MPlug | MObject | None = None, attribute: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def array(self) -> MPlug:
        """Returns a plug for the array of plugs of which this plug is an element."""
    def asBool(self) -> bool:
        """Retrieves the plug's value, as a boolean."""
    def asChar(self) -> Any:
        """Retrieves the plug's value, as a single-byte integer."""
    def asDouble(self) -> float:
        """Retrieves the plug's value, as a double-precision float."""
    def asFloat(self) -> float:
        """Retrieves the plug's value, as a single-precision float."""
    def asInt(self) -> int:
        """Retrieves the plug's value, as a regular integer."""
    def asMAngle(self) -> MAngle:
        """Retrieves the plug's value, as an MAngle."""
    def asMDataHandle(self) -> MDataHandle:
        """Retrieve the current value of the attribute this plug references."""
    def asMDistance(self) -> MDistance:
        """Retrieves the plug's value, as an MDistance."""
    def asMObject(self) -> MObject:
        """Retrieves the plug's value, as as an MObject containing a direct reference to the plug's data."""
    def asMTime(self) -> MTime:
        """Retrieves the plug's value, as an MTime."""
    def asShort(self) -> Any:
        """Retrieves the plug's value, as a short integer."""
    def asString(self) -> Any:
        """Retrieves the plug's value, as a string."""
    def attribute(self) -> MObject:
        """Returns the attribute currently referenced by this plug."""
    def child(self, index: int) -> MPlug:
        """Returns a plug for the specified child attribute of this plug."""
    def connectedTo(self, asDst: bool, asSrc: bool) -> MPlugArray:
        """Returns an array of plugs which are connected to this one."""
    def connectionByPhysicalIndex(self, physicalIndex: int) -> MPlug:
        """Returns a plug for the index'th connected element of this plug."""
    def constructHandle(self) -> MDataHandle:
        """Constructs a data handle for the plug."""
    def copy(self, *args: Any, **kwargs: Any) -> Any:
        """Copies one plug to another."""
    def destinations(self, theDestinations: MPlugArray) -> bool:
        """If this plug is a source, return the destination plugs connected to it."""
    def destinationsWithConversions(self, theDestinations: MPlugArray) -> bool:
        """If this plug is a source, return the destination plugs connected to it."""
    def destructHandle(self) -> None:
        """Destroys a data handle previously constructed using constructHandle()."""
    def elementByLogicalIndex(self, logicalIndex: int) -> MPlug:
        """Returns a plug for the element of this plug array having the specified logical index."""
    def elementByPhysicalIndex(self, physicalIndex: int) -> MPlug:
        """Returns a plug for the element of this plug array having the specified physical index."""
    def evaluateNumElements(self) -> int:
        """Like numElements() but evaluates all connected elements first to ensure that they are included in the count."""
    def getExistingArrayAttributeIndices(self, indices: MIntArray) -> int:
        """Returns an array of all the plug's logical indices which are currently in use."""
    def getSetAttrCmds(self, valueSelector: Any = None, useLongNames: bool | None = None) -> Any:
        """Returns a list of strings containing the setAttr commands (in MEL syntax) for this plug and all of its descendents."""
    def isDefaultValue(self, forceEval: bool | None = None) -> bool:
        """Returns a value indicating if the plug's value is equivalent to the plug's default value."""
    def isExactlyEqual(self, other: MPlug) -> bool:
        """Returns true if both plugs refer to the same node, attribute and multi-index. If either or both plugs are null, the plugs are not considered equal."""
    def isFreeToChange(self, checkParents: bool | None = None, checkChildren: bool | None = None) -> int:
        """Returns a value indicating if the plug's value can be changed, after taking into account the effects of locking and connections."""
    def logicalIndex(self) -> int:
        """Returns this plug's logical index within its parent array."""
    def name(self) -> Any:
        """Returns the name of the plug."""
    def node(self) -> MObject:
        """Returns the node that this plug belongs to."""
    def numChildren(self) -> int:
        """Returns the number of children this plug has."""
    def numConnectedChildren(self) -> int:
        """Returns the number of this plug's children which have connections."""
    def numConnectedElements(self) -> int:
        """Returns the number of this plug's elements which have connections."""
    def numElements(self) -> int:
        """Returns the number of the plug's logical indices which are currently in use. Connected elements which have not yet been evaluated may not yet fully exist and may be excluded from the count."""
    def parent(self) -> MPlug:
        """Returns a plug for the parent of this plug."""
    def partialName(self, includeNodeName: bool | None = None, includeNonMandatoryIndices: bool | None = None, includeInstancedIndices: bool | None = None, useAlias: bool | None = None, useFullAttributePath: bool | None = None, useLongNames: bool | None = None) -> Any:
        """Returns the name of the plug, formatted according to various criteria."""
    def proxied(self) -> MPlug:
        """Returns the proxied plug for this plug."""
    def selectAncestorLogicalIndex(self, index: int, attribute: MObject | None = None) -> None:
        """Changes the logical index of the specified attribute in the plug's path."""
    def setAttribute(self) -> MObject:
        """Switches the plug to reference the given attribute of the same node as the previously referenced attribute."""
    def setBool(self, value: bool) -> None:
        """Sets the plug's value as a boolean."""
    def setChar(self, arg: Any) -> None:
        """Sets the plug's value as a single-byte integer."""
    def setDouble(self, value: float) -> None:
        """Sets the plug's value as a double-precision float."""
    def setFloat(self, value: float) -> None:
        """Sets the plug's value as a single-precision float."""
    def setInt(self, value: int) -> None:
        """Sets the plug's value as a regular integer."""
    def setMAngle(self) -> None:
        """Sets the plug's value as an MAngle."""
    def setMDataHandle(self) -> None:
        """Sets the plug's value as a data handle."""
    def setMDistance(self) -> None:
        """Sets the plug's value as an MDistance."""
    def setMObject(self, value: MObject) -> None:
        """Sets the plug's value as an MObject."""
    def setMPxData(self) -> None:
        """Sets the plug's value using custom plug-in data."""
    def setMTime(self) -> None:
        """Sets the plug's value as an MTime."""
    def setNumElements(self, arg: int) -> None:
        """Pre-allocates space for count elements in an array of plugs."""
    def setShort(self, arg: Any) -> None:
        """Sets the plug's value as a short integer."""
    def setString(self, value: Any) -> None:
        """Sets the plug's value as a string."""
    def source(self) -> MPlug:
        """If this plug is a destination, return the source plug connected to it."""
    def sourceWithConversion(self) -> MPlug:
        """If this plug is a destination, return the source plug connected to it."""

class MPlugArray:
    sizeIncrement: Any
    def __init__(self, other: MPlugArray | int | None = None, initialValue: MPlug | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def append(self, element: MPlug) -> None:
        """Add a value to the end of the array."""
    def clear(self) -> None:
        """Remove all elements from the array."""
    def copy(self, source: MPlugArray) -> None:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self, element: MPlug, index: int) -> None:
        """Insert a new value into the array at the given index."""
    def remove(self, index: int) -> None:
        """Remove an element from the array."""
    def setLength(self, length: int) -> None:
        """Grow or shrink the array to contain a specific number of elements."""

class MPoint:
    kOrigin: Any
    kTolerance: Any
    w: float
    x: float
    y: float
    z: float
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0, w: float = 1.0) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def cartesianize(self) -> MPoint:
        """Convert point to cartesian form."""
    def distanceTo(self, other: MPoint) -> float:
        """Return distance between this point and another."""
    def homogenize(self) -> MPoint:
        """Convert point to homogenous form."""
    def isEquivalent(self, other: MPoint, tolerance: float = 1e-10) -> bool:
        """Test for equivalence of two points, within a tolerance."""
    def rationalize(self) -> MPoint:
        """Convert point to rational form."""

class MPointArray:
    sizeIncrement: Any
    def __init__(self, other: MPointArray | int | None = None, initialValue: MPoint | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def append(self, element: MPoint | float, y: float, z: float | None = None, w: float | None = None) -> None:
        """Add a value to the end of the array."""
    def clear(self) -> None:
        """Remove all elements from the array."""
    def copy(self, source: MPointArray) -> None:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self, element: MPoint, index: int) -> None:
        """Insert a new value into the array at the given index."""
    def remove(self, index: int) -> None:
        """Remove an element from the array."""
    def setLength(self, length: int) -> None:
        """Grow or shrink the array to contain a specific number of elements."""

class MPointOnMesh:
    barycentricCoords: Any
    face: Any
    normal: Any
    point: Any
    triangle: Any
    def __init__(self) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MPolyMessage:
    kDefaultAction: Any
    kDoAction: Any
    kDoNotDoAction: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def addPolyComponentIdChangedCallback(node: MObject, arg: int, function: int, clientData: None = None) -> int:
        """This method registers a callback that should be called whenever a poly"""
    @staticmethod
    def addPolyTopologyChangedCallback(node: MObject, function: int, clientData: None = None) -> int:
        """This method registers a callback that will be called when a node impacting"""
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

class MPxAttributePatternFactory:
    def __init__(self) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MPxCommand:
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
    def doIt(self, args: MArgList) -> None:
        """Called by Maya to execute the command."""
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

class MPxData:
    kData: Any
    kGeometryData: Any
    kLast: Any
    def __init__(self) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def copy(self, src: MPxData) -> MPxData:
        """This method initializes an instance of an MPxData derived class from another existing instance.  This method can be thought of as the second half of a copy constructor for the class.  The default constructor has already been called for the instance, and this method is used to set the private data by copying the values from an existing instance."""
    def name(self) -> Any:
        """Returns the name of the custom data type."""
    def readASCII(self, argList: MArgList, endOfTheLastParsedElement: Any) -> int:
        """Creates Data in Data Block as specified by input from ASCII file record."""
    def readBinary(self, in_: int, length: Any) -> int:
        """Creates Data in Data Block as specified by binary data from the given stream."""
    def typeId(self) -> MTypeId:
        """Determines the type id of the Data object."""
    def writeASCII(self) -> Any:
        """Encodes Data in accordance with the ASCII file format and returns as string."""
    def writeBinary(self) -> Any:
        """Encodes Data in accordance with the binary file format and returns as bytearray."""

class MPxGeometryData:
    kData: Any
    kGeometryData: Any
    kLast: Any
    matrix: Any
    def __init__(self) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def copy(self, src: MPxData) -> MPxGeometryData:
        """This method initializes an instance of an MPxData derived class from another existing instance.  This method can be thought of as the second half of a copy constructor for the class.  The default constructor has already been called for the instance, and this method is used to set the private data by copying the values from an existing instance."""
    def deleteComponent(self, compList: MObjectArray) -> bool:
        """This method should be overridden if this data is to support component deletion. For user defined shapes (MPxSurfaceShape) which support components, this method must be overridden if component deletion is to be supported when the shape has history."""
    def deleteComponentsFromGroups(self, compList: MObjectArray, groupIdArray: MIntArray, groupComponentArray: MObjectArray) -> bool:
        """This method should be overridden to modify the groups that flows along with the geometry, as part of the data, based on the components being deleted. It should intelligently update the groups based on what gets deleted. The class MFnGeometryData can be used to access and modify grouping information for data."""
    def getMatrix(self, matrix: Any) -> bool:
        """Gets the matrix associated to MPxGeometryData and retursn True if is identity"""
    def iterator(self, componentList: MObjectArray, component: MObject, useComponents: bool, world: bool | None = None) -> MPxGeometryIterator:
        """Associates a control point based geometry iterator with this data."""
    def name(self) -> Any:
        """Returns the name of the custom data type."""
    def readASCII(self, argList: MArgList, endOfTheLastParsedElement: Any) -> int:
        """Creates Data in Data Block as specified by input from ASCII file record."""
    def readBinary(self, in_: int, length: Any) -> int:
        """Creates Data in Data Block as specified by binary data from the given stream."""
    def smartCopy(self, srcGeom: MPxGeometryData) -> MPxGeometryData:
        """This method is used in conjunction with MPxSurfaceShape classes which support maya's deformations."""
    def typeId(self) -> MTypeId:
        """Determines the type id of the Data object."""
    def updateCompleteVertexGroup(self, component: MObject) -> bool:
        """This method is used in conjunction with MPxSurfaceShape classes which support maya's deformations."""
    def writeASCII(self) -> Any:
        """Encodes Data in accordance with the ASCII file format and returns as string."""
    def writeBinary(self) -> Any:
        """Encodes Data in accordance with the binary file format and returns as bytearray."""

class MPxGeometryIterator:
    currentPoint: Any
    maxPoints: Any
    def __init__(self, userGeometry: None, components: MObjectArray | MObject) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def component(self) -> MObject:
        """Returns a component for the current item in the iteration."""
    def geometry(self) -> Any:
        """Returns the user geometry that this iterator is iterating over."""
    def hasNormals(self) -> bool:
        """Returns whether the underlying geometry has normals."""
    def hasPoints(self) -> bool:
        """Returns whether the underlying geometry has point data."""
    def index(self) -> int:
        """Returns a unique index for the current item in the iteration."""
    def indexUnsimplified(self) -> int:
        """Returns a unique index for the current item in the iteration."""
    def isDone(self) -> bool:
        """Returns whether all the items have been traversed yet."""
    def iteratorCount(self) -> int:
        """Returns an estimate of how many items will be iterated over."""
    def next(self) -> MPxGeometryIterator:
        """Advances to the next component."""
    def point(self) -> MPoint:
        """Returns the current component's positional data."""
    def reset(self) -> MPxGeometryIterator:
        """Resets the iterator to the start of the components so that another pass over them may be made."""
    def setObject(self, shape: Any) -> MPxGeometryIterator:
        """Optional method to set a shape object to iterate over to allow tweaking of the shape's history (input geometry)."""
    def setPoint(self, point: Any) -> MPxGeometryIterator:
        """Sets the current component's positional data."""
    def setPointGetNext(self, point: Any) -> int:
        """Sets the current component's positional data, and returns the next index value."""

class MPxNode:
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
    def addExternalContentForFileAttr(self, table: MObject, attr: Any) -> bool:
        """This method is a helper for derived clases implementing getExternalContent().  It augments the external content info table passed in with an entry describing external content whose location is described by the specified attribute."""
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> None:
        """This method specifies that a particular input attribute affects a specific output attribute.  This is required to make evaluation efficient.  When an input changes, only the affected outputs will be computed. Output attributes cannot be keyable - if they are keyable, this method will fail."""
    def compute(self, plug: Any, dataBlock: Any) -> MPxNode:
        """This method should be overridden in user defined nodes."""
    def configCache(self, evalNode: Any, schema: Any) -> None:
        """Defines the node's behavior when participating in Cached Playback."""
    def connectionBroken(self, plug: bool, otherPlug: Any, asSrc: Any) -> MPxNode:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, plug: bool, otherPlug: Any, asSrc: Any) -> MPxNode:
        """This method gets called when connections are made to attributes of this node."""
    def copyInternalData(self, node: Any) -> MPxNode:
        """This method is overriden by nodes that store attribute data in some internal format."""
    def dependsOn(self, plug: Any, otherPlug: Any) -> Any:
        """This method may be overridden by the user defined node. It should only be required to override this on rare occasions."""
    def doNotWrite(self) -> bool:
        """use this method to query the "do not write" state of this proxy node. True is returned if this node will not be saved when the maya model is written out."""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    def forceCache(self, ctx: Any) -> MDataBlock:
        """Get the datablock for this node. If there is no datablock then one will be created."""
    def getCacheSetup(self, evalNode: Any, disablingInfo: Any, setupInfo: Any, objectArray: Any) -> None:
        """Provide node-specific setup info for the Cached Playback system."""
    def getExternalContent(self, table: Any) -> MPxNode:
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
    def postConstructor(self) -> MPxNode:
        """Internally maya creates two objects when a user defined node is created, the internal MObject and the user derived object."""
    def postEvaluation(self, context: MDGContext, evalNode: MEvaluationNode, evalType: Any) -> None:
        """Clean up node's internal state after threaded evaluation."""
    def preEvaluation(self, context: MDGContext, evalNode: MEvaluationNode) -> None:
        """Prepare a node's internal state for threaded evaluation."""
    def setDependentsDirty(self, plug: MPlug, plugArray: Any) -> MPxNode:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug which Maya is marking dirty. The list of plugs for Maya to mark dirty is returned by the plug array. This method handles both dynamic as well as non-dynamic plugs and is useful in the following ways:"""
    def setDoNotWrite(self, bool: bool) -> MPxNode:
        """Use this method to mark the "do not write" state of this proxy node.  If set, this node will not be saved when the Maya model is written out. """
    def setExistWithoutInConnections(self, bool: bool) -> bool:
        """This method specifies whether or not the node can exist without input"""
    def setExistWithoutOutConnections(self, bool: bool) -> bool:
        """This method specifies whether or not the node can exist without"""
    def setExternalContent(self, table: Any) -> MPxNode:
        """This is useful in the context of content relocation.  This will be called while the scene is being loaded to apply path changes performed externally. Consequently, interaction with the rest of the scene must be kept to a minimum.  It is however valid to call this method outside of scene loading contexts."""
    def setExternalContentForFileAttr(self, attr: MObject, table: Any) -> bool:
        """This method is a helper for derived clases implementing setExternalContent().  It assigns a value to a plug with the one from the table whose key is the same as the passed in attribute name."""
    def setInternalValue(self, plug: Any, dataHandle: Any) -> bool:
        """This method is overriden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self, plug: Any, dataHandle: Any, ctx: Any) -> Any:
        """This method is obsolete. Override MPxNode.setInternalValue instead."""
    def setMPSafe(self, bool: bool) -> MPxNode:
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

class MPxSurfaceShape:
    boundingBoxCenterX: Any
    boundingBoxCenterY: Any
    boundingBoxCenterZ: Any
    center: Any
    instObjGroups: Any
    intermediateObject: Any
    inverseMatrix: Any
    isRenderable: Any
    isTemplated: Any
    kAssembly: Any
    kBlendShape: Any
    kBoundingBoxChanged: Any
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
    kParticleAttributeMapperNode: Any
    kPostEvaluationTypeLast: Any
    kRestorePoints: Any
    kSavePoints: Any
    kSkinCluster: Any
    kSpringNode: Any
    kSurfaceShape: Any
    kThreadedDeviceNode: Any
    kTransformNode: Any
    kTransformOriginalPoints: Any
    kUTangent: Any
    kUVNTriad: Any
    kUpdatePoints: Any
    kVTangent: Any
    mControlPoints: Any
    mControlValueX: Any
    mControlValueY: Any
    mControlValueZ: Any
    mHasHistoryOnCreate: Any
    matrix: Any
    nodeBoundingBox: Any
    nodeBoundingBoxMax: Any
    nodeBoundingBoxMaxX: Any
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
    useObjectColor: Any
    visibility: Any
    worldInverseMatrix: Any
    worldMatrix: Any
    def __init__(self) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def acceptsGeometryIterator(self, component: bool, writeable: bool = True, forReadOnly: bool = False) -> bool:
        """acceptsGeometryIterator(writeable=True) -> boolboundingBox() -> MBoundingBox"""
    def activeComponents(self) -> MObjectArray:
        """Returns a list of active (selected) components for the shape."""
    @staticmethod
    def addAttribute(attr: MObject) -> None:
        """This method adds a new attribute to a user defined node type during the type's initialization."""
    def addExternalContentForFileAttr(self, table: MObject, attr: Any) -> bool:
        """This method is a helper for derived clases implementing getExternalContent().  It augments the external content info table passed in with an entry describing external content whose location is described by the specified attribute."""
    @staticmethod
    def attributeAffects(whenChanges: MObject, isAffected: MObject) -> None:
        """This method specifies that a particular input attribute affects a specific output attribute.  This is required to make evaluation efficient.  When an input changes, only the affected outputs will be computed. Output attributes cannot be keyable - if they are keyable, this method will fail."""
    def boundingBox(self) -> MBoundingBox:
        """This method should be overridden to return a bounding box for the shape."""
    def cachedShapeAttr(self) -> MObject:
        """Returns the attribute containing the shape's cached geometry, if it has one."""
    def canMakeLive(self) -> bool:
        """This method is used by Maya to determine whether a surface can be made live. It can be overridden to return True if you wish to allow your surface to be made live. If you return True, you will also need to implement both closestPoint() overloads. The default is to return False."""
    def childChanged(self, state: Any) -> MPxSurfaceShape:
        """This method can be used to trigger the shape to recalculate its bounding box."""
    def closestPoint(self, toThisPoint: MPoint, theClosestPoint: MVector | float, tolerance: MPoint | None = None) -> MPxSurfaceShape:
        """closestPoint(raySource, rayDirection, theClosestPoint, theClosestNormal, findClosestOnMiss, tolerance=MPoint.kTolerance) -> bool"""
    def componentToPlugs(self, component: Any, selectionList: Any) -> MPxSurfaceShape:
        """Converts the given component into a selection list of plugs."""
    def compute(self, plug: Any, dataBlock: Any) -> MPxSurfaceShape:
        """This method should be overridden in user defined nodes."""
    def configCache(self, evalNode: Any, schema: Any) -> None:
        """Defines the node's behavior when participating in Cached Playback."""
    def connectionBroken(self, plug: bool, otherPlug: Any, asSrc: Any) -> MPxSurfaceShape:
        """This method gets called when connections are broken with attributes of this node."""
    def connectionMade(self, plug: bool, otherPlug: Any, asSrc: Any) -> MPxSurfaceShape:
        """This method gets called when connections are made to attributes of this node."""
    def convertToTweakNodePlug(self, plug: MPlug) -> bool:
        """Check if a tweak node is connected to this node. If it is, then reset the supplied plug to contain the controlPoints attribute on the tweak node."""
    def copyInternalData(self, node: Any) -> MPxSurfaceShape:
        """This method is overriden by nodes that store attribute data in some internal format."""
    def createFullRenderGroup(self) -> MObject:
        """Returns a component containing all of renderable elements in the shape."""
    def createFullVertexGroup(self) -> MObject:
        """Returns a component containing all of the vertices in the shape."""
    def deleteComponents(self, componentList: MObjectArray, undoInfo: MDoubleArray) -> bool:
        """Returns True if this method was successful, False otherwise."""
    def dependsOn(self, plug: Any, otherPlug: Any) -> Any:
        """This method may be overridden by the user defined node. It should only be required to override this on rare occasions."""
    def doNotWrite(self) -> bool:
        """use this method to query the "do not write" state of this proxy node. True is returned if this node will not be saved when the maya model is written out."""
    def excludeAsPluginShape(self) -> bool:
        """A Maya viewport can be set to not display "Plugin Shapes", which means shapes derived from MPxSurfaceShape. By overriding excludeAsPluginShape() to return False, you can change that behaviour so that this shape is still displayed even when the display of "Plugin Shapes" is disabled."""
    def existWithoutInConnections(self) -> bool:
        """Determines whether or not this node can exist without input connections."""
    def existWithoutOutConnections(self) -> bool:
        """Determines whether or not this node can exist without output connections."""
    def forceCache(self, ctx: Any) -> MDataBlock:
        """Get the datablock for this node. If there is no datablock then one will be created."""
    def geometryData(self) -> MObject:
        """Returns the geometry data of the shape. The geometry data must be derived from the MPxGeometryData class."""
    def geometryIteratorSetup(self, componentList: bool, components: Any, forReadOnly: bool = False) -> MPxGeometryIterator:
        """This method should be overridden by the user to return a geometry iterator compatible with the user's geometry."""
    def getCacheSetup(self, evalNode: Any, disablingInfo: Any, setupInfo: Any, objectArray: Any) -> None:
        """Provide node-specific setup info for the Cached Playback system."""
    def getComponentSelectionMask(self) -> MSelectionMask:
        """Returns the selection mask of the shape."""
    def getExternalContent(self, table: Any) -> MPxSurfaceShape:
        """The table populated by this method must include the location of all the content (files) used by this node, including those that do not exist.  See MExternalContentInfoTable for details."""
    def getFilesToArchive(self, shortName: bool = False, unresolvedName: bool = False, markCouldBeImageSequence: bool = False) -> list[str]:
        """Use this method to return all external files used by this node. This file list will be used by the File > Archive zip feature, maya.exe -archive and the `file -q -list` mel command."""
    def getInternalValue(self, plug: Any, dataHandle: Any) -> bool:
        """This method is overridden by nodes that store attribute data in some internal format."""
    def getInternalValueInContext(self, plug: Any, dataHandle: Any, ctx: Any) -> Any:
        """This method is obsolete. Override MPxNode.getInternalValue instead."""
    def getShapeSelectionMask(self) -> MSelectionMask:
        """Returns the selection mask of the shape."""
    def getWorldMatrix(self, block: int, instanceGeom: Any) -> MMatrix:
        """Returns MMatrix which takes a point from local object space to world space."""
    def hasActiveComponents(self) -> bool:
        """This method is used to determine whether or not the shape has active (selected) components."""
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
    def legalConnection(self, plug: bool, otherPlug: Any, asSrc: Any) -> Any:
        """This method allows you to check for legal connections being made to attributes of this node."""
    def legalDisconnection(self, plug: bool, otherPlug: Any, arsSrc: Any) -> Any:
        """This method allows you to check for legal disconnections being made to attributes of this node."""
    def localShapeInAttr(self) -> MObject:
        """Returns the attribute containing the shape's input geometry in local space."""
    def localShapeOutAttr(self) -> MObject:
        """Returns the attribute containing the shape's output geometry in local space."""
    def match(self, mask: MSelectionMask, componentList: MObjectArray) -> bool:
        """This method is used to check for matches between a selection type (or mask) and a given component. If your shape has components representing attributes then this method is used to match up your components with selection masks."""
    def matchComponent(self, item: MSelectionList, spec: MAttributeSpecArray, list: MSelectionList) -> int:
        """This method is used to convert the string representation of a component into a component object and to validate that the indices."""
    def name(self) -> Any:
        """Returns the name of this particular instance of this class.  Each objectin the dependency graph has a name.  This name will be used by the UIand by MEL."""
    def newControlPointComponent(self) -> MObject:
        """The default action of this method is to return an MFnSingleIndexedComponent (of type MFn::kMeshVertComponent) in order to support rigid skinning binds."""
    def passThroughToMany(self, plug: Any, plugArray: Any) -> bool:
        """This method is overriden by nodes that want to control the traversal behavior of some Maya search algorithms which traverse the history/future of shape nodes looking for directly related nodes. In particular, the Artisan paint code uses this method when searching for paintable nodes, and the disk cache code uses this method when searching for upstream cacheFile nodes."""
    def passThroughToOne(self, plug: Any) -> Any:
        """This method may be overriden by nodes that have a one-to-one relationship between an input attribute and a corresponding output attribute. This method is used by Maya to perform the following capabilities:"""
    def pointAtParm(self, atThisParm: MPoint, evaluatedPoint: MPoint) -> bool:
        """This method is used by Maya in functions (such as select) that require point at parameter values. This only makes sense for parametric surfaces such as NURBS."""
    def postConstructor(self) -> MPxSurfaceShape:
        """Internally maya creates two objects when a user defined node is created, the internal MObject and the user derived object."""
    def postEvaluation(self, context: MDGContext, evalNode: MEvaluationNode, evalType: Any) -> None:
        """Clean up node's internal state after threaded evaluation."""
    def preEvaluation(self, context: MDGContext, evalNode: MEvaluationNode) -> None:
        """Prepare a node's internal state for threaded evaluation."""
    def renderGroupComponentType(self) -> int:
        """This method is used to return the type of renderable components for this shape. It should return a type among MFn::kMeshPolygonComponent, MFn::kSubdivFaceComponent and MFn::kSurfaceFaceComponent, which is used in the creation of per-face/patch shader assignment."""
    def setDependentsDirty(self, plug: MPlug, plugArray: Any) -> MPxSurfaceShape:
        """This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug which Maya is marking dirty. The list of plugs for Maya to mark dirty is returned by the plug array. This method handles both dynamic as well as non-dynamic plugs and is useful in the following ways:"""
    def setDoNotWrite(self, bool: bool) -> MPxSurfaceShape:
        """Use this method to mark the "do not write" state of this proxy node.  If set, this node will not be saved when the Maya model is written out. """
    def setExistWithoutInConnections(self, bool: bool) -> bool:
        """This method specifies whether or not the node can exist without input"""
    def setExistWithoutOutConnections(self, bool: bool) -> bool:
        """This method specifies whether or not the node can exist without"""
    def setExternalContent(self, table: Any) -> MPxSurfaceShape:
        """This is useful in the context of content relocation.  This will be called while the scene is being loaded to apply path changes performed externally. Consequently, interaction with the rest of the scene must be kept to a minimum.  It is however valid to call this method outside of scene loading contexts."""
    def setExternalContentForFileAttr(self, attr: MObject, table: Any) -> bool:
        """This method is a helper for derived clases implementing setExternalContent().  It assigns a value to a plug with the one from the table whose key is the same as the passed in attribute name."""
    def setInternalValue(self, plug: Any, dataHandle: Any) -> bool:
        """This method is overriden by nodes that store attribute data in some internal format."""
    def setInternalValueInContext(self, plug: Any, dataHandle: Any, ctx: Any) -> Any:
        """This method is obsolete. Override MPxNode.setInternalValue instead."""
    def setMPSafe(self, bool: bool) -> MPxSurfaceShape:
        """This method is obsolete. Override MPxNode.setSchedulingType instead."""
    def shouldSave(self, plug: Any) -> Any:
        """This method may be overridden by the user defined node.  It should only be required to override this on rare occasions."""
    def thisMObject(self) -> MObject:
        """Returns the MObject associated with this user defined node.  This makes it possible to use MFnDependencyNode or to construct plugs to this node's attributes."""
    def transformInvalidationRange(self, plug: MPlug, timeRange: MTimeRange) -> float:
        """Override this method to register this node as an Invalidation-Range-Transformation kernel (IRT kernel) An IRT kernel node will change the invalidation time range for its downstream nodes For example, Dynamics-solver will transform invalidation time range [a,b] to [a,+inf) And Clip-Time-Editor will send out the invalidation range for each of the clip [a,b] to ( [t0+a,t0+b] U [t1+a,t1+b] U [t2+a,t2+b] U ... ) """
    def transformUsing(self, matrix: MMatrix, componentList: MObjectArray, cachingMode: Any = None, pointCache: Any = None) -> MPxSurfaceShape:
        """Transform the given components using the specified transformation matrix."""
    def tweakUsing(self, matrix: MMatrix, componentList: MObjectArray, cachingMode: Any, pointCache: Any, handle: Any) -> MPxSurfaceShape:
        """Transform the given components using the specified transformation matrix."""
    def type(self) -> int:
        """Returns the type of node that this is.  This is used to differentiate user defined nodes that are derived off different MPx base classes."""
    def typeId(self) -> MTypeId:
        """Returns the TYPEID of this node."""
    def typeName(self) -> Any:
        """Returns the type name of this node.  The type name identifies the node type to the ASCII file format"""
    def undeleteComponents(self, componentList: MObjectArray, undoInfo: MDoubleArray) -> bool:
        """This method should be overridden if the shape is to support undeletion of components. A list of components to be deleted will be passed in as well as an array of doubles where information about each deleted component is stored for undo purposes. A typical use for this array is to store knot values or weights for control points that are deleted."""
    def vertexOffsetDirection(self, component: MObject, direction: MVectorArray, mode: Any, normalize: bool) -> bool:
        """This method should be overridden if the shape supports components that can be moved in the direction of the normal or UV's using the move vertex normal tool."""
    def weightedTransformUsing(self, xform: MTransformationMatrix, space: MMatrix, componentList: MObjectArray, cachingMode: Any, pointCache: MPlane, freezePlane: Any) -> MPxSurfaceShape:
        """Transform the given components with interpolation using the specified transformation matrix."""
    def weightedTweakUsing(self, xform: MTransformationMatrix, space: MMatrix, componentList: MObjectArray, cachingMode: Any, pointCache: MPlane, freezePlane: Any, handle: Any) -> MPxSurfaceShape:
        """Transform the given components with interpolation using the specified transformation matrix."""
    def worldShapeOutAttr(self) -> MObject:
        """Returns the attribute containing the shape's output geometry in world space."""

class MQuaternion:
    kIdentity: Any
    kTolerance: Any
    w: Any
    x: Any
    y: Any
    z: Any
    def __init__(self, src: MQuaternion | float | MVector | None = None, yy: float | MVector | None = None, zz: float | None = None, ww: float | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def asAxisAngle(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the rotation as a tuple containing an axis vector and an angle in radians about that axis."""
    def asEulerRotation(self) -> MEulerRotation:
        """Returns the rotation as an equivalent MEulerRotation."""
    def asMatrix(self) -> MMatrix:
        """Returns the rotation as an equivalent rotation matrix."""
    def conjugate(self) -> MQuaternion:
        """Returns the conjugate of this quaternion (i.e. x, y and z components negated)."""
    def conjugateIt(self) -> MQuaternion:
        """In-place conjugation (i.e. negates the x, y and z components)."""
    def exp(self) -> MQuaternion:
        """Returns a new quaternion containing the exponent of this one."""
    def inverse(self) -> MQuaternion:
        """Returns a new quaternion containing the inverse of this one."""
    def invertIt(self) -> MQuaternion:
        """In-place inversion."""
    def isEquivalent(self, other: MQuaternion, tolerance: float | None = None) -> bool:
        """Returns True if the distance between the two quaternions (in quaternion space) is less than or equal to the given tolerance."""
    def log(self) -> MQuaternion:
        """Returns a new quaternion containing the natural log of this one."""
    def negateIt(self) -> MQuaternion:
        """In-place negation of the x, y, z and w components."""
    def normal(self) -> MQuaternion:
        """Returns a new quaternion containing the normalized version of this one (i.e. scaled to unit length)."""
    def normalizeIt(self) -> MQuaternion:
        """In-place normalization (i.e. scales the quaternion to unit length)."""
    def setToXAxis(self, theta: float) -> MQuaternion:
        """Set this quaternion to be equivalent to a rotation of a given angle, in radians, about the X-axis."""
    def setToYAxis(self, theta: float) -> MQuaternion:
        """Set this quaternion to be equivalent to a rotation of a given angle, in radians, about the Y-axis."""
    def setToZAxis(self, theta: float) -> MQuaternion:
        """Set this quaternion to be equivalent to a rotation of a given angle, in radians, about the Z-axis."""
    def setValue(self, *args: Any, **kwargs: Any) -> Any:
        """Set the value of this quaternion to that of the specified MQuaternion, MEulerRotation, MMatrix or MVector and angle."""
    @staticmethod
    def slerp(p: MQuaternion, q: MQuaternion, t: float, spin: Any) -> Any:
        """Returns the quaternion at a given interpolation value along the shortest path between two quaternions."""
    @staticmethod
    def squad(p: MQuaternion, a: MQuaternion, b: MQuaternion, q: MQuaternion, t: float, spin: Any) -> Any:
        """Returns the quaternion at a given interpolation value along a cubic curve segment in quaternion space."""
    @staticmethod
    def squadPt(q0: MQuaternion, q1: MQuaternion, q2: MQuaternion) -> Any:
        """Returns a new quaternion representing an intermediate point which when used with squad() will produce a C1 continuous spline."""

class MRampAttribute:
    isColorRamp: Any
    isCurveRamp: Any
    kLinear: Any
    kNone: Any
    kSmooth: Any
    kSpline: Any
    def __init__(self, other: MRampAttribute | MPlug | MObject | None = None, attr: MObject | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addEntries(self) -> Any:
        """Adds entries to the ramp."""
    @staticmethod
    def createColorRamp(attrLongName: Any, attrShortName: Any) -> MObject:
        """Creates and returns a new color ramp attribute."""
    @staticmethod
    def createCurveRamp(attrLongName: Any, attrShortName: Any) -> MObject:
        """Creates and returns a new curve ramp attribute."""
    @staticmethod
    def createRamp(attrLongName: Any, attrShortName: Any, node: MObject, val: float | MColor | MFloatArray | MColorArray, pos: float | MFloatArray | None = None, interp: Any = None) -> MObject:
        """Creates and returns a new color or curve ramp attribute initialized with values."""
    def deleteEntries(self) -> MIntArray:
        """Removes from the ramp those entries with the specified indices."""
    def getEntries(self) -> Any:
        """Returns a tuple containing all of the entries in the ramp."""
    def getValueAtPosition(self, position: float) -> float:
        """Returns the value of the entry at the given position."""
    def hasIndex(self, index: int) -> bool:
        """Return true if an entry is defined at this index."""
    def numEntries(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the number of entries in the ramp."""
    def pack(self) -> None:
        """Change the indices numbering by re-ordering them from 0."""
    def setInterpolationAtIndex(self, interp: int, index: int) -> None:
        """Sets the interpolation of the entry at the given index."""
    def setPositionAtIndex(self, position: float, index: int) -> None:
        """Sets the position of the entry at the given index."""
    def setRamp(self, value: float | MColor | MFloatArray | MColorArray, position: float | MFloatArray | None = None, interp: Any = None) -> None:
        """Set this ramp with one or multiple entries. Current entries are removed before adding the new one(s)."""
    def setValueAtIndex(self, value: float, index: int) -> None:
        """Sets the value of the entry at the given index."""
    def sort(self, ascending: bool | None = None) -> None:
        """Sort the ramp by position. Indices are also re-ordered during sort."""

class MRichSelection:
    def __init__(self, src: MRichSelection | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def clear(self) -> MRichSelection:
        """Empties the rich selection."""
    def getRawSymmetryMatrix(self, arg: Any, space: Any) -> Any:
        """Returns a tuple containing the raw symmetry matrix to use for the"""
    def getSelection(self) -> MSelectionList:
        """Returns a copy of the non-symmetry component of the rich selection."""
    def getSymmetry(self) -> MSelectionList:
        """Returns a copy of the symmetry component of the rich selection."""
    def getSymmetryMatrix(self, MDagPath: MDagPath, space: int) -> MMatrix:
        """Returns the symmetry matrix to use for the symmetric component of"""
    def getSymmetryPlane(self, MDagPath: MDagPath, space: int) -> MPlane:
        """Returns the plane of symmetry, in the specified transformation space"""
    def setSelection(self, MSelectionList: MSelectionList) -> MRichSelection:
        """Sets the non-symmetry component of the rich selection."""

class MSceneMessage:
    kAfterCreateReference: Any
    kAfterCreateReferenceAndRecordEdits: Any
    kAfterExport: Any
    kAfterExportReference: Any
    kAfterFileRead: Any
    kAfterImport: Any
    kAfterImportReference: Any
    kAfterLoadReference: Any
    kAfterLoadReferenceAndRecordEdits: Any
    kAfterNew: Any
    kAfterOpen: Any
    kAfterPluginLoad: Any
    kAfterPluginUnload: Any
    kAfterReference: Any
    kAfterRemoveReference: Any
    kAfterSave: Any
    kAfterSceneReadAndRecordEdits: Any
    kAfterSoftwareFrameRender: Any
    kAfterSoftwareRender: Any
    kAfterUnloadReference: Any
    kBeforeCreateReference: Any
    kBeforeCreateReferenceAndRecordEdits: Any
    kBeforeCreateReferenceCheck: Any
    kBeforeExport: Any
    kBeforeExportCheck: Any
    kBeforeExportReference: Any
    kBeforeFileRead: Any
    kBeforeImport: Any
    kBeforeImportCheck: Any
    kBeforeImportReference: Any
    kBeforeLoadReference: Any
    kBeforeLoadReferenceAndRecordEdits: Any
    kBeforeLoadReferenceCheck: Any
    kBeforeNew: Any
    kBeforeNewCheck: Any
    kBeforeOpen: Any
    kBeforeOpenCheck: Any
    kBeforePluginLoad: Any
    kBeforePluginUnload: Any
    kBeforeReference: Any
    kBeforeReferenceCheck: Any
    kBeforeRemoveReference: Any
    kBeforeSave: Any
    kBeforeSaveCheck: Any
    kBeforeSoftwareFrameRender: Any
    kBeforeSoftwareRender: Any
    kBeforeUnloadReference: Any
    kDefaultAction: Any
    kDoAction: Any
    kDoNotDoAction: Any
    kExportStarted: Any
    kLast: Any
    kMayaExiting: Any
    kMayaInitialized: Any
    kSceneUpdate: Any
    kSoftwareRenderInterrupted: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def addCallback(message: Any, function: Any, clientData: None = None) -> int:
        """Adds a new callback for the specified scene message."""
    @staticmethod
    def addCheckCallback(message: Any, function: int, clientData: None = None) -> int:
        """This function adds a new callback for the specified scene message."""
    @staticmethod
    def addCheckFileCallback(message: Any, function: int, clientData: None = None) -> int:
        """This function adds a new callback for the specified scene message. This"""
    @staticmethod
    def addCheckReferenceCallback(message: Any, function: int, clientData: None = None) -> int:
        """This function adds a new callback for the specified scene message."""
    @staticmethod
    def addConnectionFailedCallback(function: int, clientData: None = None) -> int:
        """This method registers a callback that is called when a connection was"""
    @staticmethod
    def addNamespaceRenamedCallback(function: int, clientData: None = None) -> int:
        """This method registers a callback that is called when a namespace is renamed."""
    @staticmethod
    def addReferenceCallback(message: Any, function: int, clientData: None = None) -> int:
        """This function adds a new callback for the specified scene message."""
    @staticmethod
    def addStringArrayCallback(message: Any, function: int, clientData: None = None) -> int:
        """Adds a new callback which takes a string array argument, in addition to"""
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

class MSelectionList:
    kMergeNormal: Any
    kRemoveFromList: Any
    kXORWithList: Any
    def __init__(self, src: MSelectionList | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def add(self, pattern: Any, searchChildNamespaces: bool = False) -> MSelectionList:
        """add(item, mergeWithExisting=True) -> self"""
    def clear(self) -> MSelectionList:
        """Empties the selection list."""
    def copy(self, src: Any) -> MSelectionList:
        """Replaces the contents of the selection list with a copy of those from src (MSelectionList)."""
    def getComponent(self, arg: Any, MObject: Any) -> Any:
        """Returns the index'th item of the list as a component, represented by"""
    def getDagPath(self, index: int) -> MDagPath:
        """Returns the DAG path associated with the index'th item of the list."""
    def getDependNode(self, index: int) -> MObject:
        """Returns the node associated with the index'th item, whether it be a"""
    def getPlug(self, index: int) -> MPlug:
        """Returns the index'th item of the list as a plug. Raises TypeError if"""
    def getSelectionStrings(self, index: int, string: Any, arg: Any) -> Any:
        """Returns a tuple containing the string representation of the"""
    def hasItem(self, item: Any) -> bool:
        """Returns True if the given item is on the selection list. For a"""
    def hasItemPartly(self, dagPath: MDagPath, component: MObject) -> bool:
        """Returns True if at least one of the component's elements is on the"""
    def intersect(self, other: MSelectionList, expandToLeaves: bool = False) -> MSelectionList:
        """Modify this list to contain the intersection of itself and the given list."""
    def isEmpty(self) -> bool:
        """Returns True if the selection list is empty."""
    def length(self) -> int:
        """Returns the number of items on the selection list."""
    def merge(self, other: MSelectionList, strategy: int | None = None) -> MSelectionList:
        """merge(dagPath, component, strategy=kMergeNormal) -> self"""
    def remove(self, index: int) -> MSelectionList:
        """Removes the index'th item from the list. Raises IndexError if the"""
    def replace(self, index: int, newItem: MObject | MDagPath | MPlug) -> MSelectionList:
        """Replaces the index'th item on the list with a new item. A component"""
    def toggle(self, dagPath: MDagPath, component: MObject) -> MSelectionList:
        """Removes from the list those elements of the given component which"""

class MSelectionMask:
    kSelectAnimAny: Any
    kSelectAnimCurves: Any
    kSelectAnimInTangents: Any
    kSelectAnimKeyframes: Any
    kSelectAnimMask: Any
    kSelectAnimOutTangents: Any
    kSelectCVs: Any
    kSelectCameras: Any
    kSelectClusters: Any
    kSelectCollisionModels: Any
    kSelectComponentsMask: Any
    kSelectCurveKnots: Any
    kSelectCurveParmPoints: Any
    kSelectCurves: Any
    kSelectCurvesOnSurfaces: Any
    kSelectDynamicConstraints: Any
    kSelectEdges: Any
    kSelectEditPoints: Any
    kSelectEmitters: Any
    kSelectFacets: Any
    kSelectFields: Any
    kSelectFluids: Any
    kSelectFollicles: Any
    kSelectGuideLines: Any
    kSelectHairSystems: Any
    kSelectHandles: Any
    kSelectHulls: Any
    kSelectIkEndEffectors: Any
    kSelectIkHandles: Any
    kSelectIsoparms: Any
    kSelectJointPivots: Any
    kSelectJoints: Any
    kSelectLatticePoints: Any
    kSelectLattices: Any
    kSelectLights: Any
    kSelectLocalAxis: Any
    kSelectLocators: Any
    kSelectManipulators: Any
    kSelectMeshComponents: Any
    kSelectMeshEdges: Any
    kSelectMeshFaces: Any
    kSelectMeshFreeEdges: Any
    kSelectMeshLines: Any
    kSelectMeshUVs: Any
    kSelectMeshVerts: Any
    kSelectMeshes: Any
    kSelectNCloths: Any
    kSelectNParticles: Any
    kSelectNRigids: Any
    kSelectNurbsCurves: Any
    kSelectNurbsSurfaces: Any
    kSelectObjectGroups: Any
    kSelectObjectsMask: Any
    kSelectOrientationLocators: Any
    kSelectPPStrokes: Any
    kSelectParticleShapes: Any
    kSelectParticles: Any
    kSelectPivots: Any
    kSelectPointsForGravity: Any
    kSelectPointsOnCurvesForGravity: Any
    kSelectPointsOnSurfacesForGravity: Any
    kSelectRigidBodies: Any
    kSelectRigidConstraints: Any
    kSelectRotatePivots: Any
    kSelectScalePivots: Any
    kSelectSculpts: Any
    kSelectSelectHandles: Any
    kSelectSketchPlanes: Any
    kSelectSprings: Any
    kSelectSubdiv: Any
    kSelectSubdivMeshEdges: Any
    kSelectSubdivMeshFaces: Any
    kSelectSubdivMeshMaps: Any
    kSelectSubdivMeshPoints: Any
    kSelectSurfaceEdge: Any
    kSelectSurfaceKnots: Any
    kSelectSurfaceParmPoints: Any
    kSelectSurfaceRange: Any
    kSelectSurfaces: Any
    kSelectTemplates: Any
    kSelectTextures: Any
    kSelectUVLocators: Any
    kSelectVertices: Any
    kSelectXYZLocators: Any
    def __init__(self, selType: Any = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addMask(self, selType: Any) -> MSelectionMask:
        """Add the specified selection type to this mask."""
    def copy(self, source: Any) -> MSelectionMask:
        """Copy data from source selection mask."""
    @staticmethod
    def deregisterSelectionType(selTypeName: Any) -> bool:
        """Unregisters a previously registered selection type."""
    @staticmethod
    def getSelectionTypePriority(selTypeName: Any) -> int:
        """Gets the selection priority corresponding to a given selection type."""
    def intersects(self, mask: Any) -> bool:
        """intersects(selType) -> bool"""
    @staticmethod
    def registerSelectionType(selTypeName: Any, priority: int = 0) -> bool:
        """Registers a new selection type. It is perfectly legal for 2 plug-ins to register the same selection type."""
    def setMask(self, mask: Any) -> MSelectionMask:
        """setMask(selType) -> self"""

class MSpace:
    kInvalid: Any
    kLast: Any
    kObject: Any
    kPostTransform: Any
    kPreTransform: Any
    kTransform: Any
    kWorld: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MSyntax:
    enableEdit: Any
    enableQuery: Any
    kAngle: Any
    kBoolean: Any
    kDistance: Any
    kDouble: Any
    kInvalidArgType: Any
    kInvalidObjectFormat: Any
    kLastArgType: Any
    kLastObjectFormat: Any
    kLong: Any
    kNoArg: Any
    kNone: Any
    kSelectionItem: Any
    kSelectionList: Any
    kString: Any
    kStringObjects: Any
    kTime: Any
    kUnsigned: Any
    def __init__(self, other: MSyntax | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addArg(self, arg: Any) -> None:
        """Add a command argument."""
    def addFlag(self, shortName: Any, longName: Any, argType1: Any = None, argType2: Any = None, argType3: Any = None, argType4: Any = None, argType5: Any = None, argType6: Any = None) -> None:
        """Add a flag and its arguments."""
    def makeFlagMultiUse(self, flag: Any) -> None:
        """Set whether a flag may be used multiple times on the command line."""
    def makeFlagQueryWithFullArgs(self, flag: Any, queryArgsAreOptional: bool) -> None:
        """Set whether a flag requires its args when queried."""
    def maxObjects(self) -> int:
        """Returns the maximum number of objects which can be passed to the command."""
    def minObjects(self) -> int:
        """Returns the minimum number of objects which can be passed to the command."""
    def setMaxObjects(self, maximumObjectCount: int) -> None:
        """Sets the maximum number of objects which can be passed to the command."""
    def setMinObjects(self, minimumObjectCount: int) -> None:
        """Sets the minimum number of objects which can be passed to the command."""
    def setObjectType(self, objectFormat: Any, maximumObjects: int, minimumObjects: int | None = None) -> None:
        """Set the type and number of objects to be passed to the command."""
    def useSelectionAsDefault(self, useSelectionList: bool | None = None) -> None:
        """If set to True then when no objects are provided on the command-line Maya will pass the current selection instead."""

class MTime:
    k100FPS: Any
    k10FPS: Any
    k119_88FPS: Any
    k1200FPS: Any
    k120FPS: Any
    k125FPS: Any
    k12FPS: Any
    k1500FPS: Any
    k150FPS: Any
    k15FPS: Any
    k16FPS: Any
    k2000FPS: Any
    k200FPS: Any
    k20FPS: Any
    k23_976FPS: Any
    k240FPS: Any
    k24FPS: Any
    k250FPS: Any
    k25FPS: Any
    k29_97DF: Any
    k29_97FPS: Any
    k2FPS: Any
    k3000FPS: Any
    k300FPS: Any
    k30FPS: Any
    k375FPS: Any
    k3FPS: Any
    k400FPS: Any
    k40FPS: Any
    k44100FPS: Any
    k47_952FPS: Any
    k48000FPS: Any
    k48FPS: Any
    k4FPS: Any
    k500FPS: Any
    k50FPS: Any
    k59_94FPS: Any
    k5FPS: Any
    k6000FPS: Any
    k600FPS: Any
    k60FPS: Any
    k6FPS: Any
    k750FPS: Any
    k75FPS: Any
    k80FPS: Any
    k8FPS: Any
    k90FPS: Any
    kFilm: Any
    kGames: Any
    kHours: Any
    kInvalid: Any
    kLast: Any
    kMilliseconds: Any
    kMinutes: Any
    kNTSCField: Any
    kNTSCFrame: Any
    kPALField: Any
    kPALFrame: Any
    kSeconds: Any
    kShowScan: Any
    kUserDef: Any
    unit: Any
    value: Any
    def __init__(self, time_val: float | None = None, Unit: Any = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def asUnits(self, unit: int) -> float:
        """Return the time value, converted to the specified units."""
    @staticmethod
    def setUIUnit(new_unit: Any) -> None:
        """Change the units used to display time in Maya's UI."""
    @staticmethod
    def ticksPerSecond() -> Any:
        """Returns the number of ticks per second, the smallest unit of time available."""
    @staticmethod
    def uiUnit() -> Any:
        """Return the units used to display time in Maya's UI."""

class MTimeArray:
    sizeIncrement: Any
    def __init__(self, other: MTimeArray | int | None = None, initialValue: MTime | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def append(self, element: MTime) -> None:
        """Add a value to the end of the array."""
    def clear(self) -> None:
        """Remove all elements from the array."""
    def copy(self, source: MTimeArray) -> None:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self, element: MTime, index: int) -> None:
        """Insert a new value into the array at the given index."""
    def remove(self, index: int) -> None:
        """Remove an element from the array."""
    def setLength(self, length: int) -> None:
        """Grow or shrink the array to contain a specific number of elements."""

class MTimeRange:
    def __init__(self, MTime: Any = None, MTime_: Any = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def contains(self, arg: Any, MTime: Any) -> bool:
        """Checks if the given time point or interval is contained in this time range."""
    def empty(self) -> bool:
        """Checks if this time range is an empty set"""
    def intersects(self, MTime: Any, MTime_: Any) -> bool:
        """Checks if the given interval intersects with this time range."""

class MTimerMessage:
    kDefaultAction: Any
    kDoAction: Any
    kDoNotDoAction: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def addTimerCallback(period: float, function: int, clientData: None = None) -> int:
        """This method registers a callback which is called repeatedly with a"""
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

class MTransformationMatrix:
    kIdentity: Any
    kInvalid: Any
    kLast: Any
    kTolerance: Any
    kXYZ: Any
    kXZY: Any
    kYXZ: Any
    kYZX: Any
    kZXY: Any
    kZYX: Any
    def __init__(self, src: MTransformationMatrix | MMatrix | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def asMatrix(self, percent: float | None = None) -> MMatrix:
        """Interpolates between the identity transformation and that currently in the object, returning the result as an MMatrix."""
    def asMatrixInverse(self) -> MMatrix:
        """Returns the inverse of the matrix representing the transformation."""
    def asRotateMatrix(self) -> MMatrix:
        """Returns the matrix which takes points from object space to the space immediately following the scale/shear/rotation transformations."""
    def asScaleMatrix(self) -> MMatrix:
        """Returns the matrix which takes points from object space to the space immediately following scale and shear transformations."""
    def isEquivalent(self, other: MTransformationMatrix, tolerance: float = 1e-10) -> bool:
        """Returns true if this transformation's matrix is within tolerance of another's matrix."""
    def reorderRotation(self, order: Any) -> None:
        """Reorders the transformation's rotate component to give the same overall rotation but using a new order or rotations."""
    def rotateBy(self, q: MQuaternion | MEulerRotation, space: int) -> MTransformationMatrix:
        """Adds to the transformation's rotation component."""
    def rotateByComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Adds to the transformation's rotation component."""
    def rotatePivot(self, Space: int) -> MPoint:
        """Returns the transformation's rotate pivot component."""
    def rotatePivotTranslation(self, space: int) -> MVector:
        """Returns the transformation's rotate pivot translation component."""
    def rotation(self, space: int | None = None) -> MEulerRotation:
        """Returns the transformation's rotation component as either an Euler rotation or a quaternion."""
    def rotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the four components of the transformation's rotate component."""
    def rotationOrder(self) -> Any:
        """Returns the order of rotations when the transformation's rotate component is expressed as an euler rotation."""
    def rotationOrientation(self) -> MQuaternion:
        """Returns a quaternion which orients the local rotation space."""
    def scale(self, space: int | None = None) -> list[float]:
        """Returns a list containing the transformation's scale components."""
    def scaleBy(self, *args: Any, **kwargs: Any) -> Any:
        """Multiplies the transformation's scale components by the three floats in the provided sequence."""
    def scalePivot(self, Space: int) -> MPoint:
        """Returns the transformation's scale pivot component."""
    def scalePivotTranslation(self, Space: int) -> MVector:
        """Returns the transformation's scale pivot translation component."""
    def setRotatePivot(self, point: MPoint, Space: int, balance: bool) -> None:
        """Sets the transformation's rotate pivot component."""
    def setRotatePivotTranslation(self, vector: MVector, space: int) -> None:
        """Sets the transformation's rotate pivot translation component."""
    def setRotation(self, rot: MEulerRotation, space: int | None = None) -> None:
        """Sets the transformation's rotation component."""
    def setRotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transformation's rotate component from the four values in the provided sequence."""
    def setRotationOrientation(self, q: MQuaternion) -> MTransformationMatrix:
        """Sets a quaternion which orients the local rotation space."""
    def setScale(self, vec: MVector, space: int | None = None) -> None:
        """Sets the transformation's scale components to the three floats in the provided sequence."""
    def setScalePivot(self, Space: int, balance: bool) -> None:
        """Sets the transformation's scale pivot component."""
    def setScalePivotTranslation(self, vector: MVector, Space: int) -> None:
        """Sets the transformation's scale pivot translation component."""
    def setShear(self, space: int) -> None:
        """Sets the transformation's shear component."""
    def setToRotationAxis(self, axis: MVector, rotation: float) -> None:
        """Sets the transformation's rotate component to be a given axis vector and angle in radians."""
    def setTranslation(self, vec: MVector, space: int | None = None) -> None:
        """Sets the transformation's translation component."""
    def shear(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transformation's shear components."""
    def shearBy(self, *args: Any, **kwargs: Any) -> Any:
        """Multiplies the transformation's shear components by the three floats in the provided sequence."""
    def translateBy(self, *args: Any, **kwargs: Any) -> Any:
        """Adds a vector to the transformation's translation component."""
    def translation(self, space: int | None = None) -> MVector:
        """Returns the transformation's translation component as a vector."""

class MTypeId:
    def __init__(self, id: int | MTypeId | None = None, id_: int | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def id(self) -> int:
        """Returns the type id as a long."""

class MURI:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addQueryItem(self, key: Any, value: Any) -> MURI:
        """Add a key/value pair to the query string of the URI."""
    def asString(self) -> Any:
        """Returns the string representation of the URI."""
    def clear(self) -> MURI:
        """Clears the contents of the MURI object."""
    def copy(self, source: Any) -> MURI:
        """Copy method. Assigns the value of one MURI to another."""
    def getAllQueryItemKeys(self) -> Any:
        """Returns an array containing the keys from all query string pairs."""
    def getAllQueryItemValues(self, key: Any) -> Any:
        """Returns an array containing the values from all query string pairs which have a given key."""
    def getAuthority(self) -> Any:
        """Returns the authority component of the URI."""
    def getDirectory(self) -> Any:
        """Returns just the file directory portion of the URI, without the file name."""
    def getFileName(self, arg: Any) -> Any:
        """Returns just the file name portion of the URI, with or without the extension."""
    def getFragment(self) -> Any:
        """Returns the fragment component of the URI."""
    def getHost(self) -> Any:
        """Returns the host component of the URI."""
    def getPassword(self) -> Any:
        """Returns the password component of the URI."""
    def getPath(self) -> Any:
        """Returns the path component of the URI."""
    def getPort(self) -> int:
        """Returns the port component of the URI, or -1 if the port is not defined."""
    def getQueryItemValue(self, key: Any) -> Any:
        """Returns the value from the first query string pair in the URI which has a given key."""
    def getQueryPairDelimiter(self) -> Any:
        """Returns the character used to delimit between key-value pairs in the query string of the URI."""
    def getQueryValueDelimiter(self) -> Any:
        """Returns the character used to delimit keys and values in the query string of the URI."""
    def getScheme(self) -> Any:
        """Returns the scheme of the URI."""
    def getUserInfo(self) -> Any:
        """Returns the user info component of the URI."""
    def getUserName(self) -> Any:
        """Returns the user name component of the URI."""
    def isEmpty(self) -> bool:
        """Determines if the URI does not contain any data."""
    def isValid(self) -> bool:
        """Determines if the URI is valid."""
    @staticmethod
    def isValidURI(uri: Any) -> bool:
        """Determines if a string value represents a valid URI."""
    def removeAllQueryItems(self, int: Any) -> MURI:
        """Removes all query string pairs having a given key from the URI."""
    def removeQueryItem(self, int: Any) -> MURI:
        """Removes the first query string pair with a given key from the URI."""
    def setAuthority(self, string: Any) -> MURI:
        """Set the authority portion of the URI."""
    def setDirectory(self, string: Any) -> MURI:
        """Sets just the directory portion of the URI (i.e. not including the filename)."""
    def setFileName(self, string: Any) -> MURI:
        """Sets just the filename portion of the URI (i.e. not including the directory)."""
    def setFragment(self, string: Any) -> MURI:
        """Sets the fragment component of the URI."""
    def setHost(self, string: Any) -> MURI:
        """Set the host component of the URI."""
    def setPassword(self, string: Any) -> MURI:
        """Sets the password part of the user info component."""
    def setPath(self, string: Any) -> MURI:
        """Sets the path component of the URI."""
    def setPort(self, int: Any) -> MURI:
        """Set the port component of the URI."""
    def setQueryDelimiters(self, valueDelimiter: Any, pairDelimiter: Any) -> MURI:
        """Sets the delimiter characters used in the query string of the URI."""
    def setScheme(self, string: Any) -> MURI:
        """Sets the scheme component of the URI."""
    def setURI(self, uri: Any) -> MURI:
        """Initialize the MURI from a string value."""
    def setUserInfo(self, string: Any) -> MURI:
        """Decomposes the userInfo string to fill out the userInfo-related component values."""
    def setUserName(self, string: Any) -> MURI:
        """Sets the user name part of the user info component."""

class MUint64Array:
    sizeIncrement: Any
    def __init__(self, other: MUint64Array | int | None = None, initialValue: Any = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def append(self, element: Any) -> None:
        """Add a value to the end of the array."""
    def clear(self) -> None:
        """Remove all elements from the array."""
    def copy(self, source: MUint64Array) -> None:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self, element: Any, index: int) -> None:
        """Insert a new value into the array at the given index."""
    def remove(self, index: int) -> None:
        """Remove an element from the array."""
    def setLength(self, length: int) -> None:
        """Grow or shrink the array to contain a specific number of elements."""

class MUintArray:
    sizeIncrement: Any
    def __init__(self, other: MUintArray | int | None = None, initialValue: int | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def append(self, element: int) -> None:
        """Add a value to the end of the array."""
    def clear(self) -> None:
        """Remove all elements from the array."""
    def copy(self, source: MUintArray) -> None:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self, element: int, index: int) -> None:
        """Insert a new value into the array at the given index."""
    def remove(self, index: int) -> None:
        """Remove an element from the array."""
    def setLength(self, length: int) -> None:
        """Grow or shrink the array to contain a specific number of elements."""

class MUserData:
    def __init__(self, deleteAfterUse: bool | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def deleteAfterUse(self) -> bool:
        """Returns whether or not this user data should be deleted immediately after use instead of being"""
    def setDeleteAfterUse(self, bool: bool) -> MUserData:
        """Sets whether or not this user data should be deleted immediately after use instead of being"""

class MUserEventMessage:
    kDefaultAction: Any
    kDoAction: Any
    kDoNotDoAction: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def addUserEventCallback(eventName: Any, function: int, clientData: None = None) -> int:
        """This method registers a callback for user-defined messages."""
    @staticmethod
    def currentCallbackId() -> int:
        """Returns the callback ID of the currently executing callback. If called"""
    @staticmethod
    def deregisterUserEvent(eventName: Any) -> Any:
        """Removes the event type with the given event name.  If callbacks have been"""
    @staticmethod
    def isUserEvent(eventName: Any) -> bool:
        """Checks if an event type exists with the given event name."""
    @staticmethod
    def nodeCallbacks(node: Any) -> int:
        """Returns a list of callback IDs registered to a given node."""
    @staticmethod
    def postUserEvent(eventName: Any, clientData: Any = None) -> Any:
        """Notifies all callbacks attached to the given event type of the occurence"""
    @staticmethod
    def registerUserEvent(eventName: Any) -> Any:
        """Adds a new event type with the given string identifier.  The string"""
    @staticmethod
    def removeCallback(id: Any) -> None:
        """Removes the specified callback from Maya."""
    @staticmethod
    def removeCallbacks(ids: Any) -> None:
        """Removes all of the specified callbacks from Maya."""

class MUuid:
    def __init__(self, other: Any = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def asString(self) -> Any:
        """Return the UUID as a string."""
    def copy(self, source: MUuid) -> MUuid:
        """Copy method. Assigns the value of one MUuid to another."""
    def generate(self) -> MUuid:
        """Generate a new UUID."""
    def valid(self) -> bool:
        """Return whether the UUID is valid."""

class MVector:
    kOneVector: Any
    kTolerance: Any
    kWaxis: Any
    kXaxis: Any
    kXaxisVector: Any
    kXnegAxisVector: Any
    kYaxis: Any
    kYaxisVector: Any
    kYnegAxisVector: Any
    kZaxis: Any
    kZaxisVector: Any
    kZeroVector: Any
    kZnegAxisVector: Any
    x: float
    y: float
    z: float
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def angle(self, other: MVector) -> float:
        """Returns the angle, in radians, between this vector and another."""
    def isEquivalent(self, other: MVector, tolerance: float = 1e-10) -> bool:
        """Returns True if this vector and another are within a given tolerance of being equal."""
    def isParallel(self, other: MVector, tolerance: float | None = None) -> bool:
        """Returns True if this vector and another are within the given tolerance of being parallel."""
    def length(self) -> float:
        """Returns the magnitude of this vector."""
    def normal(self) -> MVector:
        """Returns a new vector containing the normalized version of this one."""
    def normalize(self) -> MVector:
        """Normalizes this vector in-place and returns a new reference to it."""
    def rotateBy(self, x: float | int | None = None, y: float | None = None, z: float | None = None, w: float | None = None) -> MVector:
        """Returns the vector resulting from rotating this one by the given amount."""
    def rotateTo(self) -> MQuaternion:
        """Returns the quaternion which will rotate this vector into another."""
    def transformAsNormal(self, matrix: MMatrix) -> MVector:
        """Returns a new vector which is calculated by postmultiplying this vector by the transpose of the given matrix's inverse and then normalizing the result."""

class MVectorArray:
    sizeIncrement: Any
    def __init__(self, other: MVectorArray | int | None = None, initialValue: MVector | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def append(self, element: MVector) -> None:
        """Add a value to the end of the array."""
    def clear(self) -> None:
        """Remove all elements from the array."""
    def copy(self, source: MVectorArray) -> None:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self, element: MVector, index: int) -> None:
        """Insert a new value into the array at the given index."""
    def remove(self, index: int) -> None:
        """Remove an element from the array."""
    def setLength(self, length: int) -> None:
        """Grow or shrink the array to contain a specific number of elements."""

class MWeight:
    influence: Any
    seam: Any
    def __init__(self, src: MWeight | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""