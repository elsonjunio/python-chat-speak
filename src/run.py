from nltk_use import NLTKUse
from process import Process
from speaker import Speaker
from speech_to_text import SpeechToText
from config import OPENAI_API_KEY
from chatgpt import ChatGPT


chatgpt = ChatGPT(OPENAI_API_KEY)
speaker = Speaker()
speech_to_text = SpeechToText(model='medium')
nltk_use = NLTKUse('cmd.pickle')

if __name__ == '__main__':
    p = Process(speaker, speech_to_text, chatgpt, nltk_use)
