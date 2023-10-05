#¿Es posible escribir el programa del ejercicio 7 sin usar variables? Inténtalo.

#procedimiento
def sumaSinVariables(numeroUno,numeroDos,numeroTres) ->(int):
    return numeroUno + numeroDos + numeroTres

if __name__=="__main__":
    #entrada y procedimiento: no se puede definir variables, por lo que he puesto todo en la salida.
    
    #salida
    print ("El resultado es: " + str(sumaSinVariables(int(input("Escribe primer numero: ")) , int(input("Escribe segundo numero: ")) , int(input("Escribe tercer numero: ")))))