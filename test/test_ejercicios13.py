from src.ejercicio13 import calculoDivision,calculoCociente,calculoResto,mensajeSalida

def test_calculoDivision():
    numeroUno = 10 
    numeroDos = 5
    assert calculoDivision(numeroUno,numeroDos) == 2
    
def test_calculoCociente():
    numeroUno = 10
    numeroDos = 5
    assert calculoCociente(numeroUno,numeroDos) == 2
    
def test_calculoResto():
    numeroUno = 10
    numeroDos = 5
    assert calculoResto(numeroUno,numeroDos) == 0
    
def test_mensajeSalida():
    numeroUno = 10
    numeroDos = 5
    division = 2
    cociente = 2
    resto = 0
    
    assert mensajeSalida(numeroUno,numeroDos, division,cociente, resto) == "La división entre " + str(numeroUno) + " y " + str(numeroDos) + " es: " + str(division) + ". El cociente es: " + str(cociente) + " y el resto: " + str(resto) 