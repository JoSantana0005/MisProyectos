from datetime import datetime
#Gestion de Vehiculo
class Vehiculo:
    def __init__(self,marca: str,modelo: str,añoFabrcacion,kilometraje: float):
        self.marca = marca
        self.modelo = modelo
        self.añoF = añoFabrcacion
        self.kilo = kilometraje
    
    #Getters
    def getMarca(self):
        return self.marca
    def getModelo(self):
        return self.modelo
    def getAñoF(self):
        return self.añoF
    def getKilometraje(self):
        return self.kilo
    
    #Setters
    def setMarca(self,marca):
        self.marca = marca
    def setModelo(self,modelo):
        self.modelo = modelo
    def setAñoF(self,añoF):
        self.añoF = añoF
    def setKilometraja(self,kilo):
        self.kilo = kilo

class Automovil:
    def __init__(self,numeroP: int,tipoC: str,capacidadM: float):
        self.numeroP = numeroP
        self.tipoC = tipoC
        self.capacidad = capacidadM
        self.carros = {}
    
    #Funcion que agrega los detalles del automovil en un diccionario
    def agregar_vehiculo(self):
        cent = input("Desea agregar un detalle al automovil (s/n): ")
        while cent.lower() == "s":
            try:
                detalle = input("Ingrese el detalle que quiere agregar al vehiculo: ")
                tipoDetalle = input("Diga el detalle que quiere detallar (numerop-tipoc-capacidad): ")
                if(tipoDetalle.lower() == "tipoc"):
                    self.carros[detalle] = self.tipoC
                elif(tipoDetalle.lower() == "numerop"):
                    self.carros[detalle] = self.numeroP
                elif(tipoDetalle.lower() == "capacidad"):
                    self.carros[detalle] = self.capacidad
                else:
                    raise ValueError("Ingrese un mal un dato a la hora de colocar el detalle o el tipo de detalle")
            except ValueError as error:
                print(f"Error {error}")
            except Exception as error:
                print(f"Error {error}")
            cent = input("Desea agregar un detalle al automovil (s/n): ")
        carros = self.carros
        return carros
    #Funcion que elimina un detalle del automovil en un diccionario
    def eliminar_vehiculo(self,carros: dict):
        clave = input("Ingrese el detalle que quiere eliminar: ")
        if clave in carros:
            del carros[clave]
        else:
            print("No se encuentra ningun detalle que se pueda eliminar")

        print("Actualizacion de los detalles del carro")
        print(carros)
    
    #Funcion que modifica un detalle del automovil en un diccionario
    def Modifcar_vehiculo(self,carros: dict):
        claves_validas = ["numero de puertas", "tipo de combustible", "capacidad del motor"]
        tipo = {"numero de puertas": int, "tipo de combustible": str, "capacidad del motor": float }
        clave = input("Ingrese el detalle que quiere modifcar: ")
        if clave in claves_validas:
            tipo = tipo[clave]
            valordetalle = tipo(input(f"Ingrese el nuevo detalle de la clave {clave}: "))
            carros[clave] = valordetalle
        else:
            raise ValueError(f"No es un valor valido para la clave: {clave}")
        print("Actualizacion de los vehciulos")
        print(carros)
    
    #Funcion que muestra los detalles del vehiculo
    def mostrar_detalle(self):
        print("Detalles del vehiculo")
        for key,item in self.carros.items():
            print(key,item)
    
    #Funcion que calcula el coste del mantenimiento del vehiculo
    def coste_mantenimiento(self):
        costo_base = 160
        costo_puerta = 20
        costo_capacidad = 1.5
        return costo_base + ((costo_puerta*self.numeroP) + (costo_capacidad*self.capacidad))


class Camion:
    def __init__(self,capacidadC: int,tipocarga: str,tamaño: float):
        self.capacidadC = capacidadC
        self.tipoC = tipocarga
        self.tamaño = tamaño
        self.camion = {}
    
    #Funcion que agrega los detalles de un camion a un diccionario
    def agregar_camion(self):
        cent = input("Desea agregar detalle al camion (s/n): ")
        while cent.lower() == "s":
            try:
                detalle = input("Ingrese el detalle del camion: ")
                tipoDetalle = input("Ingrese el tipo de detalle del camion (capacidadC-tipocarga-tamaño): ")
                if (tipoDetalle.lower() == "capacidadC"):
                    self.camion[detalle] = self.capacidadC
                elif (tipoDetalle.lower() == "tipocarga"):
                    self.camion[detalle] = self.tipoC
                elif(tipoDetalle.lower() == "tamaño"):
                    self.camion[detalle] = self.tamaño
                else:
                    raise ValueError("Tiene que ingresar bien los detalles y los tipos de detalles")
            
            except ValueError as error:
                print(f"Error: {error}")
            except Exception as error:
                print(f"Error: {error}")
            cent = input("Desea agregar detalle al camion (s/n): ")
        
        camiones = self.camion
        return camiones
    #Funcion que elimina un detalle de un camion en un diccionario
    def eliminar_camion(self,camion: dict):
        clave_validas = ["capacidad de carga", "tipo de carga", "tamaño"]
        clave = input("Ingrese el detalle del camion que quiere eliminar: ")
        if clave in clave_validas:
            del camion[clave]
        else:
            raise ValueError("Tiene que colocar un detalle valido para poder eliminarlo")
        print("Actualizacion de los detalles del camion")
        print(camion)
    
    #Funcion que modifica un detalle de un camion en un diccionario
    def Modificar_camion(self,camion: dict):
        clave_validas = ["capacidad de carga", "tipo de carga", "tamaño"]
        tipo = {"capacidad de carga": int, "tipo de carga": str, "tamaño": float}
        clave = input("Ingrese el detalle del camion que quiere modifcar: ")
        if clave in clave_validas:
            tipo = tipo[clave]
            valor = tipo(input("Ingrese el nuevo valor del detalle: "))
            camion[clave] = valor
        else:
            raise ValueError("Tiene que ingresar una clave valida para poder modifcar el valor")
        
        print("Actualizacion de los detalles del camion")
        print(camion)
    
    #Funcion que muestra los detalles del camion en un diccionario
    def mostrar_detalleCami(self):
        print("Detalles del camion")
        for key,item in self.camion.items():
            print(key,item)
        
    #Funcion que calcula el coste del mantemiento del camion
    def coste_mantenimiento(self):
        coste_base = 400
        coste_tamaño = 1.5
        if(self.tipoC == "Pesada"):
            coste_capacidad = 200
            return coste_base + ((coste_capacidad*self.capacidadC) + (coste_tamaño*self.tamaño))
        elif(self.tipoC == "Ligera"):
            coste_capacidad = 100
            return coste_base +((coste_capacidad*self.capacidadC) + (coste_tamaño*self.tamaño))
        else:
            raise ValueError("Tiene que ingresar pesado o ligero para poder calcular el coste")
