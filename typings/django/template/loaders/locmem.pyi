from .base import Loader as BaseLoader
from _typeshed import Incomplete
from collections.abc import Generator
from django.template import Origin as Origin, TemplateDoesNotExist as TemplateDoesNotExist

class Loader(BaseLoader):
    templates_dict: Incomplete
    def __init__(self, engine, templates_dict) -> None: ...
    def get_contents(self, origin): ...
    def get_template_sources(self, template_name) -> Generator[Incomplete]: ...
