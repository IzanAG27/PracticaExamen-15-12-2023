"""
   Izan Arnáiz Gallego
   ITB Institut Tecnològic de Barcelona
   ASIXc M03 UF2 A2 Mòduls i Fitxers
   04/04/2024
"""


def procesar_frase(frase):
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
    palabras = frase.split()
    es_valida = len(palabras) > 2
    return letras, es_valida


def calcular_letras():
    frase = input("")
    letras, es_valida = procesar_frase(frase)
    if not es_valida:
        print("La frase debe contener más de dos palabras.")
    else:
        imprimir_resultado(letras)


def imprimir_resultado(letras):
    print("Lletra    Quantitat    Posició")
    for letra, datos in letras.items():
        print(f"{letra}         {datos['cantidad']}            {', '.join(map(str, datos['posiciones']))}")