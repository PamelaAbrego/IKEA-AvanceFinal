from ikea_registro.registroCuentaExistente import RegistroCuentaExistente
from ikea_registro.registroNuevaCuenta import RegistroNuevaCuenta
from ikea_menu.menuClientes import MenuClientes


class MenuRegistro:
    def __init__(self):
        while True:
            print("Bienvenido a la tienda IKEA")
            print("Registro:")
            print("0 - Regresar.")
            print("1 - Ingresar con una cuenta existente.")
            print("2 - Crear nueva cuenta.")

            option = int(input("Opción: "))

            if option == 0:
                print("------------------------------------------")
                print("Saliendo de modo Cliente.")
                print("------------------------------------------")
                break

            if option == 1:
                print("------------------------------------------")
                print("--Ingreso con cuenta existente--")
                self.obj = RegistroCuentaExistente()
                self.var = self.obj.saveUser()
                self.var2 = self.obj.saveIdCarrito()
                self.var3 = self.obj.saveSucursal()
                self.obj2 = MenuClientes()
                self.obj2.storeVariable(self.var,self.var2,self.var3)
                self.obj2.Home()
                print("------------------------------------------")

            if option == 2:
                print("------------------------------------------")
                print("--Creación de una nueva cuenta--")
                RegistroNuevaCuenta()
                print("------------------------------------------")

    def getUserId(self):
        return self.var

    def getCarritoNum(self):
        return self.var2

    def getIdSucursal(self):
        return self.var3



