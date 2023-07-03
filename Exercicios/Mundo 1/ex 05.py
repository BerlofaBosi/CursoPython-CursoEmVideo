#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

def antecessor (in1):
    return in1 - 1

def sucessor (in1):
    return in1 + 1

user_input = int( input( 'Insira um número qualquer: ' ) )

print(f'De acordo com o número inserido {user_input}, seu antecessor é {antecessor(user_input)} e seu sucessor é {sucessor(user_input)}')
