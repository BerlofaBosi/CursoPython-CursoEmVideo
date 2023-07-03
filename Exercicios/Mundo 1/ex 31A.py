#Desenvolva um programa que pergunte a distância de uma viagem em Km. 
#Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

kilometers = int(input('Insira a distância em Km da sua viagem: '))

if kilometers <= 200:
    price = 0.5

elif kilometers > 200:
    price = 0.45

price = kilometers * price

print(f'O preço da sua viagem será de R${price:.2f}')
