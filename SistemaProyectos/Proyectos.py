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
        lista.append(self.Proyectos)
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
            
            print("Actualizacion de los Proyectos")
            print(Proyectos)
    
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
        nombre = input("Ingrese el nombre del proyecto a consultar: ")
        for elemento in Proyectos:
            if elemento['Nombre'] == nombre:
                for key,items in elemento.items():
                    print(f"{key} : {items}")
                    
            else:
                print("No se encontro el proyecto a consultar")


lista = []
id = 0
idT = 0
cent = input("Desea crear un proyecto? (s/n): ")
while cent.lower() == "s":
    id += 1
    nombre = input("Ingrese el nombre del proyecto: ")
    Desc = input("Ingrese la descripción del proyecto: ")
    fechaI = input("Ingrese la fecha de inicio del proyecto (YYYY-MM-DD): ")
    fechaV = input("Ingrese la fecha de vencimiento del proyecto (YYYY-MM-DD): ")
    estado = input("Ingrese el estado del proyecto: ")
    empresa = input("Ingrese la empresa que esta realizando el proyecto: ")
    equipo = input("Ingrese el equipo que esta realizando el proyecto: ")
    proyecto = Proyectos(id,nombre,Desc,fechaI,fechaV,estado,empresa,equipo)
    proyecto.crear__Proyecto()
    tarea = input("Desea agregar una tarea al proyecto? (s/n): ")
    tareas = []
    while tarea.lower() == "s":
        
        idT += 1
        nombreT = input("Ingrese el nombre del proyecto: ")
        Cliente = input("Ingrese el nombre del cliente: ")
        DescT = input("Ingrese la descripción del proyecto: ")
        fechaIT = input("Ingrese la fecha de inicio del proyecto (YYYY-MM-DD): ")
        fechaVT = input("Ingrese la fecha de vencimiento del proyecto (YYYY-MM-DD): ")
        estadoT = input("Ingrese el estado del proyecto: ")
        porc = float(input("Ingrese el porcentaje de la tarea: "))
        tare = Tareas(idT,nombreT,empresa,Cliente,DescT,fechaIT,fechaVT,estadoT,porc)
        tare.crear__tarea()
        agregarT = input("Desea agregar esta tarea al proyecto? (s/n): ")
        if (agregarT.lower() == "s"):
            tare.agregar__Tarea(proyecto.Proyectos,tareas)
        else:
            print("No se ha agregado la tarea al proyecto")
        tarea = input("Desea agregar una tarea al proyecto? (s/n): ")

    agregar = input("Desea agregar este proyecto a lista? (s/n): ")
    if (agregar.lower() == "s"):
        proyecto.agregar__Proyectos(lista)
    else:
        print("No se ha agregado este proyecto a la lista")
    
    cent = input("Desea crear un proyecto? (s/n): ")
print(lista)
eliminarT = input("Desea eliminar una tarea? (s/n): ")
while eliminarT.lower() == "s":
    tare.elimina__tarea(lista)
eliminar = input("Desea eliminar un proyecto de la lista? (s/n): ")
while eliminar.lower() == "s":
    proyecto.elimina__proyecto(lista)
    eliminar = input("Desea eliminar un proyecto de la lista? (s/n): ")

modificar = input("Desea modificar un proyecto? (s/n): ")
while modificar.lower() == "s":
    id = int(input("Ingrese el nuevo id: "))
    nombre = input("Ingrese el nuevo nombre del proyecto: ")
    Desc = input("Ingrese la nueva descripción del proyecto: ")
    fechaI = input("Ingrese la nueva fecha de inicio del proyecto (YYYY-MM-DD): ")
    fechaV = input("Ingrese la nueva fecha de vencimiento del proyecto (YYYY-MM-DD): ")
    estado = input("Ingrese el nuevo estado del proyecto: ")
    empresa = input("Ingrese la nueva empresa que esta realizando el proyecto: ")
    equipo = input("Ingrese el nuevo equipo que esta realizando el proyecto: ")
    proyecto.modificar__proyecto(lista,id,nombre,Desc,fechaI,fechaV,estado,empresa,equipo)
    modificar = input("Desea modificar un proyecto? (s/n): ")

consultar = input("Desea consultar n proyecto? (s/n): ")
while consultar.lower() == "s":
    proyecto.consultar__Proyecto(lista)
    consultar = input("Desea consultar un proyecto? (s/n): ")








    


    
    
