from dataBaseX.dx_logic import Logic
from ikea_obj.paises_obj import PaisesObj
from dataBaseX.databaseX import DatabaseX


class PaisesLogic(Logic):
    def __init__(self):
        super().__init__()
        self.tableName= "paises"

    def getAllPaises(self):
        database = Logic()
        data = database.getAllRows(self.tableName)
        paisesList = []
        for element in data:
            newPais = self.createPaisesObj(element)
            paisesList.append(newPais)
        return paisesList

    def getPaisById(self, id):
        rowDict = super().getRowById(id, self.tableName)
        newPaises = self.createPaisesObj(rowDict)
        return newPaises

    # polimorfismo
    def createPaisestObj(self, id, nombre):
        paisObj = PaisesObj(id, nombre)
        return paisObj

    def createPaisesObj(self, paisesDict):
        paisObj = PaisesObj(
            paisesDict["id"],
            paisesDict["nombre"],
        )
        return paisObj

    def insertPais(self, nombreNuevo):
        database = self.database
        sql = (
            f"INSERT INTO ikea.paises(nombre) values ('{nombreNuevo}')"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updatePaisById(self, id, nombre):
        database = self.database
        sql = (
            "UPDATE ikea.paises "
            + f"SET nombre = '{nombre}' "
            + f"WHERE id = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deletePaisById(self, id):
        database = Logic()
        rows = database.deleteRowById(id, self.tableName)
        return rows
