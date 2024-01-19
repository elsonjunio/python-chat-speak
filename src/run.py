from ext_interfaces.nltk.nltk_use import NLTKUse
from process import Process
from ext_interfaces.speaker.speaker import Speaker
from ext_interfaces.s2t.speech_to_text import SpeechToText
from config import OPENAI_API_KEY
from ext_interfaces.chatgpt.chatgpt import ChatGPT


chatgpt = ChatGPT(OPENAI_API_KEY)
speaker = Speaker()
speaker.engine.setProperty('voice', 'brazil')
speaker.engine.setProperty('rate', 125)

speech_to_text = SpeechToText(model="medium")
nltk_use = NLTKUse("cmd.pickle")

if __name__ == "__main__":
    p = Process(speaker, speech_to_text, chatgpt, nltk_use)
