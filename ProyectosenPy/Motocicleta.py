from datetime import datetime
class Motocicleta:
    def __init__(self,color,matricula,combustibleL,numero_ruedas,marca,
                 modelo,fecha_Fabricacion,velocidad_punta,peso,estado = False):
        
        self.color = color
        self.matricula = matricula
        self.combustibleL = combustibleL
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = datetime.today()
        self.velocidad_punta = velocidad_punta
        self.peso = peso
        self.estado = estado
    
    def arracar(self,condi):
        if(self.estado == False):
            print("El motor han arracando")
        elif(self.estado == True and condi == False):
            print("El motor ya esta en mancha")
    def detener(self,condi):
        if(self.estado == True):
            print("El motor se detuvo")
        elif(self.estado == False and condi == True):
            print("El motor ya se habia detenido")
    
    def esunamoto(self):
        if(self.numero_ruedas == 2):
            print("Es una moto normal")
        elif(self.numero_ruedas == 3):
            print("Es una moto de tres ruedas")
        else:
            print("No es una moto")

motor1 = Motocicleta("naranja","23569l",10,2,"toyota","Auto",datetime.now(),450,120,True)
motor2 = Motocicleta("Verde","3245768",0,3,"Chevorlet","sicro",datetime.now(),520,140,False)
motor1.arracar(False)
motor1.detener(True)
motor1.esunamoto()
motor2.arracar(False)
motor2.detener(True)
motor2.esunamoto()

        