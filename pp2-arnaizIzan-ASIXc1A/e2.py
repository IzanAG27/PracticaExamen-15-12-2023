"""
 Nombre: Izan Arnáiz Gallego
 Grupo: ASIXc1A M03
 Fecha: 15/12/2023
 Enunciado:
    Programa que implementi la funcionalitat del mètode replace. (sense fer ús el mètode)
    És a dir un, programa que demani una cadena de carácteres, un carácter a modificar i un altre carácter de substitució
    El programa haurá de mostrar com a resultat la cadena amb tos els carácters a modificar canviats pel caràcter de
    substitució.
    NO es pot fer servir cap funció predefinida de python. Cal fer el control d'errors.
    Exemple d'execució:
    Introdueix una frase:
    Hola món
    Quin caràcter vols reemplaçar?
    o
    Quin es el caràcter de subsitució?
    x
    RESULTAT:
    Hxla mxn
"""

# Pedimos al usuario que nos introduzca una frase y la letra que quiere cambiar
cadena = input("Dime la frase: ")
caracter_original = input("Que caracter quieres cambiar: ")

# Si introduce mas de 2 caracteres en el input del caracter original, saltará un error indicando que
# no puede poner 2 carácteres seguidos y volverá a preguntar de nuevo.
while len(caracter_original) != 1 or caracter_original not in cadena:
    print("Error: introduce un solo carácter existente en la cadena o una letra que exista en la cadena.")
    caracter_original = input("¿Qué letra quieres cambiar?: ")

# Pedimos al usuario que introduza el caracter por el cual quiere sustituir.
caracter_nuevo = input("Introduce la nueva letra: ")

# Si introduce mas de 2 carácteres en el input del carácter nuevo, saltará un error
# indicando que no puede poner 2 letras y volverá a preguntar de nuevo.
while len(caracter_nuevo) != 1:
    print("Error: introduce solo una letra.")
    caracter_nuevo = input("Introduce la nueva letra: ")

# Si el caracter original está contemplado en char, intercambia el caracter nuevo por intercambio original en char.
for char in str(cadena):
    if caracter_original == char:
        char = caracter_nuevo
    print(char, end="")
