#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
from time import sleep

print('---'*20)
pygame.init()
while True:
    music = ['DrillMtLouco.mp3', 'TellMe.mp3', 'TrapMelodiaSino.mp3']
    print(music)
    print('0, 1, 2')
    selected = int(input('Insert the number of the music: '))

    print(f'Currently playing: {music[selected]}')

   
    pygame.mixer.music.load(music[selected])
    pygame.mixer.music.play()
    input('Enter to stop the music.')
    pygame.mixer.music.stop()

    print('The music has been stoped.')
    print('---'*20)
