#Escribe un programa que le pida al usuario una temperatura en grados 
# Celsius, la convierta a grados Fahrenheit e imprima por pantalla la 
# temperatura convertida.

#proceso
def temperatura(celsius:float,valorUno:float,valorDos:float) -> float:
    '''funcion que pide convierte grados Celsius a grados Fahrenheit'''
    return (celsius * valorUno + valorDos)

def mensajeSalida(celsius:float,valorUno:float,valorDos:float) -> float:
    '''funcion que calcula el mensaje'''
    return "La temperatura en grados Fahrenheit es: " + str(temperaturaConvertida)

if __name__ == "__main__":
    #entrada
    celsius = float (input("Escribe la temperatua en grados Celsius: "))  
    valorUno = 1.8
    valorDos = 32
    
    #proceso
    temperaturaConvertida = temperatura(celsius,valorUno,valorDos)
    mensaje = mensajeSalida(celsius,valorUno,valorDos)
    
    #salida
    print (mensaje) 

