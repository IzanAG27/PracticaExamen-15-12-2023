"""
   Izan Arnáiz Gallego
   ITB Institut Tecnològic de Barcelona
   ASIXc M03 UF2 A2 Mòduls i Fitxers
   04/04/2024
"""
from SystemColors import *


def obtener_entrada_valida():
    while True:
        texto = input("")
        if texto == '':
            print("La cadena está vacía. Por favor, introduce un texto.")
        elif not any(caracter for caracter in texto):
            print("La cadena solo contiene números, los cuales no se van a pintar.")
        else:
            return texto


def es_vocal(caracter):
    return caracter.lower() in 'aeiouáéíóú'


def obtener_color(caracter):
    colores = {'a': RED, 'á': RED, 'e': GREEN, 'é': GREEN, 'i': YELLOW, 'í': YELLOW, 'o': BLUE, 'ó': BLUE, 'u': VIOLET,
               'ú': VIOLET}
    return colores.get(caracter.lower(), BLACK)


def colorear_caracter(caracter):
    color = obtener_color(caracter) if es_vocal(caracter) else BLACK
    return color + caracter + FEND


def colorear_texto(texto):
    return ''.join(colorear_caracter(c) for c in texto)


def mostrar_texto_pintado():
    texto = obtener_entrada_valida()
    texto_coloreado = colorear_texto(texto)
    print(texto_coloreado)
