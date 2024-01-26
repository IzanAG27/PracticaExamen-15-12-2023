

try:
    diesSetmana = ["dilluns", "dimarts", "dimecres", "dijous", "divendres", "dissabte", "diumenge"]
    diasSemana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sábado", "domingo"]
    daysOfWeek = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    numSemana = int(input(""))

    if numSemana > 0 and numSemana < 8:
        for num in range(1, 8):
            if numSemana == num:
                num -= 1
                print(diesSetmana[num])
                print(diasSemana[num])
                print(daysOfWeek[num])
    else:
        print("ERROR!, tiene que ser un numero entre 1 y 7")

except ValueError:
    print("\nHas introducido mal los valores")
finally:
    print("\nPrograma terminado")