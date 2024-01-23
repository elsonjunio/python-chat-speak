from abc import ABC, abstractmethod


class TextToSpeach(ABC):
    @abstractmethod
    def say(self, text: str):
        raise NotImplementedError
