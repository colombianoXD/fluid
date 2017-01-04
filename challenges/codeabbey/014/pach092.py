datos = eval(raw_input())
while 1 == 1:    
    cadena = raw_input().split()
    operador = cadena[0]
    numero = int(cadena[1])
    if operador == '%':
        respuesta = datos % numero
        print (respuesta)
        break
    elif operador == '*':
        datos = datos * numero
    else:
        datos = datos + numero
