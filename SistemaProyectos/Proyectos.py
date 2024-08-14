from datetime import datetime
from Tareas import Tareas
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
        self.Proyectos = []
    
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
        self.Proyectos.append(self.id)
        self.Proyectos.append(self.nombre)
        self.Proyectos.append(self.desc)
        self.Proyectos.append(self.fechaI)
        self.Proyectos.append(self.fechaV)
        self.Proyectos.append(self.estado)
        self.Proyectos.append(self.empresa)
        self.Proyectos.append(self.equipo)
        
        print("El proyecto creado es el siguiente")
        print(f"Id: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Descripción: {self.desc}")
        print(f"Fecha de Inicio: {self.fechaI}")
        print(f"Fecha de Vencimiento: {self.fechaV}")
        print(f"Estado del proyecto: {self.estado}")
        print(f"Empresa: {self.empresa}")
        print(f"Equipo del Proyecto: {self.equipo}")

    #Funcion que agrega el proyecto creando a una lista
    def agregar__Proyecto(self,lista:list):
        lista.append(self.Proyectos)
        print("Se ha agregando el proyecto exitosamente")
    
    #Funcion que elimina un proyecto de la lista
    def elimina__Proyecto(self,lista: list):
        try:
            id = int(input("Ingrese el proyecto que quiere eliminar de la lista: "))
            if (len(lista) == 0):
                print("Ya no hay proyectos que puedas eliminar")
            else:
                if id > 0 and id <= len(lista):
                    del lista[id - 1]
                else:
                    print("No se ha podido eliminar el proyecto de la lista")
            
            print("Actualización de la lista de los proyectos")
            print(lista)
        except:
            raise ValueError("Se equivoco en un dato")
    
    #Funcion que modifca a un proyecto de la lista segun su id
    def Modificar__Proyecto(self, lista: list, id: int, nombre: str, descripcion: str, 
                 fechaInicio: datetime, fechaVenci: datetime, estado: str,
                  empresa: str, equipo: str ):
        try:
            seleccion = int(input("Ingrese el proyecto que quiere eliminar de la lista: "))
            if(seleccion > 0 and seleccion <= len(lista)):
                lista[seleccion - 1] = [id,nombre,descripcion,fechaInicio,fechaVenci,estado,empresa,equipo]
                print("Se ha modificado el proyecto exitosamente")
            else:
                print("No se ha podido modifcar el proyecto")
            
            print("Actualización de la lista de los proyectos")
            print(lista)
        
        except:
            raise ValueError("Se equivoco en un dato")
    
    #Funcion que consulta un proyecto de la lista
    def consultar_proyecto(self,lista: list):
        sele = int(input("Ingrese el id del proyecto que quiere consultar: "))
        if (sele > 0 and sele <= len(lista)):
            print("ID     Nombre    desc    fechaI    fechaV    Estado     Empresa   Equipo")
            print("{0:^3d} {1:^10s} {2:^10s} {3:^10s} {4:^10s} {5:^10s} {6:^10s} {7:^10s}".format(
                lista[sele][0],lista[sele][1],lista[sele][2],lista[sele][3],
                lista[sele][4],lista[sele][5],lista[sele][6],lista[sele][7]
            ), end="\n")
            print("Este es el proyecto que quiere consultar")
        else:
            print("No se pudo consultar el proyecto")

 

