"""
   Izan Arnáiz Gallego
   ITB Institut Tecnològic de Barcelona
   ASIXc M03 UF2 A2 Mòduls i Fitxers
   04/04/2024
"""


def contar_vocales_y_consonantes(frase):
    vocales = 'aeiou'
    letras = {}
    for i, letra in enumerate(frase.lower(), start=1):
        if letra:
            if letra in vocales:
                tipo = 'vocal'
            else:
                tipo = 'consonante'
            if letra not in letras:
                letras[letra] = {'tipo': tipo, 'cantidad': 1, 'posiciones': [i]}
            else:
                letras[letra]['cantidad'] += 1
                letras[letra]['posiciones'].append(i)
    return letras


def validar_frase(frase):
    palabras = frase.split()
    return len(palabras)


def obtener_frase():
    return input("")


def imprimir_resultado(letras):
    print("Lletra    Quantitat    Posició")
    for letra, datos in letras.items():
        print(f"{letra}         {datos['cantidad']}            {', '.join(map(str, datos['posiciones']))}")


def calcular_letras():
    seguir = True
    while seguir:
        frase = obtener_frase()
        if frase == "\\q":
            seguir = False
        elif not validar_frase(frase):
            print("La frase debe contener más de dos palabras.")
        else:
            letras = contar_vocales_y_consonantes(frase)
            imprimir_resultado(letras)
            seguir = False
    print("\n")
