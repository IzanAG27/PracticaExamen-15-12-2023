# Bucle While

import math


num = int(input(""))
while num < 0:
    print("Introduce un numero positivo")
    num = int(input(""))

print(f"\n La raiz cuadrada es: {(math.sqrt(num)):.2f}")