#Escribir un programa que pregunte por consola por los productos de una cesta de la compra,
#separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

def listaSeparada(cesta:str) -> str:
    '''función que define la lista de la compra separada'''
    return cesta.replace(',', '\n\t')

def mensajeSalida(lista:str) -> str:
    '''función que devuelve el mensaje de salida'''
    return "Tu cesta de la compra es: \n\t" + str(lista)

if __name__=="__main__":
    #entrada
    cesta = str(input("Escribe tu cesta de la compra: "))

    #procedimiento
    lista = listaSeparada(cesta)
    mensaje = mensajeSalida(lista)

    #salida
    print (mensaje)