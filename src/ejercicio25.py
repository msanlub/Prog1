#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa
#y muestra por pantalla, el día, el mes y el año/ Adaptar el programa anterior para que también
#funcione cuando el día o el mes se introduzcan con un solo carácter/

def fechaDia(fecha:str) -> str:
    '''funcion que calcula el dia'''
    return fecha.split("/")[0]

def fechaMes(fecha:str) -> str:
    '''funcion que calcula el mes'''
    return fecha.split("/")[1]

def fechaAño(fecha:str) -> str:
    '''funcion que calcula el año'''
    return fecha.split("/")[2]

def mensajeSalida(dia,mes,año) -> str:
    '''función que da el mensaje de salida'''
    return "El dia es: " + str(dia) + ", el mes es: " + str(mes) + ", del año: " + str(año) + "."

if __name__=="__main__":
    #entrada
    fecha = str(input("Escribe la fecha de tu nacimiento en formato dd/mm/aaaa: "))

    #procedimiento
    dia = fechaDia(fecha)
    mes = fechaMes(fecha)
    año = fechaAño(fecha)
    mensaje = mensajeSalida (dia,mes,año)

    #salida
    print(mensaje)