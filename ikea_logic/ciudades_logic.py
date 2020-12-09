from dataBaseX.dx_logic import Logic
from ikea_obj.ciudades_obj import CiudadesObj
from dataBaseX.databaseX import DatabaseX


class CiudadesLogic(Logic):
    def __init__(self):
        super().__init__()
        self.tableName= "ciudades"

    def getAllCiudades(self):
        database = Logic()
        sql = f"""SELECT ciudades.id, ciudades.nombre, ciudades.idPaises, paises.nombre as nombrePais 
        FROM ikea.ciudades inner join ikea.paises on ciudades.idPaises = paises.id;"""
        data = database.getAllRowsForaneas(sql)
        ciudadesList = []
        for element in data:
            newCiudad = self.createCiudadesObj(element)
            ciudadesList.append(newCiudad)
        return ciudadesList

    def getCiudadById(self, id):
        sql = f"""select ciudades.id, ciudades.nombre, ciudades.idPaises, paises.nombre as nombrePais 
        from ikea.ciudades inner join ikea.paises on ciudades.idPaises = paises.id where ciudades.id={id};"""
        rowDict = super().getRowsByIdForaneas(sql)
        newCiudad = self.createCiudadesObj(rowDict)
        return newCiudad

    # polimorfismo
    def createCiudadesObj(self, id, nombre, idPaises, nombrePais):
        ciudadObj = CiudadesObj(id, nombre, idPaises, nombrePais)
        return ciudadObj

    def createCiudadesObj(self, ciudadesDict):
        ciudadesObj = CiudadesObj(
            ciudadesDict["id"],
            ciudadesDict["nombre"],
            ciudadesDict["idPaises"],
            ciudadesDict["nombrePais"],
        )
        return ciudadesObj

    def insertCiudad(self, nombreNuevo, idPais):
        database = self.database
        sql = (
            f"INSERT INTO ikea.ciudades(nombre, idPaises) values ('{nombreNuevo}','{idPais}')"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateCiudadById(self, id, nombre, idPais):
        database = self.database
        sql = (
            "UPDATE ikea.ciudades "
            + f"SET nombre = '{nombre}', idPaises = '{idPais}'"
            + f"WHERE id = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteCiudadById(self, id):
        database = Logic()
        rows = database.deleteRowById(id, self.tableName)
        return rows

