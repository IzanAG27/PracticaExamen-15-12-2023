from SystemColors import *


def contiene_letras(texto):
    return any(caracter.isalpha() for caracter in texto)


def obtener_entrada():
    texto = input("")
    if texto == '':
        print("La cadena está vacía. Por favor, introduce un texto.")
        return texto
    if not contiene_letras(texto):
        print("La cadena solo contiene números, los cuales no se van a pintar.")
    return texto


def colorear_caracter(caracter):
    if caracter.isdigit():
        return caracter
    color = obtener_color(caracter) if es_vocal(caracter) else BLACK
    return color + caracter + FEND


def es_vocal(caracter):
    return caracter.lower() in 'aeiouáéíóú'


def obtener_color(caracter):
    if caracter.lower() == 'a' or caracter.lower() == 'á':
        return RED
    elif caracter.lower() == 'e' or caracter.lower() == 'é':
        return GREEN
    elif caracter.lower() == 'i' or caracter.lower() == 'í':
        return YELLOW
    elif caracter.lower() == 'o' or caracter.lower() == 'ó':
        return BLUE
    elif caracter.lower() == 'u' or caracter.lower() == 'ú':
        return VIOLET
    else:
        return BLACK


def colorear_caracter(caracter):
    color = obtener_color(caracter) if es_vocal(caracter) else BLACK
    return color + caracter + FEND


def colorear_texto(texto):
    return ''.join(colorear_caracter(c) for c in texto)


def principal():
    texto = obtener_entrada()
    if contiene_letras(texto):
        texto_coloreado = colorear_texto(texto)
        print(texto_coloreado)