from _typeshed import Incomplete
from django.contrib.auth.forms import AuthenticationForm as AuthenticationForm, PasswordChangeForm as PasswordChangeForm
from django.core.exceptions import ValidationError as ValidationError

class AdminAuthenticationForm(AuthenticationForm):
    error_messages: Incomplete
    required_css_class: str
    def confirm_login_allowed(self, user) -> None: ...

class AdminPasswordChangeForm(PasswordChangeForm):
    required_css_class: str
