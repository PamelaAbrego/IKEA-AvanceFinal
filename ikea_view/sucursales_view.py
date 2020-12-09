from prettytable import PrettyTable
from ikea_logic.sucursales_logic import SucursalesLogic
from ikea_view.ciudades_view import TablaCiudades


class tablaSucursales:
    def __init__(self):
        self.logic = SucursalesLogic()
        self.getAllSucursalesView()

    def getAllSucursalesView(self):
        sucursalesList = self.logic.getAllSucursales()

        table = PrettyTable()
        table.field_names = [
            "Id",
            "Direccion",
            "IdCiudad",
            "NombreCiudad",
            "Telefono",
            "Horarios",
        ]

        for sucursal in sucursalesList:
            table.add_row([sucursal.id, sucursal.direccion, sucursal.idCiudades, sucursal.nombreCiudad, sucursal.telefono, sucursal.horarios])
        print(table)
        table.clear()

    def addNewSucursalView(self):
        print("Se está añadiendo una nueva sucursal: ")
        direccion = input("Direccion: ")
        print("--Tabla Ciudades--")
        TablaCiudades()
        idCiudad = input("Id de la ciudad: ")
        telefono = input("Número de teléfono: ")
        horario = input("Horario de la sucursal: ")

        insertar = self.logic.insertSucursal(direccion, idCiudad, telefono, horario)
        if insertar > 0:
            print(f"---La sucursal con dirección: '{direccion}' se agregó con éxito.---")
        self.getAllSucursalesView()

    def updateSucursalView(self):
        print("Se está actualizando la información de una sucursal: ")
        idSucursal = int(input("Id de la sucursal a actualizar: "))
        sucursal = self.logic.getSucursalById(idSucursal)

        update = int(input("¿Desea actualizar la dirección? 0.No, 1.Sí: "))
        if update == 1:
            print(f"Dirección anterior: {sucursal.direccion}")
            direccion = input("Nueva direccion: ")
        else:
            direccion = sucursal.direccion

        update = int(input("¿Desea actualizar el Id de la ciudad? 0.No, 1.Sí: "))
        if update == 1:
            print(f"Id anterior: {sucursal.idCiudades}")
            print("--Tabla Ciudades--")
            TablaCiudades()
            idCiudad = input("Nuevo Id: ")
        else:
            idCiudad = sucursal.idCiudades

        update = int(input("¿Desea actualizar el número de teléfono? 0.No, 1.Sí: "))
        if update == 1:
            print(f"Número de teléfono anterior: {sucursal.telefono}")
            telefono = input("Nuevo número de teléfono: ")
        else:
            telefono = sucursal.telefono

        update = int(input("¿Desea actualizar el horario? 0.No, 1.Sí: "))
        if update == 1:
            print(f"Horario anterior: {sucursal.horarios}")
            horario = input("Nuevo horario: ")
        else:
            horario = sucursal.horarios

        update = self.logic.updateSucursalById(idSucursal, direccion, idCiudad, telefono, horario)

        if update >0:
            print(f"---Se actualizó con éxito la sucursal con id: {sucursal.id}.---")

        self.getAllSucursalesView()

    def deleteSucursalView(self):
        print("Se está eliminando una sucursal: ")
        self.getAllSucursalesView()
        idSucursal = int(input("Id de la sucursal a eliminar: "))
        
        delete = self.logic.deleteSucursalById(idSucursal)

        if delete > 0:
            print(f"---Se borró con éxito la sucursal con id: {idSucursal}.---")

        self.getAllSucursalesView()
