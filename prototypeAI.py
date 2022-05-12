from datetime import datetime

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

now = datetime.now()
bot = ChatBot('Jocasta')
trainer = ListTrainer(bot)


conversa = ['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo', 'Como está?', 'Estou bem, e você?', 'Também estou.', 'Que ótimo!', 'Quem é você?',
            'Eu sou Jocasta, sua Inteligência Artificial.', 'O que você gosta de fazer?', 'Eu não tenho sentimentos como gostar, ou desgostar, o mais próximo que chego a isso é estar aqui respondendo suas perguntas.', 'Adeus', 'Tchau', 'Tchau']

trainer.train(conversa)

while True:
    pergunta = input("Usuário: ")
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('Jocasta: ', resposta)
    else:
        print('Jocasta: Ainda não sei responder esta pergunta.')
