#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

names = []

for c in range (1,5):
    name = input(f'Insira o nome do aluno {c}: ')
    names.append(name)

print(f'O aluno escolhido foi: {choice(names)}.')
