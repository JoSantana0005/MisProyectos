class Rectangulo:
    #Constructor
    def __init__(self,base = float,altura = float):
        self.base = base
        self.altura = altura

    #Getters
    def getBase(self):
        return self.base
    
    def getAltura(self):
        return self.altura

    #Setters
    def setBase(self,base):
        self.base = base   

    def setAltura(self,altura):
        self.altura = altura

    #Funciones

    def calculo_area(self):
        return self.base*self.altura    
    
    def calculo_peri(self):
        return (2*self.base) + (2*self.altura)

#   Principal

base = float(input("Ingrese la base del rectangulo: "))
alt = float(input("Ingrese la altura en rectangulo: "))

recta = Rectangulo(base,alt)

resultA = recta.calculo_area()
print("La area del recatangulo es: " + str(resultA))
resultP = recta.calculo_peri()
print("El perimetro del rectangulo es: " + str(resultP))
