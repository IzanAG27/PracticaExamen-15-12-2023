palabra = input("").split()
devnull = []
sinEspaciosON = ""
sinEspaciosRV = ""

for x in palabra:
    if x == " ":
        devnull.append(devnull)
    else:
        sinEspaciosON += x.lower()

for x in sinEspaciosON[::-1]:
    sinEspaciosRV += x.lower()

if sinEspaciosON == sinEspaciosRV:
    print("Es un palindromo")
else:
    print("NO es un palindromo")
