from openai import OpenAI


class ChatGPT(object):
    def __init__(self, api_key: str) -> None:
        self.client = OpenAI(
            api_key=api_key,
        )

    def chat(self, prompt, engine):
        completions = self.client.chat.completions.create(
            messages=[
                {
                    'role': 'user',
                    'content': prompt,
                }
            ],
            model=engine,
        )

        message = completions.choices[0].text
        return message.strip()
