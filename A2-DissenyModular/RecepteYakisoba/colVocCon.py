"""
   Izan Arnáiz Gallego
   ITB Institut Tecnològic de Barcelona
   ASIXc M03 UF2 A2 Mòduls i Fitxers
   04/04/2024
"""
from SystemColors import *


def obtenerEntrada():
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


def obtenerColor(caracter):
    colores = {'a': RED, 'á': RED, 'e': GREEN, 'é': GREEN, 'i': YELLOW, 'í': YELLOW, 'o': BLUE, 'ó': BLUE, 'u': VIOLET,
               'ú': VIOLET}
    return colores.get(caracter.lower(), BLACK)


def colorearCaracter(caracter):
    color = obtenerColor(caracter) if es_vocal(caracter) else BLACK
    return color + caracter + FEND


def colorearTexto(texto):
    return ''.join(colorearCaracter(c) for c in texto)


def mostrarTextoPintado():
    texto = obtenerEntrada()
    texto_coloreado = colorearTexto(texto)
    print(texto_coloreado)
