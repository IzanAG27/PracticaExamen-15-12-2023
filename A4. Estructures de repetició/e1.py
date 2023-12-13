
num = int(input("Introdueix un número: "))

factorial = 1  # Inicialitzem el factorial a 1

# Calculem el factorial
for x in range(1, num + 1):
    factorial *= x

print("El factorial de {} és: {}".format(num, factorial))


