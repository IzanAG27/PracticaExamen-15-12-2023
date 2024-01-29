comprobar = True
tocado = ("0 2", "0 3", "0 4", "1 5", "1 6", "1 7")
suggestion = input("")
auxT = ""
auxA = ""

for x in tocado:
    if x == suggestion:
        auxT += x
        comprobar = False
    else:
        auxA += x
        comprobar = False
if auxT == suggestion:
    print("Tocado")
else:
    print("Agua")
