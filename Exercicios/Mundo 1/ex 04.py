#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

user_input = input('Digite algo: ')

print('O tipo primitivo é: ', type(user_input))
print('É alfabetico? ', user_input.isalpha())
print('É número? ', user_input.isnumeric())
print('É alphanumerico? ', user_input.isalnum())
print('É decimal? ', user_input.isdecimal())
print('É espaço? ', user_input.isspace())
print('Está em maiusculo? ', user_input.isupper())
print('Está em minusculo? ', user_input.islower())
