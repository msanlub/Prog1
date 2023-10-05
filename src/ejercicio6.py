#Escribe un programa que pida el importe final de un artículo 
# y calcule e imprima por pantalla el IVA que se ha pagado y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%).

#proceso
def preciosinIVA(precio:float , IVA:float) -> float:
    '''funcion que calcula el precio final sin IVA'''
    return (precio / IVA)

def totalIVA(precio) -> (float):
    '''Funcion que calcula el precio del IVA segun el articulo'''
    return (precio * 10 / 100)

def mensajeSalida(precio:float,IVA:float) -> float:
    '''funcion que calcula el mensaje'''
    return "El IVA aplicado es del 10%, por lo que se paga en este articulo un total de " + str(totalIVA(precio)) + " euros de IVA.El precio sin IVA es: " + str(preciosinIVA(precio,IVA)) + " euros."

if __name__ == "__main__":
    #entrada
    precio = float (input("Escribe el precio total del artículo: ")) 
    IVA  = 1.1 #IVA 10%
    
    #procesamiento
    precioBruto = preciosinIVA(precio,IVA)
    iva = totalIVA(precio)
    mensaje = mensajeSalida(precio,IVA)
    
    #salida
    print(mensaje) 
