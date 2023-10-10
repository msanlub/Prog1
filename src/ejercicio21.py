#Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

def calculoInvertida(frase:str) -> str:
    '''función que calcula la frase al reves'''
    return frase[::-1]

def mensajeFinal(fraseInvertida) -> str:
    '''función que da el mensaje final'''
    return str(fraseInvertida)

if __name__=="__main__":
    #entrada
    frase = str(input( "Escribe una frase: "))

    #procedimiento
    fraseInvertida = calculoInvertida(frase)
    mensaje = mensajeFinal(frase)

    #salida
    print (mensaje)