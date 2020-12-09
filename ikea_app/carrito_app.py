from ikea_view.carrito_view import TablaCarritos


class MenuCarrito:
    def __init__(self):
        print("Bienvenido a la tabla Carritos de Compras")
        carrito = TablaCarritos()

        while True:
            print("Menu: ")
            print("0 - Salir. ")
            print("1 - Obtener todos los registros del Carritos de Compras.")
            print("2 - Agregar un nuevo registro a Carritos de Compras.")
            print("3 - Actualizar un registro de Carritos de Compras.")
            print("4 - Eliminar un registro de Carritos de Compras.")
            
            option = int(input("Opción: "))

            if option == 0:
                print("Saliendo del menú de Carritos de Compras.")
                break
            if option == 1:
                carrito.getAllCarritoView()
            if option == 2:
                carrito.addNewCarritoView()
            if option == 3:
                carrito.updateCarritoView()
            if option == 4:
                carrito.deleteCarritoView()


