"""
This type stub file was generated by pyright.
"""

from django.utils.functional import keep_lazy

"""
This type stub file was generated by pyright.
"""
class SafeData:
    __slots__ = ...
    def __html__(self):
        """
        Return the html representation of a string for interoperability.

        This allows other template engines to understand Django's SafeData.
        """
        ...
    


class SafeString(str, SafeData):
    """
    A str subclass that has been specifically marked as "safe" for HTML output
    purposes.
    """
    __slots__ = ...
    def __add__(self, rhs):
        """
        Concatenating a safe string with another safe bytestring or
        safe string is safe. Otherwise, the result is no longer safe.
        """
        ...
    
    def __str__(self) -> str:
        ...
    


SafeText = SafeString
@keep_lazy(SafeString)
def mark_safe(s):
    """
    Explicitly mark a string as safe for (HTML) output purposes. The returned
    object can be used everywhere a string is appropriate.

    If used on a method as a decorator, mark the returned data as safe.

    Can be called multiple times on a single string.
    """
    ...
