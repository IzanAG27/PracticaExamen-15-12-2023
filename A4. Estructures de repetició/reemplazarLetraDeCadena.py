cadena = input("Dime una cadena: ")
letra_original = input("¿Qué letra quieres cambiar?: ")

while len(letra_original) != 1 or letra_original not in cadena:
    print("Error: introduce una sola letra existente en la cadena.")
    letra_original = input("¿Qué letra quieres cambiar?: ")

letra_nueva = input("Introduce la nueva letra: ")

while len(letra_nueva) != 1:
    print("Error: introduce solo una letra.")
    letra_nueva = input("Introduce la nueva letra: ")

if letra_original not in cadena:
    print("Error: La letra a cambiar no está en la cadena.")
else:
    cadena = cadena.replace(letra_original, letra_nueva)
    print("Cadena cambiada:", cadena)
