from colorama import Fore, Style, init
init()
import pygame
import time
import shutil
import os


#Iniciando o player 

pygame.mixer.init()
pygame.mixer.music.load("2much.mp3")
pygame.mixer.music.play()

letra = [
    (0, 'Say, "I love you" under my breath'),
    (4.0, 'More times than you can digest'),
    (8.0, 'Music every time I hear your name, oh'),
    (13.0, "Your head's layin' right on my chest"),
    (17.0, "Sun's up, but I still ain't got no rest"),
    (21.0, "Don't wanna close my eyes, I'm scared I'll miss too much"),
    (27.0, "Don't wanna fall asleep, I'd rather fall in love"),
    (32.0, "When I can't feel you, I feel out of touch"),
    (36.0, "Two seconds without you's like two months")
]


inicio = time.perf_counter()

for i in range(len(letra)):
    tempo, linha = letra[i]

    #anterior
    if i > 0:
        linha_anterior = letra[i - 1][1]
    else:
        linha_anterior = ""

    #próxima
    if i < len(letra) - 1:
        proxima_linha = letra[i + 1][1]
    else:
        proxima_linha = ""

    while time.perf_counter() - inicio < tempo:
        time.sleep(0.001)
                   

    os.system('cls')

    
    if linha_anterior:
        print(Fore.LIGHTBLACK_EX + linha_anterior + Style.RESET_ALL)
        print()

    print(Fore.CYAN + linha + Style.RESET_ALL)
    print()

    if proxima_linha:
        print(Fore.WHITE + proxima_linha + Style.RESET_ALL)
    
while pygame.mixer.music.get_busy():
    time.sleep(1)

