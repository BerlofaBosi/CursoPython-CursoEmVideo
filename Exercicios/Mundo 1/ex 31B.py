#Desenvolva um programa que pergunte a distância de uma viagem em Km. 
#Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

kilometers = int(input('Insira a distância em Km da sua viagem: '))

price = kilometers * 0.5 if kilometers <= 200 else kilometers * 0.45

print(f'O preço da sua viagem será de R${price:.2f}')
