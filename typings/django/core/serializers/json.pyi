import json
from _typeshed import Incomplete
from collections.abc import Generator
from django.core.serializers.base import DeserializationError as DeserializationError
from django.core.serializers.python import Serializer as PythonSerializer
from django.utils.duration import duration_iso_string as duration_iso_string
from django.utils.functional import Promise as Promise
from django.utils.timezone import is_aware as is_aware

class Serializer(PythonSerializer):
    internal_use_only: bool
    def start_serialization(self) -> None: ...
    def end_serialization(self) -> None: ...
    def end_object(self, obj) -> None: ...
    def getvalue(self): ...

def Deserializer(stream_or_string, **options) -> Generator[Incomplete, Incomplete]: ...

class DjangoJSONEncoder(json.JSONEncoder):
    def default(self, o): ...
