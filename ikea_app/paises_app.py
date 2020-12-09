from ikea_view.paises_view import tablaPaises


class MenuPaises:
    def __init__(self):
        print("Bienvenido a la tabla Países:")
        paises = tablaPaises()
        while True:
            print("Menu: ")
            print("0 - Salir. ")
            print("1 - Obtener todos los países.")
            print("2 - Agregar un nuevo país.")
            print("3 - Actualizar un país.")
            print("4 - Eliminar un país.")
            option = int(input("Opción: "))

            if option == 0:
                print("Saliendo del menú de Países")
                break
            if option == 1:
                paises = tablaPaises()
            if option == 2:
                paises.addNewPaisView()
            if option == 3:
                paises.updatePaisView()
            if option == 4:
                paises.deletePaisView()


