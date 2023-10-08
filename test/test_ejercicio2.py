from src.ejercicio2 import costeHora
from src.ejercicio2 import mensajeSalida

#test ejercicio 2
def test_costeHora():
    hora = 4
    precio = 6
    assert costeHora(hora , precio) == 24

def test_mensajeSalida():
    hora = 4
    precio = 6
    assert mensajeSalida(hora,precio) == "El coste total es: " + str(24)