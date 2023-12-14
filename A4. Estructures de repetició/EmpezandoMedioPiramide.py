num = int(input("Ingresa un número: "))
for i in range(1, num + 1):
    # Imprimir los espacios antes de los números
    for espacio in range(num - i):
        print(' ', end=' ')
    # Imprimir los números
    for j in range(1, 2 * i):
        print(i, end=' ')

    print()  # Cambiar de línea después de cada fila