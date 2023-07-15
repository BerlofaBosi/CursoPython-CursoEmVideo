#Faça um programa que leia o ano de um nascimento de um jovem e informe, de acordo com sua idade:
#-Se ele ainda vai se alistar ao serviço militar.
#-Se é a hora de se alistar.
#-Se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

user_year = int(input('Insira o ano em que você nasceu: '))
current_year = int(str(date.today())[:4]) #Pode-se utilizar também date.today().year

age = current_year - user_year

if age == 18:
    print('Você está no ano que completa 18 anos, ou seja, é a hora de se alistar.')

elif age < 18:
    print(f'Ainda faltam {18 - age} anos para se alistar.')
    print(f'Seu alistamento será em {current_year + (18 - age)}.')

elif age > 18: 
    print(f'Você passou {age - 18} anos do alistamento.')
    print(f'Seu alistamento foi em {current_year - (age - 18)}.')

