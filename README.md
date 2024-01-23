# python-chat-speak

Este repositório contém um código que integra diversas ferramentas para realizar o reconhecimento de voz (Whisper), geração de texto (Llama-cpp/ChatGPT) e leitura de textos (pyttsx3). Além disso, utiliza o NLTK para classificar textos e executar ações específicas no script.

## Objetivo

O principal propósito deste código é fornecer uma base para estudos e experimentações nas áreas de processamento de linguagem natural (NLP) e interação entre voz e texto. Este projeto não está finalizado e é destinado a ser aprimorado e adaptado conforme as necessidades específicas.

## Ferramentas Utilizadas

- Whisper (Reconhecimento de Voz): Integração de uma ferramenta de reconhecimento de voz para capturar entrada de áudio.
- ChatGPT (Geração de Texto): Utilização do modelo ChatGPT para gerar texto com base nas interações e consultas.
- LLAMA (Geração de Texto): Utilização do modelo llama-cpp para gerar texto com base nas interações e consultas. Referências: [llama-cpp](https://github.com/ggerganov/llama.cpp), [llama-cpp-python](https://python.langchain.com/docs/integrations/llms/llamacpp)
- pyttsx3 (Leitura de Texto): Implementação de um leitor de texto para proporcionar uma experiência auditiva.
- NLTK (Processamento de Linguagem Natural): Aplicação para classificação de textos e acionamento de ações específicas.


## Instalação
Python >= 3.7.

```bash
$ git clone https://github.com/elsonjunio/python-chat-speak.git
$ cd python-chat-speak
$ python -m venv venv
source venv/bin/activate 
pip install -r requirements.txt
```

Ubuntu
```bash
sudo apt install espeak
```

Manjaro
```bash
yay -S espeak
```

## Modelo para Llama-cpp

Para testes estou usando um modelo que pode ser obtido no [Hugging Face](https://huggingface.co/TheBloke).