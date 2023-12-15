"""
Izan Arnaiz Gallego
Piramide Básica Con espacios en medio
"""

n = int(input(""))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print(i, end=" ")
        else:
            print(" ", end=" ")
    print("")
for i in range(n - 1, 0, -1):
    for j in range(1, i + 1):
        if i == n or j == 1 or j == i:
            print(i, end=" ")
        else:
            print(" ", end=" ")
    print("")
