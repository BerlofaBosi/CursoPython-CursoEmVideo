#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# -À vista dinheiro/cheque: 10% de desconto
# -À vista no cartão: 5% de desconto
# -Em até 2x no cartão: preço normal
# -3x ou mais no cartão: 20% de juros

price = float(input('Insira o valor do produto: '))
print('''
1 - À vista dinheiro/cheque
2 - À vista no cartão
3 - Em até 2x no cartão
4 - 3x ou mais no cartão
''')
payment = int(input('Insira a forma de pagamento: '))

if payment == 1:
    price = price - (price * 0.10)

elif payment == 2:
    price = price - (price * 0.05)

elif payment == 4:
    price = price + (price * 0.20)

print(f'De acordo com a sua forma de pagamento, o valor final do produto será de R${price:.2f}')
