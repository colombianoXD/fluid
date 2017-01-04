datos = [3, 7, 12, 1, 2, 2, 3, 15, 8, 10]
contador = len(datos)
z = 0
respuesta = []
while z < contador:
	a, c, m, x0, n = int(datos[z]), int(datos[z + 1]), int(datos[z + 2]), int(datos[z + 3]), int(datos[z + 4])
	x_pruebas = x0
	for x in range (n):
		x_siguiente = (a * x_pruebas + c) %m
		x_pruebas = x_siguiente
	respuesta.append(str(x_pruebas))
	print(' '.join(respuesta))
	z += 5
