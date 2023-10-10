from src.ejercicio16 import total, mensajeSalida

def test_total():
    numeroBarras = 4
    barra = 3.49
    descuento = 0.6
    assert total(numeroBarras,barra,descuento) == 8.376
    
def test_mensajeSalida():
    barra = 3.49
    descuento = 0.6
    calculoTotal = 8.376
    assert mensajeSalida(calculoTotal,barra,descuento) == "El precio de la barra de pan del día es: " + str(barra) + " euros. Si no es del día se le aplica un descuento del: " + str(descuento) + " euros. El precio total de todas las barras que no son del día es: " + str(calculoTotal) + " euros."