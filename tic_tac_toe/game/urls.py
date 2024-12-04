from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("game/<int:id>/<str:name>/", views.game),
]
