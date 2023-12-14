altura = int(input(""))

if altura >= 2 and altura <= 9:
    for i in range(1, altura + 1):
        for j in range(1, i + 1):
            if i == altura or j == 1 or j == i:
                print(i, end=' ')
            else:
                print(' ', end=' ')
        print()

