datos = int(raw_input())
respuesta = []
for raiz in range(datos):
    valores = map(int, raw_input().split())
    a, b, c = int(valores[0]), int(valores[1]), int(valores[2])
    total = ((a * b) + c)
    total = list(str(total))
    suma = 0
    for resultado in total:
        suma += int(resultado)
    respuesta.append(str(suma))
print(' '.join(respuesta))
