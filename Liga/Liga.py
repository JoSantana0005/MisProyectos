class Liga:
    def __init__(self,id: int,nombreLiga: str, PaisLiga: str):
        self.id = id
        self.nombre = nombreLiga
        self.Pais = PaisLiga
        self.equipos = []
    
    #Getters 
    def getNombreLiga(self):
        return self.nombre
    
    def getPaisLiga(self):
        return self.Pais
    
    #Setters
    def setNombreLiga(self,nombre):
        self.nombre = nombre
    
    def setPaisLiga(self,Pais):
        self.Pais = Pais
    
    