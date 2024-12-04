"""
This type stub file was generated by pyright.
"""

class BaseDatabaseValidation:
    """Encapsulate backend-specific validation."""
    def __init__(self, connection) -> None:
        ...
    
    def check(self, **kwargs): # -> list[Any]:
        ...
    
    def check_field(self, field, **kwargs): # -> list[Any]:
        ...
    

