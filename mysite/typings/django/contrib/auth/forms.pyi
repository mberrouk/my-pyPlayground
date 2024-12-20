"""
This type stub file was generated by pyright.
"""

from django import forms
from django.contrib.auth.models import User

UserModel = ...
logger = ...
class ReadOnlyPasswordHashWidget(forms.Widget):
    template_name = ...
    read_only = ...
    def get_context(self, name, value, attrs): # -> dict[str, dict[str, Any]]:
        ...
    
    def id_for_label(self, id_): # -> None:
        ...
    


class ReadOnlyPasswordHashField(forms.Field):
    widget = ReadOnlyPasswordHashWidget
    def __init__(self, *args, **kwargs) -> None:
        ...
    


class UsernameField(forms.CharField):
    def to_python(self, value): # -> str:
        ...
    
    def widget_attrs(self, widget): # -> dict[Any | str, Any]:
        ...
    


class SetPasswordMixin:
    """
    Form mixin that validates and sets a password for a user.
    """
    error_messages = ...
    @staticmethod
    def create_password_fields(label1=..., label2=...): # -> tuple[CharField, CharField]:
        ...
    
    def validate_passwords(self, password1_field_name=..., password2_field_name=...): # -> None:
        ...
    
    def validate_password_for_user(self, user, password_field_name=...): # -> None:
        ...
    
    def set_password_and_save(self, user, password_field_name=..., commit=...):
        ...
    


class SetUnusablePasswordMixin:
    """
    Form mixin that allows setting an unusable password for a user.

    This mixin should be used in combination with `SetPasswordMixin`.
    """
    usable_password_help_text = ...
    @staticmethod
    def create_usable_password_field(help_text=...): # -> ChoiceField:
        ...
    
    def validate_passwords(self, *args, usable_password_field_name=..., **kwargs): # -> None:
        ...
    
    def validate_password_for_user(self, user, **kwargs): # -> None:
        ...
    
    def set_password_and_save(self, user, commit=..., **kwargs):
        ...
    


class BaseUserCreationForm(SetPasswordMixin, forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.

    This is the documented base class for customizing the user creation form.
    It should be kept mostly unchanged to ensure consistency and compatibility.
    """
    class Meta:
        model = User
        fields = ...
        field_classes = ...
    
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def clean(self): # -> dict[Any, Any]:
        ...
    
    def save(self, commit=...):
        ...
    


class UserCreationForm(BaseUserCreationForm):
    def clean_username(self): # -> None:
        """Reject usernames that differ only in case."""
        ...
    


class UserChangeForm(forms.ModelForm):
    password = ...
    class Meta:
        model = User
        fields = ...
        field_classes = ...
    
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    


class AuthenticationForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """
    username = ...
    password = ...
    error_messages = ...
    def __init__(self, request=..., *args, **kwargs) -> None:
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        ...
    
    def clean(self): # -> dict[Any, Any]:
        ...
    
    def confirm_login_allowed(self, user): # -> None:
        """
        Controls whether the given User may log in. This is a policy setting,
        independent of end-user authentication. This default behavior is to
        allow login by active users, and reject login by inactive users.

        If the given user cannot log in, this method should raise a
        ``ValidationError``.

        If the given user may log in, this method should return None.
        """
        ...
    
    def get_user(self): # -> None:
        ...
    
    def get_invalid_login_error(self): # -> ValidationError:
        ...
    


class PasswordResetForm(forms.Form):
    email = ...
    def send_mail(self, subject_template_name, email_template_name, context, from_email, to_email, html_email_template_name=...): # -> None:
        """
        Send a django.core.mail.EmailMultiAlternatives to `to_email`.
        """
        ...
    
    def get_users(self, email): # -> Generator[Any, None, None]:
        """Given an email, return matching user(s) who should receive a reset.

        This allows subclasses to more easily customize the default policies
        that prevent inactive users and users with unusable passwords from
        resetting their password.
        """
        ...
    
    def save(self, domain_override=..., subject_template_name=..., email_template_name=..., use_https=..., token_generator=..., from_email=..., request=..., html_email_template_name=..., extra_email_context=...): # -> None:
        """
        Generate a one-use only link for resetting password and send it to the
        user.
        """
        ...
    


class SetPasswordForm(SetPasswordMixin, forms.Form):
    """
    A form that lets a user set their password without entering the old
    password
    """
    def __init__(self, user, *args, **kwargs) -> None:
        ...
    
    def clean(self): # -> dict[Any, Any]:
        ...
    
    def save(self, commit=...): # -> Any:
        ...
    


class PasswordChangeForm(SetPasswordForm):
    """
    A form that lets a user change their password by entering their old
    password.
    """
    error_messages = ...
    old_password = ...
    field_order = ...
    def clean_old_password(self):
        """
        Validate that the old_password field is correct.
        """
        ...
    


class AdminPasswordChangeForm(SetUnusablePasswordMixin, SetPasswordMixin, forms.Form):
    """
    A form used to change the password of a user in the admin interface.
    """
    required_css_class = ...
    usable_password_help_text = ...
    def __init__(self, user, *args, **kwargs) -> None:
        ...
    
    def clean(self): # -> dict[Any, Any]:
        ...
    
    def save(self, commit=...):
        """Save the new password."""
        ...
    
    @property
    def changed_data(self): # -> list[str] | list[Any]:
        ...
    


class AdminUserCreationForm(SetUnusablePasswordMixin, UserCreationForm):
    usable_password = ...


