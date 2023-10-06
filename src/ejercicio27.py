#Escribir un programa que pregunte el nombre el un    nombre, su precio y un número de unidades
#y muestre por pantalla una cadena con el nombre del    nombre seguido de su precio unitario con
#6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

def calculoTotal(nombre:str,precio:float,unidad:int) -> str:
    '''función que define el total del ejercicio'''
    total = float(precio*unidad)
    return f'{nombre} -> {unidad:3d} unidades x{precio:9.2f}€ ={total:11.2f}€'
        #unidad:3d -> soporta 3 digitos de unidades(ej: 300)
        #precio:9.2f -> 9 caracteres(contando con los decimales y la coma) y el 2 el numero de decimales. La f es de float.
        #total:11.2f -> 11 caracteres (contando con los decimales y la coma) y el 2 de numero de decimales. La f es de float.

def mensajeSalida(totalProducto:str) -> str:
    '''función que da el mensaje de salida'''
    return "\t" + str(totalProducto)

if __name__=="__main__":
    #entrada
    nombre = str(input('Introduce el nombre del producto: '))
    unidad = int(input('Introduce el número de unidades: '))
    precio = float(input('Introduce el precio por unidad: '))
  
    #procedimiento
    totalProducto = calculoTotal(nombre,precio,unidad)
    mensaje = mensajeSalida(totalProducto)
    
    #salida
    print(mensaje)