from typing import Dict

from ext_interfaces.nltk.nltk_use import NLTKUse
from ext_interfaces.speaker.speaker import Speaker
from ext_interfaces.s2t.speech_to_text import SpeechToText
from ext_interfaces.chatgpt.chatgpt import ChatGPT

command_list = ['arquivo', 'silenciar']

class Process(object):
    last_text = ''

    def __init__(self, speaker: Speaker, speech_to_text: SpeechToText, chatgpt: ChatGPT, nltk_use: NLTKUse) -> None:
        self.speaker = speaker
        self.speech_to_text = speech_to_text
        self.chatgpt = chatgpt
        self.nltk_use = nltk_use
        self.speech_to_text.listen(self.out)

    def command(self, cmd: str):

        # problemas de lógica :(

        response = self.nltk_use.text(cmd)
        
        if not response or cmd == '' or response in command_list:
            return

        if self.last_text and response == 'sim':
            text = self.chatgpt.chat(self.last_text, "davinci-002")
            self.speaker.say(text)
            self.last_text = ''
        elif self.last_text and response == 'nao':
            self.last_text = ''
        else:
            self.last_text = cmd
            self.speaker.say(f'Enviar ao LLM o text: {cmd}')

    def list_devices(self):
        print('Speaker Devices')
        self.speaker.list_voice()

        print('SpeechToText Devices')
        self.speech_to_text.get_device_list()

    def out(self, txt: Dict):
        print(f'Você disse: {txt["text"]}')
        # self.speaker.say(f'Você disse: {txt["text"]}')
        self.command(txt["text"])
