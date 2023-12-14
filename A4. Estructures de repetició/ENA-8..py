"""
Programa que demani una cadena de caracteres,
imprimeix únicament les vocals que hi hagi.
"""

try:
    vocales = []
    noValidos = []
    cadena = input("")
    # Busca en cadena y hace un filtro, si el caracter es
    # "a","e","i","o" o "u" los añade a la variable vocales
    for character in cadena.lower():
        if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
            vocales += [character]
        else: # Si no son vocales los añade a la variable noValidos
            noValidos += [character]
    print("Las vocales son: ",vocales)
    print("Los carácteres no válidos son: ", noValidos)
except ValueError:
    print("Introduce bien los datos")
finally:
    print("Programa terminado")
