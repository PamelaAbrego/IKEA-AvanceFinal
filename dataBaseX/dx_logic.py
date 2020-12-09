from dataBaseX.databaseX import DatabaseX

class Logic:
    def __init__(self):
        self.database = None
        self.__createDataBase()

    def __createDataBase(self):
        if self.database is None:
            self.database = DatabaseX()

    def getAllRows(self, tableName):
        database = self.database
        sql = f"select * from {database.database}.{tableName};"
        rowList = database.executeQueryRows(sql)
        return rowList

    def getAllRowsForaneas(self, sql):
        database = self.database
        rowList = database.executeQueryRows(sql)
        return rowList

    def getRowById(self, id, tableName):
        database = self.database
        sql = f"select * from {database.database}.{tableName} where id={id};"
        rowDict = database.executeQueryOneRow(sql)
        return rowDict
    
    def getRowsByIdForaneas(self,sql):
        database = self.database
        rowDict = database.executeQueryOneRow(sql)
        return rowDict

    def deleteRowById(self, id, tableName):
        database = self.database
        sql = f"DELETE FROM {database.database}.{tableName} WHERE id = {id};"
        rows = database.executeNonQueryRows(sql)
        return rows

    def getRegistros(self, sql):
        database = self.database
        rowList = database.executeQueryRows(sql)
        return rowList

    def getExito(self, sql):
        database = self.database
        exito = database.executeNonQueryBool(sql)
        return exito


