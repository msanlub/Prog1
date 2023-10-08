from src.ejercicio23 import calculoCorreoCeu, mensajeSalida

def test_calculoCorreoCeu():
    correo = "masanlu@gmail.com "
    assert calculoCorreoCeu(correo) == "masanlu@ceu.es"
    
def test_mensajeSalida():
    correoCeu = "masanlu@ceu.es"
    assert mensajeSalida(correoCeu) == correoCeu
    