#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.

kilometragem = int(input('Insira a quantidade de Km percorridos: '))
dias = int(input('Insira quantos dias o carro permaneceu alugado: '))

preco = (kilometragem * 0.15) + (dias * 60.00)

print(f'O preço a ser pago pelo aluguel do carro será de R${preco:.2f}.')
