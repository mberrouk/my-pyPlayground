from _typeshed import Incomplete
from django.conf import settings as settings
from django.contrib import admin as admin, messages as messages
from django.contrib.admin.options import IS_POPUP_VAR as IS_POPUP_VAR
from django.contrib.admin.utils import unquote as unquote
from django.contrib.auth import update_session_auth_hash as update_session_auth_hash
from django.contrib.auth.forms import AdminPasswordChangeForm as AdminPasswordChangeForm, AdminUserCreationForm as AdminUserCreationForm, UserChangeForm as UserChangeForm
from django.contrib.auth.models import Group as Group, User as User
from django.core.exceptions import PermissionDenied as PermissionDenied
from django.db import router as router, transaction as transaction
from django.http import Http404 as Http404, HttpResponseRedirect as HttpResponseRedirect
from django.template.response import TemplateResponse as TemplateResponse
from django.urls import path as path, reverse as reverse
from django.utils.decorators import method_decorator as method_decorator
from django.utils.html import escape as escape
from django.utils.translation import gettext as gettext
from django.views.decorators.csrf import csrf_protect as csrf_protect
from django.views.decorators.debug import sensitive_post_parameters as sensitive_post_parameters

csrf_protect_m: Incomplete
sensitive_post_parameters_m: Incomplete

class GroupAdmin(admin.ModelAdmin):
    search_fields: Incomplete
    ordering: Incomplete
    filter_horizontal: Incomplete
    def formfield_for_manytomany(self, db_field, request: Incomplete | None = None, **kwargs): ...

class UserAdmin(admin.ModelAdmin):
    add_form_template: str
    change_user_password_template: Incomplete
    fieldsets: Incomplete
    add_fieldsets: Incomplete
    form = UserChangeForm
    add_form = AdminUserCreationForm
    change_password_form = AdminPasswordChangeForm
    list_display: Incomplete
    list_filter: Incomplete
    search_fields: Incomplete
    ordering: Incomplete
    filter_horizontal: Incomplete
    def get_fieldsets(self, request, obj: Incomplete | None = None): ...
    def get_form(self, request, obj: Incomplete | None = None, **kwargs): ...
    def get_urls(self): ...
    def lookup_allowed(self, lookup, value, request: Incomplete | None = None): ...
    def add_view(self, request, form_url: str = '', extra_context: Incomplete | None = None): ...
    def user_change_password(self, request, id, form_url: str = ''): ...
    def response_add(self, request, obj, post_url_continue: Incomplete | None = None): ...
