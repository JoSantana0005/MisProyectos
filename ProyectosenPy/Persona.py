class Persona:
    #Constructor
    def __init__(self,nom= str,ap = str,correo = str):
        self.nom = nom
        self.ap = ap
        self.correo = correo
    
    #Getters
    def getNom(self):
        return self.nom
    
    def getApe(self):
        return self.ap
    
    def getCorreo(self):
        return self.correo
    
    #Setters
    def setNom(self,nom):
        self.nom = nom
    
    def setApe(self,ap):
        self.ap = ap
    
    def setCorreo(self,correo):
        self.correo = correo

    #Funciones
    def Presentarse(self):
        print("Mi nombre es: " + self.nom)
        print("Mi apellido es: " + self.ap)
        print("me puedes contactar por aqui: " + self.correo)

# Principal
nom = input("Ingrese el nombre de la persona: ")
apelli = input("Ingrese el apellido de la persona: ")
corre = input("Ingrese el correo de la persona: ")

perso1 = Persona(nom,apelli,corre)
person2 = Persona("Jose","Santana","joseasantana05@gmail.com")
perso1.Presentarse()
print("------------------------")
person2.Presentarse()
