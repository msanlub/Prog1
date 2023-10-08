from src.ejercicio7 import suma,mensajeSalida

#test ejercicio 7
def test_suma():
    numeroUno = 1
    numeroDos = 2
    numeroTres = 3
    assert suma(numeroUno,numeroDos,numeroTres) == 6

def test_mensajeSalida():
    sumaTotal = 6
    assert mensajeSalida(sumaTotal) == "La suma de los tres números es: " + str(sumaTotal)