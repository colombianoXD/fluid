datos = raw_input()
numeros = list(map(int, datos.split()))
a = numeros[:-1]
numerodatos = len(a)
pasa = 0
for i in range(numerodatos - 1):
    if a[i] > a[i + 1]:
        temporal = a[i + 1]
        a[i + 1] = a[i]
        a[i] = temporal
        pasa += 1
resultado = 0
limite = 10000007
for n in range(numerodatos):
        resultado = (resultado + a[n])* 113
        if resultado > limite:
            resultado = resultado % limite
print pasa, resultado 
