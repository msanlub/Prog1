#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses,
#que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience
#leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular
#y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

#entrada
dinero = float(input("Escribe la cantidad de dinero que tienes: "))
interes = 0.04

#procedimiento
def primerAño() -> (float):
    '''Función que hará el cálculo con el interes del primer año'''
    return round(dinero+ dinero*interes,2)

def segundoAño() -> (float):
    '''Función que hará el cálculo con el interés del segundo año'''
    return round(dinero + dinero*interes*2,2)

def tercerAño() -> (float):
    '''Función que hará el cálculo con el interés del tercer año'''
    return round(dinero + dinero*interes*3,2)

#salida
print ("El total con intereses después del primer año son: " + str(primerAño()) + " euros, el total con intereses del segundo año son: " + str(segundoAño()) + " euros, y el total con intereses después del tercer año son: " + str(tercerAño()) + "euros.")