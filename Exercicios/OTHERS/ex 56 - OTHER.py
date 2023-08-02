#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
#No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

#namesdict = {  0: {'Nome': 'Arthur', 'Idade': 17, 'Sexo': 'M'},          #Dicionario padrão para testes
#               1: {'Nome': 'Cesar', 'Idade': 14, 'Sexo': 'M'},
#               2: {'Nome': 'Alexandre', 'Idade': 53, 'Sexo': 'M'}, 
#               3: {'Nome': 'Cintia', 'Idade': 19, 'Sexo': 'F'}    }

namesdict = {}

def average():                  #Função que retorna a média de idades
    idade = 0

    for c in range(0, len(namesdict)):
        idade += namesdict[c]['Idade']

    return idade / len(namesdict)

def olderMan( _in = 0 ):        #Função que retorna por padrão a idade. 
    older_name = ''
    older = 0
    
    for c in range(0, len(namesdict)):
        age = namesdict[c]['Idade']
        gender = namesdict[c]['Sexo']
        if c == 1 and gender != 'F':
            older_name = namesdict[c]['Nome']
            older = age
        if age > older and gender != 'F':
            older_name = namesdict[c]['Nome']
            older = age

    if _in == 0:                #Retorna a idade
        return older
    elif _in == 1:              #Retorna o nome
        return older_name

def womansUnder20():            #Função que retorna a contagem de mulheres abaixo dos 20 anos
    count = 0

    for c in range(0, len(namesdict)):
        age = namesdict[c]['Idade']
        gender = namesdict[c]['Sexo']

        if age < 20 and gender != 'M':
            count += 1
        
    return count


for c in range(0, 4):
    print(f'---- {c + 1}ª PESSOA ----')
    name = str(input('Nome: ')).strip().title()
    age = int(input('Idade: '))
    gender = str(input('Sexo [M/F]: ')).strip().upper()

    namesdict[c] = {}
    namesdict[c]['Nome'] = name
    namesdict[c]['Idade'] = age
    namesdict[c]['Sexo'] = gender

print('----'*20)
print(f'A média de idade do grupo é de: {average()}')
print(f'O homem mais velho do grupo tem {olderMan(0)} anos e se chama {olderMan(1)}.')
print(f'Ao todo são {womansUnder20()} mulheres com menos de 20 anos.')
print('----'*20)