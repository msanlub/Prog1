from src.ejercicio15 import primerAño,segundoAño,tercerAño,mensajeSalida

dinero = 10
intereses = 0.04

def test_primerAño():
    assert primerAño(dinero,intereses) == 10.4

def test_segundoAño():
    assert segundoAño(dinero,intereses) == 10.8

def test_tercerAño():
    assert tercerAño(dinero,intereses) == 11.2

def test_mensajeSalida():
    primero = 10.4
    segundo = 10.8
    tercero = 11.2
    assert mensajeSalida(primero,segundo,tercero) == "El total con intereses después del primer año son: " + str(primero) + " euros, el total con intereses del segundo año son: " + str(segundo) + " euros, y el total con intereses después del tercer año son: " + str(tercero) + "euros."