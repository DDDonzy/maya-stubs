# Stub for maya.api.OpenMayaRender - generated from Maya 2024 Python API reference

from typing import Any

from maya.api.OpenMaya import MBoundingBox
from maya.api.OpenMaya import MColor
from maya.api.OpenMaya import MDagPath
from maya.api.OpenMaya import MDoubleArray
from maya.api.OpenMaya import MFloatPoint
from maya.api.OpenMaya import MImage
from maya.api.OpenMaya import MMatrix
from maya.api.OpenMaya import MObject
from maya.api.OpenMaya import MPlug
from maya.api.OpenMaya import MSelectionList
from maya.api.OpenMaya import MSelectionMask
from maya.api.OpenMaya import MUintArray
from maya.api.OpenMaya import MUserData

class MAttributeParameterMapping:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def allowConnection(self) -> bool:
        """This method returns true if Maya is allowed to connect other shade fragments to the parameter named by this mapping."""
    def allowRename(self) -> bool:
        """This method returns true if the parameter named by this mapping may be renamed in the final shading effect."""
    def attributeName(self) -> Any:
        """Get the attribute name for this mapping."""
    def parameterName(self) -> Any:
        """Get the parameter name for this mapping."""
    def resolvedParameterName(self) -> Any:
        """Get the resolved parameter name for this mapping. After the fragment has been joined with other"""

class MAttributeParameterMappingList:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def append(self, MAttributeParameterMapping: Any) -> MAttributeParameterMappingList:
        """Add a mapping to the list. The list makes a copy; ownership of the original is left with the caller."""
    def clear(self) -> MAttributeParameterMappingList:
        """Clear all mappings from the list."""
    def findByAttributeName(self, attributeName: Any) -> MAttributeParameterMapping:
        """Find a mapping by attribute name."""
    def findByParameterName(self, parameterName: Any) -> MAttributeParameterMapping:
        """Find a mapping by parameter name."""

class MBlendState:
    kAdd: Any
    kAlphaChannel: Any
    kBlendFactor: Any
    kBlueChannel: Any
    kBothInvSourceAlpha: Any
    kBothSourceAlpha: Any
    kDestinationAlpha: Any
    kDestinationColor: Any
    kGreenChannel: Any
    kInvBlendFactor: Any
    kInvDestinationAlpha: Any
    kInvDestinationColor: Any
    kInvSourceAlpha: Any
    kInvSourceColor: Any
    kMax: Any
    kMaxTargets: Any
    kMin: Any
    kNoChannels: Any
    kOne: Any
    kRGBAChannels: Any
    kRGBChannels: Any
    kRedChannel: Any
    kReverseSubtract: Any
    kSourceAlpha: Any
    kSourceAlphaSat: Any
    kSourceColor: Any
    kSubtract: Any
    kZero: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def desc(self) -> MBlendStateDesc:
        """Get the blend state descriptor that was used to create the state object."""
    def resourceHandle(self) -> int:
        """Returns a long containing a C++ 'void' pointer which points to the draw API dependent handle for a blend state."""

class MBlendStateDesc:
    alphaToCoverageEnable: Any
    blendFactor: Any
    independentBlendEnable: Any
    multiSampleMask: Any
    targetBlends: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def setDefaults(self) -> MBlendStateDesc:
        """Set all values for the blend state to their default values."""

class MCameraOverride:
    mCameraPath: Any
    mFarClippingPlane: Any
    mHiddenCameraList: Any
    mNearClippingPlane: Any
    mProjectionMatrix: Any
    mUseFarClippingPlane: Any
    mUseHiddenCameraList: Any
    mUseNearClippingPlane: Any
    mUseProjectionMatrix: Any
    mUseViewMatrix: Any
    mViewMatrix: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MClearOperation:
    kClear: Any
    kClearAll: Any
    kClearColor: Any
    kClearDepth: Any
    kClearNone: Any
    kClearStencil: Any
    kDataServer: Any
    kHUDRender: Any
    kPresentTarget: Any
    kQuadRender: Any
    kSceneRender: Any
    kUserDefined: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def clearColor(self) -> Any:
        """Query the first clear color values."""
    def clearColor2(self) -> Any:
        """Query the second clear color values."""
    def clearDepth(self) -> float:
        """Query the clear depth value."""
    def clearGradient(self) -> bool:
        """Query if the clear should clear with a vertical color gradient."""
    def clearStencil(self) -> int:
        """Query the stencil clear value."""
    def enableSRGBWrite(self) -> bool:
        """Return whether to enable GPU based gamma correction during pixel writes."""
    def mask(self) -> int:
        """Query the clear mask."""
    def name(self) -> Any:
        """Returns the name of the render operator."""
    def operationType(self) -> int:
        """Returns the type of a render operator."""
    def overridesColors(self) -> bool:
        """Query whether clear colors are set by the override or come from Maya's preferences."""
    def setClearColor(self, arg: Any) -> MClearOperation:
        """Set the first clear color values."""
    def setClearColor2(self, arg: Any) -> MClearOperation:
        """Set the second clear color values."""
    def setClearDepth(self, float: Any) -> MClearOperation:
        """Set the clear depth value."""
    def setClearGradient(self, bool: Any) -> MClearOperation:
        """Set whether to clear with a vertical color gradient."""
    def setClearStencil(self, int: Any) -> MClearOperation:
        """Set the clear stencil value."""
    def setMask(self, int: Any) -> MClearOperation:
        """Set the clear mask to define which channels to clear."""
    def setOverridesColors(self, bool: Any) -> MClearOperation:
        """Set the enabled state to control whether the clear operation overrides Maya's color preferences."""
    def targetOverrideList(self) -> list[MRenderTarget]:
        """Return a list of render target which will be used as the target overrides for the operation."""
    def viewportRectangleOverride(self) -> MFloatPoint:
        """Query for a viewport rectangle override."""

class MColorManagementUtilities:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def getColorTransformCacheIdForInputSpace(inputSpaceName: Any) -> Any:
        """Utility function to retrieve the id of a color transform"""
    @staticmethod
    def getColorTransformCacheIdForOutputTransform() -> Any:
        """Utility function to retrieve the id of the color transform to be applied on the final output."""
    @staticmethod
    def getColorTransformData(arg: Any, data: Any) -> Any:
        """Obtain a reference to opaque data containing the color transform"""
    @staticmethod
    def isColorManagementAvailable() -> bool:
        """Returns whether color management is available for the current scene."""
    @staticmethod
    def isColorManagementEnabled() -> bool:
        """Returns whether color management is enabled for the current scene."""

class MComponentDataIndexing:
    kFaceVertex: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def componentType(self) -> Any:
        """Get the component type that the vertex indices represent."""
    def indices(self) -> MUintArray:
        """Get the array of vertex indices for the component."""
    def setComponentType(self, MComponentType: Any) -> MComponentDataIndexing:
        """Set the component type that the vertex indices represent."""

class MComponentDataIndexingList:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def append(self, MComponentDataIndexing: Any) -> bool:
        """Add a MComponentDataIndexing to the list. Creates and stores a copy which is owned by the list."""
    def clear(self) -> MComponentDataIndexingList:
        """Clear the list."""
    def remove(self, index: Any) -> bool:
        """Remove a MComponentDataIndexing from the list."""

class MDepthNormalizationDescription:
    fDepthBias: Any
    fDepthScale: Any
    fFarClipDistance: Any
    fNearClipDistance: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MDepthStencilState:
    kDecrementStencil: Any
    kDecrementStencilSat: Any
    kIncrementStencil: Any
    kIncrementStencilSat: Any
    kInvertStencil: Any
    kKeepStencil: Any
    kReplaceStencil: Any
    kZeroStencil: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def desc(self) -> MDepthStencilStateDesc:
        """Get the depth-stencil state descriptor that was used to create the state object."""
    def resourceHandle(self) -> int:
        """Returns a long containing a C++ 'void' pointer which points to the draw API dependent handle for a depth-stencil state."""

class MDepthStencilStateDesc:
    backFace: Any
    depthEnable: Any
    depthFunc: Any
    depthWriteEnable: Any
    frontFace: Any
    stencilEnable: Any
    stencilReadMask: Any
    stencilReferenceVal: Any
    stencilWriteMask: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def setDefaults(self) -> MDepthStencilStateDesc:
        """Set all values for the depth stencil state to their default values."""

class MDrawContext:
    k2dViewport: Any
    k3dViewport: Any
    kAmbientLight: Any
    kAmbientOcclusion: Any
    kAntiAliasing: Any
    kBackfaceCulling: Any
    kBoundingBox: Any
    kCustomLights: Any
    kDefaultMaterial: Any
    kDepthOfField: Any
    kDepthPeeling: Any
    kExcludeAll: Any
    kExcludeCVs: Any
    kExcludeCameras: Any
    kExcludeClipGhosts: Any
    kExcludeControllers: Any
    kExcludeDeformers: Any
    kExcludeDimensions: Any
    kExcludeDynamicConstraints: Any
    kExcludeDynamics: Any
    kExcludeFluids: Any
    kExcludeFollicles: Any
    kExcludeGreasePencils: Any
    kExcludeGrid: Any
    kExcludeHUD: Any
    kExcludeHairSystems: Any
    kExcludeHoldOuts: Any
    kExcludeHulls: Any
    kExcludeIkHandles: Any
    kExcludeImagePlane: Any
    kExcludeJoints: Any
    kExcludeLights: Any
    kExcludeLocators: Any
    kExcludeManipulators: Any
    kExcludeMeshes: Any
    kExcludeMotionTrails: Any
    kExcludeNCloths: Any
    kExcludeNParticles: Any
    kExcludeNRigids: Any
    kExcludeNone: Any
    kExcludeNurbsCurves: Any
    kExcludeNurbsSurfaces: Any
    kExcludeParticleInstancers: Any
    kExcludePivots: Any
    kExcludePlanes: Any
    kExcludePluginShapes: Any
    kExcludeSelectHandles: Any
    kExcludeStrokes: Any
    kExcludeSubdivSurfaces: Any
    kExcludeTextures: Any
    kFilteredIgnoreLightLimit: Any
    kFilteredToLightLimit: Any
    kFlatShaded: Any
    kFogExp: Any
    kFogExp2: Any
    kFogLinear: Any
    kGammaCorrection: Any
    kGouraudShaded: Any
    kImage: Any
    kLightDefault: Any
    kMotionBlur: Any
    kNoLighting: Any
    kObjectSorting: Any
    kProjectionInverseMtx: Any
    kProjectionMtx: Any
    kProjectionTranposeMtx: Any
    kProjectionTranspInverseMtx: Any
    kSceneLights: Any
    kSelectedLights: Any
    kShadeActiveOnly: Any
    kSmoothWireframe: Any
    kTextured: Any
    kTwoSidedLighting: Any
    kUnsorted: Any
    kViewColorTransformEnabled: Any
    kViewDirection: Any
    kViewFarClipValue: Any
    kViewInverseMtx: Any
    kViewMtx: Any
    kViewNearClipValue: Any
    kViewPosition: Any
    kViewProjInverseMtx: Any
    kViewProjMtx: Any
    kViewProjTranposeMtx: Any
    kViewProjTranspInverseMtx: Any
    kViewRight: Any
    kViewTranspInverseMtx: Any
    kViewTransposeMtx: Any
    kViewUnnormalizedFarClipValue: Any
    kViewUnnormlizedNearClipValue: Any
    kViewUp: Any
    kViewportPixelSize: Any
    kWeightedAverage: Any
    kWireFrame: Any
    kWireFrameOnShadedNone: Any
    kWireFrameOnShadedReduced: Any
    kWireframeOnShadedFull: Any
    kWorldInverseMtx: Any
    kWorldMtx: Any
    kWorldTranspInverseMtx: Any
    kWorldTransposeMtx: Any
    kWorldViewInverseMtx: Any
    kWorldViewMtx: Any
    kWorldViewProjInverseMtx: Any
    kWorldViewProjMtx: Any
    kWorldViewProjTranspInverseMtx: Any
    kWorldViewProjTransposeMtx: Any
    kWorldViewTranspInverseMtx: Any
    kWorldViewTransposeMtx: Any
    kXray: Any
    kXrayActiveComponents: Any
    kXrayJoint: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def classificationExclusions(self) -> Any:
        """Get a list of drawdb strings for object which are excluded from display"""
    def copyCurrentColorRenderTarget(self, string: Any) -> MRenderTarget:
        """Get a copy of the current color render target."""
    def copyCurrentColorRenderTargetToTexture(self) -> MTexture:
        """Get a copy of the current color render target as a texture."""
    def copyCurrentDepthRenderTarget(self, string: Any) -> MRenderTarget:
        """Get a copy of the current depth render target."""
    def copyCurrentDepthRenderTargetToTexture(self) -> MTexture:
        """Get a copy of the current depth render target as a texture."""
    def getBackgroundParameters(self) -> Any:
        """Get parameters related to how the background is cleared"""
    def getCurrentCameraPath(self) -> MDagPath:
        """Get the path to the camera being used to render the current frame."""
    def getCurrentColorRenderTarget(self) -> MRenderTarget:
        """Get current color render target."""
    def getCurrentDepthRenderTarget(self) -> MRenderTarget:
        """Get current depth render target."""
    def getDOFParameters(self) -> Any:
        """Get the parameters generated by Maya for the circle-of-confusion depth shader used"""
    def getDepthRange(self) -> Any:
        """Get the depth range which specifies the mapping of depth values from normalized device coordinates to window coordinates."""
    def getDisplayStyle(self) -> int:
        """The DisplayStyle enums can be use to test the bit field for the enabling of any"""
    def getEnvironmentParameters(self) -> Any:
        """Get parameters for currently used environment. Note that this information is set"""
    def getFrameStamp(self) -> int:
        """Returns the current frame stamp."""
    def getFrustumBox(self) -> MBoundingBox:
        """Get the bounding box of the current view frustum in world space."""
    def getGlobalLineWidth(self) -> float:
        """Get global line width."""
    def getHwFogParameters(self) -> Any:
        """Get all the hardware fog parameters."""
    def getLightInformation(self, lightNumber: Any, lightFilter: Any) -> Any:
        """Return common lighting information for a given active light."""
    def getLightLimit(self) -> int:
        """Get the current light limit."""
    def getLightParameterInformation(self, lightNumber: Any, lightFilter: Any) -> MLightParameterInformation:
        """Return parameter information for a given active light."""
    def getLightingMode(self) -> int:
        """Get the current light mode."""
    def getMatrix(self, int: Any) -> MMatrix:
        """Get a matrix value of a certain type."""
    def getPassContext(self) -> MPassContext:
        """Access the current pass context."""
    def getPostEffectEnabled(self, int: Any) -> bool:
        """Returns if a given post effect is currently enabled."""
    def getRenderOverrideInformation(self) -> Any:
        """Get information about any render override"""
    def getRenderTargetSize(self) -> Any:
        """Get the size of the render target (output buffer) being rendered into."""
    def getSceneBox(self) -> MBoundingBox:
        """Get a bounding box of the scene in world space."""
    def getStateManager(self) -> MStateManager:
        """Access the GPU state manager for the current draw context."""
    def getTransparencyAlgorithm(self) -> int:
        """Get the current transparency algoritm."""
    def getTuple(self, int: Any) -> MDoubleArray:
        """Get a tuple (vector, position or single) value of a certain type."""
    def getViewportDimensions(self) -> Any:
        """Get the viewport dimensions. The origin is the upper left corner of the viewport."""
    @staticmethod
    def inUserInteraction() -> bool:
        """Returns True during any interactive refresh, as when user is interacting with the scene"""
    def numberOfActiveLights(self, lightFilter: Any) -> int:
        """Return the number of available lights to render the scene,"""
    def objectTypeExclusions(self) -> int:
        """Get the object type exclusions as a bitfield."""
    def renderingDestination(self) -> Any:
        """Return the destination (type and name) that the renderer is drawing to."""
    @staticmethod
    def semanticToMatrixType(string: Any) -> int:
        """Given a semantic name return the corresponding matrix enumeration that can be used to retrieve a matrix value via the getMatrix() method."""
    @staticmethod
    def semanticToTupleType(string: Any) -> int:
        """Given a semantic name return the corresponding tuple enumeration that can be used to retrieve a value via the getTuple() method."""
    @staticmethod
    def shadeTemplates() -> bool:
        """Returns the display preference indicating whether templated objects should be drawn shaded."""
    @staticmethod
    def userChangingViewContext() -> bool:
        """Returns True during any interactive refresh, as when user is	changing the view using view context"""
    def viewDirectionAlongNegZ(self) -> bool:
        """Return whether the view direction is pointing down the -Z axis."""
    @staticmethod
    def wireOnShadedMode() -> int:
        """Returns the global user display preference which indicates how wireframe should be drawn on top of objects while in shaded mode."""

