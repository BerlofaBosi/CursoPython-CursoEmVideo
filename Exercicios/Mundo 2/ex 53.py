#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

phrase = str(input('Digite uma frase: ')).strip().lower().split()
phrase = ''.join(phrase)
inverted = ''

for letter in range(len(phrase)-1, -1, -1):
    inverted += phrase[letter]

print(phrase)
print(inverted)

if phrase == inverted:
    print('A frase é um palíndromo.')

else:
    print('Essa frase não é um palíndromo.')
