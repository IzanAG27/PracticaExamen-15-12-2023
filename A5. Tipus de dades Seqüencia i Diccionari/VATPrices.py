listaNum = [float(x) for x in input("").split()]

IVA = 1.21

for x in listaNum:
    print(x, f" IVA = {round(x * IVA, 2)}")