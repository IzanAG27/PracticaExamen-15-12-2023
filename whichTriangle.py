"""
Llegeix els valors de la llargada de tres segments i escriu si poden formar o no un triangle.
Imprimeix No és un triangle, equilàter (tres costats iguals),
isòsceles (dos costats iguals) o escalè (tots els costats diferents)
segons els valors introduïts
"""

l1 = int(input(""))
l2 = int(input(""))
l3 = int(input(""))

if l1 == l2 and l1 == l3:
    print("Es un triangulo equilater")
elif l1 == l2 and l1 != l3 or l1 != l2 and l1 == l3:
    print("Es un triangulo Isosceles")
elif l1 != l2 and l1 != l3:
    print("Es un traingulo escalè")