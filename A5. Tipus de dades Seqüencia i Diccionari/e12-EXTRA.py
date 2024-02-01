"""
    Nombre: Izan Arnaiz
    Data: 1/2/2024
    Grup: ASIXc1A
    Curs: 2023-24
"""

# Solicita al usuario que introduzca el número de filas y columnas
filas = int(input("Introduce el número de filas: "))
columnas = int(input("Introduce el número de columnas: "))

# Comprueba si la matriz es cuadrada
if filas != columnas:
    print("Error: La matriz no es cuadrada. El número de filas y columnas debe ser igual.")
else:
    # Crea una matriz bidimensional de tamaño especificado por el usuario
    matriu = [[0 for x in range(columnas)] for y in range(filas)]

    # Asigna unos en los bordes de la matriz
    for fila in range(filas):
        for columna in range(columnas):
            if fila == 0 or fila == filas - 1 or columna == 0 or columna == columnas - 1:
                matriu[fila][columna] = 1

    # Muestra el contenido de la matriz
    for fila in matriu:
        for valor in fila:
            print(valor, end="")
        print()

