from dataBaseX.dx_logic import Logic
from ikea_obj.sucursales_obj import SucursalesObj
from dataBaseX.databaseX import DatabaseX


class SucursalesLogic(Logic):
    def __init__(self):
        super().__init__()
        self.tableName= "sucursales"

    def getAllSucursales(self):
        database = Logic()
        sql = f"""SELECT sucursales.id, sucursales.direccion, sucursales.idCiudades, ciudades.nombre as nombreCiudad,
        sucursales.telefono, sucursales.horarios FROM ikea.sucursales inner join ikea.ciudades on
        sucursales.idCiudades = ciudades.id;"""
        data = database.getAllRowsForaneas(sql)
        sucursalesList = []
        for element in data:
            newSucursal = self.createSucursalesObj(element)
            sucursalesList.append(newSucursal)
        return sucursalesList

    def getSucursalById(self, id):
        sql = f"""SELECT sucursales.id, sucursales.direccion, sucursales.idCiudades, ciudades.nombre as nombreCiudad,
        sucursales.telefono, sucursales.horarios FROM ikea.sucursales inner join ikea.ciudades on
        sucursales.idCiudades = ciudades.id where sucursales.id={id};"""
        rowDict = super().getRowsByIdForaneas(sql)
        newSucursal = self.createSucursalesObj(rowDict)
        return newSucursal

    # polimorfismo
    def createSucursalesObj(self, id, direccion, idCiudades, nombreCiudad, telefono, horarios):
        sucursalObj = SucursalesObj(id, direccion, idCiudades, nombreCiudad, telefono, horarios)
        return sucursalObj

    def createSucursalesObj(self, sucursalesDict):
        sucursalesObj = SucursalesObj(
            sucursalesDict["id"],
            sucursalesDict["direccion"],
            sucursalesDict["idCiudades"],
            sucursalesDict["nombreCiudad"],
            sucursalesDict["telefono"],
            sucursalesDict["horarios"],
        )
        return sucursalesObj

    def insertSucursal(self, direccion, idCiudades, telefono, horarios):
        database = self.database
        sql = (
            f"INSERT INTO ikea.sucursales(direccion, idCiudades, telefono, horarios) values ('{direccion}','{idCiudades}','{telefono}','{horarios}')"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateSucursalById(self, id ,direccion, idCiudades, telefono, horarios):
        database = self.database
        sql = (
            "UPDATE ikea.sucursales "
            + f"SET direccion = '{direccion}', idCiudades = '{idCiudades}', telefono = '{telefono}', horarios = '{horarios}' "
            + f"WHERE id = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteSucursalById(self, id):
        database = Logic()
        rows = database.deleteRowById(id, self.tableName)
        return rows

