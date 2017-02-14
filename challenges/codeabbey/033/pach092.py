"""This script contains message with corrupted bytes removed, highest bits
cleared - and represented as characters rather than numbers."""
DATOS = raw_input().split(" ")
RESPUESTA = []
for a in DATOS:
    binario = '{0:08b}'.format(int(a))
    texto = []
    for b in binario:
        texto.append(int(b))
    es_texto = sum(texto)
    if es_texto % 2 == 0:
        if binario[0] == "1":
            binario = "0" + binario[1:8]
        RESPUESTA.append(chr(int(binario, 2)))
print ''.join(RESPUESTA)
