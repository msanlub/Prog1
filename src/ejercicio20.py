#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension 
#donde el prefijo es el código del país +34, y la extensión tiene dos dígitos
#(por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de
#teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo ni la extensión.

#procedimiento
def numeroTelefono(numero) -> (int):
    '''Función que define el numero según el el formato'''
    while numero[0] == "+" and numero[1:2].isdigit() and numero[3] == "-" and numero [-2:-1].isdigit() and numero[-3] == "-" and numero [4:-4].isdigit():
        return numero[4:-3] 

if __name__=="__main__":
    #entrada
    numero = str(input("Escribe el número de teléfono con prefijo y extension: ")) 
    #salida
    print(numeroTelefono(numero))