class MDrawRegistry:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def deregisterComponentConverter(renderItemName: Any) -> None:
        """Deregister an implementation of MPxComponentConverter."""
    @staticmethod
    def deregisterDrawOverrideCreator(drawClassification: Any, registrantId: Any) -> None:
        """Deregister an implementation of MPxDrawOverride."""
    @staticmethod
    def deregisterGeometryOverrideCreator(drawClassification: Any, registrantId: Any) -> None:
        """Deregister an implementation of MPxGeometryOverride."""
    @staticmethod
    def deregisterImagePlaneOverrideCreator(drawClassification: Any, registrantId: Any) -> None:
        """Deregister an implementation of MPxImagePlaneOverride."""
    @staticmethod
    def deregisterIndexBufferMutator(primitiveType: Any) -> None:
        """Deregister an implementation of MPxIndexBufferMutator."""
    @staticmethod
    def deregisterPrimitiveGenerator(primitiveType: Any) -> None:
        """Deregister an implementation of MPxPrimitiveGenerator."""
    @staticmethod
    def deregisterShaderOverrideCreator(drawClassification: Any, registrantId: Any) -> None:
        """Deregister an implementation of MPxShaderOverride."""
    @staticmethod
    def deregisterShadingNodeOverrideCreator(drawClassification: Any, registrantId: Any) -> None:
        """Deregister an implementation of MPxShadingNodeOverride."""
    @staticmethod
    def deregisterSubSceneOverrideCreator(drawClassification: Any, registrantId: Any) -> None:
        """Deregister an implementation of MPxSubSceneOverride."""
    @staticmethod
    def deregisterSurfaceShadingNodeOverrideCreator(drawClassification: Any, registrantId: Any) -> None:
        """Deregister an implementation of MPxSurfaceShadingNodeOverride."""
    @staticmethod
    def deregisterVertexBufferGenerator(bufferName: Any) -> None:
        """Deregister an implementation of MPxVertexBufferGenerator."""
    @staticmethod
    def deregisterVertexBufferMutator(bufferName: Any) -> None:
        """Deregister an implementation of MPxVertexBufferMutator."""
    @staticmethod
    def registerComponentConverter(renderItemName: Any, creator: Any) -> None:
        """Register an implementation of MPxComponentConverter to use with render items that have the specified name."""
    @staticmethod
    def registerDrawOverrideCreator(drawClassification: Any, registrantId: Any, creator: Any) -> None:
        """Register an implementation of MPxDrawOverride to use with DAG objects that have the specified, draw-specific classification string."""
    @staticmethod
    def registerGeometryOverrideCreator(drawClassification: Any, registrantId: Any, creator: Any) -> None:
        """Register an implementation of MPxGeometryOverride to use with nodes that have the specified, draw-specific classification string."""
    @staticmethod
    def registerImagePlaneOverrideCreator(drawClassification: Any, registrantId: Any, creator: Any) -> None:
        """Register an implementation of MPxImagePlaneOverride to use with DAG objects that have the specified, draw-specific classification string."""
    @staticmethod
    def registerIndexBufferMutator(primitiveType: Any, creator: Any) -> None:
        """Register an implementation of MPxIndexBufferMutator to generate custom primitive types for shapes."""
    @staticmethod
    def registerPrimitiveGenerator(primitiveType: Any, creator: Any) -> None:
        """Register an implementation of MPxPrimitiveGenerator to generate custom primitive types for shapes."""
    @staticmethod
    def registerShaderOverrideCreator(drawClassification: Any, registrantId: Any, creator: Any) -> None:
        """Register an implementation of MPxShaderOverride to use with nodes that have the specified, draw-specific classification string."""
    @staticmethod
    def registerShadingNodeOverrideCreator(drawClassification: Any, registrantId: Any, creator: Any) -> None:
        """Register an implementation of MPxShadingNodeOverride to use with nodes that have the specified, draw-specific classification string."""
    @staticmethod
    def registerSubSceneOverrideCreator(drawClassification: Any, registrantId: Any, creator: Any) -> None:
        """Register an implementation of MPxSubSceneOverride to use with DAG objects that have the specified, draw-specific classification string."""
    @staticmethod
    def registerSurfaceShadingNodeOverrideCreator(drawClassification: Any, registrantId: Any, creator: Any) -> None:
        """Register an implementation of MPxSurfaceShadingNodeOverride to use with surface shaders that have the specified, draw-specific classification string."""
    @staticmethod
    def registerVertexBufferGenerator(bufferName: Any, creator: Any) -> None:
        """Register an implementation of MPxVertexBufferGenerator to provide custom vertex streams for shapes."""
    @staticmethod
    def registerVertexBufferMutator(bufferName: Any, creator: Any) -> None:
        """Register an implementation of MPxVertexBufferMutator to provide custom vertex streams for shapes."""

class MFragmentManager:
    kDomainShader: Any
    kGeometryShader: Any
    kHullConstantShader: Any
    kHullShader: Any
    kPixelShader: Any
    kVertexShader: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addAutomaticShaderStageInput(self, int: Any, string: Any, string_: Any, int_: Any, bool: Any) -> bool:
        """Add a parameter to the list of automatic input parameters for a specified"""
    def addDomainShaderInputNameMapping(self, string: Any, string_: Any) -> bool:
        """Add a mapping between a parameter name (realParamName) and a transient"""
    def addFragmentGraphFromBuffer(self, buffer: Any) -> Any:
        """Add a new fragment graph to the manager."""
    def addFragmentGraphFromFile(self, fileName: Any) -> Any:
        """Add a new fragment graph to the manager."""
    def addFragmentPath(self, path: Any) -> bool:
        """Add a path to the list of fragment search paths used when parsing the file path for any"""
    def addShadeFragmentFromBuffer(self, buffer: Any, hidden: Any) -> Any:
        """Add a new fragment to the manager."""
    def addShadeFragmentFromFile(self, fileName: Any, hidden: Any) -> Any:
        """Add a new fragment to the manager."""
    def findDomainShaderInputName(self, string: Any) -> Any:
        """Find the transient name which is used in domain shader."""
    def fragmentList(self) -> list[Any]:
        """Returns a list of the names of all registered fragments and fragment graphs."""
    def getColorManagementFragmentInfo(self, arg: Any, string: Any, string_: Any) -> Any:
        """Returns the name and parameters of a shader fragment that converts a color from the"""
    def getEffectOutputDirectory(self) -> Any:
        """Get the directory to be used for effect file output."""
    def getFragmentXML(self, fragmentName: Any) -> Any:
        """getFragmentXML(shadingNode, includeUpstreamNodes=False, objectContext=None) -> string"""
    def getIntermediateGraphOutputDirectory(self) -> Any:
        """Get the directory to be used for intermediate fragment graph output."""
    def hasFragment(self, string: Any) -> bool:
        """Returns True if a fragment of the given name has been registered with the fragment manager."""
    def removeAutomaticShaderStageInput(self, int: Any, string: Any) -> bool:
        """Remove a parameter from the list of automatic input parameters for a"""
    def removeDomainShaderInputNameMapping(self, string: Any) -> bool:
        """Remove a mapping between a parameter name (realParamName) and a transient"""
    def removeFragment(self, fragmentName: Any) -> bool:
        """Remove a named fragment or fragment graph from the fragment manager. This"""
    def setEffectOutputDirectory(self, string: Any) -> MFragmentManager:
        """Set the path to use for dumping final effect files."""
    def setIntermediateGraphOutputDirectory(self, string: Any) -> MFragmentManager:
        """Set the path to use for dumping intermediate fragment graph XML files."""

class MFrameContext:
    k2dViewport: Any
    k3dViewport: Any
    kAmbientLight: Any
    kAmbientOcclusion: Any
    kAntiAliasing: Any
    kBackfaceCulling: Any
    kBoundingBox: Any
    kCustomLights: Any
    kDefaultMaterial: Any
    kDepthOfField: Any
    kDepthPeeling: Any
    kExcludeAll: Any
    kExcludeCVs: Any
    kExcludeCameras: Any
    kExcludeClipGhosts: Any
    kExcludeControllers: Any
    kExcludeDeformers: Any
    kExcludeDimensions: Any
    kExcludeDynamicConstraints: Any
    kExcludeDynamics: Any
    kExcludeFluids: Any
    kExcludeFollicles: Any
    kExcludeGreasePencils: Any
    kExcludeGrid: Any
    kExcludeHUD: Any
    kExcludeHairSystems: Any
    kExcludeHoldOuts: Any
    kExcludeHulls: Any
    kExcludeIkHandles: Any
    kExcludeImagePlane: Any
    kExcludeJoints: Any
    kExcludeLights: Any
    kExcludeLocators: Any
    kExcludeManipulators: Any
    kExcludeMeshes: Any
    kExcludeMotionTrails: Any
    kExcludeNCloths: Any
    kExcludeNParticles: Any
    kExcludeNRigids: Any
    kExcludeNone: Any
    kExcludeNurbsCurves: Any
    kExcludeNurbsSurfaces: Any
    kExcludeParticleInstancers: Any
    kExcludePivots: Any
    kExcludePlanes: Any
    kExcludePluginShapes: Any
    kExcludeSelectHandles: Any
    kExcludeStrokes: Any
    kExcludeSubdivSurfaces: Any
    kExcludeTextures: Any
    kFlatShaded: Any
    kFogExp: Any
    kFogExp2: Any
    kFogLinear: Any
    kGammaCorrection: Any
    kGouraudShaded: Any
    kImage: Any
    kLightDefault: Any
    kMotionBlur: Any
    kNoLighting: Any
    kObjectSorting: Any
    kProjectionInverseMtx: Any
    kProjectionMtx: Any
    kProjectionTranposeMtx: Any
    kProjectionTranspInverseMtx: Any
    kSceneLights: Any
    kSelectedLights: Any
    kShadeActiveOnly: Any
    kSmoothWireframe: Any
    kTextured: Any
    kTwoSidedLighting: Any
    kUnsorted: Any
    kViewColorTransformEnabled: Any
    kViewDirection: Any
    kViewFarClipValue: Any
    kViewInverseMtx: Any
    kViewMtx: Any
    kViewNearClipValue: Any
    kViewPosition: Any
    kViewProjInverseMtx: Any
    kViewProjMtx: Any
    kViewProjTranposeMtx: Any
    kViewProjTranspInverseMtx: Any
    kViewRight: Any
    kViewTranspInverseMtx: Any
    kViewTransposeMtx: Any
    kViewUnnormalizedFarClipValue: Any
    kViewUnnormlizedNearClipValue: Any
    kViewUp: Any
    kViewportPixelSize: Any
    kWeightedAverage: Any
    kWireFrame: Any
    kWireFrameOnShadedNone: Any
    kWireFrameOnShadedReduced: Any
    kWireframeOnShadedFull: Any
    kWorldInverseMtx: Any
    kWorldMtx: Any
    kWorldTranspInverseMtx: Any
    kWorldTransposeMtx: Any
    kWorldViewInverseMtx: Any
    kWorldViewMtx: Any
    kWorldViewProjInverseMtx: Any
    kWorldViewProjMtx: Any
    kWorldViewProjTranspInverseMtx: Any
    kWorldViewProjTransposeMtx: Any
    kWorldViewTranspInverseMtx: Any
    kWorldViewTransposeMtx: Any
    kXray: Any
    kXrayActiveComponents: Any
    kXrayJoint: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def classificationExclusions(self) -> Any:
        """Get a list of drawdb strings for object which are excluded from display"""
    def getBackgroundParameters(self) -> Any:
        """Get parameters related to how the background is cleared"""
    def getCurrentCameraPath(self) -> MDagPath:
        """Get the path to the camera being used to render the current frame."""
    def getCurrentColorRenderTarget(self) -> MRenderTarget:
        """Get current color render target."""
    def getCurrentDepthRenderTarget(self) -> MRenderTarget:
        """Get current depth render target."""
    def getDOFParameters(self) -> Any:
        """Get the parameters generated by Maya for the circle-of-confusion depth shader used"""
    def getDisplayStyle(self) -> int:
        """The DisplayStyle enums can be use to test the bit field for the enabling of any"""
    def getEnvironmentParameters(self) -> Any:
        """Get parameters for currently used environment. Note that this information is set"""
    def getGlobalLineWidth(self) -> float:
        """Get global line width."""
    def getHwFogParameters(self) -> Any:
        """Get all the hardware fog parameters."""
    def getLightLimit(self) -> int:
        """Get the current light limit."""
    def getLightingMode(self) -> int:
        """Get the current light mode."""
    def getMatrix(self, int: Any) -> MMatrix:
        """Get a matrix value of a certain type."""
    def getPostEffectEnabled(self, int: Any) -> bool:
        """Returns if a given post effect is currently enabled."""
    def getRenderOverrideInformation(self) -> Any:
        """Get information about any render override"""
    def getTransparencyAlgorithm(self) -> int:
        """Get the current transparency algoritm."""
    def getTuple(self, int: Any) -> MDoubleArray:
        """Get a tuple (vector, position or single) value of a certain type."""
    def getViewportDimensions(self) -> Any:
        """Get the viewport dimensions. The origin is the upper left corner of the viewport."""
    @staticmethod
    def inUserInteraction() -> bool:
        """Returns True during any interactive refresh, as when user is interacting with the scene"""
    def objectTypeExclusions(self) -> int:
        """Get the object type exclusions as a bitfield."""
    def renderingDestination(self) -> Any:
        """Return the destination (type and name) that the renderer is drawing to."""
    @staticmethod
    def semanticToMatrixType(string: Any) -> int:
        """Given a semantic name return the corresponding matrix enumeration that can be used to retrieve a matrix value via the getMatrix() method."""
    @staticmethod
    def semanticToTupleType(string: Any) -> int:
        """Given a semantic name return the corresponding tuple enumeration that can be used to retrieve a value via the getTuple() method."""
    @staticmethod
    def shadeTemplates() -> bool:
        """Returns the display preference indicating whether templated objects should be drawn shaded."""
    @staticmethod
    def userChangingViewContext() -> bool:
        """Returns True during any interactive refresh, as when user is	changing the view using view context"""
    @staticmethod
    def wireOnShadedMode() -> int:
        """Returns the global user display preference which indicates how wireframe should be drawn on top of objects while in shaded mode."""

class MGeometry:
    kAdjacentLineStrip: Any
    kAdjacentLines: Any
    kAdjacentTriangleStrip: Any
    kAdjacentTriangles: Any
    kAll: Any
    kBitangent: Any
    kBoundingBox: Any
    kChar: Any
    kColor: Any
    kDouble: Any
    kFloat: Any
    kInt16: Any
    kInt32: Any
    kInvalidPrimitive: Any
    kInvalidSemantic: Any
    kInvalidType: Any
    kLineStrip: Any
    kLines: Any
    kNormal: Any
    kPatch: Any
    kPoints: Any
    kPosition: Any
    kSelectionHighlighting: Any
    kSelectionOnly: Any
    kShaded: Any
    kTangent: Any
    kTangentWithSign: Any
    kTexture: Any
    kTextured: Any
    kTriangleStrip: Any
    kTriangles: Any
    kUnsignedChar: Any
    kUnsignedInt16: Any
    kUnsignedInt32: Any
    kWireframe: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addIndexBuffer(self, MIndexBuffer: Any) -> bool:
        """Buffers cannot be added to the same object twice.Adds a index buffer to this MGeometry object."""
    def addVertexBuffer(self, MVertexBuffer: Any) -> bool:
        """Adds a vertex buffer to this MGeometry object."""
    def createIndexBuffer(self, int: Any) -> MIndexBuffer:
        """Creates a index buffer which is bound to this MGeometry object and cannot be used with any other."""
    def createVertexBuffer(self, MVertexBufferDescriptor: Any) -> MVertexBuffer:
        """Creates a vertex buffer which is bound to this MGeometry object and cannot be used with any other."""
    @staticmethod
    def dataTypeString(int: Any) -> Any:
        """Get the string name (e.g. 'Unsigned Char') for the following data type values:"""
    def deleteIndexBuffer(self, int: Any) -> bool:
        """Remove a index buffer from this object."""
    def deleteVertexBuffer(self, int: Any) -> bool:
        """Remove a vertex buffer from this object."""
    @staticmethod
    def drawModeString(int: Any) -> Any:
        """Get the string name (e.g. 'Wireframe, Shaded, Textured') for a combination of the following draw mode values:"""
    def indexBuffer(self, int: Any) -> MIndexBuffer:
        """Get the index buffer stored at the given index."""
    def indexBufferCount(self) -> int:
        """Get the number of index buffers contained in this MGeometry object."""
    @staticmethod
    def primitiveString(int: Any) -> Any:
        """Get the string name (e.g. 'Triangles') for the following primitive values:"""
    @staticmethod
    def semanticString(int: Any) -> Any:
        """Get the string name (e.g. 'Color') for the following semantic values:"""
    def vertexBuffer(self, int: Any) -> MVertexBuffer:
        """Get the vertex buffer stored at the given index."""
    def vertexBufferCount(self) -> int:
        """Get the number of vertex buffers contained in this MGeometry object."""

class MGeometryExtractor:
    kPolyGeom_BaseMesh: Any
    kPolyGeom_Normal: Any
    kPolyGeom_NotSharing: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def minimumBufferSize(primitiveCount: Any, primitive: Any, primitiveStride: int = 0) -> int:
        """Get the minimum buffer size required by populateIndexBuffer()."""
    def populateIndexBuffer(self, data: Any, primitiveCount: Any, indexDesc: Any) -> MGeometryExtractor:
        """Fill a buffer with geometry indexing data."""
    def populateVertexBuffer(self, data: Any, vertexCount: Any, bufferDesc: Any) -> MGeometryExtractor:
        """Fill a buffer with vertex data."""
    def primitiveCount(self, indexDesc: Any) -> int:
        """Returns the number of primitives (triangles, lines, points, etc.) that will be produced for the given indexing requirements."""
    def vertexCount(self) -> int:
        """Returns the number of vertices that will be produced for the vertex requirement."""

class MGeometryIndexMapping:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def component(self, int: Any) -> MObject:
        """Get the component of a geometry."""
    def dagPath(self, int: Any) -> MDagPath:
        """Get the MDagPath of a geometry."""
    def geometryCount(self) -> int:
        """Get the number of geometry described by the mapping."""
    def indexLength(self, int: Any) -> int:
        """Get the index length of a geometry."""
    def indexStart(self, int: Any) -> int:
        """Get the index start of a geometry."""

