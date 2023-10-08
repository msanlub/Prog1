from src.ejercicio21 import calculoInvertida, mensajeFinal

def test_calculoInvertida():
    frase = "hola"
    assert calculoInvertida(frase) == "aloh"
    
def test_mensajeFinal():
    fraseInvertida = "aloh"
    assert mensajeFinal(fraseInvertida) == fraseInvertida