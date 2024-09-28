"""Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)."""

#Pregunta al usuario
edad = int(input("Cuantos años tienes?: "))
print("Osea has cumplidos: ")
for i in range(1,edad):
    if i > 0 and i <= edad:
        print(f"has cumplidos: {i}")
