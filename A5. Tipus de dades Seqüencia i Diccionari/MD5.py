"""
    Nombre: Izan Arnaiz Gallego
    Data: 01/02/2023
    Examen: PP3
    Grup: ASIXc1A
    Descripció:

"""

frase = input("")

for x in range(len(frase)):
    if x == len(frase) - 1:
        print(ord(frase[x]), end="")
    else:
        print(ord(frase[x]), end=".")
