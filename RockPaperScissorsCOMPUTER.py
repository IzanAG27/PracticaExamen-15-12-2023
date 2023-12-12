import random
print("1 == Piedra.\n2 == Paper.\n3 == Tisora.\n")
num = int(input(""))
aleatori = int(random.uniform(1, 4))# Fins a 4 no inclòs

if num == aleatori:
    print(aleatori)
    print("Empate")
elif num == 1 and aleatori == 3:
    print(aleatori)
    print("Ganas")
elif num == 3 and aleatori == 1:
    print(aleatori)
    print("Gana la máquina")
elif num == 2 and aleatori == 3:
    print(aleatori)
    print("Gana la máquina")
elif num == 3 and aleatori == 2:
    print(aleatori)
    print("Ganas")
elif num == 1 and aleatori == 2:
    print(aleatori)
    print("Gana la máquina")
elif num == 2 and aleatori == 1:
    print(aleatori)
    print("Ganas")
else:
    print("Introduce bien los valores")



