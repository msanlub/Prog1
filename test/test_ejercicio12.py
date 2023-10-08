from src.ejercicio12 import imc, mensajeSalida

#test ejercicio 12
def test_imc():
    peso = 70
    estatura = 72.0
    exponente = 2,2
    assert imc(peso,estatura) == 0.95

def test_mensajeSalida():
    calculoImc = 0.95
    assert mensajeSalida(calculoImc) == "Tu índice de masa corporal es: " + str(calculoImc)