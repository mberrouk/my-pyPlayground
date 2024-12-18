from django.conf import settings as settings
from django.http import HttpResponseForbidden as HttpResponseForbidden
from django.template import Context as Context, Engine as Engine, TemplateDoesNotExist as TemplateDoesNotExist, loader as loader
from django.utils.version import get_docs_version as get_docs_version

CSRF_FAILURE_TEMPLATE_NAME: str

def builtin_template_path(name): ...
def csrf_failure(request, reason: str = '', template_name=...): ...
