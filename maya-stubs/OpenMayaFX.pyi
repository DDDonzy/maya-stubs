# Stub for maya.OpenMayaFX - OM1, signatures from Maya 2024 C++ API reference
from typing import Any, overload

from maya.OpenMaya import MCallbackIdArray
from maya.OpenMaya import MColor
from maya.OpenMaya import MDagPath
from maya.OpenMaya import MDagPathArray
from maya.OpenMaya import MDoubleArray
from maya.OpenMayaMPx import MExternalContentInfoTable
from maya.OpenMayaMPx import MExternalContentLocationTable
from maya.OpenMaya import MFloatArray
from maya.OpenMaya import MFloatPointArray
from maya.OpenMaya import MIntArray
from maya.OpenMaya import MMatrix
from maya.OpenMaya import MMatrixArray
from maya.OpenMaya import MObject
from maya.OpenMaya import MObjectArray
from maya.OpenMaya import MPlug
from maya.OpenMaya import MPlugArray
from maya.OpenMaya import MPoint
from maya.OpenMaya import MPointArray
from maya.OpenMaya import MTime
from maya.OpenMaya import MTypeId
from maya.OpenMaya import MUuid
from maya.OpenMaya import MVector
from maya.OpenMaya import MVectorArray

class MStatus:
    ...

class MDynSweptLine:
    thisown: Any
    def __init__(self) -> None:
        """The class constructor."""
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def length(self, t: float = 1.0) -> float:
        """Given a parametric time specified by 't', returns the total length of the line."""
    def normal(self, x: float, y: float, z: float, t: float = 1.0) -> MVector:
        """Given a parametric time specified by 't' and a vector, returns a normalized vector perpendicular to the tangent, and rot"""
    def tangent(self, t: float = 1.0) -> MVector:
        """Given a parametric time specified by 't', returns normalized tangent of the line."""
    def vertex(self, vertexId: int, t: float = 1.0) -> MVector:
        """Return the vertex requested by id, at the parametric time value."""

class MDynSweptTriangle:
    thisown: Any
    def __init__(self) -> None:
        """The class constructor."""
    def area(self) -> float:
        """This method returns the area."""
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def normal(self, t: float = 1.0) -> MVector:
        """Given a parametric time specified by 't', returns the normal of the triangle."""
    def normalToPoint(self, x: float, y: float, z: float, t: float = 1.0) -> MVector:
        """Given a point, returns the normal of the triangle in the direction towards the point."""
    def uvPoint(self, vertexId: int) -> MVector:
        """Given a vertex id, this method returns the UV point for the vertex as a MVector ."""
    def vertex(self, vertexId: int, t: float = 1.0) -> MVector:
        """Return the vertex requested by id, at the parametric time value."""

class MDynamicsUtil:
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @staticmethod
    def addNodeTypeToRunup(nodeTypeName: str) -> bool:
        """Add this node to the list of nodes participating in runup."""
    @staticmethod
    def evalDynamics2dTexture(node: MObject, texAttr: MObject, uCoords: MDoubleArray, vCoords: MDoubleArray, resultColors: MVectorArray, resultAlphas: MDoubleArray) -> MStatus:
        """If a supported 2d texture (see hasValidDynamics2dTexture() method documentation) is connected to the specified attribute"""
    @staticmethod
    def hasValidDynamics2dTexture(node: MObject, texAttr: MObject) -> bool:
        """Certain aspects of Maya's dynamics can be textured using 2d textures."""
    @staticmethod
    def inRunup() -> bool:
        """Is Maya's dynamics system currently doing a runup?"""
    @staticmethod
    def removeNodeTypeFromRunup(nodeTypeName: str) -> bool:
        """Remove this node from the list of nodes participating in runup."""
    @staticmethod
    def runupIfRequired() -> bool:
        """If the dynamics runup prefs are set, do a runup."""

