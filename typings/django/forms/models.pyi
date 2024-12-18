from _typeshed import Incomplete
from django.db.models.utils import AltersData
from django.forms.fields import ChoiceField, Field
from django.forms.forms import BaseForm, DeclarativeFieldsMetaclass
from django.forms.formsets import BaseFormSet
from django.forms.widgets import HiddenInput, MultipleHiddenInput, SelectMultiple
from django.utils.choices import BaseChoiceIterator

__all__ = ['ModelForm', 'BaseModelForm', 'model_to_dict', 'fields_for_model', 'ModelChoiceField', 'ModelMultipleChoiceField', 'ALL_FIELDS', 'BaseModelFormSet', 'modelformset_factory', 'BaseInlineFormSet', 'inlineformset_factory', 'modelform_factory']

ALL_FIELDS: str

def model_to_dict(instance, fields: Incomplete | None = None, exclude: Incomplete | None = None): ...
def fields_for_model(model, fields: Incomplete | None = None, exclude: Incomplete | None = None, widgets: Incomplete | None = None, formfield_callback: Incomplete | None = None, localized_fields: Incomplete | None = None, labels: Incomplete | None = None, help_texts: Incomplete | None = None, error_messages: Incomplete | None = None, field_classes: Incomplete | None = None, *, apply_limit_choices_to: bool = True, form_declared_fields: Incomplete | None = None): ...

class ModelFormOptions:
    model: Incomplete
    fields: Incomplete
    exclude: Incomplete
    widgets: Incomplete
    localized_fields: Incomplete
    labels: Incomplete
    help_texts: Incomplete
    error_messages: Incomplete
    field_classes: Incomplete
    formfield_callback: Incomplete
    def __init__(self, options: Incomplete | None = None) -> None: ...

class ModelFormMetaclass(DeclarativeFieldsMetaclass):
    def __new__(mcs, name, bases, attrs): ...

class BaseModelForm(BaseForm, AltersData):
    instance: Incomplete
    def __init__(self, data: Incomplete | None = None, files: Incomplete | None = None, auto_id: str = 'id_%s', prefix: Incomplete | None = None, initial: Incomplete | None = None, error_class=..., label_suffix: Incomplete | None = None, empty_permitted: bool = False, instance: Incomplete | None = None, use_required_attribute: Incomplete | None = None, renderer: Incomplete | None = None) -> None: ...
    def clean(self): ...
    def validate_unique(self) -> None: ...
    save_m2m: Incomplete
    def save(self, commit: bool = True): ...

class ModelForm(BaseModelForm, metaclass=ModelFormMetaclass): ...

def modelform_factory(model, form=..., fields: Incomplete | None = None, exclude: Incomplete | None = None, formfield_callback: Incomplete | None = None, widgets: Incomplete | None = None, localized_fields: Incomplete | None = None, labels: Incomplete | None = None, help_texts: Incomplete | None = None, error_messages: Incomplete | None = None, field_classes: Incomplete | None = None): ...

class BaseModelFormSet(BaseFormSet, AltersData):
    model: Incomplete
    edit_only: bool
    unique_fields: Incomplete
    queryset: Incomplete
    initial_extra: Incomplete
    def __init__(self, data: Incomplete | None = None, files: Incomplete | None = None, auto_id: str = 'id_%s', prefix: Incomplete | None = None, queryset: Incomplete | None = None, *, initial: Incomplete | None = None, **kwargs) -> None: ...
    def initial_form_count(self): ...
    def get_queryset(self): ...
    def save_new(self, form, commit: bool = True): ...
    def save_existing(self, form, obj, commit: bool = True): ...
    def delete_existing(self, obj, commit: bool = True) -> None: ...
    saved_forms: Incomplete
    save_m2m: Incomplete
    def save(self, commit: bool = True): ...
    def clean(self) -> None: ...
    def validate_unique(self) -> None: ...
    def get_unique_error_message(self, unique_check): ...
    def get_date_error_message(self, date_check): ...
    def get_form_error(self): ...
    changed_objects: Incomplete
    deleted_objects: Incomplete
    def save_existing_objects(self, commit: bool = True): ...
    new_objects: Incomplete
    def save_new_objects(self, commit: bool = True): ...
    def add_fields(self, form, index): ...

