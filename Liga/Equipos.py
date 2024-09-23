from liga import Liga
import random
class Equipos:
    def __init__(self,NombreEquipo: str, golesC: int, golesF: int, partidosG: int,
                 partidosE: int, partidosP: int):
        self.NombreEquipo = NombreEquipo
        self.GolesContra = golesC
        self.GolesFavor = golesF
        self.Ganados = partidosG
        self.empatados = partidosE
        self.perdidos = partidosP
        self.equipos = {}
    
    #Getters
    def getNombreEquipo(self):
        return self.NombreEquipo
    
    def getGolesContra(self):
        return self.GolesContra
    
    def getGolesFavor(self):
        return self.GolesFavor
    
    def getGanados(self):
        return self.Ganados
    
    def getEmpatados(self):
        return self.empatados
    
    def getPerdidos(self):
        return self.perdidos
    
    #Setters
    def setNombreEquipo(self,nombre):
        self.NombreEquipo = nombre
    
    def setGolesContra(self,goleeC):
        self.GolesContra = goleeC
    
    def setGolesFavor(self,golesF):
        self.GolesFavor = golesF
    
    def setGanados(self,Ganados):
        self.Ganados = Ganados

    def setEmpatados(self,Empatados):
        self.empatados = Empatados
    
    def setPerdidos(self,Perdidos):
        self.perdidos = Perdidos
    
    #Functions
    #Funcion que crear el equipo 
    def crear__dato(self):
        print(f"Nombre del equipo: {self.NombreEquipo}")
        print(f"Goles En contra: {self.GolesContra}")
        print(f"Goles a Favor: {self.GolesFavor}")
        print(f"Partidos Ganados: {self.Ganados}")
        print(f"Partidos Empatados: {self.empatados}")
        print(f"Partidos Perdidos: {self.perdidos}")
    
    #Function que agrega el equipo a su liga
    def agregar__dato(self, liga:dict, Equipos: list):
        self.equipos['Nombre del equipo'] = self.NombreEquipo
        self.equipos['Goles En contra'] = self.GolesContra
        self.equipos['Goles a Favor'] = self.GolesFavor
        self.equipos['Partidos Ganados'] = self.Ganados
        self.equipos['Partidos Empatados'] = self.empatados
        self.equipos['Partidos Perdidos'] = self.perdidos
        Equipos.append(self.equipos)
        liga['Equipos'] = Equipos
    
    #Function que elimina un equipo de la liga
    def eliminar__dato(self, ligas:list, Equipos: list):
        try:
            id = int(input("Ingrese el id de la liga: "))
            NombreEquipo = input("Ingrese el nombre del equipo que quiere eliminar: ")
            for liga in ligas:
                if(liga['ID'] == id):
                    for equipo in Equipos:
                        if(len(Equipos) == 0):
                            print("Ya no hay equipos en la liga")
                        else:
                            if(equipo['Nombre del equipo'] == NombreEquipo):
                                Equipos.remove(equipo)
                                print("Actualización de los equipos")
                                print(ligas)
                            else:
                                print("No se han encontrado el equipo a eliminar")
                else:
                    print("No se encontro el id")
        except:
            raise ValueError("Error: dato invalido")
    #Function que muestra los equipos
    def mostrar_dato(self):
        for x, y in self.equipos.items():
            print(x,y)

def main():
    ligas = []
    equipos = []
    id = 0
    while True:
        cent = input("Desea crear una liga? (s/n): ")
        while cent.lower() == "s":
            
            id += 1
            NombreLiga = input("Ingrese el nombre de la liga: ")
            PaisLiga = input("Ingrese el pais de la liga: ")
            NumeroPartidos = random.randrange(20,38)
            liga = Liga(id,NombreLiga,PaisLiga,NumeroPartidos)
            liga.create__data()
            agregar = input("Desesa agregar esta liga a la lista? (s/n): ")
            if (agregar.lower() == "s"):
                result = liga.add__data()
                ligas.append(result)
                print("Se agrego exitosamente")
            else:
                print("No se agrego la liga")
                break
            
            centEquipos = input("Desea crear los equipos de la liga? (s/n): ")
            while centEquipos.lower() == "s":
                
                NombreEquipo = input("Ingrese el nombre del equipo: ")
                GolesC = random.randint(1,100)
                GolesF = random.randint(1,100)
                Ganados = random.randrange(1,38)
                Empatados = random.randrange(1,38)
                Perdidos = random.randrange(1,38)
                equipo = Equipos(NombreEquipo,GolesC,GolesF,Ganados,Empatados,Perdidos)
                equipo.crear__dato()
                agregarEquipo = input("Desea agregar este equipo? (s/n): ")
                if(agregarEquipo.lower() == "s"):
                    equipo.agregar__dato(result,equipos)
                    print("Se agrego exitosamente")
                else:
                    
                    print("No se agrego el equipo a la liga")
                
                centEquipos = input("Desea crear los equipos de la liga? (s/n): ")
            
            cent = input("Desea crear una liga? (s/n): ")
        print(ligas)
        eliminarEquipo = input("Desea eliminar un equipo de la liga? (s/n): ")
        while(eliminarEquipo.lower() == "s"):
            equipo.eliminar__dato(ligas,equipos)
            eliminarEquipo = input("Desea eliminar un equipo de la liga? (s/n): ")


system = main()

    

    
        