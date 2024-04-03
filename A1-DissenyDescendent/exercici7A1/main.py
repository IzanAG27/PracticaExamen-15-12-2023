import kernel


def main():
    intents = 3
    while intents > 0:
        nomUsuari = input("\nIntroduce el nombre de usuario: ")
        contrasenya = input("Introduce la contraseña: ")
        login_correcto, intents = kernel.setLogin(nomUsuari, contrasenya, intents)
        if login_correcto:
            print("¡Bienvenido al sistema!")
            print(":-)")
            break
        else:
            print("Error: ¡Nombre de usuario o contraseña incorrecta!")
    if intents == 0:
        print("Error: ¡Se ha agotado el número de intentos!")


if __name__ == "__main__":
    main()
