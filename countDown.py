"""
L'usuari introdueix un enter (N)
i es mostra per pantalla un compte enrere de N fins a 1.
Input
5
Output
54321
"""

num = int(input(""))

for x in range(num, 0, -1):
    print(x, end="")