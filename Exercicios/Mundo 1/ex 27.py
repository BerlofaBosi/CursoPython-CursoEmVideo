#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Ex: Ana Maria de Souza
#primeiro = Ana
#último = Souza

name = str(input('Insira o seu nome: ')).strip().title().split()

first_name = name[0]
last_name = name[len(name)-1]

print('Primeiro nome:', first_name)
print('Último nome:', last_name)