class MGeometryRequirements:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addIndexingRequirement(self, MIndexBufferDescriptor: Any) -> MGeometryRequirements:
        """Add a new indexing requirement to the list of indexing requirements."""
    def addVertexRequirement(self, MVertexBufferDescriptor: Any) -> MGeometryRequirements:
        """Add a new vertex requirement to the list of vertex requirements."""
    def indexingRequirements(self) -> MIndexBufferDescriptorList:
        """Get a list of descriptors that specify the geometry indexing requirements of an object."""
    def vertexRequirements(self) -> MVertexBufferDescriptorList:
        """Get a list of descriptors that specify the vertex geometry requirements of this object."""

class MGeometryUtilities:
    kActive: Any
    kActiveAffected: Any
    kActiveComponent: Any
    kActiveTemplate: Any
    kDefaultCube: Any
    kDefaultPlane: Any
    kDefaultSphere: Any
    kDormant: Any
    kHilite: Any
    kIntermediateObject: Any
    kInvisible: Any
    kLead: Any
    kLive: Any
    kNoStatus: Any
    kTemplate: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def acquireReferenceGeometry(shape: Any, requirements: Any) -> MGeometry:
        """Acquire reference geometry with required buffers."""
    @staticmethod
    def displayStatus(path: Any) -> Any:
        """Returns the display status of the given DAG path. Note that the last selected object will have status kLead"""
    @staticmethod
    def releaseReferenceGeometry(geometry: Any) -> None:
        """Release a generated reference geometry."""
    @staticmethod
    def wireframeColor(path: Any) -> MColor:
        """Returns the wireframe color used in Viewport 2.0 for the given DAG path."""

class MHUDRender:
    kClear: Any
    kDataServer: Any
    kHUDRender: Any
    kPresentTarget: Any
    kQuadRender: Any
    kSceneRender: Any
    kUserDefined: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addUIDrawables(self, drawManager2D: Any, frameContext: Any) -> MHUDRender:
        """Provides access to the 2D version of MUIDrawManager, which can be used to queue up operations to draw simple UI shapes like lines, circles, text, etc."""
    def enableSRGBWrite(self) -> bool:
        """Return whether to enable GPU based gamma correction during pixel writes."""
    def hasUIDrawables(self) -> bool:
        """Query whether addUIDrawables() should be called or not."""
    def name(self) -> Any:
        """Returns the unique name for a hud render operation."""
    def operationType(self) -> int:
        """Returns the type of a render operator."""
    def targetOverrideList(self) -> list[MRenderTarget]:
        """Return a list of render target which will be used as the target overrides for the operation."""
    def viewportRectangleOverride(self) -> MFloatPoint:
        """Query for a viewport rectangle override."""

class MIndexBuffer:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def acquire(self, size: Any, writeOnly: Any) -> int:
        """Get a pointer to memory for the buffer."""
    def commit(self, long: Any) -> MIndexBuffer:
        """Commit the data stored in the memory given by acquire() to the buffer."""
    def dataType(self) -> int:
        """Get the data type of the buffer."""
    def hasCustomResourceHandle(self) -> bool:
        """Returns true if this index buffer is using a custom resource handle set"""
    def lockResourceHandle(self) -> MIndexBuffer:
        """Lock the resource handle. The pointer returned from resourceHandle() is"""
    def map(self) -> int:
        """Get a read-only pointer to the existing content of the buffer."""
    def resourceHandle(self) -> int:
        """Returns a long containing a C++ 'float' pointer which points to the graphics device dependent handle to the vertex indexing data."""
    def setResourceHandle(self, long: Any, int: Any) -> Any: ...
    def size(self) -> int:
        """Get the size of the buffer in units of dataType(). Returns 0 if unallocated."""
    def unload(self) -> MIndexBuffer:
        """If the buffer is resident in GPU memory, calling this method will move it to system memory and free the GPU memory."""
    def unlockResourceHandle(self) -> MIndexBuffer:
        """Unlock the resource handle. The pointer returned from resourceHandle is not"""
    def unmap(self) -> MIndexBuffer:
        """Release the data exposed by map(). If this method is not called, the buffer will not be recycled."""
    def update(self, buffer: Any, destOffset: Any, numIndices: Any, truncateIfSmaller: Any) -> MIndexBuffer:
        """Set a portion (or all) of the contents of the MIndexBuffer using the data in the provided software buffer."""

class MIndexBufferDescriptor:
    component: Any
    dataType: Any
    indexType: Any
    kControlVertex: Any
    kCustom: Any
    kEdgeLine: Any
    kEditPoint: Any
    kFaceCenter: Any
    kHullEdgeCenter: Any
    kHullEdgeLine: Any
    kHullFaceCenter: Any
    kHullTriangle: Any
    kHullUV: Any
    kSubDivEdge: Any
    kTangent: Any
    kTriangle: Any
    kTriangleEdge: Any
    kVertexPoint: Any
    name: Any
    primitive: Any
    primitiveStride: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MIndexBufferDescriptorList:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def append(self, MIndexBufferDescriptor: Any) -> bool:
        """Add a descriptor to the list. Creates and stores a copy which is owned by the list."""
    def clear(self) -> MIndexBufferDescriptorList:
        """Clear the list."""
    def remove(self, index: Any) -> bool:
        """Remove a descriptor from the list and delete it."""

class MInitContext:
    dagPath: Any
    shader: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MInitFeedback:
    customData: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MIntersection:
    barycentricCoordinates: Any
    edgeInterpolantValue: Any
    index: Any
    instanceID: Any
    intersectionPoint: Any
    selectionLevel: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MLightParameterInformation:
    kBoolean: Any
    kColor: Any
    kCosConeAngle: Any
    kDecayRate: Any
    kDepthRange: Any
    kDropoff: Any
    kEmitsDiffuse: Any
    kEmitsSpecular: Any
    kFloat: Any
    kFloat2: Any
    kFloat3: Any
    kFloat4: Any
    kFloat4x4Col: Any
    kFloat4x4Row: Any
    kGlobalShadowOn: Any
    kInteger: Any
    kIntensity: Any
    kInvalid: Any
    kIrradianceIn: Any
    kLightEnabled: Any
    kNoSemantic: Any
    kSampler: Any
    kShadowBias: Any
    kShadowColor: Any
    kShadowDirty: Any
    kShadowMap: Any
    kShadowMapSize: Any
    kShadowOn: Any
    kShadowSamp: Any
    kShadowViewProj: Any
    kStartShadowParameters: Any
    kTexture2: Any
    kTextureCube: Any
    kWorldDirection: Any
    kWorldPosition: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def arrayParameterCount(self, string: Any) -> int:
        """Return the array size of a parameter. If the parameter is not an array then a value of 0 is returned."""
    def getParameter(self, arg: Any) -> MTexture:
        """Get parameter value by name or by semantic."""
    def getParameterTextureHandle(self, arg: Any) -> int:
        """Get a resource handle for a texture parameter by name or by semantic."""
    def lightPath(self) -> MDagPath:
        """Returns the DagPath to the scene light. Will return an unitialized DagPath for default lights."""
    def lightType(self) -> Any:
        """Get the classification of the light node."""
    def parameterList(self) -> list[Any]:
        """Get the names of all light parameters that are accessible."""
    def parameterNames(self, int: Any) -> list[Any]:
        """Get the name of all parameters on the light which are tagged with the stock semantic."""
    def parameterSemantic(self, string: Any) -> int:
        """Get the stock semantic for a named parameter:"""
    def parameterType(self, string: Any) -> int:
        """Get the type of the named parameter, returns kInvalid if parameter is not found."""

class MPassContext:
    kBeginRenderSemantic: Any
    kBeginSceneRenderSemantic: Any
    kColorPassSemantic: Any
    kCullBackSemantic: Any
    kCullFrontSemantic: Any
    kDOFPassSemantic: Any
    kDepthPassSemantic: Any
    kEndRenderSemantic: Any
    kEndSceneRenderSemantic: Any
    kMaterialOverrideSemantic: Any
    kMotionVectorPassSemantic: Any
    kNonPEPatternPassSemantic: Any
    kNormalDepthPassSemantic: Any
    kOpaqueGeometrySemantic: Any
    kOpaqueUISemantic: Any
    kPEPatternPassSemantic: Any
    kPostUIGeometrySemantic: Any
    kPreUIGeometrySemantic: Any
    kSelectionPassSemantic: Any
    kShadowPassSemantic: Any
    kTransparentGeometrySemantic: Any
    kTransparentPeelAndAvgSemantic: Any
    kTransparentPeelSemantic: Any
    kTransparentUISemantic: Any
    kTransparentWeightedAvgSemantic: Any
    kUIGeometrySemantic: Any
    kUserPassSemantic: Any
    kXrayUISemantic: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def hasShaderOverride(self) -> bool:
        """Return if there is a shader instance override set for the current pass."""
    def passIdentifier(self) -> Any:
        """Return the identifier for the pass context."""
    def passSemantics(self) -> list[Any]:
        """Return an array of semantics for the pass context."""
    def shaderOverrideInstance(self) -> MShaderInstance:
        """Return the shader instance override set for the current pass."""

class MPresentTarget:
    kCenterBuffer: Any
    kClear: Any
    kDataServer: Any
    kHUDRender: Any
    kLeftBuffer: Any
    kPresentTarget: Any
    kQuadRender: Any
    kRightBuffer: Any
    kSceneRender: Any
    kUserDefined: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def enableSRGBWrite(self) -> bool:
        """Return whether to enable GPU based gamma correction during pixel writes."""
    def name(self) -> Any:
        """Returns the name of the render operator."""
    def operationType(self) -> int:
        """Returns the type of a render operator."""
    def presentDepth(self) -> bool:
        """Query whether the present operation will display depth values."""
    def setPresentDepth(self, bool: Any) -> MPresentTarget:
        """Set whether the operation will present depth values."""
    def setTargetBackBuffer(self, int: Any) -> MPresentTarget:
        """Set the desired back-buffer to use on the output target."""
    def targetBackBuffer(self) -> int:
        """Query the desired back-buffer to use on the output target."""
    def targetOverrideList(self) -> list[MRenderTarget]:
        """Return a list of render target which will be used as the target overrides for the operation."""
    def viewportRectangleOverride(self) -> MFloatPoint:
        """Query for a viewport rectangle override."""

class MPxComponentConverter:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addIntersection(self, intersection: Any) -> MPxComponentConverter:
        """Maya calls this function for every selection hit on the render item."""
    def component(self) -> MObject:
        """Once all of the geometry hits have been passed to the converter through calls to addIntersection(), Maya will call this method to retrieve the components corresponding to those hits."""
    def initialize(self, renderItem: Any) -> MPxComponentConverter:
        """Maya calls this function to allow the converter to initialize itself for the selection on the given render item."""
    def selectionMask(self) -> MSelectionMask:
        """Maya calls this function to allow the converter to specify the type of components it can handle.."""

class MPxDrawOverride:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addUIDrawables(self, objPath: Any, drawManager: Any, frameContext: Any, data: Any) -> MPxDrawOverride:
        """Provides access to the MUIDrawManager, which can be used to queue up operations to draw simple UI shapes like lines, circles, text, etc."""
    def boundingBox(self, objPath: Any, cameraPath: Any) -> MBoundingBox:
        """Called by Maya whenever the bounding box of the drawable object is needed."""
    def disableInternalBoundingBoxDraw(self) -> bool:
        """Returns True to disable bounding box drawing. The default value is False."""
    def excludedFromPostEffects(self) -> bool:
        """Returns False to indicate inclusion in post effects. The default value is true."""
    def handleTraceMessage(self, message: Any) -> MPxDrawOverride:
        """When debug tracing is enabled via MPxDrawOverride::traceCallSequence(),"""
    def hasUIDrawables(self) -> bool:
        """Query whether 'addUIDrawables()' will be called or not."""
    def isBounded(self, objPath: Any, cameraPath: Any) -> bool:
        """Returns True if object is bounded."""
    def isTransparent(self) -> bool:
        """Returns True to indicate inclusion in transparency passes. The default value is false."""
    @staticmethod
    def pointSnappingActive() -> bool:
        """This utility function can be called by a draw override to query whether Viewport 2.0 selection has been launched to find points for snapping. If so, in order for the associated DAG object to participate,"""
    def prepareForDraw(self, objPath: Any, cameraPath: Any, frameContext: Any, oldData: Any) -> MUserData:
        """Called by Maya each time the object needs to be drawn. Any data needed from the Maya dependency graph must be retrieved and cached in this stage. It is invalid to pull data from the Maya dependency graph in the draw callback method and Maya may become unstable if that is attempted."""
    def refineSelectionPath(self, selectInfo: Any, hitItem: Any, path: Any, components: Any, objectMask: Any) -> bool:
        """This method is called during the hit test phase of the viewport 2.0 selection and is used to override the selected path, the selected components or simply reject the selection."""
    def supportedDrawAPIs(self) -> Any:
        """Returns the draw API supported by this override."""
    def traceCallSequence(self) -> bool:
        """This method allows a way for a plug-in to examine"""
    def transform(self, objPath: Any, cameraPath: Any) -> MMatrix:
        """Returns The world space transformation matrix."""
    def updateSelectionGranularity(self, path: Any, selectionContext: Any) -> MPxDrawOverride:
        """This is method is called during the pre-filtering phase of the viewport 2.0 selection and is used to setup the selection context of the given DAG object."""
    def userSelect(self, selectInfo: Any, drawContext: Any, objPath: Any, data: Any, selectionList: Any, worldSpaceHitPts: Any) -> bool:
        """This method is called during the hit test phase of Viewport 2.0 selection if wantUserSelection() returns true, in order to override the default hit test implementation for the associated DAG object. """
    def wantUserSelection(self) -> bool:
        """This method is called during the hit test phase of Viewport 2.0 selection and is used to indicate whether or not the userSelect() method should be called to override the default hit test implementation for the associated DAG object. """

class MPxGeometryOverride:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addUIDrawables(self, path: Any, drawManager: Any, frameContext: Any) -> MPxGeometryOverride:
        """For each instance of the object, besides the render items updated in updateRenderItems() there is also a render item list for rendering simple UI elements."""
    def cleanUp(self) -> MPxGeometryOverride:
        """Called after all other stages are completed. Clean up any cached data stored from the updateDG() phase."""
    def configCache(self, evalNode: Any, schema: Any) -> None:
        """Defines the node's behavior when participating in Cached Playback."""
    def getFrameContext(self) -> MFrameContext:
        """Return a frame context. The context is not available if called before setup or after cleanup."""
    def handleTraceMessage(self, message: Any) -> MPxGeometryOverride:
        """When debug tracing is enabled via MPxGeometryOverride::traceCallSequence(),"""
    def hasUIDrawables(self) -> bool:
        """Query whether 'addUIDrawables()' will be called or not."""
    def isIndexingDirty(self, item: Any) -> bool:
        """Returns True if the index buffer needs to be updated."""
    def isStreamDirty(self, desc: Any) -> bool:
        """Returns True if the vertex buffer needs to be updated."""
    @staticmethod
    def pointSnappingActive() -> bool:
        """Returns True if selection has been launched to find snap points."""
    def populateGeometry(self, requirements: Any, renderItems: Any, data: Any) -> MPxGeometryOverride:
        """Implementations of this method should create and populate vertex and index buffers on the MGeometry instance 'data' in order to fulfill all of the geometry requirements defined by the 'requirements' parameter. Failure to do so will result in the object either drawing incorrectly or not drawing at all. See the documentation of MGeometryRequirements and MGeometry for more details on the usage of these classes. The geometry requirements will ask for index buffers on demand. Implementations can force the geometry requirements to update index buffers by calling MRenderer.setGeometryDrawDirty() with topologyChanged setting to True."""
    def refineSelectionPath(self, selectInfo: Any, hitItem: Any, path: Any, components: Any, objectMask: Any) -> bool:
        """This method is called during the hit test phase of the viewport 2.0 selection and is used to override the selected path, the selected components or simply reject the selection."""
    def requiresGeometryUpdate(self) -> bool:
        """This method is called one during each draw - preparation phase. If this method returns true then all of the other MPxGeometryOverride methods will be called for the associated DAG object this draw preparation phase.If this method returns false then all of the other MPxGeometryOverride methods may be called.This code has to be thread safe, non - blocking and work only on data owned by the associated DAG object."""
    def requiresUpdateRenderItems(self, path: Any) -> bool:
        """This method is called for each instance of the associated DAG object whenever the object changes.If, during a single draw - preparation phase this method returns false for all DAG instances of this MPxGeometryOverride then updateRenderItems() will not be called for the draw - preparation phase."""
    def supportedDrawAPIs(self) -> Any:
        """Returns the draw API supported by this override."""
    def supportsEvaluationManagerParallelUpdate(self) -> bool:
        """This method is called for each MPxGeometryOverride in the scene to determine if the MPxGeometryOverride is eligible for Evaluation Manager Parallel Update."""
    def supportsVP2CustomCaching(self) -> bool:
        """This method is called for each MPxGeometryOverride in the scene to determine if the MPxGeometryOverride is eligible for VP2 Evaluation Caching."""
    def traceCallSequence(self) -> bool:
        """This method allows a way for a plug-in to examine"""
    def updateDG(self) -> MPxGeometryOverride:
        """Perform any work required to translate the geometry data that needs to get information from the dependency graph.  This should be the only place that dependency graph evaluation occurs. Any data retrieved should be cached for later stages."""
    def updateRenderItems(self, path: Any, list: Any) -> MPxGeometryOverride:
        """This method is called for each instance of the associated DAG object whenever the object changes. The method is passed the path to the instance and the current list of render items associated with that instance. By default the list will contain one render item for each shader assigned to the instance. Implementations of this method method may add, remove or modify items in the list. Note that removal of items created by Maya for assigned shaders is not allowed and will fail. As an alternative this method can disable those items so that they do not draw."""
    def updateSelectionGranularity(self, path: Any, selectionContext: Any) -> MPxGeometryOverride:
        """This is method is called during the pre-filtering phase of the viewport 2.0 selection and is used to setup the selection context of the given DAG object."""

