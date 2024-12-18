from _typeshed import Incomplete
from django.forms.widgets import CheckboxInput, ClearableFileInput, DateInput, DateTimeInput, EmailInput, HiddenInput, MultipleHiddenInput, NullBooleanSelect, NumberInput, Select, SelectMultiple, SplitDateTimeWidget, SplitHiddenDateTimeWidget, TextInput, Textarea, TimeInput, URLInput

__all__ = ['Field', 'CharField', 'IntegerField', 'DateField', 'TimeField', 'DateTimeField', 'DurationField', 'RegexField', 'EmailField', 'FileField', 'ImageField', 'URLField', 'BooleanField', 'NullBooleanField', 'ChoiceField', 'MultipleChoiceField', 'ComboField', 'MultiValueField', 'FloatField', 'DecimalField', 'SplitDateTimeField', 'GenericIPAddressField', 'FilePathField', 'JSONField', 'SlugField', 'TypedChoiceField', 'TypedMultipleChoiceField', 'UUIDField']

class Field:
    widget = TextInput
    hidden_widget = HiddenInput
    default_validators: Incomplete
    default_error_messages: Incomplete
    empty_values: Incomplete
    show_hidden_initial: Incomplete
    help_text: Incomplete
    disabled: Incomplete
    label_suffix: Incomplete
    localize: Incomplete
    error_messages: Incomplete
    validators: Incomplete
    template_name: Incomplete
    def __init__(self, *, required: bool = True, widget: Incomplete | None = None, label: Incomplete | None = None, initial: Incomplete | None = None, help_text: str = '', error_messages: Incomplete | None = None, show_hidden_initial: bool = False, validators=(), localize: bool = False, disabled: bool = False, label_suffix: Incomplete | None = None, template_name: Incomplete | None = None) -> None: ...
    def prepare_value(self, value): ...
    def to_python(self, value): ...
    def validate(self, value) -> None: ...
    def run_validators(self, value) -> None: ...
    def clean(self, value): ...
    def bound_data(self, data, initial): ...
    def widget_attrs(self, widget): ...
    def has_changed(self, initial, data): ...
    def get_bound_field(self, form, field_name): ...
    def __deepcopy__(self, memo): ...

class CharField(Field):
    max_length: Incomplete
    min_length: Incomplete
    strip: Incomplete
    empty_value: Incomplete
    def __init__(self, *, max_length: Incomplete | None = None, min_length: Incomplete | None = None, strip: bool = True, empty_value: str = '', **kwargs) -> None: ...
    def to_python(self, value): ...
    def widget_attrs(self, widget): ...

class IntegerField(Field):
    widget = NumberInput
    default_error_messages: Incomplete
    re_decimal: Incomplete
    def __init__(self, *, max_value: Incomplete | None = None, min_value: Incomplete | None = None, step_size: Incomplete | None = None, **kwargs) -> None: ...
    def to_python(self, value): ...
    def widget_attrs(self, widget): ...

class FloatField(IntegerField):
    default_error_messages: Incomplete
    def to_python(self, value): ...
    def validate(self, value) -> None: ...
    def widget_attrs(self, widget): ...

class DecimalField(IntegerField):
    default_error_messages: Incomplete
    def __init__(self, *, max_value: Incomplete | None = None, min_value: Incomplete | None = None, max_digits: Incomplete | None = None, decimal_places: Incomplete | None = None, **kwargs) -> None: ...
    def to_python(self, value): ...
    def validate(self, value) -> None: ...
    def widget_attrs(self, widget): ...

class BaseTemporalField(Field):
    input_formats: Incomplete
    def __init__(self, *, input_formats: Incomplete | None = None, **kwargs) -> None: ...
    def to_python(self, value): ...
    def strptime(self, value, format) -> None: ...

class DateField(BaseTemporalField):
    widget = DateInput
    input_formats: Incomplete
    default_error_messages: Incomplete
    def to_python(self, value): ...
    def strptime(self, value, format): ...

class TimeField(BaseTemporalField):
    widget = TimeInput
    input_formats: Incomplete
    default_error_messages: Incomplete
    def to_python(self, value): ...
    def strptime(self, value, format): ...

class DateTimeFormatsIterator:
    def __iter__(self): ...

class DateTimeField(BaseTemporalField):
    widget = DateTimeInput
    input_formats: Incomplete
    default_error_messages: Incomplete
    def prepare_value(self, value): ...
    def to_python(self, value): ...
    def strptime(self, value, format): ...

class DurationField(Field):
    default_error_messages: Incomplete
    def prepare_value(self, value): ...
    def to_python(self, value): ...

class RegexField(CharField):
    def __init__(self, regex, **kwargs) -> None: ...
    regex: Incomplete

