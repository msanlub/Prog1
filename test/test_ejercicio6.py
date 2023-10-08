from src.ejercicio6 import preciosinIVA
from src.ejercicio6 import totalIVA
from src.ejercicio6 import mensajeSalida

#test ejercicio 6
def test_preciosinIVA():
    precio = 4
    IVA = 1.1
    assert preciosinIVA(precio,IVA) == 3.6363636363636362

def test_totalIVA():
    precio = 4
    assert totalIVA(precio * (10/100)) == 0.04
    
def test_mensajeSalida():
    precioBruto = 3.6363636363636362
    iva = 0.04
    assert mensajeSalida(precioBruto,iva) == "El IVA aplicado es del 10%, por lo que se paga en este articulo un total de " + str(iva) + " euros de IVA.El precio sin IVA es: " + str(precioBruto) + " euros."