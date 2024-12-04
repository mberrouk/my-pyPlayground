from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
import os

from echo.consumers import EchoConsumer

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "simple_channels.settings")
app = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": URLRouter(
            [
                path("", EchoConsumer.as_asgi()),
            ]
        ),
    }
)
