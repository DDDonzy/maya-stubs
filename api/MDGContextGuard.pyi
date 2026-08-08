# Stub for maya.api.MDGContextGuard - generated from Maya 2024 Python API reference

from typing import Any

class MDGContextGuard:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the object with a specific context"""
    def context(self, *args: Any, **kwargs: Any) -> Any:
        """Return the context that was passed into this object on entry/construction"""
    def original_context(self, *args: Any, **kwargs: Any) -> Any:
        """Return the context that was current when this object was entered/constructed"""
    def restore(self, *args: Any, **kwargs: Any) -> Any:
        """Restore the context on entry/construction to be the current evaluation context"""

class object:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""