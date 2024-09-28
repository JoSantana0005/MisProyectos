"""Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión."""
cantidad = float(input("La cantidad a invertir: "))
interes = float(input("Ingrese el interes anual: "))
años = int(input("Años: "))
for i in range(años):
    cantidad *= (1 + interes)/100
    print(f"La inversion {i + 1} es: {cantidad}")
