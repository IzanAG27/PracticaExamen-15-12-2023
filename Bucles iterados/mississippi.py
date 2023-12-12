"""
La teva tasca és molt simple aquí: escriu un programa que faci servir un bucle for per a "comptar de forma mississippi" fins a cinc. Havent comptat fins a cinc, el programa hauria d'imprimir en la pantalla el missatge final "Llest o no, aquí vaig!"
PISTA:
Fer servir el mètode sleep() per a aturar una estona "dormir" l'execució després de cada print() dins del cicle for durant un segon, de manera que el missatge enviat a la consola se sembli a un comptatge real.
Sortida esperada
1 Mississipí
2 Mississipí
3 Mississipí
4 Mississipí
5 Mississipí
"Llest o no, aquí vaig!"
"""


import time
paraula = "Mississippí"
cont = 1
for x in range(1, 5 + 1):
    print(cont,"",paraula)
    cont += 1
    time.sleep(1)
print("Llest o no, aquí vaig!")

