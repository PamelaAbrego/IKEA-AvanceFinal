from prettytable import PrettyTable
from dataBaseX.databaseX import DatabaseX
from ikea_logic.carrito_logic import CarritoLogic
from ikea_view.usuarios_view import tablaUsuarios
from ikea_view.productos_view import tablaProductos


class TablaCarritos:
    def __init__(self):
        self.logic = CarritoLogic()
        self.getAllCarritoView()
        self.database= DatabaseX()

    def getAllCarritoView(self):
        carritoList = self.logic.getAllCarritos()

        table = PrettyTable()
        table.field_names = [
            "idCarritoDeCompras",
            "numeroCarrito",
            "idUsuarios",
            "NombreUsuario",
            "idProducto",
            "NombreProducto",
            "Cantidad",
        ]

        for carrito in carritoList:
            table.add_row(
                [
                    carrito.id,
                    carrito.numeroCarrito,
                    carrito.idUsuario,
                    carrito.nombreUsuario,
                    carrito.idProducto,
                    carrito.nombreProducto,
                    carrito.cantidad,
                ]
            )
        print(table)
        table.clear()

    def addNewCarritoView(self):
        print("Se está añadiendo un nuevo Carrito:")
        print("--Tabla Usuarios--")
        tablaUsuarios()
        idUsuarios = input("idUsuario: ")

        sql = "SELECT id FROM carritosdecompras ORDER BY id desc;"
        numeroCarrito=self.logic.getAllRowsForaneas(sql)
        numeroCarrito = numeroCarrito[0]
        numeroCarrito = numeroCarrito["id"]

        print("--Tabla Productos--")
        tablaProductos()
        idProductos = input("idProducto: ")
        cantidad = input("cantidad: ")
        
        insertar = self.logic.insertCarrito(numeroCarrito,idUsuarios, idProductos,cantidad)
        if insertar > 0:
            print(f"---El carrito se agregó con éxito.---")
        self.getAllCarritoView()

    def updateCarritoView(self):
        print("Se está actualizando la información de un carrito: ")
        self.getAllCarritoView()
        id = int(input("Id del carrito a actualizar: "))
        carrito = self.logic.getCarritoById(id)

        option = int(input("¿Desea actualizar el idUsuario? 0.No, 1.Sí: "))
        if option == 1:
            print(f"IdUsuario anterior: {carrito.idUsuario}")
            print("--Tabla Usuarios--")
            tablaUsuarios()
            idUsuarios = input("Nuevo nombre: ")
            numeroCarrito = carrito.numeroCarrito

        else:
            idUsuarios = carrito.idUsuario
            numeroCarrito = idUsuarios
            numeroCarrito = carrito.numeroCarrito

        option = int(input("¿Desea actualizar el idProductos? 0.No, 1.Sí: "))
        if option == 1:
            print(f"idProducto anterior: {carrito.idProducto}")
            print("--Tabla Productos--")
            tablaProductos()
            idProductos = input("Nuevo idProductos: ")

        else:
            idProductos = carrito.idProducto

        option = int(input("¿Desea actualizar la cantidad? 0.No, 1.Sí: "))
        if option == 1:
            print(f"cantidad anterior: {carrito.cantidad}")
            cantidad = input("Nueva cantidad: ")

        else:
            cantidad = carrito.cantidad

        update = self.logic.updateCarritoById(id, numeroCarrito, idUsuarios ,idProductos, cantidad)

        if update >0:
            print(f"---Se actualizó con éxito el carrito con id: {carrito.id}.---")

        self.getAllCarritoView()

    def deleteCarritoView(self):
        print("Se está eliminando un Carrito: ")
        self.getAllCarritoView()
        id = int(input("Id del carrito a eliminar: "))

        delete = self.logic.deleteCarritoById(id)

        if delete > 0:
            print(f"---Se borró con éxito el carrito con id: {id}.---")

        self.getAllCarritoView()
