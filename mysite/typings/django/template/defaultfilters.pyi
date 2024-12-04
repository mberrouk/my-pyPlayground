"""
This type stub file was generated by pyright.
"""

"""Default variable filters."""
register = ...
def stringfilter(func): # -> _Wrapped[Callable[..., Any], Any, Callable[..., Any], Any | _Wrapped[Callable[..., Any], object, Callable[..., Any], Any] | SafeString]:
    """
    Decorator for filters which should only receive strings. The object
    passed as the first positional argument will be converted to a string.
    """
    ...

@register.filter(is_safe=True)
@stringfilter
def addslashes(value):
    """
    Add slashes before quotes. Useful for escaping strings in CSV, for
    example. Less useful for escaping JavaScript; use the ``escapejs``
    filter instead.
    """
    ...

@register.filter(is_safe=True)
@stringfilter
def capfirst(value):
    """Capitalize the first character of the value."""
    ...

@register.filter("escapejs")
@stringfilter
def escapejs_filter(value): # -> _Wrapped[Callable[..., Any], object, Callable[..., Any], Any] | SafeString:
    """Hex encode characters for use in JavaScript strings."""
    ...

@register.filter(is_safe=True)
def json_script(value, element_id=...): # -> _Wrapped[Callable[..., Any], object, Callable[..., Any], Any] | SafeString:
    """
    Output value JSON-encoded, wrapped in a <script type="application/json">
    tag (with an optional id).
    """
    ...

@register.filter(is_safe=True)
def floatformat(text, arg=...): # -> str | _Wrapped[Callable[..., Any], object, Callable[..., Any], Any] | SafeString:
    """
    Display a float to a specified number of decimal places.

    If called without an argument, display the floating point number with one
    decimal place -- but only if there's a decimal place to be displayed:

    * num1 = 34.23234
    * num2 = 34.00000
    * num3 = 34.26000
    * {{ num1|floatformat }} displays "34.2"
    * {{ num2|floatformat }} displays "34"
    * {{ num3|floatformat }} displays "34.3"

    If arg is positive, always display exactly arg number of decimal places:

    * {{ num1|floatformat:3 }} displays "34.232"
    * {{ num2|floatformat:3 }} displays "34.000"
    * {{ num3|floatformat:3 }} displays "34.260"

    If arg is negative, display arg number of decimal places -- but only if
    there are places to be displayed:

    * {{ num1|floatformat:"-3" }} displays "34.232"
    * {{ num2|floatformat:"-3" }} displays "34"
    * {{ num3|floatformat:"-3" }} displays "34.260"

    If arg has the 'g' suffix, force the result to be grouped by the
    THOUSAND_SEPARATOR for the active locale. When the active locale is
    en (English):

    * {{ 6666.6666|floatformat:"2g" }} displays "6,666.67"
    * {{ 10000|floatformat:"g" }} displays "10,000"

    If arg has the 'u' suffix, force the result to be unlocalized. When the
    active locale is pl (Polish):

    * {{ 66666.6666|floatformat:"2" }} displays "66666,67"
    * {{ 66666.6666|floatformat:"2u" }} displays "66666.67"

    If the input float is infinity or NaN, display the string representation
    of that value.
    """
    ...

@register.filter(is_safe=True)
@stringfilter
def iriencode(value): # -> str:
    """Escape an IRI value for use in a URL."""
    ...

@register.filter(is_safe=True, needs_autoescape=True)
@stringfilter
def linenumbers(value, autoescape=...): # -> _Wrapped[Callable[..., Any], object, Callable[..., Any], Any] | SafeString:
    """Display text with line numbers."""
    ...

@register.filter(is_safe=True)
@stringfilter
def lower(value):
    """Convert a string into all lowercase."""
    ...

@register.filter(is_safe=False)
@stringfilter
def make_list(value): # -> list[Any]:
    """
    Return the value turned into a list.

    For an integer, it's a list of digits.
    For a string, it's a list of characters.
    """
    ...

