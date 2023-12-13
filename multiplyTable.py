"""
Volem mostrar per pantalla les taules de multiplicar.
L'usuari introdueix un enter
Mostrar per pantalla la taula de multiplicar del número introduït:
Input:
3
Output:
1 * 3 = 3
2 * 3 = 6
3 * 3 = 9
4 * 3 = 12
5 * 3 = 15
6 * 3 = 18
7 * 3 = 21
8 * 3 = 24
9 * 3 = 27
"""
num = int(input(""))
for i in range(1, 10):
    print(i, "*", num, "=", i * num)