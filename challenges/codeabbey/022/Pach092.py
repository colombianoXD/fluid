datos = [1, 1, 5, 3, 5, 4]
cantidad = len(datos)
respuesta = []
a = 0
while a < cantidad:
    x, y, n = int(datos[a]), int(datos[a + 1]), int(datos[a + 2])
    impresora_1 = (y * n / (x + y))
    impresora_2 = (x * n / (x + y))
    respuesta1 = int(max((impresora_1 + 1) * x, impresora_2 * y))
    respuesta2 = int(max(impresora_1 * x, (impresora_2 + 1) * y))
    respuesta.append(str(min(respuesta1, respuesta2)))
    a += 3
    print(' '.join(respuesta))
