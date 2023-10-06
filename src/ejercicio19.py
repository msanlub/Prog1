#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario
#lo introduzca muestre por pantalla "NOMBRE tiene n letras.", donde NOMBRE es el nombre de usuario
#en mayúsculas y n es el número de letras que tienen el nombre.

#procedimiento
def calculoNumeroLetras(nombre:str) -> str:
    '''Función que da el numero de letras que tiene el nombre'''
    return (nombre.upper() + " -> " + str(len(nombre)))

def mensajeFinal(nombre:str) -> str:
    '''función que da el mensaje de salida'''
    return str(calculoNumeroLetras(nombre))

if __name__=="__main__":
    #entrada
    nombre = str(input("Escribe tu nombre: " + "\n"))

    #procedimiento
    numeroLetras = calculoNumeroLetras(nombre)
    mensaje = mensajeFinal(nombre)

    #salida
    print (mensaje)