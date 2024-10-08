import pygame
#Importando da biblioteca pygame
pygame.mixer.init()
#iniciando o programa pygame
pygame.mixer.music.load(r"C:\Users\Diiego\OneDrive\Documentos\Bossa_Sonsa_Quincas Moreira.mp3")
#carregando a musica do endereço em que esta localizado
pygame.mixer.music.play()
#iniciando a musica
while pygame.mixer.music.get_busy():
    pass
#enquanto a musica estiver tocando, o programa não vai fechar