from ..utils import get_random_secret_key as get_random_secret_key
from django.core.checks.security.base import SECRET_KEY_INSECURE_PREFIX as SECRET_KEY_INSECURE_PREFIX
from django.core.management.templates import TemplateCommand as TemplateCommand

class Command(TemplateCommand):
    help: str
    missing_args_message: str
    def handle(self, **options) -> None: ...
