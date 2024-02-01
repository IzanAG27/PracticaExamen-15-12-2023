"""
    Nombre: Izan Arnaiz
    Data: 01/02/2024
    Grup: ASIXc1A
 solicita al usuario ingresar 15 palabras, luego calcula la longitud
 de cada palabra y muestra la palabra más larga, la más corta y la
 longitud promedio de todas las palabras.
"""

palabras = []
longitudes = []
posiciones_extremas = []
NUMERO_PALABRAS = 15

# Solicitar al usuario que ingrese 15 palabras
for i in range(NUMERO_PALABRAS):
    palabra_actual = str(input("Ingresa una palabra: "))
    palabras.append(palabra_actual)

print("Palabras ingresadas:", palabras)

# Calcular longitudes de las palabras
for longitud in map(len, palabras):
    longitudes.append(longitud)

# Obtener las posiciones de la palabra más larga y más corta
posiciones_extremas.append(longitudes.index(max(longitudes)))
posiciones_extremas.append(longitudes.index(min(longitudes)))

# Obtener las palabras más larga y más corta
palabras_extremas = [palabras[pos] for pos in posiciones_extremas]

print("La palabra más larga es:", palabras_extremas[0], "y la más corta es:", palabras_extremas[1])
print("La longitud promedia de las palabras es:", sum(longitudes) / len(longitudes))
