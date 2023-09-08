'''
Autor: Eduardo Machado
Programa: Mp3 player virtual
Data de Desenvolvimento: 31/08/2023
'''
#importando a biblioteca pygame e time
from pygame import mixer
from time import sleep
#importando a biblioteca  intertoolls para um looping infinito for
from itertools import cycle

#criando a variável dicionário em python para guardar a lista das músicas a ser tocadas
#vai guardar todas as músicas do seu endereço especificado no caminho
#obs essa \ é nesessária para ir para a outra linha
dicionario_musics =\
{
    1: 'C:\\Users\\DELL\\Desktop\\meus_projetos\\projeto_player_music\\player_music_edu\\musicas_mp3\\metallica\\AudioCutter_Metalica - Sad But True.mp3',
    2: 'C:\\Users\\DELL\\Desktop\\meus_projetos\\projeto_player_music\\player_music_edu\\musicas_mp3\\metallica\\Metalica_-_The Unforgiven.mp3',
    3: 'C:\\Users\\DELL\\Desktop\\meus_projetos\\projeto_player_music\\player_music_edu\\musicas_mp3\\metallica\\Nothing else mathers (2).mp3',
    4: 'C:\\Users\\DELL\\Desktop\\meus_projetos\\projeto_player_music\\player_music_edu\\musicas_mp3\\scorpions\\Scorpions - Always Somewhere.mp3',
    5: 'C:\\Users\\DELL\\Desktop\\meus_projetos\\projeto_player_music\\player_music_edu\\musicas_mp3\\scorpions\\Scorpions_-_Still_Loving_You_(Jesusful.com).mp3',
    6: 'C:\\Users\\DELL\\Desktop\\meus_projetos\\projeto_player_music\\player_music_edu\\musicas_mp3\\whitesnalke\\09 Here I Go Again (Starkers Live In Tokyo, Japan, 7-5-1997) [Remixed].mp3',
    7: 'C:\\Users\\DELL\\Desktop\\meus_projetos\\projeto_player_music\\player_music_edu\\musicas_mp3\\whitesnalke\\13 - Too Many Tears.mp3'
}

#cria-se um laço infinito usando o método cycle (ciclo) da biblioteca itertools
for i in cycle(range(1)):
    #apresenta a lista de música na tela para ser escolhida
    print(60* '~')
    print('-----Música Player Virtual-----\n'
          '-------Lista de música------s')
    print('1 - Banda: Metallica -  Música: Sad But True\n'
          '2 - Banda: Metallica -  Música: The Unforgiven\n'
          '3 - Banda: Metaliica -  Música: Nothin Else Matters\n'
          '4 - Banda: Scorpions - Música: Always Somewhere\n'
          '5 - Banda: Scorpions - Música: Still Loving You\n'
          '6 - Banda: Whitesnake - Música: Here I Go Again\n'
          '7 - Banda Whitesnake - Música: Too Many Tears')
    print(60*'~')
    # diz para escolher o número da música e inserir na variável menu_music
    menu_music = int(input('N° da música: '))
    #Criando a variável que vai pegar a música da lista acima para jogar no programa
    #obs: vai pegar a músuca atraves da chave que tem na lista ex: chave 1, chave 2 etc.
    #cada chave acessa algo na lista.
    pega_musicas = dicionario_musics[menu_music]

    #iniciando a biblioteca pygame usando o método mixer para a música
    mixer.init()
    #lendo a música pela função load e a variável pega música insere o valor do local do arquivo da música
    mixer.music.load(pega_musicas)
    #coloca a música para tocar
    mixer.music.play()