class Vehiculos(Vehiculo):
    def __init__(self, marca: str, modelo: str, añoFabrcacion, kilometraje: float):
        super().__init__(marca, modelo, añoFabrcacion, kilometraje)
    
    #Funcion que muestra los carros con sus detalles,marca,etc
    def mostrar_vehiculo(self,carros:dict,precioCa:float):
        print("Automovil")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año de fabricación: {self.añoF}")
        print(f"Kilometraje: {self.kilo}")
        print("Detalles del carro")
        for key,item in carros.items():
            print(key,item)
        print(f"El precio del coste de mantenimiento: {precioCa}")
    
    #Funcion que muestra los camiones con sus detalles,marca,etc
    def mostrar_camiones(self, camiones: dict, precioCami: float):
        print("Camión")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año de Fabricación: {self.añoF}")
        print(f"Kilometraje: {self.kilo}")
        print("Detalles del camion: ")
        for key,item in camiones.items():
            print(key,item)
        print(f"El precio del coste de mantenimiento: {precioCami}")


def main():
    cent = input("Desea listar un carro o camion en el sistema? (s/n): ")
    while cent.lower() == "s":
        print("Sistema de gestion de carros y camiones")
        print("1.Carro")
        print("2.Camión")
        opc = int(input("Ingrese una opcion: "))
        if(opc == 1):
            numeroP = int(input("Ingrese el numero de puertas del carro: "))
            tipoCa = input("Ingrese el tipo de combustible deol carro: ")
            capacidad = float(input("Ingrese la capacidad del motor del carro: "))
            deta = Automovil(numeroP,tipoCa,capacidad)
            carro = deta.agregar_vehiculo()

            eliminar = input("Desea eliminar un detalle del vehiculo (s/n): ")
            while eliminar.lower() == "s":
                deta.eliminar_vehiculo(carro)
                eliminar = input("Desea eliminar un detalle del vehiculo (s/n): ")
            
            modificar = input("Desea modifcar un detalle del carro (s/n): ")
            while modificar.lower() == "s":
                deta.Modifcar_vehiculo(carro)
                modificar = input("Desea modifcar un detalle del carro (s/n): ")
            
            precioMant = deta.coste_mantenimiento()

            marca = input("Ingrese la marca del carro: ")
            modelo = input("Ingrese el modelo del carro: ")
            año = datetime.strptime(input("Ingrese el año de fabricacion: "), "%Y")
            kilometraje = float(input("Ingrese el kilometraje del carro: "))
            vehi = Vehiculos(marca,modelo,año,kilometraje)
            vehi.mostrar_vehiculo(carro,precioMant)
        elif(opc == 2):
            capacidadC = int(input("Ingrese la capacidad de carga que tiene el camion: "))
            tipoC = input("Ingrese el tipo de carga del camion (pesada o ligera): ")
            tam = input("Ingrese el tamaño del camion: ")
            detaC = Camion(capacidadC,tipoC,tam)
            camion = detaC.agregar_camion()

            eliminarC = input("Desea eliminar un detalle del camion (s/n): ")
            while eliminarC.lower() == "s":
                detaC.eliminar_camion(camion)
                eliminarC = input("Desea eliminar un detalle del camion (s/n): ")
            
            modifciarC = input("Desea modificar un detalle del camion (s/n):  ")
            while modifciarC.lower() == "s":
                detaC.Modificar_camion(camion)
                modifciarC = input("Desea modificar un detalle del camion (s/n):  ")
            
            precioCam  = detaC.coste_mantenimiento()

            marcaC = input("Ingrese la marca del camión: ")
            modeloC = input("Ingrese el modelo del camión: ")
            añoC = datetime.strptime(input("Ingrese el año de fabricacion: "), "%Y")
            kilometrajeC = float(input("Ingrese el kilometraje del camión: "))
            cami = Vehiculos(marcaC,modeloC,añoC,kilometrajeC)
            cami.mostrar_camiones(camion,precioCam)
        else:
            print("Tiene que ingresar de acuerdo a las opciones que se le dan")
        cent = input("Desea listar un carro o camion en el sistema? (s/n): ")


system = main()          
            

            

                
        

        
