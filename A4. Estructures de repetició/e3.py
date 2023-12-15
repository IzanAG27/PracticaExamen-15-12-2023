limite = int(input("Introduce un número límite: "))

suma_pares = 0
suma_impares = 0

for i in range(limite):
    if i % 2 == 0:
        suma_pares += i
    else:
        suma_impares += i

print(f"Si el límite es {limite}, la suma de los números pares es: {suma_pares}")
print(f"Si el límite es {limite}, la suma de los números impares es: {suma_impares}")
