class Liga:
    def __init__(self,id: int,nombreLiga: str, PaisLiga: str):
        self.id = id
        self.nombre = nombreLiga
        self.Pais = PaisLiga
        self.equipos = []
    
    #Getters 