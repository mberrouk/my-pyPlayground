from _typeshed import Incomplete
from django.contrib.contenttypes.models import ContentType as ContentType
from django.db import models as models
from django.forms import ModelForm as ModelForm, modelformset_factory as modelformset_factory
from django.forms.models import BaseModelFormSet as BaseModelFormSet

class BaseGenericInlineFormSet(BaseModelFormSet):
    instance: Incomplete
    rel_name: Incomplete
    save_as_new: Incomplete
    def __init__(self, data: Incomplete | None = None, files: Incomplete | None = None, instance: Incomplete | None = None, save_as_new: bool = False, prefix: Incomplete | None = None, queryset: Incomplete | None = None, **kwargs) -> None: ...
    def initial_form_count(self): ...
    @classmethod
    def get_default_prefix(cls): ...
    def save_new(self, form, commit: bool = True): ...

def generic_inlineformset_factory(model, form=..., formset=..., ct_field: str = 'content_type', fk_field: str = 'object_id', fields: Incomplete | None = None, exclude: Incomplete | None = None, extra: int = 3, can_order: bool = False, can_delete: bool = True, max_num: Incomplete | None = None, formfield_callback: Incomplete | None = None, validate_max: bool = False, for_concrete_model: bool = True, min_num: Incomplete | None = None, validate_min: bool = False, absolute_max: Incomplete | None = None, can_delete_extra: bool = True): ...
