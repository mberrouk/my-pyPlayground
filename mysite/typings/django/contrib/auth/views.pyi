"""
This type stub file was generated by pyright.
"""

from django.contrib.auth.decorators import login_not_required, login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

UserModel = ...
class RedirectURLMixin:
    next_page = ...
    redirect_field_name = ...
    success_url_allowed_hosts = ...
    def get_success_url(self): # -> str:
        ...
    
    def get_redirect_url(self): # -> Literal['']:
        """Return the user-originating redirect URL if it's safe."""
        ...
    
    def get_success_url_allowed_hosts(self): # -> set[Any]:
        ...
    
    def get_default_redirect_url(self): # -> str:
        """Return the default redirect URL."""
        ...
    


@method_decorator(login_not_required, name="dispatch")
class LoginView(RedirectURLMixin, FormView):
    """
    Display the login form and handle the login action.
    """
    form_class = AuthenticationForm
    authentication_form = ...
    template_name = ...
    redirect_authenticated_user = ...
    extra_context = ...
    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs): # -> HttpResponseRedirect | Coroutine[Any, Any, HttpResponseNotAllowed] | HttpResponseNotAllowed | Any:
        ...
    
    def get_default_redirect_url(self): # -> str:
        """Return the default redirect URL."""
        ...
    
    def get_form_class(self): # -> form_class:
        ...
    
    def get_form_kwargs(self): # -> dict[str, Any]:
        ...
    
    def form_valid(self, form): # -> HttpResponseRedirect:
        """Security check complete. Log the user in."""
        ...
    
    def get_context_data(self, **kwargs): # -> dict[str, Any]:
        ...
    


class LogoutView(RedirectURLMixin, TemplateView):
    """
    Log out the user and display the 'You are logged out' message.
    """
    http_method_names = ...
    template_name = ...
    extra_context = ...
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs): # -> Coroutine[Any, Any, HttpResponseNotAllowed] | HttpResponseNotAllowed | Any:
        ...
    
    def post(self, request, *args, **kwargs): # -> HttpResponseRedirect | response_class:
        """Logout may be done via POST."""
        ...
    
    def get_default_redirect_url(self): # -> str:
        """Return the default redirect URL."""
        ...
    
    def get_context_data(self, **kwargs): # -> dict[str, Any]:
        ...
    


def logout_then_login(request, login_url=...):
    """
    Log out the user if they are logged in. Then redirect to the login page.
    """
    ...

def redirect_to_login(next, login_url=..., redirect_field_name=...): # -> HttpResponseRedirect:
    """
    Redirect the user to the login page, passing the given 'next' page.
    """
    ...

class PasswordContextMixin:
    extra_context = ...
    def get_context_data(self, **kwargs):
        ...
    


@method_decorator(login_not_required, name="dispatch")
class PasswordResetView(PasswordContextMixin, FormView):
    email_template_name = ...
    extra_email_context = ...
    form_class = PasswordResetForm
    from_email = ...
    html_email_template_name = ...
    subject_template_name = ...
    success_url = ...
    template_name = ...
    title = ...
    token_generator = ...
    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs): # -> Coroutine[Any, Any, HttpResponseNotAllowed] | HttpResponseNotAllowed | Any:
        ...
    
    def form_valid(self, form): # -> HttpResponseRedirect:
        ...
    


INTERNAL_RESET_SESSION_TOKEN = ...
@method_decorator(login_not_required, name="dispatch")
class PasswordResetDoneView(PasswordContextMixin, TemplateView):
    template_name = ...
    title = ...


@method_decorator(login_not_required, name="dispatch")
class PasswordResetConfirmView(PasswordContextMixin, FormView):
    form_class = SetPasswordForm
    post_reset_login = ...
    post_reset_login_backend = ...
    reset_url_token = ...
    success_url = ...
    template_name = ...
    title = ...
    token_generator = ...
    @method_decorator(sensitive_post_parameters())
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs): # -> Coroutine[Any, Any, HttpResponseNotAllowed] | HttpResponseNotAllowed | Any | HttpResponseRedirect | response_class:
        ...
    
    def get_user(self, uidb64): # -> None:
        ...
    
    def get_form_kwargs(self): # -> dict[str, Any]:
        ...
    
    def form_valid(self, form): # -> HttpResponseRedirect:
        ...
    
    def get_context_data(self, **kwargs):
        ...
    


@method_decorator(login_not_required, name="dispatch")
class PasswordResetCompleteView(PasswordContextMixin, TemplateView):
    template_name = ...
    title = ...
    def get_context_data(self, **kwargs):
        ...
    


class PasswordChangeView(PasswordContextMixin, FormView):
    form_class = PasswordChangeForm
    success_url = ...
    template_name = ...
    title = ...
    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs): # -> Coroutine[Any, Any, HttpResponseNotAllowed] | HttpResponseNotAllowed | Any:
        ...
    
    def get_form_kwargs(self): # -> dict[str, Any]:
        ...
    
    def form_valid(self, form): # -> HttpResponseRedirect:
        ...
    


class PasswordChangeDoneView(PasswordContextMixin, TemplateView):
    template_name = ...
    title = ...
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs): # -> Coroutine[Any, Any, HttpResponseNotAllowed] | HttpResponseNotAllowed | Any:
        ...
    


