#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestaçao mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Insira o valor da casa em R$: '))
salario_comprador = float(input('Insira o valor do seu salário em R$: '))
anos_pagamento = int(input('Quantos anos deseja pagar o empréstimo? '))

parcela = valor_casa / (anos_pagamento * 12)

if parcela <= (salario_comprador * 0.30):
    print('Seu empréstimo foi aprovado!')
    print(f'O valor de cada parcela será de: R${parcela:.2f}')

else: 
    print(f'Seu empréstimo foi negado, ele excede o valor de 30% de seu salário em R${parcela - (salario_comprador * 0.3)}')

    