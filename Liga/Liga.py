#Programa encargado de almacenar las mejores ligas de futbol del mundo
class Liga:
    def __init__(self,nombreLiga:str,paisLiga:str,equiposLiga: list, partidos:int):
        self.Nombre = nombreLiga
        self.Pais = paisLiga
        self.equipos = equiposLiga
        self.partidos = partidos
        self.ligas = {}

    #Getters
    def getNombreLiga(self):
        return self.Nombre
    
    def getPaisLiga(self):
        return self.Pais
    
    def getEquiposliga(self):
        for i in range(len(self.equipos)):
            return self.equipos[i]
    
    #Setters
    def setNombreLiga(self,nombre):
        self.Nombre = nombre
    
    def setPaisLiga(self,pais):
        self.Pais = pais
    
    def setEquiposLiga(self,equipos):
        self.equipos = equipos
    
    #Funciones que dara la vida a la clase
    def agregar_datos(self):
        self.ligas['Nombre de Liga'] = self.Nombre
        self.ligas['Pais de Liga'] = self.Pais
        self.ligas['Equipos'] = self.equipos
        self.ligas['Partidos a jugar'] = self.partidos
        return self.ligas
    
        