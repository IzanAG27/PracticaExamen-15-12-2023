"""
    Nombre: Izan Arnaiz Gallego
    Data: 01/02/2023
    Examen: PP3
    Grup: ASIXc1A
    Descripció:

"""
fraseEncriptada = "104.111.108.97.32.113.117.101.32.116.97.108"
fraseEncriptada = fraseEncriptada.split(".")
frase = ""

for x in fraseEncriptada:
    frase += chr(int(x))

print(frase)

