import time

import pygame, time
#Criando uma variável lista para guardar o endereço da música a ser carregada
#O comando append(acrescentar) é para inserir dados na variável que no caso é lista_musicas
lista_musicas = list()
lista_musicas.append('C:\\Users\\DELL\\Desktop\\meus_projetos\\projeto_player_music\\player_music_edu\\musicas_mp3\\metallica\\AudioCutter_Metalica - Sad But True.mp3')
lista_musicas.append('C:\\Users\\DELL\\Desktop\\meus_projetos\\projeto_player_music\\player_music_edu\\musicas_mp3\\metallica\\Metalica_-_The Unforgiven.mp3')

#iniciando a biblioteca pygame com o comando init()
pygame.init()
#lendo o arquivo da música através do comando load() especificando o caminho na pasta
pygame.mixer.music.load(lista_musicas[0])
#colocando a música para tocar através do comando play
pygame.mixer.music.play()
#Colocando para esperar por 10 segundos. sleep(adormecer) a música tocará por 10 segundos.
time.sleep(10)

#Após 10 segundos troca para a faixa de baixo
print(lista_musicas)
pygame.init()
pygame.mixer.music.load(lista_musicas[1])
pygame.mixer.music.play()
time.sleep(10)