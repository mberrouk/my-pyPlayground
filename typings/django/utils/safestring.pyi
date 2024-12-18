from django.utils.functional import keep_lazy as keep_lazy

class SafeData:
    def __html__(self): ...

class SafeString(str, SafeData):
    def __add__(self, rhs): ...
SafeText = SafeString

def mark_safe(s): ...
