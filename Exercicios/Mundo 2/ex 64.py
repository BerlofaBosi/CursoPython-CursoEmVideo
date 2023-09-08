#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

usuario = soma = c = 0

while True:
    usuario = int(input('Insira um número inteiro: [999 p/ parar] '))
    if usuario == 999:
        break
    soma += usuario
    c += 1

print(f'Foram digitados {c} números e a soma entre eles é de {soma}')
