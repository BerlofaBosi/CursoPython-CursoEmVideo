#Crie um programa que leia o nome completo de uma pessoa e mostre:
#--> O nome com todas as letras maiúsculas e minúsculas.
#--> Quantas letras ao todo (sem considerar espaços).
#--> Quantas letras tem o primeiro nome.

name = input('Insira o seu nome completo: ').split()

CompleteName = (' ').join(name)
NameWithoutSpace = ('').join(name)

print(f'Seu nome em maiúsculo: {CompleteName.upper()}')
print(f'Seu nome em minúsculo: {CompleteName.lower()}')
print(f'Seu nome ao todo tem {len(NameWithoutSpace)} letras.')
print(f'Seu primeiro nome tem {len(name[0])} letras.')
