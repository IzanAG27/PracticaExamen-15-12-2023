"""
    Nombre: Izan Arnaiz
    Data: 1/2/2024
    Grup: ASIXc1A
    Curs: 2023-24
    Descripció:

"""
# Demanar a l'usuari la quantitat de files i columnes de la matriu 2D
files = int(input("Introdueix la quantitat de files de la matriu: "))
columnes = int(input("Introdueix la quantitat de columnes de la matriu: "))
# Comprovar que la matriu sigui quadrada
if files != columnes:
    print("Error: La matriu no és quadrada.")
else:
    # Comprovar que la mida de la matriu és senar
    if files % 2 == 0:
        print("Error: La mida de la matriu ha de ser senar.")
    else:
        # Inicialitzar la matriu amb zeros
        matriu = [[0] * columnes for x in range(files)]
        # Omplir la matriu amb 1's a les vores i la resta amb 0's
        for i in range(files):
            for j in range(columnes):
                if i == 0 or i == files - 1 or j == 0 or j == columnes - 1:
                    matriu[i][j] = 1
        # Mostrar la matriu resultante
        print("Matriu resultante:")
        for fila in matriu:
            print(fila)



