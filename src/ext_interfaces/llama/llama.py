from llama_cpp import Llama

from core.llm import LLM


class LammaCpp(LLM):
    def __init__(
        self, model_path: str, n_ctx: int, max_tokens: int = 512
    ) -> None:
        self.llm = Llama(model_path=f'{model_path}', n_ctx=n_ctx)
        self.max_tokens = max_tokens
        # warming_output
        self.llm(
            'Q: Name the planets in the solar system? --A++: ',
            max_tokens=self.max_tokens,
            stop=['Q:', '\n'],
            echo=True,
        )

    def chat(self, prompt: str):
        output = self.llm(
            f'Q: {prompt} --A++: ',
            max_tokens=self.max_tokens,
            stop=[
                'Q:',
                '\n',
            ],
            echo=True,
        )
        print(output)

        message = output['choices'][0]['text']

        return message.split('--A++:')[1].strip()
