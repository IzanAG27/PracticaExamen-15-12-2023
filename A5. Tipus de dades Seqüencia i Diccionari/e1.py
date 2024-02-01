import random

# Inicialitza la llista amb 10 valors aleatoris (de l'1 al 10)
llista = [random.randint(1, 10) for x in range(10)]

# Mostra en pantalla cada nombre de la llista, el seu quadrat i el seu cub
for nombre in llista:
    quadrat = nombre ** 2
    cub = nombre ** 3
    print(f'Nombre: {nombre}, Quadrat: {quadrat}, Cub: {cub}')
