from prettytable import PrettyTable
from ikea_logic.categorias_logic import CategoriasLogic


class tablaCategorias:
    def __init__(self):
        self.logic = CategoriasLogic()
        self.getAllCategoriasView()

    def getAllCategoriasView(self):
        categoriasList = self.logic.getAllCategorias()

        table = PrettyTable()
        table.field_names = ["Id", "Nombre"]

        for categoria in categoriasList:
            table.add_row([categoria.id, categoria.nombre ])
        print(table)
        table.clear()

    def addNewCategoriaView(self):
        print("Se está añadiendo una nueva categoría:")
        nombre = input("Nombre: ")
        insertar = self.logic.insertCategoria(nombre)
        if insertar > 0:
            print(f"---La categoría con nombre '{nombre}' se agregó con éxito.---")
        self.getAllCategoriasView()

    def updateCategoriaView(self):
        print("Se está actualizando la información de una categoría: ")
        self.getAllCategoriasView()
        id = int(input("Id de la categoría a actualizar: "))
        categoria = self.logic.getCategoriaById(id)

        update = int(input("¿Desea actualizar el nombre? 0.No, 1.Sí: "))
        if update == 1:
            print(f"Nombre anterior: {categoria.nombre}")
            nombre = input("Nuevo nombre: ")
        else:
            nombre = categoria.nombre

        update = self.logic.updateCategoriaById(id, nombre)

        if update >0:
            print(f"---Se actualizó con éxito la categoría con id: {categoria.id}.---")

        self.getAllCategoriasView()

    def deleteCategoriaView(self):
        print("Se está eliminando una categoría: ")
        self.getAllCategoriasView()
        id = int(input("Id de la categoría a eliminar: "))
        delete = self.logic.deleteCategoriaById(id)

        if delete > 0:
            print(f"---Se borró con éxito la categoria con id: {id}.---")

        self.getAllCategoriasView()
