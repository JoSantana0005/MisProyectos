
class Proyectos:
    def __init__(self,id: int, nombre: str, descripcion: str, 
                 fechaInicio: str, fechaVenci: str, estado: str,
                  empresa: str, equipo: str ):
        
        self.id = id
        self.nombre = nombre
        self.desc = descripcion
        self.fechaI = fechaInicio
        self.fechaV = fechaVenci
        self.estado = estado
        self.empresa = empresa
        self.equipo = equipo
        self.Proyectos = {}
    
    #Getters
    def getId(self):
        return self.id
    
    def getNombre(self):
        return self.nombre
    
    def getDesc(self):
        return self.desc
    
    def getFechaIni(self):
        return self.fechaI
    
    def getFechaVenci(self):
        return self.fechaV
    
    def getEstado(self):
        return self.estado
    
    def getEmpresa(self):
        return self.empresa
    
    def getEquipo(self):
        return self.equipo
    
    #Setters
    def setId(self,id):
        self.id = id
    
    def setNombre(self,nombre):
        self.nombre = nombre
    
    def setDesc(self,desc):
        self.desc = desc
    
    def setFechaI(self,fechaI):
        self.fechaI = fechaI
    
    def setFechaV(self,fechaV):
        self.fechaV = fechaV
    
    def setEstado(self,estado):
        self.estado = estado
    
    def setEmpresa(self,empresa):
        self.empresa = empresa
    
    def setEquipo(self,equipo):
        self.equipo = equipo
    
    #Funciones de la clase

    #Funcion que crea un nuevo proyecto
    def crear__Proyecto(self):
        self.Proyectos['ID'] = self.id
        self.Proyectos['Nombre'] = self.nombre
        self.Proyectos['Descripción'] = self.desc
        self.Proyectos['Fecha de Inicio'] = self.fechaI
        self.Proyectos['Fecha de vencimiento'] = self.fechaV
        self.Proyectos['Estado'] = self.estado
        self.Proyectos['Empresa'] = self.empresa
        self.Proyectos['Equipo'] = self.equipo
        
        print("El proyecto creado es el siguiente")
        print(f"Id: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Descripción: {self.desc}")
        print(f"Fecha de Inicio: {self.fechaI}")
        print(f"Fecha de Vencimiento: {self.fechaV}")
        print(f"Estado del proyecto: {self.estado}")
        print(f"Empresa: {self.empresa}")
        print(f"Equipo del Proyecto: {self.equipo}")
    
    #Funcion que agrega el proyecto a la lista
    def agregar__Proyectos(self,proyectos: list):
        proyectos.append(self.Proyectos)
        print("Se ha agregado exitosamente")
    
    #Elimina un proyecto de la lista
    def elimina__proyecto(self,Proyectos: list):
        sele = int(input("Ingrese el id del proyecto: "))
        if(len(Proyectos) == 0):
            print("Ya no quedan proyectos que puedas eliminar de las lista")
        else:
            for elementos in Proyectos:
                if elementos["ID"] == sele:
                    Proyectos.remove(elementos)
                    print("Se ha eliminado exitosamente el proyecto")
            
            if Proyectos:
                print("Actualización de los proyectos")
                print(Proyectos)
            else:
                print("La lista ya esta vacia jejej")
    
    #Modifica un proyecto de la lista
    def modificar__proyecto(self,Proyectos:list, id: int, nombre: str, descripcion: str, 
                 fechaInicio: str, fechaVenci: str, estado: str,
                  empresa: str, equipo: str ):
        
        sele = int(input("Ingrese el id del proyecto: "))
        for elemento in Proyectos:
            if elemento["ID"] == sele:
                elemento.update({
                    'Nombre': nombre,
                    'Descripción': descripcion,
                    'Fecha de Inicio': fechaInicio,
                    'Fecha de Vencimiento': fechaVenci,
                    'Estado': estado,
                    'Empresa': empresa,
                    'Equipo': equipo
                })
                print("Se ha modificado exitosamente el proyecto")
            else:
                print("No se ha encontrado el proyecto a modificar")
        print("Actualizacion de los proyectos")
        print(Proyectos)
    
    #Consultar un proyecto de la lista
    def consultar__Proyecto(self,Proyectos:list):
        nombre = input("Ingrese el nombre del proyecto a consultar: ").upper()
        for elemento in Proyectos:
            if elemento['Nombre'].upper() == nombre:
                for key,items in elemento.items():
                    print(f"{key} : {items}")









    


    
    
