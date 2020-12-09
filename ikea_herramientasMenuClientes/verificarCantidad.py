from dataBaseX.dx_logic import Logic


class Verify:
    def __init__(self):
        self.logic = Logic()

    def verificar(self, cantidad, producto, sucursal):
        sql = f"select cantidad from ikea.existencias where idProductos = '{producto}' and idSucursales = '{sucursal}';"
        resultado = self.logic.getAllRowsForaneas(sql)
        if len(resultado) == 0 :
            print("No hay de este producto en esta sucursal.")
            return True

        else:
            var = resultado[0]
            quant = var["cantidad"]
            if int(cantidad) > int(quant):
                print(f"No está la cantidad solicitada de artículos en esta sucursal. Solo hay {quant} artículos disponibles.")
                return True
            else:
                print("Hay suficientes.")
                return False

    def getCuant(self, cantidad, producto, sucursal):
        sql = f"select cantidad from ikea.existencias where idProductos = '{producto}' and idSucursales = '{sucursal}';"
        resultado = self.logic.getAllRowsForaneas(sql)
        if len(resultado) == 0 :
            print("No hay de este producto en esta sucursal.")
            return 0
        
        else:
            var = resultado[0]
            quant = var["cantidad"]
            return quant


