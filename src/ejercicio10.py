#Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética

#procedimiento
def operacion() -> int:
    '''función que calcula la operación'''
    return (((3 + 2) / (2 * 5)) ** 2)

def mensajeSalida(calculoFinal) -> int:
    '''función que da el mensaje final'''
    return "El resultado es: " + str(calculoFinal)

if __name__=="__main__":
    #entrada
    #no hay mensaje de entrada

    #procedimiento
    calculoFinal = operacion
    mensaje = mensajeSalida(calculoFinal)

    #salida
    print (mensaje)
