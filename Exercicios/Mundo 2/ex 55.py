#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

bigger = 0.0
smaller = 0.0

for c in range(1, 6):
    user = float(input(f'Insira o peso da {c}ª pessoa: '))
    if c == 1:
        bigger = user
        smaller = user

    if user > bigger:
        bigger = user
        
    if user < smaller:
        smaller = user
    
print(f'O maior peso encontrado foi de {bigger}Kg e o menor foi de {smaller}Kg.')
