palabra = input("").split()
devnull = []
sinEspaciosON = ""
sinEspaciosRV = ""
ACENTOS = ('á', 'à', 'è', 'é', 'ì', 'í', 'ò', 'ó', 'ù', 'ú')
VOWELS = ('a', 'a', 'e', 'e', 'i', 'i', 'o', 'o', 'u', 'u',)
for x in palabra:
    if x == " ":
        devnull.append(devnull)
    else:
        sinEspaciosON += x.lower()

for x in palabra:
    if x in ACENTOS:
        palabra.replace(x, VOWELS[ACENTOS.index(x)] )
print(palabra)
for x in sinEspaciosON[::-1]:
    sinEspaciosRV += x.lower()

if sinEspaciosON == sinEspaciosRV:
    print("Es un palindromo")
else:
    print("NO es un palindromo")
