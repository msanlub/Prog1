#Ejercicio 2.1: Escribe un programa que pida el nombre del usuario para luego darle la bienvenida.


#proceso
def calculaNombre(nombre: str) -> (str):
    '''Funcion que lee un string y da el nombre de usuario'''
    return (nombre)

def mensajeSalida(nombre: str) -> (str):
    '''Función que calcula el mensaje de salida'''
    return ("Bienvenido/a " + calculaNombre(nombre))

if __name__ == "__main__":
    #entrada
    nombre = str(input("Escribe tu nombre: "))  
    
    #procesamiento
    leeNombre = calculaNombre(nombre)
    mensaje = mensajeSalida(leeNombre)
    
    #salida
    print (mensaje)
    










