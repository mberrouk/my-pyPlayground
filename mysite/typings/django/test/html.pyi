"""
This type stub file was generated by pyright.
"""

from html.parser import HTMLParser

"""Compare two HTML documents."""
ASCII_WHITESPACE = ...
BOOLEAN_ATTRIBUTES = ...
def normalize_whitespace(string): # -> Any:
    ...

def normalize_attributes(attributes): # -> list[Any]:
    ...

class Element:
    def __init__(self, name, attributes) -> None:
        ...
    
    def append(self, element): # -> None:
        ...
    
    def finalize(self): # -> None:
        ...
    
    def __eq__(self, element) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __contains__(self, element): # -> bool:
        ...
    
    def count(self, element): # -> int:
        ...
    
    def __getitem__(self, key):
        ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self): # -> str:
        ...
    


class RootElement(Element):
    def __init__(self) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class HTMLParseError(Exception):
    ...


class Parser(HTMLParser):
    def __init__(self) -> None:
        ...
    
    def error(self, msg):
        ...
    
    def format_position(self, position=..., element=...): # -> LiteralString | str:
        ...
    
    @property
    def current(self): # -> RootElement:
        ...
    
    def handle_startendtag(self, tag, attrs): # -> None:
        ...
    
    def handle_starttag(self, tag, attrs): # -> None:
        ...
    
    def handle_endtag(self, tag): # -> None:
        ...
    
    def handle_data(self, data): # -> None:
        ...
    


def parse_html(html): # -> RootElement:
    """
    Take a string that contains HTML and turn it into a Python object structure
    that can be easily compared against other HTML on semantic equivalence.
    Syntactical differences like which quotation is used on arguments will be
    ignored.
    """
    ...

