from datetime import datetime
#Sistema de vuelos
class Vuelo:
    def __init__(self,numeroV: int,origen: str,destino: str,horadesalida: str):
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
        return self.asientos
        
    #Funcion que muestra los asientos disponibles
    def mostrar_asientos(self):
        print("Asientos disponibles del vuelo")
        print(" ".join(self.asientos))

class Pasajero:
    def __init__(self,nombre: str,numeroI: int):
        self.nombre = nombre
        self.numeroIde = numeroI
        self.asientoR = []
    
    #Funcion que reserva un asiento
    def reservar_asiento(self,asientos: list):
        cent = input("Desea reservar un asiento? (s/n): ")
        while cent.lower() == "s":
            if not asientos:
                print("Todos los asientos esta ocupados, lo sentimos")
                break
            reserva = input("Introduzca el asiento que quiere reservar: ").upper()
            if reserva in asientos:
                asientos.remove(reserva)
                self.asientoR.append(reserva)
                print(f"El asiento {reserva} fue reservado por {self.nombre}")  
            
            else:
                print(f"El asiento {reserva} ya se encuentra reservado")
                continue
            cent = input("Desea reservar un asiento? (s/n): ")
        lista = self.asientoR
        return lista
    
    #Funcion que cancelar la reservacion de un asiento
    def cancelar_reservacion(self,asientos: list):
        cent = input("Desea cancelar un asiento? (s/n): ")
        while cent.lower() == "s":
            cancelar = input("Introduzca el asiento que quiere cancelar: ")
            if cancelar in self.asientoR:
                asientos.append(cancelar)
                self.asientoR.remove(cancelar)
                print(f"El asiento {cancelar} fue cancelado por {self.nombre}")
            else:
                print(f"El asiento {cancelar} no se encuentra en los asientos reservados vuelva a intentar")
                cent = input("Desea reservar un asiento? (s/n): ")
        
        print("Actualizacion de los asientos reservados")
        print(self.asientoR)
    
    #Funcion que muestra los asientos reservados por la persona
    def mostrar_reservados(self):
        print(f"Asientos reservados de: {self.nombre} y su identificación es: {self.numeroIde}")
        print(" ".join(self.asientoR))

class Asientos(Vuelo):
    def __init__(self, numeroV: int, origen: str, destino: str, horadesalida: datetime):
        super().__init__(numeroV, origen, destino, horadesalida)
        
    
    #Mostra vuelo
    def mostrar_vuelo(self,asientosR,nombre,numeroIde):
        print("\n")
        print(f"El vuelo sale {self.hora} , parte desde {self.origen} y llega {self.destino}")
        print(f"El numero del vuelo es {self.numeroV}")
        print("Sus datos y asientos que reservo")
        print(f"Nombre del pasajero: {nombre}")
        print(f"Numero de identififcación: {numeroIde}")
        print(f"Sus asientos son: {" ".join(asientosR)}")
    
    
def main():
    vuelo = Vuelo(0,"","", "")
    asientos = vuelo.agregar_asiento()
    vuelo.mostrar_asientos()
    numeroVuelo = int(input("Ingrese el numero de vuelo: "))
    origen = input("Ingrese de donde parte el vuelo: ")
    destino = input("Ingrese el destino del vuelo: ")
    fechaVuelo = input("Ingrese la fecha del vuelo (YYYY-MM-DD): ")
    fecha = datetime.strptime(fechaVuelo,"%Y-%m-%d")
    vuen = Asientos(numeroVuelo,origen,destino,fecha)
    cent = input("Desea reservar un vuelo? (s/n): ")
    while cent.lower() == "s":
        nombre = input("Ingrese su nombre: ")
        numerodeIden = int(input("Ingrese su numero de identificación: "))
        pasajero = Pasajero(nombre,numerodeIden)
        asientoR = []
        asientorese = pasajero.reservar_asiento(asientos) #Reserva los asientos
        asientoR.extend(asientorese)
        cancelar = input("Desea cancelar la reservacion de un asiento (s/n): ")
        while cancelar.lower() == "s":
            pasajero.cancelar_reservacion(asientos) #Cancela la reserva
            cancelar = input("Desea cancelar la reservacion de un asiento (s/n): ")

        vuen.mostrar_vuelo(asientoR,nombre,numerodeIden)
        cent = input("Desea reservar un vuelo? (s/n): ")

system = main()








    


        