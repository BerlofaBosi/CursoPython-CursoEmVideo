#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

term = int(input('Insira o primeiro termo da PA: '))
ratio = int(input('Insira a razao da PA: '))

c = term

while c < term + 10 * ratio:
    print(c, end=' -> ')
    c += ratio

print('FIM')
