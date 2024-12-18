from _typeshed import Incomplete
from django.contrib.auth import get_user_model as get_user_model
from django.contrib.auth.management import get_default_username as get_default_username
from django.contrib.auth.password_validation import validate_password as validate_password
from django.core import exceptions as exceptions
from django.core.management.base import BaseCommand as BaseCommand, CommandError as CommandError
from django.db import DEFAULT_DB_ALIAS as DEFAULT_DB_ALIAS, connections as connections
from django.utils.functional import cached_property as cached_property
from django.utils.text import capfirst as capfirst

class NotRunningInTTYException(Exception): ...

PASSWORD_FIELD: str

class Command(BaseCommand):
    help: str
    requires_migrations_checks: bool
    stealth_options: Incomplete
    UserModel: Incomplete
    username_field: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def add_arguments(self, parser) -> None: ...
    stdin: Incomplete
    def execute(self, *args, **options): ...
    def handle(self, *args, **options) -> None: ...
    def get_input_data(self, field, message, default: Incomplete | None = None): ...
    def username_is_unique(self): ...
