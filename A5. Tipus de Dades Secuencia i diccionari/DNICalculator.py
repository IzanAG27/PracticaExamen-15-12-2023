try:
    dniLetter = {
        0: "T", 1: "R", 2: "W", 3: "A", 4: "G", 5: "M", 6: "Y", 7: "F", 8: "P", 9: "D", 10: "X", 11: "B", 12: "N", 13: "J", 14: "Z", 15: "S", 16: "Q", 17: "V", 18: "H", 19: "L", 20: "C", 21: "K", 22: "E"
    }
    numeroDNI = input("")
    cont = 0
    if len(numeroDNI) == 8:
        cont = int(numeroDNI) % 23
        print(dniLetter[cont])
    else:
        print("ERROR!, Exactamente 8 números")
except ValueError:
    print("Has introducido mal los valores")
finally:
    print("Programa terminado")