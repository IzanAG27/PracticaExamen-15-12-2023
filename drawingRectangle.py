"""
Fes una funció que dibuixi un rectangle donats els seus costats.
Input
3 4
Ouput
***
***
***
***
"""
rectangulo = input("").split()

lado1 = int(rectangulo[0])
lado2 = int(rectangulo[1])

for x in range(lado1):
    if x == 0 or x == lado1 - 1:
        print("*" * lado2)
    else:
        print("*" + "*" * (lado2 - 2) + "*")


