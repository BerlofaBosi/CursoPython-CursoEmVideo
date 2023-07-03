#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

user_input = float( input( 'Insira o preço do produto: ' ) )

new_price = user_input - (user_input * 0.05)

print(f'O novo preço do produto com desconto de 5% é de R${new_price:.2f}')
