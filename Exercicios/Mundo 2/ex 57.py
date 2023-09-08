#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexoCerto = False

while sexoCerto == False:
    sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()
    if sexo in 'MF':
        sexoCerto = True
        print(f'Sexo {sexo} registrado com sucesso.')
    else:
        print('Sexo não reconhecido, tente novamente.')
