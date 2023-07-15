#Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint

itens = ['Pedra', 'Papel', 'Tesoura']

print('''
1 - Pedra
2 - Papel
3 - Tesoura
''')

computer = randint(1, 3)
user = int(input('Insira a sua jogada: '))

print(f'''
Jogada do computador: {itens[computer - 1]}
Sua jogada: {itens[user - 1]}
''')

if user == computer:
    print('EMPATE \n')

elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
    print('VOCÊ GANHOU! \n')

else: 
    print('VOCÊ PERDEU. \n')

