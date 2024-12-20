"""
This type stub file was generated by pyright.
"""

from django.forms.widgets import CheckboxInput, ClearableFileInput, DateInput, DateTimeInput, EmailInput, HiddenInput, MultipleHiddenInput, NullBooleanSelect, NumberInput, Select, SelectMultiple, SplitDateTimeWidget, SplitHiddenDateTimeWidget, Textarea, TimeInput, URLInput

"""
This type stub file was generated by pyright.
"""
__all__ = ("Field", "CharField", "IntegerField", "DateField", "TimeField", "DateTimeField", "DurationField", "RegexField", "EmailField", "FileField", "ImageField", "URLField", "BooleanField", "NullBooleanField", "ChoiceField", "MultipleChoiceField", "ComboField", "MultiValueField", "FloatField", "DecimalField", "SplitDateTimeField", "GenericIPAddressField", "FilePathField", "JSONField", "SlugField", "TypedChoiceField", "TypedMultipleChoiceField", "UUIDField")
class Field:
    widget = ...
    hidden_widget = HiddenInput
    default_validators = ...
    default_error_messages = ...
    empty_values = ...
    def __init__(self, *, required=..., widget=..., label=..., initial=..., help_text=..., error_messages=..., show_hidden_initial=..., validators=..., localize=..., disabled=..., label_suffix=..., template_name=...) -> None:
        ...
    
    def prepare_value(self, value):
        ...
    
    def to_python(self, value):
        ...
    
    def validate(self, value):
        ...
    
    def run_validators(self, value):
        ...
    
    def clean(self, value):
        """
        Validate the given value and return its "cleaned" value as an
        appropriate Python object. Raise ValidationError for any errors.
        """
        ...
    
    def bound_data(self, data, initial):
        """
        Return the value that should be shown for this field on render of a
        bound form, given the submitted POST data for the field and the initial
        data, if any.

        For most fields, this will simply be data; FileFields need to handle it
        a bit differently.
        """
        ...
    
    def widget_attrs(self, widget):
        """
        Given a Widget instance (*not* a Widget class), return a dictionary of
        any HTML attributes that should be added to the Widget, based on this
        Field.
        """
        ...
    
    def has_changed(self, initial, data):
        """Return True if data differs from initial."""
        ...
    
    def get_bound_field(self, form, field_name):
        """
        Return a BoundField instance that will be used when accessing the form
        field in a template.
        """
        ...
    
    def __deepcopy__(self, memo):
        ...
    


class CharField(Field):
    def __init__(self, *, max_length=..., min_length=..., strip=..., empty_value=..., **kwargs) -> None:
        ...
    
    def to_python(self, value):
        """Return a string."""
        ...
    
    def widget_attrs(self, widget):
        ...
    


class IntegerField(Field):
    widget = NumberInput
    default_error_messages = ...
    re_decimal = ...
    def __init__(self, *, max_value=..., min_value=..., step_size=..., **kwargs) -> None:
        ...
    
    def to_python(self, value):
        """
        Validate that int() can be called on the input. Return the result
        of int() or None for empty values.
        """
        ...
    
    def widget_attrs(self, widget):
        ...
    


class FloatField(IntegerField):
    default_error_messages = ...
    def to_python(self, value):
        """
        Validate that float() can be called on the input. Return the result
        of float() or None for empty values.
        """
        ...
    
    def validate(self, value):
        ...
    
    def widget_attrs(self, widget):
        ...
    


class DecimalField(IntegerField):
    default_error_messages = ...
    def __init__(self, *, max_value=..., min_value=..., max_digits=..., decimal_places=..., **kwargs) -> None:
        ...
    
    def to_python(self, value):
        """
        Validate that the input is a decimal number. Return a Decimal
        instance or None for empty values. Ensure that there are no more
        than max_digits in the number and no more than decimal_places digits
        after the decimal point.
        """
        ...
    
    def validate(self, value):
        ...
    
    def widget_attrs(self, widget):
        ...
    


