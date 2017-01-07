datos = raw_input().split()
cantidad = len(datos)
a = 0
p, i, m = int(datos[0]), (int(datos[1]) / 100.0) / 12, int(datos[2])
mensualidad = p*(i*(1+i)**m)/((1+i)**m-1)
print(round(mensualidad))
