from ikea_view.productos_view import tablaProductos


class MenuProductos:
    def __init__(self):
        print("Bienvenido a la tabla Productos: ")
        productos = tablaProductos()
        while True:
            print("Menu: ")
            print("0 - Salir. ")
            print("1 - Obtener todos los productos.")
            print("2 - Agregar un nuevo producto.")
            print("3 - Actualizar un producto.")
            print("4 - Eliminar un producto.")
            option = int(input("Opción: "))

            if option == 0:
                print("Saliendo del menú de Productos")
                break
            if option == 1:
                productos.getAllProductosView()
            if option == 2:
                productos.addNewProductoView()
            if option == 3:
                productos.updateProductoView()
            if option == 4:
                productos.deleteProductoView()


