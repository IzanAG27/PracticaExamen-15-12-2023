print("1 == Piedra.\n2 == Paper.\n3 == Tisora.\n")
joc = input("").split()

mov1 = int(joc[0])
mov2 = int(joc[1])

if mov1 == 1 and mov2 == 2:
    print("Gana el segundo")
elif mov2 == 2 and mov1 == 1:
    print("Gana el primero")
elif mov1 == 3 and mov2 == 1:
    print("Gana el segundo")
elif mov2 == 1 and mov2 == 3:
    print("Gana el primero")
elif mov1 == 2 and mov2 == 3:
    print("Gana el segundo")
elif mov1 == 3 and mov2 == 2:
    print("Gana el primero")
else:
    print("Empate")
