# -*- coding: utf-8 -*-
import os
import time

# Função para limpar a tela
def clear():
    os.system('cls' if os.name =='nt' else 'clear')    

# Função básica para exibir textos
def texto(texto, tempo=2):
    print('_____________________________________________________________________________________')
    print(texto)
    print('_____________________________________________________________________________________')
    time.sleep(tempo)

# Função básica para exibir textos de seleção de cidades
def texto_cidade(texto, tempo=2):
    t = texto.decode('utf-8')
    print(t)
    print('_____________________________________________________________________________________')
    time.sleep(tempo)
    clear()
