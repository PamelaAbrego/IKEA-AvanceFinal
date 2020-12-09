from dataBaseX.dx_logic import Logic
from ikea_obj.usuarios_obj import UsuariosObj
from dataBaseX.databaseX import DatabaseX


class UsuariosLogic(Logic):
    def __init__(self):
        super().__init__()
        self.tableName= "usuarios"

    def getAllUsuarios(self):
        database = Logic()
        data = database.getAllRows(self.tableName)
        usuariosList = []
        for element in data:
            newUsuario = self.createUsuariosObj(element)
            usuariosList.append(newUsuario)
        return usuariosList

    def getUsuarioById(self, id):
        rowDict = super().getRowById(id, self.tableName)
        newUsuario = self.createUsuariosObj(rowDict)
        return newUsuario

    # polimorfismo
    def createUsuariosObj(self, id, nombreUsuario, nombre, apellido, segundoApellido, telefono, correoElectronico, contrasenna, direccion):
        usuarioObj = UsuariosObj(id, nombreUsuario, nombre, apellido, segundoApellido, telefono, correoElectronico, contrasenna, direccion)
        return usuarioObj

    def createUsuariosObj(self, usuariosDict):
        usuariosObj = UsuariosObj(
            usuariosDict["id"],
            usuariosDict["nombreUsuario"],
            usuariosDict["nombre"],
            usuariosDict["apellido"],
            usuariosDict["segundoApellido"],
            usuariosDict["telefono"],
            usuariosDict["idioma"],
            usuariosDict["correoElectronico"],
            usuariosDict["contrasenna"],
            usuariosDict["direccion"],
        )
        return usuariosObj

    def insertUsuario(self, nombreUsuario, nombre, apellido, segundoApellido, telefono, idioma, correoElectronico, contrasenna, direccion):
        database = self.database
        sql = (
            f"""INSERT INTO ikea.usuarios(nombreUsuario, nombre, apellido, segundoApellido, telefono, idioma, 
            correoElectronico, contrasenna, direccion) values ('{nombreUsuario}', '{nombre}', '{apellido}', 
            '{segundoApellido}', '{telefono}', '{idioma}', '{correoElectronico}', '{contrasenna}', '{direccion}')"""
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateUsuarioById(self, id, nombreUsuario, nombre, apellido, segundoApellido, telefono, correoElectronico, contrasenna, direccion):
        database = self.database
        sql = (
            "UPDATE ikea.usuarios "
            + f"SET nombreUsuario = '{nombreUsuario}',nombre = '{nombre}', apellido = '{apellido}',segundoApellido = '{segundoApellido}', telefono = '{telefono}',correoElectronico = '{correoElectronico}',contrasenna = '{contrasenna}', direccion = '{direccion}'"
            + f"WHERE id = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteUsuarioById(self, id):
        database = Logic()
        rows = database.deleteRowById(id, self.tableName)
        return rows