class MPxImagePlaneOverride:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def supportedDrawAPIs(self) -> Any:
        """Returns the draw API supported by this override."""

class MPxIndexBufferMutator:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def mutateIndexing(self, sourceIndexBuffers: Any, vertexBuffers: Any, arg: Any, int: Any) -> Any:
        """This method gets called to allow the generator to mutate the data for a custom index stream using information stored in the vertex buffers."""

class MPxPrimitiveGenerator:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def computeIndexCount(self, object: Any, component: Any) -> int:
        """This function is called to allow the primitive generator to provide the number of vertices it will use."""
    def generateIndexing(self, object: Any, component: Any, sourceIndexing: Any, targetIndexing: Any, arg: Any, int: Any) -> Any:
        """This method gets called to allow the generator to fill in the data for a custom index stream."""

class MPxShaderOverride:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def activateKey(self, context: Any, key: Any) -> MPxShaderOverride:
        """This is the activateKey callback."""
    def addGeometryRequirement(self, MVertexBufferDescriptor: Any) -> MPxShaderOverride:
        """During the initialization phase the geometry requirements for the shading effect can be updated. The update is"""
    def addGeometryRequirements(self, MVertexBufferDescriptorList: Any) -> MPxShaderOverride:
        """During the initialization phase the geometry requirements for the shading effect can be updated. The update is"""
    def addIndexingRequirement(self, MIndexBufferDescriptor: Any) -> MPxShaderOverride:
        """During the initialization phase the indexing requirements for the shading effect can be updated. The update is accomplished by"""
    def addShaderSignature(self, signature: Any, arg: Any) -> MPxShaderOverride:
        """During the initialization phase, the "signature" for the shader may be set. Certain Draw APIs (like DirectX 11) require a"""
    def boundingBoxExtraScale(self) -> float:
        """Returns the Extra scale factor."""
    def draw(self, context: Any, renderItemList: Any) -> bool:
        """This is the draw callback, the method is called during the draw phase."""
    def drawGeometry(self, MDrawContext: Any) -> MPxShaderOverride:
        """This method may be called from draw() and will cause Maya to immediately draw the current geometry using the current state of the draw API."""
    def endUpdate(self) -> MPxShaderOverride:
        """This is the final part of the update phase."""
    def handlesConsolidatedGeometry(self) -> bool:
        """Returns True if the shader instance should disable the consolidation"""
    def handlesDraw(self, context: Any) -> bool:
        """Returns True if shader handles drawing."""
    def initialize(self, shader: Any) -> Any:
        """initialize(initContext, initFeedback) -> string"""
    def initialize2(self, initContext: Any) -> Any:
        """Initialization occurs when Maya determines that the hardware shader needs to be rebuilt. Any initialization"""
    def isTransparent(self) -> bool:
        """Returns True if semi-transparent drawing should occur."""
    def nonTexturedShaderInstance(self, arg: Any, bool: Any) -> Any:
        """Returns an override shader instance to be used when drawing in non-textured"""
    def overridesDrawState(self) -> bool:
        """Returns True if the override overrides the draw state."""
    def overridesNonMaterialItems(self) -> bool:
        """Returns True if the shader instance should also be used to render non material items."""
    def rebuildAlways(self) -> bool:
        """Returns True if the shader and geometry should be rebuilt on every update."""
    def setGeometryRequirements(self, MShaderInstance: Any) -> MPxShaderOverride:
        """During the initialization phase the geometry requirements for the shading effect can be updated. The update can be"""
    def shaderInstance(self) -> MShaderInstance:
        """Returns the Shader instance."""
    def supportedDrawAPIs(self) -> Any:
        """Returns The draw API supported by this override."""
    def supportsAdvancedTransparency(self) -> bool:
        """Returns True if advanced tranparency algorithm is supported."""
    def terminateKey(self, context: Any, key: Any) -> MPxShaderOverride:
        """This is the terminateKey callback."""
    def updateDG(self, object: Any) -> MPxShaderOverride:
        """This is the first part of the update phase."""
    def updateDevice(self) -> MPxShaderOverride:
        """This is the second part of the update phase."""

class MPxShadingNodeOverride:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def allowConnections(self) -> bool:
        """Returns True if connections should be allowed to parameters of the fragment that do not have custom mappings that"""
    def fragmentName(self) -> Any:
        """Override this method to return the name of the fragment or fragment graph to use for rendering the shading node associated with this override. This fragment will be automatically connected to the other fragments for the other nodes in the shading network to produce a complete shading effect."""
    def getCustomMappings(self, mappings: Any) -> MPxShadingNodeOverride:
        """Maya will automatically match parameters on the shade fragment specified by this override with attributes on the"""
    def outputForConnection(self, sourcePlug: Any, destinationPlug: Any) -> Any:
        """Returns the name of an output parameter on the fragment for the override."""
    def supportedDrawAPIs(self) -> Any:
        """Returns the draw API supported by this override."""
    def updateDG(self) -> MPxShadingNodeOverride:
        """This method is called every time Maya needs to update the parameter values on the final shading effect of which the fragment"""
    def updateShader(self, shader: Any, mappings: Any) -> MPxShadingNodeOverride:
        """This method is called every time Maya needs to update the parameter values on the final shading effect of which the fragment"""
    def valueChangeRequiresFragmentRebuild(self, plug: Any) -> bool:
        """Returns True if a change in attribute values should cause a rebuild of the complete shading effect."""

class MPxSubSceneOverride:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addInstanceTransform(self, renderItem: Any, transform: Any) -> int:
        """Returns The instance ID for the new instance. This ID can be used to change the matrix or remove it. A return value of 0 indicates an error (render item does not support instancing or invalid state). 0 is never a valid instance ID."""
    def addUIDrawables(self, drawManager: Any, frameContext: Any) -> int:
        """Provides access to a MUIDrawManager, which can be used to queue upoperations to draw simple UI shapes like lines, circles, text, etc.If you override this method you must also override hasUIDrawables()to return true, otherwise this method will not be called.If you are not going to override this function, please don't make 'hasUIDrawables()' return trueor there may be some wasted performance overhead.By default the drawables will persist until either the DAG object associated with the overrideis destroyed or the override is deregistered.If you don't want them to be redrawn on each refresh,override areUIDrawablesDirty() to return false.That will cause the drawables to be destroyedon next refresh and this method called again to replace them."""
    def areUIDrawablesDirty(self) -> bool:
        """Determines whether addUIDrawables() should be called on the next refresh."""
    def furtherUpdateRequired(self, frameContext: Any) -> bool:
        """Returns True if further update is required. The default value return is False."""
    def getInstancedSelectionPath(self, renderItem: Any, intersection: Any, dagPath: Any) -> bool:
        """Returns True if a dag path was found for the instantiable render item."""
    def getSelectionPath(self, renderItem: Any, dagPath: Any) -> bool:
        """Returns True if a dag path was found for the render item."""
    def hasUIDrawables(self) -> bool:
        """Return Whether addUIDrawables() will be called or not."""
    @staticmethod
    def pointSnappingActive() -> bool:
        """Returns True if selection has been launched to find snap points."""
    def removeAllInstances(self, renderItem: Any) -> MPxSubSceneOverride:
        """Remove all instances for a render item. This render item will remain set up for instancing and will render nothing until new instances are added."""
    def removeExtraInstanceData(self, renderItem: Any, parameterName: Any) -> MPxSubSceneOverride:
        """Remove an entire extra instance data stream from the instanced render item."""
    def removeInstance(self, renderItem: Any, instanceId: Any) -> MPxSubSceneOverride:
        """Remove one instance of a render item."""
    def requiresUpdate(self, container: Any, frameContext: Any) -> bool:
        """On each frame Maya will give each instantiated MPxSubSceneOverride object a chance to update its set of render items. Before beginning the update process for a specific override, Maya will first call this method to give the override a chance to indicate whether or not an update is necessary. If this method returns False, MPxSubSceneOverride.update() will not be called."""
    def setAllowTransparentInstances(self, renderItem: Any, transform: Any) -> int:
        """Instancing is disabled automatically by default when the shader is transparent.This achieves the best appearance because Maya can sort individual instances."""
    def setExtraInstanceData(self, renderItem: Any, parameterName: Any, data: Any, instanceId: Any = None) -> MPxSubSceneOverride:
        """Adds an extra stream of instanced data to an instanced render item. Once a render item has been instanced, additional per-instance data may be bound to a parameter on the shader for that item. Supported shader parameter types for instanced data include: float, float2, float3 and float4. Once a stream of instanced data is specified for a shader parameter, the original value of that parameter will be ignored in favor of the per-instance data specified in this method."""
    def setGeometryForRenderItem(self, renderItem: Any, vertexBuffers: Any, indexBuffer: Any = None, objectBox: Any = None) -> MPxSubSceneOverride:
        """Call this method to provide the geometry for a render item. Although the render item will add a reference to each buffer, ultimate ownership of the geometric data remains with the caller. This method may only be called on render items which have been generated by this override and it may only be called during update(). Buffers may be shared among multiple render items. This method will replace any geometry currently associated with the render item with the newly provided geometry."""
    def setInstanceTransformArray(self, renderItem: Any, matrixArray: Any) -> MPxSubSceneOverride:
        """Sets the entire instance array for a render item.  Will convert the MRenderItem to instanced rendering if not already done.  Any pre-existing instances will be removed. The render item should already have it's other properties set (including shader and geometry). A render item converted to instanced rendering will ignore its typical matrix from setMatrix()."""
    def supportedDrawAPIs(self) -> Any:
        """Returns the draw API supported by this override."""
    def update(self, container: Any, frameContext: Any) -> MPxSubSceneOverride:
        """This method is called by Maya on each frame as long as the implementation of MPxSubSceneOverride.requiresUpdate() returns True. In this method, the MSubSceneContainer should be populated with the render items that are required to draw the associated DAG object. The render items will remain in the container until they are explicitly removed or the associated object is deleted. Render items in the container may also be modified at this time. """
    def updateInstanceTransform(self, renderItem: Any, instanceId: Any, transform: Any) -> MPxSubSceneOverride:
        """Update the instance transform matrix for one instance of a render item."""
    def updateSelectionGranularity(self, path: Any, selectionContext: Any) -> MPxSubSceneOverride:
        """This method is called during the pre-filtering phase of the viewport 2.0 selection and is used to allow derived classes to modify the selection context of the given DAG object."""

class MPxSurfaceShadingNodeOverride:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def allowConnections(self) -> bool:
        """Returns True if connections should be allowed to parameters of the fragment that do not have custom mappings that"""
    def bumpAttribute(self) -> Any:
        """Returns the name of the attribute that accepts bump connections from bump nodes."""
    def fragmentName(self) -> Any:
        """Override this method to return the name of the fragment or fragment graph to use for rendering the shading node associated with this override. This fragment will be automatically connected to the other fragments for the other nodes in the shading network to produce a complete shading effect."""
    def getCustomMappings(self, mappings: Any) -> MPxSurfaceShadingNodeOverride:
        """Maya will automatically match parameters on the shade fragment specified by this override with attributes on the"""
    def outputForConnection(self, sourcePlug: Any, destinationPlug: Any) -> Any:
        """Returns the name of an output parameter on the fragment for the override."""
    def primaryColorParameter(self) -> Any:
        """Returns the name of the fragment parameter to use as the primary color."""
    def supportedDrawAPIs(self) -> Any:
        """Returns the draw API supported by this override."""
    def transparencyParameter(self) -> Any:
        """Returns the name of the fragment parameter that should drive transparency."""
    def updateDG(self) -> MPxSurfaceShadingNodeOverride:
        """This method is called every time Maya needs to update the parameter values on the final shading effect of which the fragment"""
    def updateShader(self, shader: Any, mappings: Any) -> MPxSurfaceShadingNodeOverride:
        """This method is called every time Maya needs to update the parameter values on the final shading effect of which the fragment"""
    def valueChangeRequiresFragmentRebuild(self, plug: Any) -> bool:
        """Returns True if a change in attribute values should cause a rebuild of the complete shading effect."""

class MPxVertexBufferGenerator:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def createVertexStream(self, object: Any, vertexBuffer: Any, targetIndexing: Any, sharedIndexing: Any, sourceStreams: Any) -> MPxVertexBufferGenerator:
        """This method gets called to allow the generator to fill in the data for a custom vertex stream. Use the requirements in the vertexBuffer to get the description of the stream. Use vertexBuffer.acquire() and vertexBuffer.commit() to fill the buffer. """
    def getSourceIndexing(self, object: Any, sourceIndexing: Any) -> MPxVertexBufferGenerator:
        """This function is called to allow the vertex buffer generator to provide its vertex indexing information as well as the space the vertices are in.  The indexing and the component type are stored in the  sourceIndexing argument.  This indexing information is to allow the system to identify any potential  vertex sharing that is common across all vertex requirements. """
    def getSourceStreams(self, object: Any, sourceStreams: Any) -> MPxVertexBufferGenerator:
        """This function is called to allow the vertex buffer generator to provide the list of stream names that it requires. The names will be used to fill the array of vertex buffers that will be passed to createVertexStream. """

class MPxVertexBufferMutator:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def modifyVertexStream(self, object: Any, vertexBuffer: Any, targetIndexing: Any) -> MPxVertexBufferMutator:
        """This method gets called to allow the mutator to alter the data for a custom vertex stream."""

class MQuadRender:
    kClear: Any
    kDataServer: Any
    kHUDRender: Any
    kPresentTarget: Any
    kQuadRender: Any
    kSceneRender: Any
    kUserDefined: Any
    mClearOperation: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def blendStateOverride(self) -> MBlendState:
        """Query if a blend state override is performed by this quad operation."""
    def clearOperation(self) -> MClearOperation:
        """Get the scene clear operation."""
    def depthStencilStateOverride(self) -> MDepthStencilState:
        """Query if a depth-stencil state override is performed by this quad operation."""
    def enableSRGBWrite(self) -> bool:
        """Return whether to enable GPU based gamma correction during pixel writes."""
    def name(self) -> Any:
        """Returns the name of the render operator."""
    def operationType(self) -> int:
        """Returns the type of a render operator."""
    def rasterizerStateOverride(self) -> MRasterizerState:
        """Query if a rasterizer state override is performed by this quad operation."""
    def shader(self) -> MShaderInstance:
        """Get the shader to use when rendering a quad."""
    def targetOverrideList(self) -> list[MRenderTarget]:
        """Return a list of render target which will be used as the target overrides for the operation."""
    def viewportRectangleOverride(self) -> MFloatPoint:
        """Query for a viewport rectangle override."""

class MRasterizerState:
    kCullBack: Any
    kCullFront: Any
    kCullNone: Any
    kFillSolid: Any
    kFillWireFrame: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def desc(self) -> MRasterizerStateDesc:
        """Get the rasterizer state descriptor that was used to create the state object."""
    def resourceHandle(self) -> int:
        """Returns a long containing a C++ 'void' pointer which points to the draw API dependent handle for a rasterizer state."""

class MRasterizerStateDesc:
    antialiasedLineEnable: Any
    cullMode: Any
    depthBias: Any
    depthBiasClamp: Any
    depthBiasIsFloat: Any
    depthClipEnable: Any
    fillMode: Any
    frontCounterClockwise: Any
    multiSampleEnable: Any
    scissorEnable: Any
    slopeScaledDepthBias: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def setDefaults(self) -> MRasterizerStateDesc:
        """Set all values for the rasterizer state to their default values."""

