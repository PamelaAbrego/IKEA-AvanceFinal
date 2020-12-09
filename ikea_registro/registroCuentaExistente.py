from dataBaseX.dx_logic import Logic
from ikea_view.sucursales_view import tablaSucursales
from ikea_menu.menuClientes import MenuClientes

class RegistroCuentaExistente:
    def __init__(self):
        self.logic = Logic()
        self.registroCuentaExistente()
        self.idUser
        self.idCarrito
        self.sucursal

    def registroCuentaExistente(self):
        self.Username = str(input("Nombre Usuario: "))
        self.Contrasenna = str(input("Contraseña: "))
        Existe = False
        users = []
        username = []
        try:
                sql = f"select nombreUsuario from ikea.Usuarios;"
                users = self.logic.getAllRowsForaneas(sql)
                for user in users:
                    username.append(user["nombreUsuario"])

                Existe = self.Username in username

                if Existe is True:
                    sql2 = f"select contrasenna from ikea.usuarios where nombreUsuario = '{self.Username}';"
                    resulta = self.logic.getRowsByIdForaneas(sql2)
                    password = resulta["contrasenna"]

                    if self.Contrasenna == password:
                        print("---------------------------------------")
                        print("--Ingreso realizado con éxito--")
                        print("---------------------------------------")

                        sql3 = f"select id from ikea.Usuarios where nombreUsuario = '{self.Username}';"
                        resultado = self.logic.getRowsByIdForaneas(sql3)
                        self.idUser = resultado["id"]

                        print("Debes elegir una sucursal dónde buscar tus productos")
                        obj2 = tablaSucursales()
                        self.sucursal = int(input("Escribe el id de la sucursal que deseas: "))
                        try:
                            sql4 = f"select numeroCarrito from ikea.carritosdecompras order by numeroCarrito desc limit 1;"
                            resultado = self.logic.getRowsByIdForaneas(sql4)
                            self.idCar = resultado["numeroCarrito"]
        
                        finally:
                            self.idCarrito = (self.idCar) + 1
                            MenuClientes()

                            

                    else:
                        print("---------------------------------------")
                        print(
                            "--El usuario o la contraseña están incorrectas. Vuelve a intentarlo--"
                        )
                        print("---------------------------------------")
                        self.registroCuentaExistente()

                else:
                    print("---------------------------------------")
                    print(
                        "--No se ha encontrado este nombre de usuario. Vuelve a intentarlo--"
                    )
                    print("---------------------------------------")
                    self.registroCuentaExistente()
        finally:
            pass

    def saveUser(self):
        return self.idUser

    def saveIdCarrito(self):
        return self.idCarrito

    def saveSucursal(self):
        return self.sucursal


