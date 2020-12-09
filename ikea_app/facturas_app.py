from ikea_view.facturas_view import tablaFacturas


class Menufacturas:
    def __init__(self):
        print("Bienvenido a la tabla Facturas")
        facturas = tablaFacturas()
        while True:
            print("Menu: ")
            print("0 - Salir. ")
            print("1 - Obtener todas las Facturas.")
            print("2 - Agregar una nueva Factura.")
            print("3 - Actualizar una Factura.")
            print("4 - Eliminar una Factura.")
            option = int(input("Opción: "))

            if option == 0:
                print("Saliendo del menú de Facturas")
                break
            if option == 1:
                facturas.getAllFacturasView()
            if option == 2:
                facturas.addNewFacturaView()
            if option == 3:
                facturas.updateFacturaView()
            if option == 4:
                facturas.deleteFacturaView()


