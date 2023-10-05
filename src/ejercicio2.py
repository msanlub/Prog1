#Ejercicio 2.2: Escribe un programa para pedirle al usuario las horas de trabajo 
#y el precio por hora y calcule el importe total del servicio.

#funcion
def costeHora(hora:int, precio:float) -> (float):
    '''Funcion que calcula el importe total del servicio'''
    return (hora * precio)

def mensajeSalida(hora:str , precio:float) -> (str):
    '''Función que calcula el mensaje de salida'''
    return ("El coste total es: " + str(costeHora(hora, precio)))


if __name__ == "__main__":
    #Entrada
    hora = int (input("Escribe numero de horas: "))  
    precio = float (input("Cuanto cuesta la hora: ")) 

    #procesamiento
    precioHora = costeHora(hora,precio)
    mensaje = mensajeSalida(hora,precio)
    
    #Salida
    print (mensaje) 

