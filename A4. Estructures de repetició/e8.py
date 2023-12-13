"""
Implementa un programa que demani dos números:
un serà el límit inferior d’un interval i l’altre el límit superior.
Si el límit inferior és més gran que el superior ho ha de tornar a demanar.
A continuació el programa demanarà per teclat números fins que
introduïm el 0. Quan acabi el programa donarà la informació següent:
La suma dels números que estan dins de l'interval SENSE ser cap dels
valors indicats com a límit inferior o límit superior  (interval obert)
Quants números són fora de l'interval.
Informar de si hem introduït algun número que sigui
igual al límit inferior o al límit superior de l'interval, o no.
"""
comprobar = True
while comprobar:
    nums = input("").split()
    numInferior = int(nums[0])
    numSuperior = int(nums[1])
    if numInferior > numSuperior:
        print("Introduce un valor inferior más pequeño que el superior")
    else:
        n = input("").split()

