from django.apps import apps as apps
from django.conf import settings as settings
from django.contrib.admin.exceptions import NotRegistered as NotRegistered
from django.contrib.admin.utils import NotRelationField as NotRelationField, flatten as flatten, get_fields_from_path as get_fields_from_path
from django.core import checks as checks
from django.core.exceptions import FieldDoesNotExist as FieldDoesNotExist
from django.db import models as models
from django.db.models.constants import LOOKUP_SEP as LOOKUP_SEP
from django.db.models.expressions import Combinable as Combinable
from django.forms.models import BaseModelForm as BaseModelForm, BaseModelFormSet as BaseModelFormSet
from django.template import engines as engines
from django.template.backends.django import DjangoTemplates as DjangoTemplates
from django.utils.module_loading import import_string as import_string

def check_admin_app(app_configs, **kwargs): ...
def check_dependencies(**kwargs): ...

class BaseModelAdminChecks:
    def check(self, admin_obj, **kwargs): ...

class ModelAdminChecks(BaseModelAdminChecks):
    def check(self, admin_obj, **kwargs): ...

class InlineModelAdminChecks(BaseModelAdminChecks):
    def check(self, inline_obj, **kwargs): ...

def must_be(type, option, obj, id): ...
def must_inherit_from(parent, option, obj, id): ...
def refer_to_missing_field(field, option, obj, id): ...
