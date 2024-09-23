from Liga import Liga
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
            NombreEquipo = input("Ingrese el nombre del equipo que quiere eliminar: ")
            for liga in ligas:
                for equipo in Equipos:
                    if(equipo['Nombre del equipo'] == NombreEquipo):
                        Equipos.remove(equipo)
                        print("Actualización de los equipos")
                        print(ligas)
                    else:
                        print("No se han encontrado el equipo a eliminar")
        except:
            raise ValueError("Error: dato invalido")
    #Function que muestra los equipos
    def mostrar_dato(self, Equipos: list):
        for x, y in self.equipos.items():
            print(x,y)

def main():
        

    

    
        