"""
Programa que demana un número a l'usuari i suma els seus dígits.
"""

num = str(input())
suma = 0
for digit in num:
    digit = int(digit)
    suma += digit
print(suma)

