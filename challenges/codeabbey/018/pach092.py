datos = int(raw_input())
for raiz in range(datos):
    valores = raw_input().split()
    a, b = int(valores[0]), int(valores[1])
    r = float(1)
    for ecuaciones in range(b):
        d = a / r
        r = (r + d)/2
    print r, ''
