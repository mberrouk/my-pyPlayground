from _typeshed import Incomplete
from django import template as template
from django.template import defaultfilters as defaultfilters
from django.utils.formats import number_format as number_format
from django.utils.safestring import mark_safe as mark_safe
from django.utils.timezone import is_aware as is_aware
from django.utils.translation import gettext_lazy as gettext_lazy, ngettext as ngettext, ngettext_lazy as ngettext_lazy, npgettext_lazy as npgettext_lazy, pgettext as pgettext, round_away_from_one as round_away_from_one

register: Incomplete

def ordinal(value): ...
def intcomma(value, use_l10n: bool = True): ...

intword_converters: Incomplete

def intword(value): ...
def apnumber(value): ...
def naturalday(value, arg: Incomplete | None = None): ...
def naturaltime(value): ...

class NaturalTimeFormatter:
    time_strings: Incomplete
    past_substrings: Incomplete
    future_substrings: Incomplete
    @classmethod
    def string_for(cls, value): ...
