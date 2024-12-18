from django.conf import settings as settings
from django.contrib.staticfiles.handlers import StaticFilesHandler as StaticFilesHandler
from django.core.management.commands.runserver import Command as RunserverCommand

class Command(RunserverCommand):
    help: str
    def add_arguments(self, parser) -> None: ...
    def get_handler(self, *args, **options): ...
