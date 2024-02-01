"""
solicita al usuario que ingrese una frase, convierte la frase a
minúsculas y luego realiza la siguiente transformación:

Reemplaza cada vocal "a" (o acentuada), "e" (o acentuada), "i"
(o acentuada), "o" (o acentuada) y "u" (o acentuada) por
los números "4", "3", "1", "0" y "7" respectivamente.
Imprime la frase resultante después de aplicar estas sustituciones.
"""

frase = str(input("Especifica una frase: "))
frase = frase.lower()
for x in range(len(frase)):
    if frase[x] == "a" or frase[x] == "á" or frase[x] == "à":
        print("4", end="")
    elif frase[x] == "e" or frase[x] == "é" or frase[x] == "è":
        print("3", end="")
    elif frase[x] == "i" or frase[x] == "í" or frase[x] == "ì":
        print("1", end="")
    elif frase[x] == "o" or frase[x] == "ó" or frase[x] == "ò":
        print("0", end="")
    elif frase[x] == "u" or frase[x] == "ú" or frase[x] == "ù":
        print("7", end="")
    else:
        print(frase[x], end="")
print("")