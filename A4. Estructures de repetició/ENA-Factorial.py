n = int(input("Ingresa un número para calcular su factorial: "))
factorial = 1

if n < 0:
    print("El factorial no está definido para números negativos.")
elif n == 0:
    print("El factorial de 0 es 1.")
else:
    for i in range(1, n + 1):
        factorial *= i
    print(f"El factorial de {n} es: {factorial}")
