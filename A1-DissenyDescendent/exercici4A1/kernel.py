
"""
Este programa toma una cadena de texto como
entrada y añade un espacio entre cada carácter.
Imprime la cadena resultante. Si la cadena de
entrada está vacía, imprime "La cadena está vacía".
"""

def pedir_cadena():
    cadena = input("Texto: ")
    return cadena


def afegirEspaiACadaCaracter(cadena):
    lista = []
    if cadena:  # Comprueba si la cadena no está vacía
        for x in cadena:
            lista.append(x)
        cadena_sin_espacios = ' '.join(lista)
        print(cadena_sin_espacios)
    else:
        print("La cadena está vacía")
    return lista