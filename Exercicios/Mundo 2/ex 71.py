#Crie um programa que simule o funcionamento de um caixa eletrônico. 
#No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. 
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('===================')
print('    BANCO BERLO    ')
print('===================')

sacar = float(input('Que valor você quer sacar? R$'))

cedula50 = cedula20 = cedula10 = cedula01= 0

while sacar != 0:
    if (sacar - 50) > 0:
        cedula50 += 1

    