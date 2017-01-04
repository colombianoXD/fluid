datos = [800000, 6, 103]
cantidad = len(datos)
a = 0
p = int(datos[0])
i = (int(datos[1]) / 100.0) / 12
m = int(datos[2])
mensualidad = p*(i*(1+i)**m)/((1+i)**m-1)
print(round(mensualidad))
