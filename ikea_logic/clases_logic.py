from dataBaseX.dx_logic import Logic
from ikea_obj.clases_obj import ClasesObj
from dataBaseX.databaseX import DatabaseX


class ClasesLogic(Logic):
    def __init__(self):
        super().__init__()
        self.tableName= "claseproductos"

    def getAllClases(self):
        database = Logic()
        sql = f"""SELECT claseproductos.id, claseproductos.nombre, claseproductos.idCategoriasProductos,
        categoriasproductos.nombre as nombreCategoria FROM ikea.claseproductos inner join
        ikea.categoriasproductos on claseproductos.idCategoriasProductos = categoriasproductos.id;"""
        data = database.getAllRowsForaneas(sql)
        clasesList = []
        for element in data:
            newClase = self.createClasesObj(element)
            clasesList.append(newClase)
        return clasesList

    def getClaseById(self, id):
        sql = f"""SELECT claseproductos.id, claseproductos.nombre, claseproductos.idCategoriasProductos,
        categoriasproductos.nombre as nombreCategoria FROM ikea.claseproductos inner join ikea.categoriasproductos
        on claseproductos.idCategoriasProductos = categoriasproductos.id where claseproductos.id={id};"""
        rowDict = super().getRowsByIdForaneas(sql)
        newClase = self.createClasesObj(rowDict)
        return newClase

    # polimorfismo
    def createClasesObj(self, id, nombre, idPaises, nombrePais):
        claseObj = ClasesObj(id, nombre, idCategoriasProductos, nombreCategoria)
        return claseObj

    def createClasesObj(self, clasesDict):
        clasesObj = ClasesObj(
            clasesDict["id"],
            clasesDict["nombre"],
            clasesDict["idCategoriasProductos"],
            clasesDict["nombreCategoria"],
        )
        return clasesObj

    def insertClase(self, nombreNuevo, idCategoriasProductos):
        database = self.database
        sql = (
            f"INSERT INTO ikea.claseproductos(nombre, idCategoriasProductos) values ('{nombreNuevo}','{idCategoriasProductos}')"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateClaseById(self, id, nombre, idCategoriasProductos):
        database = self.database
        sql = (
            "UPDATE ikea.claseproductos "
            + f"SET nombre = '{nombre}', idCategoriasProductos = '{idCategoriasProductos}'"
            + f"WHERE id = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteClaseById(self, id):
        database = Logic()
        rows = database.deleteRowById(id, self.tableName)
        return rows

