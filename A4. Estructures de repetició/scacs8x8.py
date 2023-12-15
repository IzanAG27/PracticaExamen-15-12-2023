"""
Izan Arnaiz Gallego
"""
taulell = [[' ' for _ in range(8)] for _ in range(8)]
BLANC="⬛"
NEGRE="⬜"
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            taulell[i][j] = NEGRE
        else:
            taulell[i][j] = BLANC