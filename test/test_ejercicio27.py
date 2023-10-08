from src.ejercicio27 import calculoTotal,mensajeSalida

def test_calculoTotal():
    nombre = "pepsi"
    precio = 2.4
    unidad = 2
    assert calculoTotal(nombre,precio,unidad) == "pepsi ->   2 unidades x     2.40€ =       4.80€"
    
def test_mensajeSalida():
    totalProducto = "pepsi ->   2 unidades x     2.00€ =       4.00€"
    assert mensajeSalida(totalProducto) == "\t" + str(totalProducto)