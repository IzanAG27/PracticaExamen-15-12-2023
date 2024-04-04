def inicializar_tablero():
    return [['·' for _ in range(3)] for _ in range(3)]


def mostrar_tablero(tablero):
    for fila in tablero:
        print(' '.join(fila))
    print()


def cambiar_jugador(jugador_actual):
    return 'O' if jugador_actual == 'X' else 'X'


def hacer_movimiento(tablero, fila, columna, jugador_actual):
    if tablero[fila][columna] == '·':
        tablero[fila][columna] = jugador_actual
        if verificar_ganador(tablero, fila, columna, jugador_actual):
            print(f'Guanyen les {jugador_actual}')
            return True
        if '·' not in [c for fila in tablero for c in fila]:
            print('Empat')
            return True
    else:
        print('Movimiento inválido')
    return False


def verificar_ganador(tablero, fila, columna, jugador_actual):
    if all(tablero[fila][c] == jugador_actual for c in range(3)):
        return True
    if all(tablero[f][columna] == jugador_actual for f in range(3)):
        return True
    if fila == columna and all(tablero[i][i] == jugador_actual for i in range(3)):
        return True
    if fila + columna == 2 and all(tablero[i][2 - i] == jugador_actual for i in range(3)):
        return True
    return False


def jugar():
    tablero = inicializar_tablero()
    jugador_actual = 'X'
    juego_terminado = False
    while not juego_terminado:
        mostrar_tablero(tablero)
        movimiento = input(f'Turno de {jugador_actual}, introduce fila y columna: ')
        fila, columna = map(int, movimiento.split())
        juego_terminado = hacer_movimiento(tablero, fila, columna, jugador_actual)
        jugador_actual = cambiar_jugador(jugador_actual)
