from src.ejercicio4 import temperatura
from src.ejercicio4 import mensajeSalida

#test ejercicio 4
def test_temperatura():
    celsius = 4
    valorUno = 1.8
    valorDos = 32
    assert temperatura(celsius,valorUno,valorDos) == 39.2
    
def test_mensajeSalida():
    temperaturaConvertida = 39.2
    assert mensajeSalida(temperaturaConvertida) == "La temperatura en grados Fahrenheit es: " + str(temperaturaConvertida)