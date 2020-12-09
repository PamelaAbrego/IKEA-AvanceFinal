import pymysql


class DatabaseX:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "12345"
        self.database = "ikea"
        self.cursorType = pymysql.cursors.DictCursor
        self.connection = self.createConnection()

    def createConnection(self):
        connection = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.database,
            cursorclass=self.cursorType,
        )
        return connection

    # Sentencias de SQL que no regresan información
    def executeNonQueryBool(self, sql):
        currentCursor = self.connection.cursor()
        currentCursor.execute(sql)
        self.connection.commit()
        success = False
        if currentCursor.rowcount > 0:
            success = True
        return success

    def executeNonQueryRows(self, sql):
        currentCursor = self.connection.cursor()
        currentCursor.execute(sql)
        self.connection.commit()
        return currentCursor.rowcount

    # Sentencias SQL que sí traen información
    def executeQueryRows(self, sql):
        currentCursor = self.connection.cursor()
        currentCursor.execute(sql)
        return currentCursor.fetchall()

    def executeQueryOneRow(self, sql):
        currentCursor = self.connection.cursor()
        currentCursor.execute(sql)
        return currentCursor.fetchone()

    # Iniciar y cerrar conexión

    def endConnection(self):
        if self.connection.open:
            self.connection.close()

    def startConnection(self):
        if not self.connection.open:
            self.connection = self.createConnection()
