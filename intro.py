# -*- coding: utf-8 -*-
# Arquivo que vai exibir o texto inicial ao inicialiar o jogo

from utils import clear, texto
import time

from menu import main_menu

def start():
    clear()
    texto('Snakeway - um jogo com elemetos de RPG feito para ser jogado em linha de comando :)')
    clear()
    t0 = 'Vamos iniciar'
    texto(t0, 0.4)
    for i in range(3):
        clear()
        t0 += '.'
        texto(t0, 0.5)

    # clear()
start()
main_menu()