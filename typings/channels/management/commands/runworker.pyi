from _typeshed import Incomplete
from channels import DEFAULT_CHANNEL_LAYER as DEFAULT_CHANNEL_LAYER
from channels.layers import get_channel_layer as get_channel_layer
from channels.routing import get_default_application as get_default_application
from channels.worker import Worker as Worker
from django.core.management import BaseCommand

logger: Incomplete

class Command(BaseCommand):
    leave_locale_alone: bool
    worker_class = Worker
    def add_arguments(self, parser) -> None: ...
    verbosity: Incomplete
    channel_layer: Incomplete
    def handle(self, *args, **options) -> None: ...
