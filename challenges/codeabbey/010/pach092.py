datos = int(raw_input())
for funcion in range(datos):
    valores = map(int, raw_input().split())
    a, b, c, d = int(valores[0]), int(valores[1]), int(valores[2]), int(valores[3])
    pendiente = (d - b) / (c - a)
    m = int(pendiente)
    intercepcion = (b - m * a)
    g = int(intercepcion)
    print "(" + str(m), str(g) + ") "
