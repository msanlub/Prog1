from src.ejercicio25 import *

fecha = "24/03/1992" 

def test_fechaDia():
    assert fechaDia(fecha) == "24"
    
def test_fechaMes():
    assert fechaMes(fecha) == "03"
    
def test_fechaAño():
    assert fechaAño(fecha) == "1992"
    
def test_mensajeSalida():
    dia = 24
    mes = 3
    año = 1992
    assert mensajeSalida(dia,mes,año) == "El dia es: " + str(dia) + ", el mes es: " + str(mes) + ", del año: " + str(año) + "."