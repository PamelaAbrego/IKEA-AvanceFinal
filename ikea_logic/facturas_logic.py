from dataBaseX.dx_logic import Logic
from ikea_obj.facturas_obj import FacturasObj
from dataBaseX.databaseX import DatabaseX


class FacturasLogic(Logic):
    def __init__(self):
        super().__init__()
        self.tableName= "facturas"

    def getAllFacturas(self):
        database = Logic()
        sql = f"""SELECT facturas.id, facturas.idUsuarios, usuarios.nombreUsuario, facturas.tipoDePago, facturas.idSucursales,
            sucursales.direccion as direccion, facturas.fecha, facturas.hora, facturas.numeroCarrito, facturas.total
            FROM ikea.usuarios inner join ikea.facturas on usuarios.id = facturas.idUsuarios
            inner join ikea.sucursales on facturas.idSucursales = sucursales.id;"""
        data = database.getAllRowsForaneas(sql)
        facturasList = []
        for element in data:
            newFactura = self.createFacturasObj(element)
            facturasList.append(newFactura)
        return facturasList

    def getFacturaById(self, id):
        sql = f"""SELECT facturas.id, facturas.idUsuarios, usuarios.nombreUsuario, facturas.tipoDePago, facturas.idSucursales,
            sucursales.direccion as direccion, facturas.fecha, facturas.hora, facturas.numeroCarrito, facturas.total
            FROM ikea.usuarios inner join ikea.facturas on usuarios.id = facturas.idUsuarios
            inner join ikea.sucursales on facturas.idSucursales = sucursales.id
            where facturas.id={id};"""
        rowDict = super().getRowsByIdForaneas(sql)
        newFactura = self.createFacturasObj(rowDict)
        return newFactura

    # polimorfismo
    def createFacturasObj(self, id, idUsuarios, nombreUsuario, tipoDePago, idSucursales, direccion,fecha, hora, numeroCarrito, total):
        facturasObj = FacturasObj(id, idUsuarios, nombreUsuario, tipoDePago, idSucursales, direccion,fecha, hora, numeroCarrito, total)
        return facturasObj

    def createFacturasObj(self, facturasDict):
        facturasObj = FacturasObj(
            facturasDict["id"],
            facturasDict["idUsuarios"],
            facturasDict["nombreUsuario"],
            facturasDict["tipoDePago"],
            facturasDict["idSucursales"],
            facturasDict["direccion"],
            facturasDict["fecha"],
            facturasDict["hora"],
            facturasDict["numeroCarrito"],
            facturasDict["total"],
        )
        return facturasObj

    def insertFactura(self, idUsuarios, tipoDePago, idSucursales, fecha, hora, numeroCarrito, total):
        database = self.database
        sql = (
            f"INSERT INTO ikea.facturas(idUsuarios, tipoDePago, idSucursales,fecha, hora, numeroCarrito, total) values ('{idUsuarios}','{tipoDePago}','{idSucursales}','{fecha}', '{hora}','{numeroCarrito}','{total}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateFacturaById(self, id, idUsuarios, tipoDePago, idSucursales, fecha, hora, numeroCarrito, total):
        database = self.database
        sql = (
            "UPDATE ikea.facturas "
            + f"SET idUsuarios = '{idUsuarios}', tipoDePago = '{tipoDePago}', idSucursales = '{idSucursales}', fecha = '{fecha}', hora = '{hora}', numeroCarrito = '{numeroCarrito}', total = '{total}'"
            + f"WHERE id = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteFacturaById(self, id):
        database = Logic()
        rows = database.deleteRowById(id, self.tableName)
        return rows

