#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades
#y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con
#6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

def calculoNombre(nombre:str,unidad:int,precio:float,total:float) -> str:
    '''función que da el nombre del producto''' 
    return {nombre}: {unidad:2d} unidad x {precio:9.2f}€ = {total:11.2f}€.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio)


if __name__=="__main__":
    #entrada
    nombre = str(input("Escribe el nombre del producto: "))
    unidad = int(input("Escribe las unidades: "))
    precio = float(input("Escribe el precio del producto: "))

    #procedimiento
    
    #salida
