datos = [150, 0, 5, 1, 10, 3]
cantidad = len(datos)
z = 0
respuesta = []
while z < cantidad:
	a , b = int(datos[z]), int(datos[z + 1])
	r = 1.00
	for ecuaciones in range(b):
		d = a / r
		abs(r - d)
		r = (r + d)/2
	respuesta.append(str(r))
	print(' '.join(respuesta))
	z += 2
