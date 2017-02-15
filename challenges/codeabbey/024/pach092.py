"""This script contains number of iterations for
sequences with such initial values to come to the loop."""
CANTIDAD = int(input())
DATOS = map(int, raw_input().split())
RESPUESTA = ''
for numero in DATOS:
    loop = []
    iteraciones = 0
    while numero not in loop:
        loop.append(numero)
        numero = ((numero ** 2) / 100) % 10000
        iteraciones += 1
    RESPUESTA += str(iteraciones) + ' '
print RESPUESTA
