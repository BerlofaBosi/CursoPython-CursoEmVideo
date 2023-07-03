#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

print('---'*20)

user_input = radians(int(input('Insira o ângulo: ')))

print(f'''
Seno de {user_input} --> {sin(user_input):.4f}
Cosseno de {user_input} --> {cos(user_input):.4f}
Tangente de {user_input} --> {tan(user_input):.4f}''')
print('---'*20)
