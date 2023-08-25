'''
Lista de música com menu de várias bandas dessenvolvido na linguagem Python
'''

#importando a biblioteca pygame para tocar a múica que se seseja ouvir.
import pygame

#laço de repetição para continuar o programa rodando

for i in range(10):

    print(50*'~');
    #escrevendo a lista de menu na tela
    print('Lista das bandas para tocar: \n'
          '1 - Metallica \n'
          '2 - Scorpions \n'
          '3 - Whitesnake \n');
    print(60*'~');
    #menu da banda para ser tocada
    menu_banda = int(input('N° da Banda: '));
    print(60*'~')
    match menu_banda:
        case 1:
            print('Banda escolhida: Metallica');
            #menu da música para ser tocada
            print('Lista de músicas da banda Metallica')
            print(60*'~');
            print('1 - Sad but true\n'
                  '2 - The unforginven \n'
                  '3 - Nothing else mathers');
            print(60*'~');
            menu_musica = int(input('N° da Música: '));
            match menu_musica:
                case 1:
                    print('Banda: Metallica Tocando -- Música: Sad but true');
                    #iniciando a biblioteca pygame
                    pygame.init()
                    #localizando o diretório da musica mp3
                    pygame.mixer.music.load('C:\\Users\DELL\Desktop\\meus_projetos\projeto_player_music\\player_music_edu\\musicas_mp3\\metallica\\AudioCutter_Metalica - Sad But True.mp3');
                    #Iniciando a música para tocar com o comando play
                    pygame.mixer.music.play()
                    print(60 * '~');
                    #digitando alo para a música parar
                    parar_musica = input('Digite algo para voltar para o menu: ');
                case 2:
                    print('Banda Metallica Tocando -- Música: The unforginven');
                    #iniciando a biblioteca pygame
                    pygame.init()
                    #localizando o diretório da música mp3
                    pygame.mixer.music.load('C:\\Users\\DELL\\Desktop\\meus_projetos\\projeto_player_music\\player_music_edu\\musicas_mp3\\metallica\\Metalica_-_The Unforgiven.mp3')
                    #Iniciando a música com o comando play
                    pygame.mixer.music.play()
                    print(60*'~');
                    #digite algo para parar a música
                    parar_musica = input('Digite algo para voltar para o menu: ');
                case 3:
                    print('Banda: Metallica Tocando -- Música: Nothing else mathers');
                    #iniciando a biblioteca pygame
                    pygame.init()
                    #localizando o diretório da música mp3
                    pygame.mixer.music.load('C:\\Users\\DELL\\Desktop\\meus_projetos\\projeto_player_music\\player_music_edu\\musicas_mp3\\metallica\\Nothing else mathers (2).mp3')
                    #comando play para iniciar a música
                    pygame.mixer.music.play()
                    print(60*'~');
                    #digitando qualquer valor para parar a música
                    parar_musica = input('Digite algo para voltar para o menu: ');
        case 2:
            print('Banda escolhida: Scorpions');
            print('Lista de músicas da banda Scorpions')
            print('1 - Always Somewhere \n'
                  '2 - Still Loving You');
            print(60*'~')
            #menu da lista de música da banda scorpions
            menu_musica = int(input('N° da Música: '));
            print(60*'~');
            #cai na condição da música escolhida
            match menu_musica:
                case 1:
                    print('Banda: Scorpions Tocando -- Música: Always Somewhere')
                    #Inicia a biblioteca pygame
                    pygame.init()
                    #Localiza o diretorio da música
                    pygame.mixer.music.load('C:\\Users\\DELL\\Desktop\\meus_projetos\\projeto_player_music\\player_music_edu\\musicas_mp3\\scorpions\\Scorpions - Always Somewhere.mp3')
                    #Iniciando a música com o camando play
                    pygame.mixer.music.play()
                    print(60*'~');
                    #Indo para o menu ao digitar qualquer valor
                    parar_musica = input('Digite algo para voltar para o menu: ');
                case 2:
                    print('Banda: Scorpions Tocando -- Música: Still Loving You');
                    #Iniciando a biblioteca pygame
                    pygame.init()
                    #Localizando o diretório onde está a música mp3
                    pygame.mixer.music.load('C:\\Users\\DELL\\Desktop\\meus_projetos\\projeto_player_music\\player_music_edu\\musicas_mp3\\scorpions\\Scorpions_-_Still_Loving_You_(Jesusful.com).mp3')
                    #Iniciando a música com o comando play da biblioteca pygame
                    pygame.mixer.music.play()
                    #Volta para o menu ao digitar qualquer valor
                    parar_musica = input('Digite algo para voltar para o menu: ');
        case 3:
            print('Banda escolhida: Whitesnake');
        case _:
            print('Digite um menu válido!!!!');

    print(60*'~');