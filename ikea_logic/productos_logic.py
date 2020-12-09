from dataBaseX.dx_logic import Logic
from ikea_obj.productos_obj import ProductosObj
from dataBaseX.databaseX import DatabaseX


class ProductosLogic(Logic):
    def __init__(self):
        super().__init__()
        self.tableName= "productos"

    def getAllProductos(self):
        database = Logic()
        sql = f"""SELECT productos.id, productos.nombre, productos.precio, productos.dimensiones, productos.materiales, 
        productos.coloresDisponibles, productos.descripcion, productos.garantia, productos.idClaseProductos, 
        claseproductos.nombre as nombreClase FROM ikea.productos inner join ikea.claseproductos on 
        productos.idClaseProductos = claseproductos.id;"""
        data = database.getAllRowsForaneas(sql)
        productosList = []
        for element in data:
            newProducto = self.createProductosObj(element)
            productosList.append(newProducto)
        return productosList

    def getProductoById(self, id):
        sql = f"""SELECT productos.id, productos.nombre, productos.precio, productos.dimensiones, productos.materiales, 
        productos.coloresDisponibles, productos.descripcion, productos.garantia, productos.idClaseProductos, 
        claseproductos.nombre as nombreClase FROM ikea.productos inner join ikea.claseproductos on 
        productos.idClaseProductos = claseproductos.id where productos.id={id};"""
        rowDict = super().getRowsByIdForaneas(sql)
        newProducto= self.createProductosObj(rowDict)
        return newProducto

    # polimorfismo
    def createProductosObj(self, id, nombre, precio, dimensiones, materiales, coloresDisponibles, descripcion, garantia, idClaseProductos, nombreClase):
        productoObj = ProductosObj(id, id, nombre, precio, dimensiones, materiales, coloresDisponibles, descripcion, garantia, idClaseProductos, nombreClase)
        return productoObj

    def createProductosObj(self, productosDict):
        productoObj = ProductosObj(
            productosDict["id"],
            productosDict["nombre"],
            productosDict["precio"],
            productosDict["dimensiones"],
            productosDict["materiales"],
            productosDict["coloresDisponibles"],
            productosDict["descripcion"],
            productosDict["garantia"],
            productosDict["idClaseProductos"],
            productosDict["nombreClase"],
        )
        return productoObj

    def insertProducto(self, nombre, precio, dimensiones, materiales, coloresDisponibles, descripcion, garantia, idClaseProductos):
        database = self.database
        sql = (
            f"""INSERT INTO ikea.productos(nombre, precio, dimensiones, materiales, coloresDisponibles, descripcion, 
            garantia, idClaseProductos) values ('{nombre}', '{precio}', '{dimensiones}', '{materiales}', '{coloresDisponibles}', 
            '{descripcion}', '{garantia}', '{idClaseProductos}')"""
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateProductoById(self, id, nombre, precio, dimensiones, materiales, coloresDisponibles, descripcion, garantia, idClaseProductos):
        database = self.database
        sql = (
            "UPDATE ikea.productos "
            + f"SET nombre = '{nombre}', precio = '{precio}', dimensiones = '{dimensiones}', materiales = '{materiales}', coloresDisponibles = '{coloresDisponibles}',descripcion = '{descripcion}', garantia = '{garantia}', idClaseProductos = '{idClaseProductos}'"
            + f"WHERE id = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteProductoById(self, id):
        database = Logic()
        rows = database.deleteRowById(id, self.tableName)
        return rows

