#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
#No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

avg = 0
older_name = ''
older_age = 0
woman_count = 0

for c in range(1, 5):
    print(f'---- {c}ª PESSOA ----')
    name = str(input('Nome: ')).title()
    age = int(input('Idade: '))
    gender = str(input('Sexo [M/F]: ')).strip().upper()

    avg += age

    if c == 1 and gender != 'F':
        older_name = name
        age = 0

    if age > older_age and gender != 'F':
        older_name = name
        older_age = age
    
    if age < 20 and gender != 'M':
        woman_count += 1

print(f'A média de idade do grupo é de: {avg/4}')
print(f'O homem mais velho do grupo tem {older_age} e se chama {older_name}.')
print(f'Ao todo são {woman_count} mulheres com menos de 20 anos.')

