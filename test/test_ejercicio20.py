from src.ejercicio20 import calculoNumeroTelefono,mensajeSalida

def test_calculoNumeroTelefono():
    numero = "+32-234523422-54"
    assert calculoNumeroTelefono(numero) == "234523422"
    
def test_mensajeSalida():
    numeroTelefono = "234523422"
    assert mensajeSalida(numeroTelefono) == "El numero es: " + str(numeroTelefono)