#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

phrase = str(input('Digite uma frase: ')).strip().lower().split()
phrase = ''.join(phrase)
inverted = phrase[::-1]

print(phrase)
print(inverted)

if phrase == inverted:
    print('A frase é um palíndromo.')

else:
    print('Essa frase não é um palíndromo.')
