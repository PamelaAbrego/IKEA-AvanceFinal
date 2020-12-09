from prettytable import PrettyTable
from ikea_logic.existencias_logic import ExistenciasLogic
from ikea_view.productos_view import tablaProductos
from ikea_view.sucursales_view import tablaSucursales


class tablaExistencias:
    def __init__(self):
        self.logic = ExistenciasLogic()
        self.getAllExistenciasView()

    def getAllExistenciasView(self):
        existenciasList = self.logic.getAllExistencias()

        table = PrettyTable()
        table.field_names = [
            "Id",
            "IdProducto",
            "nombreProducto",
            "IdSucursal",
            "direccion",
            "Cantidad",
        ]

        for existencia in existenciasList:
            table.add_row(
                [
                    existencia.id,
                    existencia.idProductos,
                    existencia.nombreProducto,
                    existencia.idSucursales,
                    existencia.direccion,
                    existencia.cantidad,
                ]
            )
        print(table)
        table.clear()

    def addNewExistenciaView(self):
        print("Se está añadiendo una nueva existencia: ")
        print("--Tabla Productos--")
        tablaProductos()
        idProducto = int(input("IdProducto: "))
        tablaSucursales()
        idSucursal = int(input("IdSucursal: "))
        cantidad = int(input("Cantidad: "))
        
        insertar = self.logic.insertExistencia(idProducto,idSucursal,cantidad)
        if insertar > 0:
            print(f"---La existencia de {cantidad} productos de id {idProducto} se agregó con éxito.---")
        self.getAllExistenciasView()

    def updateExistenciaView(self):
        print("Se está actualizando la información de una existencia: ")
        self.getAllExistenciasView()
        id = int(input("Id de la existencia a actualizar: "))
        existencia = self.logic.getExistenciaById(id)

        update = int(input("¿Desea actualizar el id del Producto? 0.No, 1.Sí: "))
        if update == 1:
            print("--Tabla Productos--")
            tablaProductos()
            print(f"Id del Producto Anterior: {existencia.idProductos}")
            idProducto = int(input("Nuevo Id del Producto: "))
        else:
            idProducto = existencia.idProductos

        update = int(input("¿Desea actualizar el Id de la Sucursal? 0.No, 1.Sí: "))
        if update == 1:
            print("--Tabla Sucursales--")
            tablaSucursales()
            print(f"Id de la Sucursal anterior: {existencia.idSucursales}")
            idSucursal = int(input("Nuevo Id de la Sucursal: "))
        else:
            idSucursal = existencia.idSucursales

        update = int(input("¿Desea actualizar la cantidad? 0.No, 1.Sí: "))
        if update == 1:
            print(f"Cantidad anterior: {existencia.cantidad}")
            cantidad = int(input("Nueva cantidad: "))
        else:
            cantidad = existencia.cantidad

        update = self.logic.updateExistenciaById(id, idProducto, idSucursal, cantidad)

        if update >0:
            print(f"---Se actualizó con éxito la existencia con id: {existencia.id}.---")

        self.getAllExistenciasView()       

    def deleteExistenciaView(self):
        print("Se está eliminando una existencia: ")
        self.getAllExistenciasView()
        id = int(input("Id de la existencia a eliminar: "))
        
        delete = self.logic.deleteExistenciaById(id)

        if delete > 0:
            print(f"---Se borró con éxito la existencia con id: {id}.---")

        self.getAllExistenciasView()
