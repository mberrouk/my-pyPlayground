from django.conf import settings as settings
from django.core.management.color import no_style as no_style
from django.db import DEFAULT_DB_ALIAS as DEFAULT_DB_ALIAS, connections as connections, router as router

def create_default_site(app_config, verbosity: int = 2, interactive: bool = True, using=..., apps=..., **kwargs) -> None: ...
