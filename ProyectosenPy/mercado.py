class Producto:
    def __init__(self,nombre,descripcion,precio,cantidad):
        self.nombre = nombre
        self.descr = descripcion
        self.precio = precio
        self.cant = cantidad
    
    #Getters
    def getNombre(self):
        return self.nombre
    def getDescripcion(self):
        return self.descr
    def getPrecio(self):
        return self.precio
    def getCantidad(self):
        return self.cant

    #Setters
    def setNombre(self,nombre):
        self.nombre = nombre
    def setDescripcion(self,desc):
        self.descr = desc
    def setPrecio(self,precio):
        self.precio = precio
    def setCantidad(self,cantidad):
        self.cantidad = cantidad
class ProductoconOpciones:
    def __init__(self):
        self.opciones = {}
    
    #Funcion de agregar una opcion al producto
    def agregar_opcion(self):
        cent = input("Desea agregar una opción al producto: (s/n)")
        while cent.lower() == "s":
            key = input("Ingrese la opcion del producto: ")
            item = input("Ingrese la o las formas del producto: ")
            self.opciones[key] = item.split(",")
            cent = input("Desea agregar una opción al producto: (s/n)")

        result = self.opciones
        return result
    #Funcion que muestra las opciones que tiene el producto
    def mostrar_opciones(self):
        print("Lista de opciones que tiene el producto")
        for key,item in self.opciones.items():
            print(key,item)

class Carrito(Producto):
    def __init__(self, nombre, descripcion, precio, cantidad,opciones):
        super().__init__(nombre, descripcion, precio, cantidad)
        self.opc = opciones
        self.carrito = []
    
    #Funcion que agrega productos al carrito
    def agregar_producto(self):
        formas = list(self.opc.values())
        print(formas)
        forma = input("La forma que quiere del producto: ")
        if forma in [item for sublist in formas for item in sublist]:
            self.carrito.append(forma)
            self.carrito.append(self.nombre)
            self.carrito.append(self.descr)
            self.carrito.append(self.precio)
            self.carrito.append(self.cant)
        else:
            print("No es una forma de las seleccionadas")
            self.carrito.append(self.nombre)
            self.carrito.append(self.descr)
            self.carrito.append(self.precio)
            self.carrito.append(self.cant)
        result = self.carrito
        return result
    #Funcion que elimina un producto del carrito
    def eliminar_producto(self,carrito):
        seleccion = int(input("Ingrese el numero del producto que quiere eliminar: "))
        for i in range(1,len(carrito)):
            if(seleccion > 0 and seleccion <= len(carrito)):
                del carrito[seleccion-1]
            else:
                print("No se pudo eliminar el producto del carrito")
        print("Actualización del carrito")
        print(carrito)
    #Funcion que calcula el precio total de la compra
    def precio_total(self,productos):
        precio_tot = 0
        for producto in productos:
            precio = producto[3]
            cantidad = producto[4]
            precio_tot += cantidad*precio
        return precio_tot

class Orden:
    def __init__(self,lista,precioTotal):
        self.listaP = lista
        self.total = precioTotal
    #Muestra la factura
    def mostrar_factura(self):
        print("Opcion   nombreP     descripcion    precio      cantidad")
        for i in range(0,len(self.listaP)):
            print("{0:^6s} {1:^8s} {2:^10s} {3:^12.2f} {4:^18d}".
                  format(self.listaP[i][0],self.listaP[i][1],self.listaP[i][2], self.listaP[i][3], self.listaP[i][4]), "\n")
        
        print("El precio total de la compra es: " + str(self.total))

def main():
    while True:
        print("Bienvenido al mercado")
        opcPrdocuto = ProductoconOpciones()
        opciones = opcPrdocuto.agregar_opcion()
        opcPrdocuto.mostrar_opciones()
        carrito = []

        cent = input("Desea agregar productos al carrito (s/n): ")
        while cent.lower() == "s":
            nombreP = input("Ingrese el nombre del producto que se va agregar al carrito: ")
            desc = input("Ingrese la descripcion del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cant = int(input("Ingrese la cantidad del producto: "))
            carro = Carrito(nombreP,desc,precio,cant,opciones)
            productos = carro.agregar_producto()
            carrito.append(productos)
            cent = input("Desea agregar productos al carrito (s/n): ")

        cent2 = input("Desea eliminar un producto del carrito (s/n): ")
        while cent2.lower() == "s":
            carro.eliminar_producto(carrito)
            cent2 = input("Desea eliminar un producto del carrito (s/n): ")
        precio = carro.precio_total(carrito)
        print("Se muestra la siguiente factura")
        orden = Orden(carrito,precio)
        orden.mostrar_factura()
        break

menu = main()

        
