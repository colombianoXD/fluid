datos = [3, 4, 5, 1, 2, 4]
cantidad = len(datos)
a = 0
respuesta = []
while a < cantidad:
	[x , y, z] = int(datos[a]), int(datos[a + 1]), int(datos[a + 2])
	if (x + y) > z:
		respuesta.append(str('1'))
	else:
		respuesta.append(str('0'))
	print (' '.join(respuesta))
	a += 3
