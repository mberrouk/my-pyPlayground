from _typeshed import Incomplete
from ctypes import c_void_p

class CPointerBase:
    ptr_type = c_void_p
    destructor: Incomplete
    null_ptr_exception_class = AttributeError
    @property
    def ptr(self): ...
    @ptr.setter
    def ptr(self, ptr) -> None: ...
    def __del__(self) -> None: ...
