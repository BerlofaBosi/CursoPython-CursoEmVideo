#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

lista = []
continuar = True

while continuar == True:
    lista.append(int(input('Digite um número: ')))
    if input('Quer continuar? [S/N] ') in 'Nn':
        continuar = False

lista.sort()

print(f'Você digitou {len(lista)} números e a média foi {sum(lista) / len(lista)}.')
print(f'O maior valor digitado foi {lista[len(lista) - 1]} e o menor foi {lista[0]}.')
