"""
Exercici: Canadian Tree
Nom: Izan Arnaiz
Grup: ASIXc1a M03
Data: 18/12/2023
"""


HOJAS = "🌿"
TRONC = "🪵"
mida = int(input())
for i in range(1, mida + 1):
    if i >= 0.8 * mida:
        espacio = " " * (int((0.8 * mida)))
        troncos = TRONC * int((0.2 * mida))
        print(espacio, troncos)
    else:
        espacio = " " * (mida - i)
        HOJASSS = HOJAS * i
        print(espacio + HOJASSS)

