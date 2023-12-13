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

num = int(input(""))

for x in range (num):
    print("#", end="")
print()

for x in range(num - 2):
    print("#" + " " * (num - 2) + "#")

#Última linea
for x in range (num):
    print("#", end="")