n = int(input("Introduce la altura de la pirámide: "))

BRICK = "🧱"

for i in range(1, n + 1):
    # Imprime los espacios en blanco a la izquierda de los ladrillos
    print(" " * (n - i), end="")

    # Imprime los ladrillos
    print(BRICK * i)
