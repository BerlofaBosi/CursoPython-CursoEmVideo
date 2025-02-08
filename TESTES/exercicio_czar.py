contador = 1
lista = []

while contador <= 20:
    entrada = float(input(f'Insira o {contador}º número: '))
    lista.append(entrada)
    contador += 1

print(f'O maior número digitado foi: {max(lista)}')
