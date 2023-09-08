#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

term = int(input('Insira o primeiro termo da PA: '))
ratio = int(input('Insira a razao da PA: '))

c = 0
limit = 10
next = 0

while True:
    while c < limit:
        print(term, end=' -> ')
        term += ratio
        c +=1
    print('PAUSA')
    next = int(input('Quantos termos a mais você quer? '))
    if next == 0:
        break
    limit += next

print(f'Progressão finalizada com {limit} termos exibidos. \n')
