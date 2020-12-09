from ikea_herramientasMenuClientes.herramientasClientes import BuscarProducto1
from ikea_herramientasMenuClientes.verCarrito import lookCarrito
from datetime import datetime


class MenuClientes:
    def __init__(self):
        pass

    def Home(self):
        self.now = str(datetime.now())
        self.anho = self.now[:10]
        self.hora = self.now[11:19]
        self.obj2 = BuscarProducto1()
        self.obj3 = lookCarrito()
        while True:
            print("Bienvenido a la tienda IKEA")
            print("Menu: ")
            print("0 - Regresar.")
            print("1 - Buscar Producto")
            print("2 - Ver mi carrito")

            option = int(input("Opción: "))

            if option == 0:
                print("------------------------------------------")
                print("Saliendo de modo Cliente.")
                print("------------------------------------------")
                break
            if option == 1:
                print("------------------------------------------")
                self.obj2.BuscarProducto(self.idUser, self.idCarrito, self.idSucursal)
                self.Home()
                print("------------------------------------------")
                break
            if option ==2:
                print("------------------------------------------")
                self.obj3.lookForCarrito(self.idCarrito)
                print("Opciones: ")
                print("0. Regresar")
                print("1. Eliminar un producto de mi carrito")
                print("2. Confirmar compra")
                deci = int(input("Escribe el número de la opción que deseas realizar: "))
                
                if deci == 1:
                     self.obj3.eliminarDeCarrito(self.idCarrito)

                print("------------------------------------------")

                if deci ==2:
                    self.Total = self.obj3.getTotal(self.idCarrito)
                    self.obj3.AgregarFactura(self.idCarrito, self.idSucursal, self.idUser, self.anho, self.hora, self.Total)
                    self.obj3.agregarAFacturas(self.idCarrito, self.idSucursal)
                    print("Muchas gracias por tu compra en IKEA. Te esperamos pronto :)")
                    break

    def storeVariable(self, idUser, idCarrito, idSucursal):
        self.idUser = idUser
        self.idCarrito = idCarrito
        self.idSucursal = idSucursal
