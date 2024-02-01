"""

    Nombre: Izan
    Data: 1/2/2024
"""
fraseEncriptada = "104.111.108.97.32.113.117.101.32.116.97.108"
fraseEncriptada = fraseEncriptada.split(".")
frase = ""

for x in fraseEncriptada:
    frase += chr(int(x))

print(frase)

