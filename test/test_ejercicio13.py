import pytest
from src.ejercicio13 import calculoCociente,calculoDivision,calculoResto,mensajeSalida

@pytest.mark.parametrize(
    "input1,input2,salida", [
        (4,5,0),(15,3,5)

    ]
)
def test_calculoCociente(input1,input2,salida): 
    assert calculoCociente(input1,input2)==salida