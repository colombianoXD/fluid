"""This script contains names of stocks which
are volatile enough by Paul's criteria"""
CANTIDAD = int(input())
for a in range(CANTIDAD):
    valor = raw_input().split()
    nombre_valor = valor[0]
    del valor[0]
    valor = [int(precio) for precio in valor]
    promedio_valor = sum(valor) / len(valor)
    desviacion = 0
    for precio in valor:
        desviacion += (precio - promedio_valor)**2
    desviacion = (desviacion/len(valor))**0.5
    if desviacion >= 4*promedio_valor/100:
        print nombre_valor, ' '
