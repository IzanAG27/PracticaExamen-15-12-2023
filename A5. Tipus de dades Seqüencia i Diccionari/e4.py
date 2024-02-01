# Inicializa una lista vacía para almacenar los números
lista_numeros = []

# Bandera para controlar la continuación del bucle
continuar_ingresando = True

while continuar_ingresando:
    numero = float(input("Introduce un número (introduce un número negativo para dejar de agregar): "))

    if numero >= 0:
        # Agrega el número a la lista si es no negativo
        lista_numeros.append(numero)
    else:
        # Cambia la bandera para salir del bucle si se introduce un número negativo
        continuar_ingresando = False

# Muestra la lista completa
print("Lista de números:", lista_numeros)
