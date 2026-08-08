# Stub for maya.mel - MEL/Python interop (Maya 2024)
from typing import Any, Callable, Sequence


def eval(string: str) -> str: ...
def createMelWrapper(
    fn: Callable[..., Any],
    types: Sequence[str] = [],
    retType: str = "void",
    ignoreDefaultArgs: bool = True,
    returnCmd: bool = False,
    outDir: str | None = None,
) -> str: ...
