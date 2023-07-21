#Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint

while True:

    itens = ['Pedra', 'Papel', 'Tesoura']

    print('''
Pedra
Papel
Tesoura
    ''')

    computer = itens[randint(0, 2)]
    user = str(input('\033[37;40mInsira a sua jogada: ')).strip().capitalize()

    if user not in itens:
        print('\033[1;33;40m\nInput não reconhecido, tente novamente.\033[m\n')

    else:

        print(f'''\033[m
Jogada do computador: \033[1;35m{computer}\033[m
Sua jogada: \033[1;36m{user}\033[m
''')


        if user == computer:
            print('\033[1;37mEMPATE\033[m\n')

        elif (user == 'Pedra' and computer == 'Tesoura') or (user == 'Papel' and computer == 'Pedra') or (user == 'Tesoura' and computer == 'Papel'):
            print('\033[1;32mVOCÊ GANHOU! \033[m\n')

        else: 
            print('\033[1;31mVOCÊ PERDEU. \033[m\n')

