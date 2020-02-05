# -*- coding: utf-8 -*-
import os
import time
# Função para limpar a tela
def clear():
    os.system('cls' if os.name =='nt' else 'clear')    


def texto(texto, tempo):
    t = texto.decode('utf-8')
    print('_____________________________________________________________________________________')
    print(t)
    print('_____________________________________________________________________________________')
    time.sleep(tempo)

def texto_cidade(texto):
    t = texto.decode('utf-8')
    print(t)
    print('_____________________________________________________________________________________')
