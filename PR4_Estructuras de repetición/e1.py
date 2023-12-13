"""
Programa que demana a l'usuari la introducció de 10 nombres sencers
(que també podrien ser 10000000 😱😳😈) i ha de mostrar,
al final i per pantalla, quants són positius, quants negatius i quants zero.
"""

positivo = 0
negativo = 0
zero = 0


for x in range(11):
    num = int(input(""))
    if num > 0:
        positivo += 1
        print("Número positivo")
    elif num < 0:
        negativo += 1
        print("Número negativo")
    elif num == 0:
        zero += 1
        print("Zero")
    else:
        print("Introduce correctamente los valores")
print(f"Hay {positivo} positivos, {negativo} negativos y {zero} ceros.")