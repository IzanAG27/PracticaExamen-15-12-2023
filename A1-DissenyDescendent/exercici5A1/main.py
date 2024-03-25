import kernel


def main():
    nums = kernel.pedir_num()
    print(f"El numero máximo es: {kernel.calcularMax(nums)}")
    print(f"El numero mínimo es: {kernel.calcularMin(nums)}")


try:
    if __name__ == "__main__":
        main()
except ValueError:
    print("Tienen que ser numeros enteros")
