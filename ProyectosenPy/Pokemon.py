#Batalla de pokemones
class Pokemon:
    def __init__(self,nombre,tipo,HP,atq):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = HP
        self.atk = atq
    
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
    
    #Funcion que ataca el pokemon
    def ataque(self,rival:object):
        daño = self.atk
        rival.recibir_daño(daño)
        print(f"El pokemon {self.nombre} ataco al pokemon {rival.nombre} con un daño {daño}")
    
    #Funcion que el pokemon recibe daño
    def recibir_daño(self,daño):
        self.vida = self.vida - daño
        if self.vida <= 0:
            print(f"El pokemon fue derrotado")
        else:
            print(f"El pokemon recibio un ataque de {daño} quedando con una vida de {self.vida} ")

class BatallaPokemon:
    def __init__(self,pokemon1:object,pokemon2: object):
        self.poke1 = pokemon1
        self.poke2 = pokemon2
        self.turno = 1
    
    #Batalla
    def batalla(self):
        while self.poke1.vida > 0 and self.poke2.vida > 0:
            if self.turno == 1:
                self.poke1.ataque(self.poke2)
                self.turno = 2
            else:
                self.poke2.ataque(self.poke1)
                self.turno = 1
        if self.poke1.vida <= 0:
            print(f"Gano el pokemon {self.poke2.nombre}")
        else:
            print(f"Gano el pokemon {self.poke1.nombre}")

pokemon1 = Pokemon("Charizard","Fuego", 450, 120)
pokemon2 = Pokemon("Venesaur","Planta", 550, 100)
batalla = BatallaPokemon(pokemon1,pokemon2)
batalla.batalla()   




        
        