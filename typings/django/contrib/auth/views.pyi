from _typeshed import Incomplete
from django.conf import settings as settings
from django.contrib.auth import REDIRECT_FIELD_NAME as REDIRECT_FIELD_NAME, get_user_model as get_user_model, update_session_auth_hash as update_session_auth_hash
from django.contrib.auth.decorators import login_not_required as login_not_required, login_required as login_required
from django.contrib.auth.forms import AuthenticationForm as AuthenticationForm, PasswordChangeForm as PasswordChangeForm, PasswordResetForm as PasswordResetForm, SetPasswordForm as SetPasswordForm
from django.contrib.auth.tokens import default_token_generator as default_token_generator
from django.contrib.sites.shortcuts import get_current_site as get_current_site
from django.core.exceptions import ImproperlyConfigured as ImproperlyConfigured, ValidationError as ValidationError
from django.http import HttpResponseRedirect as HttpResponseRedirect, QueryDict as QueryDict
from django.shortcuts import resolve_url as resolve_url
from django.urls import reverse_lazy as reverse_lazy
from django.utils.decorators import method_decorator as method_decorator
from django.utils.http import url_has_allowed_host_and_scheme as url_has_allowed_host_and_scheme, urlsafe_base64_decode as urlsafe_base64_decode
from django.views.decorators.cache import never_cache as never_cache
from django.views.decorators.csrf import csrf_protect as csrf_protect
from django.views.decorators.debug import sensitive_post_parameters as sensitive_post_parameters
from django.views.generic.base import TemplateView as TemplateView
from django.views.generic.edit import FormView as FormView

UserModel: Incomplete

class RedirectURLMixin:
    next_page: Incomplete
    redirect_field_name = REDIRECT_FIELD_NAME
    success_url_allowed_hosts: Incomplete
    def get_success_url(self): ...
    def get_redirect_url(self): ...
    def get_success_url_allowed_hosts(self): ...
    def get_default_redirect_url(self): ...

class LoginView(RedirectURLMixin, FormView):
    form_class = AuthenticationForm
    authentication_form: Incomplete
    template_name: str
    redirect_authenticated_user: bool
    extra_context: Incomplete
    def dispatch(self, request, *args, **kwargs): ...
    def get_default_redirect_url(self): ...
    def get_form_class(self): ...
    def get_form_kwargs(self): ...
    def form_valid(self, form): ...
    def get_context_data(self, **kwargs): ...

class LogoutView(RedirectURLMixin, TemplateView):
    http_method_names: Incomplete
    template_name: str
    extra_context: Incomplete
    def dispatch(self, request, *args, **kwargs): ...
    def post(self, request, *args, **kwargs): ...
    def get_default_redirect_url(self): ...
    def get_context_data(self, **kwargs): ...

def logout_then_login(request, login_url: Incomplete | None = None): ...
def redirect_to_login(next, login_url: Incomplete | None = None, redirect_field_name=...): ...

class PasswordContextMixin:
    extra_context: Incomplete
    def get_context_data(self, **kwargs): ...

class PasswordResetView(PasswordContextMixin, FormView):
    email_template_name: str
    extra_email_context: Incomplete
    form_class = PasswordResetForm
    from_email: Incomplete
    html_email_template_name: Incomplete
    subject_template_name: str
    success_url: Incomplete
    template_name: str
    title: Incomplete
    token_generator = default_token_generator
    def dispatch(self, *args, **kwargs): ...
    def form_valid(self, form): ...

INTERNAL_RESET_SESSION_TOKEN: str

class PasswordResetDoneView(PasswordContextMixin, TemplateView):
    template_name: str
    title: Incomplete

class PasswordResetConfirmView(PasswordContextMixin, FormView):
    form_class = SetPasswordForm
    post_reset_login: bool
    post_reset_login_backend: Incomplete
    reset_url_token: str
    success_url: Incomplete
    template_name: str
    title: Incomplete
    token_generator = default_token_generator
    validlink: bool
    user: Incomplete
    def dispatch(self, *args, **kwargs): ...
    def get_user(self, uidb64): ...
    def get_form_kwargs(self): ...
    def form_valid(self, form): ...
    def get_context_data(self, **kwargs): ...

class PasswordResetCompleteView(PasswordContextMixin, TemplateView):
    template_name: str
    title: Incomplete
    def get_context_data(self, **kwargs): ...

class PasswordChangeView(PasswordContextMixin, FormView):
    form_class = PasswordChangeForm
    success_url: Incomplete
    template_name: str
    title: Incomplete
    def dispatch(self, *args, **kwargs): ...
    def get_form_kwargs(self): ...
    def form_valid(self, form): ...

class PasswordChangeDoneView(PasswordContextMixin, TemplateView):
    template_name: str
    title: Incomplete
    def dispatch(self, *args, **kwargs): ...
