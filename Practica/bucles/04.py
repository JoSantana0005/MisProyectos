"""Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas."""
numero = int(input("Ingrese un numero: "))
if numero > 0:
    for i in range(0,numero):
        cont = numero - i
        print(cont)
else:
    print("NUMERO NEGATIVO")