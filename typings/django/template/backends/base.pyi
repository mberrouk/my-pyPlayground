from _typeshed import Incomplete
from collections.abc import Generator
from django.core.exceptions import ImproperlyConfigured as ImproperlyConfigured, SuspiciousFileOperation as SuspiciousFileOperation
from django.template.utils import get_app_template_dirs as get_app_template_dirs
from django.utils._os import safe_join as safe_join
from django.utils.functional import cached_property as cached_property

class BaseEngine:
    name: Incomplete
    dirs: Incomplete
    app_dirs: Incomplete
    def __init__(self, params) -> None: ...
    def check(self, **kwargs): ...
    @property
    def app_dirname(self) -> None: ...
    def from_string(self, template_code) -> None: ...
    def get_template(self, template_name) -> None: ...
    def template_dirs(self): ...
    def iter_template_filenames(self, template_name) -> Generator[Incomplete]: ...
