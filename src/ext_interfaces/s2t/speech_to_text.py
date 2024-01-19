from typing import Callable, Dict
import whisper
import speech_recognition as sr


class SpeechToText(object):
    def __init__(self, model_dir_download='./', model: str = 'small') -> None:
        """
        model -> tiny.en, tiny, base.en, base, small.en, small, medium.en, medium, large
        """

        self.model = whisper.load_model(
            model, download_root=model_dir_download)
        self.recognizer = sr.Recognizer()

    def listen(self, callback: Callable[[Dict], None], device_index=None):

        while (1):
            try:
                with sr.Microphone(device_index=device_index) as source2:
                    self.recognizer.adjust_for_ambient_noise(
                        source2, duration=0.2)
                    audio2 = self.recognizer.listen(source2)
                    text = self.recognizer.recognize_whisper(
                        audio2, show_dict=True)

                    callback(text)

            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))

            except sr.UnknownValueError:
                print("unknown error occurred")

    def get_device_list(self):
        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(
                index, name))
