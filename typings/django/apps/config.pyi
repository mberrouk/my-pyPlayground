from _typeshed import Incomplete
from collections.abc import Generator
from django.core.exceptions import ImproperlyConfigured as ImproperlyConfigured
from django.utils.functional import cached_property as cached_property
from django.utils.module_loading import import_string as import_string, module_has_submodule as module_has_submodule

APPS_MODULE_NAME: str
MODELS_MODULE_NAME: str

class AppConfig:
    name: Incomplete
    module: Incomplete
    apps: Incomplete
    label: Incomplete
    verbose_name: Incomplete
    path: Incomplete
    models_module: Incomplete
    models: Incomplete
    def __init__(self, app_name, app_module) -> None: ...
    def default_auto_field(self): ...
    @classmethod
    def create(cls, entry): ...
    def get_model(self, model_name, require_ready: bool = True): ...
    def get_models(self, include_auto_created: bool = False, include_swapped: bool = False) -> Generator[Incomplete]: ...
    def import_models(self) -> None: ...
    def ready(self) -> None: ...
