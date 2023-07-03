#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

name = str(input('Insira o seu nome: ')).strip().lower()

print(f'Você tem Silva no nome? {"silva" in name}')
