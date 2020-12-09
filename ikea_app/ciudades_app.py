from ikea_view.ciudades_view import TablaCiudades


class MenuCiudades:
    def __init__(self):
        print("Bienvenido a la tabla Ciudades")
        ciudades = TablaCiudades()
        while True:
            print("Menu: ")
            print("0 - Salir. ")
            print("1 - Obtener todas las ciudades.")
            print("2 - Agregar una nueva ciudad.")
            print("3 - Actualizar una ciudad.")
            print("4 - Eliminar una ciudad")
            option = int(input("Opción: "))

            if option == 0:
                print("Saliendo del menú de Ciudades.")
                break
            if option == 1:
                ciudades.getAllCiudadesView()
            if option == 2:
                ciudades.addNewCiudadView()
            if option == 3:
                ciudades.updateCiudadView()
            if option == 4:
                ciudades.deleteCiudadView()

