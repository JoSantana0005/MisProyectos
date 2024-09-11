class Bolsa:
    def __init__(self, id: int,golosinas: str, marca: str):
        self.id = id
        self.golosinas = golosinas
        self.marca = marca
        self.bolsa = {}

    #Getters
    def getId(self):
        return self.id

    def getGolosinas(self):
        return self.golosinas
    
    def getMarca(self):
        return self.marca
    
    #Setters
    def setId(self,id):
        self.id = id

    def setTipo(self,golosinas):
        self.golosinas = golosinas
    
    def setMarca(self,marca):
        self.marca = marca
    
    #Funciones

    #Funcion que agrega el tipo y la marca a la bolsa
    
    def agregar_dato(self):
        self.bolsa['ID'] = self.id
        self.bolsa['Marca'] = self.marca
        self.bolsa['Golosina'] = self.golosinas

        return self.bolsa

    #Funcion que muestra el contenido de la bolsa
    def mostrar__dato(self,bolsa: list):
        print("El contenido de la bolsa es el siguiente: ")
        for i in range(len(bolsa)):
            print(bolsa, "/n")

    #Funcion que modifica los datos de la bolsa
    def modificar_dato(self, bolsas: list):
        Tipos = ["nestle", "savoy", "ferrero_rocher", "toblerone"]
        golosinas = ["pepito","gomitas","chupeta"]
        tipo = input("Ingrese la marca de la golosina: ")
        golosina = input("Ingrese la golosina: ")
        for dato in Tipos:
            if(dato == tipo):
                print("Se acepta la marca de la golosina")
            else:
                print("No se encontro la marca en la lista, vuelva a elegir")
                
        
        for dato in golosinas:
            if(dato == golosina):
                print("Se acepta la golosina")
            else:
                print("No se encontro la golisna en la lista, vuelva a elegir")
                
        
        sele = int(input("Ingrese el id del dato que quiere modificar de la bolsa: "))
        for bolsa in bolsas:
            if(bolsa['ID'] == sele):
                bolsa.update({
                    'Marca': tipo,
                    'Golosina': golosina
                })
        
        print("Actualización de la bolsa")
        print(bolsas)

    #Funcion que elimina un dato de la bolsa
    def eliminar_dato(self,bolsas:list):
        sele = int(input("Ingrese el id del dato que quiere eliminar: "))
        for dato in bolsas:
            if(dato['ID'] == sele):
                bolsas.remove(dato)
        
        print("Actualización de la bolsa")
        print(bolsas)

def main():
    bolsa = []
    id = 0
    cent = input("Desea agregar un dato a la bolsa? (s/n): ")
    while cent.lower() == "s":
        id += 1
        marca = input("Ingrese la marca de la golosina: ")
        golosina = input("Ingrese la golosina (pepito,gomita,chupeta): ")
        bolsas = Bolsa(id,golosina,marca)
        dato = bolsas.agregar_dato()
        bolsa.append(dato)
        print(bolsa)
        cent = input("Desea agregar un dato a la bolsa? (s/n): ")
    
    modificar = input("Desea modificar un dato de la bolsa (s/n): ")
    while modificar.lower() == "s":
        bolsas.modificar_dato(bolsa)
        modificar = input("Desea modificar un dato de la bolsa (s/n): ")
    
    Eliminar = input("Desea eliminar un dato de la bolsa? (s/n): ")
    while Eliminar.lower() == "s":
        bolsas.eliminar_dato(bolsa)
        Eliminar = input("Desea eliminar un dato de la bolsa? (s/n): ")
    
    bolsas.mostrar__dato(bolsa)

system = main()




