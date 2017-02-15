"""This script contains a pair of roots for each case.
it's using space to separate values of the pair and
use semicolon followed by space to separate pairs
themselves. Complex numbers are given like 5-2i or -1+1i."""
from math import sqrt
CANTIDAD = input()
RESPUESTA = []
for x in range(CANTIDAD):
    datos = raw_input().split()
    A, B, C = int(datos[0]), int(datos[1]), int(datos[2])
    resultado_raiz = B ** 2 - 4 * A * C
    if resultado_raiz >= 0:
        x1 = int((-B + sqrt(resultado_raiz)) / (2 * A))
        x2 = int((-B - sqrt(resultado_raiz)) / (2 * A))
        RESPUESTA.append("%s %s" % (x1, x2))
    else:
        x1 = -B / (2 * A)
        x2 = int(sqrt(-resultado_raiz) / (2 * A))
        RESPUESTA.append("{0}+{1}i {0}-{1}i".format(x1, x2))
print "; ".join(RESPUESTA)
