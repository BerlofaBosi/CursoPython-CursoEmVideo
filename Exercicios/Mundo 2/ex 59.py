#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

x = int(input('Insira um primeiro valor: ').strip())
y = int(input('Insira um segundo valor: ').strip())

while True:
    print("""
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
""")
    c = int(input('>>>Sua resposta: ').strip())
    match c:
        case 1:
            print(f'A soma entre {x} e {y} é: {x+y}')
        case 2:
            print(f'A multiplicação entre {x} e {y} é: {x*y}')
        case 3:
            print(f'O maior entre {x} e {y} é: {max(x, y)}')
        case 4:
            x = int(input('Insira um primeiro valor: ').strip())
            y = int(input('Insira um segundo valor: ').strip())
        case 5:
            print('Encerrando o programa.')
            break
        case other:
            print('Resposta inválida.')
    print('='*25)