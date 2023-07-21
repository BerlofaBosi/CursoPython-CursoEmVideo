#Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética ( PA ). No final, mostre os 10 primeiros termos dessa progressão.

term = int(input('Insira o primeiro termo da PA: '))
ratio = int(input('Insira a razão da PA: '))

for c in range(term, term + 10 * ratio, ratio):
    print(c, end=' -> ')

print('FIM')
