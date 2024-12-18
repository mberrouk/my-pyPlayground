from django.db.models import fields as fields

class OrderWrt(fields.IntegerField):
    def __init__(self, *args, **kwargs) -> None: ...
