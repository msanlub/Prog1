from src.ejercicio3 import operacion
from src.ejercicio3 import mensajeSalida

#test ejercicio 3
def test_operacion():
    ancho = 17
    alto = 12.0
    assert operacion(ancho,alto) == "\t8.5 \n\t8 \n\t4.0 \n\t11\n"

def test_mensajeSalida():
    valor = "\t8.5 \n\t8 \n\t4.0 \n\t11\n"
    assert mensajeSalida(valor) == "El resultado es: \n" + str(valor)