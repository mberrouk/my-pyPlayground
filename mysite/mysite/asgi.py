"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# for routing by protocol
from channels.routing import ProtocolTypeRouter, URLRouter

# from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

from chat.routing import websocket_urlpatterns


application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        # "websocket": AllowedHostsOriginValidator(
        #     AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        # ),
        "websocket": AuthMiddlewareStack(URLRouter(websocket_urlpatterns)),
    }
)