class MRenderItem:
    DecorationItem: Any
    DrawOnlyWhenDefaultMaterialActive: Any
    IgnoreDefaultMaterialMode: Any
    InternalItem: Any
    InternalMaterialItem: Any
    InternalTexturedMaterialItem: Any
    InternalUnsupportedMaterialItem: Any
    MaterialSceneItem: Any
    NonMaterialSceneItem: Any
    OverrideNonMaterialItem: Any
    SkipWhenDefaultMaterialActive: Any
    sActiveLineDepthPriority: Any
    sActivePointDepthPriority: Any
    sActiveWireDepthPriority: Any
    sDormantFilledDepthPriority: Any
    sDormantPointDepthPriority: Any
    sDormantWireDepthPriority: Any
    sHiliteWireDepthPriority: Any
    sSelectionDepthPriority: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def allowIsolateSelectCopy(self) -> bool:
        """Returns whether or not the render item allows its copies to be created forthe drawing of isolate selected components."""
    def associateWithIndexBuffer(self, MIndexBuffer: Any) -> bool:
        """Use to indicate that a particular index buffer should be used with this render item."""
    def availableShaderParameters(self) -> list[Any]:
        """Returns the list of available shader parameters."""
    def boundingBox(self, space: Any) -> MBoundingBox:
        """Returns the bounding box for the geometry data of the render item."""
    def castsShadows(self) -> bool:
        """Get the castsShadows state of the render item."""
    def component(self) -> MObject:
        """Get the optional component for the render item if the render item representsthe drawing of a component as a result of per - face shader assignment, componentselection highlighting etc."""
    @staticmethod
    def create(name: Any, type: Any, primitive: Any) -> MRenderItem:
        """create(item) -> MRenderItem"""
    def customData(self) -> MUserData:
        """Retrieve custom data from the render item, returns None if no such data has ever been set on the render item."""
    def depthPriority(self) -> int:
        """Get the depth priority of the render item."""
    @staticmethod
    def destroy(item: Any) -> None:
        """Static MRenderItem destruction utility."""
    def drawMode(self) -> int:
        """Get the draw mode for the render item."""
    def enable(self, bool: Any) -> MRenderItem:
        """Enable or disable the render item for rendering."""
    def excludedFromPostEffects(self) -> bool:
        """Get whether this item is excluded from post-effects like SSAO and depth-of-field."""
    def geometry(self) -> MGeometry:
        """Access full geometry data for the render item."""
    def getCustomData(self) -> MUserData:
        """Retrieve custom data from the render item, returns None if no such data has ever been set on the render item."""
    def getDefaultMaterialHandling(self) -> Any:
        """Returns whether or not this render item will draw when default material mode is active."""
    def getShader(self) -> MShaderInstance:
        """Get the shader used by this render item."""
    def getShaderParameters(self, name: Any) -> Any:
        """Get the value of a shader parameter."""
    def isCompatibleWithMayaInstancer(self) -> bool:
        """Returns whether or not this render item can be used as an instance object with Maya Instancer node."""
    def isConsolidated(self) -> bool:
        """Get the consolidated state of the render item."""
    def isEnabled(self) -> bool:
        """Get the enable state of the render item."""
    def isIsolateSelectCopy(self) -> bool:
        """Returns whether or not the render item is a copy created to represent thedrawing of an isolate selected component."""
    def isShaderFromNode(self) -> bool:
        """Return True if the shader instance was set by evaluating the shading network of"""
    def name(self) -> Any:
        """Get the name of the render item."""
    def objectTypeExclusionFlag(self) -> int:
        """Query the bit flag which is used in display filtering based on object types."""
    def primitive(self) -> int:
        """Get the primitive type drawn by the render item."""
    def primitiveAndStride(self) -> Any:
        """Get the primitive type drawn by the render item, as well as its stride."""
    def receivesShadows(self) -> bool:
        """Get the receivesShadows state of the render item."""
    def requiredVertexBuffers(self) -> MVertexBufferDescriptorList:
        """Get a list of vertex buffer descriptors that describe the buffers required to draw the given render item."""
    def selectionMask(self) -> MSelectionMask:
        """Get the render item selection mask."""
    def setAllowIsolateSelectCopy(self, bool: Any) -> MRenderItem:
        """When a 3D model view activates Isolate Select for components, Viewport 2.0will create and maintain necessary render items to represent the drawingof the isolate selected components specifically for that view. These renderitems are copies of their original items and thus have the same propertiesincluding name, type, primitive type, draw mode etc., but their shadingcomponents are filtered from the view selected set of that view."""
    def setBoundingBox(self, bounds: Any) -> MRenderItem:
        """Sets the bounding box for the render item."""
    def setCastsShadows(self, bool: Any) -> MRenderItem:
        """Set the castsShadows state of the render item."""
    def setCompatibleWithMayaInstancer(self, bool: Any) -> MRenderItem:
        """Set whether or not this render item can be used as an instance object with Maya Instancer node."""
    def setCustomData(self, MUserData: Any) -> MRenderItem:
        """Associate custom user data with this render item."""
    def setDefaultMaterialHandling(self, arg: Any) -> MRenderItem:
        """Set whether or not this object should be drawn when default material mode is active."""
    def setDepthPriority(self, int: Any) -> MRenderItem:
        """Set the depth priority of the render item."""
    def setDrawMode(self, int: Any) -> MRenderItem:
        """Set the draw mode for the render item."""
    def setExcludedFromPostEffects(self, bool: Any) -> MRenderItem:
        """Set whether this item should be excluded from post-effects like SSAO and depth-of-field."""
    def setMatrix(self, MMatrix: Any) -> bool:
        """Override the object to world transformation matrix to use when drawing this render item."""
    def setObjectTypeExclusionFlag(self, long: Any) -> MRenderItem:
        """Set a bit flag for use in display filtering based on object types. The"""
    def setPrimitive(self, int: Any, int_: Any) -> MRenderItem:
        """Set the primitive type of the render item. If it is kPatch, stride will be required to specify the number of control points per patch and the valid values are [1, 32]; otherwise stride won't be used."""
    def setReceivesShadows(self, bool: Any) -> MRenderItem:
        """Set the receivesShadows state of the render item."""
    def setSelectionMask(self, arg: Any) -> MRenderItem:
        """Set the render item selection mask."""
    def setShader(self, shader: Any, customStreamName: Any = None) -> bool:
        """Set shader to use when drawing this render item."""
    def setShaderFromNode(self, shaderNode: Any, shapePath: Any, linkLostCb: Any = None, linkLostUserData: Any = None, nonTextured: bool = False) -> MRenderItem:
        """Set shader to use when drawing this render item. If no shader is ever set this render item will not draw. This method sets the shader instance to a render item by evaluating the shading network of a surface shader node (either standard or custom) in the scene."""
    def setTreatAsTransparent(self, bool: Any) -> MRenderItem:
        """Set whether or not this object should be treated as a transparent item.Set this to true if the object has vertex colors with alpha or other inputsthat make it important to treat this object as if it were transparent."""
    def setWantConsolidation(self, bool: Any) -> MRenderItem:
        """Set whether or not this render item wants to participate in consolidation."""
    def setWantSubSceneConsolidation(self, bool: Any) -> MRenderItem:
        """Sets whether or not this render item is eligible for consolidation in sub scene overrides."""
    def shadingComponent(self) -> MObject:
        """Get the optional shading component for the render item. It is different fromthe component() method only when a view selected filter is applied."""
    def sourceDagPath(self) -> MDagPath:
        """Retrieve the MDagPath for the instance of the object that generated this render item."""
    def sourceIndexMapping(self) -> MGeometryIndexMapping:
        """Get the geometry index mapping of the objects contained by this consolidated render item."""
    def type(self) -> int:
        """Get the type of the render item."""
    def wantConsolidation(self) -> bool:
        """Return whether or not this render item wants to participate in consolidation."""
    def wantSubSceneConsolidation(self) -> bool:
        """Returns True if this render item is eligible for consolidation in sub scene overrides."""

class MRenderItemList:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def append(self, MVertexBufferDescriptor: Any) -> bool:
        """Add the item to the list. The list assumes ownership of the item."""
    def clear(self) -> MRenderItemList:
        """Clear the list."""
    def indexOf(self, name: Any) -> int:
        """indexOf(name, type) -> int"""
    def remove(self, index: Any) -> bool:
        """Remove the item at the specified index. Item is deleted."""

class MRenderOperation:
    kClear: Any
    kDataServer: Any
    kHUDRender: Any
    kPresentTarget: Any
    kQuadRender: Any
    kSceneRender: Any
    kUserDefined: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def enableSRGBWrite(self) -> bool:
        """Return whether to enable GPU based gamma correction during pixel writes."""
    def name(self) -> Any:
        """Returns the name of the render operator."""
    def operationType(self) -> int:
        """Returns the type of a render operator."""
    def targetOverrideList(self) -> list[MRenderTarget]:
        """Return a list of render target which will be used as the target overrides for the operation."""
    def viewportRectangleOverride(self) -> MFloatPoint:
        """Query for a viewport rectangle override."""

class MRenderOverride:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def cleanup(self) -> MRenderOverride:
        """Perform any cleanup required following the execution of render operations."""
    def getFrameContext(self) -> MFrameContext:
        """Return a frame context. The context is not available if called before setup() or after cleanup()."""
    def name(self) -> Any:
        """Returns the name of the override."""
    def nextRenderOperation(self) -> bool:
        """Iterate to the next operation. If there are no more operations then this method should return false."""
    def renderOperation(self) -> MRenderOperation:
        """Return the current operation being iterated over."""
    def select(self, frameContext: Any, selectInfo: Any, useDepth: Any, selectionList: Any, worldSpaceHitPts: Any) -> bool:
        """The method is called by Maya to override the default Viewport 2.0 selection. It returns false by default, meaning the default selection will be used. If an implementation returns true, selectionList and worldSpaceHitPts will be used to override the default selection."""
    def setup(self, destination: Any) -> MRenderOverride:
        """Perform any setup required before render operations are to be executed."""
    def startOperationIterator(self) -> bool:
        """Query if there are any operations to iterate over."""
    def supportedDrawAPIs(self) -> int:
        """Returns the draw APIs supported by this override."""
    def uiName(self) -> Any:
        """Returns the user interface name for the override."""

class MRenderParameters:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getParameter(self, parameterName: Any, bool: Any) -> MRenderParameters:
        """getParameter(parameterName, int) -> self"""
    def isArrayParameter(self, string: Any) -> bool:
        """Determine whether the named parameter is an array."""
    def parameterList(self) -> list[Any]:
        """Get the names of all parameters that are settable on this shader instance."""
    def parameterType(self, string: Any) -> int:
        """Get the type of the named parameter, returns kInvalid if parameter is not found."""
    def semantic(self, string: Any) -> Any:
        """Return the semantic for a named parameter."""
    def setArrayParameter(self, parameterName: Any, arg: Any, int: Any) -> MRenderParameters:
        """setArrayParameter(parameterName, sequence of int, int) -> self"""
    def setParameter(self, parameterName: Any, bool: Any) -> MRenderParameters:
        """setParameter(parameterName, int) -> self"""

class MRenderProfile:
    kMayaD3D: Any
    kMayaOpenGL: Any
    kMayaSoftware: Any
    def __init__(self) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addRenderer(self, arg: Any, version: float) -> MRenderProfile:
        """Add an internal renderer to this profile:"""
    def hasRenderer(self, arg: Any, version: float) -> bool:
        """Check if a Maya renderer is listed in this profile:"""
    def numberOfRenderers(self) -> int:
        """Return the number of renderers in this profile."""

class MRenderTarget:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def freeRawData(long: Any) -> None:
        """Deallocate system memory - retrieved from rawData()."""
    def rawData(self) -> Any:
        """Get a copy of the raw data mapped to the target."""
    def resourceHandle(self) -> int:
        """Returns a long containing a C++ 'void' pointer which points to the draw API dependent handle for a render target."""
    def targetDescription(self) -> MRenderTargetDescription:
        """Get target description."""
    def updateDescription(self, MRenderTargetDescription: Any) -> MRenderTarget:
        """Change the description of a render target."""

class MRenderTargetAssignment:
    target: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MRenderTargetDescription:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def allowsUnorderedAccess(self) -> bool:
        """Query whether unordered access is supported."""
    def arraySliceCount(self) -> int:
        """Query the number of array slices defined by the description."""
    def compatibleWithDescription(self, MRenderTargetDescription: Any) -> bool:
        """Determine if another target with a given description is 'compatible' with a target using this description."""
    def height(self) -> int:
        """Query the height of a 2D render target slice."""
    def isCubeMap(self) -> bool:
        """Query whether this is a cube map target."""
    def multiSampleCount(self) -> int:
        """Query the multi-sample count defined by the description."""
    def name(self) -> Any:
        """Query the name identifier for the target description."""
    def rasterFormat(self) -> int:
        """Query the raster format defined by the description."""
    def setAllowsUnorderedAccess(self, bool: Any) -> MRenderTargetDescription:
        """Set the flag for unordered data access for the target."""
    def setArraySliceCount(self, int: Any) -> MRenderTargetDescription:
        """Set array slice count of the target."""
    def setHeight(self, int: Any) -> MRenderTargetDescription:
        """Set height of the target."""
    def setIsCubeMap(self, bool: Any) -> MRenderTargetDescription:
        """Set cube map flag for the target."""
    def setMultiSampleCount(self, int: Any) -> MRenderTargetDescription:
        """Set multisample count of the target."""
    def setName(self, string: Any) -> MRenderTargetDescription:
        """Set name of the target."""
    def setRasterFormat(self, int: Any) -> MRenderTargetDescription:
        """Set the raster format of the target."""
    def setWidth(self, int: Any) -> MRenderTargetDescription:
        """Set width of the target."""
    def width(self) -> int:
        """Query the width of a 2D render target slice."""

class MRenderTargetManager:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def acquireRenderTarget(self, MRenderTargetDescription: Any) -> MRenderTarget:
        """Acquire an instance of a render target."""
    def acquireRenderTargetFromScreen(self, string: Any) -> MRenderTarget:
        """Acquire an instance of a render target with the same characteristics as the current on-screen target."""
    def formatSupportsSRGBWrite(self, int: Any) -> bool:
        """This method will perform a check to determine whether gamma correction can be performed"""
    def releaseRenderTarget(self, MRenderTarget: Any) -> MRenderTargetManager:
        """Deletes the MRenderTarget and releases the reference to the underlying target which is held by the MRenderTarget object."""

class MRenderUtilities:
    kAmbientLight: Any
    kDefaultLights: Any
    kOrthogonalCameraCloseUp: Any
    kOrthogonalCameraWithMargin: Any
    kPerspectiveCamera: Any
    kSwatchLight: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def acquireSwatchDrawContext() -> MDrawContext:
        """acquireSwatchDrawContext(colorTarget) -> MDrawContext"""
    @staticmethod
    def acquireUVTextureDrawContext() -> MDrawContext:
        """acquireUVTextureDrawContext(colorTarget) -> MDrawContext"""
    @staticmethod
    def blitTargetToGL(target: Any, region: Any, unfiltered: Any) -> None:
        """Blit the data from a target to current GL context."""
    @staticmethod
    def blitTargetToImage(target: Any, image: Any) -> None:
        """Copy the data from a target to an image."""
    @staticmethod
    def drawSimpleMesh(context: Any, vertexBuffer: Any, indexBuffer: Any, primitiveType: Any, start: Any, count: Any) -> None:
        """Render a simple mesh."""
    @staticmethod
    def releaseDrawContext(context: Any) -> None:
        """releaseDrawContext(context, releaseTargets) -> None"""
    @staticmethod
    def renderMaterialViewerGeometry(shape: Any, shaderNode: Any, image: Any, cameraMode: Any, lightRig: Any) -> None:
        """Do an off-screen render replicating the results shown by the Material Viewer window of Hypershade.."""
    @staticmethod
    def swatchBackgroundColor() -> MColor:
        """Returns the default background color for the hardware rendered swatch."""

