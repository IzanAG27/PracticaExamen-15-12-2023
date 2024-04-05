"""
   Izan Arnáiz Gallego
   ITB Institut Tecnològic de Barcelona
   ASIXc M03 UF2 A2 Mòduls i Fitxers
   04/04/2024
"""
import re


def procesar_frase(frase):
    num_caracteres = len(frase.replace(" ", ""))
    num_letras = len(re.findall(r'[a-zA-Z]', frase))
    palabras = frase.split()
    es_valida = len(palabras) > 2
    return num_caracteres, num_letras, es_valida


def calcular_letras():
    frases = []
    comprobar = True
    while comprobar:
        frase = input("")
        if frase == "\\q":
            comprobar = False
        else:
            num_caracteres, num_letras, es_valida = procesar_frase(frase)
            if not es_valida:
                print("La frase debe contener más de dos palabras.")
            else:
                frases.append((num_caracteres, num_letras))

    if not comprobar:
        for num_caracteres, num_letras in frases:
            print(f"De {num_caracteres} caracteres {num_letras} son letras")
