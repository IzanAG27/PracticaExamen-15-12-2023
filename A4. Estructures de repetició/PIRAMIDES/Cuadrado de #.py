lado = int(input(""))  # Longitud del lado del cuadrado

for i in range(lado):
    for j in range(lado):
        if i == 0 or i == lado - 1 or j == 0 or j == lado - 1:
            print('#', end=' ')
        else:
            print(' ', end=' ')  # Espacio para el interior del cuadrado
    print()  # Cambio de línea después de cada fila
