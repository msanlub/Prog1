#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero
#e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

def repetir(nombre,numero):
    '''función que repite el nombre tantas veces como el número'''
    return (nombre * numero)

if __name__ == "__main__":
    nombre = str (input("Escribe tu nombre: ") + "\n")
    numero = int (input("Escribe el número que quieres que se repita: "))
    #salida
    print (repetir(nombre,numero))