class MRenderer:
    kA8: Any
    kA8B8G8R8: Any
    kAllDevices: Any
    kB5G5R5A1: Any
    kB5G6R5: Any
    kB8G8R8A8: Any
    kB8G8R8X8: Any
    kBC6H_SF16: Any
    kBC6H_UF16: Any
    kBC7_UNORM: Any
    kBC7_UNORM_SRGB: Any
    kD24S8: Any
    kD24X8: Any
    kD32_FLOAT: Any
    kDXT1_UNORM: Any
    kDXT1_UNORM_SRGB: Any
    kDXT2_UNORM: Any
    kDXT2_UNORM_PREALPHA: Any
    kDXT2_UNORM_SRGB: Any
    kDXT3_UNORM: Any
    kDXT3_UNORM_PREALPHA: Any
    kDXT3_UNORM_SRGB: Any
    kDXT4_SNORM: Any
    kDXT4_UNORM: Any
    kDXT5_SNORM: Any
    kDXT5_UNORM: Any
    kDirectX11: Any
    kL16: Any
    kL8: Any
    kNone: Any
    kNumberOfRasterFormats: Any
    kOpenGL: Any
    kOpenGLCoreProfile: Any
    kR10G10B10A2_UINT: Any
    kR10G10B10A2_UNORM: Any
    kR16G16B16A16_FLOAT: Any
    kR16G16B16A16_SINT: Any
    kR16G16B16A16_SNORM: Any
    kR16G16B16A16_UINT: Any
    kR16G16B16A16_UNORM: Any
    kR16G16_FLOAT: Any
    kR16G16_SINT: Any
    kR16G16_SNORM: Any
    kR16G16_UINT: Any
    kR16G16_UNORM: Any
    kR16_FLOAT: Any
    kR16_SINT: Any
    kR16_SNORM: Any
    kR16_UINT: Any
    kR16_UNORM: Any
    kR1_UNORM: Any
    kR24G8: Any
    kR24X8: Any
    kR32G32B32A32_FLOAT: Any
    kR32G32B32A32_SINT: Any
    kR32G32B32A32_UINT: Any
    kR32G32B32_FLOAT: Any
    kR32G32B32_SINT: Any
    kR32G32B32_UINT: Any
    kR32G32_FLOAT: Any
    kR32G32_SINT: Any
    kR32G32_UINT: Any
    kR32_FLOAT: Any
    kR32_SINT: Any
    kR32_UINT: Any
    kR8G8B8A8_SINT: Any
    kR8G8B8A8_SNORM: Any
    kR8G8B8A8_UINT: Any
    kR8G8B8A8_UNORM: Any
    kR8G8B8X8: Any
    kR8G8_SINT: Any
    kR8G8_SNORM: Any
    kR8G8_UINT: Any
    kR8G8_UNORM: Any
    kR8_SINT: Any
    kR8_SNORM: Any
    kR8_UINT: Any
    kR8_UNORM: Any
    kR9G9B9E5_FLOAT: Any
    @staticmethod
    def GPUDeviceHandle() -> int:
        """Returns a long containing a C++ 'void' pointer which points to the GPU "device".In the case that the drawing API is OpenGL then the "device" is a handle to an OpenGL context."""
    @staticmethod
    def GPUmaximumPrimitiveCount() -> int:
        """Returns the maximum number of primitives that can be drawn per draw call by the GPU device."""
    @staticmethod
    def GPUmaximumVertexBufferSize() -> int:
        """Returns the maximum number of vertices allowed in a vertex buffer by the GPU device."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def activeRenderOverride() -> Any:
        """Returns the name of the active override."""
    @staticmethod
    def copyTargetToScreen(MRenderTarget: Any) -> bool:
        """Copy a render target to the screen."""
    @staticmethod
    def deregisterOverride(MRenderOverride: Any) -> None:
        """Deregister an existing render override on the renderer."""
    @staticmethod
    def disableChangeManagementUntilNextRefresh() -> None:
        """Calling this method will cause Viewport 2.0 to stop processing all changes to the Maya scene until the next viewport refresh."""
    @staticmethod
    def drawAPI() -> int:
        """Returns the current drawing API. Returns 'kNone' if the renderer is not initialized."""
    @staticmethod
    def drawAPIIsOpenGL() -> bool:
        """Returns whether the current drawing API is OpenGL or not"""
    @staticmethod
    def drawAPIVersion() -> int:
        """Returns the version of drawing API."""
    @staticmethod
    def findRenderOverride(string: Any) -> MRenderOverride:
        """Returns a reference to an existing render override registered with the renderer."""
    @staticmethod
    def getFragmentManager() -> MFragmentManager:
        """Returns the fragment manager or None if the renderer is not initialized properly."""
    @staticmethod
    def getRenderTargetManager() -> MRenderTargetManager:
        """Returns the render target manager or None if the renderer is not initialized properly."""
    @staticmethod
    def getShaderManager() -> MShaderManager:
        """Returns the shader manager or None if the renderer is not initialized properly."""
    @staticmethod
    def getTextureManager() -> MTextureManager:
        """Returns the texture manager or None if the renderer is not initialized properly."""
    @staticmethod
    def needEvaluateAllLights() -> None:
        """Notify the Viewport 2.0 renderer that it should evaluate all lights marked dirty, regardless of the light limit.For example, if there are 8 lights accessible because of the Viewport 2.0 light limit option, Only the first 8 non-ambient lights created will be evaluated.Call this method to instruct Viewport 2.0 to evaluate all dirty lights regardless of the light limit option."""
    @staticmethod
    def outputTargetSize() -> Any:
        """Get target size in format [width, height]."""
    @staticmethod
    def registerOverride(MRenderOverride: Any) -> None:
        """Register the override as being usable by the renderer."""
    @staticmethod
    def render(sourceName: Any, targetList: Any) -> bool:
        """Render images from a panel to render targets."""
    @staticmethod
    def renderOverrideCount() -> int:
        """Returns the number of registered render overrides."""
    @staticmethod
    def renderOverrideName() -> Any:
        """Get the current render override name used for batch rendering."""
    @staticmethod
    def setGeometryDrawDirty(object: Any, topologyChanged: bool = True) -> None:
        """Notify the Viewport 2.0 renderer that the geometry (size, shape, etc.) of object has changed, causing the object to be updated in the viewport."""
    @staticmethod
    def setLightRequiresShadows(object: Any, flag: Any) -> bool:
        """This method allows for plug-in writers to indicate that the shadow map contents for a given light are required, regardless of the light limit."""
    @staticmethod
    def setLightsAndShadowsDirty() -> None:
        """Notify the Viewport 2.0 renderer that something has changed which requires re-evaluation of lighting and shadows."""
    @staticmethod
    def setRenderOverrideName(string: Any) -> bool:
        """Set the name of a render override (MRenderOverride) for batch rendering."""

class MSamplerState:
    kAnisotropic: Any
    kMinLinear_MagMipPoint: Any
    kMinLinear_MagPoint_MipLinear: Any
    kMinMagLinear_MipPoint: Any
    kMinMagMipLinear: Any
    kMinMagMipPoint: Any
    kMinMagPoint_MipLinear: Any
    kMinPoint_MagLinear_MipPoint: Any
    kMinPoint_MagMipLinear: Any
    kTexBorder: Any
    kTexClamp: Any
    kTexMirror: Any
    kTexWrap: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def desc(self) -> MSamplerStateDesc:
        """Get the sampler state descriptor that was used to create the state object."""
    def resourceHandle(self) -> int:
        """Returns a long containing a C++ 'void' pointer which points to the draw API dependent handle for a sampler state."""

class MSamplerStateDesc:
    addressU: Any
    addressV: Any
    addressW: Any
    borderColor: Any
    comparisonFn: Any
    coordCount: Any
    elementIndex: Any
    filter: Any
    maxAnisotropy: Any
    maxLOD: Any
    minLOD: Any
    mipLODBias: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def setDefaults(self) -> MSamplerStateDesc:
        """Set all values for the target blend state to their default values."""

class MSceneRender:
    kAmbientLight: Any
    kBoundingBox: Any
    kClear: Any
    kCullBackFaces: Any
    kCullFrontFaces: Any
    kCullNone: Any
    kDataServer: Any
    kDefaultMaterial: Any
    kExcludeAll: Any
    kExcludeCVs: Any
    kExcludeCameras: Any
    kExcludeDeformers: Any
    kExcludeDimensions: Any
    kExcludeDynamicConstraints: Any
    kExcludeDynamics: Any
    kExcludeFluids: Any
    kExcludeFollicles: Any
    kExcludeGrid: Any
    kExcludeHairSystems: Any
    kExcludeHoldOuts: Any
    kExcludeHulls: Any
    kExcludeIkHandles: Any
    kExcludeImagePlane: Any
    kExcludeJoints: Any
    kExcludeLights: Any
    kExcludeLocators: Any
    kExcludeManipulators: Any
    kExcludeMeshes: Any
    kExcludeMotionTrails: Any
    kExcludeNCloths: Any
    kExcludeNParticles: Any
    kExcludeNRigids: Any
    kExcludeNone: Any
    kExcludeNurbsCurves: Any
    kExcludeNurbsSurfaces: Any
    kExcludeParticleInstancers: Any
    kExcludePivots: Any
    kExcludePlanes: Any
    kExcludeSelectHandles: Any
    kExcludeStrokes: Any
    kExcludeSubdivSurfaces: Any
    kExcludeTextures: Any
    kFlatShaded: Any
    kHUDRender: Any
    kLightDefault: Any
    kNoCullingOverride: Any
    kNoDisplayModeOverride: Any
    kNoLight: Any
    kNoLightingModeOverride: Any
    kNoSceneFilterOverride: Any
    kPostEffectDisableAll: Any
    kPostEffectDisableDOF: Any
    kPostEffectDisableMotionBlur: Any
    kPostEffectDisableNone: Any
    kPostEffectDisableSSAO: Any
    kPresentTarget: Any
    kQuadRender: Any
    kRenderAllItems: Any
    kRenderNonShadedItems: Any
    kRenderOpaqueShadedItems: Any
    kRenderPostSceneUIItems: Any
    kRenderPreSceneUIItems: Any
    kRenderShadedItems: Any
    kRenderTransparentShadedItems: Any
    kRenderUIItems: Any
    kSceneLights: Any
    kSceneRender: Any
    kSelectedLights: Any
    kShadeActiveOnly: Any
    kShaded: Any
    kTextured: Any
    kUserDefined: Any
    kWireFrame: Any
    mClearOperation: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addPostUIDrawables(self, drawManager: Any, frameContext: Any) -> MSceneRender:
        """Provides access to the MUIDrawManager, which can be used to queue up operations to draw simple UI shapes like lines, circles, text, etc."""
    def addPreUIDrawables(self, drawManager: Any, frameContext: Any) -> MSceneRender:
        """Provides access to the MUIDrawManager, which can be used to queue up operations to draw simple UI shapes like lines, circles, text, etc."""
    def cameraOverride(self) -> MCameraOverride:
        """Query for a camera override."""
    def clearOperation(self) -> MClearOperation:
        """Get the scene clear operation."""
    def cullingOverride(self) -> int:
        """Query for a face culling override."""
    def displayModeOverride(self) -> int:
        """Query for any display mode override."""
    def enableSRGBWrite(self) -> bool:
        """Return whether to enable GPU based gamma correction during pixel writes."""
    def fragmentName(self) -> Any:
        """Query the name of the fragment used to render the scene."""
    def getObjectTypeExclusions(self) -> int:
        """Query for any object type exclusions."""
    def getParameters(self) -> MRenderParameters:
        """Method to return the operation's parameter set."""
    def hasUIDrawables(self) -> bool:
        """Query whether addUIDrawables() should be called or not."""
    def lightModeOverride(self) -> int:
        """Query for any lighting mode override."""
    def name(self) -> Any:
        """Returns the name of the render operator."""
    def objectSetOverride(self) -> MSelectionList:
        """Query for override for the set of objects to view."""
    def objectTypeExclusions(self) -> int:
        """Query for any object type exclusions."""
    def operationType(self) -> int:
        """Returns the type of a render operator."""
    def postEffectsOverride(self) -> int:
        """Query for post effects override."""
    def postRender(self) -> MSceneRender:
        """Method to allow for the operation to clean up itself after being executed."""
    def postSceneRender(self, context: Any) -> MSceneRender:
        """Method to allow for the operation to update itself after a scene rendering ends."""
    def preRender(self) -> MSceneRender:
        """Method to allow for the operation to update itself before being executed. In general this would be used to update any operation parameters."""
    def preSceneRender(self, context: Any) -> MSceneRender:
        """Method to allow for the operation to update itself before a scene rendering begins."""
    def renderFilterOverride(self) -> int:
        """Query which elements of a scene render will be drawn based on semantic meaning."""
    def shaderOverride(self) -> MShaderInstance:
        """Query for a scene level shader override."""
    def shadowEnableOverride(self) -> Any:
        """Query for shadow display override."""
    def targetOverrideList(self) -> list[MRenderTarget]:
        """Return a list of render target which will be used as the target overrides for the operation."""
    def viewportRectangleOverride(self) -> MFloatPoint:
        """Query for a viewport rectangle override."""

class MSelectionContext:
    kComponent: Any
    kEdge: Any
    kFace: Any
    kNone: Any
    kObject: Any
    kVertex: Any
    selectionLevel: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MSelectionInfo:
    alignmentMatrix: Any
    cursorPoint: Any
    isRay: Any
    isSingleSelection: Any
    localRay: Any
    pointSnapping: Any
    selectClosest: Any
    selectOnHilitedOnly: Any
    selectRect: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def selectForHilite(self, mask: Any) -> bool:
        """Given the selection mask, determines if this shape can be selected for the hilite list."""
    def selectable(self, mask: Any) -> bool:
        """Given the selection mask, determines if the shape is selectable."""
    def selectableComponent(self, displayed: Any, mask: Any) -> bool:
        """Given the selection mask, determines if the component is selectable."""

class MShaderCompileMacro:
    definition: Any
    name: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MShaderInstance:
    kAnisotropyShader: Any
    kAnisotropyShader2: Any
    kBoolean: Any
    kDisplacementPosShader: Any
    kFloat: Any
    kFloat2: Any
    kFloat3: Any
    kFloat4: Any
    kFloat4x4Col: Any
    kFloat4x4Row: Any
    kGeometryShader: Any
    kGlossShader: Any
    kGlossShader2: Any
    kInteger: Any
    kInvalid: Any
    kNormalShader: Any
    kNormalShader2: Any
    kPixelShader: Any
    kReflectanceShader: Any
    kReflectanceShader2: Any
    kRotationAngleShader: Any
    kRotationAngleShader2: Any
    kRoughnessShader: Any
    kRoughnessShader2: Any
    kSampler: Any
    kTexture1: Any
    kTexture2: Any
    kTexture3: Any
    kTextureCube: Any
    kVertexShader: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def activatePass(self, MDrawContext: Any, int: Any) -> MShaderInstance:
        """Activates the given pass of the shader."""
    def addColorManagementTextures(self) -> MShaderInstance:
        """Adds all the color management textures needed to render this shader instance."""
    def addInputFragment(self, fragmentName: Any, outputName: Any, inputName: Any, promotedInputName: Any = None) -> MShaderInstance:
        """Connect a fragment that has been registered with the fragment manager to an input on the existing MShaderInstance."""
    def addInputFragmentForMultiParams(self, fragmentName: Any, uniqueName: Any, outputNames: Any, inputNames: Any, invalidParameterIndices: Any = None, fragmentUsage: Any = None) -> MShaderInstance:
        """Connect a named fragment that has been registered with the MFragmentManager """
    def addOutputFragment(self, fragmentName: Any, inputName: Any) -> MShaderInstance:
        """Connect a fragment that has been registered with the fragment manager to an output on the existing MShaderInstance."""
    def annotation(self, parameterName: Any, annotationName: Any) -> Any:
        """Returns the value of a named parameter annotation."""
    def bind(self, MDrawContext: Any) -> MShaderInstance:
        """Binds the shader instance to the draw context, so that it is the active shader."""
    def clone(self) -> MShaderInstance:
        """Clone the shader. This will return a new MShaderInstance object which is identical to the existing shader."""
    def createShaderInstanceWithColorManagementFragment(self, inputColorSpace: Any) -> MShaderInstance:
        """Return a new shader instance with Color Management fragment added, which is based on the callee."""
    def getArraySize(self, string: Any) -> int:
        """Return the size of an array if it is an array. Returns 0 if it is not an array"""
    def getPassCount(self, MDrawContext: Any) -> int:
        """Returns the number of draw passes defined by the shader."""
    def isArrayParameter(self, string: Any) -> bool:
        """Determine whether the named parameter is an array."""
    def isTransparent(self) -> bool:
        """Return whether the shader will render with transparency."""
    def isVaryingParameter(self, string: Any) -> bool:
        """Return the true if a named parameter's values vary per vertex."""
    def parameterDefaultValue(self, parameterName: Any) -> Any:
        """Returns the default value of named parameter, None if no default value."""
    def parameterList(self) -> list[Any]:
        """Get the names of all parameters that are settable on this shader instance."""
    def parameterSemantic(self, parameterName: Any) -> Any:
        """Returns the semantic associated to a named parameter."""
    def parameterType(self, string: Any) -> int:
        """Get the type of the named parameter, returns kInvalid if parameter is not found."""
    def passAnnotation(self, pass_: Any, annotationName: Any) -> Any:
        """Returns the value of the current technique's pass annotation."""
    def postDrawCallback(self) -> Any:
        """Returns the post-draw callback function set for the this shader instance."""
    def preDrawCallback(self) -> Any:
        """Returns the pre-draw callback function set for the this shader instance."""
    def renameParameter(self, parameterName: Any, string: Any) -> MShaderInstance:
        """Rename a named parameter."""
    def requiredVertexBuffers(self, MVertexBufferDescriptorList: Any) -> MShaderInstance:
        """Get the vertex buffer descriptors that describe the buffers required"""
    def resourceName(self, parameterName: Any) -> Any:
        """Returns the resource name of a named texture parameter."""
    def semantic(self, string: Any) -> Any:
        """Return the semantic for a named parameter."""
    def setArrayParameter(self, parameterName: Any, arg: Any, int: Any) -> MShaderInstance:
        """setArrayParameter(parameterName, sequence of int, int) -> self"""
    def setAsVarying(self, parameterName: Any, bool: Any) -> MShaderInstance:
        """Set whether the named parameter's values will vary per vertex."""
    def setIsTransparent(self, bool: Any) -> MShaderInstance:
        """Set whether the shader will render with transparency."""
    def setParameter(self, parameterName: Any, bool: Any) -> MShaderInstance:
        """setParameter(parameterName, int) -> self"""
    def setSemantic(self, parameterName: Any, string: Any) -> MShaderInstance:
        """Set the semantic of a named parameter."""
    def techniqueAnnotation(self, annotationName: Any) -> Any:
        """Returns the value of the current technique annotation."""
    def techniqueNames(self) -> list[str]:
        """Returns a list of the technique names for the effect."""
    def uiName(self, parameterName: Any) -> Any:
        """Returns the UI name associated with a named parameter."""
    def uiWidget(self, parameterName: Any) -> Any:
        """Returns the UI widget type associated with a named parameter."""
    def unbind(self, MDrawContext: Any) -> MShaderInstance:
        """Unbinds the shader instance from the draw context."""
    def updateParameters(self, MDrawContext: Any) -> MShaderInstance:
        """Updates the bound shader instance with the current parameter data."""
    def writeEffectSourceToFile(self, filePath: Any) -> MShaderInstance:
        """Write the source of the final OGSFX/HLSL/CgFX effect to a specified file. Use"""

