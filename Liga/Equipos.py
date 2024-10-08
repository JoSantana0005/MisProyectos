class Equipo:
    def __init__(self,nombreEquipo:str,Trofeos:int,Fundación: int):
        self.nombre = nombreEquipo
        self.Trofeo = Trofeos
        self.fundacion = Fundación
        self.equipo = []
    
    #Getters
    def getNombreEquipo(self):
        return self.nombre
    
    def getTrofeos(self):
        return self.Trofeo
    
    def getFundacion(self):
        return self.fundacion
    
    #Setters
    def setNombreEquipo(self,nombre):
        self.nombre = nombre
    
    def setTrofeos(self,trofeos):
        self.Trofeo = trofeos
    
    def setFundacion(self,funda):
        self.fundacion = funda
    
    #Funciones
    #Funcion que agrega los datos de los equipos en la lista
    def agregar__datos(self):
        