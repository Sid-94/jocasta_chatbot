import os

import speech_recognition as sr
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from gtts import gTTS
from playsound import playsound


def ouvir_microfone():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print('Microfone...')
        audio = microfone.listen(source)
    try:
        frase = microfone.recognize_google(audio, language='pt-PT')
        print('Usuário: ' + frase)
    except sr.UnknownValueError:
        print('Jocasta: Não consegui te ouvir, poderia repetir?')
    return frase


def cria_audio(audio):
    tts = gTTS(audio, lang='pt-PT')
    tts.save('jocasta.mp3')
    playsound('jocasta.mp3')
    os.remove('jocasta.mp3')


bot = ChatBot('Jocasta')

conversa = ['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo', 'Como está?', 'Estou bem, e você?', 'Também estou.', 'Que ótimo!', 'Quem é você?', 'Eu sou Jocasta, sua Inteligência Artificial.', 'Eu sou', 'Olá!', 'Meu nome é',
            'Como posso ajudar?', 'O que você gosta de fazer?', 'Eu não tenho sentimentos como gostar, ou desgostar, o mais próximo que chego a isso é estar aqui respondendo suas perguntas.', 'Adeus', 'Tchau', 'Tchau', ]

trainer = ListTrainer(bot)
trainer.train(conversa)

while True:
    quest = ouvir_microfone()
    resposta = bot.get_response(quest)
    cria_audio(str(resposta))
    print('Jocasta: ', resposta)
