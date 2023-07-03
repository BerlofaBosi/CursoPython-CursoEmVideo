#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "santo".

city_name = str(input('Insira o nome da cidade: ')).lower().strip().split()

print(f'A cidade começa com santo? {city_name[0] == "santo"}')
#print(f'A cidade começa com santo? {"santo" in city_name[0]}')
