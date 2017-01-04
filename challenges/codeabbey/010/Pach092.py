datos = [0, 0, 1, 1, 1, 0, 0, 1]
cantidad = len(datos)
z = 0
respuesta = []
while z < cantidad:
	a, b, c, d = int(datos[z]), int(datos[z + 1]), int(datos[z + 2]), int(datos[z + 3])
	pendiente = (d - b) / (c - a)
	m = int(pendiente)
	intercepcion = (b - m * a)
	g = int(intercepcion)
	respuesta.append('({0} {1})'.format(m, g))
	print(' '.join(respuesta))
	z += 4
