#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla los siguienteS: 
#"la división de n entre m da un cociente c y un resto r", donde n y m son los números introducidos por el usuario, 
#y c y r son el cociente y el resto de la división entera respectivamente.

#procedimiento
def division(numeroUno,numeroDos) -> (int):
    '''funcion que calcula la división entre los numeros'''
    return (numeroUno / numeroDos)
def cociente(numeroUno,numeroDos) -> (int):
    '''funcion que calcula el cociente de la division entre los numeros'''
    return (numeroUno // numeroDos)
def resto(numeroUno,numeroDos) -> (int):
    '''funcion que calcula el resto de la division de los numeros'''
    return (numeroUno % numeroDos)

if __name__=="__main__":
    #entrada
    numeroUno = int (input ("Escribe un numero: "))
    numeroDos = int (input ("Escribe otro numero: "))
    #salida
    print ("La división entre " + str(numeroUno) + " y " + str(numeroDos) + " es: " + str(division(numeroUno,numeroDos)) + ". El cociente es: " + str(cociente(numeroUno,numeroDos)) + " y el resto: " + str(resto(numeroUno,numeroDos)))