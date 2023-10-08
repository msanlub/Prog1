from src.ejercicio22 import calculoFraseVocal, mensajeFinal

def test_calculoFraseVocal():
    frase = "hola amigui"
    vocal = "a"
    assert calculoFraseVocal(frase,vocal) == "holA Amigui"
    
def test_mensajeFinal():
    fraseVocal = "holA Amigui"
    assert mensajeFinal(fraseVocal) == fraseVocal