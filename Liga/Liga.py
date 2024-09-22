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
    #Funcion que agrega los atributos de la clase en un diccionario
    def add__data(self):
        self.Ligas['ID'] = self.id
        self.Ligas['Nombre de la liga'] = self.nombre
        self.Ligas['Pais de la liga'] = self.Pais
        return self.Ligas
    #Funcion que modifica un dato de la lista
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
                    print("No se ha encontrado el elemento a modificar")
        except:
            raise ValueError("Error: dato invalido")
        print("Actualización de las ligas que esta en la lista")
        print(Ligas)
    #Funcion que elimina un dato de la lista
    def delete__data(self, Ligas:list):
        try:
            id = int(input("Ingrese el id de la liga que quiere eliminar: "))
            for Liga in Ligas:
                if(len(Ligas) == 0):
                    print("Ya no queda mas elemnto en la lista que pueda eliminar")
                else:
                    if(Liga['ID'] == id):
                        Ligas.remove(Liga)
                    else:
                        print("No se han encontrado el elemento a eliminar")
        except:
            raise ValueError("Error: dato invalido")
        
        print("Actualización de las ligas que esta en la lista")
        print(Ligas)
    
    #Funcion que busca una liga en especifico
    def buscar__dato(self,Ligas:list):
        try:
            id = int(input("Ingrese el id de la liga que quiere consultar: "))
            for i in range(len(Ligas)):
                if(Ligas[i] == id):
                    print(Ligas[i])
                else:
                    print("No se ha encontrado el dato a consultar: ")
        except:
            raise ValueError("Error: dato invalido")
    

    