class BaseTemporalField(Field):
    def __init__(self, *, input_formats=..., **kwargs) -> None:
        ...
    
    def to_python(self, value):
        ...
    
    def strptime(self, value, format):
        ...
    


class DateField(BaseTemporalField):
    widget = DateInput
    input_formats = ...
    default_error_messages = ...
    def to_python(self, value):
        """
        Validate that the input can be converted to a date. Return a Python
        datetime.date object.
        """
        ...
    
    def strptime(self, value, format):
        ...
    


class TimeField(BaseTemporalField):
    widget = TimeInput
    input_formats = ...
    default_error_messages = ...
    def to_python(self, value):
        """
        Validate that the input can be converted to a time. Return a Python
        datetime.time object.
        """
        ...
    
    def strptime(self, value, format):
        ...
    


class DateTimeFormatsIterator:
    def __iter__(self):
        ...
    


class DateTimeField(BaseTemporalField):
    widget = DateTimeInput
    input_formats = ...
    default_error_messages = ...
    def prepare_value(self, value):
        ...
    
    def to_python(self, value):
        """
        Validate that the input can be converted to a datetime. Return a
        Python datetime.datetime object.
        """
        ...
    
    def strptime(self, value, format):
        ...
    


class DurationField(Field):
    default_error_messages = ...
    def prepare_value(self, value):
        ...
    
    def to_python(self, value):
        ...
    


class RegexField(CharField):
    def __init__(self, regex, **kwargs) -> None:
        """
        regex can be either a string or a compiled regular expression object.
        """
        ...
    
    regex = ...


class EmailField(CharField):
    widget = EmailInput
    default_validators = ...
    def __init__(self, **kwargs) -> None:
        ...
    


class FileField(Field):
    widget = ClearableFileInput
    default_error_messages = ...
    def __init__(self, *, max_length=..., allow_empty_file=..., **kwargs) -> None:
        ...
    
    def to_python(self, data):
        ...
    
    def clean(self, data, initial=...):
        ...
    
    def bound_data(self, _, initial):
        ...
    
    def has_changed(self, initial, data):
        ...
    


class ImageField(FileField):
    default_validators = ...
    default_error_messages = ...
    def to_python(self, data):
        """
        Check that the file-upload field data contains a valid image (GIF, JPG,
        PNG, etc. -- whatever Pillow supports).
        """
        ...
    
    def widget_attrs(self, widget):
        ...
    


class URLField(CharField):
    widget = URLInput
    default_error_messages = ...
    default_validators = ...
    def __init__(self, *, assume_scheme=..., **kwargs) -> None:
        ...
    
    def to_python(self, value):
        ...
    


class BooleanField(Field):
    widget = CheckboxInput
    def to_python(self, value):
        """Return a Python boolean object."""
        ...
    
    def validate(self, value):
        ...
    
    def has_changed(self, initial, data):
        ...
    


class NullBooleanField(BooleanField):
    """
    A field whose valid values are None, True, and False. Clean invalid values
    to None.
    """
    widget = NullBooleanSelect
    def to_python(self, value):
        """
        Explicitly check for the string 'True' and 'False', which is what a
        hidden field will submit for True and False, for 'true' and 'false',
        which are likely to be returned by JavaScript serializations of forms,
        and for '1' and '0', which is what a RadioField will submit. Unlike
        the Booleanfield, this field must check for True because it doesn't
        use the bool() function.
        """
        ...
    
    def validate(self, value):
        ...
    


class ChoiceField(Field):
    widget = Select
    default_error_messages = ...
    def __init__(self, *, choices=..., **kwargs) -> None:
        ...
    
    def __deepcopy__(self, memo):
        ...
    
    @property
    def choices(self):
        ...
    
    @choices.setter
    def choices(self, value):
        ...
    
    def to_python(self, value):
        """Return a string."""
        ...
    
    def validate(self, value):
        """Validate that the input is in self.choices."""
        ...
    
    def valid_value(self, value):
        """Check to see if the provided value is a valid choice."""
        ...
    


