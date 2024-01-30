TABLA = (
    ("x", "x", "0", "0", "0", "0", "x"),
    ("0", "0", "x", "0", "0", "0", "x"),
    ("0", "0", "0", "0", "0", "0", "x"),
    ("0", "x", "x", "x", "0", "0", "x"),
    ("0", "0", "0", "0", "x", "0", "0"),
    ("0", "0", "0", "0", "x", "0", "0"),
    ("x", "0", "0", "0", "0", "0", "0")
)

posicioX, posicioY = map(int, input("").split())

for i in range(len(TABLA)):
    if i == posicioX:
        for j in range(len(TABLA)):
            if j == posicioY and TABLA[i][j] == "x":
                print("tocado")
                break
            else:
                print("aigua")
                break