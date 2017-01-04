datos = int(raw_input())
respuesta = []
for minimo in range(datos):
    valores = map(int, raw_input().split())
    a, b, c = valores[0], valores[1], valores[2]
    res = min(int(a), int(b), int(c))
    respuesta.append(str(res))
print (' '.join(respuesta))