class MShaderManager:
    k3dBlinnShader: Any
    k3dCPVDashLineShader: Any
    k3dCPVFatPointShader: Any
    k3dCPVShader: Any
    k3dCPVSolidShader: Any
    k3dCPVThickDashLineShader: Any
    k3dCPVThickLineShader: Any
    k3dColorLookupFatPointShader: Any
    k3dColorOpacityLookupFatPointShader: Any
    k3dDashLineShader: Any
    k3dDefaultMaterialShader: Any
    k3dDepthShader: Any
    k3dFatPointShader: Any
    k3dFloat2NumericShader: Any
    k3dFloat3NumericShader: Any
    k3dFloatNumericShader: Any
    k3dIntegerNumericShader: Any
    k3dIsotropicStandardSurfaceShader: Any
    k3dOpacityLookupFatPointShader: Any
    k3dPointLightShadowerShader: Any
    k3dPointVectorShader: Any
    k3dShadowerShader: Any
    k3dSolidShader: Any
    k3dSolidTextureShader: Any
    k3dStandardSurfaceShader: Any
    k3dStippleShader: Any
    k3dThickDashLineShader: Any
    k3dThickLineShader: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addShaderIncludePath(self, string: Any) -> MShaderManager:
        """Add a path to the list of paths used for searching for shader include files."""
    def addShaderPath(self, string: Any) -> MShaderManager:
        """Add a path to the list of shader search paths."""
    def clearEffectCache(self) -> MShaderManager:
        """Clear the effect cache."""
    def getEffectsBufferShader(self, buffer: Any, size: Any, techniqueName: Any, macros: Any = None, useEffectCache: bool = True, preCb: Any = None, postCb: Any = None) -> MShaderInstance:
        """Get a new instance of a shader generated from a block of memory containing device-specific source code (as char*)."""
    def getEffectsFileShader(self, effecsFileName: Any, techniqueName: Any, macros: Any = None, useEffectCache: bool = True, preCb: Any = None, postCb: Any = None) -> MShaderInstance:
        """Get a new instance of a shader generated from an effects file stored on disk."""
    def getEffectsTechniques(self, effecsFileName: Any, macros: Any = None, useEffectCache: bool = True) -> tuple[Any]:
        """Analyzes a given effect file to extract the names of the techniques that are defined."""
    def getFragmentShader(self, fragmentName: Any, structOutputName: Any, decorateFragment: Any, preCb: Any = None, postCb: Any = None) -> MShaderInstance:
        """Get a new instance of a shader generated from a named shader fragment or fragment graph."""
    @staticmethod
    def getLastError() -> Any:
        """Get the description of the last error encountered by the shader manager regarding an effect."""
    @staticmethod
    def getLastErrorSource(displayLineNumber: bool = False, filterSource: bool = False, numSurroundingLines: int = 2) -> Any:
        """Get the source of the shader that generated the last error. See getLastError()."""
    def getShaderFromNode(self, shaderNode: Any, shapePath: Any, linkLostCb: Any = None, linkLostUserData: Any = None, preCb: Any = None, postCb: Any = None, nonTextured: bool = False) -> MShaderInstance:
        """Get the shader instance by evaluating the shading network of a surface shader node (either standard or custom) in the scene."""
    def getStockShader(self, shaderId: Any, preCb: Any = None, postCb: Any = None) -> MShaderInstance:
        """Get a new instance of a stock shader."""
    @staticmethod
    def isSupportedShaderSemantic(string: Any) -> bool:
        """Return if a given string is a supported shader semantic."""
    def releaseShader(self, MShaderInstance: Any) -> None:
        """Deletes the MShaderInstance and releases its reference to the underlying shader which is held by the MShaderInstance object."""
    def removeEffectFromCache(self, effecsFileName: Any, techniqueName: Any, macros: Any = None) -> MShaderManager:
        """Remove an effect from the cache."""
    def shaderIncludePaths(self) -> list[str]:
        """Query the list of search paths user for searching for shader include files."""
    def shaderPaths(self) -> list[str]:
        """Query the list of shader search paths."""

class MStateManager:
    kCompareAlways: Any
    kCompareEqual: Any
    kCompareGreater: Any
    kCompareGreaterEqual: Any
    kCompareLess: Any
    kCompareLessEqual: Any
    kCompareNever: Any
    kCompareNotEqual: Any
    kDomainShader: Any
    kGeometryShader: Any
    kHullShader: Any
    kNoShader: Any
    kPixelShader: Any
    kVertexShader: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def acquireBlendState(MBlendStateDesc: Any) -> MBlendState:
        """Acquires an immutable unique blend state matching the blend state descriptor."""
    @staticmethod
    def acquireDepthStencilState(MDepthStencilStateDesc: Any) -> MDepthStencilState:
        """Acquires an immutable unique depth-stencil state matching the blend state descriptor."""
    @staticmethod
    def acquireRasterizerState(MRasterizerStateDesc: Any) -> MRasterizerState:
        """Acquires an immutable unique rasterizer state matching the rasterizer state descriptor."""
    @staticmethod
    def acquireSamplerState(MSamplerStateDesc: Any) -> MSamplerState:
        """Acquires an immutable unique sampler state matching the blend state descriptor."""
    def getBlendState(self) -> MBlendState:
        """Gets the current active blend state from the device."""
    def getDepthStencilState(self) -> MDepthStencilState:
        """Gets the current depth-stencil blend state from the device."""
    @staticmethod
    def getMaxSamplerCount() -> int:
        """Get the maximum number of simulataneous texture coordinate interpolation channels."""
    def getRasterizerState(self) -> MRasterizerState:
        """Gets the current active rasterizer state from the device."""
    def getSamplerState(self, shader: Any, samplerIndex: Any) -> MSamplerState:
        """Gets the current active sampler state from the device."""
    @staticmethod
    def releaseBlendState(MBlendState: Any) -> None:
        """Deletes the MBlendState and releases the reference to the underlying state object which is held by the MBlendState object."""
    @staticmethod
    def releaseDepthStencilState(MDepthStencilState: Any) -> None:
        """Deletes the MDepthStencilState and releases the reference to the underlying state object which is held by the MDepthStencilState object."""
    @staticmethod
    def releaseRasterizerState(MRasterizerState: Any) -> None:
        """Deletes the MRasterizerState and releases the reference to the underlying state object which is held by the MRasterizerState object."""
    @staticmethod
    def releaseSamplerState(MSamplerState: Any) -> None:
        """Deletes the MSamplerState and releases the reference to the underlying state object which is held by the MSamplerState object."""
    def setBlendState(self, MBlendState: Any) -> MStateManager:
        """Sets the active blend state on the device."""
    def setDepthStencilState(self, MDepthStencilState: Any) -> MStateManager:
        """Sets the active depth-stencil state on the device."""
    def setRasterizerState(self, MRasterizerState: Any) -> MStateManager:
        """Sets the active rasterizer state on the device."""
    def setSamplerState(self, shader: Any, samplerIndex: Any, samplerState: Any) -> MStateManager:
        """Sets the active sampler state for any of the texture samplers on the device."""

class MStencilOpDesc:
    stencilDepthFailOp: Any
    stencilFailOp: Any
    stencilFunc: Any
    stencilPassOp: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def setDefaults(self) -> MStencilOpDesc:
        """Set all values for the stencil operation state to their default values."""

class MSubSceneContainer:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def add(self, item: Any) -> bool:
        """Add a render item to the set of render items that will be used to draw the DAG object associated with the override that owns this container. Each item in the container must have a unique name and the same render item may not be used in the container more than once. When Viewport 2.0 draws the associated DAG object, it will process all render items in this container."""
    def clear(self) -> MSubSceneContainer:
        """Remove all render items from this container. After calling, any render items owned by this container will be invalid."""
    def count(self) -> int:
        """Get the number of render items in the container."""
    def find(self, name: Any) -> MRenderItem:
        """Get a render item by name from the container. The ownership of the render item remains with the container and callers should not call MRenderItem.destroy() on it. The render items may be cached and will remain valid until removed from the container."""
    def getIterator(self) -> MSubSceneContainerIterator:
        """Get an iterator for the container."""
    def remove(self, name: Any) -> bool:
        """Remove a render item by name from the set of render items used to draw the object associated with the override that owns this container. Note that on successful removal any render item that was removed become invalid and any attempts to use such items will result in instability."""

class MSubSceneContainerIterator:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def destroy(self) -> MSubSceneContainerIterator:
        """Call this method to delete the iterator. After calling, the iterator will be invalid."""
    def next(self) -> MRenderItem:
        """Advance the iterator to the next render item in the associated MSubSceneContainer and return it."""
    def reset(self) -> MSubSceneContainerIterator:
        """Reset the iterator to the beginning of the associated MSubSceneContainer."""

class MSwatchRenderBase:
    renderQuality: Any
    def __init__(self, obj: MObject, renderObj: MObject, res: int) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def cancelCurrentSwatchRender() -> None:
        """The method cancels the swatch which is being rendered in parallel, and push the swatch render item back to the render queue after. """
    def cancelParallelRendering(self) -> MSwatchRenderBase:
        """Method to cancel the parallel rendering."""
    def doIteration(self) -> bool:
        """Method called from the MSwatchRenderRegister for generation of swatch image. The doIteration function is called repeatedly (during idle events) until it returns true. Using this swatch image can be generated in stages."""
    def finishParallelRender(self) -> MSwatchRenderBase:
        """Method to update the swatch image when the parallel rendering is finished."""
    def image(self) -> MImage:
        """This method returns the render swatch as an image."""
    def node(self) -> MObject:
        """This method returns the node that is used to compute the swatch."""
    def renderParallel(self) -> bool:
        """Method indicates if the swatch is rendered parallel."""
    def resolution(self) -> int:
        """This method returns the expected resolution of the swatch."""
    def swatchNode(self) -> MObject:
        """This method returns the node for which the swatch is required to be generated."""

class MTargetBlendDesc:
    alphaBlendOperation: Any
    alphaDestinationBlend: Any
    alphaSourceBlend: Any
    blendEnable: Any
    blendOperation: Any
    destinationBlend: Any
    sourceBlend: Any
    targetWriteMask: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def setDefaults(self) -> MTargetBlendDesc:
        """Set all values for the target blend state to their default values."""

class MTexture:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def bytesPerPixel(self) -> int:
        """Get the number of bytes per pixel in the texture."""
    @staticmethod
    def freeRawData(long: Any) -> None:
        """Deallocate system memory - retrieved from rawData()."""
    def hasAlpha(self) -> bool:
        """Get whether the texture has an alpha channel."""
    def hasTransparentAlpha(self) -> bool:
        """Get whether the texture has semi-transparent texels."""
    def hasZeroAlpha(self) -> bool:
        """Get whether the texture has any texels with an alpha value of 0.0."""
    def name(self) -> Any:
        """Get the name of the texture."""
    def rawData(self, arg: Any, rowPitch: Any, slicePitch: Any) -> Any:
        """Returns a long containing a C++ 'void' pointer which points to the raw data mapped to the texture."""
    def resourceHandle(self) -> int:
        """Returns a long containing a C++ 'void' pointer which points to the texture."""
    def setHasAlpha(self, bool: Any) -> MTexture:
        """Specify that the texture has an alpha channel."""
    def setHasTransparentAlpha(self, bool: Any) -> MTexture:
        """Specify that the texture has texels with an alpha value greater than or equal to 0.0 and less than 1.0."""
    def setHasZeroAlpha(self, bool: Any) -> MTexture:
        """Specify that the texture has texels with an alpha value of 0.0."""
    def textureDescription(self) -> MTextureDescription:
        """Get texture description."""
    def update(self, pixelData: Any, generateMipMaps: Any, rowPitch: int = 0, region: Any = None) -> MTexture:
        """update(image, generateMipMaps) -> selfupdate(textureNode) -> self"""

class MTextureAssignment:
    texture: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MTextureDescription:
    fArraySlices: Any
    fBytesPerRow: Any
    fBytesPerSlice: Any
    fDepth: Any
    fEnvMapType: Any
    fFormat: Any
    fHeight: Any
    fMipmaps: Any
    fTextureType: Any
    fWidth: Any
    kCubeMap: Any
    kDepthTexture: Any
    kEnvCrossHoriz: Any
    kEnvCrossVert: Any
    kEnvCubemap: Any
    kEnvHemiSphere: Any
    kEnvLatLong: Any
    kEnvNone: Any
    kEnvSphere: Any
    kImage1D: Any
    kImage1DArray: Any
    kImage2D: Any
    kImage2DArray: Any
    kNumberOfEnvMapTypes: Any
    kNumberOfTextureTypes: Any
    kVolumeTexture: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def setToDefault2DTexture(self) -> MTextureDescription:
        """Utility to set texture description to describe a 0 size 2-dimensional texture."""

class MTextureManager:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def acquireDepthTexture(self, textureName: Any, image: Any, generateMipMaps: bool = True, normalizationDesc: Any = None) -> MTexture:
        """acquireDepthTexture(textureName, pixelData, width, height, generateMipMaps=True, normalizationDesc=None) -> MTexture"""
    def acquireTexture(self, *args: Any, **kwargs: Any) -> Any:
        """(Deprecated) acquireTexture(filePath, mipmapLevels=0, layerName="", alphaChannelIdx=-1) -> MTexture"""
    def acquireTiledTexture(self, textureName: Any, tilePaths: Any, tilePositions: Any, undefinedColor: Any, width: Any, height: Any) -> Any:
        """Ask the renderer to acquire a tiled hardware texture."""
    def addImagePath(self, string: Any) -> MTextureManager:
        """Adds an additional search path for looking up images on disk."""
    def imagePaths(self) -> list[str]:
        """Get the current set of image search paths."""
    def releaseTexture(self, MTexture: Any) -> MTextureManager:
        """Deletes the MTexture and releases the reference to the underlying texture which is held by the MTexture object."""
    def saveTexture(self, MTexture: Any, string: Any) -> MTextureManager:
        """Ask the renderer to save a hardware texture to disk."""

class MTextureUpdateRegion:
    fXRangeMax: Any
    fXRangeMin: Any
    fYRangeMax: Any
    fYRangeMin: Any
    fZRangeMax: Any
    fZRangeMin: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MUIDrawManager:
    kAutomatic: Any
    kCenter: Any
    kClosedLine: Any
    kDashed: Any
    kDefaultFontSize: Any
    kDotted: Any
    kFlat: Any
    kInclineItalic: Any
    kInclineNormal: Any
    kInclineOblique: Any
    kLeft: Any
    kLineNone: Any
    kLineOverline: Any
    kLineStrikeoutLine: Any
    kLineStrip: Any
    kLineUnderline: Any
    kLines: Any
    kNonSelectable: Any
    kPoints: Any
    kRight: Any
    kSelectable: Any
    kShaded: Any
    kShortDashed: Any
    kShortDotted: Any
    kSmallFontSize: Any
    kSolid: Any
    kStippled: Any
    kStretchCondensed: Any
    kStretchExpanded: Any
    kStretchExtraCondensed: Any
    kStretchExtraExpanded: Any
    kStretchSemiCondensed: Any
    kStretchSemiExpanded: Any
    kStretchUltraCondensed: Any
    kStretchUltraExpanded: Any
    kStretchUnstretched: Any
    kTriStrip: Any
    kTriangles: Any
    kWeightBlack: Any
    kWeightBold: Any
    kWeightDemiBold: Any
    kWeightLight: Any
    kWeightNormal: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def arc(self, center: Any, start: Any, end: Any, normal: Any, radius: Any, numSubdivisions: Any, arg: Any, start_: Any, end_: Any, normal_: Any, radius_: Any, filled: bool = False) -> MUIDrawManager:
        """Draw an arc. The arc is within the plane determined by a normal vector."""
    def arc2d(self, center: Any, start: Any, end: Any, radius: Any, numSubdivisions: Any, arg: Any, start_: Any, end_: Any, radius_: Any, filled: bool = False) -> MUIDrawManager:
        """Draw a 2D arc on the screen. The arc is always facing the camera."""
    def beginDrawInXray(self) -> MUIDrawManager:
        """The drawables to be drawn between calls to beginDrawInXray() and endDrawInXray() will display"""
    def beginDrawable(self, selectability: Any, selectionName: int = 0) -> MUIDrawManager:
        """Resets all draw state, such as color and line style, to defaults and indicates the start of a sequence of drawing operations."""
    def box(self, center: Any, up: Any, right: Any, scaleX: float = 1.0, scaleY: float = 1.0, scaleZ: float = 1.0, filled: bool = False) -> MUIDrawManager:
        """Draw a box."""
    def capsule(self, center: Any, up: Any, radius: Any, height: Any, subdivisionsAxis: Any, subdivisionsHeight: Any, filled: bool = False) -> MUIDrawManager:
        """Draw a capsule."""
    def circle(self, center: Any, normal: Any, radius: Any, numSubdivision: Any, arg: Any, normal_: Any, radius_: Any, filled: bool = False) -> MUIDrawManager:
        """Draw a circle."""
    def circle2d(self, center: Any, radius: Any, numSubdivision: Any, arg: Any, radius_: Any, filled: bool = False) -> MUIDrawManager:
        """Draw a 2D circle on the screen."""
    def cone(self, base: Any, direction: Any, radius: Any, height: Any, subdivisionsCap: Any, arg: Any, direction_: Any, radius_: Any, height_: Any, filled: bool = False) -> MUIDrawManager:
        """Draw a cone."""
    def cylinder(self, center: Any, up: Any, radius: Any, height: Any, subdivisionsAxis: Any, filled: bool = False) -> MUIDrawManager:
        """Draw a cylinder."""
    def depthPriority(self) -> int:
        """Get the current depth priority value for primitive drawing."""
    def endDrawInXray(self) -> MUIDrawManager:
        """Pair with beginDrawInXray()."""
    def endDrawable(self) -> MUIDrawManager:
        """Indicates the end of a sequence of drawing operations."""
    @staticmethod
    def getFontList() -> list[str]:
        """Get the names of all font faces that are available on current system."""
    @staticmethod
    def getIconNames() -> list[str]:
        """Get list of icon names. The names can be used"""
    def icon(self, position: Any, name: Any, arg: Any) -> MUIDrawManager:
        """Draw an icon at a given 3d position."""
    def line(self, startPoint: Any, endPoint: Any) -> MUIDrawManager:
        """Draw a straight line between two points."""
    def line2d(self, startPoint: Any, endPoint: Any) -> MUIDrawManager:
        """Draw a straight line between two points."""
    def lineList(self, points: Any, draw2D: Any) -> MUIDrawManager:
        """Draw a series of line segments in 3D or 2D."""
    def lineStrip(self, points: Any, draw2D: Any) -> MUIDrawManager:
        """Draw a series of connected line segments in 3D or 2D"""
    def mesh(self, mode: Any, position: Any, normal: Any = None, color: Any = None, index: Any = None, texcoord: Any = None) -> MUIDrawManager:
        """Draw custom geometric shapes from an array of vertices."""
    def mesh2d(self, mode: Any, position: Any, color: Any = None, index: Any = None, texcoord: Any = None) -> MUIDrawManager:
        """Draw custom 2d geometric shapes from an array of vertices."""
    def point(self, point: Any) -> MUIDrawManager:
        """Draw a point."""
    def point2d(self, point: Any) -> MUIDrawManager:
        """Draw a point."""
    def points(self, points: Any, draw2D: Any) -> MUIDrawManager:
        """Draw a series of points in 3D or 2D."""
    def rect(self, center: Any, up: Any, normal: Any, scaleX: Any, scaleY: Any, filled: bool = False) -> MUIDrawManager:
        """Draw a rectangle."""
    def rect2d(self, center: Any, up: Any, scaleX: Any, scaleY: Any, filled: bool = False) -> MUIDrawManager:
        """Draw a 2D rectangle on the screen."""
    def setColor(self, color: Any) -> MUIDrawManager:
        """Set the draw color. This will remain in effect until the next call to setColor(), setColorIndex() or endDrawable()."""
    def setColorIndex(self, index: Any) -> MUIDrawManager:
        """Set the color index for the later primitive and text drawing."""
    def setDepthPriority(self, priority: Any) -> MUIDrawManager:
        """Set the depth priority for primitive drawing."""
    def setFontIncline(self, fontIncline: Any) -> MUIDrawManager:
        """Set the incline of font to be used when drawing text."""
    def setFontLine(self, fontLine: Any) -> MUIDrawManager:
        """Set the line of font to be used when drawing text."""
    def setFontName(self, faceName: Any) -> MUIDrawManager:
        """Set the face name of font to be used when drawing text."""
    def setFontSize(self, fontSize: Any) -> MUIDrawManager:
        """Set the size of font to be used when drawing text."""
    def setFontStretch(self, fontStretch: Any) -> MUIDrawManager:
        """Set the stretch of font to be used when drawing text."""
    def setFontWeight(self, fontWeight: Any) -> MUIDrawManager:
        """Set the weight of font to be used when drawing text."""
    def setLineStyle(self, style: Any) -> MUIDrawManager:
        """setLineStyle(factor, pattern) -> self"""
    def setLineWidth(self, value: Any) -> MUIDrawManager:
        """Set the line width for the primitive drawing (line, rect, box...)"""
    def setPaintStyle(self, style: Any) -> MUIDrawManager:
        """Set the paint style for filled primitive drawing."""
    def setPointSize(self, value: Any) -> MUIDrawManager:
        """Set the point size for the point drawing."""
    def setTexture(self, texture: Any) -> MUIDrawManager:
        """Set the active texture to apply when drawing a mesh."""
    def setTextureMask(self, mask: Any) -> MUIDrawManager:
        """Set the channel mask to used when applying a texture to a mesh."""
    def setTextureSampler(self, filter: Any, address: Any) -> MUIDrawManager:
        """Set the filter and address mode used when applying a texture to a mesh."""
    def sphere(self, center: Any, radius: Any, subdivisionsAxis: Any, subdivisionsHeight: Any, filled: Any, radius_: Any, filled_: bool = False) -> MUIDrawManager:
        """Draw a sphere."""
    def text(self, position: Any, text: Any, alignment: Any, backgroundSize: Any = None, backgroundColor: Any = None, dynamic: bool = False) -> MUIDrawManager:
        """Draw a screen facing and horizontal aligned text in viewport 2.0."""
    def text2d(self, position: Any, text: Any, alignment: Any, backgroundSize: Any = None, backgroundColor: Any = None, dynamic: bool = False) -> MUIDrawManager:
        """Draw a text on the screen."""

