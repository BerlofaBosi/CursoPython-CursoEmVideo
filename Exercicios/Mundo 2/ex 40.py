#Crie um pograma que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO

grade1 = float(input('Insira a sua primeira nota: '))
grade2 = float(input('Insira a sua segunda nota: '))

average = (grade1 + grade2) / 2

print(f'Sua média foi de {average:.2f}')

if average < 5.0:
    print('REPROVADO')

elif average < 7.0:
    print('RECUPERAÇÃO')

elif average >= 7.0:
    print('APROVADO')

