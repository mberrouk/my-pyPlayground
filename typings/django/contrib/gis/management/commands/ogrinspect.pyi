import argparse
from _typeshed import Incomplete
from django.contrib.gis import gdal as gdal
from django.core.management.base import BaseCommand as BaseCommand, CommandError as CommandError
from django.utils.inspect import get_func_args as get_func_args

class LayerOptionAction(argparse.Action):
    def __call__(self, parser, namespace, value, option_string: Incomplete | None = None) -> None: ...

class ListOptionAction(argparse.Action):
    def __call__(self, parser, namespace, value, option_string: Incomplete | None = None) -> None: ...

class Command(BaseCommand):
    help: str
    requires_system_checks: Incomplete
    def add_arguments(self, parser) -> None: ...
    def handle(self, *args, **options): ...
