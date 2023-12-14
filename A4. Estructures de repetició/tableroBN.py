BLANC = " B "
NEGRE = " N "
TORRE = " T "
MOVTORRE = " * "

tablero = [[BLANC if (fila + columna) % 2 == 0 else NEGRE for columna in range(8)] for fila in range(8)]

numeros = [str(i) for i in range(8, 0, -1)]  # Lista de números de fila

print("Tablero de ajedrez:")
for fila in range(8):
    for columna in range(8):
        print(tablero[fila][columna], end=" ")
    print(numeros[fila])  # Muestra los números de fila correspondientes

print(" a   b   c   d   e   f   g   h")  # Muestra las letras de columna

# Obtener coordenadas de la torre
coordenada_torre = input("Introduce las coordenadas para la torre (8a - 1h): ")

# Verificar coordenadas
fila_letra = coordenada_torre[0]
columna_letra = coordenada_torre[1]

# Validar coordenadas
if '1' <= fila_letra <= '8' and 'a' <= columna_letra <= 'h':
    fila_numero = int(fila_letra)
    columna_torre = ord(columna_letra) - ord('a')

    fila_torre = 8 - fila_numero  # Ajuste de la fila

    tablero[fila_torre][columna_torre] = TORRE

    # Marcar los movimientos posibles de la torre en el tablero
    for i in range(8):
        if i != fila_torre:
            tablero[i][columna_torre] = MOVTORRE
        if i != columna_torre:
            tablero[fila_torre][i] = MOVTORRE

    # Mostrar el tablero resultante con la torre y sus movimientos posibles
    print("\nTablero con la torre y sus movimientos posibles:")
    for fila in range(8):
        for columna in range(8):
            print(tablero[fila][columna], end=" ")
        print(numeros[fila])  # Muestra los números de fila correspondientes

    print(" a   b   c   d   e   f   g   h")  # Muestra las letras de columna
else:
    print("Coordenadas no válidas.")
