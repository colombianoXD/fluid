datos = int(raw_input())
numeros = map(int,raw_input().split())
for a in numeros:
    suma = 0
    for (indice,valor) in enumerate(str(a)):
        suma += (indice + 1) * int(valor)
    print "%d " %suma
