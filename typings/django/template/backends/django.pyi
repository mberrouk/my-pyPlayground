from .base import BaseEngine as BaseEngine
from _typeshed import Incomplete
from collections.abc import Generator
from django.apps import apps as apps
from django.conf import settings as settings
from django.core.checks import Error as Error, Warning as Warning
from django.template import TemplateDoesNotExist as TemplateDoesNotExist
from django.template.context import make_context as make_context
from django.template.engine import Engine as Engine
from django.template.library import InvalidTemplateLibrary as InvalidTemplateLibrary

class DjangoTemplates(BaseEngine):
    app_dirname: str
    engine: Incomplete
    def __init__(self, params) -> None: ...
    def check(self, **kwargs): ...
    def from_string(self, template_code): ...
    def get_template(self, template_name): ...
    def get_templatetag_libraries(self, custom_libraries): ...

class Template:
    template: Incomplete
    backend: Incomplete
    def __init__(self, template, backend) -> None: ...
    @property
    def origin(self): ...
    def render(self, context: Incomplete | None = None, request: Incomplete | None = None): ...

def copy_exception(exc, backend: Incomplete | None = None): ...
def reraise(exc, backend) -> None: ...
def get_template_tag_modules() -> Generator[Incomplete]: ...
def get_installed_libraries(): ...
def get_package_libraries(pkg) -> Generator[Incomplete]: ...