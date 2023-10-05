#Escribir un programa que pregunte el nombre completo del usuario en la consola y
#después muestre por pantalla el nombre completo del usuario tres veces, una con
#todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con
#la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir
#su nombre combinando mayúsculas y minúsculas como quiera.

#procedimiento
def minuscula(nombre) -> (str):
    '''Función que pone el nombre en minúsculas'''
    return (nombre.lower()) + "\n"

def mayuscula(nombre) -> (str):
    '''Función que pone el nombre en mayúsculas'''
    return (nombre.upper()) + "\n"

def primeraLetra(nombre) -> (str):
    '''Función que coge las 3 primeras letras de nombre y apellidos'''
    return (nombre.title())


if __name__=="__main__":
    #entrada
    nombre = str (input("Escribe tu nombre y apellidos: " + "\n"))
    #salida
    print (str(minuscula(nombre)) + str(mayuscula(nombre)) + str(primeraLetra(nombre)))