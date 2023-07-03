#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

list = []

for i in range(1, 4):
    user = int(input(f'Insira o {i}º número: '))

    list.append(user)

list.sort()

print(f'O MAIOR número é {list[2]}.')
print(f'O MENOR número é {list[0]}')
print('E a ordem é:', ' < '.join(map(str, list)))
