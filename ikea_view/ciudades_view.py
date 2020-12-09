from prettytable import PrettyTable
from ikea_logic.ciudades_logic import CiudadesLogic
from ikea_view.paises_view import tablaPaises


class TablaCiudades:
    def __init__(self):
        self.logic = CiudadesLogic()
        self.getAllCiudadesView()

    def getAllCiudadesView(self):
        ciudadesList = self.logic.getAllCiudades()

        table = PrettyTable()
        table.field_names = [
            "Id",
            "Nombre",
            "IdPais",
            "NombrePais",
        ]

        for ciudad in ciudadesList:
            table.add_row([ciudad.id, ciudad.nombre, ciudad.idPaises, ciudad.nombrePais ])
        print(table)
        table.clear()

    def addNewCiudadView(self):
        print("Se está añadiendo una nueva ciudad: ")
        nombre = input("Nombre: ")
        print("--Tabla Países--")
        tablaPaises()
        idPais = input("Id del país: ")
        
        insertar = self.logic.insertCiudad(nombre, idPais)
        if insertar > 0:
            print(f"---La ciudad con nombre '{nombre}' se agregó con éxito.---")
        self.getAllCiudadesView()

    def updateCiudadView(self):
        print("Se está actualizando la información de una ciudad: ")
        self.getAllCiudadesView()
        id = int(input("Id de la ciudad a actualizar: "))
        ciudad = self.logic.getCiudadById(id)

        update = int(input("¿Desea actualizar el nombre? 0.No, 1.Sí: "))
        if update == 1:
            print(f"Nombre anterior: {ciudad.nombre}")
            nombre = input("Nuevo nombre: ")
        else:
            nombre = ciudad.nombre

        update = int(input("¿Desea actualizar el Id del país? 0.No, 1.Sí: "))
        if update == 1:
            print("--Tabla Países--")
            tablaPaises()
            print(f"Id anterior: {ciudad.idPaises}")
            idPais = input("Nuevo Id: ")
        else:
            idPais = ciudad.idPaises
        
        update = self.logic.updateCiudadById(id, nombre, idPais)

        if update >0:
            print(f"---Se actualizó con éxito la ciudad con id: {ciudad.id}.---")

        self.getAllCiudadesView()

    def deleteCiudadView(self):
        print("Se está eliminando una ciudad: ")
        self.getAllCiudadesView()
        idCiudad = int(input("Id de la ciudad a eliminar: "))
        delete = self.logic.deleteCiudadById(idCiudad)

        if delete > 0:
            print(f"---Se borró con éxito la ciudad con id: {idCiudad}.---")

        self.getAllCiudadesView()
