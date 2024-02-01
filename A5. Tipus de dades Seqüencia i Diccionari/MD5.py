"""
    Nombre: Izan
    Data: 1/2/2024
"""

frase = input("")

for x in range(len(frase)):
    if x == len(frase) - 1:
        print(ord(frase[x]), end="")
    else:
        print(ord(frase[x]), end=".")
