#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# -Equilátero: todos os lados iguais
# -Isósceles: dois lados iguais
# -Escaleno: todos os lados diferentes

reta1 = float(input('Insira o valor da primeira reta: '))
reta2 = float(input('Insira o valor da segunda reta: '))
reta3 = float(input('Insira o valor da terceira reta: '))

def FormaTriangulo(in1, in2, in3):
    if (in1 < in2 + in3) and (in2 < in1 + in3) and (in3 < in1 + in2):
        return True
    
    return False
    
if FormaTriangulo(reta1, reta2, reta3):
    print('Com essas retas dá pra formar um triângulo!')

    if reta1 == reta2 == reta3:
        print('Esse triângulo é EQUILÁTERO, já todos os lados são iguais.')

    elif reta1 != reta2 != reta3:
        print('Esse triângulo é ESCALENO, já que todos os lados são diferentes.')

    else:
        print('Esse triângulo é ISÓSCELES, já que tem dois lados iguais.')

else:
    print('Com essas três retas não da para formar um triângulo.')
