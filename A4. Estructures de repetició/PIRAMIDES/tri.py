a = int(input(""))

for i in range(1, a + 1):
    for j in range(1, i + 1):
        if i == a or j == i or j == 1:
            print(i, end=" ")
        else:
            print(' ', end=" ")
    print()