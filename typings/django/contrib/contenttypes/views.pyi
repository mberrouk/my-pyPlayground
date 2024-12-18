from django.apps import apps as apps
from django.contrib.contenttypes.models import ContentType as ContentType
from django.contrib.sites.shortcuts import get_current_site as get_current_site
from django.core.exceptions import ObjectDoesNotExist as ObjectDoesNotExist
from django.http import Http404 as Http404, HttpResponseRedirect as HttpResponseRedirect

def shortcut(request, content_type_id, object_id): ...
