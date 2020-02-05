# -*- coding: utf-8 -*-
# Arquivo que vai exibir o texto inicial ao inicialiar o jogo

from utils import clear
from utils import texto
from capa import capa
from asciimatics.screen import Screen
import time

from menu import menu

def start():
    clear()
    texto('Snakeway é um jogo de com elemetos de RPG feito para ser jogado em linha de comando :)', 2)
    clear()
    ponto1 = '.'
    ponto2 = '..'
    ponto3 = '...'
    for i in range(1):
        texto('Vamos começar '+ ponto1, 1)
        clear()
        texto('Vamos começar '+ ponto2, 1)
        clear()
        texto('Vamos começar '+ ponto3, 1)
        clear()
    # Screen.wrapper(capa)
    # clear()
start()
menu()