def setLogin(nomUsuari, contrasenya, intents):
    if nomUsuari == "usuari1" and contrasenya == "asdasd":
        return True, intents
    else:
        intents -= 1
        print(f"Te quedan {intents} intentos.")
        return False, intents

