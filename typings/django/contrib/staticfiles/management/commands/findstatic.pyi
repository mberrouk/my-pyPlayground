from django.contrib.staticfiles import finders as finders
from django.core.management.base import LabelCommand as LabelCommand

class Command(LabelCommand):
    help: str
    label: str
    def add_arguments(self, parser) -> None: ...
    def handle_label(self, path, **options): ...
