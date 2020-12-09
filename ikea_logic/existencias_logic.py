from dataBaseX.dx_logic import Logic
from ikea_obj.existencias_obj import ExistenciasObj
from dataBaseX.databaseX import DatabaseX


class ExistenciasLogic(Logic):
    def __init__(self):
        super().__init__()
        self.tableName= "existencias"

    def getAllExistencias(self):
        database = Logic()
        sql = f"""SELECT existencias.id, existencias.idProductos, productos.nombre as nombreProducto, 
        existencias.idSucursales, sucursales.direccion, existencias.cantidad FROM ikea.productos inner join ikea.existencias on 
        productos.id = existencias.idProductos inner join ikea.sucursales on sucursales.id= existencias.idSucursales;"""
        data = database.getAllRowsForaneas(sql)
        existenciasList = []
        for element in data:
            newExistencia = self.createExistenciasObj(element)
            existenciasList.append(newExistencia)
        return existenciasList

    def getExistenciaById(self, id):
        sql = f"""SELECT existencias.id, existencias.idProductos, productos.nombre as nombreProducto, 
        existencias.idSucursales, sucursales.direccion, existencias.cantidad FROM ikea.productos inner join ikea.existencias on 
        productos.id = existencias.idProductos inner join ikea.sucursales on sucursales.id= existencias.idSucursales 
        where existencias.id={id};"""
        rowDict = super().getRowsByIdForaneas(sql)
        newExistencia = self.createExistenciasObj(rowDict)
        return newExistencia

    # polimorfismo
    def createExistenciasObj(self, id, idProductos, nombreProducto, idSucursales, direccion, cantidad):
        existenciaObj = ExistenciasObj(id, idProductos, nombreProducto, idSucursales, direccion, cantidad)
        return existenciaObj

    def createExistenciasObj(self,existenciasDict):
        existenciasObj = ExistenciasObj(
            existenciasDict["id"],
            existenciasDict["idProductos"],
            existenciasDict["nombreProducto"],
            existenciasDict["idSucursales"],
            existenciasDict["direccion"],
            existenciasDict["cantidad"],
        )
        return existenciasObj

    def insertExistencia(self, idProductos,idSucursales,cantidad):
        database = self.database
        sql = (
            f"INSERT INTO ikea.existencias(idProductos,idSucursales, cantidad) values ('{idProductos}','{idSucursales}','{cantidad}')"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateExistenciaById(self, id, idProductos,idSucursales,cantidad):
        database = self.database
        sql = (
            "UPDATE ikea.existencias "
            + f"SET idProductos = '{idProductos}', idSucursales = '{idSucursales}', cantidad = '{cantidad}' "
            + f"WHERE id = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteExistenciaById(self, id):
        database = Logic()
        rows = database.deleteRowById(id, self.tableName)
        return rows

