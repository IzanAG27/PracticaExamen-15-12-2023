"""
Programa que mostra un triangle amb nombres a les cantonades.
Cal demanar quina alçada ha de tenir el triangle. Els valors permesos per a l'alçada son entre 2 i 9. (ambdós inclosos)
INPUT
Alçada del triangle: 5
OUTPUT
1
2 2
3   3
4     4
5 5 5 5 5
"""
num = int(input("Alçada del triangle: "))

for i in range(1, num + 1):
    if i == 1 or i == num: # Imprimir primera fila y última fila del triangulo
        print(f"{i} " * i)
    else: # Imprimir primer número y ultimo de la fila y dejar espacios por medio.
        print(f"{i}{' ' * (2 * (i - 1) - 1)}{i}")
