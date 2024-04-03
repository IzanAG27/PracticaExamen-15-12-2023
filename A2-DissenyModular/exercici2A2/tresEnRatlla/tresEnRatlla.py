def crear_tablero():
    return [[' ' for _ in range(3)] for _ in range(3)]


def mostrar_tablero(tablero):
    for fila in tablero:
        print('|'.join(fila))
        print('-' * 5)


def jugada_valida(tablero, fila, columna):
    if fila < 0 or fila > 2 or columna < 0 or columna > 2:
        print("Por favor, introduce una fila y una columna válidas (1-3).")
        return False
    if tablero[fila][columna] != ' ':
        print("Esa posición ya está ocupada. Por favor, elige otra.")
        return False
    return True


def hacer_jugada(tablero, fila, columna, jugador):
    if jugada_valida(tablero, fila, columna):
        tablero[fila][columna] = jugador
        return True
    return False


def ganador(tablero):
    for fila in tablero:
        if fila.count(fila[0]) == len(fila) and fila[0] != ' ':
            return True
    for columna in range(len(tablero[0])):
        if tablero[0][columna] == tablero[1][columna] == tablero[2][columna] != ' ':
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != ' ':
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != ' ':
        return True
    return False


def play_game():
    tablero = crear_tablero()
    jugador_actual = 'X'
    game_over = False

    while not game_over:
        mostrar_tablero(tablero)
        entrada = input("Introduce la fila y la columna (0-2) separadas por un espacio: ").split()
        if len(entrada) != 2:
            print("Por favor, introduce dos valores, y que sean enteros positivos..")
            continue
        fila, columna = map(int, entrada)
        if hacer_jugada(tablero, fila, columna, jugador_actual):
            if ganador(tablero):
                print(f"¡El jugador {jugador_actual} ha ganado!")
                game_over = True
            else:
                jugador_actual = 'O' if jugador_actual == 'X' else 'X'
        else:
            print("Jugada no válida. Inténtalo de nuevo.")