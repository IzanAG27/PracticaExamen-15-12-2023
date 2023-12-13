"""
Una persona va adquirir un producte per pagar en 20 mesos.
El primer mes va pagar 10€, el segon 20€, el tercer 40€ i
així successivament (cada mes va pagar el doble que a l’anterior)
Realitzar un algorisme que mostri quant ha de pagar mensualment
i el total del qual ha de pagar després dels 20 mesos.
"""

try:
    totalImporte = 0
    Importe = 10
    for x in range(1, 21):
        Importe *= 2
    print(f"Has pagado {Importe} en total por los 20 meses.")
except ValueError:
    print("Introduce los valores correctamente")
finally:
    print("Programa terminado")
