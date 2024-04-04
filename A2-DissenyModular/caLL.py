"""
   Izan Arnáiz Gallego
   ITB Institut Tecnològic de Barcelona
   ASIXc M03 UF2 A2 Mòduls i Fitxers
   04/04/2024
"""
import string
import re


def contar_letras_y_caracteres(frase):
    num_caracteres = len(frase.replace(" ", ""))
    num_letras = len(re.findall(r'[a-zA-Z]', frase))
    return num_caracteres, num_letras


def validar_frase(frase):
    palabras = frase.split()
    return len(palabras) > 2


def calcular_letras():
    frases = []
    seguir = True
    while seguir:
        frase = input("")
        if frase == "\\q":
            seguir = False
        elif not validar_frase(frase):
            print("La frase debe contener más de dos palabras.")
            continue
        else:
            frases.append(frase)

    for frase in frases:
        num_caracteres, num_letras = contar_letras_y_caracteres(frase)
        print(f"De {num_caracteres} caracteres {num_letras} son letras")



