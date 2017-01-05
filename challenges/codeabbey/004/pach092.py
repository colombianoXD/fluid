datos = int(raw_input())
respuesta = []
for minimo in range(datos):
    valores = map(int, raw_input().split())
    a, b = valores[0], valores[1]
    res = min(int(a), int(b))
    respuesta.append(str(res))
print (' '.join(respuesta))
