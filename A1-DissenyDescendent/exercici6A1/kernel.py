"""
Dissenyeu dues funcions, calcularArea i calcularPerimetre,
que calculin respectivament l'àrea i el perímetre d'una circumferència.
Les funcions reben un paràmetre, radi, que és un nombre que pot tenir decimals.
Utilitza aquesta funció en un programa que llegeixi el radi d'una circumferència
i en mostri l'àrea i el perímetre.
"""

import math


def calcularArea(radi):
    return math.pi * math.pow(radi, 2)


def calcularPerimetre(radi):
    return 2 * math.pi * radi
