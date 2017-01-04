import math
datos = [9, 15, 1776]
suma = ""
for a in datos:
    digito = []
    s = 0
    sumatoria = 0
    while a >= 1:
        digito.append(int(math.fmod(a,10)))
        a = math.trunc(a/10)
        s += 1
    s = 0
    for x in digito:
        sumatoria += x * (len(digito) - s)
        s += 1
    suma += str(sumatoria) + ' '
print (suma)
