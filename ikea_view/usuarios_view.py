from prettytable import PrettyTable
from ikea_logic.usuarios_logic import UsuariosLogic
from dataBaseX.dx_logic import Logic


class tablaUsuarios:
    def __init__(self):
        self.logic = UsuariosLogic()
        self.getAllUsuariosView()

    def getAllUsuariosView(self):
        usuariosList = self.logic.getAllUsuarios()

        table = PrettyTable()
        table.field_names = [
            "Id",
            "NombreUsuario",
            "Nombre",
            "Apellido",
            "Segundo Apellido",
            "Teléfono",
            "Idioma",
            "Correo Electrónico",
            "Contraseña",
            "Dirección",
        ]

        for usuario in usuariosList:
            table.add_row([usuario.id, usuario.nombreUsuario,usuario.nombre, usuario.apellido, usuario.segundoApellido, usuario.telefono, usuario.idioma, usuario.correoElectronico, usuario.contrasenna, usuario.direccion])
        print(table)
        table.clear()

    def addNewUsuarioView(self):
        print("Crearás un nuevo Usuario")
        nombreUsuario = input("Nombre Usuario:")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        segundoApellido = input("Segundo apellido: ")
        username = input("Usuario: ")
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
                    rowList = Logic().getRegistros(sql)
                    for user in rowList:
                        usuarios.append(user["nombreUsuario"])
                    Existe = username in usuarios

                    if Existe is True:
                        print("---------------------------------------------------")
                        print(
                            "Este nombre de usuario ya está registrado, vuelve a intentarlo"
                        )
                        print("---------------------------------------------------")
                        addNewUsuariosView()

                    else:
                        insertar = self.logic.insertUsuario(nombreUsuario, nombre, apellido, segundoApellido, telefono, idioma, correoElectronico, contrasenna, direccion)
                        if insertar > 0:
                            print(f"---El usuario con nombre de usuario '{nombreUsuario}' se agregó con éxito.---")
            finally:
                pass
        else:
            print("---------------------------------------------------")
            print("Las contraseñas ingresadas no corresponden, vuelve a intentarlo")
            print("---------------------------------------------------")
            addNewUsuarioView()
        self.getAllUsuariosView()

    def updateUsuarioView(self):
        print("Se está actualizando la información de un Usuario: ")
        self.getAllUsuariosView()
        id = int(input("Id del Usuario a actualizar: "))
        usuario = self.logic.getUsuarioById(id)

        update = int(input("¿Desea actualizar el nombre del usuario? 0.No, 1.Sí: "))
        if update == 1:
            print(f"Nombre anterior: {usuario.nombreUsuario}")
            nombreUsuario = input("Nuevo nombre de Usuario: ")
        else:
            nombreUsuario = usuario.nombreUsuario

        update = int(input("¿Desea actualizar el nombre? 0.No, 1.Sí: "))
        if update == 1:
            print(f"Nombre anterior: {usuario.nombre}")
            nombre = input("Nuevo nombre: ")
        else:
            nombre = usuario.nombre

        update = int(input("¿Desea actualizar el apellido? 0.No, 1.Sí: "))
        if update == 1:
            print(f"Apellido anterior: {usuario.apellido}")
            apellido = input("Nuevo apellido: ")
        else:
            apellido = usuario.apellido

        update = int(input("¿Desea actualizar el segundo apellido? 0.No, 1.Sí: "))
        if update == 1:
            print(f"Segundo Apellido anterior: {usuario.segundoApellido}")
            segundoApellido = input("Nuevo Segundo apellido: ")
        else:
            segundoApellido = usuario.segundoApellido

        update = int(input("¿Desea actualizar el teléfono? 0.No, 1.Sí: "))
        if update == 1:
            print(f"Teléfono anterior: {usuario.telefono}")
            telefono = input("Nuevo teléfono: ")
        else:
            telefono = usuario.telefono

        update = int(input("¿Desea actualizar el idioma? 0.No, 1.Sí: "))
        if update == 1:
            print(f"Idioma anterior: {usuario.idioma}")
            idioma = input("Nuevo idioma: ")
        else:
            idioma = usuario.idioma

        update = int(input("¿Desea actualizar el correo electrónico? 0.No, 1.Sí: "))
        if update == 1:
            print(f"Correo Electrónico anterior: {usuario.correoElectronico}")
            correoElectronico = input("Nuevo correo electrónico: ")
        else:
            correoElectronico = usuario.correoElectronico

        update = int(input("¿Desea actualizar la contraseña? 0.No, 1.Sí: "))
        if update == 1:
            print(f"Contraseña anterior: {usuario.contrasenna}")
            contrasenna = input("Nueva contraseña: ")
        else:
            contrasenna = usuario.contrasenna

        update = int(input("¿Desea actualizar la dirección? 0.No, 1.Sí: "))
        if update == 1:
            print(f"Dirección anterior: {usuario.direccion}")
            direccion = input("Nueva dirección: ")
        else:
            direccion = usuario.direccion

        updateFinal = self.logic.updateUsuarioById(id, nombreUsuario, nombre, apellido, segundoApellido, telefono, correoElectronico, contrasenna, direccion)

        if update >0:
            print(f"---Se actualizó con éxito el usuario con id: {usuario.id}.---")

        self.getAllUsuariosView()

    def deleteUsuarioView(self):
        print("Se está eliminando un Usuario: ")
        self.getAllUsuariosView()
        id = int(input("Id del usuario a eliminar: "))
        
        delete = self.logic.deleteUsuarioById(id)

        if delete > 0:
            print(f"---Se borró con éxito el usuario con id: {id}.---")

        self.getAllUsuariosView()
