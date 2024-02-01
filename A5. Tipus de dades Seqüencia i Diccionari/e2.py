# Inicialitza la primera llista llegint 5 cadenes de caràcters per teclat
llista_original = []
for x in range(5):
    cadena = input("Introdueix una cadena de caràcters: ")
    llista_original.append(cadena)

# Copia els elements de la primera llista a una altra en ordre invers
llista_inversa = llista_original[::-1]

# Mostra els elements de la segona llista per pantalla
print("Llista Original:", llista_original)
print("Llista Inversa:", llista_inversa)
