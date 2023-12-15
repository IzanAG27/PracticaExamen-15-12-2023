try:
    n = input("Pon las coordenadas: ").split()
    cordx = int(n[0])
    cordy = int(n[1])

    if 1 <= cordx <= 8 and 1 <= cordy <= 8:
        for y in range(1, 9):
            for x in range(1, 9):
                if cordx == x and cordy == y:
                    print("C", end=" ")
                elif (abs(x - cordx) == 1 and abs(y - cordy) == 2) or (abs(x - cordx) == 2 and abs(y - cordy) == 1):
                    print("*", end=" ")
                else:
                    if (x + y) % 2 == 0:
                        print("B", end=" ")
                    else:
                        print("N", end=" ")
            print()
    else:
        print("Coordenadas fuera del tablero.")
except ValueError:
    print("Error: Ingresa coordenadas válidas.")