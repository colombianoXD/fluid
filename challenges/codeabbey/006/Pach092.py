numeros = [12,8,11,-3,400,5]
cantidad = len(numeros)
a = 0
res=0
respuesta = []
while a < cantidad:
	res = (str(int(round(float("%.02f" % (float(numeros[a]) / float(numeros[a+1])))))))
	respuesta.append(res)
	a += 2
print (' '.join(respuesta))
