class Subtareas:
    def __init__(self, id: int, nombre: str, estado: str, 
                 fechaI: str, fechaV: str, porc: float) -> None:
        
        self.id = id
        self.nom = nombre
        self.estado = estado
        self.fechaI = fechaI
        self.fechaV = fechaV
        self.porc = porc
        self.subtareas = {}
    
    #Getters
    def getId(self):
        return self.id
    
    def getNombre(self):
        return self.nom
    
    def getEstado(self):
        return self.estado

    def getFechaI(self):
        return self.fechaI
    
    def getFechaV(self):
        return self.fechaV
    
    def getPorcentaje(self):
        return self.porc
    
    #Setters
    def setId(self,id):
        self.id = id
    
    def setNombre(self,nombre):
        self.nom = nombre
    
    def setEstado(self,estado):
        self.estado = estado
    
    def setFechaI(self,fechaI):
        self.fechaI = fechaI
    
    def setFechaV(self,fechaV):
        self.fechaV = fechaV
    
    def setPorcentaje(self,porc):
        self.porc = porc
    
    #Funciones

    #Funcion que crea una subtarea
    def crear__subtarea(self):
       self.subtareas['ID de la subtarea'] = self.id
       self.subtareas['Nombre de la subtarea'] = self.nom
       self.subtareas['Estado de la subtarea'] = self.estado
       self.subtareas['Fecha de inicio'] = self.fechaI
       self.subtareas['Fecha de vencimiento'] = self.fechaV
       self.subtareas['Porcentaje de la subtarea'] = self.porc

       print("Se ha creado la siguiente subtarea")
       print(f"ID de la subtarea: {self.id}")
       print(f"Nombre de la subtarea: {self.nom}")
       print(f"Estado de la subtarea: {self.estado}")
       print(f"Fecha de inicio de la subtarea: {self.fechaI}")
       print(f"Fecha de vencimiento de la subtarea: {self.fechaV}")
       print(f"Porcentaje de la subtarea: {self.porc}")
    
    #Funcion que agrega la subtarea a una tarea
    def agregar__subtarea(self,tareas: dict, subtarea: list):
        subtarea.append(self.subtareas)
        tareas['Subtareas'] = subtarea
        print("Se ha agregado exitosamente la subtarea")
    
    #Funcion que elimina una subtarea de una tarea
    def eliminar__subtarea(self,proyectos: list,tareas: list ,subtareas: list):
        idProyecto = int(input("Ingrese el id del proyecto: "))
        for proyecto in proyectos:
            if proyecto['ID'] == idProyecto:
                idTarea = int(input("Ingrese el id de la tarea: "))
                for tarea in tareas:
                    if tarea['ID Tarea'] == idTarea:
                        sele = int(input("La subtarea que quiere eliminar: "))
                        if(len(subtareas) == 0):
                            print("Elimino todas las subtareas que habia en la tarea")
                        else:
                            for subtarea in subtareas:
                                if subtarea['ID de la subtarea'] == sele:
                                    subtareas.remove(subtarea)
                                else:
                                    print("No se pudo eliminar la subtarea")
                    else:
                        print("No se pudo encontrar la tarea")
            else:
                print("No se encontro el proyecto")
        print("Actualizacón de las subtareas")
        print(proyectos)
        
    #Funcion que modifica una subtarea de una tarea
    def modificar__subtarea(self,proyectos: list, tareas: list,subtareas: list, 
                            id: int, nombre: str, estado: str, fechaI: str, fechaV: str, porc: float):
        idProyecto = int(input("Ingrese el id del proyecto: "))
        for proyecto in proyectos:
            if(proyecto['ID'] == idProyecto):
                idtarea = int(input("Ingrese el id de la tarea: "))
                for tarea in tareas:
                    if(tarea['ID Tarea'] == idtarea):
                        nombreSubtarea = input("Ingrese el nombre de la subtarea que quiere modificar: ")
                        for subtarea in subtareas:
                            if subtarea['ID de la subtarea'] == nombreSubtarea:
                                subtarea.update({
                                    'ID de la subtarea': id,
                                    'Nombre de la subtarea': nombre,
                                    'Estado de la subtarea': estado,
                                    'Fecha de inicio': fechaI,
                                    'Fecha de vencimiento': fechaV,
                                    'Porcentaje de la subtarea': porc
                                    })
                                print("Se modifico exitosamente la tarea")
                            else:
                                print("No se pudo modificar la subtarea")
                    else:
                         print("No se pudo encontrar la tarea")
            else:
                print("No se encontro el proyecto")
        print("Actualización de las subtareas")
        print(proyectos)
