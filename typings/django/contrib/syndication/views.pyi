from _typeshed import Incomplete
from django.contrib.sites.shortcuts import get_current_site as get_current_site
from django.core.exceptions import ImproperlyConfigured as ImproperlyConfigured, ObjectDoesNotExist as ObjectDoesNotExist
from django.http import Http404 as Http404, HttpResponse as HttpResponse
from django.template import TemplateDoesNotExist as TemplateDoesNotExist, loader as loader
from django.utils import feedgenerator as feedgenerator
from django.utils.encoding import iri_to_uri as iri_to_uri
from django.utils.html import escape as escape
from django.utils.http import http_date as http_date
from django.utils.timezone import get_default_timezone as get_default_timezone, is_naive as is_naive, make_aware as make_aware
from django.utils.translation import get_language as get_language

def add_domain(domain, url, secure: bool = False): ...

class FeedDoesNotExist(ObjectDoesNotExist): ...

class Feed:
    feed_type: Incomplete
    title_template: Incomplete
    description_template: Incomplete
    language: Incomplete
    def __call__(self, request, *args, **kwargs): ...
    def item_title(self, item): ...
    def item_description(self, item): ...
    def item_link(self, item): ...
    def item_enclosures(self, item): ...
    def feed_extra_kwargs(self, obj): ...
    def item_extra_kwargs(self, item): ...
    def get_object(self, request, *args, **kwargs) -> None: ...
    def get_context_data(self, **kwargs): ...
    def get_feed(self, obj, request): ...
