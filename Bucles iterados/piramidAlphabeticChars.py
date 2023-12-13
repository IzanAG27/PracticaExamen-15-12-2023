"""
Imprimir de la A fins la Z.
A cada linia apareix un carcater i la seguent linia apareix un carcater més de forma progresiva. Fins aconseguir tenir una linia que mostri de la A fins la Z
Output
A
A B
A B C
A B C D
A B C D E
A B C D E F
A B C D E F G
A B C D E F G H
A B C D E F G H I
A B C D E F G H I J
"""
# Definir el número de filas para el patrón
num_filas = 26  # Para el alfabeto completo

# Crear el patrón de letras de la 'A' a la 'Z'
for i in range(1, num_filas + 1):
    letra = 65  # Código ASCII para 'A'
    for j in range(0, i):
        print(chr(letra + j), end=" ")
    print()


