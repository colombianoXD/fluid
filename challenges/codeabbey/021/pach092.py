rango = raw_input()
rango, numeros = rango.split()
numeros = int(numeros)
contador = [0] * numeros
numerador = raw_input()
numerador = numerador.split()
for j in numerador:
    j = int(j)
    contador[j - 1] += 1
print " ".join(str(respuesta) for respuesta in contador)
