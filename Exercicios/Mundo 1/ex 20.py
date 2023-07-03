#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. 
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import sample

names = []

for c in range(1,5):
    name = input(f'Insira o nome do aluno {c}: ')
    names.append(name)

names = sample(names, k=len(names))

print('A ordem de apresentação ficou:')
print(*names, sep='\n')
