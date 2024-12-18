from _typeshed import Incomplete
from collections.abc import Generator
from django.core.serializers.base import DeserializationError as DeserializationError
from django.core.serializers.python import Serializer as PythonSerializer
from django.db import models as models
from yaml import SafeDumper

class DjangoSafeDumper(SafeDumper):
    def represent_decimal(self, data): ...
    def represent_ordered_dict(self, data): ...

class Serializer(PythonSerializer):
    internal_use_only: bool
    def handle_field(self, obj, field) -> None: ...
    def end_serialization(self) -> None: ...
    def getvalue(self): ...

def Deserializer(stream_or_string, **options) -> Generator[Incomplete, Incomplete]: ...
