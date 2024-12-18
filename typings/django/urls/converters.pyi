from _typeshed import Incomplete
from django.utils.deprecation import RemovedInDjango60Warning as RemovedInDjango60Warning

class IntConverter:
    regex: str
    def to_python(self, value): ...
    def to_url(self, value): ...

class StringConverter:
    regex: str
    def to_python(self, value): ...
    def to_url(self, value): ...

class UUIDConverter:
    regex: str
    def to_python(self, value): ...
    def to_url(self, value): ...

class SlugConverter(StringConverter):
    regex: str

class PathConverter(StringConverter):
    regex: str

DEFAULT_CONVERTERS: Incomplete
REGISTERED_CONVERTERS: Incomplete

def register_converter(converter, type_name) -> None: ...
def get_converters(): ...
