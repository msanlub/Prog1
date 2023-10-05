#Escribe un programa que solicite tres números al usuario y calcule e imprima por pantalla su suma.

#proceso
def suma(numeroUno:int,numeroDos:int,numeroTres:int) -> (int):
    '''funcion de la suma de los tres numeros dados por el usuario'''
    return (numeroUno + numeroDos + numeroTres)

def mensajeSalida(numeroUno:int,numeroDos:int,numeroTres:int) -> (int):
    '''funcion que calcula el mensaje'''
    return "La suma de los tres números es: " + str(suma(numeroUno,numeroDos,numeroTres))

if __name__ == "__main__":
    #entrada
    numeroUno = int(input ("Escribe el primer número: "))
    numeroDos = int(input ("Escribe el segundo número: "))
    numeroTres = int(input ("Escribe el tercer número: "))
    
    #procesamiento
    sumaTotal = suma(numeroUno,numeroDos,numeroTres)
    mensaje = mensajeSalida(numeroUno,numeroDos,numeroTres)
    
    #salida
    print(mensaje)