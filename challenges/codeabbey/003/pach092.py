datos = int(raw_input())
respuesta = []
for suma in range(datos):
    valores = map(int, raw_input().split())
    a, b = valores[0], valores[1]
    res = a + b
    respuesta.append(str(res))
print (' '.join(respuesta))
