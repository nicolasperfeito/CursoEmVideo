#   Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
#   O arquivo .mp3 deve estar no mesmo diretório do programa
#   Pode precisar reiniciar o PC após instalação do módulo pygame
#   pygame.error: Failed loading libmpg123-0.dll: Não foi possível encontrar o módulo especificado.
import pygame
pygame.mixer.init()
pygame.mixer.music.load('teste.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass

