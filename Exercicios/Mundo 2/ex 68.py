#Faça um programa que jogue par ou ímpar com o computador. 
#O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

contador = 0

while True:
    print('----' * 20)
    computador = randint(0, 10)
    usuario_num = int(input('Diga um valor: '))
    usuario = str(input('Par ou Ímpar? [P/I] ')).strip()

    soma = computador + usuario_num
    if soma % 2 == 0:
        parimpar = 'PAR'
    else:
        parimpar = 'ÍMPAR'

    print()
    print(f'Você jogou {usuario_num} e o computador {computador}. Total de {usuario_num + computador} é {parimpar}')

    if (usuario in 'Pp' and parimpar == 'PAR') or (usuario in 'Ii' and parimpar == 'ÍMPAR'):
        print('----' * 20)
        print('Você Venceu! Vamos denovo...')
        contador += 1
    else:
        break

print('----' * 20)
print(f'GAME OVER! Você perdeu após {contador} vítorias!')
