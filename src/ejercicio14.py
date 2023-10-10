#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y
#la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y
#muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g.
#Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

def pesoTotal(payasos:int, muñecas:int) -> int:
    '''funcion que calcula peso de payasos y muñecas'''
    return ((payasos*112) + (muñecas*75))

def mensajeSalida(peso) -> int:
    '''funcion que da el mensaje final'''
    return "El peso de tu paquete es de: " + str(peso) + " gramos."

if __name__=="__main__":
    #entrada
    payasos = int (input("Indica cuantos payasos quieres enviar: "))
    muñecas = int (input("Indica cuantas muñecas vas a enviar: "))

    #procedimiento
    peso = pesoTotal(payasos,muñecas)
    mensaje = mensajeSalida(payasos,muñecas)

    #salida
    print (mensaje)
