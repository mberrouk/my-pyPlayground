"""
ASGI config for tic_tac_toe project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.urls import path

from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator
from channels.routing import ProtocolTypeRouter, URLRouter

from game.routing import websocket_urlpatterns

# from game.consumers import GameConsumer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tic_tac_toe.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        ),
        # "websocket": AuthMiddlewareStack(
        #     URLRouter(
        #         [
        #             path("ws/game/<int:id>/", GameConsumer.as_asgi()),
        #         ]
        #     )
        # ),
    }
)
