import kernel


def main():
    dia, mes, any = kernel.llegirData()
    dia_julia = kernel.calcularDiaJulia(dia, mes, any)
    print("El día juliano correspondiente es:", dia_julia)


if __name__ == "__main__":
    main()
