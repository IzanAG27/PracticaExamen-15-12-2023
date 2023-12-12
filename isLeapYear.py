comprobar = True
import time
while comprobar == True:
    time = input("").split()
    hora = int(time[0])
    minuto = int(time[1])
    segundo = int(time[2])
    segundo += 1
    if segundo == 60:
        segundo = 0
        minuto += 1
        if minuto == 60:
            minuto = 0
            hora += 1
            if hora == 60:
                hora = 0
    print(hora,":",minuto,":",segundo)