class EmailField(CharField):
    widget = EmailInput
    default_validators: Incomplete
    def __init__(self, **kwargs) -> None: ...

class FileField(Field):
    widget = ClearableFileInput
    default_error_messages: Incomplete
    max_length: Incomplete
    allow_empty_file: Incomplete
    def __init__(self, *, max_length: Incomplete | None = None, allow_empty_file: bool = False, **kwargs) -> None: ...
    def to_python(self, data): ...
    def clean(self, data, initial: Incomplete | None = None): ...
    def bound_data(self, _, initial): ...
    def has_changed(self, initial, data): ...

class ImageField(FileField):
    default_validators: Incomplete
    default_error_messages: Incomplete
    def to_python(self, data): ...
    def widget_attrs(self, widget): ...

class URLField(CharField):
    widget = URLInput
    default_error_messages: Incomplete
    default_validators: Incomplete
    assume_scheme: Incomplete
    def __init__(self, *, assume_scheme: Incomplete | None = None, **kwargs) -> None: ...
    def to_python(self, value): ...

class BooleanField(Field):
    widget = CheckboxInput
    def to_python(self, value): ...
    def validate(self, value) -> None: ...
    def has_changed(self, initial, data): ...

class NullBooleanField(BooleanField):
    widget = NullBooleanSelect
    def to_python(self, value): ...
    def validate(self, value) -> None: ...

class ChoiceField(Field):
    widget = Select
    default_error_messages: Incomplete
    def __init__(self, *, choices=(), **kwargs) -> None: ...
    def __deepcopy__(self, memo): ...
    @property
    def choices(self): ...
    @choices.setter
    def choices(self, value) -> None: ...
    def to_python(self, value): ...
    def validate(self, value) -> None: ...
    def valid_value(self, value): ...

class TypedChoiceField(ChoiceField):
    coerce: Incomplete
    empty_value: Incomplete
    def __init__(self, *, coerce=..., empty_value: str = '', **kwargs) -> None: ...
    def clean(self, value): ...

class MultipleChoiceField(ChoiceField):
    hidden_widget = MultipleHiddenInput
    widget = SelectMultiple
    default_error_messages: Incomplete
    def to_python(self, value): ...
    def validate(self, value) -> None: ...
    def has_changed(self, initial, data): ...

class TypedMultipleChoiceField(MultipleChoiceField):
    coerce: Incomplete
    empty_value: Incomplete
    def __init__(self, *, coerce=..., **kwargs) -> None: ...
    def clean(self, value): ...
    def validate(self, value) -> None: ...

class ComboField(Field):
    fields: Incomplete
    def __init__(self, fields, **kwargs) -> None: ...
    def clean(self, value): ...

class MultiValueField(Field):
    default_error_messages: Incomplete
    require_all_fields: Incomplete
    fields: Incomplete
    def __init__(self, fields, *, require_all_fields: bool = True, **kwargs) -> None: ...
    def __deepcopy__(self, memo): ...
    def validate(self, value) -> None: ...
    def clean(self, value): ...
    def compress(self, data_list) -> None: ...
    def has_changed(self, initial, data): ...

class FilePathField(ChoiceField):
    choices: Incomplete
    match_re: Incomplete
    def __init__(self, path, *, match: Incomplete | None = None, recursive: bool = False, allow_files: bool = True, allow_folders: bool = False, **kwargs) -> None: ...

class SplitDateTimeField(MultiValueField):
    widget = SplitDateTimeWidget
    hidden_widget = SplitHiddenDateTimeWidget
    default_error_messages: Incomplete
    def __init__(self, *, input_date_formats: Incomplete | None = None, input_time_formats: Incomplete | None = None, **kwargs) -> None: ...
    def compress(self, data_list): ...

class GenericIPAddressField(CharField):
    unpack_ipv4: Incomplete
    default_validators: Incomplete
    def __init__(self, *, protocol: str = 'both', unpack_ipv4: bool = False, **kwargs) -> None: ...
    def to_python(self, value): ...

class SlugField(CharField):
    default_validators: Incomplete
    allow_unicode: Incomplete
    def __init__(self, *, allow_unicode: bool = False, **kwargs) -> None: ...

class UUIDField(CharField):
    default_error_messages: Incomplete
    def prepare_value(self, value): ...
    def to_python(self, value): ...

class InvalidJSONInput(str): ...
class JSONString(str): ...

class JSONField(CharField):
    default_error_messages: Incomplete
    widget = Textarea
    encoder: Incomplete
    decoder: Incomplete
    def __init__(self, encoder: Incomplete | None = None, decoder: Incomplete | None = None, **kwargs) -> None: ...
    def to_python(self, value): ...
    def bound_data(self, data, initial): ...
    def prepare_value(self, value): ...
    def has_changed(self, initial, data): ...