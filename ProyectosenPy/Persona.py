import math
import random
class Persona:
    def __init__(self, nombre: str, edad: int, dni:str, sexo: str, peso: float, altura: float):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
    
    #Getters
    def getNombre(self):
        return self.nombre
    
    def getEdad(self):
        return self.edad
    
    def getDni(self):
        return self.dni
    
    def getSexo(self):
        return self.sexo
    
    def getPeso(self):
        return self.peso
    
    def getAltura(self):
        return self.altura
    
    #Setters
    def setNombre(self,nombre):
        self.nombre = nombre
    
    def setEdad(self,edad):
        self.edad = edad
    
    def setDni(self,dni):
        self.dni = dni
    
    def setSexo(self,sexo):
        self.sexo = sexo
    
    def setPeso(self,peso):
        self.peso = peso
    
    def setAltura(self,altura):
        self.altura = altura
    
    #Funciones

    #Calculo del peso de la persona
    def ClaculoMC(self):
        ideal = 0
        pesoActual = self.peso/math.pow(self.altura,2)
        print(pesoActual)
        if(pesoActual < 20):
            ideal = -1
            return ideal
        elif(pesoActual >= 20 and pesoActual <= 25):
            return ideal
        else:
            ideal = 1
            return ideal
    #Comparar sexo
    def comparar__sexo(self):
        if(self.sexo.lower() == "h" or self.sexo.lower() == "m"):
            print("Introdujo los datos correctos para el sexo")
        else:
            raise ValueError("Introdujo los datos incorrectos de sexo")
    
    def mostrar__datos(self):
        print("Datos de la persona")
        print("Nombre      edad      dni       sexo (h/m)     peso      altura")
        print("{0:^10s} {1:^10d} {2:^10s} {3:^10s} {4:^10.2f} {5:^10.2f}".format(self.nombre,self.edad,
                                                                                 self.dni,self.sexo,self.peso,self.altura))
    
def main():
    try:
        nombre = input("Ingrese el nombre de la persona: ")
        edad = int(input("Ingrese la edad de la persona: "))
        dni = str(random.randint(10000000,99999999))
        sexo = input("Ingrese el sexo de la persona: ")
        peso = float(input("Ingrese el peso de la persona: "))
        altura = float(input("Ingrese la altura de la persona: "))
        persona = Persona(nombre,edad,dni,sexo,peso,altura)
        result = persona.ClaculoMC()
        if(result == -1):
            print("Esta en su peso ideal")
        elif(result == 0):
            print("Esta por debajo de su peso ideal")
        else:
            print("Tiene sobrepeso")
        persona.mostrar__datos()
    except:
        raise ValueError("Error: error de dato")
system = main()
