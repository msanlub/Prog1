#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y
#muestre por pantalla el número de euros y el número de céntimos del precio introducido.

def numeroEuros(precio:str) -> str:
    '''función que da los euros'''
    return precio[:precio.find(".")]

def numeroCentimos(precio:str) -> str:
    '''función que da los centimos'''
    return precio[precio.find(".")+1:]

def mensajeSalida(numeroEuros:str,numeroCentimos:str) -> str:
    '''función que da el mensaje de salida'''
    return "El precio del producto es " + str(numeroEuros) + " euros " + str(numeroCentimos) + " centimos."

if __name__=="__main__":
    #entrada
    precio = str(input("Escribe el precio del producto con decimales: "))

    #procedimiento
    euros = numeroEuros(precio)
    centimos = numeroCentimos(precio)
    mensaje = mensajeSalida(euros,centimos)

    #salida
    print (mensaje)