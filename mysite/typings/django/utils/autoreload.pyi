"""
This type stub file was generated by pyright.
"""

from functools import lru_cache
from django.utils.functional import cached_property

"""
This type stub file was generated by pyright.
"""
autoreload_started = ...
file_changed = ...
DJANGO_AUTORELOAD_ENV = ...
logger = ...
_error_files = ...
_exception = ...
def is_django_module(module):
    """Return True if the given module is nested under Django."""
    ...

def is_django_path(path):
    """Return True if the given file path is nested under Django."""
    ...

def check_errors(fn):
    ...

def raise_last_exception():
    ...

def ensure_echo_on():
    """
    Ensure that echo mode is enabled. Some tools such as PDB disable
    it which causes usability issues after reload.
    """
    ...

def iter_all_python_module_files():
    ...

@lru_cache(maxsize=1)
def iter_modules_and_files(modules, extra_files):
    """Iterate through all modules needed to be watched."""
    ...

@lru_cache(maxsize=1)
def common_roots(paths):
    """
    Return a tuple of common roots that are shared between the given paths.
    File system watchers operate on directories and aren't cheap to create.
    Try to find the minimum set of directories to watch that encompass all of
    the files that need to be watched.
    """
    ...

def sys_path_directories():
    """
    Yield absolute directories from sys.path, ignoring entries that don't
    exist.
    """
    ...

def get_child_arguments():
    """
    Return the executable. This contains a workaround for Windows if the
    executable is reported to not have the .exe extension which can cause bugs
    on reloading.
    """
    ...

def trigger_reload(filename):
    ...

def restart_with_reloader():
    ...

class BaseReloader:
    def __init__(self) -> None:
        ...
    
    def watch_dir(self, path, glob):
        ...
    
    def watched_files(self, include_globs=...):
        """
        Yield all files that need to be watched, including module files and
        files within globs.
        """
        ...
    
    def wait_for_apps_ready(self, app_reg, django_main_thread):
        """
        Wait until Django reports that the apps have been loaded. If the given
        thread has terminated before the apps are ready, then a SyntaxError or
        other non-recoverable error has been raised. In that case, stop waiting
        for the apps_ready event and continue processing.

        Return True if the thread is alive and the ready event has been
        triggered, or False if the thread is terminated while waiting for the
        event.
        """
        ...
    
    def run(self, django_main_thread):
        ...
    
    def run_loop(self):
        ...
    
    def tick(self):
        """
        This generator is called in a loop from run_loop. It's important that
        the method takes care of pausing or otherwise waiting for a period of
        time. This split between run_loop() and tick() is to improve the
        testability of the reloader implementations by decoupling the work they
        do from the loop.
        """
        ...
    
    @classmethod
    def check_availability(cls):
        ...
    
    def notify_file_changed(self, path):
        ...
    
    @property
    def should_stop(self):
        ...
    
    def stop(self):
        ...
    


class StatReloader(BaseReloader):
    SLEEP_TIME = ...
    def tick(self):
        ...
    
    def snapshot_files(self):
        ...
    
    @classmethod
    def check_availability(cls):
        ...
    


class WatchmanUnavailable(RuntimeError):
    ...


class WatchmanReloader(BaseReloader):
    def __init__(self) -> None:
        ...
    
    @cached_property
    def client(self):
        ...
    
    def watched_roots(self, watched_files):
        ...
    
    def update_watches(self):
        ...
    
    def request_processed(self, **kwargs):
        ...
    
    def tick(self):
        ...
    
    def stop(self):
        ...
    
    def check_server_status(self, inner_ex=...):
        """Return True if the server is available."""
        ...
    
    @classmethod
    def check_availability(cls):
        ...
    


def get_reloader():
    """Return the most suitable reloader for this environment."""
    ...

def start_django(reloader, main_func, *args, **kwargs):
    ...

def run_with_reloader(main_func, *args, **kwargs):
    ...

