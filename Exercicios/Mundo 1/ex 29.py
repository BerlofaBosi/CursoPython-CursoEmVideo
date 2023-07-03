#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.

user = int(input('Insira a velocidade do seu carro em Km/h: '))

if user > 80:
    multa = float((user - 80) * 7.00)

    print(f'Você foi multado. O valor a ser pago será de R${multa:.2f}')

else:
    print('Você está dentro do limite de velocidade de 80Km/h. Continue assim!')

