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
    (3.5, 'More times than you can digest'),
    (7.5, 'Music every time I hear your name, oh'),
    (12.5, "Your head's layin' right on my chest"),
    (16.5, "Sun's up, but I still ain't got no rest"),
    (20.5, "Don't wanna close my eyes, I'm scared I'll miss too much"),
    (26.5, "Don't wanna fall asleep, I'd rather fall in love"),
    (31.5, "When I can't feel you, I feel out of touch"),
    (35.5, "Two seconds without you's like two months")
]

inicio = time.time()

for i in range(len(letra)):
    tempo, linha = letra[i]

    if i < len(letra) - 1:
        proximo_tempo = letra[i + 1][0]
    else:
        proximo_tempo = tempo + 4

    while time.time() - inicio < tempo:
        time.sleep(0.005)

    os.system('cls')

    texto = linha

    duracao = proximo_tempo - tempo
    delay_por_letra = (duracao / len(texto)) * 1.0

    for letra_char in texto:
        print(Fore.CYAN + letra_char, end="", flush=True)
        time.sleep(delay_por_letra)

    print(Style.RESET_ALL)

while pygame.mixer.music.get_busy():
    time.sleep(1)

