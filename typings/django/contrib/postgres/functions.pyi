from _typeshed import Incomplete
from django.db.models import DateTimeField as DateTimeField, Func as Func, UUIDField as UUIDField

class RandomUUID(Func):
    template: str
    output_field: Incomplete

class TransactionNow(Func):
    template: str
    output_field: Incomplete
