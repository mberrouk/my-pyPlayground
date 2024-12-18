from _typeshed import Incomplete
from django.contrib.admin.checks import InlineModelAdminChecks as InlineModelAdminChecks
from django.contrib.admin.options import InlineModelAdmin as InlineModelAdmin, flatten_fieldsets as flatten_fieldsets
from django.contrib.contenttypes.fields import GenericForeignKey as GenericForeignKey
from django.contrib.contenttypes.forms import BaseGenericInlineFormSet as BaseGenericInlineFormSet, generic_inlineformset_factory as generic_inlineformset_factory
from django.core import checks as checks
from django.core.exceptions import FieldDoesNotExist as FieldDoesNotExist
from django.forms import ALL_FIELDS as ALL_FIELDS
from django.forms.models import modelform_defines_fields as modelform_defines_fields

class GenericInlineModelAdminChecks(InlineModelAdminChecks): ...

class GenericInlineModelAdmin(InlineModelAdmin):
    ct_field: str
    ct_fk_field: str
    formset = BaseGenericInlineFormSet
    checks_class = GenericInlineModelAdminChecks
    def get_formset(self, request, obj: Incomplete | None = None, **kwargs): ...

class GenericStackedInline(GenericInlineModelAdmin):
    template: str

class GenericTabularInline(GenericInlineModelAdmin):
    template: str
