from django.contrib.sitemaps import Sitemap as Sitemap
from django.core.exceptions import ImproperlyConfigured as ImproperlyConfigured

class FlatPageSitemap(Sitemap):
    def items(self): ...
