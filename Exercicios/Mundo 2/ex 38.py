#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# -O primeiro valor é maior
# -O segundo valor é maior
# -Não existe valor maior, os dois são iguais.

number1 = int(input('Insira o primeiro valor: '))
number2 = int(input('Insira o segundo valor: '))

if number1 > number2:
    print('O primeiro valor é maior.')

elif number1 < number2:
    print('O segundo valor é maior.')

elif number1 == number2:
    print('Não existe valor maior, os dois são iguais.')

