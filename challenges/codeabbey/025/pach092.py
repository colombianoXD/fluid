datos = int(input())
for lineal in range(datos):
    valores = raw_input().split()
    a, c, m, x, n = int(valores[0]), int(valores[1]), int(valores[2]), int(valores[3]), int(valores[4])
    for resultado in range(n):
        x = (a * x + c) % m
    print x, ''
