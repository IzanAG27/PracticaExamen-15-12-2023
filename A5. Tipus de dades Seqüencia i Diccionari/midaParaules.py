# Crear una variable per emmagatzemar 666 paraules
paraules = [''] * 666
# Mostrar tot el contingut de la variable
print("Contingut inicial:")
# Omplir-la pel teclat amb paraules fins que es introdueixi "\q"
max_llargada = 0
index = 0
continuar_introduint = True
while index < len(paraules) and continuar_introduint:
    paraula = input("Introdueix una paraula (o '\\q' per sortir): ")
    if paraula == "\\q":
        continuar_introduint = False
    else:
        paraules[index] = paraula
        # Actualitzar la longitud màxima
        if len(paraula) > max_llargada:
            max_llargada = len(paraula)
        index += 1
# Mostrar la longitud màxima de les paraules introduïdes
print("La longitud màxima de les paraules introduïdes és:", max_llargada)
# Crear una tupla amb les paraules i les seves longituds
tupla_paraules_mides = tuple((paraula, len(paraula)) for paraula in paraules if paraula)
# Mostrar la tupla amb les paraules i mides corresponents
print("Tupla amb paraules i mides:")
print(tupla_paraules_mides)
