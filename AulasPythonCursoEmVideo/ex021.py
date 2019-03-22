# Faça um programa que abra e reproduza um arquivo mp3

import pygame

pygame.mixer.init()
pygame.mixer.music.load('redrose.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait

# Por algum motivo de incompatibilidade com o sistema, foi necessário usar o input após o .play
# Há uma maneira mais fácil de executar o som, usando o modulo playsound

