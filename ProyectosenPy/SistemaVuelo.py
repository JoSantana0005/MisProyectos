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
        cent = input("Desea agregar asientos al vuelo (s/n): ")
        while cent.lower() == "s":
            asiento = input("Ingrese el asiento que quiera agregar al vuelo: ")
            if asiento in self.asientos:
                print("El asiento ya encuentra en la lista agregue otro")
            else:
                self.asientos.append(asiento)
            cent = input("Desea agregar asientos al vuelo (s/n): ")
        lista = self.asientos
        return lista
    #Funcion que muestra los asientos disponibles
    def mostrar_asientos(self):
        print("Asientos disponibles del vuelo")
        for i in range(0,len(self.asientos)):
            print(self.asientos[i])

vuelo = Vuelo(1432,"España","Dubai", datetime.strptime("2024-12-04", "%Y-%m-%d"))
asientosD = vuelo.agregar_asiento()
vuelo.mostrar_asientos()
    


        