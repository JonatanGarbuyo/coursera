import unittest


class ListaDePrecios:
    def __init__(self):
        self.lista_de_items = {
            "4444": {"precio": 5},
            "5555": {"precio": 7},
            "6666": {"precio": 3.5},
            "7777": {"precio": 9.5}
        }

    def obtener_producto(self, codigo):
        """Devuelve un producto segun el codigo pasado como argumento"""
        return self.lista_de_items[codigo]

    def obtener_producto_con_descuento(self, codigo, decuento):
        """Devuelve un producto segun el codigo pasado como argumento.
        Incluye el precio con el descuento pasado como argumento"""
        item = self.lista_de_items[codigo]
        porcentaje_de_descuento = (item.precio * descuento) / 100
        item.precio -= porcentaje_de_descuento
        return item


class Item:
    def __init__(self, producto):
        self.codigo = producto
        self.precio = producto["precio"]


class Compra:
    def __init__(self):
        self.lista_de_items = []

    def agregar_item(self, item):
        """Agrega un item a la lista de compra y devuelve la lista completa """
        self.lista_de_items.append(item)
        return self.obtener_lista_de_items()

    def obtener_lista_de_items(self):
        """Devuelve la lista completa actual"""
        return self.lista_de_items

    def eliminar_item_de_la_lista(self, item):
        """elimina un item de la lista de compra y devuelve la lista completa """
        self.lista_de_items.remove(item)
        return self.obtener_lista_de_items()


class CajaRegistradora:

    def __init__(self):
        self.total = 0.0
        self.carritoCliente = Compra()
        self.precios = ListaDePrecios()
        #print("Ingrese un producto: ")

    def obtener_subTotal(self):
        """Suma los valores de los Items del carrito del cliente"""
        subtotal = 0.0
        for item in self.carritoCliente.obtener_lista_de_items():
            subtotal += item.precio
        return round(subtotal, 2)

    def scannear_producto(self, codigo):
        """Agrega un Item al carrito del cliente segun el codigo pasado como argumento y devuelve el subtotal"""
        self.carritoCliente.agregar_item(
            Item(self.precios.obtener_producto(str(codigo))))
        return self.obtener_subTotal()

    def finalizar_compra(self):
        """Asigna el valor del subtotal actual al valor Total de la compra """
        self.total = self.obtener_subTotal()
        return round(self.total, 2)

    def aplicar_descuento(self, porcentaje):
        """Aplica un porcentaje de descuento al valor Total de la compra """
        descuento = (self.total * porcentaje) / 100
        self.total = self.total - descuento
        return round(self.total, 2)

    def pago(self, pago):
        """Descuenta del total la cantidad ingresada como pago y devuelve la cantidad de cambio. 
        Una cantidad negativa indica pago insuficiente"""
        self.total = self.total - pago
        cambio = self.total * -1
        return round(cambio, 2)


class CajaRegistradoraTest(unittest.TestCase):
    def setUp(self):
        self.caja = CajaRegistradora()

    def test_escanear_ningun_producto(self):
        subTotal = self.caja.obtener_subTotal()
        self.assertEqual(0, subTotal)

    def test_escanear_un_producto(self):
        subTotal = self.caja.scannear_producto(codigo=4444)
        self.assertEqual(5, subTotal)

    def test_escanear_dos_productos(self):
        subTotal = self.caja.scannear_producto(codigo=4444)
        subTotal = self.caja.scannear_producto(codigo=5555)
        self.assertEqual(12, subTotal)

    def test_escanear_tres_productos(self):
        subTotal = self.caja.scannear_producto(codigo=4444)
        subTotal = self.caja.scannear_producto(codigo=5555)
        subTotal = self.caja.scannear_producto(codigo=6666)
        self.assertEqual(15.5, subTotal)

    def test_escanear_tres_productos_y_finalizar(self):
        subTotal = self.caja.scannear_producto(codigo=4444)
        subTotal = self.caja.scannear_producto(codigo=5555)
        subTotal = self.caja.scannear_producto(codigo=6666)
        total = self.caja.finalizar_compra()
        self.assertEqual(15.5, total)

    def test_escanear_tres_productos_y_finalizar_aplicando_descuento(self):
        subTotal = self.caja.scannear_producto(codigo=4444)
        subTotal = self.caja.scannear_producto(codigo=5555)
        subTotal = self.caja.scannear_producto(codigo=6666)
        self.caja.finalizar_compra()
        total = self.caja.aplicar_descuento(10)
        self.assertEqual(13.95, total)

    def test_escanear_tres_productos_y_finalizar_aplicando_descuento_con_pago(self):
        subTotal = self.caja.scannear_producto(codigo=4444)
        subTotal = self.caja.scannear_producto(codigo=5555)
        subTotal = self.caja.scannear_producto(codigo=6666)
        self.caja.finalizar_compra()
        self.caja.aplicar_descuento(10)
        cambio = self.caja.pago(20)
        self.assertEqual(6.05, cambio)

    def test_escanear_tres_productos_y_finalizar_aplicando_descuento_con_pago_insuficiente(self):
        subTotal = self.caja.scannear_producto(codigo=4444)
        subTotal = self.caja.scannear_producto(codigo=5555)
        subTotal = self.caja.scannear_producto(codigo=6666)
        self.caja.finalizar_compra()
        self.caja.aplicar_descuento(10)
        cambio = self.caja.pago(10)
        self.assertEqual(-3.95, cambio)


class CompraTest(unittest.TestCase):
    def setUp(self):
        self.carrito = Compra()

    def test_carrito_vacio(self):
        lista_de_compra = self.carrito.obtener_lista_de_items()
        self.assertEqual([], lista_de_compra)

    def test_agregar_un_producto(self):
        lista_de_compra = self.carrito.agregar_item(1)
        self.assertEqual([1], lista_de_compra)

    def test_borrar_un_producto(self):
        lista_de_compra = self.carrito.agregar_item(1)
        lista_de_compra = self.carrito.agregar_item(2)
        lista_de_compra = self.carrito.agregar_item(3)
        lista_de_compra = self.carrito.eliminar_item_de_la_lista(2)
        self.assertEqual([1, 3], lista_de_compra)


if __name__ == "__main__":
    unittest.main()
