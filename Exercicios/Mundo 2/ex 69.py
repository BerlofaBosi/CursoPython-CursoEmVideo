#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
#No final, mostre:
#   A) quantas pessoas tem mais de 18 anos.
#   B) quantos homens foram cadastrados.
#   C) quantas mulheres tem menos de 20 anos.

pessoa = homens = mulheres = dezoito = 0

while True:
    print(f'---- {pessoa + 1}ª PESSOA ----')
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    pessoa += 1

    if idade > 18:
        dezoito += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade > 20:
        mulheres += 1

    print('----' * 5)
    if input('Continuar? [S/N] ').strip().upper() == 'N':
        break

print('----' * 20)
print(f'Tivemos {dezoito} pessoas cadastradas que tem mais de 18 anos.')
print(f'Foram cadastrados {homens} homens.')
print(f'E por fim foram cadastradas {mulheres} mulheres acima dos 20 anos.')
print('----' * 20)
