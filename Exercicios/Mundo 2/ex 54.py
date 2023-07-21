#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

current_year = date.today().year

bigger = []
smaller = []

for c in range(1, 8):
    user_year = int(input(f'Insira o ano de nascimento da {c}ª pessoa: '))
    if current_year - user_year < 18:
        smaller.append(user_year)
    
    else:
        bigger.append(user_year)

print(f'\nAo todo tivemos {len(bigger)} pessoas maiores de idade. Segue a lista delas: {bigger}')
print(f'E também tivemos {len(smaller)} pessoas menores de idade. Segue a lista delas: {smaller}')
