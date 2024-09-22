class Equipos:
    def __init__(self,NombreEquipo: str, golesC: int, golesF: int, partidosG: int,
                 partidosE: int, partidosP: int):
        self.NombreEquipo = NombreEquipo
        self.GolesContra = golesC
        self.GolesFavor = golesF
        self.Ganados = partidosG
        self.empatados = partidosE
        self.perdidos = partidosP
    
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
    
    
        