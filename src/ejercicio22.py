#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, 
#y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

def calculoFraseVocal (frase:str,vocal:str) -> str:
    '''función que calcula la frase con la vocal'''
    return frase.replace(vocal,vocal.upper())

def mensajeFinal (fraseVocal) -> str:
    '''función que da el mensaje de salida'''
    return str(fraseVocal)

if __name__=="__main__":
    #entrada
    frase = str(input("Escribe una frase: "))
    vocal = str(input("Escribe una vocal: "))

    #procedimiento
    fraseVocal = calculoFraseVocal(frase,vocal)
    mensaje = mensajeFinal(frase,vocal)

    #salida
    print(mensaje)