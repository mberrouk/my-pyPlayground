from _typeshed import Incomplete
from django.core.exceptions import ImproperlyConfigured as ImproperlyConfigured
from django.db import models as models
from django.http import Http404 as Http404
from django.views.generic.base import ContextMixin as ContextMixin, TemplateResponseMixin as TemplateResponseMixin, View as View

class SingleObjectMixin(ContextMixin):
    model: Incomplete
    queryset: Incomplete
    slug_field: str
    context_object_name: Incomplete
    slug_url_kwarg: str
    pk_url_kwarg: str
    query_pk_and_slug: bool
    def get_object(self, queryset: Incomplete | None = None): ...
    def get_queryset(self): ...
    def get_slug_field(self): ...
    def get_context_object_name(self, obj): ...
    def get_context_data(self, **kwargs): ...

class BaseDetailView(SingleObjectMixin, View):
    object: Incomplete
    def get(self, request, *args, **kwargs): ...

class SingleObjectTemplateResponseMixin(TemplateResponseMixin):
    template_name_field: Incomplete
    template_name_suffix: str
    def get_template_names(self): ...

class DetailView(SingleObjectTemplateResponseMixin, BaseDetailView): ...
