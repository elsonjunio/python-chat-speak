from abc import ABC, abstractmethod


class LLM(ABC):
    @abstractmethod
    def chat(self, prompt: str):
        raise NotImplementedError
