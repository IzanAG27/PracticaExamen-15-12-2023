# Crea una tabla (lista bidimensional) de 5x5 números enteros
taula = [[0 for x in range(5)] for y in range(5)]

# Llena la tabla con números ingresados por el usuario
for fila in range(5):
    for columna in range(5):
        taula[fila][columna] = int(input(f"Introduce un número para la fila {fila+1}, columna {columna+1}: "))

# Muestra la tabla
print("\nTabla:")
for fila in taula:
    print(fila)

# Calcula y muestra la suma de cada fila
print("\nSuma de cada fila:")
for fila in taula:
    suma_fila = sum(fila)
    print(f"Suma: {suma_fila}")

# Calcula y muestra la suma de cada columna
print("\nSuma de cada columna:")
for columna in range(5):
    suma_columna = sum(taula[fila][columna] for fila in range(5))
    print(f"Suma: {suma_columna}")
