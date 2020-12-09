from datetime import datetime
from dataBaseX.dx_logic import Logic
from prettytable import PrettyTable

now = str(datetime.now())
año = now[:10]
hora = now[11:19]

class lookCarrito:
    def __init__(self):
        self.logic = Logic()
        self.now = str(datetime.now())
        self.anho = self.now[:10]
        self.hora = self.now[11:19]

    def lookForCarrito(self, idCarrito):
        try:
            sql = f"select ikea.productos.id, ikea.productos.nombre, ikea.productos.precio, ikea.carritosdecompras.cantidad from ikea.carritosdecompras inner join ikea.productos on ikea.carritosdecompras.idProducto = ikea.productos.id where numeroCarrito = '{idCarrito}';"
            result = self.logic.getAllRowsForaneas(sql)

            if len(result) == 0:
                print("No tienes ningún artículo en tu carrito")
 
            else:
                Total = 0 
                table2 = PrettyTable()
                table2.field_names = ["Id Producto","Nombre Producto","Precio","Cantidad", "Total por producto"]
                for product in result:
                    table2.add_row([product["id"],product["nombre"], product["precio"],product["cantidad"], (product["precio"]) * (product["cantidad"])])
                    Total = Total + ((product["precio"]) * (product["cantidad"]))
                print(table2)
                print("El total de tu carrito es: $" + str(Total))

        finally:
            pass

    def eliminarDeCarrito(self, idCarrito):
        idProd = int(input("Escribe el id del producto que deseas eliminar de tu carrito: "))
        sql = f"delete from ikea.carritosdecompras where numeroCarrito = '{idCarrito}' and idProducto = '{idProd}';"
        self.logic.database.executeNonQueryBool(sql)

    def agregarAFacturas(self, idCarrito, sucursal):
        sql = f"select ikea.productos.id, ikea.productos.nombre, ikea.productos.precio, ikea.carritosdecompras.cantidad from ikea.carritosdecompras inner join ikea.productos on ikea.carritosdecompras.idProducto = ikea.productos.id where numeroCarrito = '{idCarrito}';"
        result = self.logic.getAllRowsForaneas(sql)
        
        for dic in result:
            var1 = dic["id"]
            var2 = dic["cantidad"]
            sql2 = f"select cantidad from ikea.existencias where idProductos = '{var1}' and idSucursales = '{sucursal}';"
            resultado = self.logic.getAllRowsForaneas(sql2)
            resultado = resultado[0]
            quantity = resultado["cantidad"]
            nuevaCantidad = quantity - var2
            sql3 = f"update ikea.existencias set cantidad = '{nuevaCantidad}' where ikea.existencias.idProductos = '{var1}' and ikea.existencias.idSucursales = '{sucursal}';"
            self.logic.database.executeNonQueryBool(sql3)

    def AgregarFactura(self, idCarrito, idSucursal, idUsuario, fecha, hora, total):
        intTipoPago = int(input("En qué forma deseas pagar? (1. Efectivo - 2. Tarjeta de crédito - 3. Cheque)"))
        if intTipoPago == 1:
            tipoPago = "Efectivo"
        if intTipoPago ==2:
            tipoPago = "Tarjeta de crédito"
        if intTipoPago ==3:
            tipoPago = "Cheque" 

        sql = f"INSERT INTO ikea.facturas(id, idUsuarios, tipoDePago, idSucursales, fecha, hora, numeroCarrito,total) VALUES('0', '{idUsuario}', '{tipoPago}', '{idSucursal}', '{fecha}','{hora}','{idCarrito}', '{total}' ); "
        self.logic.database.executeNonQueryBool(sql)

    def AgregarACarrito(self, idCarrito, idUsuario, idProducto, cantidad):
        sql = f"insert into ikea.carritosdecompras (id, numeroCarrito, idUsuario, idProducto, cantidad) values ('0', '{idCarrito}', '{idUsuario}', '{idProducto}', '{cantidad}');"
        self.logic.database.executeNonQueryBool(sql)

    def getTotal(self, idCarrito):
        sql = f"select ikea.productos.id, ikea.productos.nombre, ikea.productos.precio, ikea.carritosdecompras.cantidad from ikea.carritosdecompras inner join ikea.productos on ikea.carritosdecompras.idProducto = ikea.productos.id where numeroCarrito = '{idCarrito}';"
        result =  self.logic.getAllRowsForaneas(sql)
        if len(result) == 0:
            print("No tienes ningún artículo en tu carrito")
 
        else:
            Total = 0 
            table2 = PrettyTable()
            table2.field_names = ["Id Producto","Nombre Producto","Precio","Cantidad", "Total por producto"]
            for product in result:
                table2.add_row([product["id"],product["nombre"], product["precio"],product["cantidad"], (product["precio"]) * (product["cantidad"])])
                Total = Total + ((product["precio"]) * (product["cantidad"]))
            return Total




