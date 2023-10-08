from src.ejercicio1 import calculaNombre
from src.ejercicio1 import mensajeSalida

#test ejercicio 1
def test_leeNombre():
    nombre = "Marta"
    assert calculaNombre(nombre) == "Marta"
    
def test_mensaje():
    nombre = "Marta"
    assert mensajeSalida(nombre) == "Bienvenido/a " + str(nombre)