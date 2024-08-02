#Batalla de pokemones
class Pokemon:
    def __init__(self,nombre,tipo,HP,atq):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = HP
        self.ataque = atq
    
    #Getters
    def getNombre(self):
        return self.nombre
    def getTipo(self):
        return self.tipo
    def getHP(self):
        return self.vida
    def getAtaque(self):
        return self.ataque
    
    #Setters
    def setNombre(self,nombre):
        self.nombre = nombre
    def setTipo(self,tipo):
        self.tipo = tipo
    def setHP(self,HP):
        self.vida = HP
    def setAtaque(self,Ataque):
        self.ataque = Ataque
    
        