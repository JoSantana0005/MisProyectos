from datetime import datetime
#Sistema de vuelos
class Vuelo:
    def __init__(self,numeroV: int,origen: str,destino: str,horadesalida: datetime):
        self.numeroV = numeroV
        self.origen = origen
        self.destino = destino
        self.hora = horadesalida
        self.asientos = []
    
    #Getters
    def getNumeroV(self):
        return self.numeroV
    def getOrigen(self):
        return self.origen
    def getDestino(self):
        return self.destino
    def getHora(self):
        return self.hora
    #Setters
    def setNumeroV(self,numeroV):
        self.numeroV = numeroV
    def setOrigen(self,origen):
        self.origen = origen
    def setDestino(self,destino):
        self.destino = destino
    def setHora(self,hora):
        self.hora = hora
    
    #Funcion que agrega asientos al vuelo:
    def agregar_asiento(self):
        pass


        