# Crear una variable para almacenar 666 palabras
LONGUITUD = 666
palabras = [''] * LONGUITUD
# Mostrar el contenido inicial de la variable
print("Contenido inicial:")
# Llenarla por teclado con palabras hasta que se introduzca "\q"
max_longitud = 0
indice = 0
continuar_introduciendo = True
print(palabras)
while indice < len(palabras) and continuar_introduciendo:
    palabra = input("Introduce una palabra (o '\\q' para salir): ")
    if palabra == "\\q":
        continuar_introduciendo = False
    else:
        palabras[indice] = palabra
        # Actualizar la longitud máxima
        if len(palabra) > max_longitud:
            max_longitud = len(palabra)
        indice += 1
print("La longitud máxima de las palabras introducidas es:", max_longitud)
tuplaLonguitud = tuple((palabra, len(palabra)) for palabra in palabras if palabra)
print("Tupla con palabras y longitudes:")
print(tuplaLonguitud)
