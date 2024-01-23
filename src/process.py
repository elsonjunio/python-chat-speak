import inject
from typing import Dict
from core.llm import LLM
from core.nlp import NLP
from core.speach_to_text import SpeachToText
from core.text_to_speach import TextToSpeach


command_list = ['arquivo', 'silenciar']


class Process(object):
    last_text = ''

    @inject.autoparams()
    def __init__(
        self,
        text_to_speach: TextToSpeach,
        speech_to_text: SpeachToText,
        llm: LLM,
        nlp: NLP,
    ) -> None:
        self.text_to_speach = text_to_speach
        self.speech_to_text = speech_to_text
        self.llm = llm
        self.nlp = nlp
        self.speech_to_text.listen(self.out)

    def command(self, cmd: str):

        # problemas de lógica :(

        response = self.nlp.text(cmd)

        if not response or cmd == '' or response in command_list:
            return

        if self.last_text and response == 'sim':
            text = self.llm.chat(self.last_text)
            self.text_to_speach.say(text)
            self.last_text = ''
        elif self.last_text and response == 'nao':
            self.last_text = ''
        else:
            self.last_text = cmd
            self.text_to_speach.say(f'Enviar ao LLM o text: {cmd}')

    def list_devices(self):
        print('text_to_speach Devices')
        self.text_to_speach.list_voice()

        print('SpeechToText Devices')
        self.speech_to_text.get_device_list()

    def out(self, txt: Dict):
        print(f'Você disse: {txt["text"]}')
        # self.text_to_speach.say(f'Você disse: {txt["text"]}')
        self.command(txt['text'])
