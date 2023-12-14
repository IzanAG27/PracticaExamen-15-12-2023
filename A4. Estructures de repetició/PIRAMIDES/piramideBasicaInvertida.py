
num = int(input(""))

for x in range(1, num + 1):
    for i in range(1, x + 1):
        print(x,end=" ")
    print()

for x in range(x - 1, 0, -1):
    for i in range(1, x + 1):
        print(x, end=" ")
    print()