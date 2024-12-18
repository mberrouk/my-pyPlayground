from .. import Error as Error, Tags as Tags, Warning as Warning, register as register
from _typeshed import Incomplete
from django.conf import settings as settings

W003: Incomplete
W016: Incomplete

def check_csrf_middleware(app_configs, **kwargs): ...
def check_csrf_cookie_secure(app_configs, **kwargs): ...
def check_csrf_failure_view(app_configs, **kwargs): ...
