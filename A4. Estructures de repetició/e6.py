"""
Realitza un programa que mostri la taula
de multiplicar d'un número introduït per teclat.
"""

try:
    num = int(input(""))
    for x in range(1,10):
        print(x,"*",num,"=",x*num)
except ValueError:
    print("Introduce bien los datos")
finally:
    print("Programa terminado")