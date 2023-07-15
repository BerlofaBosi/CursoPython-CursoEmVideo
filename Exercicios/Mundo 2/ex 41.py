#A Confederaçao Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# -Até 9 anos: MIRIM
# -Até 14 anos: INFANTIL
# -Até 19 anos: JUNIOR
# -Até 20 anos: SÊNIOR
# -Acima: MASTER

from datetime import date

user_year = int(input('Insira o ano em que você nasceu: '))
current_year = int(str(date.today())[:4])

age = current_year - user_year

if age <= 9:
    category = 'MIRIM'

elif age <= 14:
    category = 'INFANTIL'

elif age <= 19:
    category = 'JUNIOR'

elif age <= 20:
    category = 'SÊNIOR'

else:
    category = 'MASTER'

print(f'A sua categoria, de acordo com a sua idade é: {category}.')
