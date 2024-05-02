class Cliente:
    def __init__(self,nom,apellido,dni):
        self.nom = nom
        self.apellido = apellido
        self.dni = dni
    
    #Getters
    def getNombre(self):
        return self.nom
    def getApellido(self):
        return self.apellido
    def getDni(self):
        return self.dni
    
    #Setters
    def setNombre(self,nom):
        self.nom = nom
    def setApellido(self,ape):
        self.apellido = ape
    def setDni(self,dni):
        self.dni = dni
    
class Articulo:
    def __init__(self,codigo,deno,precio):
        self.codigo = codigo
        self.deno = deno
        self.precio = precio
    
    #Getters
    def getCodigo(self):
        return self.codigo
    def getDeno(self):
        return self.deno
    def getPrecio(self):
        return self.precio
    
    #Setters
    def setCodigo(self,codi):
        self.codigo = codi
    def setDeno(self,deno):
        self.deno = deno
    def setPrecio(self,precio):
        self.precio = precio

class Factura(Articulo,Cliente):
    def __init__(self, codigo, deno, precio,numero,clien,linea):
        super().__init__(codigo, deno, precio)
        self.numero = numero
        self.clien = clien
        self.linea = linea
    
    def agregarArticulo(self):

        if(self.linea == 1):
            print(self.codigo)
            print(self.deno)
            print(self.precio)

        elif(self.linea == 2):
            print(self.codigo)
            print(self.deno)
            print(self.precio)
               
        elif(self.linea == 3):
            print(self.codigo)
            print(self.deno)
            print(self.precio)
                
        else:
            print("Hay solamente tres lineas")

    def PrecioTotal(self):
        return self.numero*self.precio
        
    
    def factura(self,lista,result):
        print("El cliente: ", self.clien, " compro: ")
        print("Codigo     articulo      precio")
        print("{0:^10} {1:^10} {2:^10}".format(self.codigo,self.deno,self.precio))
        print("El precio total de la factura es: " + str(result))
   
    

Clien1 = Cliente("Jose","Santana","31.608.829")
Factur1 = Factura("23567","Naranjas",3,6,Clien1.getNombre(),1)

carrito = Factur1.agregarArticulo()
precioT = Factur1.PrecioTotal()
Factur1.factura(carrito,precioT)

        