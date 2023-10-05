#Escribe un programa que pida el importe sin IVA de un artículo 
#y el tipo de IVA a aplicar y calcule e imprima por pantalla 
#el precio final del artículo.


#proceso
def calculaPrecioDelArticulo(precio: float , IVA: float) -> float:
    '''funcion que calcula el precio final con IVA'''
    return (precio * IVA)

def mensajeSalida(precio: float) -> float:
    '''funcion que calcula el mensaje'''
    return "El precio con IVA incluido es: " + str(precioDelArticulo)


if __name__ == "__main__":
    #entrada
    precio = float(input("Escribe el precio del artículo: "))  
    IVA  = float(input("Escribe el IVA a aplicar: ")) 

    #procesamiento
    precioDelArticulo = calculaPrecioDelArticulo(precio , IVA)
    mensaje = mensajeSalida(precioDelArticulo)
    
    #salida
    print (mensaje)
    