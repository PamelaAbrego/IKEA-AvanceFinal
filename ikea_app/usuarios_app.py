from ikea_view.usuarios_view import tablaUsuarios


class MenuUsuarios:
    def __init__(self):
        print("Bienvenido a la tabla Usuarios")
        usuario = tablaUsuarios()
        while True:
            print("Menu: ")
            print("0 - Salir. ")
            print("1 - Obtener todos los usuarios.")
            print("2 - Agregar un nuevo usuario.")
            print("3 - Actualizar un usuario.")
            print("4 - Eliminar un usuario.")
            option = int(input("Opción: "))

            if option == 0:
                print("Saliendo del menú de Usuarios")
                break
            if option == 1:
                usuario.getAllUsuariosView()
            if option == 2:
                usuario.addNewUsuarioView()
            if option == 3:
                usuario.updateUsuarioView()
            if option == 4:
                usuario.deleteUsuarioView()


