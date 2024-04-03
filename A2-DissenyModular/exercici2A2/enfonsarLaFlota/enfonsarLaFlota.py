import random


def crear_tablero():
    tablero = [['💧' for _ in range(6)] for _ in range(6)]
    for i in range(1, 6):
        tablero[i][0] = str(i)
        tablero[0][i] = chr(64 + i)
    return tablero

def mostrar_tablero(tablero):
    for fila in tablero:
        print(' '.join(fila))


def colocar_barcos(tablero, num_barcos):
    for _ in range(num_barcos):
        fila = random.randint(1, 5)
        columna = random.randint(1, 5)
        while tablero[fila][columna] == '🚢':
            fila = random.randint(1, 5)
            columna = random.randint(1, 5)
        tablero[fila][columna] = '🚢'
    return tablero


def hacer_jugada(tablero, fila, columna):
    if tablero[fila][columna] == '🚢':
        tablero[fila][columna] = 'X'
        print("¡Has hundido un barco!")
    else:
        print("¡Agua!")

def comprobar_ganador(tablero):
    for fila in tablero:
        if '🚢' in fila:
            return False
    return True

def play_game():
    tablero = crear_tablero()
    tablero = colocar_barcos(tablero, 3)
    game_over = False

    while not game_over:
        mostrar_tablero(tablero)
        entrada = input("Introduce la coordenada (A-E 1-5): ").split()
        fila = int(entrada[1])
        columna = ord(entrada[0].upper()) - 64
        hacer_jugada(tablero, fila, columna)
        if comprobar_ganador(tablero):
            print("¡Has ganado!")
            game_over = True

