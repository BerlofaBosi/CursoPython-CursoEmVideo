#Crie um programa que simule o funcionamento de um caixa eletrônico. 
#No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. 
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('='*50)
print(f'\n{"BANCO BERLO":^50}\n')
print('='*50)

valorSacar = int(input('\nQue valor você quer sacar? R$'))

print(f'\n\n{"SACANDO...":^50}\n')

valorCedula = 50
quantidadeCedula = 0

while True:
    if valorSacar >= valorCedula:
        valorSacar -= valorCedula
        quantidadeCedula += 1
    else:
        if quantidadeCedula > 0:
            print(f'{quantidadeCedula} cédulas de R${valorCedula}')

        match valorCedula:
            case 50:
                valorCedula = 20
            case 20:
                valorCedula = 10
            case 10:
                valorCedula = 1
            
        if valorSacar == 0:
            print('\nObrigado por utilizar o Banco Berlo!')
            print('='*50)
            break
        
        quantidadeCedula = 0
