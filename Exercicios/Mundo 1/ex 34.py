#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

user = float(input('Insira o seu salário em reais: '))

if user > 1250.00:
    increase = 0.10

elif user <= 1250.00:
    increase = 0.15

print(f'O seu salário já com aumento de {increase:.2f}% será de R${user + user * increase:.2f}')