class MFnAirField:
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
    def attenuation(self) -> float:
        """Returns the rate of change where the strength of the field changes as the distance between the field and the affected ob"""
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
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def classification(nodeTypeName: str) -> str:
        """Retrieves the classification string for a node type."""
    def componentOnly(self) -> bool:
        """Returns true if the air field will apply force only in the direction specified by the combination of its direction, spee"""
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
        """Creates a new DAG node with the given type tag."""
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
    def direction(self) -> MVector:
        """Returns the direction the air is blowing."""
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
    def enableSpread(self) -> bool:
        """Returns true if the air field is using the spread angle to define the influence of the air field."""
    def falloffCurve(self, param: float) -> float:
        """Returns falloff given the param in [0,1]."""
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
    @overload
    def getForceAtPoint(self, point: MPointArray, velocity: MVectorArray, mass: MDoubleArray, force: MVectorArray, deltaTime: float) -> MStatus: ...
    @overload
    def getForceAtPoint(self, point: MVectorArray, velocity: MVectorArray, mass: MDoubleArray, force: MVectorArray, deltaTime: float) -> MStatus:
        """Compute the force of a field on an array of points, given their position, velocity, and mass."""
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
    def inheritRotation(self) -> bool:
        """Returns true if the air field is rotating or parented to a rotating object, and will undergo that same rotation."""
    def inheritVelocity(self) -> float:
        """Returns the amount of the moving air field's velocity that is added to the direction and magnitude of the wind."""
    def instanceCount(self, total: bool) -> int:
        """Determines the number of times the Node attached to the Function Set is instanced."""
    def isChildOf(self, node: MObject) -> bool:
        """Determines whether or not the DAG Node attached to the Function Set is a child of the given node."""
    def isDefaultNode(self) -> bool:
        """Returns true if the node is a default node."""
    def isFalloffCurveConstantOne(self) -> bool:
        """Returns true if falloffCurve is a constant one (default) or false if not."""
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
    def magnitude(self) -> float:
        """Returns the strength of the field."""
    def maxDistance(self) -> float:
        """Returns the maximum distance from the field at which the force of the field is exerted."""
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
    def perVertex(self) -> bool:
        """Returns true if the field exerts its force on each individual point (cv, particle, vertex) equally."""
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
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setAttenuation(self, atten: float) -> MStatus:
        """Sets the rate of change where the strength of the field changes as the distance between the field and the affected objec"""
    def setComponentOnly(self, enable: bool) -> MStatus:
        """Enables the air field to apply force specified as a combination of its direction, speed, and inherit veloicty attributes"""
    def setDirection(self, airDirection: MVector) -> MStatus:
        """Sets the direction vector for the air to blow."""
    def setDoNotWrite(self, flag: bool) -> MStatus:
        """Use this method to mark the "do not write" state of this node."""
    def setEnableSpread(self, enable: bool) -> MStatus:
        """Enables the air field to influence objects based on the spread angle setting."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> MStatus:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> MStatus:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> MStatus:
        """Sets the state of the specified flag for the node."""
    def setIcon(self, filename: str) -> MStatus:
        """Associates a custom icon with the node for display in the Maya UI."""
    def setInheritRotation(self, enable: bool) -> MStatus:
        """Enables the air field to undergo rotations and effect the direction that the air field points."""
    def setInheritVelocity(self, velocity: float) -> MStatus:
        """Sets the amount of the moving air field's velocity that is added to the direction and magnitude of the wind."""
    def setInstanceable(self, how: bool) -> MStatus:
        """Sets whether or not the DAG node is instanceable."""
    def setIntermediateObject(self, isIntermediate: bool) -> MStatus:
        """Sets whether this object is an intermediate in a geometry calculation."""
    def setLocked(self, locked: bool) -> MStatus:
        """Locks or unlocks this node."""
    def setMagnitude(self, mag: float) -> MStatus:
        """Sets the strength of the field."""
    def setMaxDistance(self, maxDist: float) -> MStatus:
        """Sets the maximum distance from the field at which the force of the field is exerted."""
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
    def setPerVertex(self, enable: bool) -> MStatus:
        """Enables the field to exert its force on each individual point (cv, particle, vertex) equally."""
    def setSpeed(self, value: float) -> MStatus:
        """Sets the control setting on how quickly the objects match the velocity of the air field."""
    def setSpread(self, value: float) -> MStatus:
        """Sets the value representing an angle which objects are affected by the air fields direction setting."""
    def setUseMaxDistance(self, enable: bool) -> MStatus:
        """Enables the field to use the maximum distance setting to determine the area of influence."""
    def setUseObjectColor(self, useObjectColor: bool) -> MStatus:
        """Deprecated in 2016.0"""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def speed(self) -> float:
        """Returns the control setting on how quickly objects match the velocity of the air field."""
    def spread(self) -> float:
        """Returns a value that represents an angle which objects are affected by the air fields direction setting."""
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
    def useMaxDistance(self) -> bool:
        """Returns true if the field will use the maximum distance setting to determine the area of influence."""
    def userNode(self) -> Any:
        """If the function set's node is a plug-in node, then this method will extract the MPxNode pointer from it."""
    def usingHiliteColor(self) -> bool:
        """Determines whether or not the hilite color will be used for the node."""
    def usingObjectColor(self) -> bool:
        """Deprecated in 2016.0"""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnDragField:
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
    def attenuation(self) -> float:
        """Returns the rate of change where the strength of the field changes as the distance between the field and the affected ob"""
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
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def classification(nodeTypeName: str) -> str:
        """Retrieves the classification string for a node type."""
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
        """Creates a new DAG node with the given type tag."""
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
    def direction(self) -> MVector:
        """Returns the direction of the drag force's influence along the x, y, and z axes."""
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
    def falloffCurve(self, param: float) -> float:
        """Returns falloff given the param in [0,1]."""
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
    @overload
    def getForceAtPoint(self, point: MPointArray, velocity: MVectorArray, mass: MDoubleArray, force: MVectorArray, deltaTime: float) -> MStatus: ...
    @overload
    def getForceAtPoint(self, point: MVectorArray, velocity: MVectorArray, mass: MDoubleArray, force: MVectorArray, deltaTime: float) -> MStatus:
        """Compute the force of a field on an array of points, given their position, velocity, and mass."""
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
    def isFalloffCurveConstantOne(self) -> bool:
        """Returns true if falloffCurve is a constant one (default) or false if not."""
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
    def magnitude(self) -> float:
        """Returns the strength of the field."""
    def maxDistance(self) -> float:
        """Returns the maximum distance from the field at which the force of the field is exerted."""
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
    def perVertex(self) -> bool:
        """Returns true if the field exerts its force on each individual point (cv, particle, vertex) equally."""
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
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setAttenuation(self, atten: float) -> MStatus:
        """Sets the rate of change where the strength of the field changes as the distance between the field and the affected objec"""
    def setDirection(self, dragDirection: MVector) -> MStatus:
        """Sets the direction of the drag force's influence along the x, y, and z axes."""
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
    def setMagnitude(self, mag: float) -> MStatus:
        """Sets the strength of the field."""
    def setMaxDistance(self, maxDist: float) -> MStatus:
        """Sets the maximum distance from the field at which the force of the field is exerted."""
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
    def setPerVertex(self, enable: bool) -> MStatus:
        """Enables the field to exert its force on each individual point (cv, particle, vertex) equally."""
    def setUseDirection(self, enable: bool) -> MStatus:
        """Enables the braking force to be exerted only against the component of the object's velocity that lies along the directio"""
    def setUseMaxDistance(self, enable: bool) -> MStatus:
        """Enables the field to use the maximum distance setting to determine the area of influence."""
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
    def useDirection(self) -> bool:
        """Returns true if the braking force is exerted only against the component of the object's velocity that lies along the dir"""
    def useMaxDistance(self) -> bool:
        """Returns true if the field will use the maximum distance setting to determine the area of influence."""
    def userNode(self) -> Any:
        """If the function set's node is a plug-in node, then this method will extract the MPxNode pointer from it."""
    def usingHiliteColor(self) -> bool:
        """Determines whether or not the hilite color will be used for the node."""
    def usingObjectColor(self) -> bool:
        """Deprecated in 2016.0"""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnDynSweptGeometryData:
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
    def create(self) -> MObject:
        """This method create a new swept geometry data object for use with the dependency graph."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    @staticmethod
    def isValid(Type: int) -> bool:
        """Introduced in 2020.0"""
    def lineCount(self) -> int:
        """Return the number of line segments contained in the data."""
    def object(self) -> MObject:
        """Returns the MObject that is attached to the Function Set."""
    @overload
    def setObject(self, object: MObject) -> MStatus: ...
    @overload
    def setObject(self, object: MObject) -> MStatus:
        """Attaches the Function Set to the specified Maya Object."""
    def sweptLine(self, index: int) -> MDynSweptLine:
        """Return data for a swept line."""
    def sweptTriangle(self, index: int) -> MDynSweptTriangle:
        """Return data for a swept triangle."""
    def triangleCount(self) -> int:
        """Return the number of triangles contained in the data."""
    def type(self) -> int:
        """Function set type."""
    @staticmethod
    def typeString(Type: int) -> str:
        """Introduced in 2020.0"""

class MFnField:
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
    def attenuation(self) -> float:
        """Returns the rate of change where the strength of the field changes as the distance between the field and the affected ob"""
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
        """Creates a new DAG node with the given type tag."""
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
    def falloffCurve(self, param: float) -> float:
        """Returns falloff given the param in [0,1]."""
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
    @overload
    def getForceAtPoint(self, point: MPointArray, velocity: MVectorArray, mass: MDoubleArray, force: MVectorArray, deltaTime: float) -> MStatus: ...
    @overload
    def getForceAtPoint(self, point: MVectorArray, velocity: MVectorArray, mass: MDoubleArray, force: MVectorArray, deltaTime: float) -> MStatus:
        """Compute the force of a field on an array of points, given their position, velocity, and mass."""
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
    def isFalloffCurveConstantOne(self) -> bool:
        """Returns true if falloffCurve is a constant one (default) or false if not."""
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
    def magnitude(self) -> float:
        """Returns the strength of the field."""
    def maxDistance(self) -> float:
        """Returns the maximum distance from the field at which the force of the field is exerted."""
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
    def perVertex(self) -> bool:
        """Returns true if the field exerts its force on each individual point (cv, particle, vertex) equally."""
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
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setAttenuation(self, atten: float) -> MStatus:
        """Sets the rate of change where the strength of the field changes as the distance between the field and the affected objec"""
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
    def setMagnitude(self, mag: float) -> MStatus:
        """Sets the strength of the field."""
    def setMaxDistance(self, maxDist: float) -> MStatus:
        """Sets the maximum distance from the field at which the force of the field is exerted."""
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
    def setPerVertex(self, enable: bool) -> MStatus:
        """Enables the field to exert its force on each individual point (cv, particle, vertex) equally."""
    def setUseMaxDistance(self, enable: bool) -> MStatus:
        """Enables the field to use the maximum distance setting to determine the area of influence."""
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
    def useMaxDistance(self) -> bool:
        """Returns true if the field will use the maximum distance setting to determine the area of influence."""
    def userNode(self) -> Any:
        """If the function set's node is a plug-in node, then this method will extract the MPxNode pointer from it."""
    def usingHiliteColor(self) -> bool:
        """Determines whether or not the hilite color will be used for the node."""
    def usingObjectColor(self) -> bool:
        """Deprecated in 2016.0"""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnFluid:
    kCenterGradient: Any
    kConstant: Any
    kDynamicColorGrid: Any
    kDynamicGrid: Any
    kExtensionAttr: Any
    kFixed: Any
    kGradient: Any
    kGrid: Any
    kInvalidAttr: Any
    kLocalDynamicAttr: Any
    kNegXGradient: Any
    kNegYGradient: Any
    kNegZGradient: Any
    kNextPos: Any
    kNoFalloffGrid: Any
    kNormalAttr: Any
    kStaticColorGrid: Any
    kStaticFalloffGrid: Any
    kStaticGrid: Any
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
    kUseShadingColor: Any
    kXGradient: Any
    kYGradient: Any
    kZGradient: Any
    kZero: Any
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
        """Creates a new DAG node with the given type tag."""
    def create2D(self, Xres: int, Yres: int, Xdim: float, Ydim: float, parentOrOwner: MObject | None = None) -> MObject:
        """Creates a fluid object from the specified data and sets this function set to operate on the new fluid object."""
    def create3D(self, Xres: int, Yres: int, Zres: int, Xdim: float, Ydim: float, Zdim: float, parentOrOwner: MObject | None = None) -> MObject:
        """Creates a fluid object from the specified data and sets this function set to operate on the new fluid object."""
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
    def density(self) -> float:
        """This method returns a pointer to the storage for the density data in the fluid."""
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
    def emitIntoArrays(self, val: float, x: int, y: int, z: int, density: float, heat: float, fuel: float, doColor: bool, emitColor: MColor) -> None:
        """Use this method to add density, heat, fuel, and/or color to a particular voxel of a fluid."""
    @staticmethod
    def enableDGTiming(enable: bool) -> None:
        """Globally enables or disables the DG node timing mechanism."""
    def expandToInclude(self, min: MPoint, max: MPoint) -> MStatus:
        """Tells the fluid shape to autoresize to include these two points This would normally be used in a fluid emitter node if t"""
    def falloff(self) -> float:
        """This method returns a pointer to the storage for the falloff data in the fluid."""
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
    def fuel(self) -> float:
        """This method returns a pointer to the storage for the fuel data in the fluid."""
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
    def getColorMode(self, mode: Any) -> MStatus:
        """Get the modes by which the color values in the grid are determined."""
    def getColors(self, r: float, g: float, b: float) -> MStatus:
        """This method returns pointers to the storage for the color data in the fluid."""
    def getConnectedSetsAndMembers(self, instanceNumber: int, sets: MObjectArray, comps: MObjectArray, renderableSetsOnly: bool) -> MStatus:
        """Returns all the sets connected to the specified instance of this DAG object."""
    def getConnections(self, array: MPlugArray) -> MStatus:
        """Get all of the current connections to this node as an array of plugs."""
    def getCoordinateMode(self, mode: Any) -> MStatus:
        """Get the modes by which the UVW coordinates values in the grid are determined."""
    def getCoordinates(self, u: float, v: float, w: float) -> MStatus:
        """This method returns pointers to the storage for the uvw coordinate data in the fluid."""
    def getDensityMode(self, mode: Any, gradient: Any) -> MStatus:
        """Get the modes by which the density values in the grid are determined."""
    def getDimensions(self, Xdim: float, Ydim: float, Zdim: float) -> MStatus:
        """Gets the dimensions of the fluid."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> MStatus:
        """Returns the external content (files) that this node depends on."""
    def getFalloffMode(self, mode: Any) -> MStatus:
        """Get the modes by which the falloff values in the grid are determined."""
    @overload
    def getForceAtPoint(self, point: MPointArray, velocity: MVectorArray, mass: MDoubleArray, force: MVectorArray, deltaTime: float) -> MStatus: ...
    @overload
    def getForceAtPoint(self, point: MVectorArray, velocity: MVectorArray, mass: MDoubleArray, force: MVectorArray, deltaTime: float) -> MStatus:
        """Compute the force of the fluid as a field on an array of points, given their position, velocity, and mass."""
    def getFuelMode(self, mode: Any, gradient: Any) -> MStatus:
        """Get the modes by which the fuel values in the grid are determined."""
    def getPath(self, path: MDagPath) -> MStatus:
        """Returns a DAG Path to the DAG Node attached to the Function Set."""
    @overload
    def getResolution(self, Xres: int, Yres: int, Zres: int) -> MStatus: ...
    @overload
    def getResolution(self, Xres: int, Yres: int) -> MStatus:
        """Gets the resolution of the fluid."""
    def getTemperatureMode(self, mode: Any, gradient: Any) -> MStatus:
        """Get the modes by which the temperature values in the grid are determined."""
    def getVelocity(self, Xvel: float, Yvel: float, Zvel: float) -> MStatus:
        """This method returns pointers to the storage for the velocity data in the fluid."""
    def getVelocityMode(self, mode: Any, gradient: Any) -> MStatus:
        """Get the modes by which the velocity values in the grid are determined."""
    def gridSize(self) -> int:
        """Returns the number of elements in the grid."""
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
    @overload
    def index(self, xi: int, yi: int) -> int: ...
    @overload
    def index(self, xi: int, yi: int, zi: int) -> int: ...
    @overload
    def index(self, ai: int, xi: int, yi: int, zi: int) -> None: ...
    @overload
    def index(self, xi: int, yi: int, zi: int, xres: int, yres: int, zres: int) -> int: ...
    @overload
    def index(self, ai: int, xres: int, yres: int, zres: int, xi: int, yi: int, zi: int) -> None:
        """This is a utility routine for finding the index of a cell in an array of fluid data."""
    def instanceCount(self, total: bool) -> int:
        """Determines the number of times the Node attached to the Function Set is instanced."""
    def isAutoResize(self) -> bool:
        """Is this an autoresize fluid?"""
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
    def isResizeToEmitter(self) -> bool:
        """If this is an autoresize fluid, should it also resize to the emitter."""
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
    def pressure(self) -> float:
        """This method returns a pointer to the storage for the pressure data in the fluid."""
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
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setColorMode(self, mode: Any) -> MStatus:
        """Set the modes by which the color values in the grid are determined."""
    def setCoordinateMode(self, mode: Any) -> MStatus:
        """Set the modes by which the UVW coordinate values in the grid are determined."""
    def setDensityMode(self, mode: Any, gradient: Any) -> MStatus:
        """Set the modes by which the density values in the grid are determined."""
    def setDoNotWrite(self, flag: bool) -> MStatus:
        """Use this method to mark the "do not write" state of this node."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> MStatus:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> MStatus:
        """Sets content info in the specified attribute from the table."""
    def setFalloffMode(self, mode: Any) -> MStatus:
        """Set the modes by which the shader falloff values in the grid are determined."""
    def setFlag(self, flag: int, state: bool) -> MStatus:
        """Sets the state of the specified flag for the node."""
    def setFuelMode(self, mode: Any, gradient: Any) -> MStatus:
        """Set the modes by which the fuel values in the grid are determined."""
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
    @overload
    def setSize(self, Xres: int, Yres: int, Zres: int, Xdim: float, Ydim: float, Zdim: float, resample: bool) -> MStatus: ...
    @overload
    def setSize(self, Xres: int, Yres: int, Xdim: float, Ydim: float, resample: bool) -> MStatus:
        """Sets the size and resolution of the grid."""
    def setTemperatureMode(self, mode: Any, gradient: Any) -> MStatus:
        """Set the modes by which the temperature values in the grid are determined."""
    def setUseObjectColor(self, useObjectColor: bool) -> MStatus:
        """Deprecated in 2016.0"""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def setVelocityMode(self, mode: Any, gradient: Any) -> MStatus:
        """Set the modes by which the velocity values in the grid are determined."""
    def temperature(self) -> float:
        """This method returns a pointer to the storage for the temperature data in the fluid."""
    def toGridIndex(self, objectSpacePoint: MPoint, gridCoords: Any) -> bool:
        """For the given point in object space, get the grid indices of the voxel that it happens to lie in."""
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
    def updateGrid(self) -> MStatus:
        """Tells the fluid shape that the contents of the fluid grid has changed."""
    def userNode(self) -> Any:
        """If the function set's node is a plug-in node, then this method will extract the MPxNode pointer from it."""
    def usingHiliteColor(self) -> bool:
        """Determines whether or not the hilite color will be used for the node."""
    def usingObjectColor(self) -> bool:
        """Deprecated in 2016.0"""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""
    def velocityGridSizes(self, xsize: int, ysize: int, zsize: int) -> MStatus:
        """Returns the number of elements in the velocity grids."""
    def voxelCenterPosition(self, xi: int, yi: int, zi: int, objectSpacePoint: MPoint) -> MStatus:
        """For the given voxel, get the location of the center in object space."""

