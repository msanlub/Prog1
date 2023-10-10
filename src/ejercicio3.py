#Suponiendo que se han ejecutado las siguientes sentencias de asignación:

#ancho = 17
#alto = 12.0

#Para cada una de las expresiones siguientes, intenta adivinar el valor de la expresión 
# y su tipo sin ejecutarlas en el intérprete:
#1. ancho / 2
#2. ancho // 2
#3. alto / 3
#4. 1 + 2 * 5

#proceso
def operacion(ancho:float, alto:float) -> (float):
    '''función que  hace el calculo'''
    return f"\t{ancho / 2} \n\t{ancho // 2} \n\t{alto / 3} \n\t{1 + 2 * 5}\n"

def mensajeSalida(valor) -> float:
    '''funcion que calcula el mensaje'''
    return "El resultado es: \n" + str(valor)

if __name__ == "__main__":
    #entrada
    ancho:float = 17  
    alto:float = 12.0  
   
    #proceso
    valor:float = operacion(ancho, alto)
    mensaje:str = mensajeSalida(ancho, alto)
    
    #salida
    print (mensaje) 
 
