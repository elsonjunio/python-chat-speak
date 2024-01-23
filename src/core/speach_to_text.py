from abc import ABC, abstractmethod
from typing import Callable, Dict


class SpeachToText(ABC):
    @abstractmethod
    def listen(self, callback: Callable[[Dict], None], device_index=None):
        raise NotImplementedError
