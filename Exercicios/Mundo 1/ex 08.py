#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

user_input = float(input('Insira o valor a ser convertido em metros: '))

cm = user_input * 100
mm = cm * 10

print(f'{user_input:.2f}m --> {cm:.2f}cm --> {mm:.2f}mm.')
