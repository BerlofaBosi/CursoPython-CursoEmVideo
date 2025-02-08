#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. 
#No final, mostre:
#   A) qual é o total gasto na compra.
#   B) quantos produtos custam mais de R$1000.
#   C) qual é o nome do produto mais barato.

cont = bigprice = thousand = 0
bigger = ''

while True:
    name = str(input('Insira o nome do produto: ').strip().capitalize())
    price = float(input('Insira o preço do produto: ').strip())

    cont += price

    if price > bigprice:
        bigprice = price
        bigger = name

    if price > 1000:
        thousand += 1

    if str(input('Continuar? [S/N] ').strip()) in 'Nn':
        break
    
print('----'*20)
print(f'O total gasto na compra foi de R${cont:.2f}')
print(f'Ao todo, foram constatados {thousand} produtos acima dos R$1000,00')
print(f'O produto mais caro é: {bigger} e custa R${bigprice:.2f}')
print('----'*20)
