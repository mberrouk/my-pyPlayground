from _typeshed import Incomplete
from django.core.management.base import BaseCommand as BaseCommand, CommandError as CommandError
from django.core.management.utils import find_command as find_command, is_ignored_path as is_ignored_path, popen_wrapper as popen_wrapper

def has_bom(fn): ...
def is_writable(path): ...

class Command(BaseCommand):
    help: str
    requires_system_checks: Incomplete
    program: str
    program_options: Incomplete
    def add_arguments(self, parser) -> None: ...
    verbosity: Incomplete
    has_errors: bool
    def handle(self, **options) -> None: ...
    def compile_messages(self, locations) -> None: ...
