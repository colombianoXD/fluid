datos = int(raw_input())
for minimo in range(datos):
    valores = raw_input().split()
    a, b = int(valores[0]), int(valores[1])
    res = min(a, b)
    print res,''
