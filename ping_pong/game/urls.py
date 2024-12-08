from django.urls import path

from . import views

urlpatterns = [path("", views.index), path("game/<int:id>/<str:name>/", views.game)]
