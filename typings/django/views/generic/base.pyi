from _typeshed import Incomplete
from django.core.exceptions import ImproperlyConfigured as ImproperlyConfigured
from django.http import HttpResponse as HttpResponse, HttpResponseGone as HttpResponseGone, HttpResponseNotAllowed as HttpResponseNotAllowed, HttpResponsePermanentRedirect as HttpResponsePermanentRedirect, HttpResponseRedirect as HttpResponseRedirect
from django.template.response import TemplateResponse as TemplateResponse
from django.urls import reverse as reverse
from django.utils.decorators import classonlymethod as classonlymethod
from django.utils.functional import classproperty as classproperty

logger: Incomplete

class ContextMixin:
    extra_context: Incomplete
    def get_context_data(self, **kwargs): ...

class View:
    http_method_names: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def view_is_async(cls): ...
    def as_view(cls, **initkwargs): ...
    head: Incomplete
    request: Incomplete
    args: Incomplete
    kwargs: Incomplete
    def setup(self, request, *args, **kwargs) -> None: ...
    def dispatch(self, request, *args, **kwargs): ...
    def http_method_not_allowed(self, request, *args, **kwargs): ...
    def options(self, request, *args, **kwargs): ...

class TemplateResponseMixin:
    template_name: Incomplete
    template_engine: Incomplete
    response_class = TemplateResponse
    content_type: Incomplete
    def render_to_response(self, context, **response_kwargs): ...
    def get_template_names(self): ...

class TemplateView(TemplateResponseMixin, ContextMixin, View):
    def get(self, request, *args, **kwargs): ...

class RedirectView(View):
    permanent: bool
    url: Incomplete
    pattern_name: Incomplete
    query_string: bool
    def get_redirect_url(self, *args, **kwargs): ...
    def get(self, request, *args, **kwargs): ...
    def head(self, request, *args, **kwargs): ...
    def post(self, request, *args, **kwargs): ...
    def options(self, request, *args, **kwargs): ...
    def delete(self, request, *args, **kwargs): ...
    def put(self, request, *args, **kwargs): ...
    def patch(self, request, *args, **kwargs): ...
