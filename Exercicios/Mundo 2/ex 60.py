#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input('Insira um número: ').strip())
c = num
fatorial = 1

print(f'Calculando seu fatorial: {num}! = ', end='')
while c > 0:
    print(c, end='')
    fatorial *= c
    c -= 1
    if c != 0:
        print(' X ', end='')
    
print(' =', fatorial)
