def checksum(list):
    resultado_checksum = 0
    for a in list:
        resultado_checksum += a
        resultado_checksum *= 113
        resultado_checksum = resultado_checksum%10000007
    return resultado_checksum
def cadena(list):
    contador = 0
    for a in range(len(list)-2):
        if list[a] > list[a+1]:
            espera = list[a+1]
            list[a+1] = list[a]
            list[a] = espera
            contador += 1
    print contador, checksum(list[:-1])        
cadena([1, 4, 3, 2, 6, 5, -1])
