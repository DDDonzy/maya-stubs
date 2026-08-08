# Stub for maya.utils - reflected from Maya 2024

from typing import Any, Callable

class MayaGuiLogHandler:
    def acquire(self):
        """Acquire the I/O thread lock."""
    def addFilter(self, filter):
        """Add the specified filter to this handler."""
    def close(self):
        """Tidy up any resources used by the handler."""
    def createLock(self):
        """Acquire a thread lock for serializing access to the underlying I/O."""
    def emit(self, record): ...
    def filter(self, record):
        """Determine if a record is loggable by consulting all the filters."""
    def flush(self):
        """Ensure all logging output has been flushed."""
    def format(self, record):
        """Format the specified record."""
    def get_name(self): ...
    def handle(self, record):
        """Conditionally emit the specified logging record."""
    def handleError(self, record):
        """Handle errors which occur during an emit() call."""
    name: Any
    def release(self):
        """Release the I/O thread lock."""
    def removeFilter(self, filter):
        """Remove the specified filter from this handler."""
    def setFormatter(self, fmt):
        """Set the formatter for this handler."""
    def setLevel(self, level):
        """Set the logging level of this handler.  level must be an int or a str."""
    def set_name(self, name): ...

class Output:
    def flush(*args: Any, **kwargs: Any):
        """Flush no-op"""
    def isatty(*args: Any, **kwargs: Any):
        """test whether a file descriptor refers to a terminal"""
    softspace: Any
    def write(*args: Any, **kwargs: Any):
        """Write the given string"""
    def writelines(*args: Any, **kwargs: Any):
        """Write the given sequence"""

class StringTable:
    ...

def abs_over(*args: Any, **kwargs: Any):
    """abs"""

def all_over(*args: Any, **kwargs: Any):
    """all"""

def any_over(*args: Any, **kwargs: Any):
    """any"""

def ascii_over(*args: Any, **kwargs: Any):
    """ascii"""

def bin_over(*args: Any, **kwargs: Any):
    """bin"""

def bool_over(*args: Any, **kwargs: Any):
    """bool"""

def breakpoint_over(*args: Any, **kwargs: Any):
    """breakpoint"""

def bytearray_over(*args: Any, **kwargs: Any):
    """bytearray"""

def bytes_over(*args: Any, **kwargs: Any):
    """bytes"""

def callable_over(*args: Any, **kwargs: Any):
    """callable"""

def chr_over(*args: Any, **kwargs: Any):
    """chr"""

def classmethod_over(*args: Any, **kwargs: Any):
    """classmethod"""

cmds: Any

def compile_over(*args: Any, **kwargs: Any):
    """compile"""

def complex_over(*args: Any, **kwargs: Any):
    """complex"""

def delattr_over(*args: Any, **kwargs: Any):
    """delattr"""

def dict_over(*args: Any, **kwargs: Any):
    """dict"""

def dir_over(*args: Any, **kwargs: Any):
    """dir"""

def divmod_over(*args: Any, **kwargs: Any):
    """divmod"""

def enumerate_over(*args: Any, **kwargs: Any):
    """enumerate"""

def eval_over(*args: Any, **kwargs: Any):
    """eval"""

def exec_over(*args: Any, **kwargs: Any):
    """exec"""

def execfile(filename, myglobals=None, mylocals=None):
    """Read and execute a Python script from a file in the given namespaces."""

def executeDeferred(func: Callable[..., Any], *args: Any) -> None:
    """Delays the execution of the given script or function until Maya is idle."""

