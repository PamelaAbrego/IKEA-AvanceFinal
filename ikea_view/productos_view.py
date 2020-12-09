from prettytable import PrettyTable
from ikea_logic.productos_logic import ProductosLogic
from ikea_view.clases_view import tablaClase


class tablaProductos:
    def __init__(self):
        self.logic = ProductosLogic()
        self.getAllProductosView()

    def getAllProductosView(self):
        productosList = self.logic.getAllProductos()

        table = PrettyTable()
        table.field_names = [
            "Id",
            "Nombre",
            "Precio",
            "Dimensiones",
            "Materiales",
            "Colores Disponibles",
            "Descripción",
            "Garantía",
            "IdClaseProducto",
            "NombreClase",
        ]

        for producto in productosList:
            table.add_row(
                [producto.id, producto.nombre, producto.precio, producto.dimensiones, producto.materiales, producto.coloresDisponibles, producto.descripcion, producto.garantia, producto.idClaseProductos, producto.nombreClase]
            )
        print(table)
        table.clear()

    def addNewProductoView(self):
        print("Se está añadiendo un nuevo Producto:")
        nombre = input("Nombre: ")
        precio = input("Precio: ")
        dimensiones = input("Dimensiones: ")
        materiales = input("Materiales: ")
        coloresDisponibles = input("Colores disponibles: ")
        descripcion = input("Descripción: ")
        garantia = input("Garantía: ")
        print("--Tabla Clases de Productos--")
        tablaClase()
        idClaseProductos = input("IdClaseProductos: ")

        insertar = self.logic.insertProducto(nombre, precio, dimensiones, materiales, coloresDisponibles, descripcion, garantia, idClaseProductos)
        if insertar > 0:
            print(f"---El producto con nombre '{nombre}' se agregó con éxito.---")
        self.getAllProductosView()

    def updateProductoView(self):
        print("Se está actualizando la información de un Producto: ")
        self.getAllProductosView()
        id = int(input("Id del Producto a actualizar: "))
        producto = self.logic.getProductoById(id)

        option = int(input("¿Desea actualizar el nombre? 0.No, 1.Sí: "))
        if option == 1:
            print(f"Nombre anterior: {producto.nombre}")
            nombre = input("Nuevo nombre: ")

        else:
            nombre = producto.nombre

        option = int(input("¿Desea actualizar el precio? 0.No, 1.Sí: "))
        if option == 1:
            print(f"Precio anterior: {producto.precio}")
            precio = input("Nuevo precio: ")

        else:
            precio = producto.precio

        option = int(input("¿Desea actualizar las dimensiones? 0.No, 1.Sí: "))
        if option == 1:
            print(f"Dimensiones anteriores: {producto.dimensiones}")
            dimensiones = input("Nuevas dimensiones: ")

        else:
            dimensiones = producto.dimensiones

        option = int(input("¿Desea actualizar los materiales? 0.No, 1.Sí: "))
        if option == 1:
            print(f"Materiales anteriores: {producto.materiales}")
            materiales = input("Nuevos materiales: ")

        else:
            materiales = producto.materiales

        option = int(input("¿Desea actualizar los colores disponibles? 0.No, 1.Sí: "))
        if option == 1:
            print(f"Colores disponibles anteriores: {producto.coloresDisponibles}")
            coloresDisponibles = input("Nuevos colores disponibles: ")

        else:
            coloresDisponibles = producto.coloresDisponibles

        option = int(input("¿Desea actualizar la descripción? 0.No, 1.Sí: "))
        if option == 1:
            print(f"Descripción anterior: {producto.descripcion}")
            descripcion = input("Nueva descrpción: ")

        else:
            descripcion = producto.descripcion

        option = int(input("¿Desea actualizar la garantía? 0.No, 1.Sí: "))
        if option == 1:
            print(f"Garantía anterior: {producto.garantia}")
            garantia = input("Nueva garantía: ")

        else:
            garantia = producto.garantia

        option = int(input("¿Desea actualizar el IdClaseProducto? 0.No, 1.Sí: "))
        if option == 1:
            print("--Tabla Clases de Productos--")
            tablaClase()
            print(f"IdClaseProducto anterior: {producto.idClaseProductos}")
            idClaseProducto = input("Nuevo IdClaseProducto: ")

        else:
            idClaseProducto = producto.idClaseProductos

        update = self.logic.updateProductoById(id, nombre, precio, dimensiones, materiales, coloresDisponibles, descripcion, garantia, idClaseProducto)

        if update >0:
            print(f"---Se actualizó con éxito el producto con id: {producto.id}.---")

        self.getAllProductosView()

    def deleteProductoView(self):
        print("Se está eliminando un Producto: ")
        self.getAllProductosView()
        id = int(input("Id del producto a eliminar: "))
        
        delete = self.logic.deleteProductoById(id)

        if delete > 0:
            print(f"---Se borró con éxito el producto con id: {id}.---")

        self.getAllProductosView()
