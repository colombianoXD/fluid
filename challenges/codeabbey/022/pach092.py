datos = int(raw_input())
respuesta = []
for hojas in range(datos):
    valores = map(int, raw_input().split())
    x, y, n = int(valores[0]), int(valores[1]), int(valores[2])
    impresora_1 = (y * n / (x + y))
    impresora_2 = (x * n / (x + y))
    respuesta1 = int(max((impresora_1 + 1) * x, impresora_2 * y))
    respuesta2 = int(max(impresora_1 * x, (impresora_2 + 1) * y))
    respuesta.append(str(min(respuesta1, respuesta2)))
print(' '.join(respuesta))
