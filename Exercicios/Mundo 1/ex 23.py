#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Ex: Digite um número: 1834
#    Unidade: 4 Dezena: 3 Centena: 8 Milhar: 1

number = int(input('Insira um número de 0 a 9999: '))

print(f'Milhar: {number // 1000 % 10}')
print(f'Centena: {number // 100 % 10}')
print(f'Dezena: {number // 10 % 10}')
print(f'Unidade: {number // 1 % 10}')
