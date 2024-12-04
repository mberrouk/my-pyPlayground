"""
This type stub file was generated by pyright.
"""

from contextlib import contextmanager

"""
This type stub file was generated by pyright.
"""
__all__ = ("Approximate", "ContextList", "isolate_lru_cache", "garbage_collect", "get_runner", "CaptureQueriesContext", "ignore_warnings", "isolate_apps", "modify_settings", "override_settings", "override_system_checks", "tag", "requires_tz_support", "setup_databases", "setup_test_environment", "teardown_test_environment")
TZ_SUPPORT = ...
class Approximate:
    def __init__(self, val, places=...) -> None:
        ...
    
    def __repr__(self):
        ...
    
    def __eq__(self, other) -> bool:
        ...
    


class ContextList(list):
    """
    A wrapper that provides direct key access to context items contained
    in a list of context objects.
    """
    def __getitem__(self, key):
        ...
    
    def get(self, key, default=...):
        ...
    
    def __contains__(self, key):
        ...
    
    def keys(self):
        """
        Flattened keys of subcontexts.
        """
        ...
    


def instrumented_test_render(self, context):
    """
    An instrumented Template render method, providing a signal that can be
    intercepted by the test Client.
    """
    ...

class _TestState:
    ...


def setup_test_environment(debug=...):
    """
    Perform global pre-test setup, such as installing the instrumented template
    renderer and setting the email backend to the locmem email backend.
    """
    ...

def teardown_test_environment():
    """
    Perform any global post-test teardown, such as restoring the original
    template renderer and restoring the email sending functions.
    """
    ...

def setup_databases(verbosity, interactive, *, time_keeper=..., keepdb=..., debug_sql=..., parallel=..., aliases=..., serialized_aliases=..., **kwargs):
    """Create the test databases."""
    ...

def iter_test_cases(tests):
    """
    Return an iterator over a test suite's unittest.TestCase objects.

    The tests argument can also be an iterable of TestCase objects.
    """
    ...

def dependency_ordered(test_databases, dependencies):
    """
    Reorder test_databases into an order that honors the dependencies
    described in TEST[DEPENDENCIES].
    """
    ...

def get_unique_databases_and_mirrors(aliases=...):
    """
    Figure out which databases actually need to be created.

    Deduplicate entries in DATABASES that correspond the same database or are
    configured as test mirrors.

    Return two values:
    - test_databases: ordered mapping of signatures to (name, list of aliases)
                      where all aliases share the same underlying database.
    - mirrored_aliases: mapping of mirror aliases to original aliases.
    """
    ...

def teardown_databases(old_config, verbosity, parallel=..., keepdb=...):
    """Destroy all the non-mirror databases."""
    ...

def get_runner(settings, test_runner_class=...):
    ...

class TestContextDecorator:
    """
    A base class that can either be used as a context manager during tests
    or as a test function or unittest.TestCase subclass decorator to perform
    temporary alterations.

    `attr_name`: attribute assigned the return value of enable() if used as
                 a class decorator.

    `kwarg_name`: keyword argument passing the return value of enable() if
                  used as a function decorator.
    """
    def __init__(self, attr_name=..., kwarg_name=...) -> None:
        ...
    
    def enable(self):
        ...
    
    def disable(self):
        ...
    
    def __enter__(self):
        ...
    
    def __exit__(self, exc_type, exc_value, traceback):
        ...
    
    def decorate_class(self, cls):
        ...
    
    def decorate_callable(self, func):
        ...
    
    def __call__(self, decorated):
        ...
    


class override_settings(TestContextDecorator):
    """
    Act as either a decorator or a context manager. If it's a decorator, take a
    function and return a wrapped function. If it's a contextmanager, use it
    with the ``with`` statement. In either event, entering/exiting are called
    before and after, respectively, the function/block is executed.
    """
    enable_exception = ...
    def __init__(self, **kwargs) -> None:
        ...
    
    def enable(self):
        ...
    
    def disable(self):
        ...
    
    def save_options(self, test_func):
        ...
    
    def decorate_class(self, cls):
        ...
    


class modify_settings(override_settings):
    """
    Like override_settings, but makes it possible to append, prepend, or remove
    items instead of redefining the entire list.
    """
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def save_options(self, test_func):
        ...
    
    def enable(self):
        ...
    


class override_system_checks(TestContextDecorator):
    """
    Act as a decorator. Override list of registered system checks.
    Useful when you override `INSTALLED_APPS`, e.g. if you exclude `auth` app,
    you also need to exclude its system checks.
    """
    def __init__(self, new_checks, deployment_checks=...) -> None:
        ...
    
    def enable(self):
        ...
    
    def disable(self):
        ...
    


