import kernel


def main():
    opcion = kernel.escoger_opcion()
    kernel.ejecutar_opcion(opcion)


if __name__ == "__main__":
    main()