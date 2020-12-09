from ikea_view.sucursales_view import tablaSucursales


class MenuSucursales:
    def __init__(self):
        print("Bienvenido a la tabla Sucursales")
        sucursal = tablaSucursales()
        while True:
            print("Menu: ")
            print("0 - Salir. ")
            print("1 - Obtener todas las sucursales.")
            print("2 - Agregar una nueva sucursal.")
            print("3 - Actualizar una sucursal.")
            print("4 - Eliminar una sucursal")
            option = int(input("Opción: "))

            if option == 0:
                print("Saliendo del menú de Sucursales.")
                break
            if option == 1:
                sucursal.getAllSucursalesView()
            if option == 2:
                sucursal.addNewSucursalView()
            if option == 3:
                sucursal.updateSucursalView()
            if option == 4:
                sucursal.deleteSucursalView()


