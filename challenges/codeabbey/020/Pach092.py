oraciones = """abracAdabra
pear tree
o a kak ushakov lil vo kashu kakao
my pyx""".split("\n")
contador = len(oraciones)
a = 0
vocales = list("aeiouy")
respuesta = []
while a < contador:
	frase = oraciones[a].lower()
	contador_vocales = sum(frase.count(v) for v in vocales)
	respuesta.append(str(contador_vocales))
	print(' '.join(respuesta))
	a += 1
