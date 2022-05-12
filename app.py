import os
from datetime import datetime

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome}, meu nome é Jocasta, sou a assistente virtual que irá auxiliar e guiar a sua visita ao nosso estabelecimento.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}, atualmente estamos em fase de testes/construção, o que torna esta definição um tanto quanto difícil de ser dada. Vale dizer que este sítio, atualmente, pode ser o que precisar que seja, como a "sala precisa" de Harry Potter.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}, fui criada para ser uma assistente virtual para apresentação de eventos, dando informações a respeito do que estiver apresentando ou guiando visitas a sítios específicos onde estiver sendo utilizada.{os.linesep}')
    elif resposta == '4':
      now = datetime.now()
      print(f"Agora são {now.hour} horas e {now.minute} minutos.")
    elif resposta == '5':
        print(f'{os.linesep}{nome}, muito obrigado por ter utilizado os meus serviços, fui criada para isto. Volte sempre que precisar.{os.linesep}')
        quit(resposta)
    else:
        print(f'Desculpe {nome}, mas não entendi. Digite apenas 1, 2, 3, 4 ou 5 por favor.')


def start():
    # Apresentar o chatbox
    print('Olá, seja bem vindo! Qual é o seu nome?')
    # pedir o nome
    nome = input('')
    while True:
        # Oferecer o menu de opções
        resposta = input(
            f'Como poderia lhe ajudar hoje, {nome}?{os.linesep}[1] - Quem é você?{os.linesep}[2] - Que sítio é este?{os.linesep}[3] - Conte-me a sua história{os.linesep}[4] - Que horas são?{os.linesep}[5] - Nada.{os.linesep}')
        # processar a resposta enviada
        processar_resposta(resposta, nome)


def quit(resposta):
    if resposta == '5':
        exit()


if __name__ == '__main__':
    start()
