#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario
#lo introduzca muestre por pantalla "NOMBRE tiene n letras.", donde NOMBRE es el nombre de usuario
#en mayúsculas y n es el número de letras que tienen el nombre.

#procedimiento
def numeroLetras(nombre) -> (str):
    '''Función que da el numero de letras que tiene el nombre'''
    return (nombre.upper() + " -> " + str(len(nombre)))

if __name__=="__main__":
    #entrada
    nombre = str(input("Escribe tu nombre: " + "\n"))
    #salida
    print (str(numeroLetras(nombre)))