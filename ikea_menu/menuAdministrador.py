from ikea_app.categorias_app import MenuCategorias
from ikea_app.ciudades_app import MenuCiudades
from ikea_app.clases_app import MenuClases
from ikea_app.paises_app import MenuPaises
from ikea_app.productos_app import MenuProductos
from ikea_app.usuarios_app import MenuUsuarios
from ikea_app.existencias_app import MenuExistencias
from ikea_app.facturas_app import Menufacturas
from ikea_app.carrito_app import MenuCarrito
from ikea_app.sucursales_app import MenuSucursales


class MenuAdministrador:
    def __init__(self):
        while True:
            print("Bienvenido a la Administración de IKEA")
            print("------------------------------------------")
            print("Seleccione la tabla que desea administrar:")
            print("0 - Salir. ")
            print("1 - Tabla Usuarios.")
            print("2 - Tabla Productos.")
            print("3 - Tabla Clases de Productos.")
            print("4 - Tabla Categorías de Productos.")
            print("5 - Tabla Carritos de Compras.")
            print("6 - Tabla Facturas.")
            print("7 - Tabla Existencias.")
            print("8 - Tabla Sucursales.")
            print("9 - Tabla Ciudades.")
            print("10 - Tabla Países.")
            option = int(input("Opción: "))

            if option == 0:
                print("------------------------------------------")
                print("Saliendo de la Administración de IKEA.")
                print("------------------------------------------")
                break
            if option == 1:
                print("------------------------------------------")
                MenuUsuarios()
                print("------------------------------------------")
            if option == 2:
                print("------------------------------------------")
                MenuProductos()
                print("------------------------------------------")
            if option == 3:
                print("------------------------------------------")
                MenuClases()
                print("------------------------------------------")
            if option == 4:
                print("------------------------------------------")
                MenuCategorias()
                print("------------------------------------------")
            if option == 5:
                print("------------------------------------------")
                MenuCarrito()
                print("------------------------------------------")
                pass
            if option == 6:
                print("------------------------------------------")
                Menufacturas()
                print("------------------------------------------")
                pass
            if option == 7:
                print("------------------------------------------")
                MenuExistencias()
                print("------------------------------------------")
                pass
            if option == 8:
                print("------------------------------------------")
                MenuSucursales()
                print("------------------------------------------")
                pass
            if option == 9:
                print("------------------------------------------")
                MenuCiudades()
                print("------------------------------------------")
            if option == 10:
                print("------------------------------------------")
                MenuPaises()
                print("------------------------------------------")
