
p = input("").split()

palabra = str(p[0])
posicion = int(p[1])
cont = 0
for letter in palabra:
    if posicion == cont:
        print(letter)
    cont += 1
