import time

import pygame, time


lista_musicas = ['C:\\Users\\DELL\\Desktop\\meus_projetos\\projeto_player_music\\player_music_edu\\musicas_mp3\\metallica\\AudioCutter_Metalica - Sad But True.mp3']
lista_musicas = ['C:\\Users\\DELL\\Desktop\\meus_projetos\\projeto_player_music\\player_music_edu\\musicas_mp3\\metallica\\Metalica_-_The Unforgiven.mp3']

pygame.init()
pygame.mixer.music.load(lista_musicas[0])
pygame.mixer.music.play()

time.sleep(10)
print(lista_musicas[1]);
pygame.init()
pygame.mixer.music.load(lista_musicas[1])
pygame.mixer.music.play()