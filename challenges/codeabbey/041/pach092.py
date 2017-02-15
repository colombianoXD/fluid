"""This script contains selected medians of triplets, separated by spaces."""
DATOS = int(raw_input())
for minimo in range(DATOS):
    valores = raw_input().split()
    datos = int(valores[0]), int(valores[1]), int(valores[2])
    orden = sorted(datos)
    print orden[1], ''
