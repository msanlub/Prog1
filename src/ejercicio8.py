#Escribir el programa del ejercicio 7 usando solamente dos variables diferentes.

#proceso
def sumaDosVariables (numeroUno:int,numeroDos:int) -> int:
    '''Función que calcula la suma de las dos variables'''
    return (numeroUno + numeroDos)

def mensajeSalida(numeroUno:int,numeroDos:int) -> int:
    '''funcion que calcula el mensaje'''
    return "La suma de los tres números es: " + str(sumaDosVariables(numeroUno,numeroDos))


if __name__ == "__main__":
    #entrada
    numeroUno = int (input ("Escribe el primer número: ")) + int(input ("Escribe un segundo numero: "))
    numeroDos = int (input ("Escribe el tercer número: "))
    
    #procesamiento
    suma = sumaDosVariables(numeroUno,numeroDos)
    mensaje = mensajeSalida(numeroUno,numeroDos)
    
    #salida
    print (mensaje)
