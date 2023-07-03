#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

user_input1 = float(input('Insira a sua primeira nota: '))
user_input2 = float(input('Insira a sua segunda nota: '))

average = ( user_input1 + user_input2 ) / 2

print(f'A média das duas notas inseridas é de {average:.2f}')
