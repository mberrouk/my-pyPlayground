from django.conf import settings as settings
from django.contrib.flatpages.models import FlatPage as FlatPage
from django.contrib.sites.shortcuts import get_current_site as get_current_site
from django.http import Http404 as Http404, HttpResponse as HttpResponse, HttpResponsePermanentRedirect as HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404 as get_object_or_404
from django.template import loader as loader
from django.utils.safestring import mark_safe as mark_safe
from django.views.decorators.csrf import csrf_protect as csrf_protect

DEFAULT_TEMPLATE: str

def flatpage(request, url): ...
def render_flatpage(request, f): ...
