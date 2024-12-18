from _typeshed import Incomplete
from django import forms as forms
from django.conf import settings as settings
from django.contrib.flatpages.models import FlatPage as FlatPage
from django.core.exceptions import ValidationError as ValidationError
from django.utils.translation import gettext as gettext

class FlatpageForm(forms.ModelForm):
    url: Incomplete
    class Meta:
        model = FlatPage
        fields: str
    def __init__(self, *args, **kwargs) -> None: ...
    def clean_url(self): ...
    def clean(self): ...
