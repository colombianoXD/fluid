datos = int(raw_input())
vocales = list("aeiouy")
for pasos in range(datos):
    oraciones = raw_input().split("\n")
    frase = oraciones[0].lower()
    contador_vocales = sum(frase.count(v) for v in vocales)
    print contador_vocales, ''