class MFnGravityField:
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
    def attenuation(self) -> float:
        """Returns the rate of change where the strength of the field changes as the distance between the field and the affected ob"""
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
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def classification(nodeTypeName: str) -> str:
        """Retrieves the classification string for a node type."""
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
        """Creates a new DAG node with the given type tag."""
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
    def direction(self) -> MVector:
        """Returns the direction of the gravitational force."""
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
    def falloffCurve(self, param: float) -> float:
        """Returns falloff given the param in [0,1]."""
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
    @overload
    def getForceAtPoint(self, point: MPointArray, velocity: MVectorArray, mass: MDoubleArray, force: MVectorArray, deltaTime: float) -> MStatus: ...
    @overload
    def getForceAtPoint(self, point: MVectorArray, velocity: MVectorArray, mass: MDoubleArray, force: MVectorArray, deltaTime: float) -> MStatus:
        """Compute the force of a field on an array of points, given their position, velocity, and mass."""
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
    def isFalloffCurveConstantOne(self) -> bool:
        """Returns true if falloffCurve is a constant one (default) or false if not."""
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
    def magnitude(self) -> float:
        """Returns the strength of the field."""
    def maxDistance(self) -> float:
        """Returns the maximum distance from the field at which the force of the field is exerted."""
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
    def perVertex(self) -> bool:
        """Returns true if the field exerts its force on each individual point (cv, particle, vertex) equally."""
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
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setAttenuation(self, atten: float) -> MStatus:
        """Sets the rate of change where the strength of the field changes as the distance between the field and the affected objec"""
    def setDirection(self, gravityDirection: MVector) -> MStatus:
        """Sets the direction vector of the gravitational force."""
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
    def setMagnitude(self, mag: float) -> MStatus:
        """Sets the strength of the field."""
    def setMaxDistance(self, maxDist: float) -> MStatus:
        """Sets the maximum distance from the field at which the force of the field is exerted."""
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
    def setPerVertex(self, enable: bool) -> MStatus:
        """Enables the field to exert its force on each individual point (cv, particle, vertex) equally."""
    def setUseMaxDistance(self, enable: bool) -> MStatus:
        """Enables the field to use the maximum distance setting to determine the area of influence."""
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
    def useMaxDistance(self) -> bool:
        """Returns true if the field will use the maximum distance setting to determine the area of influence."""
    def userNode(self) -> Any:
        """If the function set's node is a plug-in node, then this method will extract the MPxNode pointer from it."""
    def usingHiliteColor(self) -> bool:
        """Determines whether or not the hilite color will be used for the node."""
    def usingObjectColor(self) -> bool:
        """Deprecated in 2016.0"""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnInstancer:
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
    def allInstances(self, paths: MDagPathArray, matrices: MMatrixArray, particlePathStartIndices: MIntArray, pathIndices: MIntArray) -> MStatus:
        """Returns information about all instances generated by a particular particle instancer node."""
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
        """Creates a new DAG node with the given type tag."""
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
    def instancesForParticle(self, p: int, paths: MDagPathArray, instancerMatrix: MMatrix) -> int:
        """Returns the DAG paths and instancer matrix for all instances generated by a specified particle."""
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
    def particleCount(self) -> int:
        """Returns the number of particles feeding the active instancer."""
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

class MFnNIdData:
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
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def className(self, *args: Any, **kwargs: Any) -> Any: ...
    def create(self, *args: Any, **kwargs: Any) -> Any: ...
    def getObjectPtr(self, *args: Any, **kwargs: Any) -> Any: ...
    def hasObj(self, *args: Any, **kwargs: Any) -> Any: ...
    def isValid(self, *args: Any, **kwargs: Any) -> Any: ...
    def object(self, *args: Any, **kwargs: Any) -> Any: ...
    def setObject(self, *args: Any, **kwargs: Any) -> Any: ...
    def type(self, *args: Any, **kwargs: Any) -> Any: ...
    def typeString(self, *args: Any, **kwargs: Any) -> Any: ...

class MFnNObjectData:
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
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def className(self, *args: Any, **kwargs: Any) -> Any: ...
    def create(self, *args: Any, **kwargs: Any) -> Any: ...
    def getClothObjectPtr(self, *args: Any, **kwargs: Any) -> Any: ...
    def getCollide(self, *args: Any, **kwargs: Any) -> Any: ...
    def getParticleObjectPtr(self, *args: Any, **kwargs: Any) -> Any: ...
    def getRigidObjectPtr(self, *args: Any, **kwargs: Any) -> Any: ...
    def hasObj(self, *args: Any, **kwargs: Any) -> Any: ...
    def isCached(self, *args: Any, **kwargs: Any) -> Any: ...
    def isValid(self, *args: Any, **kwargs: Any) -> Any: ...
    def object(self, *args: Any, **kwargs: Any) -> Any: ...
    def setCached(self, *args: Any, **kwargs: Any) -> Any: ...
    def setObject(self, *args: Any, **kwargs: Any) -> Any: ...
    def setObjectPtr(self, *args: Any, **kwargs: Any) -> Any: ...
    def type(self, *args: Any, **kwargs: Any) -> Any: ...
    def typeString(self, *args: Any, **kwargs: Any) -> Any: ...

