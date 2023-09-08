#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

term = int(input('Insira o primeiro termo da PA: '))
ratio = int(input('Insira a razao da PA: '))

c = 0

while c < 10:
    print(term, end=' -> ')
    term += ratio
    c += 1

print('FIM')
