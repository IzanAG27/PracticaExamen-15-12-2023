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
        if letra.isalpha():
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


def calcular_letras():
    seguir = True
    while seguir:
        frase = input("")
        if frase == "\\q":
            seguir = False
        elif not validar_frase(frase):
            print("La frase debe contener más de dos palabras.")
        else:
            letras = contar_vocales_y_consonantes(frase)
            print("Lletra    Quantitat    Posició")
            for letra, datos in letras.items():
                print(
                    f"{letra}         {datos['cantidad']}            {', '.join(map(str, datos['posiciones']))}")
            seguir = False  # Termina el bucle después de imprimir la tabla
    print("\n")  # Imprime una línea en blanco después de la tabla