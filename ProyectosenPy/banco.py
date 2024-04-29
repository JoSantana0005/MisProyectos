class Cuenta:
    #Constructor
    def __init__(self,cuenta = str,saldo = int,numCuen = str):
        self.cuenta = cuenta
        self.saldo = saldo
        self.numCuen = numCuen
    #Getters
    def getCuenta(self):
        return self.cuenta
    
    def getSaldo(self):
        return self.saldo
    
    def getNumCuen(self):
        return self.numCuen
    
    #Setters
    def setCuenta(self,cuenta):
        self.cuenta = cuenta

    def setSaldo(self,saldo):
        self.saldo = saldo
    
    def setNumCuen(self,numCuen):
        self.numCuen= numCuen
    
    #Funciones
    def Ingresar(self):
        ing = int(input("Ponga la cantidad a ingresar: "))
        self.saldo = self.saldo + ing
        print("Se agrego dinero a la cuenta de: ", self.cuenta, " su numero de cuenta es: ",
             self.numCuen, " se ingreso ", ing, " ahora tienes: ", self.saldo )

    def retirar(self):
        reti = int(input("Ponga la cantidad a retirar: "))
        if(reti > self.saldo):
            print("La cantidad que quieres retirar no tienes el suficiente saldo para realizar el retiro")
        else:
            print("Se retiro dinero a la cuenta de: ", self.cuenta, " su numero de cuenta es: ",
             self.numCuen, " se retiro: ", reti, " y te quedo: ", (self.saldo - reti)  )

#Principal

cuenta = input("Ingrese el nombre de la cuenta: ")
numC = input("Ingrese el numero de cuenta: ")
saldo = int(input("Ingrese el saldo que tiene la cuenta: "))

clien1 = Cuenta(cuenta,saldo,numC)
clien1.Ingresar()
clien1.retirar()
        