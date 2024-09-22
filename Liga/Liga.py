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
    #Funcion que crear los atributos de la clase en un diccionario
    def create__data(self):
        print(f"ID: {self.id}")
        print(f"Nombre de la liga: {self.nombre}")
        print(f"Pais deonde se juega la liga: {self.Pais}")
    #Funcion que agrega los elementos creandos a la lista
    def add__data(self):
        self.Ligas['ID'] = self.id
        self.Ligas['Nombre de la Liga'] = self.nombre
        self.Ligas['Pais de la Liga'] = self.Pais
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

def main():
    lista = []
    id = 0
    while True:
        cent = input("Desea crear una liga a la lista? (s/n): ")
        while cent.lower() == "s":
            id += 1
            NombreLiga = input("Ingrese el nombre de la liga: ")
            paisLiga = input("Ingrese el pais de la liga: ")
            liga = Liga(id,NombreLiga,paisLiga)
            liga.create__data()
            agregar = input("Desea agregar esta liga a la lista? (s/n): ")
            if agregar.lower() == "s":
                result = liga.add__data()
                lista.append(result)
                print("Se ha agregando exitosamente")
            else:
                print("No se ha agregado la liga")
            cent = input("Desea crear una liga a la lista? (s/n): ")
        print(lista)
        

system = main()
                
            

    