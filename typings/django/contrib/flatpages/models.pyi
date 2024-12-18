from _typeshed import Incomplete
from django.contrib.sites.models import Site as Site
from django.db import models as models
from django.urls import NoReverseMatch as NoReverseMatch, get_script_prefix as get_script_prefix, reverse as reverse
from django.utils.encoding import iri_to_uri as iri_to_uri

class FlatPage(models.Model):
    url: Incomplete
    title: Incomplete
    content: Incomplete
    enable_comments: Incomplete
    template_name: Incomplete
    registration_required: Incomplete
    sites: Incomplete
    class Meta:
        db_table: str
        verbose_name: Incomplete
        verbose_name_plural: Incomplete
        ordering: Incomplete
    def get_absolute_url(self): ...
