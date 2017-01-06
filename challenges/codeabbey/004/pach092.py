datos = int(raw_input())
respuesta = []
for minimo in range(datos):
    valores = raw_input().split()
    a, b = valores[0], valores[1]
    res = min(int(a), int(b))
    respuesta = res
    print respuesta, ''
