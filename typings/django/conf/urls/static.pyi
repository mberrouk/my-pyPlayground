from django.conf import settings as settings
from django.core.exceptions import ImproperlyConfigured as ImproperlyConfigured
from django.urls import re_path as re_path
from django.views.static import serve as serve

def static(prefix, view=..., **kwargs): ...
