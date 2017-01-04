datos = [11, 9, 1, 14, 90, 232, 111, 15, 111]
cantidad = len(datos)
z = 0
respuesta = []
while z < cantidad:
	a, b, c = int(datos[z]), int(datos[z + 1]), int(datos[z + 2])
	valor = ((a * b) + c)
	valor = list(str(valor))
	suma = 0
	for resultado in valor:
		suma += int(resultado)
	respuesta.append(str(suma))
	print(' '.join(respuesta))
	z += 3