class MFnNewtonField:
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
    def attenuation(self) -> float:
        """Returns the rate of change where the strength of the field changes as the distance between the field and the affected ob"""
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
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def classification(nodeTypeName: str) -> str:
        """Retrieves the classification string for a node type."""
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
        """Creates a new DAG node with the given type tag."""
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
    def falloffCurve(self, param: float) -> float:
        """Returns falloff given the param in [0,1]."""
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
    @overload
    def getForceAtPoint(self, point: MPointArray, velocity: MVectorArray, mass: MDoubleArray, force: MVectorArray, deltaTime: float) -> MStatus: ...
    @overload
    def getForceAtPoint(self, point: MVectorArray, velocity: MVectorArray, mass: MDoubleArray, force: MVectorArray, deltaTime: float) -> MStatus:
        """Compute the force of a field on an array of points, given their position, velocity, and mass."""
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
    def isFalloffCurveConstantOne(self) -> bool:
        """Returns true if falloffCurve is a constant one (default) or false if not."""
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
    def magnitude(self) -> float:
        """Returns the strength of the field."""
    def maxDistance(self) -> float:
        """Returns the maximum distance from the field at which the force of the field is exerted."""
    def minDistance(self) -> float:
        """Returns the minimum distance from the newton field at which the force of the field is exerted."""
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
    def perVertex(self) -> bool:
        """Returns true if the field exerts its force on each individual point (cv, particle, vertex) equally."""
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
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setAttenuation(self, atten: float) -> MStatus:
        """Sets the rate of change where the strength of the field changes as the distance between the field and the affected objec"""
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
    def setMagnitude(self, mag: float) -> MStatus:
        """Sets the strength of the field."""
    def setMaxDistance(self, maxDist: float) -> MStatus:
        """Sets the maximum distance from the field at which the force of the field is exerted."""
    def setMinDistance(self, distance: float) -> MStatus:
        """Sets the minimum distance from the newton field at which the force of the field is exerted."""
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
    def setPerVertex(self, enable: bool) -> MStatus:
        """Enables the field to exert its force on each individual point (cv, particle, vertex) equally."""
    def setUseMaxDistance(self, enable: bool) -> MStatus:
        """Enables the field to use the maximum distance setting to determine the area of influence."""
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
    def useMaxDistance(self) -> bool:
        """Returns true if the field will use the maximum distance setting to determine the area of influence."""
    def userNode(self) -> Any:
        """If the function set's node is a plug-in node, then this method will extract the MPxNode pointer from it."""
    def usingHiliteColor(self) -> bool:
        """Determines whether or not the hilite color will be used for the node."""
    def usingObjectColor(self) -> bool:
        """Deprecated in 2016.0"""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnParticleSystem:
    kBlobby: Any
    kCloud: Any
    kExtensionAttr: Any
    kInvalidAttr: Any
    kLocalDynamicAttr: Any
    kMultiPoint: Any
    kMultiStreak: Any
    kNextPos: Any
    kNormalAttr: Any
    kNumeric: Any
    kPoints: Any
    kSpheres: Any
    kSprites: Any
    kStreak: Any
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
    kTube: Any
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
    def acceleration(self) -> None:
        """To return acceleration array for all particles."""
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
    def age(self) -> None:
        """Populates the given array with the age values of the particles in this system."""
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
    def betterIllum(self) -> bool:
        """Only for use with an MFnParticleSystem of renderType kCloud."""
    def boundingBox(self) -> Any:
        """Returns the bounding box for the dag node in object space."""
    def canBeWritten(self) -> bool:
        """Returns the do not write state of the node."""
    def castsShadows(self) -> bool:
        """Returns whether or not the rendering attribute for particles casting shadows has been enabled."""
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
    def count(self) -> int:
        """Returns the particle count at the current frame."""
    @overload
    def create(self) -> MObject: ...
    @overload
    def create(self, parent: MObject) -> MObject: ...
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
        """To create a new particleShape with a transform."""
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
    def deformedParticleShape(self) -> MObject:
        """To get the deformed particleShape."""
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
    def disableCloudAxis(self) -> bool:
        """Only for use with an MFnParticleSystem of renderType kCloud."""
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
    def emission(self) -> None:
        """Populates the given array with the incandescence values of the particles in this system, if the particles have this attr"""
    @overload
    def emit(self, position: MPoint) -> MStatus: ...
    @overload
    def emit(self, positionArray: MPointArray) -> MStatus: ...
    @overload
    def emit(self, position: MPoint, velocity: MVector) -> MStatus: ...
    @overload
    def emit(self, positionArray: MPointArray, velocityArray: MVectorArray) -> MStatus:
        """To add a new particle at the given position."""
    @staticmethod
    def enableDGTiming(enable: bool) -> None:
        """Globally enables or disables the DG node timing mechanism."""
    def evaluateDynamics(self, to: MTime, runupFromStart: bool) -> None:
        """Run up the particle system to a certain frame, from either the current frame, or from the start of the simulation."""
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
    def flatShaded(self) -> bool:
        """To check if a particle shape of cloud type is flat shaded."""
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
    def getPerParticleAttribute(self, attrName: str) -> int: ...
    @overload
    def getPerParticleAttribute(self, attrName: str) -> int: ...
    @overload
    def getPerParticleAttribute(self, attrName: str) -> int:
        """To get per particle integer attribute with its attribute name."""
    def hasAttribute(self, name: str) -> bool:
        """Returns true if the node already has an attribute with the given name."""
    def hasChild(self, node: MObject) -> bool:
        """Determines whether or not the given Node is a child of the DAG Node attached to the Function Set."""
    def hasEmission(self) -> bool:
        """Returns whether or not the particles in this system have an emission attribute."""
    def hasLifespan(self) -> bool:
        """Returns whether or not the particles in this system have a lifespan attribute."""
    @overload
    def hasObj(self, Type: int) -> bool: ...
    @overload
    def hasObj(self) -> bool:
        """Determines whether or not the Function Set is compatible with the specified Maya Object within the API RTTI system."""
    def hasOpacity(self) -> bool:
        """Returns whether or not the particles in this system have an opacity attribute."""
    def hasParent(self, node: MObject) -> bool:
        """Determines whether or not the given Node is a parent of the DAG Node attached to the Function Set."""
    def hasRgb(self) -> bool:
        """Returns whether or not the particles in this system have an rgb attribute."""
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
    def isDeformedParticleShape(self) -> bool:
        """To return if this particle shape is deformed."""
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
    def isPerParticleDoubleAttribute(self, attrName: str) -> bool:
        """To check if the input attribute is a per particle double attribute."""
    def isPerParticleIntAttribute(self, attrName: str) -> bool:
        """To check if the input attribute is a per particle integer attribute."""
    def isPerParticleVectorAttribute(self, attrName: str) -> bool:
        """To check if the input attribute is a per particle vector attribute."""
    def isShared(self) -> bool:
        """Indicates whether or not this node is shared."""
    def isTrackingEdits(self) -> bool:
        """Returns whether or not edits on the given node are being tracked by the generalized edit system."""
    @overload
    def isValid(self) -> bool: ...
    @overload
    def isValid(self, Type: int) -> bool:
        """Returns false if the particle array is nullptr."""
    def lifespan(self) -> None:
        """Populates the given array with the lifespan values of the particles in this system, if the particles have this attribute"""
    def mass(self) -> None:
        """To return mass array for all particles."""
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
    def opacity(self) -> None:
        """Populates the given array with the opacity values of the particles in this system, if the particles have this attribute."""
    def originalParticleShape(self) -> MObject:
        """To get the original particleShape."""
    def parent(self, i: int) -> MObject:
        """Queries the DAG Node attached to the Function Set for the parent Node corresponding to the given index."""
    def parentCount(self) -> int:
        """Determines the number of parent Nodes of the Node."""
    def parentNamespace(self) -> str:
        """Returns the name of the namespace in which this node resides."""
    def partialPathName(self) -> str:
        """Return a string representing the partial path from the root of the dag to this object."""
    def particleIds(self) -> None:
        """Return an array of particle identifiers at the start of the time step."""
    def particleName(self) -> str:
        """Returns the name of this particle system."""
    def pluginName(self) -> str:
        """Returns the name of the plug-in this MFnDependendencyNode was defined in."""
    def plugsAlias(self, plug: MPlug) -> str:
        """Returns the alias for the plug's attribute or the empty string if that attribute has no alias."""
    def position(self) -> None:
        """Compute each particle's position at the start of the time step."""
    def position0(self) -> None:
        """Only for use with an MFnParticleSystem of renderType kTube."""
    def position1(self) -> None:
        """Only for use with an MFnParticleSystem of renderType kTube."""
    def primaryVisibility(self) -> bool:
        """Returns whether or not the rendering attribute for primary visibility in reflections has been enabled."""
    def radius(self) -> None:
        """Calculates particle radii."""
    def radius0(self) -> None:
        """Only for use with an MFnParticleSystem of renderType kTube."""
    def radius1(self) -> None:
        """Only for use with an MFnParticleSystem of renderType kTube."""
    def receiveShadows(self) -> bool:
        """Returns whether or not the rendering attribute for particles receiving shadows has been enabled."""
    @overload
    def removeAttribute(self, attr: MObject) -> MStatus: ...
    @overload
    def removeAttribute(self, attr: MObject, type: Any) -> MStatus:
        """Remove a dynamic attribute from a node."""
    def removeChild(self, child: MObject) -> MStatus:
        """Removes the given DAG Node from the parent."""
    def removeChildAt(self, index: int) -> MStatus:
        """Removes the child at the given index from the parent."""
    def renderType(self) -> Any:
        """Return the render type used by the particle object."""
    def reorderedAttribute(self, index: int) -> MObject:
        """Some nodes, such as the various animCurve nodes, require that their attributes be set in a specific order for proper ope"""
    def rgb(self) -> None:
        """Populates the given array with the color values of the particles in this system, if the particles have this attribute."""
    def saveInitialState(self) -> MStatus:
        """To reset the particle's current state as the initial state."""
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setCount(self, arg: int) -> None:
        """Set the particle count at the current frame."""
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
    @overload
    def setPerParticleAttribute(self, attrName: str) -> None: ...
    @overload
    def setPerParticleAttribute(self, attrName: str) -> None:
        """To set the per particle vector attribute of the given name with the given values."""
    def setUseObjectColor(self, useObjectColor: bool) -> MStatus:
        """Deprecated in 2016.0"""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def surfaceShading(self) -> float:
        """Only for use with an MFnParticleSystem of renderType kCloud."""
    def tailSize(self) -> float:
        """Only for use with an MFnParticleSystem of renderType kTube."""
    def threshold(self) -> float:
        """Only for use with an MFnParticleSystem of renderType kCloud or kBlobby."""
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
    def velocity(self) -> None:
        """To return velocity array for all particles."""
    def visibleInReflections(self) -> bool:
        """Returns whether or not the rendering attribute for particle visibility in reflections has been enabled."""
    def visibleInRefractions(self) -> bool:
        """Returns whether or not the rendering attribute for particle visibility in refractions has been enabled."""

