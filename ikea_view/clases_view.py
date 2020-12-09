from prettytable import PrettyTable
from ikea_view.categorias_view import tablaCategorias
from ikea_logic.clases_logic import ClasesLogic


class tablaClase:
    def __init__(self):
        self.logic=ClasesLogic()
        self.getAllClasesView()

    def getAllClasesView(self):
        clasesList = self.logic.getAllClases()

        table = PrettyTable()
        table.field_names = [
            "Id",
            "Nombre",
            "IdCategoriaProducto",
            "NombreCategoria",
        ]

        for clase in clasesList:
            table.add_row([clase.id, clase.nombre, clase.idCategoriasProductos, clase.nombreCategoria])
        print(table)
        table.clear()

    def addNewClaseView(self):
        print("Se está añadiendo una nueva clase: ")
        nombre = input("Nombre: ")
        print("--Tabla Categorías--")
        tablaCategorias()
        idCategoria = int(input("idCategoria: "))

        insertar = self.logic.insertClase(nombre, idCategoria)
        if insertar > 0:
            print(f"---La clase con nombre '{nombre}' se agregó con éxito.---")
        self.getAllClasesView()

    def updateClaseView(self):
        print("Se está actualizando la información de una clase: ")
        self.getAllClasesView()
        id = int(input("Id de la clase a actualizar: "))
        clase = self.logic.getClaseById(id)

        update = int(input("¿Desea actualizar el nombre? 0.No, 1.Sí: "))
        if update == 1:
            print(f"Nombre anterior: {clase.nombre}")
            nombre = input("Nuevo nombre: ")
        else:
            nombre = clase.nombre

        update = int(input("¿Desea actualizar el Id de la Categoría? 0.No, 1.Sí: "))
        if update == 1:
            print("--Tabla Categorías--")
            tablaCategorias()
            print(f"Id anterior: {clase.idCategoriasProductos}")
            idCategoria = input("Nuevo Id: ")
        else:
            idCategoria = clase.idCategoriasProductos

        update = self.logic.updateClaseById(id, nombre, idCategoria)

        if update >0:
            print(f"---Se actualizó con éxito la clase con id: {clase.id}.---")

        self.getAllClasesView()

    def deleteClaseView(self):
        print("Se está eliminando una clase: ")
        self.getAllClasesView()
        idClase = int(input("Id de la clase a eliminar: "))

        delete = self.logic.deleteClaseById(idClase)

        if delete > 0:
            print(f"---Se borró con éxito la clase con id: {idClase}.---")

        self.getAllClasesView()
