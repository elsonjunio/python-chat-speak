from abc import ABC, abstractmethod


class NLP(ABC):
    @abstractmethod
    def train(self):
        raise NotImplementedError

    @abstractmethod
    def text(self, text: str):
        raise NotImplementedError
