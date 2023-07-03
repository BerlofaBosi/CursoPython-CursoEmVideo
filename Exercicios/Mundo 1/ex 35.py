#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

reta1 = float(input('Insira o valor da primeira reta: '))
reta2 = float(input('Insira o valor da segunda reta: '))
reta3 = float(input('Insira o valor da terceira reta: '))

if (reta1 < reta2 + reta3) and (reta2 < reta1 + reta3) and (reta3 < reta1 + reta2):
    print('Com essas três retas da para formar um triângulo!')

else:
    print('Com essas três retas não da para formar um triângulo.')
