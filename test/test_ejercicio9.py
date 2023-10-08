from src.ejercicio9 import sumaSinVariables

#ejercicio 9 
def test_sumaSinVariables():
    numeroUno = 1
    numeroDos = 2
    numeroTres = 3
    assert sumaSinVariables(numeroUno,numeroDos,numeroTres) == 6
  
