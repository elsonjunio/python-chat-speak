
import pyttsx3


class Speaker(object):
    def __init__(self):
        self.voices = {}
        self.engine = pyttsx3.init()
        self.refresh_voices()

    def refresh_voices(self):
        self.voices = {}
        for voice in self.engine.getProperty('voices'):
            self.voices.update({len(self.voices): voice})

    def list_voice(self):
        keys = self.voices.keys()
        for key in keys:
            print(f'key: {key} - {str(self.voices[key])}')

    def set_voice(self, key: int):
        self.engine.setProperty(
            'voice', str(self.voices[key]))

    def say(self, text: str):
        self.engine.say(text)
        self.engine.runAndWait()
