num = int(input(""))

for x in range(num + 1):
    print("#", end="")
print()

for x in range(num - 2):
    print("#\n", end="")
    for y in range(num - 2, -1):
        print("#\n", end="")

for x in range(num + 1):
    print("#", end="")