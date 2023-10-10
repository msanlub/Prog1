#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero
#e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

def nombreVeces(nombre:str,numero:int) ->str:
    '''función que repite el nombre tantas veces como el número'''
    return nombre * numero

def mensajeFinal(repetir) -> str:
    '''función que da el mensaje de salida'''
    return str(repetir)

if __name__ == "__main__":
    #entrada
    nombre = str (input("Escribe tu nombre: ") + "\n")
    numero = int (input("Escribe el número que quieres que se repita: "))
    
    #procedimiento
    repetir = nombreVeces(nombre,numero)
    mensaje = mensajeFinal(repetir)

    #salida
    print (mensaje)