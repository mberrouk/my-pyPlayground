from django.core.exceptions import SuspiciousFileOperation as SuspiciousFileOperation

def safe_join(base, *paths): ...
def symlinks_supported(): ...
def to_path(value): ...