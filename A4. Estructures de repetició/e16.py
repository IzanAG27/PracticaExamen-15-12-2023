"""
Una empresa paga als seus empleats amb base en les hores treballades a la setmana. Escriu un programa que:
demani per teclat el nombre de treballadors de l’empresa i el sou per hora treballada
demani per cada treballador:
el nombre d’hores treballada a la setmana
mostri per pantalla el sou setmanal del treballador
mostri el total corresponent als sous pagats per l’empresa en una setmana
"""

trabajadores = int(input(""))
sueldoPorHora = int(input(""))
horasALaSemana = int(input(""))
print(f"Ganas a la semana {horasALaSemana * sueldoPorHora} euros.")
print(f"El dinero que se invierte en el sueldo de los trabajadores semanalmente es: {trabajadores *(horasALaSemana * sueldoPorHora)}")
