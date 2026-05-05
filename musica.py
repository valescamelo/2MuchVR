from colorama import Fore, Style, init
init()
import pygame
import time
import shutil
import os

#Função centralizar texto

def centralizar(texto):
    largura = shutil.get_terminal_size().columns
    return texto.center(largura)

#Iniciando o player 

pygame.mixer.init()
pygame.mixer.music.load("2much.mp3")
pygame.mixer.music.play()

letra = [
    (0, 'Say, "I love you" under my breath'),
    (4, 'More times than you can digest'),
    (8, 'Music every time I hear your name, oh'),
    (13, "Your head's layin' right on my chest"),
    (17, "Sun's up, but I still ain't got no rest"),
    (21, "Don't wanna close my eyes, I'm scared I'll miss too much"),
    (27, "Don't wanna fall asleep, I'd rather fall in love"),
    (32, "When I can't feel you, I feel out of touch"),
    (36, "Two seconds without you's like two months")
]

inicio = time.time()

for tempo, linha in letra:
    while time.time() - inicio < tempo:
        time.sleep(0.1)

    os.system('cls')

    linha_centrada = centralizar(linha)
    
#Sincronizando letra..

    for letra_char in linha:
        print(Fore.CYAN + letra_char, end="", flush=True)
        time.sleep(0.08)
    print(Style.RESET_ALL)
    time.sleep(1)

#Aguardando a música terminar 

while pygame.mixer.music.get_busy():
    time.sleep(1)

