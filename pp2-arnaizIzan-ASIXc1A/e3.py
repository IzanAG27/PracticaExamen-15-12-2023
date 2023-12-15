"""
 Nombre: Izan Arnáiz Gallego
 Grupo: ASIXc1A M03
 Fecha: 15/12/2023
 Enunciado:
    Programa que printa por pantalla una matriz de 8x8 (filas y columnas) con zeros en cada posicion,
    con excepción de:
    · Pintar un 1 a les posicions de la diagonal que va de 0.0 a 7.7
    · Pintar un 2 a les posicions de la diagonal inversa que va de 0.7 a 7.0
    Cal fer un control d'errors. Obligatori fer servir sentencies de repetició, no es pot solucionar amb un print.
"""
try:

    # Pedimos las coordendas al usuario
    coordenadas = input("Introduce las coordenadas:  ").split()
    xCoord = int(coordenadas[0])
    yCoord = int(coordenadas[1])

    for o in range(1, 8 + 1):
        if o / 2 != o // 2:
            var1 = "0"
            var2 = "0"
        else:
            var1 = "0"
            var2 = "0"

        for p in range(1, 8 + 1):
                if ((xCoord == p or yCoord == o) or (xCoord + yCoord == o + p or xCoord - yCoord == p - o)) and p == 8:
                    print("1",end="\n")
                elif xCoord + yCoord == o + p or xCoord - yCoord == p - o:
                    print("2",end=" ")
                elif p // 2 != p / 2:
                    print(var1,end=" ")
                elif p == 8:
                    print(var2,end=" \n")

                else:
                    print(var2,end=" ")
except ValueError:
    print("\nIntroduce correctamente los valores")
finally:
    print("\n/_|*_·_*|_/ Programa terminado /_|*_·_*|_/")