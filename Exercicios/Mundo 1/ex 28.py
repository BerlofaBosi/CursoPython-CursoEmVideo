#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

while True:
    user = int(input('Insira um número inteiro entre 0 e 5: '))

    if user == randint(0, 5):
        print('Parabéns, você acertou o número que o computador pensou.')
        break
    
    else:
        print('Não foi dessa vez, tente novamente.')
