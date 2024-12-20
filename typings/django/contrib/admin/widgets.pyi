from _typeshed import Incomplete
from django import forms as forms
from django.conf import settings as settings
from django.core.exceptions import ValidationError as ValidationError
from django.core.validators import URLValidator as URLValidator
from django.db.models import CASCADE as CASCADE, UUIDField as UUIDField
from django.urls import reverse as reverse
from django.urls.exceptions import NoReverseMatch as NoReverseMatch
from django.utils.html import smart_urlquote as smart_urlquote
from django.utils.http import urlencode as urlencode
from django.utils.text import Truncator as Truncator
from django.utils.translation import get_language as get_language

class FilteredSelectMultiple(forms.SelectMultiple):
    class Media:
        js: Incomplete
    verbose_name: Incomplete
    is_stacked: Incomplete
    def __init__(self, verbose_name, is_stacked, attrs: Incomplete | None = None, choices=()) -> None: ...
    def get_context(self, name, value, attrs): ...

class BaseAdminDateWidget(forms.DateInput):
    class Media:
        js: Incomplete
    def __init__(self, attrs: Incomplete | None = None, format: Incomplete | None = None) -> None: ...

class AdminDateWidget(BaseAdminDateWidget):
    template_name: str

class BaseAdminTimeWidget(forms.TimeInput):
    class Media:
        js: Incomplete
    def __init__(self, attrs: Incomplete | None = None, format: Incomplete | None = None) -> None: ...

class AdminTimeWidget(BaseAdminTimeWidget):
    template_name: str

class AdminSplitDateTime(forms.SplitDateTimeWidget):
    template_name: str
    def __init__(self, attrs: Incomplete | None = None) -> None: ...
    def get_context(self, name, value, attrs): ...

class AdminRadioSelect(forms.RadioSelect):
    template_name: str

class AdminFileWidget(forms.ClearableFileInput):
    template_name: str

def url_params_from_lookup_dict(lookups): ...

class ForeignKeyRawIdWidget(forms.TextInput):
    template_name: str
    rel: Incomplete
    admin_site: Incomplete
    db: Incomplete
    def __init__(self, rel, admin_site, attrs: Incomplete | None = None, using: Incomplete | None = None) -> None: ...
    def get_context(self, name, value, attrs): ...
    def base_url_parameters(self): ...
    def url_parameters(self): ...
    def label_and_url_for_value(self, value): ...

class ManyToManyRawIdWidget(ForeignKeyRawIdWidget):
    template_name: str
    def get_context(self, name, value, attrs): ...
    def url_parameters(self): ...
    def label_and_url_for_value(self, value): ...
    def value_from_datadict(self, data, files, name): ...
    def format_value(self, value): ...

class RelatedFieldWidgetWrapper(forms.Widget):
    template_name: str
    needs_multipart_form: Incomplete
    attrs: Incomplete
    widget: Incomplete
    rel: Incomplete
    can_add_related: Incomplete
    can_change_related: Incomplete
    can_delete_related: Incomplete
    can_view_related: Incomplete
    admin_site: Incomplete
    def __init__(self, widget, rel, admin_site, can_add_related: Incomplete | None = None, can_change_related: bool = False, can_delete_related: bool = False, can_view_related: bool = False) -> None: ...
    def __deepcopy__(self, memo): ...
    @property
    def is_hidden(self): ...
    @property
    def media(self): ...
    @property
    def choices(self): ...
    @choices.setter
    def choices(self, value) -> None: ...
    def get_related_url(self, info, action, *args): ...
    def get_context(self, name, value, attrs): ...
    def value_from_datadict(self, data, files, name): ...
    def value_omitted_from_data(self, data, files, name): ...
    def id_for_label(self, id_): ...

class AdminTextareaWidget(forms.Textarea):
    def __init__(self, attrs: Incomplete | None = None) -> None: ...

class AdminTextInputWidget(forms.TextInput):
    def __init__(self, attrs: Incomplete | None = None) -> None: ...

class AdminEmailInputWidget(forms.EmailInput):
    def __init__(self, attrs: Incomplete | None = None) -> None: ...

class AdminURLFieldWidget(forms.URLInput):
    template_name: str
    validator: Incomplete
    def __init__(self, attrs: Incomplete | None = None, validator_class=...) -> None: ...
    def get_context(self, name, value, attrs): ...

class AdminIntegerFieldWidget(forms.NumberInput):
    class_name: str
    def __init__(self, attrs: Incomplete | None = None) -> None: ...

class AdminBigIntegerFieldWidget(AdminIntegerFieldWidget):
    class_name: str

class AdminUUIDInputWidget(forms.TextInput):
    def __init__(self, attrs: Incomplete | None = None) -> None: ...

SELECT2_TRANSLATIONS: Incomplete

def get_select2_language(): ...

class AutocompleteMixin:
    url_name: str
    field: Incomplete
    admin_site: Incomplete
    db: Incomplete
    choices: Incomplete
    attrs: Incomplete
    i18n_name: Incomplete
    def __init__(self, field, admin_site, attrs: Incomplete | None = None, choices=(), using: Incomplete | None = None) -> None: ...
    def get_url(self): ...
    def build_attrs(self, base_attrs, extra_attrs: Incomplete | None = None): ...
    def optgroups(self, name, value, attr: Incomplete | None = None): ...
    @property
    def media(self): ...

class AutocompleteSelect(AutocompleteMixin, forms.Select): ...
class AutocompleteSelectMultiple(AutocompleteMixin, forms.SelectMultiple): ...
