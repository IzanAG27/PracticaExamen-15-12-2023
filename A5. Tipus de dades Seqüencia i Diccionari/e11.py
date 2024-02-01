# Crea una matriz bidimensional de longitud 5x5
matriu = [[0 for x in range(5)] for y in range(5)]

# Asigna los valores en las diagonales principales
for i in range(5):
    matriu[i][i] = 1
    matriu[i][4 - i] = 1

# Muestra el contenido de la matriz
for fila in matriu:
    for valor in fila:
        print(valor, end=" ")
    print()
