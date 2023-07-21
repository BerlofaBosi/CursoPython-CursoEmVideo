#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

def isprimo(num):
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 11 == 0:
        return False
    
    return True

user = int(input('Insira um número inteiro: '))

for c in range(1, user + 1):
    if user % c == 0:
        print('\033[34m', end='')
    else:
        print('\033[31m', end='')
    print(c, end=' ')

print(f'\033[m\nO número inserido é primo? {isprimo(user)}')
