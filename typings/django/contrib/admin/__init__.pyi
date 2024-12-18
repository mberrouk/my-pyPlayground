from django.contrib.admin.decorators import action as action, display as display, register as register
from django.contrib.admin.filters import AllValuesFieldListFilter as AllValuesFieldListFilter, BooleanFieldListFilter as BooleanFieldListFilter, ChoicesFieldListFilter as ChoicesFieldListFilter, DateFieldListFilter as DateFieldListFilter, EmptyFieldListFilter as EmptyFieldListFilter, FieldListFilter as FieldListFilter, ListFilter as ListFilter, RelatedFieldListFilter as RelatedFieldListFilter, RelatedOnlyFieldListFilter as RelatedOnlyFieldListFilter, SimpleListFilter as SimpleListFilter
from django.contrib.admin.options import HORIZONTAL as HORIZONTAL, ModelAdmin as ModelAdmin, ShowFacets as ShowFacets, StackedInline as StackedInline, TabularInline as TabularInline, VERTICAL as VERTICAL
from django.contrib.admin.sites import AdminSite as AdminSite, site as site

__all__ = ['action', 'display', 'register', 'ModelAdmin', 'HORIZONTAL', 'VERTICAL', 'StackedInline', 'TabularInline', 'AdminSite', 'site', 'ListFilter', 'SimpleListFilter', 'FieldListFilter', 'BooleanFieldListFilter', 'RelatedFieldListFilter', 'ChoicesFieldListFilter', 'DateFieldListFilter', 'AllValuesFieldListFilter', 'EmptyFieldListFilter', 'RelatedOnlyFieldListFilter', 'ShowFacets', 'autodiscover']

def autodiscover() -> None: ...
