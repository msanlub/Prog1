#Escribir un programa que pregunte el correo electrónico del usuario en la consola y
#muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

def calculoCorreoCeu(correo:str) -> str:
    '''función que calcula el correo y lo transforma a ceu.es'''
    return correo.split("@")[0] + "@ceu.es" 

def mensajeSalida(correo:str) -> str:
    '''función que calcula el mensaje de salida'''
    return calculoCorreoCeu(correo)

if __name__=="__main__":
    #entrada
    correo = str(input("Escribe tu correo electrónico: "))

    #procedimiento
    correoCeu = calculoCorreoCeu(correo)
    mensaje = mensajeSalida(correo)

    #salida
    print (mensaje)