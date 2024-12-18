from _typeshed import Incomplete
from django.contrib.auth import get_user_model as get_user_model
from django.contrib.auth.password_validation import validate_password as validate_password
from django.core.exceptions import ValidationError as ValidationError
from django.core.management.base import BaseCommand as BaseCommand, CommandError as CommandError
from django.db import DEFAULT_DB_ALIAS as DEFAULT_DB_ALIAS, connections as connections

UserModel: Incomplete

class Command(BaseCommand):
    help: str
    requires_migrations_checks: bool
    requires_system_checks: Incomplete
    def add_arguments(self, parser) -> None: ...
    def handle(self, *args, **options): ...