cent = input("Desea crear un Proyecto? (s/n): ")
lista = []
id = 0
idT = 0
while cent.lower() == "s":
    try:
        id += 1
        nombre = input("Ingrese el nombre del proyecto: ")
        Desc = input("Ingrese la descripción del proyecto: ")
        fechaI = input("Ingrese la fecha de inicio del proyecto (YYYY-MM-DD): ")
        fechaIni = datetime.strptime(fechaI, "%Y-%m-%d")
        fechaV = input("Ingrese la fecha de vencimiento del proyecto (YYYY-MM-DD): ")
        fechaVen = datetime.strptime(fechaV,"%Y-%m-%d")
        estado = input("Ingrese el estado del proyecto: ")
        empresa = input("Ingrese la empresa que esta realizando el proyecto: ")
        equipo = input("Ingrese el equipo que esta realizando el proyecto: ")
        proyecto = Proyectos(id,nombre,Desc,fechaIni,fechaVen,estado,empresa,equipo)
        proyecto.crear__Proyecto()
        Tare = input("Desea crear una tarea a este proyecto? (s/n): ")
        while Tare.lower() == "s":
            idT += 1
            nombreT = input("Ingrese el nombre de la tarea: ")
            DescT = input("Ingrese la descripción de la tarea: ")
            cliente = input("Ingrese el nombre del cliente: ")
            fechaIT = input("Ingrese la fecha de inicio de la tarea (YYYY-MM-DD): ")
            fechaVT = input("Ingrese la fecha de vencimiento de la tarea (YYYY-MM-DD): ")
            estadoT = input("Ingrese el estado de la tarea: ")
            porcentaje = float(input("Ingrese el porcentaje de la tarea: "))
            tarea = Tareas(idT,nombreT,empresa,cliente,DescT,fechaIT,fechaVT,estadoT,porcentaje)
            tarea.crear__tarea()
            agregarT = input("Desea agregar esta tarea al proyecto? (s/n): ")
            if(agregarT.lower() == "s"):
                tarea.agregar_tarea(proyecto.Proyectos)
            else:
                print("No se ha agregado la tarea al proyecto")
                continue
            Tare = input("Desea crear una tarea a este proyecto? (s/n): ")
        
        agregar = input("Desea agregar este proyecto a la lista? (s/n): ")
        if (agregar.lower() == "s"):
            proyecto.agregar__Proyecto(lista)
        else:
            print("No se agregado el proyecto a la lista")
        cent = input("Desea crear un Proyecto? (s/n): ")
    except:
        raise ValueError("Se equivocó a la hora de poner un dato")
print(lista)
tarea.eliminar_tarea(lista)




"""eliminar = input("Desea eliminar un proyecto de la lista? (s/n): ")
while eliminar.lower() == "s":
    proyecto.elimina__Proyecto(lista)
    eliminar = input("Desea eliminar un proyecto de la lista? (s/n): ")

modificar = input("Desea Modificar un Proyecto? (s/n): ")
while modificar.lower() == "s":
    nuevoId = int(input("Ingrese el nuevo id del proyecto: "))
    Nuevonombre = input("Ingrese el nuevo nombre del proyecto: ")
    NuevaDesc = input("Ingrese la nueva descripción del proyecto: ")
    NuevafechaI = input("Ingrese la nueva fecha de inicio del proyecto (YYYY-MM-DD): ")
    NuevafechaIni = datetime.strptime(fechaI, "%Y-%m-%d")
    NuevafechaV = input("Ingrese la nueva fecha de vencimiento del proyecto (YYYY-MM-DD): ")
    NuevafechaVen = datetime.strptime(fechaV,"%Y-%m-%d")
    Nuevoestado = input("Ingrese el nuevo estado del proyecto: ")
    Nuevaempresa = input("Ingrese la nueva empresa que esta realizando el proyecto: ")
    Nuevoequipo = input("Ingrese el nuevo equipo que esta realizando el proyecto: ")

    proyecto.Modificar__Proyecto(lista,nuevoId,Nuevonombre,NuevaDesc,NuevafechaI,NuevafechaV,Nuevoestado,Nuevaempresa,Nuevoequipo)
    modificar = input("Desea Modificar un Proyecto? (s/n): ")

consultar = input("Desea cosultar un proyecto? (s/n): ")
while consultar.lower() == "s":
    proyecto.consultar_proyecto(lista)
    consultar = input("Desea cosultar un proyecto? (s/n): ")

print(lista)"""



    


    
    
