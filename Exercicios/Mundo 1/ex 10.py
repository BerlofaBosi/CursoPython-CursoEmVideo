#Crie um programa que leia quanto dinehrio uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#Considere US$1,00 -> R$3,27

user_input = float( input( 'Insira o quanto de Reais que você tem na carteira: ' ) )

dolar = user_input / 3.27

print('De acordo com o quanto de dinheiro que você tem:')
print(f'R${user_input:.2f} --> US${dolar:.2f}')
