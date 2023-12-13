"""
Programa que imprimeix un tauler d’escacs per pantalla.
Un taulell d’escacs comença amb la casella  Blanca i és de mida 8x8 sempre ;-)
Fer servir:
BLANC = "⬜"
NEGRE = "⬛"
o
NEGRE="██"
BLANC=" "
Interessant: mostrar els numeris de filera i la lletra de columna (com a la imatge)
"""

BLANC = "⬜"
NEGRE = "⬛"

print("   a b c d  e f g h")
for fila in range(8, 0, -1):
    print(f"{fila} ", end="")
    for columna in range(1, 9):
        if (fila + columna) % 2 == 0:
            print(NEGRE, end="")
        else:
            print(BLANC, end="")
    print(f"{fila}")
print("   a b c d  e f g h")
