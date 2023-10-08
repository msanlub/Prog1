from src.ejercicio14 import pesoTotal, mensajeSalida

def test_pesoTotal():
    payasos = 2
    muñecas = 4
    assert pesoTotal(payasos,muñecas) == 524
    
def test_mensajeSalida():
    peso = 524
    assert mensajeSalida(peso) == "El peso de tu paquete es de: " + str(peso)