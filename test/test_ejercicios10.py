from src.ejercicio10 import operacion, mensajeSalida

def test_operacion():
    assert operacion() == 0.25
    
def test_mensajeSalida():
    calculo = 0.25
    assert mensajeSalida(calculo) == "El resultado es: " + str(calculo)