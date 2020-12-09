from dataBaseX.dx_logic import Logic
from ikea_obj.categorias_obj import CategoriasObj
from dataBaseX.databaseX import DatabaseX


class CategoriasLogic(Logic):
    def __init__(self):
        super().__init__()
        self.tableName= "categoriasproductos"

    def getAllCategorias(self):
        database = Logic()
        data = database.getAllRows(self.tableName)
        categoriasList = []
        for element in data:
            newCategoria = self.createCategoriasObj(element)
            categoriasList.append(newCategoria)
        return categoriasList

    def getCategoriaById(self, id):
        rowDict = super().getRowById(id, self.tableName)
        newCategoria = self.createCategoriasObj(rowDict)
        return newCategoria

    # polimorfismo
    def createCategoriasObj(self, id, nombre):
        categoriaObj = CategoriasObj(id, nombre)
        return categoriaObj

    def createCategoriasObj(self, categoriasDict):
        categoriasObj = CategoriasObj(
            categoriasDict["id"],
            categoriasDict["nombre"],
        )
        return categoriasObj

    def insertCategoria(self, nombreNuevo):
        database = self.database
        sql = (
            f"INSERT INTO ikea.categoriasproductos(nombre) values ('{nombreNuevo}')"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateCategoriaById(self, id, nombre):
        database = self.database
        sql = (
            "UPDATE ikea.categoriasproductos "
            + f"SET nombre = '{nombre}' "
            + f"WHERE id = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteCategoriaById(self, id):
        database = Logic()
        rows = database.deleteRowById(id, self.tableName)
        return rows
