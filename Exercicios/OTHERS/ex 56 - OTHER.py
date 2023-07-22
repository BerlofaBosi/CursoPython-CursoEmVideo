#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
#No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

#namesdict = {   'Arthur': {'Idade': 17, 'Sexo': 'M'},          #Dicionario padrão para testes
#                'Cesar': {'Idade': 14, 'Sexo': 'M'},
#                'Alexandre': {'Idade': 53, 'Sexo': 'M'}, 
#                'Cintia': {'Idade': 19, 'Sexo': 'F'}    }

namesdict = {}
nameslist = []

def average():                  #Função que retorna a média de idades
    idade = 0

    for avg in range(0, len(nameslist)):
        idade += namesdict[nameslist[avg]]['Idade']

    return idade / 4

def olderMan( _in = 0 ):        #Função que retorna por padrão a idade. 
    older_name = ''
    older = 0
    
    for c in range(0, len(nameslist)):
        age = namesdict[nameslist[c]]['Idade']
        gender = namesdict[nameslist[c]]['Sexo']
        if c == 1 and gender != 'F':
            older_name = nameslist[c]
            older = age
        if age > older and gender != 'F':
            older_name = nameslist[c]
            older = age

    if _in == 0:                #Retorna a idade
        return older
    elif _in == 1:              #Retorna o nome
        return older_name

def womansUnder20():            #Função que retorna a contagem de mulheres abaixo dos 20 anos
    count = 0

    for c in range(0, len(nameslist)):
        age = namesdict[nameslist[c]]['Idade']
        gender = namesdict[nameslist[c]]['Sexo']

        if age < 20 and gender != 'M':
            count += 1
        
    return count


for c in range(1, 5):
    print(f'---- {c}ª PESSOA ----')
    name = str(input('Nome: ')).strip().title()
    age = int(input('Idade: '))
    gender = str(input('Sexo [M/F]: ')).strip().upper()

    nameslist.append(name)

    namesdict[name] = {}
    namesdict[name]['Idade'] = age
    namesdict[name]['Sexo'] = gender

print('----'*20)
print(f'A média de idade do grupo é de: {average()}')
print(f'O homem mais velho do grupo tem {olderMan(0)} anos e se chama {olderMan(1)}.')
print(f'Ao todo são {womansUnder20()} mulheres com menos de 20 anos.')
print('----'*20)
