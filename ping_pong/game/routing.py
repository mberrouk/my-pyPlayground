from django.urls import path

from . import consumer

websocket_urlpatterns = [path("ws/game/<int:id>/", consumer.GameConsumer.as_asgi())]
