from src.ejercicio19 import calculoNumeroLetras, mensajeFinal

def test_calculoNumeroLetras():
    nombre = "natalia"
    assert calculoNumeroLetras(nombre) == "NATALIA -> 7"
    
