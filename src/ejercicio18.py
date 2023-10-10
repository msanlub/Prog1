#Escribir un programa que pregunte el nombre completo del usuario en la consola y
#después muestre por pantalla el nombre completo del usuario tres veces, una con
#todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con
#la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir
#su nombre combinando mayúsculas y minúsculas como quiera.

#procedimiento
def calculoMinuscula(nombre:str) -> str:
    '''Función que pone el nombre en minúsculas'''
    return "\n\t" +(nombre.lower()) + "\n\t"

def calculoMayuscula(nombre:str) -> str:
    '''Función que pone el nombre en mayúsculas'''
    return (nombre.upper()) + "\n\t"

def calculoPrimeraLetra(nombre:str) -> str:
    '''Función que coge las primera letra de nombre y apellidos y las pone en mayúscula'''
    return (nombre.title() + "\n\t")

def mensajeSalida(minuscula,mayuscula,primeraLetra) -> str:
    '''función que da el mensaje de salida'''
    return str(minuscula) + str(mayuscula) + str(primeraLetra)

if __name__=="__main__":
    #entrada
    nombre = str (input("Escribe tu nombre y apellidos: "))

    #procedimiento
    minuscula = calculoMinuscula(nombre)
    mayuscula = calculoMayuscula(nombre)
    primeraLetra = calculoPrimeraLetra(nombre)
    mensaje = mensajeSalida (nombre)

    #salida
    print (mensaje)