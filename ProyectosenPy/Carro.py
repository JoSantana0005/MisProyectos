class Carro:
    #Constructor
    def __init__(self,color,marca,modelo,ve) -> None:
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.ve = ve
    #Getters

    def getColor(self):
        return self.color
    
    def getMarca(self):
        return self.marca
    
    def getModelo(self):
        return self.modelo
    
    def getVelo(self):
        return self.ve
    
    #Setters

    def setColor(self,color):
        self.color = color

    def setMarca(self,marca):
        self.marca = marca
    
    def setModelo(self,modelo):
        self.modelo = modelo
    
    def setVelo(self,ve):
        self.ve = ve
    
    #Funciones

    def acelerar(self):
        self.ve += 10
    def frenar(self):
        self.ve -= 10
    def mostrar(self):
        print("Modelo    Marca     Color    Velocidad")
        print("{0:<10} {1:^10} {2:^10} {3:^10}".format(self.modelo,self.marca,self.color,self.ve),end ="")

#Principal

color = input("Ingrese el color del carro: ")
marca = input("Ingrese la marca del carro: ")
modelo = input("Ingrese el modelo del carro: ")
veloc = float(input("Ingrese la velocidad del carro"))


car = Carro(color,marca,modelo,veloc)
car.frenar()
car.mostrar()

