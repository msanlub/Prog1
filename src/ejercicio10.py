#Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética

#procedimiento
def operacion(calculo:int) -> int:
    '''función que calcula la operación'''
    return calculo
def mensajeSalida(calculo) -> int:
    '''función que da el mensaje final'''
    return "El resultado es: " + str(operacion(calculo))

if __name__=="__main__":
    #entrada
    #no hay mensaje de entrada

    #procedimiento
    calculo = (((3 + 2) / (2 * 5)) ** 2)
    mensaje = mensajeSalida(calculo)

    #salida
    print (mensaje)
