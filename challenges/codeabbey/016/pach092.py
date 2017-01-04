datos = int(raw_input())
for linea in range(datos):
    numeros = map(int, raw_input().split())[:-1]
    promedio = round(sum(numeros) / float(len(numeros)))
    print int(promedio),''
