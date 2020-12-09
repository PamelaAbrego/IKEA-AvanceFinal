from prettytable import PrettyTable
from ikea_logic.facturas_logic import FacturasLogic
from ikea_view.usuarios_view import tablaUsuarios
from ikea_view.carrito_view import TablaCarritos
from ikea_view.sucursales_view import tablaSucursales


class tablaFacturas:
    def __init__(self):
        self.logic = FacturasLogic()
        self.getAllFacturasView()

    def getAllFacturasView(self):
        result = self.logic.getAllFacturas()

        table = PrettyTable()
        table.field_names = [
            "Id",
            "IdUsuario",
            "NombreUsuario",
            "Tipo de pago",
            "IdSucursal",
            "Direccion",
            "Fecha",
            "Hora",
            "NumeroCarrito",
            "Total",
        ]

        for factura in result:
            table.add_row(
                [
                    factura.id,
                    factura.idUsuarios,
                    factura.nombreUsuario,
                    factura.tipoDePago,
                    factura.idSucursales,
                    factura.direccion,
                    factura.fecha,
                    factura.hora,
                    factura.numeroCarrito,
                    factura.total,
                ]
            )
        print(table)
        table.clear()

    def addNewFacturaView(self):
        print("Se está añadiendo un nueva Factura:")
        print("--Tabla Usuarios--")
        tablaUsuarios()
        idUsuarios = int(input("idUsuario: "))
        sql = f"SELECT total FROM ikea.facturas where idUsuarios = {idUsuarios}"
        totales = self.logic.getAllRowsForaneas(sql)
        totales = totales[0]
        total = totales["total"]
        tipoDePago = input("tipo de pago: ")
        print("--Tabla Sucursales--")
        tablaSucursales()
        idSucursales = int(input("Id Sucursal: "))
        fecha = input("Fecha: ")
        hora = input("Hora: ")
        numeroCarrito= idUsuarios
        
        insertar = self.logic.insertFactura(idUsuarios, tipoDePago, idSucursales, fecha, hora, numeroCarrito, total)
        if insertar > 0:
            print(f"---La factura se agregó con éxito.---")
        self.getAllFacturasView()

    def updateFacturaView(self):
        print("Se está actualizando la información de una Factura : ")
        self.getAllFacturasView()
        id = int(input("Id de la factura a actualizar: "))
        factura = self.logic.getFacturaById(id)

        option = int(input("¿Desea actualizar el IdUsuario? 0.No, 1.Sí: "))
        if option == 1:
            print("--Tabla Usuarios--")
            tablaUsuarios()
            print(f"IdUsuario anterior: {factura.idUsuarios}")
            idUsuarios = input("Nuevo idUsuario: ")
            sql = f"SELECT total FROM ikea.facturas where idUsuarios = {idUsuarios}"
            totales = self.logic.getAllRowsForaneas(sql)
            totales = totales[0]
            total = totales["total"]

        else:
            idUsuarios = factura.idUsuarios

        option = int(input("¿Desea actualizar el tipo de pago? 0.No, 1.Sí: "))
        if option == 1:
            print(f"Tipo de pago anteriores: {factura.tipoDePago}")
            tipoDePago = input("Nuevao tipo de pago: ")

        else:
            tipoDePago = factura.tipoDePago

        option = int(input("¿Desea actualizar el idSucursal? 0.No, 1.Sí: "))
        if option == 1:
            print("--Tabla Sucursales--")
            tablaSucursales()
            print(f"IdSucursal anteriores: {factura.idSucursales}")
            idSucursales = input("Nuevo ID sucursal: ")

        else:
            idSucursales = factura.idSucursales

        option = int(input("¿Desea actualizar la fecha? 0.No, 1.Sí: "))
        if option == 1:
            print(f"Fecha anterior: {factura.fecha}")
            fecha = input("Nueva fecha: ")

        else:
            fecha = factura.fecha

        option = int(input("¿Desea actualizar la hora? 0.No, 1.Sí: "))
        if option == 1:
            print(f"Hora anterior: {factura.hora}")
            hora = input("Nueva hora: ")

        else:
            hora = factura.hora

        numeroCarrito = factura.numeroCarrito
        update = self.logic.updateFacturaById(id,idUsuarios, tipoDePago, idSucursales, fecha, hora, numeroCarrito, total)

        if update >0:
            print(f"---Se actualizó con éxito la factura con id: {factura.id}.---")

        self.getAllFacturasView()

    def deleteFacturaView(self):
        print("Se está eliminando una Factura: ")
        self.getAllFacturasView()
        id = int(input("Id de la factura a eliminar: "))
        
        delete = self.logic.deleteFacturaById(id)

        if delete > 0:
            print(f"---Se borró con éxito la factura con id: {id}.---")

        self.getAllFacturasView()
