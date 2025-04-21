#Crie um programa que simule o funcionamento de um caixa eletrônico. 
#No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. 
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('='*50)
print(f'\n{"BANCO BERLO":^50}\n')
print('='*50)


valorSacar = int(input('\nQue valor você quer sacar? R$'))
print(f'\n\n{"SACANDO...":^50}\n')


cedula50 = valorSacar // 50 # Quantidade de cédulas de 50
valorSacar -= cedula50 * 50 # Atualiza o valor a ser sacado

cedula20 = valorSacar // 20 # Quantidade de cédulas de 20
valorSacar -= cedula20 * 20 # Atualiza o valor a ser sacado

cedula10 = valorSacar // 10 # Quantidade de cédulas de 10
valorSacar -= cedula10 * 10 # Atualiza o valor a ser sacado

cedula01 = valorSacar       # Quantidade de cédulas de 1


if cedula50 != 0: print(f'{cedula50} cédulas de R$50')
if cedula20 != 0: print(f'{cedula20} cédulas de R$20')
if cedula10 != 0: print(f'{cedula10} cédulas de R$10')
if cedula01 != 0: print(f'{cedula01} cédulas de R$1')

print('\nObrigado por utilizar o Banco Berlo!')
print('='*50)