@register.filter(is_safe=True)
@stringfilter
def slugify(value): # -> str:
    """
    Convert to ASCII. Convert spaces to hyphens. Remove characters that aren't
    alphanumerics, underscores, or hyphens. Convert to lowercase. Also strip
    leading and trailing whitespace.
    """
    ...

@register.filter(is_safe=True)
def stringformat(value, arg): # -> str:
    """
    Format the variable according to the arg, a string formatting specifier.

    This specifier uses Python string formatting syntax, with the exception
    that the leading "%" is dropped.

    See https://docs.python.org/library/stdtypes.html#printf-style-string-formatting
    for documentation of Python string formatting.
    """
    ...

@register.filter(is_safe=True)
@stringfilter
def title(value): # -> str:
    """Convert a string into titlecase."""
    ...

@register.filter(is_safe=True)
@stringfilter
def truncatechars(value, arg): # -> str | Any:
    """Truncate a string after `arg` number of characters."""
    ...

@register.filter(is_safe=True)
@stringfilter
def truncatechars_html(value, arg): # -> str | Any:
    """
    Truncate HTML after `arg` number of chars.
    Preserve newlines in the HTML.
    """
    ...

@register.filter(is_safe=True)
@stringfilter
def truncatewords(value, arg): # -> str | Any:
    """
    Truncate a string after `arg` number of words.
    Remove newlines within the string.
    """
    ...

@register.filter(is_safe=True)
@stringfilter
def truncatewords_html(value, arg): # -> str | Any:
    """
    Truncate HTML after `arg` number of words.
    Preserve newlines in the HTML.
    """
    ...

@register.filter(is_safe=False)
@stringfilter
def upper(value):
    """Convert a string into all uppercase."""
    ...

@register.filter(is_safe=False)
@stringfilter
def urlencode(value, safe=...): # -> str:
    """
    Escape a value for use in a URL.

    The ``safe`` parameter determines the characters which should not be
    escaped by Python's quote() function. If not provided, use the default safe
    characters (but an empty string can be provided when *all* characters
    should be escaped).
    """
    ...

@register.filter(is_safe=True, needs_autoescape=True)
@stringfilter
def urlize(value, autoescape=...): # -> _Wrapped[Callable[..., Any], object, Callable[..., Any], Any] | SafeString:
    """Convert URLs in plain text into clickable links."""
    ...

@register.filter(is_safe=True, needs_autoescape=True)
@stringfilter
def urlizetrunc(value, limit, autoescape=...): # -> _Wrapped[Callable[..., Any], object, Callable[..., Any], Any] | SafeString:
    """
    Convert URLs into clickable links, truncating URLs to the given character
    limit, and adding 'rel=nofollow' attribute to discourage spamming.

    Argument: Length to truncate URLs to.
    """
    ...

@register.filter(is_safe=False)
@stringfilter
def wordcount(value): # -> int:
    """Return the number of words."""
    ...

@register.filter(is_safe=True)
@stringfilter
def wordwrap(value, arg): # -> LiteralString:
    """Wrap words at `arg` line length."""
    ...

@register.filter(is_safe=True)
@stringfilter
def ljust(value, arg):
    """Left-align the value in a field of a given width."""
    ...

@register.filter(is_safe=True)
@stringfilter
def rjust(value, arg):
    """Right-align the value in a field of a given width."""
    ...

@register.filter(is_safe=True)
@stringfilter
def center(value, arg):
    """Center the value in a field of a given width."""
    ...

@register.filter
@stringfilter
def cut(value, arg): # -> _Wrapped[Callable[..., Any], object, Callable[..., Any], Any] | SafeString:
    """Remove all values of arg from the given string."""
    ...

@register.filter("escape", is_safe=True)
@stringfilter
def escape_filter(value): # -> SafeString:
    """Mark the value as a string that should be auto-escaped."""
    ...

