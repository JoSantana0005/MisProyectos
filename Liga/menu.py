from Equipos import Equipo
from Ligas import Ligas

def main():
    ligas = []
    equi = []
    while True:
        print("1.Agregar Ligas")
        print("2.Eliminar Ligas")
        print("3.Eliminar Equipos")
        print("4.Modificar Equipos")
        opc = int(input("Ingrese una opcion: "))
        if(opc == 1):
            cent = input("Desea agregar una liga del futbol a la lista? (s/n): ")
            while cent.lower() == "s":
                nombre_liga = input("Ingrese el nombre de la liga: ")
                pais_liga = input("Ingrese el pais donde se juega la liga: ")
                partidos = int(input("Ingrese la cantidad de partidos que se juega: "))
                equipos = input("Desea agregar los equipos de la liga? (s/n): ")
                while equipos.lower() == "s":
                    nombre_equipo = input("Ingrese el nombre del equipo: ")
                    trofeos = int(input("Ingrese la cantidad de trofeos del equipo: "))
                    fundacion = int(input("Ingrese el año que se fundo el equipo: "))
                    equipo = Equipo(nombre_equipo,trofeos,fundacion)
                    lista = equipo.agregar__datos()
                    equi.append(lista)
                    print(equi)
                    equipos = input("Desea agregar los equipos de la liga? (s/n): ")
                lig = Ligas(nombre_liga,pais_liga,equi,partidos)
                liga = lig.agregar_datos()
                ligas.append(liga)
                print(ligas)
                cent = input("Desea agregar una liga del futbol a la lista? (s/n): ")

system = main()

