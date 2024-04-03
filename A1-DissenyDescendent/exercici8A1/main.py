import kernel


def main():
    n = int(input("Introduce un número entero no negativo: "))
    factorial_no_recursivo = kernel.factorial_no_recursivo(n)
    factorial_recursivo = kernel.factorial_recursivo(n)
    print("El factorial (no recursivo) de", n, "es:", factorial_no_recursivo)
    print("El factorial (recursivo) de", n, "es:", factorial_recursivo)


if __name__ == "__main__":
    main()
