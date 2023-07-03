#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
#Ex: Digite um número: 6.127
#    O número 6.127 tem a parte inteira 6.

user_input = float(input('Insira um número Real qualquer: '))

inter = user_input // 1

print(f'A parte inteira do número {user_input} é de {inter:.0f}.')