def compare_xml(want, got):
    """
    Try to do a 'xml-comparison' of want and got. Plain string comparison
    doesn't always work because, for example, attribute ordering should not be
    important. Ignore comment nodes, processing instructions, document type
    node, and leading and trailing whitespaces.

    Based on https://github.com/lxml/lxml/blob/master/src/lxml/doctestcompare.py
    """
    ...

class CaptureQueriesContext:
    """
    Context manager that captures queries executed by the specified connection.
    """
    def __init__(self, connection) -> None:
        ...
    
    def __iter__(self):
        ...
    
    def __getitem__(self, index):
        ...
    
    def __len__(self):
        ...
    
    @property
    def captured_queries(self):
        ...
    
    def __enter__(self):
        ...
    
    def __exit__(self, exc_type, exc_value, traceback):
        ...
    


class ignore_warnings(TestContextDecorator):
    def __init__(self, **kwargs) -> None:
        ...
    
    def enable(self):
        ...
    
    def disable(self):
        ...
    


requires_tz_support = ...
@contextmanager
def extend_sys_path(*paths):
    """Context manager to temporarily add paths to sys.path."""
    ...

@contextmanager
def isolate_lru_cache(lru_cache_object):
    """Clear the cache of an LRU cache object on entering and exiting."""
    ...

@contextmanager
def captured_output(stream_name):
    """Return a context manager used by captured_stdout/stdin/stderr
    that temporarily replaces the sys stream *stream_name* with a StringIO.

    Note: This function and the following ``captured_std*`` are copied
          from CPython's ``test.support`` module."""
    ...

def captured_stdout():
    """Capture the output of sys.stdout:

    with captured_stdout() as stdout:
        print("hello")
    self.assertEqual(stdout.getvalue(), "hello\n")
    """
    ...

def captured_stderr():
    """Capture the output of sys.stderr:

    with captured_stderr() as stderr:
        print("hello", file=sys.stderr)
    self.assertEqual(stderr.getvalue(), "hello\n")
    """
    ...

def captured_stdin():
    """Capture the input to sys.stdin:

    with captured_stdin() as stdin:
        stdin.write('hello\n')
        stdin.seek(0)
        # call test code that consumes from sys.stdin
        captured = input()
    self.assertEqual(captured, "hello")
    """
    ...

@contextmanager
def freeze_time(t):
    """
    Context manager to temporarily freeze time.time(). This temporarily
    modifies the time function of the time module. Modules which import the
    time function directly (e.g. `from time import time`) won't be affected
    This isn't meant as a public API, but helps reduce some repetitive code in
    Django's test suite.
    """
    ...

def require_jinja2(test_func):
    """
    Decorator to enable a Jinja2 template engine in addition to the regular
    Django template engine for a test or skip it if Jinja2 isn't available.
    """
    ...

class override_script_prefix(TestContextDecorator):
    """Decorator or context manager to temporary override the script prefix."""
    def __init__(self, prefix) -> None:
        ...
    
    def enable(self):
        ...
    
    def disable(self):
        ...
    


class LoggingCaptureMixin:
    """
    Capture the output from the 'django' logger and store it on the class's
    logger_output attribute.
    """
    def setUp(self):
        ...
    
    def tearDown(self):
        ...
    


class isolate_apps(TestContextDecorator):
    """
    Act as either a decorator or a context manager to register models defined
    in its wrapped context to an isolated registry.

    The list of installed apps the isolated registry should contain must be
    passed as arguments.

    Two optional keyword arguments can be specified:

    `attr_name`: attribute assigned the isolated registry if used as a class
                 decorator.

    `kwarg_name`: keyword argument passing the isolated registry if used as a
                  function decorator.
    """
    def __init__(self, *installed_apps, **kwargs) -> None:
        ...
    
    def enable(self):
        ...
    
    def disable(self):
        ...
    


class TimeKeeper:
    def __init__(self) -> None:
        ...
    
    @contextmanager
    def timed(self, name):
        ...
    
    def print_results(self):
        ...
    


class NullTimeKeeper:
    @contextmanager
    def timed(self, name):
        ...
    
    def print_results(self):
        ...
    


def tag(*tags):
    """Decorator to add tags to a test class or method."""
    ...

@contextmanager
def register_lookup(field, *lookups, lookup_name=...):
    """
    Context manager to temporarily register lookups on a model field using
    lookup_name (or the lookup's lookup_name if not provided).
    """
    ...

def garbage_collect():
    ...
