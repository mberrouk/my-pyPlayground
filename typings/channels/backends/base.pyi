import abc
from ..types import SendOptions as SendOptions
from abc import abstractmethod

class BaseChannel(metaclass=abc.ABCMeta):
    @abstractmethod
    def send(self, message: Text, fail_silently: bool = False, options: Optional[SendOptions] = None) -> None: ...
