from src.ejercicio5 import calculaPrecioDelArticulo
from src.ejercicio5 import mensajeSalida

#test ejercicio 5
def test_precioDelArticulo():
    precio = 5
    IVA = 1.10
    assert calculaPrecioDelArticulo(precio,IVA) == 5.5
    
def test_mensajeSalida():
    precioDelArticulo = 5.5
    assert mensajeSalida(precioDelArticulo) == "El precio con IVA incluido es: " + str(precioDelArticulo)