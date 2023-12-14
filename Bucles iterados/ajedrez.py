"""
Noms: Jofre Aleman, Dani Arco, Izan Arnaiz
Data: 1/12/2023
Lliurament: 4/12/2023
ASIXc M03-UF1 A4 PR4

Descripció:
Programa que imprimeix un tauler d’escacs per pantalla.
Un taulell d’escacs comença amb la casella  Blanca i és de mida 8x8 sempre ;-)

Fer servir:
BLANC = "⬜"
NEGRE = "⬛"
o
NEGRE="██"
BLANC=" "

 Interessant: mostrar els numeris de filera
  i la lletra de columna (com a la imatge)
"""
BLANC = " B "
NEGRE = " N "

lletres = "  a  b  c  d  e  f  g  h"
numeros = ("87654321")

for fila in range(8):
    print("\n" + numeros[fila], end="")
    for columna in range(8):
        if (fila + columna) % 2 == 0:
            casella = BLANC
        else:
            casella = NEGRE
        print(casella, end="")

print()
print(lletres)