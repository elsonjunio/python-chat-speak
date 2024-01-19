import openai


class ChatGPT(object):
    def __init__(self, api_key: str) -> None:
        openai.api_key = api_key

    def chat(self, prompt, engine):
        completions = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )

        message = completions.choices[0].text
        return message.strip()
