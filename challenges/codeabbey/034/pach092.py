'''This script contains solutions values of x which satisfy equation with
given coefficents'''
import math
DATOS = int(raw_input())
RESPUESTA = []
for i in range(0, DATOS):
    d = [float(x) for x in raw_input().split(" ")]
    minimo = 0.0
    maximo = 100.0
    while (maximo - minimo) > pow(10, -7):
        x = (maximo + minimo)/2
        r = d[0] * x + d[1] * pow(x, 1.5) - d[2] * math.exp(-x / 50.0) - d[3]
        if r < 0:
            minimo = x
        if r > 0:
            maximo = x
        if r == 0:
            break
    RESPUESTA.append(str(x))
print ' '.join(RESPUESTA)