def executeInMainThreadWithResult(func: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
    """Runs Python code in the main thread and waits for the return code."""

def filter_over(*args: Any, **kwargs: Any):
    """filter"""

def float_over(*args: Any, **kwargs: Any):
    """float"""

def formatGuiException(exceptionType, exceptionObject, traceBack, detail=2):
    """Format a trace stack into a string."""

def formatGuiResult(obj):
    """Gets a string representation of a result object."""

def format_over(*args: Any, **kwargs: Any):
    """format"""

def frozenset_over(*args: Any, **kwargs: Any):
    """frozenset"""

class futureStr:
    def capitalize(self, /):
        """Return a capitalized version of the string."""
    def casefold(self, /):
        """Return a version of the string suitable for caseless comparisons."""
    def center(self, width, fillchar=' ', /):
        """Return a centered string of length width."""
    def count(*args: Any, **kwargs: Any):
        """S.count(sub[, start[, end]]) -> int"""
    def encode(self, /, encoding='utf-8', errors='strict'):
        """Encode the string using the codec registered for encoding."""
    def endswith(*args: Any, **kwargs: Any):
        """S.endswith(suffix[, start[, end]]) -> bool"""
    def expandtabs(self, /, tabsize=8):
        """Return a copy where all tab characters are expanded using spaces."""
    def find(*args: Any, **kwargs: Any):
        """S.find(sub[, start[, end]]) -> int"""
    def format(*args: Any, **kwargs: Any):
        """S.format(*args, **kwargs) -> str"""
    def format_map(*args: Any, **kwargs: Any):
        """S.format_map(mapping) -> str"""
    def index(*args: Any, **kwargs: Any):
        """S.index(sub[, start[, end]]) -> int"""
    def isalnum(self, /):
        """Return True if the string is an alpha-numeric string, False otherwise."""
    def isalpha(self, /):
        """Return True if the string is an alphabetic string, False otherwise."""
    def isascii(self, /):
        """Return True if all characters in the string are ASCII, False otherwise."""
    def isdecimal(self, /):
        """Return True if the string is a decimal string, False otherwise."""
    def isdigit(self, /):
        """Return True if the string is a digit string, False otherwise."""
    def isidentifier(self, /):
        """Return True if the string is a valid Python identifier, False otherwise."""
    def islower(self, /):
        """Return True if the string is a lowercase string, False otherwise."""
    def isnumeric(self, /):
        """Return True if the string is a numeric string, False otherwise."""
    def isprintable(self, /):
        """Return True if the string is printable, False otherwise."""
    def isspace(self, /):
        """Return True if the string is a whitespace string, False otherwise."""
    def istitle(self, /):
        """Return True if the string is a title-cased string, False otherwise."""
    def isupper(self, /):
        """Return True if the string is an uppercase string, False otherwise."""
    def join(self, iterable, /):
        """Concatenate any number of strings."""
    def ljust(self, width, fillchar=' ', /):
        """Return a left-justified string of length width."""
    def lower(self, /):
        """Return a copy of the string converted to lowercase."""
    def lstrip(self, chars=None, /):
        """Return a copy of the string with leading whitespace removed."""
    def maketrans(*args: Any, **kwargs: Any):
        """Return a translation table usable for str.translate()."""
    def partition(self, sep, /):
        """Partition the string into three parts using the given separator."""
    def removeprefix(self, prefix, /):
        """Return a str with the given prefix string removed if present."""
    def removesuffix(self, suffix, /):
        """Return a str with the given suffix string removed if present."""
    def replace(self, old, new, count=-1, /):
        """Return a copy with all occurrences of substring old replaced by new."""
    def rfind(*args: Any, **kwargs: Any):
        """S.rfind(sub[, start[, end]]) -> int"""
    def rindex(*args: Any, **kwargs: Any):
        """S.rindex(sub[, start[, end]]) -> int"""
    def rjust(self, width, fillchar=' ', /):
        """Return a right-justified string of length width."""
    def rpartition(self, sep, /):
        """Partition the string into three parts using the given separator."""
    def rsplit(self, /, sep=None, maxsplit=-1):
        """Return a list of the substrings in the string, using sep as the separator string."""
    def rstrip(self, chars=None, /):
        """Return a copy of the string with trailing whitespace removed."""
    def split(self, /, sep=None, maxsplit=-1):
        """Return a list of the substrings in the string, using sep as the separator string."""
    def splitlines(self, /, keepends=False):
        """Return a list of the lines in the string, breaking at line boundaries."""
    def startswith(*args: Any, **kwargs: Any):
        """S.startswith(prefix[, start[, end]]) -> bool"""
    def strip(self, chars=None, /):
        """Return a copy of the string with leading and trailing whitespace removed."""
    def swapcase(self, /):
        """Convert uppercase characters to lowercase and lowercase characters to uppercase."""
    def title(self, /):
        """Return a version of the string where each word is titlecased."""
    def translate(self, table, /):
        """Replace each character in the string using the given translation table."""
    def upper(self, /):
        """Return a copy of the string converted to uppercase."""
    def zfill(self, width, /):
        """Pad a numeric string with zeros on the left, to fill a field of the given width."""

def getPossibleCompletions(input):
    """Utility method to handle command completion"""

def getattr_over(*args: Any, **kwargs: Any):
    """getattr"""

def globals_over(*args: Any, **kwargs: Any):
    """globals"""

def guiLogHandler():
    """Adds an additional handler to the root logger to print to"""

def hasattr_over(*args: Any, **kwargs: Any):
    """hasattr"""

def hash_over(*args: Any, **kwargs: Any):
    """hash"""

def helpNonVerbose(thing, title='Python Library Documentation: %s', forceload=0):
    """Utility method to return python help in the form of a string"""

def help_over(*args: Any, **kwargs: Any):
    """help"""

def hex_over(*args: Any, **kwargs: Any):
    """hex"""

def id_over(*args: Any, **kwargs: Any):
    """id"""

def input_over(*args: Any, **kwargs: Any):
    """input"""

inspect: Any

def int_over(*args: Any, **kwargs: Any):
    """int"""

def isinstance_over(*args: Any, **kwargs: Any):
    """isinstance"""

def issubclass_over(*args: Any, **kwargs: Any):
    """issubclass"""

def iter_over(*args: Any, **kwargs: Any):
    """iter"""

def len_over(*args: Any, **kwargs: Any):
    """len"""

def list_over(*args: Any, **kwargs: Any):
    """list"""

def loadStringResourcesForFile(scriptPath, fullModulePath, resourceFileName):
    """Load a string resource."""

def loadStringResourcesForModule(moduleName):
    """Load the string resources associated with the given module"""

def locals_over(*args: Any, **kwargs: Any):
    """locals"""

logging: Any

def map_over(*args: Any, **kwargs: Any):
    """map"""

def max_over(*args: Any, **kwargs: Any):
    """max"""

def memoryview_over(*args: Any, **kwargs: Any):
    """memoryview"""

def min_over(*args: Any, **kwargs: Any):
    """min"""

def next_over(*args: Any, **kwargs: Any):
    """next"""

def object_over(*args: Any, **kwargs: Any):
    """object"""

def oct_over(*args: Any, **kwargs: Any):
    """oct"""

def open_over(*args: Any, **kwargs: Any):
    """open"""

def ord_over(*args: Any, **kwargs: Any):
    """ord"""

os_environ: Any

def pow_over(*args: Any, **kwargs: Any):
    """pow"""

def print_over(*args: Any, **kwargs: Any):
    """print"""

def processIdleEvents() -> None:
    """Run commands from the idle queue."""

def property_over(*args: Any, **kwargs: Any):
    """property"""

pydoc: Any

class range:
    def count(*args: Any, **kwargs: Any):
        """rangeobject.count(value) -> integer -- return number of occurrences of value"""
    def index(*args: Any, **kwargs: Any):
        """rangeobject.index(value) -> integer -- return index of value."""
    start: Any
    step: Any
    stop: Any

def range_over(*args: Any, **kwargs: Any):
    """range"""

re: Any

def repr_over(*args: Any, **kwargs: Any):
    """repr"""

def reversed_over(*args: Any, **kwargs: Any):
    """reversed"""

def round_over(*args: Any, **kwargs: Any):
    """round"""

def set_over(*args: Any, **kwargs: Any):
    """set"""

def setattr_over(*args: Any, **kwargs: Any):
    """setattr"""

def shellLogHandler():
    """Adds an additional handler to the root logger to print to sys.stdout"""

def slice_over(*args: Any, **kwargs: Any):
    """slice"""

def sorted_over(*args: Any, **kwargs: Any):
    """sorted"""

def staticmethod_over(*args: Any, **kwargs: Any):
    """staticmethod"""

def str_over(*args: Any, **kwargs: Any):
    """str"""

def sum_over(*args: Any, **kwargs: Any):
    """sum"""

def super_over(*args: Any, **kwargs: Any):
    """super"""

def tuple_over(*args: Any, **kwargs: Any):
    """tuple"""

def type_over(*args: Any, **kwargs: Any):
    """type"""

def vars_over(*args: Any, **kwargs: Any):
    """vars"""

def zip_over(*args: Any, **kwargs: Any):
    """zip"""

