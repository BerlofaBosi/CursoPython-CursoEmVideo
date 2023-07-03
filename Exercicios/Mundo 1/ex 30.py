#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

user = int(input('Insira um número inteiro e mostrarei se é PAR ou ÍMPAR: '))

if (user % 2) == 0:
    print(f'O número inserido {user} é PAR.')

else:
    print(f'O número inserido {user} é ÍMPAR')
