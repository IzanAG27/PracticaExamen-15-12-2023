
limite_superior = int(input("Introduce un número superior: "))

print("Números primos entre 2 y", limite_superior, "son:")

for num in range(2, limite_superior + 1):
    es_primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            es_primo = False
    if es_primo and num != 1:
        print(num)