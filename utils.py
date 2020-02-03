# -*- coding: utf-8 -*-
import os
import time
# Função para limpar a tela
def clear():
    os.system('cls' if os.name =='nt' else 'clear')    


def texto(texto, tempo):
    t = texto.decode('utf-8')
    #t = texto.encode('unicode')
    print('_____________________________________________________________________________________')
    print(t)
    print('_____________________________________________________________________________________')
    time.sleep(tempo)