#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

contador = 1
computador = randint(0, 10)

print('-=-'*10)
chute = int(input('Insira um número de 0 a 10. ').strip())

while chute != computador:
    chute = int(input('Não foi dessa vez, insira novamente um número de 0 a 10. ').strip())
    contador += 1

print(f'Parabéns, você venceu em {contador} tentativas.')
print('-=-'*20)