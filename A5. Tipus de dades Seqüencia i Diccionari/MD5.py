"""
    Nombre: Izan
    Data: 1/2/2024
"""

frase = input("")

for x in frase:
    if x == frase[-1]:
        print(ord(x), end="")
    else:
        print(ord(x), end=".")
