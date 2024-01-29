tablero = 8
TORRE = "♖"
letras = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8
}

posicionX = input("")
posicionY = int(input(""))

for i in range(tablero):
    for j in range(tablero):
        if i+1 == letras[posicionX] and j+1 == posicionY:
            print(TORRE, end="")
        elif i+1 == letras[posicionX]:
            print("* ", end="")
        elif j+1 == posicionY:
            print("* ", end="")
        else:
            print("x ", end="")
    print("")

