"""
Demana un enter a l'usuari, per saber quantes línies
Demana un enter a l'usuari, per saber quants punts
Imprimeix per pantalla tantes línies amb tants punts
com l'usuari hagi indicat
Input
4
10
Output
..........
..........
..........
..........
"""

nums = input("").split()

num1 = int(nums[0])
num2 = int(nums[1])
for x in range(num1 + 1):
    print(".", end=" ")
print()
for x in range(num2 - 2):
    print(".", end="")
    for i in range (num2 - 2):
        print(" ", end="")
    print(".")

for x in range(num1 + 1):
    print(".", end=" ")