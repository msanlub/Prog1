from src.ejercicio10 import operacion, mensajeSalida

def test_operacion():
    assert operacion() == 0.25
    
def test_mensajeSalida():
    calculoFinal = 0.25
    assert mensajeSalida(calculoFinal) == "El resultado es: " + str(calculoFinal)