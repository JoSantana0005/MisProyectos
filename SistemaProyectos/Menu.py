from Proyectos import Proyectos
from Tareas import Tareas
from datetime import datetime

def main():
    print("Bienvenido al sistema avanzado de proyectos")
    print("Que desea hacer?")
    print("1.proyectos")
    print("2.Consultar proyectos")
    proyectos = []
    tareas = []
    id = 0
    idT = 0
    opc = int(input("Ingrese la opción: "))
    while True:
        if(opc == 1):
            print("Que desea hacer?")
            print("1.Crear Proyectos")
            print("2.Eliminar proyectos")
            print("3.Modifica proyectos")
            print("4.Consultar proyectos")
            opc = int(input("Ingrese una opción: "))
            if(opc == 1):
                try:
                    #Crear es el proyecto y le pregutamos al usuario si quiere crear una tarea y agregarla al proyecto
                    crear = input("Desea crear un proyecto? (s/n): ")
                    while crear.lower() == "s":
                        id += 1
                        nombre = input("Ingrese el nombre del proyecto: ").upper()
                        desc = input("Ingrese la Descripción del proyecto: ")
                        fecha = input("Ingrese la fecha de inicio del proyecto (YYYY-MM-DD): ")
                        fechaI = datetime.strptime(fecha,"%Y-%m-%d")
                        vencimiento = input("Ingrese la fecha de vencimiento del proyecto (YYYY-MM-DD): ")
                        fechaV = datetime.strptime(vencimiento,"%Y-%m-%d")
                        estado = input("Ingrese el estado del proyecto: ")
                        empresa = input("Ingrese la empresa encargada del proyecto: ").upper()
                        equipo = input("Ingrese el equipo encargado del proyecto: ")
                        proyecto = Proyectos(id,nombre,desc,fechaI.date(),fechaV.date(),estado,empresa,equipo)
                        proyecto.crear__Proyecto()
                        
                        crearTarea = input("Desea crear tareas a este proyecto? (s/n): ")
                        while crearTarea.lower() == "s":
                            idT += 1
                            nombreT = input("Ingrese el nombre de la tarea: ").upper()
                            cliente = input("Ingrese el nombre del cliente: ")
                            DescT = input("Ingrese la descripción de la tarea: ")
                            inicio = input("Ingrese la fecha de inicio de la tarea (YYYY-MM-DD):")
                            fechaIT = datetime.strptime(inicio,"%Y-%m-%d")
                            vencimiento = input("Ingrese la fecha de vencimiento de la tarea (YYYY-MM-Dd): ")
                            fechaVT = datetime.strptime(vencimiento, "%Y-%m-%d")
                            estadoT = input("Ingrese el estado de la tarea: ")
                            porc = input("Ingrese el porcentaje de la tarea: ")
                            tarea = Tareas(idT,nombreT,empresa,cliente,DescT,fechaIT.date(),fechaVT.date(),estadoT,porc)
                            tarea.crear__tarea()

                            agregarTarea = input("Desea agregar esta tarea al proyecto? (s/n): ")
                            if(agregarTarea.lower() == "s"):
                                tarea.agregar__Tarea(proyecto.Proyectos,tareas)
                            else:
                                print("No se agrego la tarea al proyecto")
                            crearTarea = input("Desea crear tareas a este proyecto? (s/n): ")
                        
                        agregar = input("Desea agregar este proyecto a la lista? (s/n): ")
                        if(agregar.lower() == "s"):
                            proyecto.agregar__Proyectos(proyectos)
                        else:
                            print("No se ha agregado el proyecto a la lista")
                        crear = input("Desea crear un proyecto? (s/n): ")
                except:
                    raise ValueError("Error: Dato invalido")
                print(proyectos)
            if(opc == 2):
                #Preguntamos primero si quiere eliminar una tarea , despues pregutamos si quiere borrar todo el proyecto
                try:
                    eliminarTarea = input("Desea eliminar una tarea de un proyecto? (s/n): ")
                    while eliminarTarea.lower() == "s":
                        tarea.elimina__tarea(proyectos,tareas)
                        eliminarTarea = input("Desea eliminar una tarea de un proyecto? (s/n): ")
                
                    eliminar = input("Desea eliminar un proyecto? (s/n): ")
                    while eliminar.lower() == "s":
                        proyecto.elimina__proyecto(proyectos)
                        eliminar = input("Desea eliminar un proyecto? (s/n): ")
                except:
                    raise ValueError("Error: Dato invalido")
            if(opc == 3):
                #Pregutamos primero si el usuario quiere modificar una tarea , despues pregutamos si quiere modificar un proyecto
                try:
                    modificarTarea = input("Desea modificar una tarea del proyecto? (s/n): ")
                    while modificarTarea.lower() == "s":
                        idnuevoT = int(input("Ingrese el nuevo id de la tarea: "))
                        nombrenuevo = input("Ingrese el nuevo nombre de la tarea: ")
                        empresanueva = input("Ingrese la nueva empresa que mando la tarea: ")
                        clientenuevo = input("Ingrese el nuevo cliente: ")
                        descnuevo = input("Ingrese la nueva descripción de la tarea: ")
                        inicionuevo = input("Ingrese la nueva fecha de inicio de la tarea (YYYY-MM-DD): ")
                        fechaInueva = datetime.strptime(inicionuevo,"%Y-%m-%d")
                        vencimientonuevo = input("Ingrese la nueva fecha de vencimiento de la tarea (YYYY-MM-DD): ")
                        fechaVnueva = datetime.strptime(vencimientonuevo,"%Y-%m-%d")
                        estadonuevo = input("Ingrese el nuevo estado de la tarea: ")
                        porcnuevo = input("Ingrese el nuevo porcentaje de la tarea: ")
                        tarea.modificar__tarea(proyectos,tareas,idnuevoT,nombrenuevo,empresanueva,clientenuevo,
                                               descnuevo,fechaInueva,fechaVnueva,estadonuevo,porcnuevo)
                        modificarTarea = input("Desea modificar una tarea del proyecto? (s/n): ")

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
                        proyecto.modificar__proyecto(proyectos,id,nombre,Desc,fechaI,fechaV,estado,empresa,equipo)
                        modificar = input("Desea modificar un proyecto? (s/n): ")
                except:
                    raise ValueError("Error: Dato invalido")
            if(opc == 4):
                #Pregutamos primero si el usuario quiere consultar una tarea y despues pregutamos si quiere consultar un proyecto
                try:
                    consultar = input("Desea consultar un proyecto? (s/n): ")
                    while consultar.lower() == "s":
                        proyecto.consultar__Proyecto(proyectos)
                        consultar = input("Desea consultar un proyecto? (s/n): ")
                except:
                    raise ValueError("Error: Dato invalido")

system = main() 

                
        