datos = int(raw_input())
respuesta = []
for redondeo in range(datos):
    valores = map(int, raw_input().split())
    a, b = valores[0], valores[1]
    res = (str(int(round(float("%.02f" % (float(a) / float(b)))))))
    respuesta.append(res)
print (' '.join(respuesta))
