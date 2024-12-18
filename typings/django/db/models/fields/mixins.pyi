from _typeshed import Incomplete
from django.core import checks as checks
from django.utils.deprecation import RemovedInDjango60Warning as RemovedInDjango60Warning
from django.utils.functional import cached_property as cached_property

NOT_PROVIDED: Incomplete

class FieldCacheMixin:
    def get_cache_name(self) -> None: ...
    def cache_name(self): ...
    def get_cached_value(self, instance, default=...): ...
    def is_cached(self, instance): ...
    def set_cached_value(self, instance, value) -> None: ...
    def delete_cached_value(self, instance) -> None: ...

class CheckFieldDefaultMixin:
    def check(self, **kwargs): ...
