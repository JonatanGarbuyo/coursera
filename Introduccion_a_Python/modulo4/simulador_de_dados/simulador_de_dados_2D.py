# -*- coding: utf-8 -*-
# Jonatan Garbuyo
# 09-2020


from random import random

# https://en.wikipedia.org/wiki/Box-drawing_character
mis_dados = {
    "1":   ["┏━━━━━━━┓",
            "┃       ┃",
            "┃   ♦   ┃",
            "┃       ┃",
            "┗━━━━━━━┛"],
    "2":   ["┏━━━━━━━┓",
            "┃ ♦     ┃",
            "┃       ┃",
            "┃     ♦ ┃",
            "┗━━━━━━━┛"],
    "3":  ["┏━━━━━━━┓",
           "┃ ♦     ┃",
           "┃   ♦   ┃",
           "┃     ♦ ┃",
           "┗━━━━━━━┛"],
    "4": ["┏━━━━━━━┓",
          "┃ ♦   ♦ ┃",
          "┃       ┃",
          "┃ ♦   ♦ ┃",
          "┗━━━━━━━┛"],
    "5": ["┏━━━━━━━┓",
          "┃ ♦   ♦ ┃",
          "┃   ♦   ┃",
          "┃ ♦   ♦ ┃",
          "┗━━━━━━━┛"],
    "6":  ["┏━━━━━━━┓",
           "┃ ♦   ♦ ┃",
           "┃ ♦   ♦ ┃",
           "┃ ♦   ♦ ┃",
           "┗━━━━━━━┛"]
}


def dibujar_dado(numero):
    """Imprime en pantalla el dibujo de un dado.
    Toma el diseño desde el diccionario mis_dados
    segun el numero pasado como argumento convertido a string.
    """
    for item in mis_dados[str(numero)]:
        print(item)


def obtener_valor_para_dado():
    """devuelve un número aleatorio entre 1 y 6"""
    return int((random()*10) % 6+1)


def tirar_dados(cantidad):
    """imprime en pantalla la cantidad de dados pasados como argumento
    y la suma de ellos"""
    suma = 0
    for i in range(cantidad):
        valor_del_dado = obtener_valor_para_dado()
        dibujar_dado(valor_del_dado)
        suma += valor_del_dado
    print("La suma de los dados es:", suma)


def continuar_jugando():
    """ consulta con el usuario si desea seguir jugando y devuelve un booleano"""
    while True:
        continuar = input("Desea volver a tirar dados? s/n ")
        if continuar.lower() == "s":
            return True
        elif continuar.lower() == "n":
            return False


repetir = True

while repetir:
    tirar_dados(2)
    repetir = continuar_jugando()