class MFnPfxGeometry:
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
        """Creates a new DAG node with the given type tag."""
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
    def getBoundingBox(self, min: float, max: float) -> MStatus:
        """Gets the bounding box of the specified geometry."""
    def getConnectedSetsAndMembers(self, instanceNumber: int, sets: MObjectArray, comps: MObjectArray, renderableSetsOnly: bool) -> MStatus:
        """Returns all the sets connected to the specified instance of this DAG object."""
    def getConnections(self, array: MPlugArray) -> MStatus:
        """Get all of the current connections to this node as an array of plugs."""
    def getExternalContent(self, table: MExternalContentInfoTable) -> MStatus:
        """Returns the external content (files) that this node depends on."""
    def getLineData(self, mainLines: MRenderLineArray, leafLines: MRenderLineArray, flowerLines: MRenderLineArray, doLines: bool, doTwist: bool, doWidth: bool, doFlatness: bool, doParameter: bool, doColor: bool, doIncandescence: bool, doTransparency: bool, worldSpace: bool) -> MStatus:
        """Get line data for the current output pfx tubes."""
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

class MFnRadialField:
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
    def attenuation(self) -> float:
        """Returns the rate of change where the strength of the field changes as the distance between the field and the affected ob"""
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
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def classification(nodeTypeName: str) -> str:
        """Retrieves the classification string for a node type."""
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
        """Creates a new DAG node with the given type tag."""
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
    def falloffCurve(self, param: float) -> float:
        """Returns falloff given the param in [0,1]."""
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
    @overload
    def getForceAtPoint(self, point: MPointArray, velocity: MVectorArray, mass: MDoubleArray, force: MVectorArray, deltaTime: float) -> MStatus: ...
    @overload
    def getForceAtPoint(self, point: MVectorArray, velocity: MVectorArray, mass: MDoubleArray, force: MVectorArray, deltaTime: float) -> MStatus:
        """Compute the force of a field on an array of points, given their position, velocity, and mass."""
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
    def isFalloffCurveConstantOne(self) -> bool:
        """Returns true if falloffCurve is a constant one (default) or false if not."""
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
    def magnitude(self) -> float:
        """Returns the strength of the field."""
    def maxDistance(self) -> float:
        """Returns the maximum distance from the field at which the force of the field is exerted."""
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
    def perVertex(self) -> bool:
        """Returns true if the field exerts its force on each individual point (cv, particle, vertex) equally."""
    def pluginName(self) -> str:
        """Returns the name of the plug-in this MFnDependendencyNode was defined in."""
    def plugsAlias(self, plug: MPlug) -> str:
        """Returns the alias for the plug's attribute or the empty string if that attribute has no alias."""
    def radialType(self) -> float:
        """Returns a type that controls the way the radial field is attenuated."""
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
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setAttenuation(self, atten: float) -> MStatus:
        """Sets the rate of change where the strength of the field changes as the distance between the field and the affected objec"""
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
    def setMagnitude(self, mag: float) -> MStatus:
        """Sets the strength of the field."""
    def setMaxDistance(self, maxDist: float) -> MStatus:
        """Sets the maximum distance from the field at which the force of the field is exerted."""
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
    def setPerVertex(self, enable: bool) -> MStatus:
        """Enables the field to exert its force on each individual point (cv, particle, vertex) equally."""
    def setType(self, value: float) -> MStatus:
        """Sets a radial field type that controls the way the field is attenuated."""
    def setUseMaxDistance(self, enable: bool) -> MStatus:
        """Enables the field to use the maximum distance setting to determine the area of influence."""
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
    def useMaxDistance(self) -> bool:
        """Returns true if the field will use the maximum distance setting to determine the area of influence."""
    def userNode(self) -> Any:
        """If the function set's node is a plug-in node, then this method will extract the MPxNode pointer from it."""
    def usingHiliteColor(self) -> bool:
        """Determines whether or not the hilite color will be used for the node."""
    def usingObjectColor(self) -> bool:
        """Deprecated in 2016.0"""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnTurbulenceField:
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
    def attenuation(self) -> float:
        """Returns the rate of change where the strength of the field changes as the distance between the field and the affected ob"""
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
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def classification(nodeTypeName: str) -> str:
        """Retrieves the classification string for a node type."""
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
        """Creates a new DAG node with the given type tag."""
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
    def falloffCurve(self, param: float) -> float:
        """Returns falloff given the param in [0,1]."""
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
    def frequency(self) -> float:
        """Returns the frequency parameter that generates irregularities in the fields motion."""
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
    @overload
    def getForceAtPoint(self, point: MPointArray, velocity: MVectorArray, mass: MDoubleArray, force: MVectorArray, deltaTime: float) -> MStatus: ...
    @overload
    def getForceAtPoint(self, point: MVectorArray, velocity: MVectorArray, mass: MDoubleArray, force: MVectorArray, deltaTime: float) -> MStatus:
        """Compute the force of a field on an array of points, given their position, velocity, and mass."""
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
    def isFalloffCurveConstantOne(self) -> bool:
        """Returns true if falloffCurve is a constant one (default) or false if not."""
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
    def magnitude(self) -> float:
        """Returns the strength of the field."""
    def maxDistance(self) -> float:
        """Returns the maximum distance from the field at which the force of the field is exerted."""
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
    def perVertex(self) -> bool:
        """Returns true if the field exerts its force on each individual point (cv, particle, vertex) equally."""
    def phase(self) -> float:
        """Returns the phase shift parameter that influences the direction of the turbulence field disruption."""
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
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setAttenuation(self, atten: float) -> MStatus:
        """Sets the rate of change where the strength of the field changes as the distance between the field and the affected objec"""
    def setDoNotWrite(self, flag: bool) -> MStatus:
        """Use this method to mark the "do not write" state of this node."""
    def setExternalContent(self, table: MExternalContentLocationTable) -> MStatus:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self, attr: MObject, table: MExternalContentLocationTable) -> MStatus:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self, flag: int, state: bool) -> MStatus:
        """Sets the state of the specified flag for the node."""
    def setFrequency(self, value: float) -> MStatus:
        """Sets the frequency parameter of the Perlin noise function used by the turbulence field."""
    def setIcon(self, filename: str) -> MStatus:
        """Associates a custom icon with the node for display in the Maya UI."""
    def setInstanceable(self, how: bool) -> MStatus:
        """Sets whether or not the DAG node is instanceable."""
    def setIntermediateObject(self, isIntermediate: bool) -> MStatus:
        """Sets whether this object is an intermediate in a geometry calculation."""
    def setLocked(self, locked: bool) -> MStatus:
        """Locks or unlocks this node."""
    def setMagnitude(self, mag: float) -> MStatus:
        """Sets the strength of the field."""
    def setMaxDistance(self, maxDist: float) -> MStatus:
        """Sets the maximum distance from the field at which the force of the field is exerted."""
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
    def setPerVertex(self, enable: bool) -> MStatus:
        """Enables the field to exert its force on each individual point (cv, particle, vertex) equally."""
    def setPhase(self, value: float) -> MStatus:
        """Sets the phase shift parameter of the Perlin noise function used by the turbulence field."""
    def setUseMaxDistance(self, enable: bool) -> MStatus:
        """Enables the field to use the maximum distance setting to determine the area of influence."""
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
    def useMaxDistance(self) -> bool:
        """Returns true if the field will use the maximum distance setting to determine the area of influence."""
    def userNode(self) -> Any:
        """If the function set's node is a plug-in node, then this method will extract the MPxNode pointer from it."""
    def usingHiliteColor(self) -> bool:
        """Determines whether or not the hilite color will be used for the node."""
    def usingObjectColor(self) -> bool:
        """Deprecated in 2016.0"""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnUniformField:
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
    def attenuation(self) -> float:
        """Returns the rate of change where the strength of the field changes as the distance between the field and the affected ob"""
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
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def classification(nodeTypeName: str) -> str:
        """Retrieves the classification string for a node type."""
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
        """Creates a new DAG node with the given type tag."""
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
    def direction(self) -> MVector:
        """Returns the direction the uniform field pushes objects."""
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
    def falloffCurve(self, param: float) -> float:
        """Returns falloff given the param in [0,1]."""
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
    @overload
    def getForceAtPoint(self, point: MPointArray, velocity: MVectorArray, mass: MDoubleArray, force: MVectorArray, deltaTime: float) -> MStatus: ...
    @overload
    def getForceAtPoint(self, point: MVectorArray, velocity: MVectorArray, mass: MDoubleArray, force: MVectorArray, deltaTime: float) -> MStatus:
        """Compute the force of a field on an array of points, given their position, velocity, and mass."""
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
    def isFalloffCurveConstantOne(self) -> bool:
        """Returns true if falloffCurve is a constant one (default) or false if not."""
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
    def magnitude(self) -> float:
        """Returns the strength of the field."""
    def maxDistance(self) -> float:
        """Returns the maximum distance from the field at which the force of the field is exerted."""
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
    def perVertex(self) -> bool:
        """Returns true if the field exerts its force on each individual point (cv, particle, vertex) equally."""
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
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setAttenuation(self, atten: float) -> MStatus:
        """Sets the rate of change where the strength of the field changes as the distance between the field and the affected objec"""
    def setDirection(self, uniformDirection: MVector) -> MStatus:
        """Sets the direction the uniform field pushes objects."""
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
    def setMagnitude(self, mag: float) -> MStatus:
        """Sets the strength of the field."""
    def setMaxDistance(self, maxDist: float) -> MStatus:
        """Sets the maximum distance from the field at which the force of the field is exerted."""
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
    def setPerVertex(self, enable: bool) -> MStatus:
        """Enables the field to exert its force on each individual point (cv, particle, vertex) equally."""
    def setUseMaxDistance(self, enable: bool) -> MStatus:
        """Enables the field to use the maximum distance setting to determine the area of influence."""
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
    def useMaxDistance(self) -> bool:
        """Returns true if the field will use the maximum distance setting to determine the area of influence."""
    def userNode(self) -> Any:
        """If the function set's node is a plug-in node, then this method will extract the MPxNode pointer from it."""
    def usingHiliteColor(self) -> bool:
        """Determines whether or not the hilite color will be used for the node."""
    def usingObjectColor(self) -> bool:
        """Deprecated in 2016.0"""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnVolumeAxisField:
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
    def attenuation(self) -> float:
        """Returns the rate of change where the strength of the field changes as the distance between the field and the affected ob"""
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
    def className() -> str: ...
    @overload
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @staticmethod
    def classification(nodeTypeName: str) -> str:
        """Retrieves the classification string for a node type."""
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
        """Creates a new DAG node with the given type tag."""
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
    @overload
    def detailTurbulence(self) -> float: ...
    @overload
    def detailTurbulence(self, value: float) -> MStatus:
        """Returns the intensity of a second higher frequency turbulence."""
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
        """Returns the direction attribute for the field force."""
    def directionalSpeed(self) -> float:
        """Returns the directionalSpeed attribute of the field."""
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
    def falloffCurve(self, param: float) -> float:
        """Returns falloff given the param in [0,1]."""
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
    @overload
    def getForceAtPoint(self, point: MPointArray, velocity: MVectorArray, mass: MDoubleArray, force: MVectorArray, deltaTime: float) -> MStatus: ...
    @overload
    def getForceAtPoint(self, point: MVectorArray, velocity: MVectorArray, mass: MDoubleArray, force: MVectorArray, deltaTime: float) -> MStatus:
        """Compute the force of a field on an array of points, given their position, velocity, and mass."""
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
    def invertAttenuation(self) -> bool:
        """Returns the value of the invertAttenuation attribute for the field force."""
    def isChildOf(self, node: MObject) -> bool:
        """Determines whether or not the DAG Node attached to the Function Set is a child of the given node."""
    def isDefaultNode(self) -> bool:
        """Returns true if the node is a default node."""
    def isFalloffCurveConstantOne(self) -> bool:
        """Returns true if falloffCurve is a constant one (default) or false if not."""
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
    def magnitude(self) -> float:
        """Returns the strength of the field."""
    def maxDistance(self) -> float:
        """Returns the maximum distance from the field at which the force of the field is exerted."""
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
    def perVertex(self) -> bool:
        """Returns true if the field exerts its force on each individual point (cv, particle, vertex) equally."""
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
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setAttenuation(self, atten: float) -> MStatus:
        """Sets the rate of change where the strength of the field changes as the distance between the field and the affected objec"""
    def setDirection(self, direction: MVector) -> MStatus:
        """Sets the direction attribute for the field force."""
    def setDirectionalSpeed(self, value: float) -> MStatus:
        """Sets the directional speed attribute for the field force."""
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
    def setInvertAttenuation(self, enable: bool) -> MStatus:
        """Enables the field will be stronger the closer to the edge of the volume a point is."""
    def setLocked(self, locked: bool) -> MStatus:
        """Locks or unlocks this node."""
    def setMagnitude(self, mag: float) -> MStatus:
        """Sets the strength of the field."""
    def setMaxDistance(self, maxDist: float) -> MStatus:
        """Sets the maximum distance from the field at which the force of the field is exerted."""
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
    def setPerVertex(self, enable: bool) -> MStatus:
        """Enables the field to exert its force on each individual point (cv, particle, vertex) equally."""
    def setSpeedAlongAxis(self, value: float) -> MStatus:
        """Sets the speed along axis attribute for the field force."""
    def setSpeedAroundAxis(self, value: float) -> MStatus:
        """Sets the speed around axis attribute for the field force."""
    def setSpeedAwayFromAxis(self, value: float) -> MStatus:
        """Sets the speed away from axis attribute for the field force."""
    def setSpeedAwayFromCenter(self, value: float) -> MStatus:
        """Sets the speed away from center attribute for the field force."""
    def setTurbulence(self, value: float) -> MStatus:
        """Sets the turbulence attribute for the field force."""
    def setTurbulenceFrequency(self, value: MVector) -> MStatus:
        """Sets the turbulenceFrequency attribute for the field force."""
    def setTurbulenceOffset(self, value: MVector) -> MStatus:
        """Sets the turbulenceOffset attribute for the field force."""
    def setTurbulenceSpeed(self, value: float) -> MStatus:
        """Sets the turbulence speed attribute for the field force."""
    def setUseMaxDistance(self, enable: bool) -> MStatus:
        """Enables the field to use the maximum distance setting to determine the area of influence."""
    def setUseObjectColor(self, useObjectColor: bool) -> MStatus:
        """Deprecated in 2016.0"""
    def setUuid(self, uuid: MUuid) -> None:
        """Sets the node's UUID."""
    def speedAlongAxis(self) -> float:
        """Returns the alongAxis attribute of the field."""
    def speedAroundAxis(self) -> float:
        """Returns the aroundAxis attribute of the field."""
    def speedAwayFromAxis(self) -> float:
        """Returns the awayFromAxis attribute of the field."""
    def speedAwayFromCenter(self) -> float:
        """Returns the awayFromCenter attribute of the field."""
    def transformationMatrix(self) -> MMatrix:
        """Returns the object space transformation matrix for this DAG node."""
    def turbulence(self) -> float:
        """Returns the turbulence intensity of the field."""
    def turbulenceFrequency(self) -> MVector:
        """Returns the turbulenceFrequency attribute for the field force."""
    def turbulenceOffset(self) -> MVector:
        """Returns the turbulenceOffset attribute for the field force."""
    def turbulenceSpeed(self) -> float:
        """Returns the rate of change of the turbulence over time."""
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
    def useMaxDistance(self) -> bool:
        """Returns true if the field will use the maximum distance setting to determine the area of influence."""
    def userNode(self) -> Any:
        """If the function set's node is a plug-in node, then this method will extract the MPxNode pointer from it."""
    def usingHiliteColor(self) -> bool:
        """Determines whether or not the hilite color will be used for the node."""
    def usingObjectColor(self) -> bool:
        """Deprecated in 2016.0"""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MFnVortexField:
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
    def attenuation(self) -> float:
        """Returns the rate of change where the strength of the field changes as the distance between the field and the affected ob"""
    @overload
    def attribute(self, index: int) -> MObject: ...
    @overload
    def attribute(self, attrName: str) -> MObject:
        """Finds the attribute of this node at the given index."""
    def attributeClass(self, attr: MObject) -> Any:
        """Returns the class (normal, dynamic, extension) of the specified attribute."""
    def attributeCount(self) -> int:
        """Returns the number of attributes that this node has."""
    def axis(self) -> MVector:
        """Returns the axis around which the vortex field exerts it's force."""
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
        """Creates a new DAG node with the given type tag."""
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
    def falloffCurve(self, param: float) -> float:
        """Returns falloff given the param in [0,1]."""
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
    @overload
    def getForceAtPoint(self, point: MPointArray, velocity: MVectorArray, mass: MDoubleArray, force: MVectorArray, deltaTime: float) -> MStatus: ...
    @overload
    def getForceAtPoint(self, point: MVectorArray, velocity: MVectorArray, mass: MDoubleArray, force: MVectorArray, deltaTime: float) -> MStatus:
        """Compute the force of a field on an array of points, given their position, velocity, and mass."""
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
    def isFalloffCurveConstantOne(self) -> bool:
        """Returns true if falloffCurve is a constant one (default) or false if not."""
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
    def magnitude(self) -> float:
        """Returns the strength of the field."""
    def maxDistance(self) -> float:
        """Returns the maximum distance from the field at which the force of the field is exerted."""
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
    def perVertex(self) -> bool:
        """Returns true if the field exerts its force on each individual point (cv, particle, vertex) equally."""
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
    def setAffectsAnimation(self) -> MStatus:
        """Introduced in 2019.0"""
    def setAlias(self, alias: str, name: str, plug: MPlug, add: bool = True) -> bool:
        """Sets or removes an alias (i.e."""
    def setAttenuation(self, atten: float) -> MStatus:
        """Sets the rate of change where the strength of the field changes as the distance between the field and the affected objec"""
    def setAxis(self, axisVector: MVector) -> MStatus:
        """Sets the axis around which the vortex field exerts it's force."""
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
    def setMagnitude(self, mag: float) -> MStatus:
        """Sets the strength of the field."""
    def setMaxDistance(self, maxDist: float) -> MStatus:
        """Sets the maximum distance from the field at which the force of the field is exerted."""
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
    def setPerVertex(self, enable: bool) -> MStatus:
        """Enables the field to exert its force on each individual point (cv, particle, vertex) equally."""
    def setUseMaxDistance(self, enable: bool) -> MStatus:
        """Enables the field to use the maximum distance setting to determine the area of influence."""
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
    def useMaxDistance(self) -> bool:
        """Returns true if the field will use the maximum distance setting to determine the area of influence."""
    def userNode(self) -> Any:
        """If the function set's node is a plug-in node, then this method will extract the MPxNode pointer from it."""
    def usingHiliteColor(self) -> bool:
        """Determines whether or not the hilite color will be used for the node."""
    def usingObjectColor(self) -> bool:
        """Deprecated in 2016.0"""
    def uuid(self) -> MUuid:
        """Returns the node's UUID."""

