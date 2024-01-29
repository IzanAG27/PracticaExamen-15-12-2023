"""
    Noms: Daniel Arco, Izan Arnáiz.
    Grup: ASIXc1A
    Data: 22/01/2024
    Descripció:
    Lista de 100 nombres aleatorios entre 1 y 50 y después hacer una media de los nombres pares
    y después de los nombres impares.
"""
import random

# Generem una llista de 100 numeros aleatoris entre el 1 y el 50 cadascun.
nums = [random.randint(1,50) for x in range(100)]

sumaParell = 0
sumaSenar = 0
nombreParell = 0
nombreSenar = 0
listaPS = []
# Bucle del 0 al 99(100 Numeros)
for i in range(0, 99):
    if i % 2 == 0:
        sumaParell += nums[i]
        nombreParell += 1
        listaPS.append(nums[i])
    else:
        sumaSenar += nums[i]
        nombreSenar += 1
        listaPS.append(nums[i])

# Imprimim els parells i senars i els dividim per el nombre de Parells o Senars respectivament
print(f"Amb els nombres: {listaPS}")
print(f"mitjana posicions parelles: {sumaParell // nombreParell}.")
print(f"mitjana posicions senars: {sumaSenar // nombreSenar}.")