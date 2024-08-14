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
        self.tarea = []
    
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
    
    #Funciones de la clase tarea

    #Funcion que crea una tarea
    def crear__tarea(self):
        self.tarea.append(self.id)
        self.tarea.append(self.nombre)
        self.tarea.append(self.empresa)
        self.tarea.append(self.cliente)
        self.tarea.append(self.desc)
        self.tarea.append(self.fechaI)
        self.tarea.append(self.fechaV)
        self.tarea.append(self.estado)
        self.tarea.append(self.porc)

        print("La tarea creada es la siguiente: ")
        print(f"ID de la tarea: {self.id}")
        print(f"Nombre de la tarea: {self.nombre}")
        print(f"Empresa que mando a hacer la tarea: {self.empresa}")
        print(f"Cliente a entregar la tarea: {self.cliente}")
        print(f"Descripcion de la tarea: {self.desc}")
        print(f"Fecha de Inicio de la tarea: {self.fechaI}")
        print(f"Fecha de vencimiento de la tarea: {self.fechaV}")
        print(f"Estado de la tarea: {self.estado}")
        print(f"Porcentaje que lleva la tarea: {self.porc}")
    
    #Funcion que agrega la tarea a un proyecto
    def agregar_tarea(self,lista:list):
        lista.append(self.tarea)
        print("Se ha agregado exitosamente la tarea")
    
    #Función que elimina una tarea de la lista
    def eliminar_tarea(self,lista: list):
        tarea_nombre = 'BYA'
        for i, tarea in enumerate(lista):
            if isinstance(tarea, list):
                if tarea[1] == tarea_nombre:
                    del lista[i]
                    print("Se ha eliminado la tarea exitosamente")
                    print("Actualización de las tareas")
                    print(lista)
                    return lista
                else:
                    lista[i] = eliminar_tarea(tarea)

    print("No se encontró la tarea con ese nombre")
    
    #Funcion que modifica una tarea de la lista
    def modificar_Tarea(self,lista: list, id: int, nombre: str, empresa: str, 
                 cliente: str, descripcion: str, fechaI: str, 
                 fechaV: str, estado: str, porcentaje: float):
        
        try:
            sele = int(input("Ingrese el id de la tarea que quiere modificar: "))
            if(sele > 0 and sele <= len(self.tarea)):
                self.tarea[sele-1] = [id,nombre,empresa,cliente,descripcion,fechaI,fechaV,estado,porcentaje]
                print("Se ha modificado exitosamente")
            else:
                print("No se ha podido modifcar la tarea")
            
            print("Actualización de las tareas")
            print(self.tareas)
        except:
            raise ValueError("Se equivoco en el tipo de dato")
    
    #Funcion que 
