datos = int(raw_input())
respuesta = []
for progresion in range(datos):
    valores = map(int, raw_input().split())
    x, y, z = int(valores[0]), int(valores[1]), int(valores[2])
    total = 0
    for b in range(z):
        total = (x + (y * b)) + total
    respuesta.append(str(total))
print (' '.join(respuesta))
