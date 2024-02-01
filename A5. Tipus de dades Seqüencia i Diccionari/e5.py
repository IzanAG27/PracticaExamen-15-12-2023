import random

# Inicialitza la llista amb 10 nombres aleatoris de l'1 al 10
llista = [random.randint(1, 10) for _ in range(10)]

# Ordena la llista de menor a major
llista.sort()

# Mostra la llista ordenada
print("Llista ordenada:", llista)