class MHairSystem:
    thisown: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    @overload
    @staticmethod
    def getCollisionObject(hairSystem: MObject, index: int) -> MObject: ...
    @overload
    @staticmethod
    def getCollisionObject(hairSystem: MObject, objects: MObjectArray, logicalIndices: MIntArray) -> MStatus:
        """Returns the requested collision object from the hair system."""
    @overload
    @staticmethod
    def getFollicle(hairSystem: MObject, index: int) -> MObject: ...
    @overload
    @staticmethod
    def getFollicle(hairSystem: MObject, follicles: MObjectArray, logicalIndices: MIntArray) -> MStatus:
        """Returns the requested follicle from the hair system."""
    @staticmethod
    def registerCollisionSolverCollide(MHairSystemCollisionSolverCollideFnPtr: Any) -> MStatus:
        """Register the user-supplied collision solver `fnPtr' with Maya."""
    @staticmethod
    def registerCollisionSolverPreFrame(MHairSystemCollisionSolverPreFrameFnPtr: Any) -> MStatus:
        """Register the user-supplied pre-frame method `fnPtr' with Maya."""
    @staticmethod
    def registeringCallableScript() -> bool:
        """Return true if this MHairSystem object has its callbacks defined in script."""
    @staticmethod
    def setRegisteringCallableScript() -> None:
        """Mark this MHairSystem object as one that will be passed callbacks defined in script."""
    @staticmethod
    def unregisterCollisionSolverCollide() -> MStatus:
        """De-register any user-defined collision solver that might have been registered via registerCollisionSolverCollide() ."""
    @staticmethod
    def unregisterCollisionSolverPreFrame() -> MStatus:
        """De-register any user-defined pre-frame callback that might have been registered via MHairSystem::registerCollisionSolver"""

