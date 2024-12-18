from _typeshed import Incomplete
from django.conf import settings as settings
from django.core.management.base import BaseCommand as BaseCommand, CommandError as CommandError
from django.core.servers.basehttp import WSGIServer as WSGIServer, get_internal_wsgi_application as get_internal_wsgi_application, run as run
from django.db import connections as connections
from django.utils import autoreload as autoreload

naiveip_re: Incomplete

class Command(BaseCommand):
    help: str
    requires_system_checks: Incomplete
    stealth_options: Incomplete
    suppressed_base_arguments: Incomplete
    default_addr: str
    default_addr_ipv6: str
    default_port: str
    protocol: str
    server_cls = WSGIServer
    def add_arguments(self, parser) -> None: ...
    def execute(self, *args, **options) -> None: ...
    def get_handler(self, *args, **options): ...
    use_ipv6: Incomplete
    addr: str
    port: Incomplete
    def handle(self, *args, **options) -> None: ...
    def run(self, **options) -> None: ...
    def inner_run(self, *args, **options) -> None: ...
    def on_bind(self, server_port) -> None: ...
