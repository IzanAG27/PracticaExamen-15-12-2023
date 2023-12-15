try:
    n = input("Pon las coordenadas:  ").split()
    cordx = int(n[0])
    cordy = int(n[1])
    for y in range(1, 9):
        if y // 2 != y / 2:
            aux1 = "B"
            aux2 = "N"
        else:
            aux1 = "N"
            aux2 = "B"
        for l in range(1, 9):
                if ((cordx == l or cordy == y) or (cordx + cordy == y + l or cordx - cordy == l - y)) and l == 8:
                    print("*", end="\n")
                elif(cordx + cordy == y + l or cordx - cordy == l - y):
                    print("*", end=" ")
                elif l == 8:
                    print(aux2, end="\n")
                elif l // 2 != l / 2:
                    print(aux1, end=" ")
                else:
                    print(aux2, end=" ")
    print("----------------")
    print("  1 2 3 4 5 6 7 8")
except ValueError:
    print("Error de datos")
finally:
    print("Programa terminado")