"""
This type stub file was generated by pyright.
"""

"""
This type stub file was generated by pyright.
"""
class TemplateDoesNotExist(Exception):
    """
    The exception used when a template does not exist. Optional arguments:

    backend
        The template backend class used when raising this exception.

    tried
        A list of sources that were tried when finding the template. This
        is formatted as a list of tuples containing (origin, status), where
        origin is an Origin object or duck type and status is a string with the
        reason the template wasn't found.

    chain
        A list of intermediate TemplateDoesNotExist exceptions. This is used to
        encapsulate multiple exceptions when loading templates from multiple
        engines.
    """
    def __init__(self, msg, tried=..., backend=..., chain=...) -> None:
        ...
    


class TemplateSyntaxError(Exception):
    """
    The exception used for syntax errors during parsing or rendering.
    """
    ...


