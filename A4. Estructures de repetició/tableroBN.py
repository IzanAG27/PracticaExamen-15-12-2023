# Crear el tablero de ajedrez
taulell = [[' ' for _ in range(8)] for _ in range(8)]

# Llenar el tablero con 'B' y 'N' para las casillas blancas y negras respectivamente
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            taulell[i][j] = 'B'
        else:
            taulell[i][j] = 'N'

posicion_valida = False

# Pedir al usuario la posición de la torre
while not posicion_valida:
    try:
        fila = int(input("Introduce la fila de la torre (1-8): "))
        columna_letra = input("Introduce la columna de la torre (A-H): ")

        # Convertir la letra a número de columna
        columna = ord(columna_letra.upper()) - ord('A') + 1

        if 1 <= fila <= 8 and 1 <= columna <= 8:
            posicion_valida = True
        else:
            print("Debes ingresar valores válidos.")
    except ValueError:
        print("Por favor, ingresa un valor válido para la fila.")

# Mostrar el tablero con las casillas blancas y negras, y marcar las casillas a las que se puede mover la torre con '*'
print('  A B C D E F G H')
for i in range(8):
    print(8 - i, end=' ')
    for j in range(8):
        if (i + 1 == fila) or (j + 1 == columna):
            print('*', end=' ')
        else:
            print(taulell[i][j], end=' ')
    print()
