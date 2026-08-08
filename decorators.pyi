# Stub for maya.decorators - reflected from Maya 2024

from typing import Any

class DebugDecorator:
    ENABLED: Any
    INDENTATION: Any
    INDENT_LEVEL: Any
    OUTPUT: Any
    def begin(title):
        """Start a new debugging section, with header"""
    def end(result=None):
        """Complete a debugging section, showing the result of the block"""
    def output(message):
        """Print a debugging message, if enabled"""
    sys_stdout: Any

class TestDecorators:
    def ClassDecoration(*args, **kwargs):
        """Decorator class, providing decorated overrides to all of the base class methods"""
    def MethodDecoration():
        """Class decorated with debug information at the method level"""
    def addClassCleanup(function, /, *args, **kwargs):
        """Same as addCleanup, except the cleanup items are called even if"""
    def addCleanup(self, function, /, *args, **kwargs):
        """Add a function, with arguments, to be called when the test is"""
    def addTypeEqualityFunc(self, typeobj, function):
        """Add a type specific assertEqual style function to compare a type."""
    def assertAlmostEqual(self, first, second, places=None, msg=None, delta=None):
        """Fail if the two objects are unequal as determined by their"""
    def assertAlmostEquals(*args, **kwargs): ...
    def assertCountEqual(self, first, second, msg=None):
        """Asserts that two iterables have the same elements, the same number of"""
    def assertDictContainsSubset(self, subset, dictionary, msg=None):
        """Checks whether dictionary is a superset of subset."""
    def assertDictEqual(self, d1, d2, msg=None): ...
    def assertEqual(self, first, second, msg=None):
        """Fail if the two objects are unequal as determined by the '=='"""
    def assertEquals(*args, **kwargs): ...
    def assertFalse(self, expr, msg=None):
        """Check that the expression is false."""
    def assertGreater(self, a, b, msg=None):
        """Just like self.assertTrue(a > b), but with a nicer default message."""
    def assertGreaterEqual(self, a, b, msg=None):
        """Just like self.assertTrue(a >= b), but with a nicer default message."""
    def assertIn(self, member, container, msg=None):
        """Just like self.assertTrue(a in b), but with a nicer default message."""
    def assertIs(self, expr1, expr2, msg=None):
        """Just like self.assertTrue(a is b), but with a nicer default message."""
    def assertIsInstance(self, obj, cls, msg=None):
        """Same as self.assertTrue(isinstance(obj, cls)), with a nicer"""
    def assertIsNone(self, obj, msg=None):
        """Same as self.assertTrue(obj is None), with a nicer default message."""
    def assertIsNot(self, expr1, expr2, msg=None):
        """Just like self.assertTrue(a is not b), but with a nicer default message."""
    def assertIsNotNone(self, obj, msg=None):
        """Included for symmetry with assertIsNone."""
    def assertLess(self, a, b, msg=None):
        """Just like self.assertTrue(a < b), but with a nicer default message."""
    def assertLessEqual(self, a, b, msg=None):
        """Just like self.assertTrue(a <= b), but with a nicer default message."""
    def assertListEqual(self, list1, list2, msg=None):
        """A list-specific equality assertion."""
    def assertLogs(self, logger=None, level=None):
        """Fail unless a log message of level *level* or higher is emitted"""
    def assertMultiLineEqual(self, first, second, msg=None):
        """Assert that two multi-line strings are equal."""
    def assertNoLogs(self, logger=None, level=None):
        """Fail unless no log messages of level *level* or higher are emitted"""
    def assertNotAlmostEqual(self, first, second, places=None, msg=None, delta=None):
        """Fail if the two objects are equal as determined by their"""
    def assertNotAlmostEquals(*args, **kwargs): ...
    def assertNotEqual(self, first, second, msg=None):
        """Fail if the two objects are equal as determined by the '!='"""
    def assertNotEquals(*args, **kwargs): ...
    def assertNotIn(self, member, container, msg=None):
        """Just like self.assertTrue(a not in b), but with a nicer default message."""
    def assertNotIsInstance(self, obj, cls, msg=None):
        """Included for symmetry with assertIsInstance."""
    def assertNotRegex(self, text, unexpected_regex, msg=None):
        """Fail the test if the text matches the regular expression."""
    def assertNotRegexpMatches(*args, **kwargs): ...
    def assertRaises(self, expected_exception, *args, **kwargs):
        """Fail unless an exception of class expected_exception is raised"""
    def assertRaisesRegex(self, expected_exception, expected_regex, *args, **kwargs):
        """Asserts that the message in a raised exception matches a regex."""
    def assertRaisesRegexp(*args, **kwargs): ...
    def assertRegex(self, text, expected_regex, msg=None):
        """Fail the test unless the text matches the regular expression."""
    def assertRegexpMatches(*args, **kwargs): ...
    def assertSequenceEqual(self, seq1, seq2, msg=None, seq_type=None):
        """An equality assertion for ordered sequences (like lists and tuples)."""
    def assertSetEqual(self, set1, set2, msg=None):
        """A set-specific equality assertion."""
    def assertTrue(self, expr, msg=None):
        """Check that the expression is true."""
    def assertTupleEqual(self, tuple1, tuple2, msg=None):
        """A tuple-specific equality assertion."""
    def assertWarns(self, expected_warning, *args, **kwargs):
        """Fail unless a warning of class warnClass is triggered"""
    def assertWarnsRegex(self, expected_warning, expected_regex, *args, **kwargs):
        """Asserts that the message in a triggered warning matches a regexp."""
    def assert_(*args, **kwargs): ...
    def countTestCases(self): ...
    def debug(self):
        """Run the test without collecting errors in a TestResult"""
    def defaultTestResult(self): ...
    def doClassCleanups():
        """Execute all class cleanup functions. Normally called for you after"""
    def doCleanups(self):
        """Execute all cleanup functions. Normally called for you after"""
    def fail(self, msg=None):
        """Fail immediately, with the given message."""
    def failIf(*args, **kwargs): ...
    def failIfAlmostEqual(*args, **kwargs): ...
    def failIfEqual(*args, **kwargs): ...
    def failUnless(*args, **kwargs): ...
    def failUnlessAlmostEqual(*args, **kwargs): ...
    def failUnlessEqual(*args, **kwargs): ...
    def failUnlessRaises(*args, **kwargs): ...
    def failureException(*args: Any, **kwargs: Any):
        """Assertion failed."""
    def id(self): ...
    longMessage: Any
    maxDiff: Any
    def run(self, result=None): ...
    def setUp(self):
        """Hook method for setting up the test fixture before exercising it."""
    def setUpClass():
        """Hook method for setting up class fixture before running tests in the class."""
    def shortDescription(self):
        """Returns a one-line description of the test, or None if no"""
    def skipTest(self, reason):
        """Skip this test."""
    def subTest(self, msg=..., **params):
        """Return a context manager that will return the enclosed block"""
    def tearDown(self):
        """Hook method for deconstructing the test fixture after testing it."""
    def tearDownClass():
        """Hook method for deconstructing the class fixture after running all tests in the class."""
    def test_class_decoration(self):
        """Test for use of the debugclass decorator"""
    def test_method_decoration(self):
        """Test for use of the debugmethod decorator"""
    def test_private(self):
        """Test for private method decorator"""

def arguments_as_string(*args, **kwargs):
    """Convert the function argument list to a representative string"""

def debugclass(cls):
    """Decorator that attaches to a class in order to attach the debugmethod decorator to all methods in that class."""

def debugmethod(func):
    """Decorator that will print the function signature and return value of a function when DebugDecorator is enabled."""

functools: Any

inspect: Any

class object:
    ...

def private(method):
    """Use this decorator to force a class method to be really private"""

re: Any

standard_library: Any

types: Any

unittest: Any

