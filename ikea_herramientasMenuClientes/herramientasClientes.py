from dataBaseX.dx_logic import Logic
from prettytable import PrettyTable
from ikea_herramientasMenuClientes.verificarCantidad import Verify
from ikea_herramientasMenuClientes.verCarrito import lookCarrito

class BuscarProducto1:
    def __init__(self):
        self.obj = Verify()
        self.obj2 = lookCarrito()
        self.logic = Logic()

    def BuscarProducto(self, idUser, idCarrito, idSucursal):
        while True:
            print("¿Cómo deseas realizar tu búsqueda?")
            print("1. Escribir lo que buscas")
            print("2. Directorio de categorías")
            print(" ")
            opcion = int(input("Opción: "))

            if opcion == 1:
                producto = input("¿Qué estás buscando?")
                sql = f"""select ikea.categoriasproductos.nombre, ikea.claseproductos.nombre,
                        ikea.productos.id, ikea.productos.nombre, ikea.productos.precio,
                        ikea.productos.dimensiones, ikea.productos.materiales, ikea.productos.coloresDisponibles,
                        ikea.productos.descripcion, ikea.productos.garantia from ikea.categoriasproductos inner join
                        ikea.claseproductos on ikea.claseproductos.idCategoriasProductos = ikea.categoriasproductos.id inner join
                        ikea.productos on ikea.productos.idClaseProductos = ikea.claseproductos.id where
                        ikea.categoriasproductos.nombre = '{producto}' or ikea.claseproductos.nombre = '{producto}' or
                        ikea.productos.nombre = '{producto}';"""
                result = self.logic.getAllRowsForaneas(sql)
                table = PrettyTable()
                table.field_names = ["Categoría","Clase","idProducto","Nombre producto","Precio","Dimensiones","Materiales","Colores disponibles","Descripción","Garantía",]
                for product in result:
                    table.add_row(
                        [product["nombre"],product["claseproductos.nombre"],product["id"],product["productos.nombre"],product["precio"],product["dimensiones"],product["materiales"],product["coloresDisponibles"],product["descripcion"],product["garantia"]])
                print(" ")
                print(" ")
                print("Estos son todos los productos que se han encontrado con tu busqueda: " + str(producto))
                print(table)
                print(" ")
                deci = int(input("Deseas agregar alguno de estos productos a tu carrito? (1.Si - 0.No)"))
                if deci == 1:
                    while True:
                        idProduct = int(input("Escribe el id del producto que deseas ordenar: "))
                        while True:
                            quantity = int(input("Escribe cuántas unidades del producto deseas: "))
                            var2 = self.obj.verificar(quantity, idProduct, idSucursal)
                            quant = self.obj.getCuant(quantity, idProduct, idSucursal)
                                
                            if var2 == True:
                                print("--Lo sentimos, no contamos con esta cantidad de unidades de este producto en la sucursal seleccionada. Puedes comprar hasta " + str(quant)  + " unidades.")
                                deciis = int(input("--Deseas seguir volver a ingresar la cantidad? (1.Si, 0.No)"))
                                if deciis == 1:
                                    pass

                                else:
                                    print("--No se ha agregado nada a tu carrito--")
                                    break           
                            else:
                                self.obj2.AgregarACarrito(idCarrito, idUser, idProduct, quantity)
                                break
                            
                        decision = int(input("--Deseas agregar algún otro producto a tu carrito de la lista anterior? /Asegúrate que no sea del mismo artículo por favor/ (1.Si - 0.No) "))
                        if decision == 1:
                            pass
                        else:
                            break

                    print(" ")
                    dec = int(input("Deseas seguir buscando productos? 1: Si, 0: No "))
                    if dec == 1:
                        self.BuscarProducto(idUser, idCarrito, idSucursal)
                    else:
                        break      

            if opcion == 2:
                print("Estas son las CATEGORÍAS DE PRODUCTOS: ")
                listaCategorias = []
                listaClases = []
                intA = 1
                intC = 1
                sql = f"select ikea.categoriasproductos.nombre from ikea.categoriasproductos;"
                Dict = {}
                Dict2 = {}
                result = self.logic.getAllRowsForaneas(sql)
                for category in result:
                    listaCategorias.append(category["nombre"])

                for cat in listaCategorias:
                    print(str(intC) + "." + cat)
                    Dict.update({intC: cat})
                    intC = intC + 1

                option = int(input("¿Qué categoría de producto deseas buscar?"))
                categoria = Dict[option]

                sql2 = f"""select ikea.claseproductos.nombre from ikea.claseproductos inner join
                        ikea.categoriasproductos on ikea.claseproductos.idCategoriasProductos = ikea.categoriasproductos.id
                        where ikea.categoriasproductos.nombre = '{categoria}';"""
                result2 = result = self.logic.getAllRowsForaneas(sql2)

                for clase in result2:
                    listaClases.append(clase["nombre"])

                print("Estas son las CLASES DE PRODUCTOS: ")

                for cla in listaClases:
                    print(str(intA) + "." + cla)
                    Dict2.update({intA: cla})
                    intA = intA + 1

                num = int(input("¿Qué clase de producto de deseas buscar?"))
                clath = Dict2[num]

                sql3 = f"""select ikea.productos.id, ikea.productos.nombre, ikea.productos.precio,
                        ikea.productos.dimensiones, ikea.productos.materiales, ikea.productos.coloresDisponibles,
                        ikea.productos.descripcion, ikea.productos.garantia from ikea.productos inner join
                        ikea.claseproductos on ikea.productos.idClaseProductos = ikea.claseproductos.id
                        where ikea.claseproductos.nombre = '{clath}';"""
                result3 = result = self.logic.getAllRowsForaneas(sql3)
                table2 = PrettyTable()
                table2.field_names = [
                    "idProducto",
                    "Nombre Producto",
                    "Precio",
                    "Dimensiones",
                    "Materiales",
                    "Colores Disponibles",
                    "Descripción",
                    "Garantía",
                ]
                for product in result3:
                    table2.add_row(
                        [
                            product["id"],
                            product["nombre"],
                            product["precio"],
                            product["dimensiones"],
                            product["materiales"],
                            product["coloresDisponibles"],
                            product["descripcion"],
                            product["garantia"],
                        ]
                    )
                print(" ")
                print("Estos son los resultados de tu búsqueda:")
                print(table2)

                print(" ")
                deci = int(input("Deseas agregar alguno de estos productos a tu carrito? (1.Si - 0.No)"))
                if deci == 1:
                    while True:
                        idProduct = int(input("Escribe el id del producto que deseas ordenar: "))
                        while True:
                            quantity = int(input("Escribe cuántas unidades del producto deseas: "))
                            var2 = self.obj.verificar(quantity, idProduct, idSucursal)
                            quant = self.obj.getCuant(quantity, idProduct, idSucursal)

                            if var2 == True:
                                print("Lo sentimos, no contamos con esta cantidad de unidades de este producto en la sucursal seleccionada. Puedes comprar hasta " + str(quant)  + " unidades")
                                deciis = int(input("Deseas seguir volver a ingresar la cantidad? (1.Si, 0.No)"))
                                if deciis == 1:
                                    pass
                                    
                                else:
                                    print("No se ha agregado nada a tu carrito")
                                    break           
                            else:
                                self.obj2.AgregarACarrito(idCarrito, idUser, idProduct, quantity)
                                break
                            
                        decision = int(input("Deseas agregar algún otro producto a tu carrito de la lista anterior? /Asegúrate que no sea del mismo artículo por favor/ (1.Si - 0.No) "))
                        if decision == 1:
                            pass

                        else:
                            break

                print(" ")
                dec = int(input("Deseas seguir buscando productos? 1: Si, 0: No "))
                if dec == 1:
                    self.BuscarProducto(idUser, idCarrito, idSucursal)

                else:
                    break
            break        


    def storeVariable(self, idUser):
        self.idUser = idUser

