from _typeshed import Incomplete
from django.utils.html import avoid_wrapping as avoid_wrapping
from django.utils.timezone import is_aware as is_aware
from django.utils.translation import gettext as gettext, ngettext_lazy as ngettext_lazy

TIME_STRINGS: Incomplete
TIME_STRINGS_KEYS: Incomplete
TIME_CHUNKS: Incomplete
MONTHS_DAYS: Incomplete

def timesince(d, now: Incomplete | None = None, reversed: bool = False, time_strings: Incomplete | None = None, depth: int = 2): ...
def timeuntil(d, now: Incomplete | None = None, time_strings: Incomplete | None = None, depth: int = 2): ...
