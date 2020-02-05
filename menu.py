# -*- coding: utf-8 -*-

from utils import clear, texto
from cidades.cidades import cidade_01, cidade_02, cidade_03, cidade_04, cidade_05, cidade_06
import time
import random

def main_menu():

    nome = raw_input(str("Informe seu NickName: "))
    classe = raw_input(str("Informe sua classe: "))

    if nome != '':
        clear()
        bemvindo = ('Bem-vindo ao jogo, ' + nome)
        texto(bemvindo, 1)

        dado()
    else:
        texto(('Seu nome não pode ser vazio !').decode('utf-8'))
        clear()
        main_menu()

def dado():
    rodar_dado = raw_input(str("Clique ENTER para rodar o dado: "))

    if (rodar_dado == '' or rodar_dado != ''):
        for i in range(0, 1):
            resultado = random.randint(1, 6)
            clear()
            bar = ' ===== '
            texto(bar + str(resultado) + bar)
            if resultado == 1:
                return cidade_01()
            elif resultado == 2:
                return cidade_02()
            elif resultado == 3:
                return cidade_03()
            elif resultado == 4:
                return cidade_04()
            elif resultado == 5:
                return cidade_05()
            elif resultado == 6:
                return cidade_06()
            else:
                texto('UPDATE SEM WHERE !')