@register.filter(is_safe=True)
def escapeseq(value): # -> list[Any | SafeString]:
    """
    An "escape" filter for sequences. Mark each element in the sequence,
    individually, as a string that should be auto-escaped. Return a list with
    the results.
    """
    ...

@register.filter(is_safe=True)
@stringfilter
def force_escape(value): # -> SafeString:
    """
    Escape a string's HTML. Return a new string containing the escaped
    characters (as opposed to "escape", which marks the content for later
    possible escaping).
    """
    ...

@register.filter("linebreaks", is_safe=True, needs_autoescape=True)
@stringfilter
def linebreaks_filter(value, autoescape=...): # -> _Wrapped[Callable[..., Any], object, Callable[..., Any], Any] | SafeString:
    """
    Replace line breaks in plain text with appropriate HTML; a single
    newline becomes an HTML line break (``<br>``) and a new line
    followed by a blank line becomes a paragraph break (``</p>``).
    """
    ...

@register.filter(is_safe=True, needs_autoescape=True)
@stringfilter
def linebreaksbr(value, autoescape=...): # -> _Wrapped[Callable[..., Any], object, Callable[..., Any], Any] | SafeString:
    """
    Convert all newlines in a piece of plain text to HTML line breaks
    (``<br>``).
    """
    ...

@register.filter(is_safe=True)
@stringfilter
def safe(value): # -> _Wrapped[Callable[..., Any], object, Callable[..., Any], Any] | SafeString:
    """Mark the value as a string that should not be auto-escaped."""
    ...

@register.filter(is_safe=True)
def safeseq(value): # -> list[Any | _Wrapped[Callable[..., Any], object, Callable[..., Any], Any] | SafeString]:
    """
    A "safe" filter for sequences. Mark each element in the sequence,
    individually, as safe, after converting them to strings. Return a list
    with the results.
    """
    ...

@register.filter(is_safe=True)
@stringfilter
def striptags(value): # -> str | LiteralString:
    """Strip all [X]HTML tags."""
    ...

@register.filter(is_safe=False)
def dictsort(value, arg): # -> list[Any] | Literal['']:
    """
    Given a list of dicts, return that list sorted by the property given in
    the argument.
    """
    ...

@register.filter(is_safe=False)
def dictsortreversed(value, arg): # -> list[Any] | Literal['']:
    """
    Given a list of dicts, return that list sorted in reverse order by the
    property given in the argument.
    """
    ...

@register.filter(is_safe=False)
def first(value): # -> Literal['']:
    """Return the first item in a list."""
    ...

@register.filter(is_safe=True, needs_autoescape=True)
def join(value, arg, autoescape=...): # -> _Wrapped[Callable[..., Any], object, Callable[..., Any], Any] | SafeString:
    """Join a list with a string, like Python's ``str.join(list)``."""
    ...

@register.filter(is_safe=True)
def last(value): # -> Literal['']:
    """Return the last item in a list."""
    ...

@register.filter(is_safe=False)
def length(value): # -> int:
    """Return the length of the value - useful for lists."""
    ...

@register.filter(is_safe=True)
def random(value): # -> Literal['']:
    """Return a random item from the list."""
    ...

@register.filter("slice", is_safe=True)
def slice_filter(value, arg):
    """
    Return a slice of the list using the same syntax as Python's list slicing.
    """
    ...

@register.filter(is_safe=True, needs_autoescape=True)
def unordered_list(value, autoescape=...): # -> _Wrapped[Callable[..., Any], object, Callable[..., Any], Any] | SafeString:
    """
    Recursively take a self-nested list and return an HTML unordered list --
    WITHOUT opening and closing <ul> tags.

    Assume the list is in the proper format. For example, if ``var`` contains:
    ``['States', ['Kansas', ['Lawrence', 'Topeka'], 'Illinois']]``, then
    ``{{ var|unordered_list }}`` returns::

        <li>States
        <ul>
                <li>Kansas
                <ul>
                        <li>Lawrence</li>
                        <li>Topeka</li>
                </ul>
                </li>
                <li>Illinois</li>
        </ul>
        </li>
    """
    ...