class MRenderLine:
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self) -> None:
        """The class constructor."""
    def assign(self, other: MRenderLine) -> None: ...
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def getColor(self) -> MVectorArray:
        """Return the array of colors along the curve."""
    def getFlatness(self) -> MDoubleArray:
        """Return the array of flatness along the curve."""
    def getIncandescence(self) -> MVectorArray:
        """Return the array of incandescence along the curve."""
    def getLine(self) -> MVectorArray:
        """Return the array of vertices along the curve."""
    def getParameter(self) -> MDoubleArray:
        """Return the array of parameter along the curve."""
    def getTransparency(self) -> MVectorArray:
        """Return the array of transparency along the curve."""
    def getTwist(self) -> MVectorArray:
        """Return the array of twist vectors along the curve."""
    def getWidth(self) -> MDoubleArray:
        """Return the array of tube widths along the curve."""

class MRenderLineArray:
    thisown: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self) -> None:
        """The class constructor."""
    def assign(self, other: MRenderLineArray) -> None: ...
    @staticmethod
    def className() -> str:
        """Returns the name of this class."""
    def deleteArray(self) -> None:
        """Free up the memory held in the render line array."""
    def length(self) -> int:
        """Return the number of entries in the array."""
    def renderLine(self, index: int) -> MRenderLine:
        """Return the render line at the defined index."""

class MnCloth:
    thisown: Any
    def __init__(self) -> None:
        """Default constructor."""
    def createNCloth(self) -> MStatus:
        """Creates the underlying Maya TnCloth and sets this class to wrap it."""
    def getBounce(self, bounce: MFloatArray) -> MStatus:
        """gets the bounce at each point of the underlying N cloth object."""
    def getFriction(self, friction: MFloatArray) -> MStatus:
        """gets the friction at each point of the underlying N cloth object."""
    def getInverseMass(self, inverseMass: MFloatArray) -> MStatus:
        """gets the inverseMass at each point of the underlying N cloth object."""
    def getNumVertices(self, numVerts: int) -> MStatus:
        """Returns the number of vertices in the underlying n Cloth."""
    def getPositions(self, positions: MFloatPointArray) -> MStatus:
        """gets the positions of the points of the underlying N Object."""
    def getThickness(self, radius: MFloatArray) -> MStatus:
        """gets the thickness at each point of the underlying N cloth object."""
    def getVelocities(self, velocities: MFloatPointArray) -> MStatus:
        """gets the velocities of the points of the underlying N cloth object."""
    def setAddCrossLinks(self, addCrossLinks: bool) -> MStatus:
        """For faces with more than 3 vertices this will create additional stretch and bends links such that each vertex is connect"""
    def setAirTightness(self, airTightness: float) -> MStatus:
        """Defines the rate at which air can escape from the object, or how permiable the surface is."""
    def setBendAngleDropoff(self, dropoff: float) -> MStatus:
        """Defines the way bend resistance changes with the angle."""
    def setBendAngleScale(self, scale: float) -> MStatus:
        """Defines the amount by which the rest state of the bend angle is scaled."""
    def setBendResistance(self, strength: float) -> MStatus:
        """Bend resistance measures the amount of attraction to the restAngle, which is defined between cvs on either side of an ed"""
    def setBendRestAngleFromPositions(self, positions: MFloatPointArray) -> MStatus:
        """Sets the the bend rest angle from the list of positions for the underlying N Object This sets the shape that bend resist"""
    @overload
    def setBounce(self, bounce: float) -> MStatus: ...
    @overload
    def setBounce(self, bounce: float) -> MStatus:
        """sets the bounce for every point in this mesh"""
    def setCollisionFlags(self, vertToVert: bool, edgeToEdge: bool = False, faceToFace: bool = False) -> MStatus:
        """Sets how (or if) this object will collide with other objects."""
    def setComputeRestAngles(self, b: bool) -> MStatus:
        """Sets whether rest angles will be automatically computed, or overridden manually."""
    def setComputeRestLength(self, b: bool) -> MStatus:
        """Sets whether rest lengths will be automatically computed, or overridden manually."""
    @overload
    def setDamping(self, damping: float) -> MStatus: ...
    @overload
    def setDamping(self, damping: float) -> MStatus:
        """sets the damping for every point in this mesh"""
    def setDisableGravity(self, b: bool) -> MStatus:
        """Sets whether gravity will affect this object."""
    def setDragAndLift(self, drag: float, lift: float) -> MStatus:
        """Sets the drag and lift values for the cloth."""
    @overload
    def setFriction(self, friction: float) -> MStatus: ...
    @overload
    def setFriction(self, friction: float) -> MStatus:
        """sets the friction for every point in this mesh"""
    def setIncompressibility(self, *args: Any, **kwargs: Any) -> Any: ...
    def setInputMeshAttractAndRigidStrength(self, inputAttractArray: float, rigidArray: float, deformArray: float) -> MStatus:
        """Sets on a per particle basis, the amount by which each particle is affected by the input mesh attract, rigidity, and def"""
    def setInputMeshAttractDamping(self, damping: float) -> MStatus:
        """Defines how springy the effect of Input Mesh Attract is."""
    def setInputMeshAttractPositions(self, positions: MFloatPointArray) -> MStatus:
        """Sets the positions for input mesh attract."""
    @overload
    def setInverseMass(self, invMass: float) -> MStatus: ...
    @overload
    def setInverseMass(self, invMass: float) -> MStatus:
        """sets the mass for every point in this mesh"""
    def setLinksRestLengthFromPositions(self, positions: MFloatPointArray) -> MStatus:
        """Sets the the rest length from the list of positions for the underlying N Object."""
    def setMaxIterations(self, it: int) -> MStatus:
        """Sets the number of iterations the solver will perform on various dynamic properties like drag, damping, stretch and bend"""
    def setMaxSelfCollisionIterations(self, it: int) -> MStatus:
        """Sets the number of iterations the solver will perform for self collisions on this object."""
    def setPositions(self, positions: MFloatPointArray, startFrame: bool = True) -> MStatus:
        """Sets the positions of the vertices of the underlying N cloth object."""
    def setPressure(self, pressure: float) -> MStatus:
        """Sets the pressure within the cloth."""
    def setPressureDamping(self, damp: float) -> MStatus:
        """Sets the damping value for pressure."""
    def setPumpRate(self, pump: float) -> MStatus:
        """Defines the rate at which air pressure is added to the object."""
    def setRestitutionAngle(self, angle: float) -> MStatus:
        """Defines how far we can bend across an edge before it will fail to go back to the rest angle when there are no forces act"""
    def setRestitutionTension(self, tension: float) -> MStatus:
        """How far can the links be stretched before they fail to go back to their rest length when there are no forces acting on t"""
    def setSealHoles(self, seal: bool) -> MStatus:
        """When the volume tracking pressure method is used this determines if physical holes in the cloth model are treated as bei"""
    def setSelfCollideWidth(self, width: float) -> MStatus:
        """Sets the self collision width."""
    def setSelfCollisionFlags(self, vertToVert: bool, vertToEdge: bool = False, vertToFace: bool = False, edgeToEdge: bool = False, edgeToFace: bool = False) -> MStatus:
        """Sets how (or if) this object will collide with itself."""
    def setSelfCollisionSoftness(self, softness: float) -> MStatus:
        """This allows one to lower the repulsive force of self collisions such that some interpenetration within the collide width"""
    def setSelfCrossoverPush(self, val: float) -> MStatus:
        """See node documentation."""
    def setSelfTrappedCheck(self, on: bool) -> MStatus:
        """This tracks self collision crossovers and attempts to push the crossed over points back."""
    def setShearResistance(self, resistance: float) -> MStatus:
        """Sets the shear resistance."""
    def setStartPressure(self, startPressure: float) -> MStatus:
        """With the volume tracking pressure method this defines the relative air pressure inside the object at the startframe."""
    @overload
    def setStretchAndCompressionResistance(self, stretchResist: float, compressionResist: float) -> MStatus: ...
    @overload
    def setStretchAndCompressionResistance(self, stretchResist: float, compressionResist: float) -> MStatus:
        """Stretch Resistance:"""
    def setTangentialDrag(self, tangentialDrag: float) -> MStatus:
        """Sets the tangential drag values for the cloth."""
    @overload
    def setThickness(self, radius: float) -> MStatus: ...
    @overload
    def setThickness(self, radius: float) -> MStatus:
        """sets a radius on each point of the mesh for collision purposes."""
    def setTopology(self, numFaces: int, numVertsPerFace: int, faces: int, numEdges: int, edges: int) -> MStatus:
        """sets the topology of the underlying N Object."""
    def setTrackVolume(self, track: bool) -> MStatus:
        """When the volume tracking pressure model is used this defines how incompressible the internal volume of fluid is."""
    def setVelocities(self, velocities: MFloatPointArray) -> MStatus:
        """Sets the velocities of the vertices of the underlying Ncloth object."""

