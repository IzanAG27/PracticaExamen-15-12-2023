import kernel


def main():
    a = int(input("Introduce el primer número entero: "))
    b = int(input("Introduce el segundo número entero: "))
    mcd_no_recursivo = kernel.mcd_no_recursivo(a, b)
    mcd_recursivo = kernel.mcd_recursivo(a, b)
    print("El MCD (no recursivo) de", a, "y", b, "es:", mcd_no_recursivo)
    print("El MCD (recursivo) de", a, "y", b, "es:", mcd_recursivo)


if __name__ == "__main__":
    main()
