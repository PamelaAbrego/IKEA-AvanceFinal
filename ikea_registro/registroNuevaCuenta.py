import pymysql
from dataBaseX.dx_logic import Logic
from ikea_herramientasMenuClientes.herramientasClientes import BuscarProducto1

class RegistroNuevaCuenta:
    def __init__(self):
        self.logic = Logic()
        self.registroNuevaCuenta()
        self.idUsuario = 0

    def registroNuevaCuenta(self):
        global userName
    
        print("Crearás un nuevo Usuario:")
        name = input("Nombre: ")
        apellido = input("Apellido: ")
        segundoApellido = input("Segundo apellido: ")
        userName = input("Usuario: ")
        telefono = input("Número de teléfono: ")
        idioma = input("Idioma: ")
        correoElectronico = input("Correo electrónico: ")
        contrasenna = input("Contraseña: ")
        contrasenna2 = input("Confirma tu contraseña: ")
        direccion = input("Dirección: ")
        Existe = False
        users = []
        usuarios = []

        if contrasenna == contrasenna2:
            try:
                    sql = f"select nombreUsuario from ikea.Usuarios;"
                    users = self.logic.getAllRowsForaneas(sql)
                    for user in users:
                        usuarios.append(user["nombreUsuario"])
                    Existe = userName in usuarios

                    if Existe is True:
                        print("---------------------------------------------------")
                        print(
                            "Este nombre de usuario ya está registrado. Vuelve a intentarlo"
                        )
                        print("---------------------------------------------------")
                        self.registroNuevaCuenta()

                    else:
                        sql = f"""insert into ikea.usuarios (nombreUsuario, nombre, apellido, segundoApellido, telefono,
                            idioma, correoElectronico, contrasenna, direccion) values ('{userName}','{name}','{apellido}',
                            '{segundoApellido}','{telefono}','{idioma}','{correoElectronico}','{contrasenna}', '{direccion}');"""
                        exito = self.logic.getExito(sql)
                        
                        if exito == True: 
                            print("-----------Se agregó correctamente el usuario----------")
            finally:
                pass
        else:
            print("---------------------------------------------------")
            print("Las contraseñas ingresadas no corresponden. Vuelve a intentarlo")
            print("---------------------------------------------------")
            self.registroNuevaCuenta()







