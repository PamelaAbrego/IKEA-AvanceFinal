from dataBaseX.dx_logic import Logic
from ikea_obj.carrito_obj import CarritoObj
from dataBaseX.databaseX import DatabaseX


class CarritoLogic(Logic):
    def __init__(self):
        super().__init__()
        self.tableName= "carritosdecompras"

    def getAllCarritos(self):
        database = Logic()
        sql = f"""SELECT carritosdecompras.id, carritosdecompras.numeroCarrito ,carritosdecompras.idUsuario, usuarios.nombreUsuario, 
        carritosdecompras.idProducto, productos.nombre as nombreProducto, carritosdecompras.cantidad FROM ikea.usuarios 
        inner join ikea.carritosdecompras on usuarios.id = carritosdecompras.idUsuario inner join ikea.productos 
        on productos.id= carritosdecompras.idProducto;"""
        data = database.getAllRowsForaneas(sql)
        carritosList = []
        for element in data:
            newCarrito = self.createCarritosObj(element)
            carritosList.append(newCarrito)
        return carritosList

    def getCarritoById(self, id):
        sql = f"""SELECT carritosdecompras.id, carritosdecompras.numeroCarrito, carritosdecompras.idUsuario, usuarios.nombreUsuario, 
        carritosdecompras.idProducto, productos.nombre as nombreProducto, carritosdecompras.cantidad FROM ikea.usuarios 
        inner join ikea.carritosdecompras on usuarios.id = carritosdecompras.idUsuario inner join ikea.productos 
        on productos.id= carritosdecompras.idProducto where carritosdecompras.id={id};"""
        rowDict = super().getRowsByIdForaneas(sql)
        newCarrito = self.createCarritosObj(rowDict)
        return newCarrito

    # polimorfismo
    def createCarritosObj(self, id, numeroCarrito, idUsuario, nombreUsuarios, idProducto, nombreProducto, cantidad):
        carritoObj = CarritoObj(id, idUsuario, numeroCarrito, nombreUsuarios, idProducto, nombreProducto, cantidad)
        return carritoObj

    def createCarritosObj(self,carritosDict):
        carritoObj = CarritoObj(
            carritosDict["id"],
            carritosDict["numeroCarrito"],
            carritosDict["idUsuario"],
            carritosDict["nombreUsuario"],
            carritosDict["idProducto"],
            carritosDict["nombreProducto"],
            carritosDict["cantidad"],
        )
        return carritoObj

    def insertCarrito(self, numeroCarrito, idUsuario,idProducto,cantidad):
        database = self.database
        sql = (
            f"INSERT INTO ikea.carritosdecompras(numeroCarrito,idUsuario,idProducto, cantidad) values ('{numeroCarrito}','{idUsuario}','{idProducto}','{cantidad}')"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateCarritoById(self, id, numeroCarrito, idUsuario,idProducto,cantidad):
        database = self.database
        sql = (
            "UPDATE ikea.carritosdecompras "
            + f"SET numeroCarrito = '{numeroCarrito}', idUsuario = '{idUsuario}', idProducto = '{idProducto}', cantidad = '{cantidad}' "
            + f"WHERE id = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteCarritoById(self, id):
        database = Logic()
        rows = database.deleteRowById(id, self.tableName)
        return rows

