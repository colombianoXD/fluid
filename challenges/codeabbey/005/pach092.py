datos = int(raw_input())
for minimo in range(datos):
    valores = raw_input().split()
    a, b, c = int(valores[0]), int(valores[1]), int(valores[2])
    res = min(a, b, c)
    print res, ''
