#Crie um programa que leia dois números e mostre a soma entre eles.
def soma (in1, in2):
    return in1 + in2

num1 = int(input('Insira o primeiro valor: '))
num2 = int(input('Insira o segundo valor: '))

print(f'A soma entre esses valores é {soma(num1, num2)}.')