@register.filter(is_safe=False)
def add(value, arg): # -> int | Literal['']:
    """Add the arg to the value."""
    ...

@register.filter(is_safe=False)
def get_digit(value, arg): # -> int:
    """
    Given a whole number, return the requested digit of it, where 1 is the
    right-most digit, 2 is the second-right-most digit, etc. Return the
    original value for invalid input (if input or argument is not an integer,
    or if argument is less than 1). Otherwise, output is always an integer.
    """
    ...

@register.filter(expects_localtime=True, is_safe=False)
def date(value, arg=...): # -> LiteralString | Literal['']:
    """Format a date according to the given format."""
    ...

@register.filter(expects_localtime=True, is_safe=False)
def time(value, arg=...): # -> LiteralString | Literal['']:
    """Format a time according to the given format."""
    ...

@register.filter("timesince", is_safe=False)
def timesince_filter(value, arg=...): # -> Any | Literal['']:
    """Format a date as the time since that date (i.e. "4 days, 6 hours")."""
    ...

@register.filter("timeuntil", is_safe=False)
def timeuntil_filter(value, arg=...): # -> Any | Literal['']:
    """Format a date as the time until that date (i.e. "4 days, 6 hours")."""
    ...

@register.filter(is_safe=False)
def default(value, arg):
    """If value is unavailable, use given default."""
    ...

@register.filter(is_safe=False)
def default_if_none(value, arg):
    """If value is None, use given default."""
    ...

@register.filter(is_safe=False)
def divisibleby(value, arg): # -> bool:
    """Return True if the value is divisible by the argument."""
    ...

@register.filter(is_safe=False)
def yesno(value, arg=...): # -> Any:
    """
    Given a string mapping values for true, false, and (optionally) None,
    return one of those strings according to the value:

    ==========  ======================  ==================================
    Value       Argument                Outputs
    ==========  ======================  ==================================
    ``True``    ``"yeah,no,maybe"``     ``yeah``
    ``False``   ``"yeah,no,maybe"``     ``no``
    ``None``    ``"yeah,no,maybe"``     ``maybe``
    ``None``    ``"yeah,no"``           ``"no"`` (converts None to False
                                        if no mapping for None is given.
    ==========  ======================  ==================================
    """
    ...

@register.filter(is_safe=True)
def filesizeformat(bytes_): # -> Any:
    """
    Format the value like a 'human-readable' file size (i.e. 13 KB, 4.1 MB,
    102 bytes, etc.).
    """
    ...

@register.filter(is_safe=False)
def pluralize(value, arg=...): # -> str:
    """
    Return a plural suffix if the value is not 1, '1', or an object of
    length 1. By default, use 's' as the suffix:

    * If value is 0, vote{{ value|pluralize }} display "votes".
    * If value is 1, vote{{ value|pluralize }} display "vote".
    * If value is 2, vote{{ value|pluralize }} display "votes".

    If an argument is provided, use that string instead:

    * If value is 0, class{{ value|pluralize:"es" }} display "classes".
    * If value is 1, class{{ value|pluralize:"es" }} display "class".
    * If value is 2, class{{ value|pluralize:"es" }} display "classes".

    If the provided argument contains a comma, use the text before the comma
    for the singular case and the text after the comma for the plural case:

    * If value is 0, cand{{ value|pluralize:"y,ies" }} display "candies".
    * If value is 1, cand{{ value|pluralize:"y,ies" }} display "candy".
    * If value is 2, cand{{ value|pluralize:"y,ies" }} display "candies".
    """
    ...

@register.filter("phone2numeric", is_safe=True)
def phone2numeric_filter(value): # -> str:
    """Take a phone number and converts it in to its numerical equivalent."""
    ...

@register.filter(is_safe=True)
def pprint(value): # -> str:
    """A wrapper around pprint.pprint -- for debugging, really."""
    ...
