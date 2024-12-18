from _typeshed import Incomplete
from django import forms as forms
from django.contrib.auth import authenticate as authenticate, get_user_model as get_user_model, password_validation as password_validation
from django.contrib.auth.hashers import UNUSABLE_PASSWORD_PREFIX as UNUSABLE_PASSWORD_PREFIX, identify_hasher as identify_hasher
from django.contrib.auth.models import User as User
from django.contrib.auth.tokens import default_token_generator as default_token_generator
from django.contrib.sites.shortcuts import get_current_site as get_current_site
from django.core.exceptions import ValidationError as ValidationError
from django.core.mail import EmailMultiAlternatives as EmailMultiAlternatives
from django.template import loader as loader
from django.utils.encoding import force_bytes as force_bytes
from django.utils.http import urlsafe_base64_encode as urlsafe_base64_encode
from django.utils.text import capfirst as capfirst
from django.utils.translation import gettext as gettext

UserModel: Incomplete
logger: Incomplete

class ReadOnlyPasswordHashWidget(forms.Widget):
    template_name: str
    read_only: bool
    def get_context(self, name, value, attrs): ...
    def id_for_label(self, id_) -> None: ...

class ReadOnlyPasswordHashField(forms.Field):
    widget = ReadOnlyPasswordHashWidget
    def __init__(self, *args, **kwargs) -> None: ...

class UsernameField(forms.CharField):
    def to_python(self, value): ...
    def widget_attrs(self, widget): ...

class SetPasswordMixin:
    error_messages: Incomplete
    @staticmethod
    def create_password_fields(label1=..., label2=...): ...
    def validate_passwords(self, password1_field_name: str = 'password1', password2_field_name: str = 'password2') -> None: ...
    def validate_password_for_user(self, user, password_field_name: str = 'password2') -> None: ...
    def set_password_and_save(self, user, password_field_name: str = 'password1', commit: bool = True): ...

class SetUnusablePasswordMixin:
    usable_password_help_text: Incomplete
    @staticmethod
    def create_usable_password_field(help_text=...): ...
    def validate_passwords(self, *args, usable_password_field_name: str = 'usable_password', **kwargs) -> None: ...
    def validate_password_for_user(self, user, **kwargs) -> None: ...
    def set_password_and_save(self, user, commit: bool = True, **kwargs): ...

class BaseUserCreationForm(SetPasswordMixin, forms.ModelForm):
    password1: Incomplete
    password2: Incomplete
    class Meta:
        model = User
        fields: Incomplete
        field_classes: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def clean(self): ...
    def save(self, commit: bool = True): ...

class UserCreationForm(BaseUserCreationForm):
    def clean_username(self): ...

class UserChangeForm(forms.ModelForm):
    password: Incomplete
    class Meta:
        model = User
        fields: str
        field_classes: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class AuthenticationForm(forms.Form):
    username: Incomplete
    password: Incomplete
    error_messages: Incomplete
    request: Incomplete
    user_cache: Incomplete
    username_field: Incomplete
    def __init__(self, request: Incomplete | None = None, *args, **kwargs) -> None: ...
    def clean(self): ...
    def confirm_login_allowed(self, user) -> None: ...
    def get_user(self): ...
    def get_invalid_login_error(self): ...

class PasswordResetForm(forms.Form):
    email: Incomplete
    def send_mail(self, subject_template_name, email_template_name, context, from_email, to_email, html_email_template_name: Incomplete | None = None) -> None: ...
    def get_users(self, email): ...
    def save(self, domain_override: Incomplete | None = None, subject_template_name: str = 'registration/password_reset_subject.txt', email_template_name: str = 'registration/password_reset_email.html', use_https: bool = False, token_generator=..., from_email: Incomplete | None = None, request: Incomplete | None = None, html_email_template_name: Incomplete | None = None, extra_email_context: Incomplete | None = None) -> None: ...

class SetPasswordForm(SetPasswordMixin, forms.Form):
    new_password1: Incomplete
    new_password2: Incomplete
    user: Incomplete
    def __init__(self, user, *args, **kwargs) -> None: ...
    def clean(self): ...
    def save(self, commit: bool = True): ...

class PasswordChangeForm(SetPasswordForm):
    error_messages: Incomplete
    old_password: Incomplete
    field_order: Incomplete
    def clean_old_password(self): ...

class AdminPasswordChangeForm(SetUnusablePasswordMixin, SetPasswordMixin, forms.Form):
    required_css_class: str
    usable_password_help_text: Incomplete
    password1: Incomplete
    password2: Incomplete
    user: Incomplete
    def __init__(self, user, *args, **kwargs) -> None: ...
    def clean(self): ...
    def save(self, commit: bool = True): ...
    @property
    def changed_data(self): ...

class AdminUserCreationForm(SetUnusablePasswordMixin, UserCreationForm):
    usable_password: Incomplete
