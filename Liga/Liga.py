class Liga:
    def __init__(self,id: int,nombreLiga: str, PaisLiga: str):
        self.id = id
        self.nombre = nombreLiga
        self.Pais = PaisLiga
        self.Ligas = {}
    
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
    

    #Function
    #Function that adds the name of the league and the country in a dictionary
    def add__data(self):
        self.Ligas['ID'] = self.id
        self.Ligas['Nombre de la liga'] = self.nombre
        self.Ligas['Pais de la liga'] = self.Pais
        return self.Ligas
    #Function Function that modifies the dictionary data
    def edit__data(self, Ligas: list, nombre: str, pais: str):
        try:
            id = int(input("Ingrese el id de la liga que quiere modificar: "))
            for Liga in Ligas:
                if Liga['ID'] == id:
                    Liga.update({
                        'Nombre de la liga': nombre,
                        'Pais de la liga': pais
                    })
                else:
                    print("The link to modify was not found")
        except:
            raise ValueError("Error: data invalid")
    
    