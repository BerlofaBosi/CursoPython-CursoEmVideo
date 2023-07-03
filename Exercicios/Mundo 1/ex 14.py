#Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF

celsius = int(input('Insira a temperatura em ºC: '))

fahrenheit = (celsius * 9/5) + 32 

print(f'A temperatura de {celsius}ºC --> {fahrenheit:.1f}ºF.')
