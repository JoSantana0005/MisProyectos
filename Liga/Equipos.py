class Equipo:
    def __init__(self,nombreEquipo:str,Trofeos:int,Fundación: int):
        self.nombre = nombreEquipo
        self.Trofeo = Trofeos
        self.fundacion = Fundación
        self.equipo = {}
    
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
        self.equipo['Nombre de Equipo'] = self.nombre
        self.equipo['Trofeos'] = self.Trofeo
        self.equipo['Fundación'] = self.fundacion
        return self.equipo

    #Funcion que elimina un equipo de la liga
    def eliminar_dato(self,lista:list,equipos:list):
        try:
            nombreLiga = input("Ingrese el nombre de la liga: ")
            for liga in lista:
                if(liga['Nombre de Liga'] == nombreLiga):
                    nombreEquipo = input("Ingrese el nombre del equipo a eliminar: ")
                    for equipo in equipos:
                        if(len(equipos) == 0):
                            print("No queda equipos en la lista de los equipos")
                        else:
                            if(equipo['Nombre de Equipo'] == nombreEquipo):
                                equipos.remove(equipo)
                            else:
                                print("No se encontro el equipo a eliminar")
                else:
                    print("No se encontro la liga del equipo a eliminar")
            print(lista)
        except:
            raise ValueError("Error:dato invalido")
    
    #Funcion que modifica un equipo de la lista
    def modificar_dato(self,lista:list, equipos: list):
        try:
            nombreLiga = input("Ingrese el nombre de la liga del equipo: ")
            for liga in lista:
                if(liga['Nombre de Liga'] == nombreLiga):
                    nombreEquipo = input("Ingrese el nombre del equipo que quiere modificar")
                    for equipo in equipos:
                        if(equipo['Nombre de Equipo'] == nombreEquipo):
                            equipo.update({
                                "Nombre de Equipo": input("Ingrese el nuevo nombre del equipo"),
                                "Trofeos": int(input("Ingrese los trofeos que han ganado el equipo: ")),
                                "Fundación": int(input("Ingrese la fecha de fundacion del equipo"))
                            })
                        else:
                            print("No se encontro el equipo a modificar")
                else:
                    print("No se encontro la liga del equipo")
        except:
            raise ValueError("Error: dato invalido")
    
