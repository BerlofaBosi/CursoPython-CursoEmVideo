#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

user_input = int( input ( 'Insira um número inteiro: ' ) )

print(f'TABUADA DO NÚMERO {user_input}')

for c in range(0, 11):
    print(f'{c} x {user_input} = {c * user_input}')

