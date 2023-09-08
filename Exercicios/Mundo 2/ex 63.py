#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

terms = int(input('Quantos termos você quer mostrar? '))

c = 0
t1 = 0
t2 = 1
t3 = t1 + t2

print(f'{t1} -> {t2} -> ', end='')
while c < 10:
    print(t3, end=' -> ')
    t1 = t2
    t2 = t3
    t3 = t1 + t2
    c += 1

print('FIM')
