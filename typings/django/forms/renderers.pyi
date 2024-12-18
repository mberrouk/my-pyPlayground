from _typeshed import Incomplete
from django.conf import settings as settings
from django.template.backends.django import DjangoTemplates as DjangoTemplates
from django.template.loader import get_template as get_template
from django.utils.deprecation import RemovedInDjango60Warning as RemovedInDjango60Warning
from django.utils.functional import cached_property as cached_property
from django.utils.module_loading import import_string as import_string

def get_default_renderer(): ...

class BaseRenderer:
    form_template_name: str
    formset_template_name: str
    field_template_name: str
    def get_template(self, template_name) -> None: ...
    def render(self, template_name, context, request: Incomplete | None = None): ...

class EngineMixin:
    def get_template(self, template_name): ...
    def engine(self): ...

class DjangoTemplates(EngineMixin, BaseRenderer):
    backend = DjangoTemplates

class Jinja2(EngineMixin, BaseRenderer):
    def backend(self): ...

class DjangoDivFormRenderer(DjangoTemplates):
    def __init__(self, *args, **kwargs) -> None: ...

class Jinja2DivFormRenderer(Jinja2):
    def __init__(self, *args, **kwargs) -> None: ...

class TemplatesSetting(BaseRenderer):
    def get_template(self, template_name): ...
