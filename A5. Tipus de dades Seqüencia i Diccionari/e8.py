# Inicializa las listas para almacenar nombres y edades
nombres = []
edades = []

# Variable para indicar si se debe continuar la entrada de datos
continuar = True

# Lee nombres y edades hasta que se introduzca un asterisco o se alcance un límite
while continuar and len(nombres) < 10:
    nombre = input("Introduce el nombre del alumno (o * para terminar): ")

    # Verifica si se debe terminar la entrada de datos
    if nombre == '*':
        continuar = False
    else:
        # Lee la edad del alumno
        edad = int(input(f"Introduce la edad de {nombre}: "))

        # Almacena el nombre y la edad en las listas correspondientes
        nombres.append(nombre)
        edades.append(edad)

# Muestra los alumnos mayores de edad
print("\nAlumnos mayores de edad:")
for i in range(len(nombres)):
    if edades[i] >= 18:
        print(f"{nombres[i]} - {edades[i]} años")

# Encuentra la edad máxima
edad_maxima = max(edades)

# Muestra los alumnos más viejos
print("\nAlumnos más viejos:")
for i in range(len(nombres)):
    if edades[i] == edad_maxima:
        print(f"{nombres[i]} - {edades[i]} años")
