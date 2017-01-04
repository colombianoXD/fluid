datos = int(raw_input())
numeros= [int(z) for z in raw_input().split()]
def orden(cadena, pasa, descartado):
    respuesta = str(pasa), str(descartado) 
    arreglado = True
    pasa += 1
    for a in range(len(cadena) - 1):
        x = cadena[a]
        y = cadena[a + 1]
        if x > y:
            arreglado = False
            cadena[a], cadena[a + 1] = cadena[a + 1], cadena[a]
            descartado += 1
    if arreglado is False:
        respuesta = orden(cadena, pasa, descartado)
    return respuesta
print ('%s %s') % orden(numeros, 1, 0)