class MnObject:
    thisown: Any
    def __init__(self) -> None:
        """Default constructor."""

class MnParticle:
    thisown: Any
    def __init__(self) -> None:
        """Default constructor."""
    def createNParticle(self) -> MStatus:
        """Creates the underlying Maya TnParticle and sets this class to wrap it."""
    def getBounce(self, bounce: MFloatArray) -> MStatus:
        """gets the Bounce of the points of the underlying N particle object."""
    def getFriction(self, friction: MFloatArray) -> MStatus:
        """gets the friction of the points of the underlying N particle object."""
    def getInverseMass(self, inverseMass: MFloatArray) -> MStatus:
        """gets the inverseMass of the points of the underlying N particle object."""
    def getNumVertices(self, numVerts: int) -> MStatus:
        """Returns the number of vertices in the underlying nParticle."""
    def getPositions(self, positions: MFloatPointArray) -> MStatus:
        """gets the positions of the points of the underlying N Object."""
    def getThickness(self, radius: MFloatArray) -> MStatus:
        """gets the radii of the points of the underlying N particle object."""
    def getVelocities(self, velocities: MFloatPointArray) -> MStatus:
        """gets the velocities of the points of the underlying nParticle object."""
    @overload
    def setBounce(self, bounce: float) -> MStatus: ...
    @overload
    def setBounce(self, bounce: float) -> MStatus:
        """sets the bounce for every particle"""
    def setCollide(self, b: bool) -> MStatus:
        """Sets whether collisions will affect this object."""
    @overload
    def setDamping(self, damping: float) -> MStatus: ...
    @overload
    def setDamping(self, damping: float) -> MStatus:
        """sets the damping for every particle"""
    def setDisableGravity(self, b: bool) -> MStatus:
        """Sets whether gravity will affect this object."""
    def setDragAndLift(self, drag: float, lift: float) -> MStatus:
        """Sets the drag and lift values for the nParticle."""
    @overload
    def setFriction(self, friction: float) -> MStatus: ...
    @overload
    def setFriction(self, friction: float) -> MStatus:
        """sets the friction for every particle"""
    def setIncompressibility(self, incompressibility: float) -> MStatus:
        """sets the incompressibility"""
    @overload
    def setInverseMass(self, invMass: float) -> MStatus: ...
    @overload
    def setInverseMass(self, invMass: float) -> MStatus:
        """sets the mass for every particle"""
    def setLiquidRadiusScale(self, liquidRadiusScale: float) -> MStatus:
        """sets the liquidRadiusScale for every particle"""
    def setLiquidSimulation(self, b: bool) -> MStatus:
        """Sets whether this object will solve as a liquid."""
    def setMaxIterations(self, it: int) -> MStatus:
        """Sets the number of iterations the solver will perform on various dynamic properties like drag, damping, stretch and bend"""
    def setMaxSelfCollisionIterations(self, it: int) -> MStatus:
        """Sets the number of iterations the solver will perform for self collisions on this object."""
    def setPositions(self, positions: MFloatPointArray, startFrame: bool = True) -> MStatus:
        """Sets the positions of the vertices of the underlying nParticle object."""
    def setRestDensity(self, restDensity: float) -> MStatus:
        """sets the rest density for every particle"""
    def setSelfCollide(self, b: bool) -> MStatus:
        """Sets whether self collisions will affect this object."""
    def setSelfCollideWidth(self, width: float) -> MStatus:
        """Sets the self collision width."""
    def setSelfCollisionSoftness(self, softness: float) -> MStatus:
        """This allows one to lower the repulsive force of self collisions such that some interpenetration within the collide width"""
    @overload
    def setSurfaceTension(self, surfaceTension: float) -> MStatus: ...
    @overload
    def setSurfaceTension(self, surfaceTension: float) -> MStatus:
        """sets the surfaceTension for every particle"""
    @overload
    def setThickness(self, radius: float) -> MStatus: ...
    @overload
    def setThickness(self, radius: float) -> MStatus:
        """sets a radius on each point collision purposes."""
    def setTopology(self, numPoints: int) -> MStatus:
        """Sets the topology of the underlying N Object."""
    def setVelocities(self, velocities: MFloatPointArray) -> MStatus:
        """Sets the velocities of the vertices of the underlying nParticle object."""
    @overload
    def setViscosity(self, viscosity: float) -> MStatus: ...
    @overload
    def setViscosity(self, viscosity: float) -> MStatus:
        """sets the viscosity for every particle"""

class MnRigid:
    thisown: Any
    def __init__(self) -> None:
        """Default constructor."""
    def createNRigid(self) -> MStatus:
        """Creates the underlying Maya TnRigid and sets this class to wrap it."""
    def getBounce(self, bounce: MFloatArray) -> MStatus:
        """gets the bounce at each point of the underlying N rigid object."""
    def getFriction(self, friction: MFloatArray) -> MStatus:
        """gets the friction at each point of the underlying N rigid object."""
    def getInverseMass(self, inverseMass: MFloatArray) -> MStatus:
        """gets the inverseMass at each point of the underlying N rigid object."""
    def getNumVertices(self, numVerts: int) -> MStatus:
        """Returns the number of vertices in the underlying nRigid."""
    def getPositions(self, positions: MFloatPointArray) -> MStatus:
        """gets the positions of the points of the underlying N Object."""
    def getThickness(self, radius: MFloatArray) -> MStatus:
        """gets the thickness at each point of the underlying N rigid object."""
    def getVelocities(self, velocities: MFloatPointArray) -> MStatus:
        """gets the velocities of the points of the underlying nRigid object."""
    @overload
    def setBounce(self, bounce: float) -> MStatus: ...
    @overload
    def setBounce(self, bounce: float) -> MStatus:
        """sets the bounce for every point in this mesh"""
    def setCollisionFlags(self, vertToVert: bool, edgeToEdge: bool = False, faceToFace: bool = False) -> MStatus:
        """Sets how (or if) this object will collide with other objects."""
    @overload
    def setFriction(self, friction: float) -> MStatus: ...
    @overload
    def setFriction(self, friction: float) -> MStatus:
        """sets the friction for every point in this mesh"""
    def setPositions(self, positions: MFloatPointArray, startFrame: bool = True) -> MStatus:
        """Sets the positions of the vertices of the underlying nRigid object."""
    @overload
    def setThickness(self, radius: float) -> MStatus: ...
    @overload
    def setThickness(self, radius: float) -> MStatus:
        """sets a radius on each point of the mesh for collision purposes."""
    def setTopology(self, numFaces: int, numVertsPerFace: int, faces: int, numEdges: int, edges: int) -> MStatus:
        """sets the topology of the underlying N Object."""
    def setVelocities(self, velocities: MFloatPointArray) -> MStatus:
        """Sets the velocities of the vertices of the underlying nRigid object."""

class MnSolver:
    thisown: Any
    def __init__(self) -> None:
        """Default constructor."""
    def addNObject(self, obj: MnObject) -> MStatus:
        """Assign the nucleus object to be solved by this solver."""
    def createNSolver(self) -> MStatus:
        """Creates the underlying Maya solver object and sets this class to wrap it."""
    def makeAllCollide(self) -> MStatus:
        """Allow all the objects assigned to the Maya solver object to collide."""
    def removeAllCollisions(self) -> MStatus:
        """Remove the collisions between all the objects assigned to the Maya solver object."""
    def removeNObject(self, obj: MnObject) -> MStatus:
        """Remove the nucleus object from being solved by this solver."""
    def setAirDensity(self, dens: float) -> MStatus:
        """Sets the air Density for the solver."""
    def setDisabled(self, disabled: bool) -> MStatus:
        """Disables the solver - or re-enables it again."""
    def setGravity(self, grav: float) -> MStatus:
        """Sets the gravity magnitude for the objects being solved."""
    def setGravityDir(self, gravX: float, gravY: float, gravZ: float) -> MStatus:
        """Sets the gravity direction for the underlying Maya solver object."""
    def setMaxIterations(self, maxIter: int) -> MStatus:
        """Set the max number of collision iterations used by the solver."""
    def setStartTime(self, startTime: float) -> MStatus:
        """Sets the start Time in seconds for the solver."""
    def setSubsteps(self, substeps: int) -> MStatus:
        """Set the number of substeps used by the solver."""
    def setWindDir(self, windX: float, windY: float, windZ: float) -> MStatus:
        """Sets the wind direction for the underlying Maya solver object."""
    def setWindNoiseIntensity(self, noise: float) -> MStatus:
        """Sets the wind noise intensity for the underlying Maya solver object."""
    def setWindSpeed(self, speed: float) -> MStatus:
        """Sets the wind magnitude for the underlying Maya solver object."""
    def solve(self, solveTime: float) -> MStatus:
        """Solve from the last eval time until the specified time (in seconds)."""

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
