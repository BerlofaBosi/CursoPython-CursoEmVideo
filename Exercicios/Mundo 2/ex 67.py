#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
#O programa será interrompido quando o número solicitado for negativo.

while True:
    print('----'*20)
    num_base = int(input('Insira um número para mostrar a tabuada: (negativo para parar) '))
    if num_base < 0:
        break
    
    for c in range(1, 11):
        print(f'{c} X {num_base} = {c * num_base}')
    
print('Encerrando o programa...')
