#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

user = int(input('Insira o ano a ser analisado: '))

if (user % 4) == 0 and (user % 100) != 0 or (user % 400) == 0:
    print(f'O ano {user} é um ano BISSEXTO.')

else:
    print(f'O ano {user} não é um ano BISSEXTO.')
