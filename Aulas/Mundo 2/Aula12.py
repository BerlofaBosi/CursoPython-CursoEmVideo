nome = str(input('Qual é o seu nome? '))

if nome == 'Arthur':
    print('Que nome bonito!')

elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')

elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Que belo nome feminino')

else:
    print('Que nome comum')

print(f'Tenha um bom dia, {nome}!')
