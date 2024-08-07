import re
#Lista de contactos
class Contacto:
    def __init__(self,nombre: str, tlf: str, email: str):
        self.nombre = nombre
        self.telefono = tlf
        self.email = email
    
    #Getters
    def getNombre(self):
        return self.nombre
    
    def getTelefono(self):
        return self.telefono
    
    def getEmail(self):
        return self.email
    
    #Setters
    def setNombre(self,nombre):
        self.nombre = nombre
    
    def setTelefono(self,tlf):
        self.telefono = tlf
    
    def setEmail(self,email):
        self.email = email

#Clase para la lista de contactos que hereda la clase Contacto
class Lista(Contacto):
    def __init__(self, nombre: str, tlf: str, email: str):
        super().__init__(nombre, tlf, email)
        self.lista = []
    
    #funcion que Agrega un contacto a la lista de contactos
    def agregar_contacto(self):
        self.lista.append(self.nombre)
        self.lista.append(self.telefono)
        self.lista.append(self.email)
        return self.lista

    #Funcion que busca un contacto en la lista de contactos
    def Buscar_Contacto(self,contactos: list):
        try:
            numeroTlf = input("Ingrese el numero de telefono del contacto que quiere buscar:")
            contacto_dic = {contacto[1]: contacto for contacto in contactos}
            if numeroTlf in contacto_dic:
                print("El contacto que esta buscando si se necunetra en la lista")
                print(contacto_dic[numeroTlf])
            else:
                print("El contacto que esta bsucando no se encuentra en la lista")
        except:
            raise ValueError("El telefono esta formato int")
    
    #Funcion que elimina un contacto de la lista
    def eliminar_Contacto(self,contactos: list):
        print(contactos)
        if len(contactos) == 0:
            print("Elimino ya todos los contactos")
        else:
            eliminar = int(input("Ingrese que contacto que quiere elimnar"))
            if eliminar > 0 and eliminar <= len(contactos):
                del contactos[eliminar - 1]
            else:
                print("No se encontro el contacto al eliminar")
        print("Actualizacion de contactos")
        print(contactos)
    
    #Funcion que modifica un contacto de la lista
    def modificar_Contacto(self,contactos: list, nombre: str, tlf: str, email: str):
        print(contactos)
        modifcar = int(input("Ingrese que contacto quiere modificar: "))
        if(modifcar > 0 and modifcar <= len(contactos)):
            contactos[modifcar - 1] = [nombre,tlf,email]
        else:
            print("No se encontro el contacto a modifcar")
        
        print("Actualizacion de contactos")
        print(contactos)
    
    #Funcion que lista los contactos
    def listar_contactos(self,contactos: list):
        print("Listas de contactos")
        print("Nombre      telefono        email")
        for i in range(len(contactos)):
            print("{0:^12s}  {1:^12s} {2:^12s}".format(contactos[i][0], contactos[i][1], contactos[i][2]), "\n")

def main():
    print("Sistema de listar contactos")
    lista = []
    patronTlf = re.compile(r'^04\d{2}\d{7}$')
    patronCorreo = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    while True:
        print(" 1. Agregar Contactos ")
        print(" 2. Buscar Contactos ")
        print(" 3. Eliminar Contactos ")
        print(" 4. Modificar Contacto ")
        print(" 5. Mostrar Contactos ")
        print(" 6. Cerrar sección ")
        opc = int(input("Ingrese una opción: "))
        if opc == 1:
            cent = input("Desea agregar un contacto? (s/n): ")
            while cent.lower() == "s":
                try:
                    nombre = input("Ingrese el nombre del contacto: ")
                    tlf = input("Ingrese el telefono del contacto: ")
                    correo = input("Ingrese el email de la persona: ")
                    if patronTlf.match(tlf) and patronCorreo.match(correo):
                        conta = Lista(nombre,tlf,correo)
                        contacto = conta.agregar_contacto()
                        lista.append(contacto)
                        cent = input("Desea agregar un contacto (s/n): ")
                    else:
                        continue
                except:
                    raise ValueError("Fallo a la hoa de introducir los datos")
        elif opc == 2:
            buscar = input("Desea buscar un contacto? (s/n): ")
            while buscar.lower() == "s":
                conta.Buscar_Contacto(lista)
                buscar = input("Desea buscar un contacto? (s/n): ")
        elif opc == 3:
            eliminar = input("Desea eliminar un contacto? (s/n): ")
            while eliminar.lower() == "s":
                conta.eliminar_Contacto(lista)
                eliminar = input("Desea eliminar un contacto? (s/n): ")
        elif opc == 4:
            modificar = input("Desea modificar un contacto? (s/n): ")
            while modificar.lower() == "s":
                nombre = input("Ingrese el nombre del contacto: ")
                tlf = input("Ingrese el telefono del contacto: ")
                correo = input("Ingrese el email de la persona: ")
                conta.modificar_Contacto(lista,nombre,tlf,correo)
                modificar = input("Desea modificar un contacto? (s/n): ")
        elif opc == 5:
            conta.listar_contactos(lista)
        else:
            print("Se cierra la sección")
            lista = []



system = main()

    
        
        