class TypedChoiceField(ChoiceField):
    def __init__(self, *, coerce=..., empty_value=..., **kwargs) -> None:
        ...
    
    def clean(self, value):
        ...
    


class MultipleChoiceField(ChoiceField):
    hidden_widget = MultipleHiddenInput
    widget = SelectMultiple
    default_error_messages = ...
    def to_python(self, value):
        ...
    
    def validate(self, value):
        """Validate that the input is a list or tuple."""
        ...
    
    def has_changed(self, initial, data):
        ...
    


class TypedMultipleChoiceField(MultipleChoiceField):
    def __init__(self, *, coerce=..., **kwargs) -> None:
        ...
    
    def clean(self, value):
        ...
    
    def validate(self, value):
        ...
    


class ComboField(Field):
    """
    A Field whose clean() method calls multiple Field clean() methods.
    """
    def __init__(self, fields, **kwargs) -> None:
        ...
    
    def clean(self, value):
        """
        Validate the given value against all of self.fields, which is a
        list of Field instances.
        """
        ...
    


class MultiValueField(Field):
    """
    Aggregate the logic of multiple Fields.

    Its clean() method takes a "decompressed" list of values, which are then
    cleaned into a single value according to self.fields. Each value in
    this list is cleaned by the corresponding field -- the first value is
    cleaned by the first field, the second value is cleaned by the second
    field, etc. Once all fields are cleaned, the list of clean values is
    "compressed" into a single value.

    Subclasses should not have to implement clean(). Instead, they must
    implement compress(), which takes a list of valid values and returns a
    "compressed" version of those values -- a single value.

    You'll probably want to use this with MultiWidget.
    """
    default_error_messages = ...
    def __init__(self, fields, *, require_all_fields=..., **kwargs) -> None:
        ...
    
    def __deepcopy__(self, memo):
        ...
    
    def validate(self, value):
        ...
    
    def clean(self, value):
        """
        Validate every value in the given list. A value is validated against
        the corresponding Field in self.fields.

        For example, if this MultiValueField was instantiated with
        fields=(DateField(), TimeField()), clean() would call
        DateField.clean(value[0]) and TimeField.clean(value[1]).
        """
        ...
    
    def compress(self, data_list):
        """
        Return a single value for the given list of values. The values can be
        assumed to be valid.

        For example, if this MultiValueField was instantiated with
        fields=(DateField(), TimeField()), this might return a datetime
        object created by combining the date and time in data_list.
        """
        ...
    
    def has_changed(self, initial, data):
        ...
    


class FilePathField(ChoiceField):
    def __init__(self, path, *, match=..., recursive=..., allow_files=..., allow_folders=..., **kwargs) -> None:
        ...
    


class SplitDateTimeField(MultiValueField):
    widget = SplitDateTimeWidget
    hidden_widget = SplitHiddenDateTimeWidget
    default_error_messages = ...
    def __init__(self, *, input_date_formats=..., input_time_formats=..., **kwargs) -> None:
        ...
    
    def compress(self, data_list):
        ...
    


class GenericIPAddressField(CharField):
    def __init__(self, *, protocol=..., unpack_ipv4=..., **kwargs) -> None:
        ...
    
    def to_python(self, value):
        ...
    


class SlugField(CharField):
    default_validators = ...
    def __init__(self, *, allow_unicode=..., **kwargs) -> None:
        ...
    


class UUIDField(CharField):
    default_error_messages = ...
    def prepare_value(self, value):
        ...
    
    def to_python(self, value):
        ...
    


class InvalidJSONInput(str):
    ...


class JSONString(str):
    ...


class JSONField(CharField):
    default_error_messages = ...
    widget = Textarea
    def __init__(self, encoder=..., decoder=..., **kwargs) -> None:
        ...
    
    def to_python(self, value):
        ...
    
    def bound_data(self, data, initial):
        ...
    
    def prepare_value(self, value):
        ...
    
    def has_changed(self, initial, data):
        ...
    


