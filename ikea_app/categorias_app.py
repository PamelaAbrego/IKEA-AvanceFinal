from ikea_view.categorias_view import tablaCategorias


class MenuCategorias:
    def __init__(self):
        print("Bienvenido a la tabla Categorías de Productos: ")
        categorias = tablaCategorias()
        while True:
            print("Menu: ")
            print("0 - Salir. ")
            print("1 - Obtener todas las categorías.")
            print("2 - Agregar una nueva categoría.")
            print("3 - Actualizar una categoría.")
            print("4 - Eliminar una categoría.")
            option = int(input("Opción: "))

            if option == 0:
                print("Saliendo del menú de Categorías de Productos")
                break
            if option == 1:
                categorias.getAllCategoriasView()
            if option == 2:
                categorias.addNewCategoriaView()
            if option == 3:
                categorias.updateCategoriaView()
            if option == 4:
                categorias.deleteCategoriaView()


