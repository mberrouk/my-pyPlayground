from django.contrib import messages as messages
from django.contrib.admin import helpers as helpers
from django.contrib.admin.decorators import action as action
from django.contrib.admin.utils import model_ngettext as model_ngettext
from django.core.exceptions import PermissionDenied as PermissionDenied
from django.template.response import TemplateResponse as TemplateResponse
from django.utils.translation import gettext_lazy as gettext_lazy

def delete_selected(modeladmin, request, queryset): ...
