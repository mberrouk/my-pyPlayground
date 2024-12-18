from _typeshed import Incomplete
from django.db.models.utils import make_model_tuple as make_model_tuple
from django.dispatch import Signal as Signal

class_prepared: Incomplete

class ModelSignal(Signal):
    def connect(self, receiver, sender: Incomplete | None = None, weak: bool = True, dispatch_uid: Incomplete | None = None, apps: Incomplete | None = None) -> None: ...
    def disconnect(self, receiver: Incomplete | None = None, sender: Incomplete | None = None, dispatch_uid: Incomplete | None = None, apps: Incomplete | None = None): ...

pre_init: Incomplete
post_init: Incomplete
pre_save: Incomplete
post_save: Incomplete
pre_delete: Incomplete
post_delete: Incomplete
m2m_changed: Incomplete
pre_migrate: Incomplete
post_migrate: Incomplete
