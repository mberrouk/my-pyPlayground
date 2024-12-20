from _typeshed import Incomplete
from django import forms as forms
from django.core import checks as checks
from django.core.exceptions import FieldError as FieldError
from django.core.files.base import ContentFile as ContentFile, File as File
from django.core.files.images import ImageFile as ImageFile
from django.core.files.storage import Storage as Storage, default_storage as default_storage
from django.core.files.utils import validate_file_name as validate_file_name
from django.db.models import signals as signals
from django.db.models.expressions import DatabaseDefault as DatabaseDefault
from django.db.models.fields import Field as Field
from django.db.models.query_utils import DeferredAttribute as DeferredAttribute
from django.db.models.utils import AltersData as AltersData
from django.utils.version import PY311 as PY311

class FieldFile(File, AltersData):
    instance: Incomplete
    field: Incomplete
    storage: Incomplete
    def __init__(self, instance, field, name) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    file: Incomplete
    @property
    def path(self): ...
    @property
    def url(self): ...
    @property
    def size(self): ...
    def open(self, mode: str = 'rb'): ...
    name: Incomplete
    def save(self, name, content, save: bool = True) -> None: ...
    def delete(self, save: bool = True) -> None: ...
    @property
    def closed(self): ...
    def close(self) -> None: ...

class FileDescriptor(DeferredAttribute):
    def __get__(self, instance, cls: Incomplete | None = None): ...
    def __set__(self, instance, value) -> None: ...

class FileField(Field):
    attr_class = FieldFile
    descriptor_class = FileDescriptor
    description: Incomplete
    storage: Incomplete
    upload_to: Incomplete
    def __init__(self, verbose_name: Incomplete | None = None, name: Incomplete | None = None, upload_to: str = '', storage: Incomplete | None = None, **kwargs) -> None: ...
    def check(self, **kwargs): ...
    def deconstruct(self): ...
    def get_internal_type(self): ...
    def get_prep_value(self, value): ...
    def pre_save(self, model_instance, add): ...
    def contribute_to_class(self, cls, name, **kwargs) -> None: ...
    def generate_filename(self, instance, filename): ...
    def save_form_data(self, instance, data) -> None: ...
    def formfield(self, **kwargs): ...

class ImageFileDescriptor(FileDescriptor):
    def __set__(self, instance, value) -> None: ...

class ImageFieldFile(ImageFile, FieldFile):
    def delete(self, save: bool = True) -> None: ...

class ImageField(FileField):
    attr_class = ImageFieldFile
    descriptor_class = ImageFileDescriptor
    description: Incomplete
    def __init__(self, verbose_name: Incomplete | None = None, name: Incomplete | None = None, width_field: Incomplete | None = None, height_field: Incomplete | None = None, **kwargs) -> None: ...
    def check(self, **kwargs): ...
    def deconstruct(self): ...
    def contribute_to_class(self, cls, name, **kwargs) -> None: ...
    def update_dimension_fields(self, instance, force: bool = False, *args, **kwargs) -> None: ...
    def formfield(self, **kwargs): ...
