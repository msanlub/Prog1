#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y
#la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y
#muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g.
#Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

#entrada
payasos = int (input("Indica cuantos payasos quieres enviar: "))
muñecas = int (input("Indica cuantas muñecas vas a enviar: "))

#procedimiento
def pesoTotal() -> (int):
    return ((payasos*112) + (muñecas*75))

#salida
print ("El peso de tu paquete es de: " + str(pesoTotal()) + " gramos.")
