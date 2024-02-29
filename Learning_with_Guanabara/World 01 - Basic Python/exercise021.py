# Tocando uma música mp3 no Python
import pygame
pygame.init() # Iniciando a biblioteca pygame
pygame.mixer.music.load('nome_arquivo_da_ música') # Carregando a música
pygame.mixer.music.play() # Tocando a música
pygame.event.wait() # Esperando a música finalizar