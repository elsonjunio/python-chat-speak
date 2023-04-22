from typing import Dict
from nltk_use import NLTKUse
from speaker import Speaker
from speech_to_text import SpeechToText
from chatgpt import ChatGPT


class Process(object):
    to_chatgpt = False
    w_chatgpt = False
    mute = True
    last_text = ''

    def __init__(self, speaker: Speaker, speech_to_text: SpeechToText, chatgpt: ChatGPT, nltk_use: NLTKUse) -> None:
        self.speaker = speaker
        self.speech_to_text = speech_to_text
        self.chatgpt = chatgpt
        self.nltk_use = nltk_use
        self.speech_to_text.listen(self.out)

    def command(self, cmd: str):
        response = self.nltk_use.text(cmd)
        if response == 'chatgpt':
            self.to_chatgpt = True
            return

        if self.to_chatgpt and not self.w_chatgpt:
            self.speaker.say(f'enviar texto ao chatgpt:{cmd}')
            self.last_text = cmd
            self.w_chatgpt = True

        if self.to_chatgpt and self.w_chatgpt and response == 'sim':
            text = self.chatgpt.chat(self.last_text, "davinci")
            self.speaker.say(text)
            self.to_chatgpt = False
            self.w_chatgpt = False
        elif self.to_chatgpt and response == 'nao':
            self.to_chatgpt = False
            self.w_chatgpt = False

    def list_devices(self):
        print('Speaker Devices')
        self.speaker.list_voice()

        print('SpeechToText Devices')
        self.speech_to_text.get_device_list()

    def out(self, txt: Dict):
        print(f'Você disse: {txt["text"]}')
        # self.speaker.say(f'Você disse: {txt["text"]}')
        self.command(txt["text"])
