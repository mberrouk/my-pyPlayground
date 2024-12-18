from .base import BaseEngine as BaseEngine
from .utils import csrf_input_lazy as csrf_input_lazy, csrf_token_lazy as csrf_token_lazy
from _typeshed import Incomplete
from django.conf import settings as settings
from django.template import TemplateDoesNotExist as TemplateDoesNotExist, TemplateSyntaxError as TemplateSyntaxError
from django.utils.functional import cached_property as cached_property
from django.utils.module_loading import import_string as import_string

class Jinja2(BaseEngine):
    app_dirname: str
    context_processors: Incomplete
    env: Incomplete
    def __init__(self, params) -> None: ...
    def from_string(self, template_code): ...
    def get_template(self, template_name): ...
    def template_context_processors(self): ...

class Template:
    template: Incomplete
    backend: Incomplete
    origin: Incomplete
    def __init__(self, template, backend) -> None: ...
    def render(self, context: Incomplete | None = None, request: Incomplete | None = None): ...

class Origin:
    name: Incomplete
    template_name: Incomplete
    def __init__(self, name, template_name) -> None: ...

def get_exception_info(exception): ...
