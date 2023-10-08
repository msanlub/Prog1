from src.ejercicio19 import calculoNumeroLetras, mensajeFinal

def test_calculoNumeroLetras():
    nombre = "natalia"
    assert calculoNumeroLetras(nombre) == "NATALIA -> 7"
    
def test_mensajeFinal():
    numeroLetras = "NATALIA -> 7"
    assert mensajeFinal(numeroLetras) == "NATALIA -> 7 letras"