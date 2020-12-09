from ikea_logic.paises_logic import PaisesLogic
from prettytable import PrettyTable


class tablaPaises:
    def __init__(self):
        self.logic = PaisesLogic()
        self.getAllPaisesView()

    def getAllPaisesView(self):
        paisesList = self.logic.getAllPaises()

        table = PrettyTable()
        table.field_names = ["Id", "Nombre"]

        for pais in paisesList:
            table.add_row([pais.id, pais.nombre])
        print(table)
        table.clear()

    def addNewPaisView(self):
        print("Se está añadiendo un nuevo País:")
        nombre = input("Nombre: ")
        insertar = self.logic.insertPais(nombre)
        if insertar > 0:
            print(f"---El país con nombre '{nombre}' se agregó con éxito.---")
        self.getAllPaisesView()

    def updatePaisView(self):
        print("Se está actualizando la información de un país: ")
        self.getAllPaisesView()
        id = int(input("Id del país a actualizar: "))
        pais = self.logic.getPaisById(id)
        
        option = int(input("¿Desea actualizar el nombre? 0.No, 1.Sí: "))
        if option == 1:
            print(f"Nombre anterior: {pais.nombre}")
            nombre = input("Nuevo nombre: ")
        else:
            nombre = pais.nombre

        update = self.logic.updatePaisById(id, nombre)

        if update >0:
            print(f"---Se actualizó con éxito el país con id: {pais.id}.---")

        self.getAllPaisesView()

    def deletePaisView(self):
        print("Se está eliminando un país: ")
        self.getAllPaisesView()
        id = int(input("Id del país a eliminar: "))
        
        delete = self.logic.deletePaisById(id)

        if delete > 0:
            print(f"---Se borró con éxito el país con id: {id}.---")

        self.getAllPaisesView()
