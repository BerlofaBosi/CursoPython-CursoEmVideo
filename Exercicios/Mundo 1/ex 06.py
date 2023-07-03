#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

from math import sqrt

user_input = int(input('Insira um valor inteiro: '))

double = user_input * 2
triple = user_input * 3
square_root = sqrt(user_input)

print(f'O dobro do número {user_input} é: {double}, já seu triplo é: {triple}, e por fim sua raiz quadrada é {square_root:.2f}.')
