from _typeshed import Incomplete
from django.contrib import admin as admin
from django.contrib.flatpages.forms import FlatpageForm as FlatpageForm
from django.contrib.flatpages.models import FlatPage as FlatPage

class FlatPageAdmin(admin.ModelAdmin):
    form = FlatpageForm
    fieldsets: Incomplete
    list_display: Incomplete
    list_filter: Incomplete
    search_fields: Incomplete
