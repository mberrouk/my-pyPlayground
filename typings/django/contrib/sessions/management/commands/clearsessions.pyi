from django.conf import settings as settings
from django.core.management.base import BaseCommand as BaseCommand, CommandError as CommandError

class Command(BaseCommand):
    help: str
    def handle(self, **options) -> None: ...
