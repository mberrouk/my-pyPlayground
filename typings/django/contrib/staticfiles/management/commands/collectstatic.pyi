from _typeshed import Incomplete
from django.apps import apps as apps
from django.contrib.staticfiles.finders import get_finders as get_finders
from django.contrib.staticfiles.storage import staticfiles_storage as staticfiles_storage
from django.core.checks import Tags as Tags
from django.core.files.storage import FileSystemStorage as FileSystemStorage
from django.core.management.base import BaseCommand as BaseCommand, CommandError as CommandError
from django.core.management.color import no_style as no_style
from django.utils.functional import cached_property as cached_property

class Command(BaseCommand):
    help: str
    requires_system_checks: Incomplete
    copied_files: Incomplete
    symlinked_files: Incomplete
    unmodified_files: Incomplete
    post_processed_files: Incomplete
    storage: Incomplete
    style: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def local(self): ...
    def add_arguments(self, parser) -> None: ...
    interactive: Incomplete
    verbosity: Incomplete
    symlink: Incomplete
    clear: Incomplete
    dry_run: Incomplete
    ignore_patterns: Incomplete
    post_process: Incomplete
    def set_options(self, **options) -> None: ...
    def collect(self): ...
    def handle(self, **options): ...
    def log(self, msg, level: int = 2) -> None: ...
    def is_local_storage(self): ...
    def clear_dir(self, path) -> None: ...
    def delete_file(self, path, prefixed_path, source_storage): ...
    def link_file(self, path, prefixed_path, source_storage): ...
    def copy_file(self, path, prefixed_path, source_storage): ...
