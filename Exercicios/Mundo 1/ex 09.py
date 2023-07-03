#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

user_input = int( input ( 'Insira um número inteiro: ' ) )

print(f'TABUADA DO NÚMERO {user_input}')

for c in range(1,11):
    print(user_input * c)

