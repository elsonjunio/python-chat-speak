from openai import OpenAI

from core.llm import LLM


class ChatGPT(LLM):
    def __init__(self, api_key: str, engine: str) -> None:
        self.client = OpenAI(
            api_key=api_key,
        )

        self.engine = engine

    def chat(self, prompt: str):
        completions = self.client.chat.completions.create(
            messages=[
                {
                    'role': 'user',
                    'content': prompt,
                }
            ],
            model=self.engine,
        )

        message = completions.choices[0].text
        return message.strip()
