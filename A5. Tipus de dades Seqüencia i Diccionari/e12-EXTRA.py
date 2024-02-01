"""
    Nombre: Izan Arnaiz
    Data: 1/2/2024
    Grup: ASIXc1A
    Curs: 2023-24
"""

# Inicializa la variable para controlar el bucle
continuar_pidiendo = True

# Mientras sea necesario, sigue solicitando al usuario que introduzca los números correctos
while continuar_pidiendo:
    try:
        filas = int(input("Introduce el número de filas (impar e igual al número de columnas): "))
        columnas = int(input("Introduce el número de columnas (impar e igual al número de filas): "))

        # Comprueba si los números cumplen con los requisitos
        if filas % 2 == 1 and columnas % 2 == 1 and filas == columnas:
            continuar_pidiendo = False  # Cambia la variable para salir del bucle
        else:
            print("Error: Ambos números deben ser impares e iguales. Vuelve a intentarlo.")
    except ValueError:
        print("Error: Debes introducir un número entero. Vuelve a intentarlo.")

# Crea una matriz bidimensional de tamaño especificado por el usuario
    matriz = [[0 for x in range(columnas)] for y in range(filas)]

# Asigna 1s en los bordes de la matriz
    for fila in range(filas):
        for columna in range(columnas):
            if fila == 0 or fila == filas - 1 or columna == 0 or columna == columnas - 1:
                matriz[fila][columna] = 1

# Muestra el contenido de la matriz
    for fila in matriz:
        for valor in fila:
            print(valor, end="")
        print()

