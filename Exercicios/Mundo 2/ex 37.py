#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# -1 para binário
# -2 para octal
# -3 para hexadecimal

number = int(input('Insira o valor inteiro a ser convertido: '))

print('''
1 para binário
2 para octal
3 para hexadecimal
''')

type = int(input('Insira o tipo:'))

if type == 1:
    print(f'O valor inserido em binário será: {number:b}.')

elif type == 2:
    print(f'O valor inserido em octal será: {number:o}.')

elif type == 3:
    print(f'O valor inserido em hexadecimal será: {number:X}.')

else:
    print('Tipo não reconhecido.')

