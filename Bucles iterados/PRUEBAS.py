cadena = input("Introduce una frase: ")
letra_original = ""
letra_nueva = ""

# Solicitar la letra que se quiere reemplazar y verificar si está en la cadena
while letra_original not in cadena or len(letra_original) != 1:
    letra_original = input("Introduce la letra que quieres reemplazar: ")
    if len(letra_original) != 1 or letra_original not in cadena:
        print("La letra que deseas reemplazar no está en la cadena o no es válida. Introduce otra vez.")

# Solicitar la letra nueva
while len(letra_nueva) != 1:
    letra_nueva = input("Introduce la letra nueva: ")
    if len(letra_nueva) != 1:
        print("Por favor, introduce solo una letra.")

nueva_cadena = ""
for caracter in cadena:
    if caracter == letra_original:
        nueva_cadena += letra_nueva
    else:
        nueva_cadena += caracter

print("Cadena original:", cadena)
print("Cadena modificada:", nueva_cadena)
