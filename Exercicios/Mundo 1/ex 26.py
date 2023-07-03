#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A";
#Em que posição ela aparece a primeira vez;
#Em que posição ela aparece a última vez.

phrase = str(input('Insira uma frase: ')).strip().lower()

print('Quantas vezes aparece a letra "A": ', phrase.count('a'))
print('Em que posição ela aparece a primeira vez: ', phrase.find('a')+1)
print('Em que posição ela aparece a última vez: ', phrase.rfind('a')+1)
