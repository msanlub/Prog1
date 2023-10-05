#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%.
#Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el
#programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante),
#el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas.

#procedimiento
def total(numeroBarras,barra,descuento) -> (float):
    '''Función que calcula el previo final de todas las barras que no son del día'''
    return (numeroBarras*(barra*descuento))


if __name__ == "__main__":
    #entrada
    numeroBarras = int(input("Escribe la cantidad de barras que has vendido sin ser del día: "))
    barra = 3.49
    descuento = (60/100)
    #salida
    print ("El precio de la barra de pan del día es: " + str(barra) + " euros. Si no es del día se le aplica un descuento del: " + str(descuento) + " euros. El precio total de todas las barras que no son del día es: " + str(total(numeroBarras,barra,descuento)) + " euros.")