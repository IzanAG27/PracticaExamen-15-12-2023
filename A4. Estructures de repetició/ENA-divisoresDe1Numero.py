"""
Programa que demana un número a l'usuari i mostra per pantalla els seus divisors.
"""
numero = int(input("Introduce un número: "))

print(f"Los divisores de {numero} son:")

for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)
