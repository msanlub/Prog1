#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla los siguienteS: 
#"la división de n entre m da un cociente c y un resto r", donde n y m son los números introducidos por el usuario, 
#y c y r son el cociente y el resto de la división entera respectivamente.

#proceso
def calculoDivision(numeroUno:int,numeroDos:int) -> int:
    '''funcion que calcula la división entre los numeros'''
    return (numeroUno/ numeroDos)

def calculoCociente(numeroUno:int,numeroDos:int) -> int:
    '''funcion que calcula el cociente de la division entre los numeros'''
    return (numeroUno// numeroDos)

def calculoResto(numeroUno:int,numeroDos:int) -> int:
    '''funcion que calcula el resto de la division de los numeros'''
    return (numeroUno % numeroDos)

def mensajeSalida (numeroUno:int,numeroDos:int, division:float,cociente:float, resto:int) -> int:
    '''funcion que da el mensaje final'''
    return "La división entre " + str(numeroUno) + " y " + str(numeroDos) + " es: " + str(division) + ". El cociente es: " + str(cociente) + " y el resto: " + str(resto)

if __name__=="__main__":
    #entrada
    numeroUno = int (input ("Escribe un numero: "))
    numeroDos = int (input ("Escribe otro numero: "))

    #procedimiento
    division = calculoDivision(numeroUno,numeroDos)
    cociente = calculoCociente(numeroUno,numeroDos)
    resto = calculoResto(numeroUno,numeroDos)
    mensaje = mensajeSalida(numeroUno,numeroDos,division,cociente,resto)

    #salida
    print (mensaje)
