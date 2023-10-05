from ejercicios.ejercicio1 import leeNombre
from ejercicios.ejercicio2 import costeHora
from ejercicios.ejercicio3 import operacion
from ejercicios.ejercicio4 import temperatura
from ejercicios.ejercicio5 import preciofinal
from ejercicios.ejercicio6 import preciosinIVA
from ejercicios.ejercicio6 import totalIVA
from ejercicios.ejercicio7 import suma

from ejercicios.ejercicio11 import sumaN


#test ejercicio 1
def test_leeNombre():
    nombre = "Marta"
    assert leeNombre(nombre) == "Marta"

#test ejercicio 2
def test_costeHora():
    hora = 4
    precio = 6
    assert costeHora(hora , precio) == 24

#test ejercicio 3
def test_operacion():
    ancho = 17
    alto = 12.0
    assert operacion(ancho,alto) == "\t8.5 \n\t8 \n\t4.0 \n\t11\n"

#test ejercicio 4
def test_temperatura():
    celsius = 4
    assert temperatura(celsius * 1.8 + 32) == 102.56

#test ejercicio 5
def test_preciofinal():
    precio = 5
    IVA = 1.10
    assert preciofinal(precio,IVA) == 5.5

#test ejercicio 6
def test_preciosinIVA():
    precio = 4
    IVA = 1.1
    assert preciosinIVA(precio,IVA) == 3.6363636363636362

def test_totalIVA():
    precio = 4
    assert totalIVA(precio * (10/100)) == 0.4

#test ejercicio 7
def test_suma():
    numeroUno = 1
    numeroDos = 2
    numeroTres = 3
    assert suma(numeroUno,numeroDos,numeroTres) == 6




#test ejercicio 11
def test_sumaN():
    n = 2
    assert sumaN(n) == 3