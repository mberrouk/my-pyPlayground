from _typeshed import Incomplete
from dataclasses import dataclass
from django.contrib.sites.shortcuts import get_current_site as get_current_site
from django.core.paginator import EmptyPage as EmptyPage, PageNotAnInteger as PageNotAnInteger
from django.http import Http404 as Http404
from django.template.response import TemplateResponse as TemplateResponse
from django.urls import reverse as reverse
from django.utils import timezone as timezone
from django.utils.http import http_date as http_date

@dataclass
class SitemapIndexItem:
    location: str
    last_mod: bool = ...
    def __init__(self, location, last_mod=...) -> None: ...

def x_robots_tag(func): ...
def index(request, sitemaps, template_name: str = 'sitemap_index.xml', content_type: str = 'application/xml', sitemap_url_name: str = 'django.contrib.sitemaps.views.sitemap'): ...
def sitemap(request, sitemaps, section: Incomplete | None = None, template_name: str = 'sitemap.xml', content_type: str = 'application/xml'): ...
