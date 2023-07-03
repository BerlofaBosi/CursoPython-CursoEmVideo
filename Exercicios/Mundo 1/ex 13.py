#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Insira o seu salário atual: '))

novo_salario = salario + (salario * 0.15)

print(f'O seu novo salário com o aumento de 15% será de R${novo_salario:.2f}')
