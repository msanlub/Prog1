from src.ejercicio26 import listaSeparada, mensajeSalida

def test_listaSeparada():
    cesta = "pan,picos,salmorejo"
    assert listaSeparada(cesta) == "pan\n\tpicos\n\tsalmorejo"

def test_mensajeSalida():
    lista = "pan"
    assert mensajeSalida(lista) == "Tu cesta de la compra es: \n\t" + str(lista)