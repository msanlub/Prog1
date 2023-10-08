from src.ejercicio24 import numeroCentimos,numeroEuros,mensajeSalida

precio ="10.00"
 
def test_numeroCentimos():
    assert numeroCentimos(precio) == "00"

def test_numeroEuros():
    assert numeroEuros(precio) == "10"
    
def test_mensajeSalida():
    euros = 2
    centimos = 00
    assert mensajeSalida(euros,centimos) == "El precio del producto es " + str(euros) + " euros " + str(centimos) + " centimos."