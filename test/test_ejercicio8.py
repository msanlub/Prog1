from src.ejercicio8 import sumaDosVariables,mensajeSalida

def test_sumaDosVariables():
    numeroUno = 1 + 2
    numeroDos = 3
    assert sumaDosVariables(numeroUno,numeroDos) == 6
    
def test_mensajeSalida():
    suma = 6
    assert mensajeSalida(suma) == "La suma de los tres números es: " + str(suma)
    
