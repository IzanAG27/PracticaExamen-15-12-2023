"""
Mostrar per pantalla un quadrat de mida N (la triarà l'usuari)
Cal "printar"  #  a les vores. És a dir, dalt, baix dreta i esquerra
Cal fer servir estructures de repetició, per fer servir la mínima quantitat possible de sentències print
input
5
output
#####
#   #
#   #
#   #
#####
"""

#Primera línea
num = 7
for x in range (num):
    print("#", end="")
print()


# Líneas internas
for x in range(num - 2):
    print("#", end="")
    for y in range(num - 2):
        print(" ", end="")
    print("#")

#Última linea
for x in range (num):
    print("#", end="")

