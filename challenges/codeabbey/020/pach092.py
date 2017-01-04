datos = int(raw_input())
vocales = list("aeiouy")
respuesta = []
for pasos in range(datos):
    oraciones = map(str, raw_input().split("\n"))
    frase = oraciones[0].lower()
    contador_vocales = sum(frase.count(v) for v in vocales)
    respuesta.append(str(contador_vocales))
print(' '.join(respuesta))
