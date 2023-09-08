#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Insira o seu sexo: [M/F] ')).strip().upper()

while sexo not in 'MF':
    sexo = str(input('Dado inválido. Insira o seu sexo: [M/F] ')).strip().upper()

print(f'Sexo {sexo} registrado com sucesso!')
