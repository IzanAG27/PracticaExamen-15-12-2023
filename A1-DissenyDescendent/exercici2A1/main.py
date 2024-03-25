import kernel


def main():
    num1, num2 = kernel.pedir_numeros()
    kernel.comprobar_multiplo(num1, num2)


if __name__ == "__main__":
    main()
