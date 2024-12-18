from _typeshed import Incomplete
from django.http import HttpResponseNotAllowed as HttpResponseNotAllowed
from django.middleware.http import ConditionalGetMiddleware as ConditionalGetMiddleware
from django.utils import timezone as timezone
from django.utils.cache import get_conditional_response as get_conditional_response
from django.utils.decorators import decorator_from_middleware as decorator_from_middleware
from django.utils.http import http_date as http_date, quote_etag as quote_etag
from django.utils.log import log_response as log_response

conditional_page: Incomplete

def require_http_methods(request_method_list): ...

require_GET: Incomplete
require_POST: Incomplete
require_safe: Incomplete

def condition(etag_func: Incomplete | None = None, last_modified_func: Incomplete | None = None): ...
def etag(etag_func): ...
def last_modified(last_modified_func): ...
