import random
from datetime import datetime
class Lector:
    def __init__(self,numero,nombre,apellido,moroso,codi,titulo,autor,editor,prestado):
        self.numero = numero
        self.nombre = nombre
        self.apellido = apellido
        self.moroso = moroso
        self.codi = codi
        self.titulo = titulo
        self.autor = autor
        self.editor = editor
        self.prestado = prestado
    
    #Getters
    
    def getCodi(self):
        return self.codi
    
    def getTitulo(self):
        return self.titulo
    
    def getAutor(self):
        return self.autor
    
    def getEditor(self):
        return self.editor
    
    def getPrestado(self):
        return self.prestado
    #Setters

    def setCodi(self,codi):
        self.codi = codi
    
    def setTitulo(self,titulo):
        self.titulo = titulo
    
    def setAutor(self,autor):
        self.autor = autor
    
    def setEditor(self,editor):
        self.editor = editor
    
    def setPrestado(self,prestado):
        self.prestado = prestado
    
    #Getters

    def getNumero(self):
        return self.numero
    
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getMoroso(self):
        return self.moroso
    
    #Setters

    def setNumero(self,numero):
        self.numero = numero
    
    def setNombre(self,nombre):
        self.nombre = nombre

    def setApellido(self,apellido):
        self.apellido = apellido
    
    def setMoroso(self,moroso):
        self.moroso = moroso
        

class Prestamo(Lector):
    #Logica del programa
    def __init__(self, numero, nombre, apellido, moroso, codi, titulo, autor,editor, prestado):
        super().__init__(numero, nombre, apellido, moroso, codi, titulo, autor, editor, prestado)
    def escogerLibro(self,fechaDP):
        if (self.codi == 1 and self.prestado == True):
            print(self.nombre, " ", self.apellido, " han elegido elegido el libro: ", " el dia: ",fechaDP )
            print("TiLibro     Autor    Editor")
            print("{0:^10} {1:^10} {2:^10}".format(self.titulo,self.autor,self.editor),end=" ")    
        elif(self.codi == 1 and self.prestado == False):
            print("El libro ya fue prestado")

        if(self.codi == 2 and self.prestado == True):
            print(self.nombre, " ", self.apellido," han elegido elegido el libro: "," el dia: ",fechaDP )
            print("TiLibro     Autor    Editor")
            print("{0:^10} {1:^10} {2:^10}".format(self.titulo,self.autor,self.editor),end=" ")
            
        elif(self.codi == 2 and self.prestado == False):
            print("El libro ya fue prestado")        
            
        if(self.codi == 3 and self.prestado == True):
            print(self.nombre, " ", self.apellido, "han elegido elegido el libro: "," el dia: ", fechaDP)
            print("TiLibro     Autor    Editor")
            print("{0:^10} {1:^10} {2:^10}".format(self.titulo,self.autor,self.editor),end=" ")
            print("\n")

        elif(self.codi == 3 and self.prestado == False):
            print("El libro ya fue prestado")
             
        if(self.codi > 3):
            print("Se equivoco a la hora de colocar el numero del libro y el codigo del libro")
    def devolver(self,fechaDP):
        if(self.numero > 15):
            self.moroso = True
            print("La persona no han entregado el libro a tiempo")
        else:
            if(self.codi == 1):
                self.prestado = False
                print("La persona: ",self.nombre," ",self.apellido," han devuelto el libro: ",self.titulo, " el dia: ", fechaDP)
                print(self.titulo)
                print(self.autor)
                print(self.editor)
            elif(self.codi == 2):
                self.prestado = False
                print("La persona: ",self.nombre," ",self.apellido," han devuelto el libro: ",self.titulo, " el dia: ",fechaDP)
                print(self.titulo)
                print(self.autor)
                print(self.editor)
            elif(self.codi == 3):
                self.prestado = False
                print("La persona: ",self.nombre," ",self.apellido," han devuelto el libro: ",self.titulo, " el dia: ",fechaDP)
                print(self.titulo)
                print(self.autor)
                print(self.editor)    
        

# Principal
FechaDp = datetime.now()
fechaP = datetime.now()
"""
num = int(input("Ingrese los dias que tiene la persona con el libro: "))
nom = input("Ingrese el nombre de la persona: ")
ape = input("Ingrese el apellido de la persona: ")
codi = random.randrange(1,4)
titu = input("Ingrese el titulo del libro: ")
autor = input("Ingrese el nombre del autor del libro: ")
edi = input("Ingrese el editor del libro: ")
moro = False
pres = True
"""
Clien1 = Lector(2,"Jose","Santana",False,2,"w","Car","q",True)
reseva1 = Prestamo(Clien1.getNumero(),Clien1.getNombre(),Clien1.getApellido(),Clien1.getMoroso(),Clien1.getCodi(),
                   Clien1.getTitulo(),Clien1.getAutor(),Clien1.getEditor(),Clien1.getPrestado())
reseva1.escogerLibro(FechaDp)
print("---------------------------------------------")
Clien2 = Lector(2,"carlos","ramos",False,2,"w","Car","q",False)
reseva1 = Prestamo(Clien2.getNumero(),Clien2.getNombre(),Clien2.getApellido(),Clien2.getMoroso(),Clien2.getCodi(),
                   Clien2.getTitulo(),Clien2.getAutor(),Clien2.getEditor(),Clien2.getPrestado())
reseva1.escogerLibro(FechaDp)
