"""
 Nombre: Izan Arnáiz Gallego
 Grupo: ASIXc1A M03
 Fecha: 15/12/2023
 Enunciado:
    Programa que demana a l'usuari les notes(sense decimals) d'11 alumnes.
    El programa ens dirà cuantes són suspeses i quantes aprovades, mostrant el seu conjunt de notes.
    Cal fer control d'errors.
    Exemple d'execució:
    Input:
    5 6 3 10 9 1 2 5 3 8 9
    Output:
    :( Suspesos: 4
    3, 1, 0, 3
    :) Aprovats:
    5, 6, 10, 9, 5, 8, 9
"""

# Pedimos las notas
notas = [int(nota) for nota in input("").split()]
# Listas de aprovados y suspendidos
aprovat = []
suspes = []

# Si la nota es mayor a 5 es aprovado, sino suspendido
for i in notas:
    if i >= 0 and i <= 10:
        if i >= 5 and i <= 10:
            aprovat.append(i)
        elif i < 5 and i >= 0:
            suspes.append(i)
    else:
        print("Introduce valores positivos entre 0 y 10")

print("Printea los valores")
print("· Total de notes: ")
print(f"--Han aprovat aquestes notes: \n{aprovat}")
print(f"--Han suspes aquestes notes: \n{suspes}")

# nota = [int(x) for x in input("").split()]
# for i in nota:
#
# notas =