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
cadena = input("Dime una frase: ")
letra_original = input("¿Qué letra quieres cambiar?: ")

# Esta parte indica que si el usuario falla por razón X al introducir una letra,
# Saltará un error y le volverá a preguntar que letra quiere seleccionar.
while len(letra_original) != 1 or letra_original not in cadena:
    print("Error: introduce una sola letra existente en la cadena.")
    letra_original = input("¿Qué letra quieres cambiar?: ")

# Pedimos que letra quiere cambiar por la letra seleccionada anteriormente
letra_nueva = input("Introduce la nueva letra: ")

# Si introduce mas de 2 en la nueva letra, saltará un error indicando que no puede poner 2 letras,
# Y volverá a preguntar.
while len(letra_nueva) != 1:
    print("Error: introduce solo una letra.")
    letra_nueva = input("Introduce la nueva letra: ")

if letra_original not in cadena:
    print("Error: La letra a cambiar no está en la cadena.")
else:
    cadena = cadena.replace(letra_original, letra_nueva)
    print("Cadena cambiada:", cadena)
