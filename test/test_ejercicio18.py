from src.ejercicio18 import calculoMinuscula,calculoMayuscula,calculoPrimeraLetra,mensajeSalida

nombre = "marta sanchez lubian"

def test_calculoMinuscula():
    assert calculoMinuscula(nombre) == "\n\tmarta sanchez lubian\n\t"
    
def test_calculoMayuscula():
    assert calculoMayuscula(nombre) == "MARTA SANCHEZ LUBIAN\n\t"
    
def test_calculoPrimeraLetra():
    assert calculoPrimeraLetra(nombre) == "Marta Sanchez Lubian\n\t"
    
def test_mensajeSalida():
    minuscula = "marta sanchez lubian"
    mayuscula = "MARTA SANCHEZ LUBIAN"
    primeraLetra = "Marta Sanchez Lubian"
    assert mensajeSalida(minuscula,mayuscula,primeraLetra) == str(minuscula) + str(mayuscula) + str(primeraLetra)
