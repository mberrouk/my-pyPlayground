import string
from .base import BaseEngine as BaseEngine
from .utils import csrf_input_lazy as csrf_input_lazy, csrf_token_lazy as csrf_token_lazy
from _typeshed import Incomplete
from django.core.exceptions import ImproperlyConfigured as ImproperlyConfigured
from django.template import Origin as Origin, TemplateDoesNotExist as TemplateDoesNotExist
from django.utils.html import conditional_escape as conditional_escape

class TemplateStrings(BaseEngine):
    app_dirname: str
    def __init__(self, params) -> None: ...
    def from_string(self, template_code): ...
    def get_template(self, template_name): ...

class Template(string.Template):
    def render(self, context: Incomplete | None = None, request: Incomplete | None = None): ...
