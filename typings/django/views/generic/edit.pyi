from _typeshed import Incomplete
from django.core.exceptions import ImproperlyConfigured as ImproperlyConfigured
from django.forms import Form as Form
from django.http import HttpResponseRedirect as HttpResponseRedirect
from django.views.generic.base import ContextMixin as ContextMixin, TemplateResponseMixin as TemplateResponseMixin, View as View
from django.views.generic.detail import BaseDetailView as BaseDetailView, SingleObjectMixin as SingleObjectMixin, SingleObjectTemplateResponseMixin as SingleObjectTemplateResponseMixin

class FormMixin(ContextMixin):
    initial: Incomplete
    form_class: Incomplete
    success_url: Incomplete
    prefix: Incomplete
    def get_initial(self): ...
    def get_prefix(self): ...
    def get_form_class(self): ...
    def get_form(self, form_class: Incomplete | None = None): ...
    def get_form_kwargs(self): ...
    def get_success_url(self): ...
    def form_valid(self, form): ...
    def form_invalid(self, form): ...
    def get_context_data(self, **kwargs): ...

class ModelFormMixin(FormMixin, SingleObjectMixin):
    fields: Incomplete
    def get_form_class(self): ...
    def get_form_kwargs(self): ...
    def get_success_url(self): ...
    object: Incomplete
    def form_valid(self, form): ...

class ProcessFormView(View):
    def get(self, request, *args, **kwargs): ...
    def post(self, request, *args, **kwargs): ...
    def put(self, *args, **kwargs): ...

class BaseFormView(FormMixin, ProcessFormView): ...
class FormView(TemplateResponseMixin, BaseFormView): ...

class BaseCreateView(ModelFormMixin, ProcessFormView):
    object: Incomplete
    def get(self, request, *args, **kwargs): ...
    def post(self, request, *args, **kwargs): ...

class CreateView(SingleObjectTemplateResponseMixin, BaseCreateView):
    template_name_suffix: str

class BaseUpdateView(ModelFormMixin, ProcessFormView):
    object: Incomplete
    def get(self, request, *args, **kwargs): ...
    def post(self, request, *args, **kwargs): ...

class UpdateView(SingleObjectTemplateResponseMixin, BaseUpdateView):
    template_name_suffix: str

class DeletionMixin:
    success_url: Incomplete
    object: Incomplete
    def delete(self, request, *args, **kwargs): ...
    def post(self, request, *args, **kwargs): ...
    def get_success_url(self): ...

class BaseDeleteView(DeletionMixin, FormMixin, BaseDetailView):
    form_class = Form
    object: Incomplete
    def post(self, request, *args, **kwargs): ...
    def form_valid(self, form): ...

class DeleteView(SingleObjectTemplateResponseMixin, BaseDeleteView):
    template_name_suffix: str
