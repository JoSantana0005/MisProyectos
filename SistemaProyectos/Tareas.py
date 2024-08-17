class Tareas:
    def __init__(self,id: int, nombre: str, empresa: str, 
                 cliente: str, descripcion: str, fechaI: str, 
                 fechaV: str, estado: str, porcentaje: float):
        
        self.id = id
        self.nombre = nombre
        self.empresa = empresa
        self.cliente = cliente
        self.desc = descripcion
        self.fechaI = fechaI
        self.fechaV = fechaV
        self.estado = estado
        self.porc = porcentaje
        self.tareas = {}
    
    #Getters
    def getID(self):
        return self.id
    
    def getNombre(self):
        return self.nombre
    
    def getEmpresa(self):
        return self.empresa
    
    def getCliente(self):
        return self.cliente
    
    def getDescripción(self):
        return self.desc
    
    def getFechaI(self):
        return self.fechaI
    
    def getFechaV(self):
        return self.fechaV
    
    def getEstado(self):
        return self.estado
    
    def getPorcentaje(self):
        return self.porc
    
    
    #Setters
    def setID(self,id):
        self.id = id
    
    def setNombre(self,nombre):
        self.nombre = nombre
    
    def setEmpresa(self,empresa):
        self.empresa = empresa
    
    def setCliente(self,cliente):
        self.cliente = cliente
    
    def setDescripción(self,desc):
        self.desc = desc
    
    def setFechaI(self,fechaI):
        self.fechaI = fechaI
    
    def setFechaV(self,fechaV):
        self.fechaV = fechaV
    
    def setEstado(self,estado):
        self.estado = estado
    
    def setPorcentaje(self,porc):
        self.porc = porc
    
    #Funciones

    #Funcion que crea una tarea
    def crear__tarea(self):
        self.tareas['ID Tarea'] = self.id
        self.tareas['Nombre de la tarea'] = self.nombre
        self.tareas['Empresa'] = self.empresa
        self.tareas['Cliente'] = self.cliente
        self.tareas['Descripción'] = self.desc
        self.tareas['Fecha de Inicio'] = self.fechaI
        self.tareas['Fecha de Vencimiento'] = self.fechaV
        self.tareas['Estado de la tarea'] = self.estado
        self.tareas['Porcentaje de la tarea'] = self.porc

        print("La tarea creada es la siguiente: ")
        print(f"id: {self.id}")
        print(f"Nombre de la tarea: {self.nombre}")
        print(f"Empresa: {self.empresa}")
        print(f"Nombre del cliente: {self.cliente}")
        print(f"Descripción de la tarea: {self.desc}")
        print(f"Fecha de Inicio de la tarea: {self.fechaI}")
        print(f"Fecha de Vencimiento de la tarea: {self.fechaV}")
        print(f"Estado de la tarea: {self.estado}")
        print(f"Porcentaje: {self.porc}")
    
    #Funcion que agrega la tarea al proyecto
    def agregar__Tarea(self,proyecto: dict, tareas: list):
        tareas.append(self.tareas)
        proyecto["Tareas"] = tareas
        print("Se ha agregado exitosamente")
    
    #Funcion que elimina una tarea de un proyecto
    def elimina__tarea(self,proyectos: list, tareas: list):
        idProyectos = int(input("Ingrese el id del proyecto: "))
        for elementos in proyectos:
            if elementos['ID'] == idProyectos:
                sele = int(input("Ingrese la tarea que quiere eliminar: "))
                if(len(tareas) == 0):
                    print("Ya no queda tareas por eliminar")
                else:
                    for tarea in tareas:
                        if tarea['ID Tarea'] == sele:
                            tareas.remove(tarea)
            else:
                print("No se encontro el id del poryecto")
        
        print("Actualización de las tareas")
        print(proyectos)
    
    #Funcion que modifica una tarea de un proyecto
    def modificar__tarea(self,proyectos:list, tareas:list, id: int, nombre: str, empresa: str, 
                 cliente: str, descripcion: str, fechaI: str, 
                 fechaV: str, estado: str, porcentaje: float):
        
        idProyectos = int(input("Ingrese el id del proyecto: "))
        for elemento in proyectos:
            if(elemento['ID'] == idProyectos):
                nombreT = input("Ingrese el nombre de la tarea que quiere modificar: ")
                for tarea in tareas:
                    if tarea['Nombre de la tarea'] == nombreT:
                        tarea.update({
                            'ID Tarea': id,
                            'Nombre de la tarea':nombre,
                            'Empresa':empresa,
                            'Cliente':cliente,
                            'Descripción': descripcion,
                            'Fecha de Inicio': fechaI,
                            'Fecha de Vencimiento': fechaV,
                            'Estado de la Tarea': estado,
                            'Porcentaje': porcentaje
                        })
                        print("Se ha modificado exitosamente la tarea")
                    else:
                        print("No se ha podido modificar la tarea")
            else:
                print("No se ha encontrado el id del proyecto")
        
        print("Actualización de las tareas")
        print(proyectos)
    
    



