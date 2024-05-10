"""
Noms: Daniel Arco i Izan Arnáiz
Data: 23/02/2024
Grup: ASIXc1A
Descripció:
Implementar en Python un programa que demani una
frase per teclat i la retorni per pantalla amb les lletres de
cada paraula de la frase desordenada, tal com diu l’estudi de
la Universitat de Cambridge.
"""
import random
import re


def solicitar_frase():
    return input("Introduce una frase: ")


def desordenar_palabras(frase):
    urls = re.findall(r'(http://|https://|ssh@)[^\s]+', frase)
    for i, url in enumerate(urls):
        frase = frase.replace(url, f'URLPLACEHOLDER{i}')
    palabras = re.split('([^a-zA-Z0-9áéíóúÁÉÍÓÚ])', frase)
    resultado = []
    for palabra in palabras:
        if 'URLPLACEHOLDER' in palabra:
            nueva_palabra = palabra
        elif palabra.isdigit() and len(palabra) == 9:
            nueva_palabra = palabra
        elif len(palabra) > 3 and (palabra[0].isalnum() and palabra[-1].isalnum()):
            first_char = palabra[0]
            last_char = palabra[-1]
            centro = list(palabra[1:-1])
            random.shuffle(centro)
            nueva_palabra = first_char + ''.join(centro) + last_char
        else:
            nueva_palabra = palabra
        resultado.append(nueva_palabra)
    frase_randomizada = ''.join(resultado)
    for i, url in enumerate(urls):
        frase_randomizada = frase_randomizada.replace(f'URLPLACEHOLDER{i}', url)
    return frase_randomizada


frase = solicitar_frase()
print(desordenar_palabras(frase))
