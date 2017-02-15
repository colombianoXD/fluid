"""This script contains number of years to
wait for each case, separated by spaces."""
CANTIDAD = int(raw_input())
RESPUESTA = ''
for a in range(CANTIDAD):
    datos = raw_input().split()
    s, r, p = datos[0], datos[1], datos[2]
    total = round(float(s), 2)
    contador = 0
    while total < round(float(r), 2):
        total = round((total * (1 + (float(p) / 100))), 2)
        contador += 1
    RESPUESTA = RESPUESTA + '%d ' % contador
print RESPUESTA
