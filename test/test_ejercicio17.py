from src.ejercicio17 import nombreVeces,mensajeFinal

def test_nombreVeces():
    nombre = "cesar"
    numero = 2
    assert nombreVeces(nombre,numero) == nombre * numero
    
def test_mensajeFinal():
    repetir = "cesar \n cesar"
    assert mensajeFinal(repetir) == repetir