TABLERO = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

x = int(input())
y = int(input())

for i in range(len(TABLERO)):
    if TABLERO[i][x] == 0:
        TABLERO[i][x] = 1
    for j in range(len(TABLERO)):
        if TABLERO[y][j] == 0:
            TABLERO[y][j] = 1
        elif TABLERO[y][x] == 1:
            TABLERO[y][x] = 2

for i in range(len(TABLERO)):
    print(TABLERO[i])