class MUniformParameter:
    enumFieldNames: Any
    kSemanticBackgroundColor: Any
    kSemanticBump: Any
    kSemanticBumpTexture: Any
    kSemanticColor: Any
    kSemanticColorTexture: Any
    kSemanticEnvironment: Any
    kSemanticFarClipPlane: Any
    kSemanticFrameNumber: Any
    kSemanticHWSEdgeLevel: Any
    kSemanticHWSFaceLevel: Any
    kSemanticHWSFrontCCW: Any
    kSemanticHWSHighlighting: Any
    kSemanticHWSInstancedDraw: Any
    kSemanticHWSObjectLevel: Any
    kSemanticHWSOccluder: Any
    kSemanticHWSPrimitiveBase: Any
    kSemanticHWSPrimitiveCountPerInstance: Any
    kSemanticHWSVertexLevel: Any
    kSemanticLocalViewer: Any
    kSemanticNearClipPlane: Any
    kSemanticNormal: Any
    kSemanticNormalTexture: Any
    kSemanticNormalizationTexture: Any
    kSemanticObjectDir: Any
    kSemanticObjectPos: Any
    kSemanticOpaqueDepthTexture: Any
    kSemanticProjectionDir: Any
    kSemanticProjectionInverseMatrix: Any
    kSemanticProjectionInverseTransposeMatrix: Any
    kSemanticProjectionMatrix: Any
    kSemanticProjectionPos: Any
    kSemanticProjectionTransposeMatrix: Any
    kSemanticTime: Any
    kSemanticTranspDepthTexture: Any
    kSemanticUnknown: Any
    kSemanticViewDir: Any
    kSemanticViewInverseMatrix: Any
    kSemanticViewInverseTransposeMatrix: Any
    kSemanticViewMatrix: Any
    kSemanticViewPos: Any
    kSemanticViewProjectionInverseMatrix: Any
    kSemanticViewProjectionInverseTransposeMatrix: Any
    kSemanticViewProjectionMatrix: Any
    kSemanticViewProjectionTransposeMatrix: Any
    kSemanticViewTransposeMatrix: Any
    kSemanticViewportPixelSize: Any
    kSemanticWorldDir: Any
    kSemanticWorldInverseMatrix: Any
    kSemanticWorldInverseTransposeMatrix: Any
    kSemanticWorldMatrix: Any
    kSemanticWorldPos: Any
    kSemanticWorldTransposeMatrix: Any
    kSemanticWorldViewInverseMatrix: Any
    kSemanticWorldViewInverseTransposeMatrix: Any
    kSemanticWorldViewMatrix: Any
    kSemanticWorldViewProjectionInverseMatrix: Any
    kSemanticWorldViewProjectionInverseTransposeMatrix: Any
    kSemanticWorldViewProjectionMatrix: Any
    kSemanticWorldViewProjectionTransposeMatrix: Any
    kSemanticWorldViewTransposeMatrix: Any
    kType1DTexture: Any
    kType2DTexture: Any
    kType3DTexture: Any
    kTypeBool: Any
    kTypeCubeTexture: Any
    kTypeEnum: Any
    kTypeEnvTexture: Any
    kTypeFloat: Any
    kTypeInt: Any
    kTypeString: Any
    kTypeUnknown: Any
    keyable: Any
    rangeMax: Any
    rangeMin: Any
    softRangeMax: Any
    softRangeMin: Any
    uiHidden: Any
    uiNiceName: Any
    def __init__(self, name: Any = None, type: Any = None, semantic: Any = None, numRows: int | None = None, numColumns: int | None = None, userData: None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def asBool(self, context: Any) -> bool:
        """Get the value of this uniform parameter as a boolean value."""
    def asFloat(self, context: Any) -> float:
        """Get the value of this uniform parameter as a float."""
    def asFloatArray(self, context: Any) -> tuple[Any]:
        """Get the value of this uniform parameter as one or more floating point values."""
    def asInt(self, context: Any) -> int:
        """Get the value of this uniform parameter as an integer."""
    def asString(self, context: Any) -> Any:
        """Get the value of this uniform parameter as a string."""
    def copy(self, source: Any) -> MUniformParameter:
        """Copy data from source parameter."""
    def hasChanged(self, context: Any) -> bool:
        """Has the value of this parameter changed since the last time it was accessed?"""
    def isATexture(self) -> bool:
        """Returns True if this parameter represents a texture, False otherwise."""
    def name(self) -> Any:
        """Get the name of this parameter."""
    def numColumns(self) -> int:
        """Get the number of columns in this parameter."""
    def numElements(self) -> int:
        """Get the number of elements in this parameter (including rows and columns)."""
    def numRows(self) -> int:
        """Get the number of rows in this parameter."""
    def plug(self) -> MPlug:
        """Get the plug managed by this parameter."""
    def semantic(self) -> int:
        """Get the semantic of this parameter."""
    def setBool(self, value: Any) -> MUniformParameter:
        """Set the value of this uniform parameter as a boolean value."""
    def setDirty(self) -> MUniformParameter:
        """Mark the data for this parameter as dirty. This will force the parameter to report that it has been changed the next time it is accessed. This allows external events (e.g. device lost, texture management, etc) to force a shader to re-set parameters tied to externally managed resources."""
    def setFloat(self, value: Any) -> MUniformParameter:
        """Set the value of this uniform parameter as a float."""
    def setFloatArray(self, value: Any) -> MUniformParameter:
        """Set the value of this uniform parameter as one or more floating point values."""
    def setInt(self, value: Any) -> MUniformParameter:
        """Set the value of this uniform parameter as an integer value."""
    def setString(self, value: Any) -> MUniformParameter:
        """Set the value of this uniform parameter as a string."""
    def source(self) -> MPlug:
        """Get the source plug connected to this parameter. Other than textures, this will typically be an invalid plug."""
    def type(self) -> int:
        """Get the type of this parameter."""
    def userData(self) -> int:
        """Get the user data for this parameter. User data can be used to store plugin specific information that you want to associate with this parameter. Typically this will be used to store a handle to the effect parameter."""

class MUniformParameterList:
    def __init__(self, src: MUniformParameterList | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def append(self, element: MUniformParameter) -> bool:
        """Append a new parameter to this end of this list."""
    def copy(self, source: Any) -> MUniformParameterList:
        """Copy data from source list."""
    def setElement(self, n: int, element: MUniformParameter) -> bool:
        """Set the nth parameter in this list."""
    def setLength(self, length: int) -> bool:
        """Set the number of parameters in this list. If this is greater than the current number of parameters in the list, the caller is responsible for setting the new parameters to valid values using setElement."""

class MUserRenderOperation:
    kClear: Any
    kDataServer: Any
    kHUDRender: Any
    kPresentTarget: Any
    kQuadRender: Any
    kSceneRender: Any
    kUserDefined: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addUIDrawables(self, drawManager: Any, frameContext: Any) -> MUserRenderOperation:
        """Provides access to the MUIDrawManager, which can be used to queue up operations to draw simple UI shapes like lines, circles, text, etc."""
    def cameraOverride(self) -> MCameraOverride:
        """Query for a camera override."""
    def enableSRGBWrite(self) -> bool:
        """Return whether to enable GPU based gamma correction during pixel writes."""
    def hasUIDrawables(self) -> bool:
        """Query whether addUIDrawables() should be called or not."""
    def name(self) -> Any:
        """Returns the name of the render operator."""
    def operationType(self) -> int:
        """Returns the type of a render operator."""
    def requiresLightData(self) -> bool:
        """Indicates whether light data from the renderer is required for this user operation."""
    def requiresResetDeviceStates(self) -> bool:
        """Indicates whether reset of device states is required for this user operation."""
    def targetOverrideList(self) -> list[MRenderTarget]:
        """Return a list of render target which will be used as the target overrides for the operation."""
    def viewportRectangleOverride(self) -> MFloatPoint:
        """Query for a viewport rectangle override."""

class MVaryingParameter:
    kBinormal: Any
    kChar: Any
    kColor: Any
    kDouble: Any
    kFloat: Any
    kInt16: Any
    kInt32: Any
    kInvalidParameter: Any
    kNoSemantic: Any
    kNormal: Any
    kPosition: Any
    kStructure: Any
    kTangent: Any
    kTexCoord: Any
    kUnsignedChar: Any
    kUnsignedInt16: Any
    kUnsignedInt32: Any
    kWeight: Any
    def __init__(self, name: Any = None, type: Any = None, minDimension: int | None = None, maxDimension: int | None = None, semantic: Any = None, invertTexCoords: Any = None, semanticName: Any = None, invertTexCoords_: bool | None = None, semanticName_: Any = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addElement(self, child: MVaryingParameter) -> MVaryingParameter:
        """Add a child element to this parameter."""
    def copy(self, source: Any) -> MVaryingParameter:
        """Copy data from source parameter."""
    def destinationSetName(self) -> Any:
        """Get the destination Set of this parameter."""
    def dimension(self) -> int:
        """Get the dimension of this parameter."""
    def elementSize(self) -> int:
        """Get the size in bytes of one element of this parameter."""
    def getElement(self, index: int) -> MVaryingParameter:
        """Get an element within a structure."""
    def maximumStride(self) -> int:
        """Get the maximum stride of this parameter in bytes."""
    def name(self) -> Any:
        """Get the name of this parameter."""
    def numElements(self) -> int:
        """Get the number of elements in this structure."""
    def removeElements(self) -> MVaryingParameter:
        """Remove all child elements from a structure."""
    def semantic(self) -> int:
        """Get the semantic of this parameter."""
    def semanticName(self) -> Any:
        """Get the semantic name assigned to this parameter."""
    def setSource(self, semantic: int, name: Any) -> MVaryingParameter:
        """While the source of geometry parameters is usually configured by the artist through Maya's user interface, this method allows you to programatically set the source of a geometry parameter, including both the data type (e.g. position, normal, etc) and an optional set name (e.g. UV set 'map1'). This is useful for implementing custom default values or shader operations."""
    def sourceSemantic(self) -> int:
        """Get the type of data (e.g. position, normal, uv) currently populating this parameter."""
    def sourceSetName(self) -> Any:
        """If the current data type supports data sets (e.g. uv sets, color sets), get the name of the data set populating this parameter. This method will only return a useful value when called on leaf-level parameters (e.g. structures do not have sources, only the elements of a structure have sources)."""
    def type(self) -> int:
        """Get the type of this parameter."""
    def updateId(self) -> int:
        """Get the update id."""

class MVaryingParameterList:
    def __init__(self, src: MVaryingParameterList | None = None) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def append(self, element: MVaryingParameter) -> bool:
        """Append a new parameter to this end of this list."""
    def copy(self, source: Any) -> MVaryingParameterList:
        """Copy data from source list."""
    def setElement(self, n: int, element: MVaryingParameter) -> bool:
        """Set the nth parameter in this list."""
    def setLength(self, length: int) -> bool:
        """Set the number of parameters in this list. If this is greater than the current number of parameters in the list, the caller is responsible for setting the new parameters to valid values using setElement."""

class MVertexBuffer:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def acquire(self, size: Any, writeOnly: Any) -> int:
        """Get a pointer to memory for the buffer."""
    def commit(self, long: Any) -> MVertexBuffer:
        """Commit the data stored in the memory given by acquire() to the buffer."""
    def descriptor(self) -> MVertexBufferDescriptor:
        """Get the the buffer descriptor."""
    def hasCustomResourceHandle(self) -> bool:
        """Returns true if this vertex buffer is using a custom resource handle set"""
    def lockResourceHandle(self) -> MVertexBuffer:
        """Lock the resource handle. The pointer returned from resourceHandle() is"""
    def map(self) -> int:
        """Get a read-only pointer to the existing content of the buffer."""
    def resourceHandle(self) -> int:
        """Returns a long containing a C++ 'float' pointer which points to the graphics device dependent handle to the vertex buffer."""
    def setResourceHandle(self, long: Any, int: Any) -> MVertexBuffer:
        """Set the graphics-device-dependent hardware buffer resource handle."""
    def unload(self) -> MVertexBuffer:
        """If the buffer is resident in GPU memory, calling this method will move it to system memory and free the GPU memory."""
    def unlockResourceHandle(self) -> MVertexBuffer:
        """Unlock the resource handle. The pointer returned from resourceHandle is not"""
    def unmap(self) -> MVertexBuffer:
        """Release the data exposed by map(). If this method is not called, the buffer will not be recycled."""
    def update(self, buffer: Any, destOffset: Any, numVerts: Any, truncateIfSmaller: Any) -> MVertexBuffer:
        """Set a portion (or all) of the contents of the MVertexBuffer using the data in the provided software buffer."""
    def vertexCount(self) -> int:
        """Get the size of the vertex buffer."""

class MVertexBufferArray:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def append(self, MVertexBuffer: Any, name: Any) -> MVertexBufferArray:
        """Add a new vertex buffer to the list."""
    def clear(self) -> MVertexBufferArray:
        """Clear the array."""
    def getBuffer(self, string: Any) -> MVertexBuffer:
        """Get vertex buffer by name."""
    def getName(self, int: Any) -> Any:
        """Get the name of the buffer at desired index."""

class MVertexBufferDescriptor:
    dataType: Any
    dataTypeSize: Any
    dimension: Any
    name: Any
    offset: Any
    semantic: Any
    semanticName: Any
    stride: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MVertexBufferDescriptorList:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def append(self, MVertexBufferDescriptor: Any) -> bool:
        """Add a descriptor to the list. Creates and stores a copy which is owned by the list."""
    def clear(self) -> MVertexBufferDescriptorList:
        """Clear the list."""
    def remove(self, index: Any) -> bool:
        """Remove a descriptor from the list and delete it."""