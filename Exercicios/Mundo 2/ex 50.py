#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

sum = 0
counter = 0

for c in range(0, 6):
    user_input = int(input('Insira um número inteiro: '))
    if user_input % 2 == 0:
        sum += user_input
        counter += 1

print(f'A soma dos {counter} números pares inseridos é {sum}')
