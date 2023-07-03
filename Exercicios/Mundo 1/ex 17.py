#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

cateto_oposto = float(input('Insira o valor do cateto oposto: '))
cateto_adjacente = float(input('Insira o valor do cateto adjacente: '))

print(f'O valor da hypotenusa será de {hypot(cateto_oposto, cateto_adjacente):.2f}')
