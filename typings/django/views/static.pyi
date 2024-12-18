from _typeshed import Incomplete
from django.http import FileResponse as FileResponse, Http404 as Http404, HttpResponse as HttpResponse, HttpResponseNotModified as HttpResponseNotModified
from django.template import Context as Context, Engine as Engine, TemplateDoesNotExist as TemplateDoesNotExist, loader as loader
from django.utils._os import safe_join as safe_join
from django.utils.http import http_date as http_date, parse_http_date as parse_http_date
from django.utils.translation import gettext_lazy as gettext_lazy

def builtin_template_path(name): ...
def serve(request, path, document_root: Incomplete | None = None, show_indexes: bool = False): ...

template_translatable: Incomplete

def directory_index(path, fullpath): ...
def was_modified_since(header: Incomplete | None = None, mtime: int = 0): ...