def modelformset_factory(model, form=..., formfield_callback: Incomplete | None = None, formset=..., extra: int = 1, can_delete: bool = False, can_order: bool = False, max_num: Incomplete | None = None, fields: Incomplete | None = None, exclude: Incomplete | None = None, widgets: Incomplete | None = None, validate_max: bool = False, localized_fields: Incomplete | None = None, labels: Incomplete | None = None, help_texts: Incomplete | None = None, error_messages: Incomplete | None = None, min_num: Incomplete | None = None, validate_min: bool = False, field_classes: Incomplete | None = None, absolute_max: Incomplete | None = None, can_delete_extra: bool = True, renderer: Incomplete | None = None, edit_only: bool = False): ...

class BaseInlineFormSet(BaseModelFormSet):
    instance: Incomplete
    save_as_new: Incomplete
    unique_fields: Incomplete
    def __init__(self, data: Incomplete | None = None, files: Incomplete | None = None, instance: Incomplete | None = None, save_as_new: bool = False, prefix: Incomplete | None = None, queryset: Incomplete | None = None, **kwargs) -> None: ...
    def initial_form_count(self): ...
    @classmethod
    def get_default_prefix(cls): ...
    def save_new(self, form, commit: bool = True): ...
    def add_fields(self, form, index) -> None: ...
    def get_unique_error_message(self, unique_check): ...

def inlineformset_factory(parent_model, model, form=..., formset=..., fk_name: Incomplete | None = None, fields: Incomplete | None = None, exclude: Incomplete | None = None, extra: int = 3, can_order: bool = False, can_delete: bool = True, max_num: Incomplete | None = None, formfield_callback: Incomplete | None = None, widgets: Incomplete | None = None, validate_max: bool = False, localized_fields: Incomplete | None = None, labels: Incomplete | None = None, help_texts: Incomplete | None = None, error_messages: Incomplete | None = None, min_num: Incomplete | None = None, validate_min: bool = False, field_classes: Incomplete | None = None, absolute_max: Incomplete | None = None, can_delete_extra: bool = True, renderer: Incomplete | None = None, edit_only: bool = False): ...

class InlineForeignKeyField(Field):
    widget = HiddenInput
    default_error_messages: Incomplete
    parent_instance: Incomplete
    pk_field: Incomplete
    to_field: Incomplete
    def __init__(self, parent_instance, *args, pk_field: bool = False, to_field: Incomplete | None = None, **kwargs) -> None: ...
    def clean(self, value): ...
    def has_changed(self, initial, data): ...

class ModelChoiceIteratorValue:
    value: Incomplete
    instance: Incomplete
    def __init__(self, value, instance) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other): ...

class ModelChoiceIterator(BaseChoiceIterator):
    field: Incomplete
    queryset: Incomplete
    def __init__(self, field) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def choice(self, obj): ...

class ModelChoiceField(ChoiceField):
    default_error_messages: Incomplete
    iterator = ModelChoiceIterator
    empty_label: Incomplete
    queryset: Incomplete
    limit_choices_to: Incomplete
    to_field_name: Incomplete
    def __init__(self, queryset, *, empty_label: str = '---------', required: bool = True, widget: Incomplete | None = None, label: Incomplete | None = None, initial: Incomplete | None = None, help_text: str = '', to_field_name: Incomplete | None = None, limit_choices_to: Incomplete | None = None, blank: bool = False, **kwargs) -> None: ...
    def validate_no_null_characters(self, value): ...
    def get_limit_choices_to(self): ...
    def __deepcopy__(self, memo): ...
    def label_from_instance(self, obj): ...
    choices: Incomplete
    def prepare_value(self, value): ...
    def to_python(self, value): ...
    def validate(self, value): ...
    def has_changed(self, initial, data): ...

class ModelMultipleChoiceField(ModelChoiceField):
    widget = SelectMultiple
    hidden_widget = MultipleHiddenInput
    default_error_messages: Incomplete
    def __init__(self, queryset, **kwargs) -> None: ...
    def to_python(self, value): ...
    def clean(self, value): ...
    def prepare_value(self, value): ...
    def has_changed(self, initial, data): ...