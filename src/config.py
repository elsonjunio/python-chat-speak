import os
from dotenv import load_dotenv

load_dotenv()

LLM_IMP = os.getenv('LLM_IMP', '')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
OPENAI_ENGINE = os.getenv('OPENAI_ENGINE', "gpt-3.5-turbo")

LLAMA_MODEL_PATH = os.getenv('LLAMA_MODEL_PATH', '')
LLAMA_N_CTX = int(os.getenv('LLAMA_N_CTX', '512'))
LLAMA_MAX_TOKENS = int(os.getenv('LLAMA_MAX_TOKENS', '512'))

WHISPER_MODEL = os.getenv('WHISPER_MODEL', 'medium')
NLTK_FILE_PATH = os.getenv('NLTK_FILE_PATH', 'cmd.pickle')
