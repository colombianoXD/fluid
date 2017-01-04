datos = int(raw_input())
respuesta = []
for raiz in range(datos):
    valores = map(int, raw_input().split())
    a , b = int(valores[0]), int(valores[1])
    r = 1.00
    for ecuaciones in range(b):
        d = a / r
        abs(r - d)
        r = (r + d)/2
    respuesta.append(str(r))
print(' '.join(respuesta))
