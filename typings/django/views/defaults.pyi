from django.http import HttpResponseBadRequest as HttpResponseBadRequest, HttpResponseForbidden as HttpResponseForbidden, HttpResponseNotFound as HttpResponseNotFound, HttpResponseServerError as HttpResponseServerError
from django.template import Context as Context, Engine as Engine, TemplateDoesNotExist as TemplateDoesNotExist, loader as loader
from django.views.decorators.csrf import requires_csrf_token as requires_csrf_token

ERROR_404_TEMPLATE_NAME: str
ERROR_403_TEMPLATE_NAME: str
ERROR_400_TEMPLATE_NAME: str
ERROR_500_TEMPLATE_NAME: str
ERROR_PAGE_TEMPLATE: str

def page_not_found(request, exception, template_name=...): ...
def server_error(request, template_name=...): ...
def bad_request(request, exception, template_name=...): ...
def permission_denied(request, exception, template_name=...): ...
