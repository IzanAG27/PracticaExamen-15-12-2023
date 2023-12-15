"""
 Nombre: Izan Arnáiz Gallego
 Grupo: ASIXc1A M03
 Fecha: 15/12/2023
 Enunciado:

"""


# Crear el tablero de ajedrez
TableroAjedrez = [[' ' for _ in range(8)] for _ in range(8)]

# Llenar el tablero con 0 para las casillas blancas y negras respectivamente
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            taulell[i][j] = '0'
        else:
            taulell[i][j] = '0'

posicion_valida = False

# Pedir al usuario la posición de las coordenadas
while not posicion_valida:
    try:
        fila = int(input("Introduce la fila de la torre (1-8): "))
        columna_letra = input("Introduce la columna de la torre (A-H): ")

        # Convertir la letra a número de columna
        columna = ord(columna_letra.upper()) - ord('A') + 1

        if 1 <= fila <= 8 and 1 <= columna <= 8:
            posicion_valida = True
        else:
            print("Debes introducir valores válidos.")
    except ValueError:
        print("Introduce un solo valor para la fila.")

# Mostrar el tablero con las casillas con zeros, y marcar las casillas a las que se puede con '1' y '2'
print('  A B C D E F G H')
print('-----------------')
for i in range(8):
    print(8 - i, end=' ')
    for j in range(8):
        if (i + 1 == fila) or (j + 1 == columna):
            print('1', end=' ')
        else:
            print(taulell[i][j], end=' ')
    print()
