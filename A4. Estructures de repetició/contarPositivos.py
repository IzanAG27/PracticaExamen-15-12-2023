nums = [int(caracter) for caracter in input().split()]
sumas = []

for x in nums:
    if x > 0:
        sumas.append(x)
    else:
        print("Introduce un entero válido")

print(sum(sumas))
