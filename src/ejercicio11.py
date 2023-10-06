#Escribir un programa que lea un entero positivo, n, introducido por 
#el usuario y después muestre en pantalla la suma de todos los enteros 
#desde 1 hasta n. La suma de los n primeros enteros positivos puede ser
# calculada de la siguiente forma:

#proceso
def sumaN(n) -> (int):
    '''funcion que da la suma de un numero entero introducido por el usuario'''
    return (n * (n + 1) / 2)


if __name__ == "__main__":
    #entrada
    n = int (input("Escribe el número: "))
    
    #procedimiento
    while n < 0:
        print ("El número tiene que ser positivo.")
        n = int (input("Escribe el número: "))
        
    #salida
    else:
        print ("La suma de los primeros números enteros desde 1 hasta " + str(n) + " es " + str(sumaN(n)))