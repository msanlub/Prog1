#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
#calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase 
#Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales.

def imc(peso:float,estatura:float) -> float:
    '''funcion que calcula el indice de masa corporal'''
    return round((peso / estatura)**2,2)

def mensajeSalida (calculoImc) -> float:
    '''funcion que da el mensaje final'''
    return "Tu índice de masa corporal es: " + str(calculoImc)

if __name__=="__main__":
    #entrada
    peso = float(input("Escribe tu peso en kg: "))
    estatura = float(input("Ahora escribe tu estatura en metros: "))

    #procedimiento 
    calculoImc = imc(peso,estatura)
    mensaje = mensajeSalida(calculoImc)

    #salida
    print (mensaje)