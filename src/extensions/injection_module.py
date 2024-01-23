import inject
from config import (
    LLM_IMP,
    OPENAI_API_KEY,
    OPENAI_ENGINE,
    LLAMA_MODEL_PATH,
    LLAMA_N_CTX,
    LLAMA_MAX_TOKENS,
    WHISPER_MODEL,
    NLTK_FILE_PATH,
)
from core.llm import LLM
from core.nlp import NLP
from core.speach_to_text import SpeachToText
from core.text_to_speach import TextToSpeach
from ext_interfaces.chatgpt.chatgpt import ChatGPT
from ext_interfaces.llama.llama import LammaCpp
from ext_interfaces.nltk.nltk_use import NLTKUse
from ext_interfaces.s2t.whisper_imp import WhisperImp
from ext_interfaces.speaker.speaker import Speaker


def ioc_config(binder):

    if LLM_IMP.lower() == 'chatgpt':
        chatgpt = ChatGPT(OPENAI_API_KEY, OPENAI_ENGINE)
        binder.bind(LLM, chatgpt)
    else:
        lamma_cpp = LammaCpp(LLAMA_MODEL_PATH, LLAMA_N_CTX, LLAMA_MAX_TOKENS)
        binder.bind(LLM, lamma_cpp)

    speaker = Speaker()
    speaker.engine.setProperty('voice', 'brazil')
    speaker.engine.setProperty('rate', 125)
    binder.bind(TextToSpeach, speaker)

    speech_to_text = WhisperImp(model=WHISPER_MODEL)
    binder.bind(SpeachToText, speech_to_text)

    nltk_use = NLTKUse(NLTK_FILE_PATH)
    binder.bind(NLP, nltk_use)


def register_ioc():
    inject.configure(ioc_config)
