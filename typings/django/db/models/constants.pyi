from enum import Enum

LOOKUP_SEP: str

class OnConflict(Enum):
    IGNORE = 'ignore'
    UPDATE = 'update'
