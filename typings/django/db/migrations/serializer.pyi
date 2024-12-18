from _typeshed import Incomplete
from django.conf import SettingsReference as SettingsReference
from django.db import models as models
from django.db.migrations.operations.base import Operation as Operation
from django.db.migrations.utils import COMPILED_REGEX_TYPE as COMPILED_REGEX_TYPE, RegexObject as RegexObject
from django.utils.functional import LazyObject as LazyObject, Promise as Promise
from django.utils.version import PY311 as PY311, get_docs_version as get_docs_version

FUNCTION_TYPES: Incomplete

class BaseSerializer:
    value: Incomplete
    def __init__(self, value) -> None: ...
    def serialize(self) -> None: ...

class BaseSequenceSerializer(BaseSerializer):
    def serialize(self): ...

class BaseUnorderedSequenceSerializer(BaseSequenceSerializer):
    def __init__(self, value) -> None: ...

class BaseSimpleSerializer(BaseSerializer):
    def serialize(self): ...

class ChoicesSerializer(BaseSerializer):
    def serialize(self): ...

class DateTimeSerializer(BaseSerializer):
    def serialize(self): ...

class DatetimeDatetimeSerializer(BaseSerializer):
    value: Incomplete
    def serialize(self): ...

class DecimalSerializer(BaseSerializer):
    def serialize(self): ...

class DeconstructableSerializer(BaseSerializer):
    @staticmethod
    def serialize_deconstructed(path, args, kwargs): ...
    def serialize(self): ...

class DictionarySerializer(BaseSerializer):
    def serialize(self): ...

class EnumSerializer(BaseSerializer):
    def serialize(self): ...

class FloatSerializer(BaseSimpleSerializer):
    def serialize(self): ...

class FrozensetSerializer(BaseUnorderedSequenceSerializer): ...

class FunctionTypeSerializer(BaseSerializer):
    def serialize(self): ...

class FunctoolsPartialSerializer(BaseSerializer):
    def serialize(self): ...

class IterableSerializer(BaseSerializer):
    def serialize(self): ...

class ModelFieldSerializer(DeconstructableSerializer):
    def serialize(self): ...

class ModelManagerSerializer(DeconstructableSerializer):
    def serialize(self): ...

class OperationSerializer(BaseSerializer):
    def serialize(self): ...

class PathLikeSerializer(BaseSerializer):
    def serialize(self): ...

class PathSerializer(BaseSerializer):
    def serialize(self): ...

class RegexSerializer(BaseSerializer):
    def serialize(self): ...

class SequenceSerializer(BaseSequenceSerializer): ...
class SetSerializer(BaseUnorderedSequenceSerializer): ...

class SettingsReferenceSerializer(BaseSerializer):
    def serialize(self): ...

class TupleSerializer(BaseSequenceSerializer): ...

class TypeSerializer(BaseSerializer):
    def serialize(self): ...

class UUIDSerializer(BaseSerializer):
    def serialize(self): ...

class Serializer:
    @classmethod
    def register(cls, type_, serializer) -> None: ...
    @classmethod
    def unregister(cls, type_) -> None: ...

def serializer_factory(value): ...