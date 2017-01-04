datos = [5, 2, 3, 3, 0, 10]
cantidad = len(datos)
a = 0
respuesta = []
while a < cantidad:
	x , y, z = int(datos[a]), int(datos[a + 1]), int(datos[a + 2])
	total = 0
	for b in range(z):
		total = (x + (y * b)) + total
	respuesta.append(str(total))
	print (' '.join(respuesta))
	a += 3
