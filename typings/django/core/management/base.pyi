from _typeshed import Incomplete
from argparse import ArgumentParser, HelpFormatter
from django.core import checks as checks
from django.core.exceptions import ImproperlyConfigured as ImproperlyConfigured
from django.core.management.color import color_style as color_style, no_style as no_style
from django.db import DEFAULT_DB_ALIAS as DEFAULT_DB_ALIAS, connections as connections
from io import TextIOBase

ALL_CHECKS: str

class CommandError(Exception):
    returncode: Incomplete
    def __init__(self, *args, returncode: int = 1, **kwargs) -> None: ...

class SystemCheckError(CommandError): ...

class CommandParser(ArgumentParser):
    missing_args_message: Incomplete
    called_from_command_line: Incomplete
    def __init__(self, *, missing_args_message: Incomplete | None = None, called_from_command_line: Incomplete | None = None, **kwargs) -> None: ...
    def parse_args(self, args: Incomplete | None = None, namespace: Incomplete | None = None): ...
    def error(self, message) -> None: ...
    def add_subparsers(self, **kwargs): ...

def handle_default_options(options) -> None: ...
def no_translations(handle_func): ...

class DjangoHelpFormatter(HelpFormatter):
    show_last: Incomplete
    def add_usage(self, usage, actions, *args, **kwargs) -> None: ...
    def add_arguments(self, actions) -> None: ...

class OutputWrapper(TextIOBase):
    @property
    def style_func(self): ...
    @style_func.setter
    def style_func(self, style_func): ...
    ending: Incomplete
    def __init__(self, out, ending: str = '\n') -> None: ...
    def __getattr__(self, name): ...
    def flush(self) -> None: ...
    def isatty(self): ...
    def write(self, msg: str = '', style_func: Incomplete | None = None, ending: Incomplete | None = None) -> None: ...

class BaseCommand:
    help: str
    output_transaction: bool
    requires_migrations_checks: bool
    requires_system_checks: str
    base_stealth_options: Incomplete
    stealth_options: Incomplete
    suppressed_base_arguments: Incomplete
    stdout: Incomplete
    stderr: Incomplete
    style: Incomplete
    def __init__(self, stdout: Incomplete | None = None, stderr: Incomplete | None = None, no_color: bool = False, force_color: bool = False) -> None: ...
    def get_version(self): ...
    def create_parser(self, prog_name, subcommand, **kwargs): ...
    def add_arguments(self, parser) -> None: ...
    def add_base_argument(self, parser, *args, **kwargs) -> None: ...
    def print_help(self, prog_name, subcommand) -> None: ...
    def run_from_argv(self, argv): ...
    def execute(self, *args, **options): ...
    def check(self, app_configs: Incomplete | None = None, tags: Incomplete | None = None, display_num_errors: bool = False, include_deployment_checks: bool = False, fail_level=..., databases: Incomplete | None = None): ...
    def check_migrations(self) -> None: ...
    def handle(self, *args, **options) -> None: ...

class AppCommand(BaseCommand):
    missing_args_message: str
    def add_arguments(self, parser) -> None: ...
    def handle(self, *app_labels, **options): ...
    def handle_app_config(self, app_config, **options) -> None: ...

class LabelCommand(BaseCommand):
    label: str
    missing_args_message: Incomplete
    def add_arguments(self, parser) -> None: ...
    def handle(self, *labels, **options): ...
    def handle_label(self, label, **options) -> None: ...