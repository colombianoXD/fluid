contador = int(raw_input())
respuesta = []
for operaciones in range(contador):
    valores = map(int, raw_input().split())
    a, c, m, x0, n = int(valores[0]), int(valores[1]), int(valores[2]), int(valores[3]), int(valores[4])
    x_pruebas = x0
    for x in range (n):
        x_siguiente = (a * x_pruebas + c) %m
        x_pruebas = x_siguiente
    respuesta.append(str(x_pruebas))
print(' '.join(respuesta))
