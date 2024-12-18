from django.conf import settings as settings
from django.contrib.staticfiles import finders as finders
from django.http import Http404 as Http404
from django.views import static as static

def serve(request, path, insecure: bool = False, **kwargs): ...
