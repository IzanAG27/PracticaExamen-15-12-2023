# Crea una matriz bidimensional de longitud 5x15
matriu = [[0 for x in range(15)] for y in range(5)]

# Asigna unos en los bordes de la matriz
for fila in range(5):
    for columna in range(15):
        if fila == 0 or fila == 4 or columna == 0 or columna == 14:
            matriu[fila][columna] = 1

# Muestra el contenido de la matriz
for fila in matriu:
    for valor in fila:
        print(valor, end="")
    print()
