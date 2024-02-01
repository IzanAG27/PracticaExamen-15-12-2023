"""
    Nombre: Izan Arnaiz Gallego
    Data: 01/02/2023
    Examen: PP3
    Grup: ASIXc1A
    Descripció:
"""
try:
    files = int(input("Introdueix la quantitat de files de la matriu: "))
    columnes = int(input("Introdueix la quantitat de columnes de la matriu: "))
    if files == columnes:
        if files % 2 != 0 and columnes % 2 != 0:
            matriu = [[0] * columnes for j in range(files)]
            for x in range(files):
                for y in range(columnes):
                    if x == 0 or y == files - 1 or y == 0 or x == files - 1:
                        matriu[x][y] = int(1)
            for x in matriu:
                print(x)
        else:
            print("L'HAS CAGAO BACALAO, Introduce valores enteros impares.")
except ValueError:
    print("\nIntroduce valores enters")
finally:
    print("\nPrograma terminado")