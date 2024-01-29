"""
    Noms: Daniel Arco, Izan Arnáiz.
    Grup: ASIXc1A
    Data: 22/01/2024
    Descripció:
    Programa de traducció d'insults.
"""
INSULTSDICCIONARI = (("CARALLOT", "MOCOS", "MALPARIT"),
                     ("CARAROLLO", "MOCOSO", "MALPARIDO"),
                     ("HECK", "BRAT", "BASTARD"),
                     ("QARDANG", "yIv", "marqeq"))

print("Introdueix l'insult en majúscules: \n")
insult = input("")
posicioX = -1
posicioY = -1

for x in range(0, len(INSULTSDICCIONARI)):
    for y in range(0, len(INSULTSDICCIONARI[x])):
        if insult.upper() == INSULTSDICCIONARI[x][y]:
            posicioX = x
            posicioY = y

if posicioX != -1 or posicioY != -1:
    for x in range(0, len(INSULTSDICCIONARI)):
        if x != posicioX:
            print(INSULTSDICCIONARI[x][posicioY])
else:

    print("ERROR, Introdueix un insult vàlid i en català")