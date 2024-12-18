from ctypes import Structure, Union, c_int64, c_ulong, c_void_p

__all__ = ['LOCK_EX', 'LOCK_SH', 'LOCK_NB', 'lock', 'unlock']

LOCK_SH: int
LOCK_NB: int
LOCK_EX: int
ULONG_PTR = c_int64
ULONG_PTR = c_ulong
PVOID = c_void_p

class _OFFSET(Structure): ...
class _OFFSET_UNION(Union): ...
class OVERLAPPED(Structure): ...

def lock(f, flags): ...
def unlock(f): ...
