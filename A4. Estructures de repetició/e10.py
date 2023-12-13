"""
Escriu un programa
que mostri la taula de multiplicar dels números 1,2,3,4 i 5.
"""

for primerNum in range(1,6):
    for segundoNum in range(1,11):
        print(f"{primerNum}x{segundoNum}={primerNum*segundoNum}")
    print()
